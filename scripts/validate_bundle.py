#!/usr/bin/env python3
"""Validate local Skill frontmatter, registry paths, routes, and Markdown links."""

from __future__ import annotations

import argparse
import ast
import re
from pathlib import Path


NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def frontmatter(path: Path, errors: list[str]) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append(f"{path}: missing YAML frontmatter")
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        errors.append(f"{path}: unterminated YAML frontmatter")
        return {}
    values: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" in line and not line.startswith((" ", "\t")):
            key, value = line.split(":", 1)
            values[key.strip()] = value.strip().strip('"\'')
    for key in ("name", "description"):
        if not values.get(key):
            errors.append(f"{path}: missing frontmatter field {key}")
    return values


def markdown_links(path: Path, root: Path, errors: list[str]) -> None:
    for raw in LINK_RE.findall(path.read_text(encoding="utf-8")):
        target = raw.strip().split("#", 1)[0]
        if not target or re.match(r"^[a-z]+://", target) or target.startswith(("mailto:", "/")):
            continue
        target = target.replace("%20", " ")
        resolved = (path.parent / target).resolve()
        try:
            resolved.relative_to(root)
        except ValueError:
            errors.append(f"{path}: link escapes bundle: {raw}")
            continue
        if not resolved.exists():
            errors.append(f"{path}: broken link: {raw}")


def parse_registry(path: Path, root: Path, errors: list[str]) -> tuple[set[str], set[str]]:
    section = ""
    canonical: set[str] = set()
    external: set[str] = set()
    aliases: set[str] = set()
    current_name = ""
    routes: list[tuple[str, str]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line and not line.startswith(" ") and line.endswith(":"):
            section = line[:-1]
            current_name = ""
            continue
        item = re.match(r"^  ([A-Za-z0-9_.-]+):(?:\s.*)?$", line)
        if item and section in {"canonical_skills", "external_skills"}:
            current_name = item.group(1)
            (canonical if section == "canonical_skills" else external).add(current_name)
            continue
        path_match = re.match(r"^    path:\s*(.+)$", line)
        if path_match and section in {"canonical_skills", "standalone_skills"}:
            relative = path_match.group(1).strip().strip('"\'')
            if not (root / relative).is_file():
                errors.append(f"registry missing path for {current_name}: {relative}")
        alias_match = re.match(r"^    aliases:\s*\[(.*)\]$", line)
        if alias_match and section == "canonical_skills":
            for alias in (part.strip() for part in alias_match.group(1).split(",")):
                if alias in aliases or alias in canonical:
                    errors.append(f"duplicate registry alias: {alias}")
                aliases.add(alias)
        route_match = re.match(r'^  "?([G0-9.]+)"?:\s*\[(.*)\]$', line)
        if route_match and section == "stage_routes":
            routes.extend((route_match.group(1), part.strip()) for part in route_match.group(2).split(","))
    for stage, skill in routes:
        if skill not in canonical and skill not in external:
            errors.append(f"stage route {stage} references unknown skill: {skill}")
    return canonical, external


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, nargs="?", default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    errors: list[str] = []

    registry = root / "skills" / "registry.yaml"
    canonical, _ = parse_registry(registry, root, errors)
    required_control_files = (
        "references/skill-coverage-and-rework.md",
        "scripts/set_skill_status.py",
        "scripts/record_rework.py",
        "scripts/close_rework.py",
    )
    for relative in required_control_files:
        if not (root / relative).is_file():
            errors.append(f"missing workflow control file: {relative}")
    registry_text = registry.read_text(encoding="utf-8")
    for section in ("coverage_control:", "rework_control:"):
        if section not in registry_text:
            errors.append(f"registry missing section: {section[:-1]}")

    init_path = root / "scripts" / "init_project.py"
    try:
        tree = ast.parse(init_path.read_text(encoding="utf-8"))
        initialized: set[str] | None = None
        for node in tree.body:
            if isinstance(node, ast.Assign) and any(
                isinstance(target, ast.Name) and target.id == "CANONICAL_SKILLS"
                for target in node.targets
            ):
                initialized = set(ast.literal_eval(node.value))
                break
        if initialized is None:
            errors.append("init_project.py missing CANONICAL_SKILLS")
        elif initialized != canonical:
            errors.append(
                "init_project.py canonical Skill set differs from registry: "
                f"missing={sorted(canonical - initialized)} stale={sorted(initialized - canonical)}"
            )
    except Exception as exc:
        errors.append(f"cannot validate init_project.py Skill set: {exc}")
    skill_files = [root / "SKILL.md", *sorted((root / "skills").glob("*/SKILL.md"))]
    found_names: set[str] = set()
    for path in skill_files:
        values = frontmatter(path, errors)
        name = values.get("name", "")
        if name and not NAME_RE.fullmatch(name):
            errors.append(f"{path}: invalid skill name: {name}")
        if path != root / "SKILL.md" and name != path.parent.name:
            errors.append(f"{path}: frontmatter name does not match folder")
        if name in found_names:
            errors.append(f"duplicate skill name: {name}")
        found_names.add(name)
        markdown_links(path, root, errors)

    local_names = found_names - {"mathskills"}
    missing_registry = local_names - canonical
    missing_folder = canonical - local_names
    for name in sorted(missing_registry):
        errors.append(f"local skill not registered: {name}")
    for name in sorted(missing_folder):
        errors.append(f"registered skill has no matching folder/frontmatter: {name}")

    markdown_links(root / "SKILL.md", root, errors)
    for error in errors:
        print(f"ERROR {error}")
    if errors:
        print(f"FAIL errors={len(errors)} local_skills={len(local_names)}")
        return 1
    print(f"PASS errors=0 local_skills={len(local_names)} registered={len(canonical)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
