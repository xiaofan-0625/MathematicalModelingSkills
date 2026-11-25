# mathskills v4.6

`mathskills` 是面向数学建模竞赛的端到端 Skill 系统。它把官方题面、原始附件和比赛规则转化为可审计、可回退、可重做的建模证据链，而不是只生成一段题解或一篇看起来完整的论文。

```text
审题取证 → 数据与文献证据 → 建模蓝图 → 实现求解
→ 验证冻结 → 图表与论文 → 编译复现 → 评分修订 → 提交封装
```

如果中途发现题意、数据、模型、代码、验证、图表或论文有问题，不允许只修改最后一个文件。系统会记录变更事件，标记下游产物过期，回到最早受影响阶段，重跑主动 Skill，重新验证并重新冻结，最后再重建论文、评分和提交包。

主入口是 `SKILL.md`，模块注册表是 `skills/registry.yaml`。`CLAUDE.md` 仅保留旧平台兼容规则，不能覆盖主入口。

## 适用范围

支持五种工作模式：

| 模式 | 用途 |
|---|---|
| `solve` | 从赛题开始完成完整建模项目 |
| `review` | 审查已有模型、代码或论文并追溯证据 |
| `repair` | 修复指定阶段的问题，再执行必要的下游复核 |
| `score` | 按评委口径评分、识别封顶项、安排提分顺序 |
| `deliver` | 清洁编译、复现核验、匿名审查和提交包封装 |

普通作业中只需一次计算或简短证明的任务，不需要启动完整流程。

## G0–G7 质量门

| 阶段 | 核心产物 | 关键验收 |
|---|---|---|
| G0 启动 | 项目状态、输入清单、执行边界 | 原始输入受保护，范围与下一步明确 |
| G1 审题取证 | 题目契约、数据审计、外部数据契约、歧义表 | 每问的目标、约束、输出、数据来源和依赖可核对 |
| G1.5 证据与范文 | 文献地图、引用台账、范文模式 | 外部主张可追溯，范文未被当作答案 |
| G2 建模蓝图 | 基线、公式、算法、实验、推导与验证设计 | 模型可实现、可检验并覆盖所有问题 |
| G3 求解实现 | 代码、原始输出、求解日志 | 实现与公式一致，结果合法且保证不越权 |
| G3.5 验证冻结 | 对照、敏感性、失败测试、冻结数值 | 结论强度与证据匹配 |
| G4 图文生产 | 图源、图数据、论文与附录 | 每问形成方法—结果—验证—边界闭环 |
| G5 编译复现 | PDF、产物清单、复现报告 | 清洁重跑、版式和跨文件数值一致 |
| G6 评委审查 | 量化评分、硬门槛、问题台账 | 分数有证据，阻断项已清除或显式保留 |
| G7 提交封装 | 最终目录、清单、哈希、归档复核 | 匿名、命名、文件与当届规则一致 |

详细门槛见 `references/workflow-gates.md`。

## 全模块覆盖与回退协议

每个项目在 G0 创建 `求解/计划/skill_use_ledger.json`，逐一记录 32 个 canonical Skill 是 `active` 还是 `not_applicable`。没有触发的条件模块也必须留下触发检查和具体理由，不能通过“没用到”跳过登记。

每次实质修改都写入 `求解/计划/rework_log.jsonl`，包括最早受影响阶段、失效产物、需要重跑的 Skill、重新冻结条件和修订前后证据。完整字段和影响矩阵见 `references/skill-coverage-and-rework.md`。

## 32 个本地模块

系统保留审题取证、数据分析、文献证据、模型争辩、公式化、稳健性、科研绘图、论文写作、评分和提交等能力。v3 的六个专职模块为：

- `problem-forensics`：题面法证、逐问交付矩阵、歧义与附件契约；
- `exemplar-distillation`：从优秀论文提炼可迁移模式，禁止复制答案与措辞；
- `model-formulation-and-solving`：变量、公式、求解器、实现接口与独立可行性检查；
- `technical-diagrams`：技术路线图、流程图、机制图和可编辑源的视觉 QA；
- `competition-scoring`：证据绑定的 100 分诊断、硬门槛和提分优先级；
- `submission-packaging`：清洁构建、匿名、清单、SHA-256 与归档解压复核。

v4 通过 `Find Skills` 检索并结合本地只读参考，又补充七个不与原体系重复的模块：

