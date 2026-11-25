#!/usr/bin/env python3
"""Initialize a mathskills project without overwriting user inputs or state."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


CANONICAL_SKILLS = (
    "problem-forensics",
    "data-analysis",
    "external-data-acquisition",
    "experimental-design-and-inference",
    "model-deliberation",
    "model-formulation-and-solving",
    "mathematical-derivation-and-proof",
    "forecasting-and-backtesting",
    "simulation-and-uncertainty",
    "geospatial-modeling",
    "network-modeling",
    "scientific-visualization",
    "technical-diagrams",
    "scientific-tables",
    "academic-writing",
    "academic-humanization",
    "workflow-orchestration",
    "literature-evidence",
    "systematic-evidence-review",
    "exemplar-distillation",
    "validation-and-robustness",
    "reproducibility-audit",
    "national-award-paper-style",
    "measured-experiment-loop",
    "jupyter-live-analysis",
    "sql-data-analysis",
    "academic-translation",
    "research-presentation",
    "plan-and-execution",
    "competition-scoring",
    "submission-packaging",
    "ai-use-disclosure",
)
STAGE_ORDER = ("G0", "G1", "G1.5", "G2", "G3", "G3.5", "G4", "G5", "G6", "G7")


DEFAULT_SKILL_META = {
    "problem-forensics": ("G1", "题面、附件或规则需要结构化解释", "题目事实、目标、约束和交付矩阵"),
    "data-analysis": ("G1,G3", "任何附件数据需要审计、清洗、探索或统计分析", "数据审计、转换日志和诊断"),
    "external-data-acquisition": ("conditional:G0,G1,G3,G5,G6", "使用公开 API、门户、网页或二手数据", "来源契约、原始快照、字段字典和联结审计"),
    "experimental-design-and-inference": ("conditional:G1,G2,G3,G3.5,G6", "控制数据采集、分配、算法比较或仿真运行", "实验契约、估计目标、分配和分析计划"),
    "model-deliberation": ("G2", "多个建模方案、创新点或关键假设需要比较", "候选矩阵、反例和决策日志"),
    "model-formulation-and-solving": ("G2,G3", "需要建立并求解数学模型", "建模蓝图、公式、求解器契约和诊断"),
    "mathematical-derivation-and-proof": ("conditional:G2,G3,G4,G6", "结论依赖非平凡推导、定理、界、近似或保证", "推导契约、证明义务台账和审计报告"),
    "forecasting-and-backtesting": ("conditional:G1,G2,G3,G3.5,G4,G6", "目标按时间排序或要求预测未来", "预测契约、时间基线和滚动回测"),
    "simulation-and-uncertainty": ("conditional:G2,G3,G3.5,G4,G6", "随机输入、情景、队列、事件或不确定性传播影响结论", "仿真契约、种子、重复和收敛证据"),
    "geospatial-modeling": ("conditional:G1,G2,G3,G3.5,G4,G6", "坐标、区域、路线、栅格、邻接或地理距离影响模型", "CRS、几何审计、空间连接和空间划分"),
    "network-modeling": ("conditional:G1,G2,G3,G3.5,G4,G6", "节点、边、路径、流、社区或扩散影响模型", "图契约、构图元数据、零模型和扰动"),
    "scientific-visualization": ("G4", "需要数据图或审查已有科研图", "图稿契约、图源、数据和 QA"),
    "technical-diagrams": ("G4", "需要路线图、机制图、系统图或算法图", "可编辑图源、语义映射和视觉 QA"),
    "scientific-tables": ("G4", "需要结果、对比、消融、敏感性或最终答案表", "机器可读表格数据、单位、精度和来源"),
    "academic-writing": ("G4,G6", "需要论文、报告、摘要、图注或审稿回复", "论证图、主张台账、论文源和一致性检查"),
    "academic-humanization": ("G6", "技术内容稳定后需要自然度和作者声音审查", "受保护 token 审计和修订报告"),
    "workflow-orchestration": ("G0-G7", "任何多阶段项目", "状态、门、任务契约和故障路由"),
    "literature-evidence": ("G1.5", "使用外部方法、事实、假设或创新性表述", "检索日志、来源护照和引用台账"),
    "systematic-evidence-review": ("conditional:G0,G1,G1.5,G2,G3.5,G4,G6", "用户要求深度研究、系统综述或状态地图", "综述协议、筛选表、矩阵和综合报告"),
    "exemplar-distillation": ("conditional:G1.5", "有优秀论文或获奖论文库可供对标", "来源和可迁移模式表"),
    "validation-and-robustness": ("G3.5,G6", "模型输出将用于推荐、比较或论文结论", "基线、失败测试、敏感性和稳健性报告"),
    "reproducibility-audit": ("G5-G7", "结果、论文或交付包需要复现或发生重大修改", "清洁重跑、manifest、跨文件一致性报告"),
    "national-award-paper-style": ("G4,G5", "竞赛模板、页数、匿名或获奖论文风格影响交付", "格式契约、版式检查和规则核验"),
    "measured-experiment-loop": ("conditional:G3.5", "候选配置按固定指标和预算迭代比较", "实验契约、基线、事件日志和原始输出"),
    "jupyter-live-analysis": ("conditional:G1,G3", "持久 kernel 状态或可见 notebook 对探索有实质帮助", "执行 notebook、导出输入和清洁运行路径"),
    "sql-data-analysis": ("conditional:G3", "SQL 数据库或关系模式是输入的一部分", "schema、查询、计划检查和导出结果"),
    "academic-translation": ("conditional:G4,G5", "需要双语或英文论文、摘要、图注或回复", "受保护 token 审计和译稿"),
    "research-presentation": ("conditional:G4", "需要答辩、组会或论文汇报", "证据台账、演示文稿、讲稿和渲染 QA"),
    "plan-and-execution": ("G0,G2", "任务具有多个输出、依赖或需要可恢复执行", "计划、负责人、检查和停止条件"),
    "competition-scoring": ("G6", "需要评委式评分、预审、复审或提分排序", "证据评分表、问题台账和置信度"),
    "submission-packaging": ("G7", "最终文件必须符合比赛交付规则", "manifest、哈希、匿名和清洁解压检查"),
    "ai-use-disclosure": ("G0,G7", "AI、代码助手、翻译、检索、图像工具或模型 API 有实质参与", "规则记录、使用台账和声明"),
}


def registry_skill_names(root: Path) -> tuple[str, ...]:
    registry = root / "skills" / "registry.yaml"
    if not registry.is_file():
        return CANONICAL_SKILLS
    names = []
    in_canonical = False
    for line in registry.read_text(encoding="utf-8").splitlines():
        if line == "canonical_skills:":
            in_canonical = True
            continue
        if in_canonical and line and not line.startswith(" "):
            break
        if in_canonical and line.startswith("  ") and not line.startswith("    ") and line.rstrip().endswith(":"):
            names.append(line.strip()[:-1])
    if not names:
        raise SystemExit(f"ERROR no canonical Skills found in {registry}")
    missing_meta = sorted(set(names) - set(DEFAULT_SKILL_META))
    stale_meta = sorted(set(DEFAULT_SKILL_META) - set(names))
    if missing_meta or stale_meta:
        raise SystemExit(f"ERROR registry/ledger metadata mismatch missing={missing_meta} stale={stale_meta}")
    return tuple(names)


def expand_stage_spec(value: str) -> list[str]:
    stages: list[str] = []
    for token in value.split(","):
        token = token.strip()
        if not token:
            continue
        if "-" in token:
            start, end = token.split("-", 1)
            if start not in STAGE_ORDER or end not in STAGE_ORDER:
                raise SystemExit(f"ERROR invalid stage range: {token}")
            stages.extend(STAGE_ORDER[STAGE_ORDER.index(start): STAGE_ORDER.index(end) + 1])
        elif token in STAGE_ORDER:
            stages.append(token)
        else:
            raise SystemExit(f"ERROR invalid stage: {token}")
    return list(dict.fromkeys(stages))


def build_skill_ledger(root: Path) -> str:
    records = []
    for name in registry_skill_names(root):
        stage, trigger, evidence = DEFAULT_SKILL_META[name]
        conditional = stage.startswith("conditional:")
        stage_text = stage.split(":", 1)[1] if conditional else stage
        planned = expand_stage_spec(stage_text)
        records.append({
            "name": name,
            "status": "pending" if conditional else "active",
            "trigger_checked": not conditional,
            "planned_stages": planned,
            "stage_status": {planned_stage: "pending" for planned_stage in planned},
            "trigger": trigger,
            "reason": "" if conditional else "完整 solve 流程的基础模块",
            "required_outputs": [evidence],
            "owner": "workflow-orchestration",
            "invocations": [],
            "last_revision": 0,
            "evidence": [],
        })
    return json.dumps({"schema_version": 1, "revision": 0, "records": records}, ensure_ascii=False, indent=2) + "\n"


def build_rework_log() -> str:
    return json.dumps({
        "event_type": "log_init",
        "schema_version": 1,
        "revision": 0,
        "open_events": 0,
    }, ensure_ascii=False) + "\n"


WORK_DIRS = (
    "题目",
    "数据",
    "求解/计划",
    "求解/数据审计",
    "求解/证据",
    "求解/实验",
    "论文",
    "提交",
)


def yaml_scalar(value: str) -> str:
    """Return a JSON-quoted scalar, which is also valid YAML."""

    return json.dumps(value, ensure_ascii=False)


def build_state(args: argparse.Namespace, root: Path) -> str:
    created = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    project_id = args.project_id or root.name
    metadata = {
        "competition": args.competition or "",
        "problem": args.problem or "",
        "deadline": args.deadline or "",
    }
    metadata_lines = "\n".join(
        f"  {key}: {yaml_scalar(value)}" for key, value in metadata.items()
    )
    return f"""schema_version: 3
