---
name: ai-use-disclosure
description: Audit and prepare truthful competition-specific disclosure of AI-assisted work, including rule checks, use logs, human verification, privacy boundaries, and submission evidence. Use at project launch and delivery when generative AI, code assistants, translation, search, image tools, or model APIs may have contributed.
---

# Audit AI Use and Disclosure

The current official competition rules are the only authority on whether AI use is allowed, restricted, prohibited, or must be disclosed. Historical templates and third-party examples cannot grant permission.

## Compliance workflow

1. At G0, capture the exact official rule text, version or retrieval date, competition, track, and affected deliverables. Mark the status `allowed`, `restricted`, `prohibited`, or `unclear`; do not assume silence means permission.
2. Maintain an AI-use ledger as work occurs. Record date, tool and model when known, purpose, inputs or data class, output used, human verification, affected files or sections, and responsible team member.
3. Distinguish assistance types: brainstorming, literature discovery, translation, coding, debugging, data analysis, modeling, prose revision, figure generation, and final-answer production. Record material uses even if the output was later edited.
4. Verify every retained output against primary data, executable code, authoritative sources, or independent reasoning. AI output is not evidence, a citation, a software run, or a substitute for team responsibility.
5. Check privacy, confidentiality, copyright, licensing, personal data, unpublished data, and organizer restrictions before sending material to any external model or service. Redact or use a local alternative when required.
6. Generate the disclosure only from the ledger and official requested format. State what was used, for what purpose, and how it was verified without exaggerating or concealing the contribution.
7. At G7, reconcile the disclosure with code metadata, document history, generated assets, references, acknowledgments, and package contents. Preserve evidence that the required statement is present in the correct file and location.

If use is prohibited or a material rule remains unclear, stop the affected AI-assisted operation and surface the issue to the user. Do not fabricate a no-use statement, backdate a ledger, invent tool versions or prompts, list AI as an author, or reveal secrets and personal data merely to make a disclosure more detailed.

## Outputs and gate

Recommended artifacts are `求解/证据/ai_rule_record.md`, `求解/证据/ai_use_ledger.csv`, and the competition-required declaration in its mandated location. If no declaration is required, retain the internal audit without adding unnecessary text to the paper.

G7 passes only when the applicable rule is identified, the ledger and deliverables agree, material use is truthfully represented, required human verification is documented, and the package contains the mandated declaration without leaking sensitive information.