- `forecasting-and-backtesting`：历史信息边界、滚动回测、多步预测与区间覆盖率；
- `simulation-and-uncertainty`：Monte Carlo、情景、离散事件、独立重复、收敛与尾部风险；
- `geospatial-modeling`：CRS、几何质量、空间连接、MAUP、空间泄漏和隐私；
- `network-modeling`：节点边契约、方向权重、路径流、零模型与结构扰动；
- `scientific-tables`：冻结结果到表格的单位、精度、不确定性和来源链；
- `ai-use-disclosure`：当届规则核验、使用台账、人类复核和真实披露；
- `systematic-evidence-review`：深度检索、系统证据综述、来源质量、文献矩阵、偏倚审查和差距分析。

v4.2 继续核验 GitHub、微信公众号原文与可信转载，没有再堆叠同义模块，而是强化 `literature-evidence` 和 G1.5：检索词中英转换、多渠道合并去重、书目信息交叉核验、来源证据护照、全文/摘要/片段访问等级，以及“未取得全文不得声称核验方法细节”的证据边界。公众号标题、来源等级和归并决定见 `references/wechat-research-skills-audit.md`。

v4.3 审阅了 `figures4papers`、`Anatomy` 和 `Supervisor-Skills`。三者没有被机械复制为新模块，而是按真实缺口归并：模型创意增加“可执行路径先验门、致命缺陷封顶和下一档改进动作”；图稿增加动机图、方案总览图、结果图的角色分工和最终尺寸预算；机制图增加抽象概念到部件、关系、状态和标注的一一映射。网页专属动画、安装命令、硬编码风格和可能误导的截断柱状图轴没有采用。详细审计见 `references/selected-candidate-skills-audit.md`。

v4.4 逐项审计了《科研论文与数学建模 Skills 清单.xlsx》的 196 项候选。新增两个真正缺失且不与原模块重复的能力：

- `external-data-acquisition`：外部 API、门户、网页和公开数据的权威源选择、原始响应快照、查询参数、版本/vintage、许可、字段字典、联结基数与泄漏检查；
- `experimental-design-and-inference`：数据采集前的 estimand、独立实验单位、随机化、阻断、因子设计、样本量/功效、多重比较、停止规则和与设计匹配的分析计划。

PyMC、SHAP、statsmodels、统计分析、模型验证、文献检索、科研绘图、写作、审稿和排版等候选均按机制归并到原有规范模块；专利、基金、期刊投稿、海报和领域专属数据库 API 没有被复制成数模主流程模块。完整逐项处置见 `references/excel-full-skills-audit.md` 和 `references/excel-skills-disposition.csv`。

v4.5 对第二批新增的 94 项进行了差集审计。新增 `mathematical-derivation-and-proof`，专门处理公式推导、定理/命题证明、近似边界、反例优先检查和证明义务台账。`result-to-claim`、`paper-claim-audit`、`experiment-audit`、`training-check`、`system-profile`、`ablation-planner` 和 `figure-spec` 的有效机制分别合并到写作、复现、验证、求解和绘图模块；搜索适配器、远程计算、专利、海报、网页渲染和文件格式工具未被复制为重复数模模块。第二批与总表处置见 `references/excel-second-batch-skills-audit.md`、`references/excel-second-batch-disposition.csv` 及更新后的 290 项总审计。

多目标优化没有被做成重复的泛化模块，而是增强在 `model-formulation-and-solving` 中：保留 Pareto 权衡、解释最终折中、重复随机种子并限制全局最优表述。系统综述只在确有深度检索需求时条件加载。Find Skills 的检索与取舍见 `references/find-skills-modeling-audit.md`。

别名只用于发现，执行时统一解析到规范模块，避免重复加载相同规则。

v4.6 完成流程级整理：新增全模块适用性台账、条件 Skill 触发检查、变更影响矩阵、回退与重做日志、版本化冻结和交付前一致性要求。该协议解决“模块存在但没有被调用”和“修改上游后遗漏重做下游”的问题，见 `references/skill-coverage-and-rework.md`。

## 快速开始

把官方赛题和规则放入 `题目/`，原始附件放入 `数据/`。不要修改这两个目录中的原文件。

初始化工作区：