project_id: {yaml_scalar(project_id)}
metadata:
{metadata_lines}
revision: 0
current_mode: solve
current_stage: G0
user_request: ""
protected_paths:
  - 题目/
  - 数据/
input_versions: []
decisions: []
approvals: []
artifacts: []
gates:
  G0: in_progress
  G1: not_started
  G1.5: not_started
  G2: not_started
  G3: not_started
  G3.5: not_started
  G4: not_started
  G5: not_started
  G6: not_started
  G7: not_started
open_gates:
  - G0
failures: []
created_at_utc: {yaml_scalar(created)}
next_action: "Inventory official files, data, rules, runtimes, and constraints."
last_rework_event: ""
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, help="mathskills project root")
    parser.add_argument("--project-id", help="stable project identifier")
    parser.add_argument("--competition", help="competition name, for example CUMCM")
    parser.add_argument("--problem", help="problem identifier or short title")
    parser.add_argument("--deadline", help="deadline as a documented string with timezone")
    args = parser.parse_args()

    root = args.root.resolve()
    created_dirs: list[Path] = []
    for relative in WORK_DIRS:
        path = root / relative
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
            created_dirs.append(path)
        elif not path.is_dir():
            raise SystemExit(f"ERROR expected directory but found file: {path}")

    state = root / "求解" / "project_state.yaml"
    if state.exists():
        print(f"UNCHANGED {state}")
    else:
        state.write_text(build_state(args, root), encoding="utf-8", newline="\n")
        print(f"CREATED {state}")

    ledger = root / "求解" / "计划" / "skill_use_ledger.json"
    if not ledger.exists():
        ledger.write_text(build_skill_ledger(root), encoding="utf-8", newline="\n")
        print(f"CREATED {ledger}")
    rework_log = root / "求解" / "计划" / "rework_log.jsonl"
    if not rework_log.exists():
        rework_log.write_text(build_rework_log(), encoding="utf-8", newline="\n")
        print(f"CREATED {rework_log}")

    for path in created_dirs:
        print(f"CREATED_DIR {path}")
    print(f"READY root={root} created_dirs={len(created_dirs)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
