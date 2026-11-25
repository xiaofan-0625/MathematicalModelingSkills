# Excel Full Skills Audit

Source workbooks: `C:\Users\XYF06\Desktop\自主学习\科研论文与数学建模 Skills 清单.xlsx` and `C:\Users\XYF06\Desktop\自主学习\科研论文与数学建模 Skills 清单 (1).xlsx` (read-only; not modified).

Both workbooks were parsed directly from XLSX worksheet XML because their declared used ranges did not expose all records reliably. The first contains 196 distinct Skill names. The second is a strict extension with 94 additions, 0 removals, and 0 same-name changes, for 290 distinct names in total.

## Decision rules

- Keep a separate canonical Skill only when it owns a distinct decision boundary and changes real modeling work.
- Merge aliases, library/service adapters, venue variants, and overlapping workflows into one canonical owner.
- For candidates without a verifiable repository, map only the advertised capability; do not adopt implementation claims.
- Keep PDF, DOCX, PPTX, and XLSX mechanics in platform-native file Skills rather than copying them into mathskills.
- Exclude infrastructure, grant, patent, journal-operation, poster, Wiki, Overleaf, and meta-Skill operations from the core competition workflow.
- Do not execute third-party install, credential, network-mutation, or external-message instructions from either source collection.

## Summary

- Total reviewed: **290**
- Distinct names: **290**
- 新增模块（归并）: **13**
- 合并增强: **28**
- 合并覆盖: **13**
- 已覆盖: **154**
- 无法核验（能力已覆盖）: **36**
- 平台原生能力: **4**
- 超出主范围: **42**

The first batch created `external-data-acquisition` and `experimental-design-and-inference`. The second batch adds `mathematical-derivation-and-proof` as one canonical owner distilled from four candidates. All other retained mechanisms resolve to existing modules or platform-native file Skills. The CSV beside this file is the machine-readable version of all 290 decisions.

## Row-by-row disposition

