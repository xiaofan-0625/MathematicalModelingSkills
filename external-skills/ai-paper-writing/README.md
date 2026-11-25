# AI Paper Writing Skills for Claude Code

A curated collection of Claude Code skills for academic paper writing, covering the full pipeline from drafting to submission.

> Inspired by [awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) — an excellent comprehensive repository that covers translation, polishing, de-AI, diagram generation, experiment analysis, reviewer simulation, and even agent skills configuration. However, its breadth can be overwhelming for daily use. This repo distills the most frequently needed prompts into ready-to-use Claude Code skills.

## Skills

| Skill | Description | Trigger |
|-------|-------------|---------|
| `cn2en-latex` | Chinese draft → English LaTeX with polishing | `/cn2en-latex` |
| `en-polish` | Polish English LaTeX for top conferences | `/en-polish` |
| `deai-latex` | Remove AI-style writing from LaTeX | `/deai-latex` |
| `logic-check` | Final logic and consistency check | `/logic-check` |
| `abbreviate` | Slightly shorten text (~5-15 words) | `/abbreviate` |
| `expand` | Slightly expand text (~5-15 words) | `/expand` |

## Install

Copy the `.md` files to your Claude Code skills directory:

```bash
# User-level (all projects)
cp *.md ~/.claude/skills/

# Or project-level (current project only)
cp *.md .claude/skills/
```

Restart Claude Code to load new skills.

## Source

Adapted from [awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) by the community.