```bash
python scripts/init_project.py . --competition "比赛名称" --problem "题号或简称" --deadline "2026-09-13T18:00:00+08:00"
```

随后让 AI 读取 `SKILL.md`，例如：

```text
使用 mathskills 的 solve 模式。先完成 G1 审题和数据审计，暂不开始建模。
```

阶段切换前执行结构验收：

```bash
python scripts/validate_project.py . --through G1
```

该脚本验证目录、台账、JSON 和阶段必需产物，不替代数学正确性、代码复核或人工评审。

初始化后，基础模块默认进入 `active`；条件模块保持 `pending`，必须根据题目逐项激活或写明不适用。例如：

```bash
python scripts/set_skill_status.py . forecasting-and-backtesting not_applicable --reason "本题没有时间顺序或未来预测目标" --evidence "求解/计划/problem_contract.md"
```

主动模块按阶段完成；同一 Skill 后续阶段仍需再次留下调用证据：

```bash
python scripts/set_skill_status.py . workflow-orchestration complete --reason "G0 状态、保护路径和适用性台账已核验" --stage G0 --evidence "求解/project_state.yaml" --evidence "求解/计划/skill_use_ledger.json"
```

## 项目结构

```text
mathskills/
├── SKILL.md
├── agents/openai.yaml
├── skills/
│   ├── registry.yaml
│   └── <canonical-skill>/SKILL.md
├── references/
├── scripts/
│   ├── init_project.py
│   ├── set_skill_status.py
│   ├── record_rework.py
│   ├── close_rework.py
│   ├── validate_project.py
│   ├── validate_bundle.py
│   └── score_project.py
├── 题目/                         # 官方原始输入，只读
├── 数据/                         # 官方原始附件，只读
├── 求解/
│   ├── project_state.yaml
│   ├── 计划/
│   │   ├── skill_use_ledger.json
│   │   ├── rework_log.jsonl
│   ├── 数据审计/
│   ├── 证据/
│   ├── 实验/
│   └── 问题X/{code,结果,图片}/
├── 论文/
└── 提交/
```

国赛模板资产位于 `国赛/`。使用时复制到 `论文/` 后修改副本，不直接修改模板资产；公开分发前须单独确认字体许可证。

## 评分和复现

评分量表位于 `references/judge-scorecard.md`。先填写证据 JSON，再由脚本校验权重、证据、硬门槛和区间分：

```bash
python scripts/score_project.py score-input.json 求解/scorecard.json
```

缺失或没有证据的维度保持“未评估”，脚本不会自动给高分。这个分数用于内部诊断，不预测官方奖项。

关键数值只能从机器可读结果进入论文。推荐事实所有权：题面要求归 `problem_contract.md`，模型选择归建模蓝图，数值归 `frozen_numbers.json`，引用归 `citation_ledger.csv`，图表归生成脚本与图数据，审稿问题归 scorecard，提交文件归 manifest 和哈希。

发生实质修改时先记录回退：

```bash
python scripts/record_rework.py . --trigger "验证失败" --changed-path "求解/问题2/code/model.py" --earliest-gate G2 --invalidated-gate G3 --invalidated-gate G3.5 --invalidated-gate G4 --replay-skill model-formulation-and-solving --replay-skill validation-and-robustness --replay-skill academic-writing
```

重做、验证和重新冻结完成后，用当前证据关闭该 revision：

```bash
python scripts/close_rework.py . --revision 1 --evidence "求解/问题2/结果/validation_report.md" --evidence "求解/问题2/结果/frozen_numbers.json"
```

## Skill 包维护

修改模块或注册表后运行：

```bash
python scripts/validate_bundle.py .
```

还应对主入口和每个子 Skill 运行 `skill-creator` 的 `quick_validate.py`（当前共 33 个入口：根入口加 32 个子 Skill），并对脚本执行语法检查和临时项目冒烟测试。压缩分发包只能在这些检查通过后重建，避免包内仍保留旧规则。

## 关键边界

- 当届官方题面和规则始终高于范文、论坛、搜索结果和历史模板；
- 不虚构数据、引用、实验、软件运行、显著性或全局最优；
- 复杂度与“前沿”不是创新，只有解决本题真实缺口且经验证的改进才算；
- 优化器收敛不等于模型正确，漂亮图表不等于结论成立；
- 本地打包完成不等于已经外部提交，除非实际观察到上传回执。