| ID | Candidate Skill | Source | Disposition | Canonical owner | Reason |
|---:|---|---|---|---|---|
| 1 | academic-pipeline | academic-research-skills | 已覆盖 | workflow-orchestration + plan-and-execution | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 2 | academic-research-skills（总入口） | academic-research-skills | 已覆盖 | workflow-orchestration + plan-and-execution | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 3 | 1start-mathmodel | MathModelAgent | 已覆盖 | workflow-orchestration + plan-and-execution | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 4 | vibe-research-workflow | Supervisor-Skills | 合并增强 | workflow-orchestration + plan-and-execution | 采用能改变实际决策的机制，删除平台命令、固定风格、重复工作流和工具绑定。 |
| 5 | deep-research | Supervisor-Skills | 合并增强 | systematic-evidence-review | 采用能改变实际决策的机制，删除平台命令、固定风格、重复工作流和工具绑定。 |
| 6 | research-paper-writing | research-paper-writing | 已覆盖 | workflow-orchestration + plan-and-execution | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 7 | academic-research-skills-codex | academic-research-skills-codex | 已覆盖 | workflow-orchestration + plan-and-execution | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 8 | research-to-paper | 未提供可核验仓库 | 无法核验（能力已覆盖） | workflow-orchestration + plan-and-execution | 清单未提供可核验仓库；仅按描述映射到现有规范模块，不采信未知实现细节。 |
| 9 | experiment-agent | academic-research-skills | 已覆盖 | experimental-design-and-inference + measured-experiment-loop | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 10 | research-plan | ChineseResearchLaTeX | 已覆盖 | workflow-orchestration + plan-and-execution | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 11 | scientific-brainstorming | K-Dense scientific-agent-skills | 已覆盖 | model-deliberation | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 12 | denario | K-Dense scientific-agent-skills | 已覆盖 | model-deliberation | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 13 | paper-novelty-design | 未提供可核验仓库 | 无法核验（能力已覆盖） | model-deliberation | 清单未提供可核验仓库；仅按描述映射到现有规范模块，不采信未知实现细节。 |
| 14 | idea-evaluator | Supervisor-Skills | 合并增强 | model-deliberation | 采用能改变实际决策的机制，删除平台命令、固定风格、重复工作流和工具绑定。 |
| 15 | research-idea | ChineseResearchLaTeX | 已覆盖 | model-deliberation | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 16 | hypothesis-generation | K-Dense scientific-agent-skills | 已覆盖 | model-deliberation | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 17 | PaperPilot | 未提供可核验仓库 | 无法核验（能力已覆盖） | model-deliberation | 清单未提供可核验仓库；仅按描述映射到现有规范模块，不采信未知实现细节。 |
| 18 | Scientific Brainstorming | 未提供可核验仓库 | 无法核验（能力已覆盖） | model-deliberation | 清单未提供可核验仓库；仅按描述映射到现有规范模块，不采信未知实现细节。 |
| 19 | research-brainstorm | 未提供可核验仓库 | 无法核验（能力已覆盖） | model-deliberation | 清单未提供可核验仓库；仅按描述映射到现有规范模块，不采信未知实现细节。 |
| 20 | research-to-paper-scope | 未提供可核验仓库 | 无法核验（能力已覆盖） | model-deliberation | 清单未提供可核验仓库；仅按描述映射到现有规范模块，不采信未知实现细节。 |
| 21 | nature-social-science | nature-skills | 已覆盖 | literature-evidence + systematic-evidence-review | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 22 | nature-academic-search | nature-skills | 已覆盖 | literature-evidence + systematic-evidence-review | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 23 | nature-downloader | nature-skills | 已覆盖 | literature-evidence + systematic-evidence-review | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 24 | nature-literature-pipeline | nature-skills | 已覆盖 | literature-evidence + systematic-evidence-review | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 25 | paper-lookup | K-Dense scientific-agent-skills | 已覆盖 | literature-evidence + systematic-evidence-review | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 26 | research-lookup | K-Dense scientific-agent-skills | 已覆盖 | literature-evidence + systematic-evidence-review | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 27 | bgpt-paper-search | K-Dense scientific-agent-skills | 已覆盖 | literature-evidence + systematic-evidence-review | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 28 | paper-scraper | 未提供可核验仓库 | 无法核验（能力已覆盖） | literature-evidence + systematic-evidence-review | 清单未提供可核验仓库；仅按描述映射到现有规范模块，不采信未知实现细节。 |
| 29 | ArXiv Digest | 未提供可核验仓库 | 无法核验（能力已覆盖） | literature-evidence + systematic-evidence-review | 清单未提供可核验仓库；仅按描述映射到现有规范模块，不采信未知实现细节。 |
| 30 | Literature Survey | 未提供可核验仓库 | 无法核验（能力已覆盖） | literature-evidence + systematic-evidence-review | 清单未提供可核验仓库；仅按描述映射到现有规范模块，不采信未知实现细节。 |
| 31 | paper-search-mcp | 未提供可核验仓库 | 无法核验（能力已覆盖） | literature-evidence + systematic-evidence-review | 清单未提供可核验仓库；仅按描述映射到现有规范模块，不采信未知实现细节。 |
| 32 | research-literature-search | ChineseResearchLaTeX | 已覆盖 | literature-evidence + systematic-evidence-review | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 33 | research-literature-radar | ChineseResearchLaTeX | 已覆盖 | literature-evidence + systematic-evidence-review | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 34 | literature-research | 未提供可核验仓库 | 无法核验（能力已覆盖） | literature-evidence + systematic-evidence-review | 清单未提供可核验仓库；仅按描述映射到现有规范模块，不采信未知实现细节。 |
| 35 | arxiv-translator | 未提供可核验仓库 | 无法核验（能力已覆盖） | literature-evidence + systematic-evidence-review | 清单未提供可核验仓库；仅按描述映射到现有规范模块，不采信未知实现细节。 |
| 36 | openalex-database | K-Dense scientific-agent-skills | 已覆盖 | literature-evidence + systematic-evidence-review | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 37 | pubmed-database | K-Dense scientific-agent-skills | 已覆盖 | literature-evidence + systematic-evidence-review | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 38 | arxiv-database | K-Dense scientific-agent-skills | 已覆盖 | literature-evidence + systematic-evidence-review | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 39 | biorxiv-database | K-Dense scientific-agent-skills | 已覆盖 | literature-evidence + systematic-evidence-review | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 40 | nature-citation | nature-skills | 已覆盖 | literature-evidence + systematic-evidence-review | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 41 | nature-reader | nature-skills | 已覆盖 | exemplar-distillation + systematic-evidence-review | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 42 | nature-paper-xray | nature-skills | 已覆盖 | exemplar-distillation + systematic-evidence-review | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 43 | nature-paper-trans | nature-skills | 已覆盖 | literature-evidence + systematic-evidence-review | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 44 | nature-paper-card | nature-skills | 已覆盖 | literature-evidence + systematic-evidence-review | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 45 | research-literature-review | ChineseResearchLaTeX | 已覆盖 | literature-evidence + systematic-evidence-review | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 46 | research-literature-interpretation | ChineseResearchLaTeX | 已覆盖 | exemplar-distillation + systematic-evidence-review | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 47 | research-topic-extractor | ChineseResearchLaTeX | 已覆盖 | literature-evidence + systematic-evidence-review | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 48 | research-guide-updater | ChineseResearchLaTeX | 已覆盖 | literature-evidence + systematic-evidence-review | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 49 | literature-review | K-Dense scientific-agent-skills | 已覆盖 | literature-evidence + systematic-evidence-review | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 50 | literature-review-builder | 未提供可核验仓库 | 无法核验（能力已覆盖） | literature-evidence + systematic-evidence-review | 清单未提供可核验仓库；仅按描述映射到现有规范模块，不采信未知实现细节。 |
| 51 | academic-literature-research | 未提供可核验仓库 | 无法核验（能力已覆盖） | literature-evidence + systematic-evidence-review | 清单未提供可核验仓库；仅按描述映射到现有规范模块，不采信未知实现细节。 |
| 52 | background-research-processor | 未提供可核验仓库 | 无法核验（能力已覆盖） | literature-evidence + systematic-evidence-review | 清单未提供可核验仓库；仅按描述映射到现有规范模块，不采信未知实现细节。 |
| 53 | PaperSpine | 未提供可核验仓库 | 无法核验（能力已覆盖） | literature-evidence + systematic-evidence-review | 清单未提供可核验仓库；仅按描述映射到现有规范模块，不采信未知实现细节。 |
| 54 | AI Research | 未提供可核验仓库 | 无法核验（能力已覆盖） | literature-evidence + systematic-evidence-review | 清单未提供可核验仓库；仅按描述映射到现有规范模块，不采信未知实现细节。 |
| 55 | open-notebook | K-Dense scientific-agent-skills | 已覆盖 | literature-evidence + systematic-evidence-review | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 56 | markitdown | K-Dense scientific-agent-skills | 已覆盖 | literature-evidence + systematic-evidence-review | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 57 | paper-2-web | K-Dense scientific-agent-skills | 已覆盖 | literature-evidence + systematic-evidence-review | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 58 | research-to-paper-curate | 未提供可核验仓库 | 无法核验（能力已覆盖） | literature-evidence + systematic-evidence-review | 清单未提供可核验仓库；仅按描述映射到现有规范模块，不采信未知实现细节。 |
| 59 | paper-explain-figures | ChineseResearchLaTeX | 已覆盖 | exemplar-distillation + systematic-evidence-review | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 60 | nature-writing | nature-skills | 已覆盖 | academic-writing + national-award-paper-style | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 61 | paper-writer | Supervisor-Skills | 合并增强 | academic-writing + national-award-paper-style | 采用能改变实际决策的机制，删除平台命令、固定风格、重复工作流和工具绑定。 |
| 62 | intro-drafter | Supervisor-Skills | 合并增强 | academic-writing + national-award-paper-style | 采用能改变实际决策的机制，删除平台命令、固定风格、重复工作流和工具绑定。 |
| 63 | tech-paper-template | Supervisor-Skills | 已覆盖 | academic-writing + national-award-paper-style | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 64 | benchmark-paper-template | Supervisor-Skills | 已覆盖 | academic-writing + national-award-paper-style | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 65 | research-writing-skill | Academic Skills | 已覆盖 | academic-writing + national-award-paper-style | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 66 | academic-paper | academic-research-skills | 已覆盖 | academic-writing + national-award-paper-style | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 67 | paper-write-sci | ChineseResearchLaTeX | 已覆盖 | academic-writing + national-award-paper-style | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 68 | PaperCraft | 未提供可核验仓库 | 无法核验（能力已覆盖） | academic-writing + national-award-paper-style | 清单未提供可核验仓库；仅按描述映射到现有规范模块，不采信未知实现细节。 |
| 69 | Scientific Write | 未提供可核验仓库 | 无法核验（能力已覆盖） | academic-writing + national-award-paper-style | 清单未提供可核验仓库；仅按描述映射到现有规范模块，不采信未知实现细节。 |
| 70 | academic-writing-publication | 未提供可核验仓库 | 无法核验（能力已覆盖） | academic-writing + national-award-paper-style | 清单未提供可核验仓库；仅按描述映射到现有规范模块，不采信未知实现细节。 |
| 71 | research-to-paper-write | 未提供可核验仓库 | 无法核验（能力已覆盖） | academic-writing + national-award-paper-style | 清单未提供可核验仓库；仅按描述映射到现有规范模块，不采信未知实现细节。 |
| 72 | nature-proposal-writer | nature-skills | 超出主范围 | academic-writing + national-award-paper-style | 保留通用原则，不把基金、专利、期刊运营、海报或高度领域专属工具扩成数模主流程模块。 |
| 73 | NSFC 基金写作 | ChineseResearchLaTeX | 超出主范围 | academic-writing + national-award-paper-style | 保留通用原则，不把基金、专利、期刊运营、海报或高度领域专属工具扩成数模主流程模块。 |
| 74 | nature-polishing | nature-skills | 已覆盖 | academic-humanization | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 75 | paper-polish | Supervisor-Skills | 已覆盖 | academic-humanization | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 76 | academic-humanizer | 未提供可核验仓库 | 无法核验（能力已覆盖） | academic-humanization | 清单未提供可核验仓库；仅按描述映射到现有规范模块，不采信未知实现细节。 |
| 77 | anti-defensive-writing | 未提供可核验仓库 | 无法核验（能力已覆盖） | academic-humanization | 清单未提供可核验仓库；仅按描述映射到现有规范模块，不采信未知实现细节。 |
| 78 | humanizer | 未提供可核验仓库 | 无法核验（能力已覆盖） | academic-humanization | 清单未提供可核验仓库；仅按描述映射到现有规范模块，不采信未知实现细节。 |
| 79 | abstract-polish-trackchanges | 未提供可核验仓库 | 无法核验（能力已覆盖） | academic-writing + national-award-paper-style | 清单未提供可核验仓库；仅按描述映射到现有规范模块，不采信未知实现细节。 |
| 80 | nature-paper2word | nature-skills | 已覆盖 | academic-writing + national-award-paper-style | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 81 | nature-ref-verifier | nature-skills | 已覆盖 | literature-evidence | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 82 | citation-management | K-Dense scientific-agent-skills | 已覆盖 | literature-evidence | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 83 | pyzotero | K-Dense scientific-agent-skills | 已覆盖 | literature-evidence | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 84 | research-citation-check | ChineseResearchLaTeX | 已覆盖 | literature-evidence | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 85 | nsfc-ref-alignment | ChineseResearchLaTeX | 超出主范围 | literature-evidence | 保留通用原则，不把基金、专利、期刊运营、海报或高度领域专属工具扩成数模主流程模块。 |
| 86 | ars-citation-check | academic-research-skills | 已覆盖 | literature-evidence | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 87 | nature-reviewer | nature-skills | 已覆盖 | competition-scoring + academic-writing | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 88 | nature-response | nature-skills | 已覆盖 | competition-scoring + academic-writing | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 89 | academic-paper-reviewer | academic-research-skills | 已覆盖 | competition-scoring + academic-writing | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 90 | peer-review | K-Dense scientific-agent-skills | 已覆盖 | competition-scoring + academic-writing | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 91 | pre-submission-reviewer | Supervisor-Skills | 合并增强 | competition-scoring + academic-writing | 采用能改变实际决策的机制，删除平台命令、固定风格、重复工作流和工具绑定。 |
| 92 | rebuttal-guidance | Supervisor-Skills | 合并增强 | competition-scoring + academic-writing | 采用能改变实际决策的机制，删除平台命令、固定风格、重复工作流和工具绑定。 |
| 93 | scholar-evaluation | K-Dense scientific-agent-skills | 已覆盖 | competition-scoring + academic-writing | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 94 | scientific-critical-thinking | K-Dense scientific-agent-skills | 已覆盖 | competition-scoring + academic-writing | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 95 | research-paper-structure-editor | 未提供可核验仓库 | 无法核验（能力已覆盖） | competition-scoring + academic-writing | 清单未提供可核验仓库；仅按描述映射到现有规范模块，不采信未知实现细节。 |
| 96 | nsfc-reviewers | ChineseResearchLaTeX | 超出主范围 | competition-scoring + academic-writing | 保留通用原则，不把基金、专利、期刊运营、海报或高度领域专属工具扩成数模主流程模块。 |
| 97 | nsfc-qc | ChineseResearchLaTeX | 超出主范围 | competition-scoring + academic-writing | 保留通用原则，不把基金、专利、期刊运营、海报或高度领域专属工具扩成数模主流程模块。 |
| 98 | nsfc-length-aligner | ChineseResearchLaTeX | 超出主范围 | competition-scoring + academic-writing | 保留通用原则，不把基金、专利、期刊运营、海报或高度领域专属工具扩成数模主流程模块。 |
| 99 | ars-review | academic-research-skills | 已覆盖 | competition-scoring + academic-writing | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 100 | ars-revision | academic-research-skills | 已覆盖 | competition-scoring + academic-writing | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 101 | paper-select-journal | ChineseResearchLaTeX | 超出主范围 | 超出数学建模竞赛主流程 | 保留通用原则，不把基金、专利、期刊运营、海报或高度领域专属工具扩成数模主流程模块。 |
| 102 | paper-know-journal | ChineseResearchLaTeX | 超出主范围 | 超出数学建模竞赛主流程 | 保留通用原则，不把基金、专利、期刊运营、海报或高度领域专属工具扩成数模主流程模块。 |
| 103 | venue-templates | K-Dense scientific-agent-skills | 超出主范围 | 超出数学建模竞赛主流程 | 保留通用原则，不把基金、专利、期刊运营、海报或高度领域专属工具扩成数模主流程模块。 |
| 104 | research-grants | K-Dense scientific-agent-skills | 超出主范围 | 超出数学建模竞赛主流程 | 保留通用原则，不把基金、专利、期刊运营、海报或高度领域专属工具扩成数模主流程模块。 |
| 105 | nature-figure | nature-skills | 合并增强 | scientific-visualization | 采用能改变实际决策的机制，删除平台命令、固定风格、重复工作流和工具绑定。 |
| 106 | figure-designer | Supervisor-Skills | 合并增强 | scientific-visualization | 采用能改变实际决策的机制，删除平台命令、固定风格、重复工作流和工具绑定。 |
| 107 | drawio-reconstruction | Supervisor-Skills | 合并增强 | technical-diagrams | 采用能改变实际决策的机制，删除平台命令、固定风格、重复工作流和工具绑定。 |
| 108 | scibox-figure | sci-box | 已覆盖 | scientific-visualization | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 109 | scibox-diagram | sci-box | 已覆盖 | technical-diagrams | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 110 | 4drawio | MathModelAgent | 已覆盖 | technical-diagrams | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 111 | mathmodel-figure-templates | MathModelAgent | 已覆盖 | scientific-visualization | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 112 | scientific-visualization | K-Dense scientific-agent-skills | 已覆盖 | scientific-visualization | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 113 | scientific-schematics | K-Dense scientific-agent-skills | 已覆盖 | technical-diagrams | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 114 | infographics | K-Dense scientific-agent-skills | 已覆盖 | scientific-visualization | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 115 | matplotlib | K-Dense scientific-agent-skills | 已覆盖 | scientific-visualization | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 116 | seaborn | K-Dense scientific-agent-skills | 已覆盖 | scientific-visualization | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 117 | plotly | K-Dense scientific-agent-skills | 已覆盖 | scientific-visualization | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 118 | figures4papers | figures4papers | 合并增强 | scientific-visualization | 采用能改变实际决策的机制，删除平台命令、固定风格、重复工作流和工具绑定。 |
| 119 | academic-figure-generator | academic-figure-generator | 已覆盖 | scientific-visualization | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 120 | paper-figure-visual | 未提供可核验仓库 | 无法核验（能力已覆盖） | scientific-visualization | 清单未提供可核验仓库；仅按描述映射到现有规范模块，不采信未知实现细节。 |
| 121 | scipilot-figure | 未提供可核验仓库 | 无法核验（能力已覆盖） | scientific-visualization | 清单未提供可核验仓库；仅按描述映射到现有规范模块，不采信未知实现细节。 |
| 122 | Nature Figure（未核验条目） | 未提供可核验仓库 | 无法核验（能力已覆盖） | scientific-visualization | 清单未提供可核验仓库；仅按描述映射到现有规范模块，不采信未知实现细节。 |
| 123 | latex-posters | K-Dense scientific-agent-skills | 超出主范围 | 超出数学建模竞赛论文主流程 | 保留通用原则，不把基金、专利、期刊运营、海报或高度领域专属工具扩成数模主流程模块。 |
| 124 | pptx-posters | K-Dense scientific-agent-skills | 超出主范围 | 超出数学建模竞赛论文主流程 | 保留通用原则，不把基金、专利、期刊运营、海报或高度领域专属工具扩成数模主流程模块。 |
| 125 | statistical-analysis | K-Dense scientific-agent-skills | 已覆盖 | data-analysis | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 126 | statsmodels | K-Dense scientific-agent-skills | 已覆盖 | data-analysis | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 127 | scikit-learn | K-Dense scientific-agent-skills | 已覆盖 | data-analysis | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 128 | pymc-bayesian-modeling | K-Dense scientific-agent-skills | 合并增强 | data-analysis | 采用能改变实际决策的机制，删除平台命令、固定风格、重复工作流和工具绑定。 |
| 129 | statistical-power | K-Dense scientific-agent-skills | 新增模块（归并） | experimental-design-and-inference | 与同簇候选共同抽取 estimand、独立实验单位、随机化、阻断、功效、多重比较和停止规则。 |
| 130 | experimental-design | K-Dense scientific-agent-skills | 新增模块（归并） | experimental-design-and-inference | 与同簇候选共同抽取 estimand、独立实验单位、随机化、阻断、功效、多重比较和停止规则。 |
| 131 | uncertainty-and-units | K-Dense scientific-agent-skills | 合并增强 | simulation-and-uncertainty + data-analysis | 采用能改变实际决策的机制，删除平台命令、固定风格、重复工作流和工具绑定。 |
| 132 | analytical-method-validation | K-Dense scientific-agent-skills | 新增模块（归并） | experimental-design-and-inference | 与同簇候选共同抽取 estimand、独立实验单位、随机化、阻断、功效、多重比较和停止规则。 |
| 133 | exploratory-data-analysis | K-Dense scientific-agent-skills | 已覆盖 | data-analysis | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 134 | shap | K-Dense scientific-agent-skills | 已覆盖 | data-analysis | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 135 | sympy | K-Dense scientific-agent-skills | 已覆盖 | model-formulation-and-solving | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 136 | polars | K-Dense scientific-agent-skills | 已覆盖 | data-analysis | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 137 | dask | K-Dense scientific-agent-skills | 已覆盖 | data-analysis | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 138 | networkx | K-Dense scientific-agent-skills | 已覆盖 | network-modeling | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 139 | simpy | K-Dense scientific-agent-skills | 已覆盖 | simulation-and-uncertainty | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 140 | pymoo | K-Dense scientific-agent-skills | 合并增强 | model-formulation-and-solving | 采用能改变实际决策的机制，删除平台命令、固定风格、重复工作流和工具绑定。 |
| 141 | timesfm-forecasting | K-Dense scientific-agent-skills | 合并增强 | forecasting-and-backtesting | 采用能改变实际决策的机制，删除平台命令、固定风格、重复工作流和工具绑定。 |
| 142 | aeon | K-Dense scientific-agent-skills | 已覆盖 | forecasting-and-backtesting | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 143 | scikit-survival | K-Dense scientific-agent-skills | 已覆盖 | data-analysis | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 144 | matlab | K-Dense scientific-agent-skills | 已覆盖 | model-formulation-and-solving | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 145 | scientific-toolkit-skill | Academic Skills | 已覆盖 | workflow-orchestration + model-formulation-and-solving | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 146 | pymatgen | K-Dense scientific-agent-skills | 超出主范围 | 超出通用数学建模主范围 | 保留通用原则，不把基金、专利、期刊运营、海报或高度领域专属工具扩成数模主流程模块。 |
| 147 | qutip | K-Dense scientific-agent-skills | 超出主范围 | 超出通用数学建模主范围 | 保留通用原则，不把基金、专利、期刊运营、海报或高度领域专属工具扩成数模主流程模块。 |
| 148 | typst-author | MathModelAgent | 已覆盖 | academic-writing + national-award-paper-style | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 149 | 5writing | MathModelAgent | 已覆盖 | academic-writing + national-award-paper-style | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 150 | make-latex-model | ChineseResearchLaTeX | 已覆盖 | academic-writing + national-award-paper-style | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 151 | transfer-old-latex-to-new | ChineseResearchLaTeX | 已覆盖 | academic-writing + national-award-paper-style | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 152 | complete-example | ChineseResearchLaTeX | 已覆盖 | academic-writing + national-award-paper-style | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 153 | research-to-paper-build | 未提供可核验仓库 | 无法核验（能力已覆盖） | academic-writing + national-award-paper-style | 清单未提供可核验仓库；仅按描述映射到现有规范模块，不采信未知实现细节。 |
| 154 | office-academic-skill | Academic Skills | 已覆盖 | academic-writing + national-award-paper-style | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 155 | nsfc-code | ChineseResearchLaTeX | 超出主范围 | 超出数学建模竞赛主流程 | 保留通用原则，不把基金、专利、期刊运营、海报或高度领域专属工具扩成数模主流程模块。 |
| 156 | paper-coverletter | ChineseResearchLaTeX | 超出主范围 | 超出数学建模竞赛主流程 | 保留通用原则，不把基金、专利、期刊运营、海报或高度领域专属工具扩成数模主流程模块。 |
| 157 | nature-image2ppt | nature-skills | 已覆盖 | research-presentation + technical-diagrams | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 158 | markdown-mermaid-writing | K-Dense scientific-agent-skills | 已覆盖 | research-presentation + technical-diagrams | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 159 | nature-paper2ppt | nature-skills | 已覆盖 | research-presentation + technical-diagrams | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 160 | scientific-slides | K-Dense scientific-agent-skills | 已覆盖 | research-presentation + technical-diagrams | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 161 | talk-builder | 未提供可核验仓库 | 无法核验（能力已覆盖） | research-presentation + technical-diagrams | 清单未提供可核验仓库；仅按描述映射到现有规范模块，不采信未知实现细节。 |
| 162 | paper-wechat-article | 未提供可核验仓库 | 超出主范围 | 超出数学建模竞赛主流程 | 保留通用原则，不把基金、专利、期刊运营、海报或高度领域专属工具扩成数模主流程模块。 |
| 163 | paper-infographic-builder | 未提供可核验仓库 | 无法核验（能力已覆盖） | scientific-visualization + research-presentation | 清单未提供可核验仓库；仅按描述映射到现有规范模块，不采信未知实现细节。 |
| 164 | cls-code-annotator | 未提供可核验仓库 | 超出主范围 | 超出数学建模竞赛主流程 | 保留通用原则，不把基金、专利、期刊运营、海报或高度领域专属工具扩成数模主流程模块。 |
| 165 | datamagic | 未提供可核验仓库 | 无法核验（能力已覆盖） | external-data-acquisition | 清单未提供可核验仓库；仅按描述映射到现有规范模块，不采信未知实现细节。 |
| 166 | nature-paper-to-patent | nature-skills | 超出主范围 | 超出数学建模竞赛主流程 | 保留通用原则，不把基金、专利、期刊运营、海报或高度领域专属工具扩成数模主流程模块。 |
| 167 | patent-disclosure | 未提供可核验仓库 | 超出主范围 | 超出数学建模竞赛主流程 | 保留通用原则，不把基金、专利、期刊运营、海报或高度领域专属工具扩成数模主流程模块。 |
| 168 | patent-engineering-workbench | 未提供可核验仓库 | 超出主范围 | 超出数学建模竞赛主流程 | 保留通用原则，不把基金、专利、期刊运营、海报或高度领域专属工具扩成数模主流程模块。 |
| 169 | 2analysis-modeling | MathModelAgent | 已覆盖 | model-formulation-and-solving | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 170 | 3coding-visual | MathModelAgent | 已覆盖 | scientific-visualization + model-formulation-and-solving | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 171 | 6verity | MathModelAgent | 已覆盖 | validation-and-robustness | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 172 | mathmodel-to-ei | MathModelAgent | 已覆盖 | academic-writing + national-award-paper-style | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 173 | doctor | MathModelAgent | 已覆盖 | competition-scoring + validation-and-robustness | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 174 | mathmodel-to-ei 模板集 | MathModelAgent | 已覆盖 | academic-writing + national-award-paper-style | 候选能力已由所列规范模块承担；避免重复加载同义 Skill。 |
| 175 | nature-experiment-log | nature-skills | 合并增强 | measured-experiment-loop | 采用能改变实际决策的机制，删除平台命令、固定风格、重复工作流和工具绑定。 |
| 176 | research-to-paper-audit | 未提供可核验仓库 | 无法核验（能力已覆盖） | reproducibility-audit + competition-scoring | 清单未提供可核验仓库；仅按描述映射到现有规范模块，不采信未知实现细节。 |
| 177 | research-to-paper-humanize | 未提供可核验仓库 | 无法核验（能力已覆盖） | academic-humanization | 清单未提供可核验仓库；仅按描述映射到现有规范模块，不采信未知实现细节。 |
| 178 | nature-data | nature-skills | 新增模块（归并） | external-data-acquisition | 与其他数据服务共同抽取来源权威性、查询快照、版本、许可、覆盖和联结审计，归并为一个来源无关模块。 |
| 179 | nature-statistics | nature-skills | 新增模块（归并） | experimental-design-and-inference | 与同簇候选共同抽取 estimand、独立实验单位、随机化、阻断、功效、多重比较和停止规则。 |
| 180 | get-available-resources | K-Dense scientific-agent-skills | 新增模块（归并） | external-data-acquisition | 与其他数据服务共同抽取来源权威性、查询快照、版本、许可、覆盖和联结审计，归并为一个来源无关模块。 |
| 181 | chembl-database | K-Dense scientific-agent-skills | 合并覆盖 | external-data-acquisition | 通用数据获取与快照规则已纳入；数据库专属 API、凭据和领域语义不复制为独立模块。 |
| 182 | pubchem-database | K-Dense scientific-agent-skills | 合并覆盖 | external-data-acquisition | 通用数据获取与快照规则已纳入；数据库专属 API、凭据和领域语义不复制为独立模块。 |
| 183 | drugbank-database | K-Dense scientific-agent-skills | 合并覆盖 | external-data-acquisition | 通用数据获取与快照规则已纳入；数据库专属 API、凭据和领域语义不复制为独立模块。 |
| 184 | uniprot-database | K-Dense scientific-agent-skills | 合并覆盖 | external-data-acquisition | 通用数据获取与快照规则已纳入；数据库专属 API、凭据和领域语义不复制为独立模块。 |
| 185 | pdb-database | K-Dense scientific-agent-skills | 合并覆盖 | external-data-acquisition | 通用数据获取与快照规则已纳入；数据库专属 API、凭据和领域语义不复制为独立模块。 |
| 186 | kegg-database | K-Dense scientific-agent-skills | 合并覆盖 | external-data-acquisition | 通用数据获取与快照规则已纳入；数据库专属 API、凭据和领域语义不复制为独立模块。 |
| 187 | reactome-database | K-Dense scientific-agent-skills | 合并覆盖 | external-data-acquisition | 通用数据获取与快照规则已纳入；数据库专属 API、凭据和领域语义不复制为独立模块。 |
| 188 | clinvar-database | K-Dense scientific-agent-skills | 合并覆盖 | external-data-acquisition | 通用数据获取与快照规则已纳入；数据库专属 API、凭据和领域语义不复制为独立模块。 |
| 189 | gnomad-database | K-Dense scientific-agent-skills | 合并覆盖 | external-data-acquisition | 通用数据获取与快照规则已纳入；数据库专属 API、凭据和领域语义不复制为独立模块。 |
| 190 | gtex-database | K-Dense scientific-agent-skills | 合并覆盖 | external-data-acquisition | 通用数据获取与快照规则已纳入；数据库专属 API、凭据和领域语义不复制为独立模块。 |
| 191 | geo-database | K-Dense scientific-agent-skills | 合并覆盖 | external-data-acquisition | 通用数据获取与快照规则已纳入；数据库专属 API、凭据和领域语义不复制为独立模块。 |
| 192 | clinicaltrials-database | K-Dense scientific-agent-skills | 合并覆盖 | external-data-acquisition | 通用数据获取与快照规则已纳入；数据库专属 API、凭据和领域语义不复制为独立模块。 |
| 193 | uspto-database | K-Dense scientific-agent-skills | 合并覆盖 | external-data-acquisition | 通用数据获取与快照规则已纳入；数据库专属 API、凭据和领域语义不复制为独立模块。 |
| 194 | alpha-vantage | K-Dense scientific-agent-skills | 新增模块（归并） | external-data-acquisition | 与其他数据服务共同抽取来源权威性、查询快照、版本、许可、覆盖和联结审计，归并为一个来源无关模块。 |
| 195 | fred-economic-data | K-Dense scientific-agent-skills | 新增模块（归并） | external-data-acquisition | 与其他数据服务共同抽取来源权威性、查询快照、版本、许可、覆盖和联结审计，归并为一个来源无关模块。 |
| 196 | datacommons-client | K-Dense scientific-agent-skills | 新增模块（归并） | external-data-acquisition | 与其他数据服务共同抽取来源权威性、查询快照、版本、许可、覆盖和联结审计，归并为一个来源无关模块。 |
| 197 | semantic-scholar | ARIS 科研技能库 | 已覆盖 | literature-evidence | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 198 | arxiv | ARIS 科研技能库 | 已覆盖 | literature-evidence | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 199 | research-lit | ARIS 科研技能库 | 已覆盖 | literature-evidence | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 200 | deepxiv | ARIS 科研技能库 | 已覆盖 | literature-evidence | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 201 | alphaxiv | ARIS 科研技能库 | 已覆盖 | literature-evidence | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 202 | exa-search | ARIS 科研技能库 | 已覆盖 | literature-evidence | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 203 | gemini-search | ARIS 科研技能库 | 已覆盖 | literature-evidence | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 204 | firecrawl-search | ARIS 科研技能库 | 已覆盖 | literature-evidence | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 205 | keenable-search | ARIS 科研技能库 | 已覆盖 | literature-evidence | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 206 | openalex | ARIS 科研技能库 | 已覆盖 | literature-evidence | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 207 | comm-lit-review | ARIS 科研技能库 | 已覆盖 | systematic-evidence-review | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 208 | comm-lit-review-claude-single | ARIS 科研技能库 | 已覆盖 | systematic-evidence-review | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 209 | pdf-explore | AcademicForge | 已覆盖 | literature-evidence + platform-native pdf | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 210 | idea-discovery | ARIS 科研技能库 | 已覆盖 | model-deliberation | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 211 | idea-creator | ARIS 科研技能库 | 已覆盖 | model-deliberation | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 212 | idea-discovery-robot | ARIS 科研技能库 | 已覆盖 | model-deliberation | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 213 | novelty-check | ARIS 科研技能库 | 已覆盖 | model-deliberation + literature-evidence | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 214 | research-refine | ARIS 科研技能库 | 已覆盖 | model-deliberation | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 215 | kill-argument | ARIS 科研技能库 | 已覆盖 | model-deliberation | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 216 | experiment-plan | ARIS 科研技能库 | 已覆盖 | experimental-design-and-inference | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 217 | run-experiment | ARIS 科研技能库 | 已覆盖 | measured-experiment-loop | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 218 | monitor-experiment | ARIS 科研技能库 | 已覆盖 | measured-experiment-loop | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 219 | experiment-audit | ARIS 科研技能库 | 合并增强 | validation-and-robustness + reproducibility-audit | 纳入结果—主张一致性、失败实验留痕和日志完整性审计；不另建实验审计入口。 |
| 220 | experiment-queue | ARIS 科研技能库 | 已覆盖 | measured-experiment-loop | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 221 | experiment-bridge | ARIS 科研技能库 | 已覆盖 | workflow-orchestration + measured-experiment-loop | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 222 | ablation-planner | ARIS 科研技能库 | 合并增强 | validation-and-robustness | 纳入基线、完整模型、单因素消融和交互消融的预先设计及结论降级规则。 |
| 223 | dse-loop | ARIS 科研技能库 | 合并增强 | measured-experiment-loop + model-formulation-and-solving | 纳入设计空间、配置哈希去重、预算、patience、正确性守卫和原始输出留存。 |
| 224 | analyze-results | ARIS 科研技能库 | 已覆盖 | data-analysis | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 225 | result-to-claim | ARIS 科研技能库 | 合并增强 | academic-writing + claim-evidence-integrity | 纳入从统计结果到论文主张的证据强度门，禁止把相关、局部或数值证据升级成更强结论。 |
| 226 | training-check | ARIS 科研技能库 | 合并增强 | validation-and-robustness | 纳入数据划分泄漏、早停、种子、检查点选择和训练稳定性核验。 |
| 227 | system-profile | ARIS 科研技能库 | 合并增强 | model-formulation-and-solving | 纳入求解前的硬件、软件、依赖、资源上限和可复现环境画像。 |
| 228 | remote-compute-ssh | AcademicForge | 超出主范围 | 超出数学建模竞赛主流程 | 远程基础设施、基金、形式化证明器、海报/网页/Wiki、Overleaf、元 Skill 优化、专利或领域注册材料不扩成数模核心模块。 |
| 229 | compute-env-setup | AcademicForge | 超出主范围 | 超出数学建模竞赛主流程 | 远程基础设施、基金、形式化证明器、海报/网页/Wiki、Overleaf、元 Skill 优化、专利或领域注册材料不扩成数模核心模块。 |
| 230 | paper-writing | ARIS 科研技能库 | 已覆盖 | academic-writing + national-award-paper-style | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 231 | paper-write | ARIS 科研技能库 | 已覆盖 | academic-writing + national-award-paper-style | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 232 | paper-plan | ARIS 科研技能库 | 已覆盖 | academic-writing + national-award-paper-style | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 233 | paper-narrative | AcademicForge | 已覆盖 | academic-writing | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 234 | writing-systems-papers | ARIS 科研技能库 | 已覆盖 | academic-writing | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 235 | paper-claim-audit | ARIS 科研技能库 | 合并增强 | academic-writing + reproducibility-audit + competition-scoring | 纳入逐条主张—证据—代码—冻结数值追踪，并把无证据主张送回上游修复。 |
| 236 | auto-paper-improvement-loop | ARIS 科研技能库 | 已覆盖 | academic-writing + competition-scoring | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 237 | resubmit-pipeline | ARIS 科研技能库 | 已覆盖 | workflow-orchestration + competition-scoring | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 238 | grant-proposal | ARIS 科研技能库 | 超出主范围 | 超出数学建模竞赛主流程 | 远程基础设施、基金、形式化证明器、海报/网页/Wiki、Overleaf、元 Skill 优化、专利或领域注册材料不扩成数模核心模块。 |
| 239 | specification-writing | ARIS 科研技能库 | 已覆盖 | problem-forensics | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 240 | scientific-writing | K-Dense 科研技能库 | 已覆盖 | academic-writing | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 241 | formula-derivation | ARIS 科研技能库 | 新增模块（归并） | mathematical-derivation-and-proof | 与公式推导、证明撰写、反例检查和证明义务编排共同归并为一个推导证明模块，区分证明、近似、数值证据与启发式。 |
| 242 | proof-writer | ARIS 科研技能库 | 新增模块（归并） | mathematical-derivation-and-proof | 与公式推导、证明撰写、反例检查和证明义务编排共同归并为一个推导证明模块，区分证明、近似、数值证据与启发式。 |
| 243 | proof-checker | ARIS 科研技能库 | 新增模块（归并） | mathematical-derivation-and-proof | 与公式推导、证明撰写、反例检查和证明义务编排共同归并为一个推导证明模块，区分证明、近似、数值证据与启发式。 |
| 244 | proof-orchestrator | ARIS 科研技能库 | 新增模块（归并） | mathematical-derivation-and-proof | 与公式推导、证明撰写、反例检查和证明义务编排共同归并为一个推导证明模块，区分证明、近似、数值证据与启发式。 |
| 245 | lean-formalize | ARIS 科研技能库 | 超出主范围 | 超出数学建模竞赛主流程 | 远程基础设施、基金、形式化证明器、海报/网页/Wiki、Overleaf、元 Skill 优化、专利或领域注册材料不扩成数模核心模块。 |
| 246 | auto-review-loop | ARIS 科研技能库 | 已覆盖 | competition-scoring + reproducibility-audit | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 247 | auto-review-loop-llm | ARIS 科研技能库 | 已覆盖 | competition-scoring + reproducibility-audit | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 248 | research-review | ARIS 科研技能库 | 已覆盖 | competition-scoring + reproducibility-audit | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 249 | rebuttal | ARIS 科研技能库 | 已覆盖 | academic-writing + competition-scoring | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 250 | citation-audit | ARIS 科研技能库 | 已覆盖 | literature-evidence | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 251 | citation-crosscheck | ARIS 科研技能库 | 已覆盖 | literature-evidence | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 252 | integrity-forensics | ARIS 科研技能库 | 合并增强 | reproducibility-audit + competition-scoring | 纳入异常结果、元数据、日志与产物链的完整性取证；不得据此自动指控不端。 |
| 253 | paper-figure | ARIS 科研技能库 | 已覆盖 | scientific-visualization | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 254 | paper-illustration | ARIS 科研技能库 | 已覆盖 | scientific-visualization + technical-diagrams | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 255 | paper-illustration-image2 | ARIS 科研技能库 | 已覆盖 | scientific-visualization + technical-diagrams | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 256 | figure-description | ARIS 科研技能库 | 已覆盖 | scientific-visualization + academic-writing | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 257 | figure-spec | ARIS 科研技能库 | 合并增强 | scientific-visualization | 纳入图稿契约：证据句、数据映射、面板、尺寸、字体、注释、格式和QA预算。 |
| 258 | figure-style | AcademicForge | 合并增强 | scientific-visualization | 纳入跨图字体、线宽、标记、色彩、图例和最终物理尺寸的一致性检查。 |
| 259 | figure-composer | AcademicForge | 合并增强 | scientific-visualization | 纳入多面板组合、共享图例、对齐、边距和最终版面可读性检查。 |
| 260 | algorithmic-art | AcademicForge | 合并增强 | scientific-visualization | 仅吸收概念图创作边界：生成图不能承担数据几何、标签或定量证据。 |
| 261 | mermaid-diagram | ARIS 科研技能库 | 已覆盖 | technical-diagrams | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 262 | paper-poster | ARIS 科研技能库 | 超出主范围 | 超出数学建模竞赛主流程 | 远程基础设施、基金、形式化证明器、海报/网页/Wiki、Overleaf、元 Skill 优化、专利或领域注册材料不扩成数模核心模块。 |
| 263 | paper-poster-html | ARIS 科研技能库 | 超出主范围 | 超出数学建模竞赛主流程 | 远程基础设施、基金、形式化证明器、海报/网页/Wiki、Overleaf、元 Skill 优化、专利或领域注册材料不扩成数模核心模块。 |
| 264 | paper-slides | ARIS 科研技能库 | 已覆盖 | research-presentation | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 265 | slides-polish | ARIS 科研技能库 | 已覆盖 | research-presentation | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 266 | paper-talk | ARIS 科研技能库 | 已覆盖 | research-presentation | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 267 | render-html | ARIS 科研技能库 | 超出主范围 | 超出数学建模竞赛主流程 | 远程基础设施、基金、形式化证明器、海报/网页/Wiki、Overleaf、元 Skill 优化、专利或领域注册材料不扩成数模核心模块。 |
| 268 | research-wiki | ARIS 科研技能库 | 超出主范围 | 超出数学建模竞赛主流程 | 远程基础设施、基金、形式化证明器、海报/网页/Wiki、Overleaf、元 Skill 优化、专利或领域注册材料不扩成数模核心模块。 |
| 269 | wiki-enrich | ARIS 科研技能库 | 超出主范围 | 超出数学建模竞赛主流程 | 远程基础设施、基金、形式化证明器、海报/网页/Wiki、Overleaf、元 Skill 优化、专利或领域注册材料不扩成数模核心模块。 |
| 270 | paper-compile | ARIS 科研技能库 | 已覆盖 | submission-packaging + reproducibility-audit | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 271 | overleaf-sync | ARIS 科研技能库 | 超出主范围 | 超出数学建模竞赛主流程 | 远程基础设施、基金、形式化证明器、海报/网页/Wiki、Overleaf、元 Skill 优化、专利或领域注册材料不扩成数模核心模块。 |
| 272 | planning-with-files | AcademicForge | 已覆盖 | workflow-orchestration + plan-and-execution | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 273 | writing-skills | AcademicForge | 超出主范围 | 超出数学建模竞赛主流程 | 远程基础设施、基金、形式化证明器、海报/网页/Wiki、Overleaf、元 Skill 优化、专利或领域注册材料不扩成数模核心模块。 |
| 274 | meta-optimize | ARIS 科研技能库 | 超出主范围 | 超出数学建模竞赛主流程 | 远程基础设施、基金、形式化证明器、海报/网页/Wiki、Overleaf、元 Skill 优化、专利或领域注册材料不扩成数模核心模块。 |
| 275 | meta-apply | ARIS 科研技能库 | 超出主范围 | 超出数学建模竞赛主流程 | 远程基础设施、基金、形式化证明器、海报/网页/Wiki、Overleaf、元 Skill 优化、专利或领域注册材料不扩成数模核心模块。 |
| 276 | patent-novelty-check | ARIS 科研技能库 | 超出主范围 | 超出数学建模竞赛主流程 | 远程基础设施、基金、形式化证明器、海报/网页/Wiki、Overleaf、元 Skill 优化、专利或领域注册材料不扩成数模核心模块。 |
| 277 | patent-pipeline | ARIS 科研技能库 | 超出主范围 | 超出数学建模竞赛主流程 | 远程基础设施、基金、形式化证明器、海报/网页/Wiki、Overleaf、元 Skill 优化、专利或领域注册材料不扩成数模核心模块。 |
| 278 | patent-review | ARIS 科研技能库 | 超出主范围 | 超出数学建模竞赛主流程 | 远程基础设施、基金、形式化证明器、海报/网页/Wiki、Overleaf、元 Skill 优化、专利或领域注册材料不扩成数模核心模块。 |
| 279 | prior-art-search | ARIS 科研技能库 | 超出主范围 | 超出数学建模竞赛主流程 | 远程基础设施、基金、形式化证明器、海报/网页/Wiki、Overleaf、元 Skill 优化、专利或领域注册材料不扩成数模核心模块。 |
| 280 | claims-drafting | ARIS 科研技能库 | 超出主范围 | 超出数学建模竞赛主流程 | 远程基础设施、基金、形式化证明器、海报/网页/Wiki、Overleaf、元 Skill 优化、专利或领域注册材料不扩成数模核心模块。 |
| 281 | invention-structuring | ARIS 科研技能库 | 超出主范围 | 超出数学建模竞赛主流程 | 远程基础设施、基金、形式化证明器、海报/网页/Wiki、Overleaf、元 Skill 优化、专利或领域注册材料不扩成数模核心模块。 |
| 282 | jurisdiction-format | ARIS 科研技能库 | 超出主范围 | 超出数学建模竞赛主流程 | 远程基础设施、基金、形式化证明器、海报/网页/Wiki、Overleaf、元 Skill 优化、专利或领域注册材料不扩成数模核心模块。 |
| 283 | indication-dossier | AcademicForge | 超出主范围 | 超出数学建模竞赛主流程 | 远程基础设施、基金、形式化证明器、海报/网页/Wiki、Overleaf、元 Skill 优化、专利或领域注册材料不扩成数模核心模块。 |
| 284 | research-pipeline | ARIS 科研技能库 | 已覆盖 | workflow-orchestration | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 285 | research-refine-pipeline | ARIS 科研技能库 | 已覆盖 | workflow-orchestration | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 286 | research-implement-feature | ARIS 科研技能库 | 已覆盖 | workflow-orchestration + plan-and-execution | 候选能力已由所列规范模块承担；保留服务或平台适配器为可选工具，不复制同义入口。 |
| 287 | pdf | K-Dense 科研技能库 | 平台原生能力 | platform-native file skills | 由平台原生文件 Skill 负责格式读写、渲染和视觉核验；mathskills 只负责建模逻辑、证据链和跨文件一致性。 |
| 288 | docx | K-Dense 科研技能库 | 平台原生能力 | platform-native file skills | 由平台原生文件 Skill 负责格式读写、渲染和视觉核验；mathskills 只负责建模逻辑、证据链和跨文件一致性。 |
| 289 | pptx | K-Dense 科研技能库 | 平台原生能力 | platform-native file skills | 由平台原生文件 Skill 负责格式读写、渲染和视觉核验；mathskills 只负责建模逻辑、证据链和跨文件一致性。 |
| 290 | xlsx | K-Dense 科研技能库 | 平台原生能力 | platform-native file skills | 由平台原生文件 Skill 负责格式读写、渲染和视觉核验；mathskills 只负责建模逻辑、证据链和跨文件一致性。 |

## Verification boundary

This disposition table proves coverage and routing, not the correctness of every third-party repository. Only mechanisms that survived overlap, scope, provenance, and decision-impact review were integrated. Both workbooks and `skills大全` remain unchanged.
