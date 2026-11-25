---
name: mathskills
description: End-to-end mathematical-modeling competition workflow for problem forensics, external data, evidence, experimental design, formulation, derivation and proof, forecasting, simulation, spatial and network models, validation, figures, tables, writing, scoring, reproducibility, AI-use compliance, and submission packaging. Use to solve, review, repair, score, or deliver a mathematical-modeling competition project; not for ordinary homework that needs only a short calculation.
metadata:
  version: "4.6.0"
  short-description: "数学建模竞赛全流程：审题、建模、求解、验证、制图、写作、评分与提交"
---

# Mathematical Modeling Competition Workflow

把赛题和原始附件转化为一条可审计、可回退、可重做的证据链：

```text
题面事实 → 建模决策 → 可执行代码 → 冻结结果
        → 图表与论文 → 评委式审查 → 可复现提交包

任何上游实质变化都必须沿依赖关系回退，不能只改最后一个文件：

```text
变更事件 → 标记下游过期 → 返回最早受影响阶段 → 重跑主动 Skills
         → 重新验证 → 重新冻结 → 重建图表/论文/评分/提交包
```
```

本 Skill 是路由器和质量总纲，不把所有专业规则一次加载进上下文。先读 `skills/registry.yaml`，再只读取当前阶段需要的子 Skill 与参考资料。`CLAUDE.md` 是兼容旧平台的历史资料，不是当前规范来源。

## 先确定工作模式

根据用户请求选择最小充分模式；不要无故启动完整流程。

| 模式 | 适用请求 | 默认起点 |
|---|---|---|
| `solve` | 从赛题开始完成建模竞赛项目 | G0 |
| `review` | 客观评价已有论文或项目 | G6，并回溯证据 |
| `repair` | 修复指定模型、代码、图表或论文问题 | 对应阶段 |
| `score` | 按评委口径评分、排名风险与改进优先级 | G6 |
| `deliver` | 编译、核验、整理附件与提交包 | G5 |

若输入不完整，先完成能做的只读审计并标记缺口。只有缺失信息会实质改变答案时才询问用户；其他情况采用可解释的保守假设并记录。

## 每个 Skill 都必须被考虑

G0 初始化 `求解/计划/skill_use_ledger.json`，为注册表中的每个 canonical Skill 记录
`active` 或 `not_applicable`。条件 Skill 只有在完成触发条件检查并写出具体理由后才能标记
`not_applicable`；不能因为本题暂时没有用到就删除或忽略它。`pending`、`blocked` 和被变更
影响的 `superseded` 记录会阻塞对应阶段或最终交付。

使用和回退协议见 [`references/skill-coverage-and-rework.md`](references/skill-coverage-and-rework.md)。
该协议规定每个模块的触发条件、最小证据、必备产物、变更影响、回退阶段、重新执行顺序和
重新冻结要求。

## 不可破坏的原则

1. **官方题面与当届规则最高优先。** 翻译、范文、论坛答案和搜索结果只能辅助理解，不能改写目标、约束或提交要求。
2. **保护原始输入。** `题目/`、`数据/` 和用户指定的模板为只读事实源；生成物进入 `求解/`、`论文/` 与 `提交/`。
3. **不伪造。** 不虚构数据、引用、实验、软件运行、全局最优性、统计显著性或成功日志。
4. **先回答赛题，再谈创新。** 创新必须解决本题的真实缺口，并有公式、代码、对照实验和适用边界；复杂度本身不是创新。
5. **每个数字可追溯。** 正文关键数值必须来自机器可读结果；发现冲突时修复产生该数值的上游，不手工改论文数字。
6. **验证必须可能推翻结论。** 至少设置一个失败导向测试，记录失败、无效和负结果，不只保留漂亮结果。
7. **图表承担证据功能。** 每张图回答一个问题；流程图与数据图分工明确；必须检查最终 PDF 中的实际可读性。
8. **评分必须给证据。** 不给“感觉分”；每项分数绑定页码、公式、代码、输出或缺失项，并给置信度。
9. **声明边界。** 有限枚举、局部搜索、经验压力测试和一阶近似不能被写成连续全局证明或普适结论。
10. **用户保留重大决定权。** 只有当选题解释、目标优先级、数据删除、模型主线或结论强度会实质改变成果时暂停确认。

## 阶段门

详细输入、产物与验收条件见 `references/workflow-gates.md`。

| 阶段 | 核心任务 | 必备产物 | 通过条件 |
|---|---|---|---|
| G0 启动 | 盘点规则、输入、环境、预算与恢复点 | `project_state.yaml`、输入清单、计划 | 范围、保护路径和下一步明确 |
| G1 审题取证 | 双遍审题、交付矩阵、歧义、数据审计与外部数据契约 | `problem_contract.md`、`data_audit.md`、条件性数据快照清单 | 每一问的输入、目标、约束、输出与数据来源可核对 |
| G1.5 证据与范文 | 文献核验、方法证据、优秀范文蒸馏 | 文献地图、引用台账、范文模式表 | 核心外部主张可追溯，范文未被当作答案 |
| G2 建模蓝图 | 基线、主模型、变量、公式、算法、实验、推导与验证设计 | 建模蓝图、决策矩阵、依赖图、条件性实验/推导契约 | 模型可实现、可检验、完整回答题目 |
| G3 求解实现 | 逐问编码、求解、约束核验、日志 | 代码、原始输出、运行日志 | 产生合法可复算结果，不以收敛代替正确性 |
| G3.5 验证冻结 | 基线、敏感性、稳健性、消融、压力测试 | 验证报告、`frozen_numbers.json` | 结论强度与证据匹配，结果被冻结 |
| G4 叙事生产 | 数据图、流程图、正文、表格与附录 | 可编辑图源、论文源文件 | 每项结论形成“方法—结果—验证”闭环 |
| G5 编译复现 | 清洁编译、逐页视觉检查、重跑与一致性 | PDF、manifest、复现报告 | 编译、版式、数值和引用无阻断问题 |
| G6 评委审查 | 对抗式审稿、量化评分、修订优先级 | scorecard、问题台账、修订稿 | 硬伤清零，分数有证据且无越权表述 |
| G7 提交封装 | 匿名、命名、附件、哈希与提交清单 | `提交/`、最终清单、哈希 | 从干净副本可重建，提交包符合当届规则 |

不得为了“走流程”机械地产生空文件。短任务只执行相关阶段；完整竞赛项目按门推进，未通过的阶段不能被后续漂亮排版掩盖。

每个阶段还必须记录 `revision`。如果题面、数据、文献、实验设计、公式、代码、验证、冻结
结果、图表、论文、模板、评分或提交规则发生实质变化，先写入
`求解/计划/rework_log.jsonl`，再把受影响的下游门和产物标为过期，返回最早受影响阶段，
完成重做后才允许再次通过。旧版本保留用于审计，不得用新文件覆盖历史证据而不留记录。

## 子 Skill 路由

| 需求 | 读取并执行 |
|---|---|
| 题面法证、逐问交付矩阵、歧义管理 | `skills/problem-forensics/SKILL.md` |
| 数据读取、清洗、EDA、统计审计 | `skills/data-analysis/SKILL.md` |
| 外部 API、门户、网页、公开数据与可复现快照 | `skills/external-data-acquisition/SKILL.md` |
| 随机化、阻断、因子设计、样本量、功效与推断计划 | `skills/experimental-design-and-inference/SKILL.md` |
| 文献、方法、领域事实与引用核验 | `skills/literature-evidence/SKILL.md` |
| 深度检索、系统证据综述、文献矩阵与差距分析 | `skills/systematic-evidence-review/SKILL.md` |
| 优秀范文蒸馏与可迁移模式 | `skills/exemplar-distillation/SKILL.md` |
| 模型候选争辩、盲点与反例 | `skills/model-deliberation/SKILL.md` |
| 公式化、求解器设计、实现接口 | `skills/model-formulation-and-solving/SKILL.md` |
| 公式推导、命题证明、近似边界与证明义务审计 | `skills/mathematical-derivation-and-proof/SKILL.md` |
| 时间序列预测、滚动回测、预测区间 | `skills/forecasting-and-backtesting/SKILL.md` |
| Monte Carlo、情景、离散事件与不确定性传播 | `skills/simulation-and-uncertainty/SKILL.md` |
| 坐标、区域、空间连接、距离与空间验证 | `skills/geospatial-modeling/SKILL.md` |
| 图结构、路径、流、中心性、社区与网络稳健性 | `skills/network-modeling/SKILL.md` |
| 模型完成后的验证、敏感性与压力测试 | `skills/validation-and-robustness/SKILL.md`、`skills/measured-experiment-loop/SKILL.md` |
| 数据型科研图 | `skills/scientific-visualization/SKILL.md` |
| 技术路线图、流程图、机制图 | `skills/technical-diagrams/SKILL.md` |
| 描述、对比、消融、敏感性与结果表格 | `skills/scientific-tables/SKILL.md` |
| 论文、翻译、自然化、国赛风格 | 相应 `academic-*` 与 `national-award-paper-style` |
| 评委评分、问题优先级、重评 | `skills/competition-scoring/SKILL.md` |
| 清洁重跑、产物链与跨文件一致性 | `skills/reproducibility-audit/SKILL.md` |
| 匿名、命名、清单、哈希和提交压缩包 | `skills/submission-packaging/SKILL.md` |
| AI 使用规则、过程台账与提交声明 | `skills/ai-use-disclosure/SKILL.md` |

存在本地或平台原生文档、PDF、表格、幻灯片技能时，按文件类型调用；专业文件技能负责读写和渲染，本 Skill 负责建模逻辑与证据一致性。

## 工作区与事实源

优先复用现有目录。新项目可运行：

```bash
python scripts/init_project.py <project-root> --competition "<比赛名称>"
python scripts/validate_project.py <project-root> --through G1
```

初始化后用 `scripts/set_skill_status.py` 完成条件模块的触发判断。发生实质修改时先运行
`scripts/record_rework.py`，完成重做和证据复核后再用 `scripts/close_rework.py` 关闭该
revision；这些脚本记录控制状态，不代替数学判断和人工验收。

推荐结构：

```text
题目/                         原始赛题与官方规则（保护）
数据/                         原始附件（保护）
求解/
  project_state.yaml          当前阶段、决策、开放门与下一步
  计划/
    skill_use_ledger.json     全部 canonical Skill 的适用性与调用证据
    rework_log.jsonl          变更、失效、回退和重做事件
  数据审计/                   字段、单位、缺失、异常、泄漏检查
    外部数据/                 查询清单、原始快照、字段字典与联结审计
  证据/                       文献地图、引用台账、范文蒸馏
  实验/                       预注册实验契约、运行事件与失败记录
  问题X/
    code/                     确定性脚本与测试
    结果/                     原始输出、验证报告、frozen_numbers.json
    图片/                     图源、图数据与导出文件
  artifact_manifest.json
  reproducibility_report.md
  scorecard.json
论文/                         官方模板副本、正文、参考文献与 PDF
提交/                         最终提交副本、支撑材料、清单与哈希
```

当同一事实出现在多处时采用以下所有权：

- 题面要求：`problem_contract.md`；
- 建模选择：建模蓝图与决策日志；
- 数值：`frozen_numbers.json`；
- 引用：`citation_ledger.csv`；
- 图表数据：生成图表的机器可读文件；
- 问题状态：审稿/评分台账；
- 交付文件：提交清单与哈希。
- Skill 适用性与调用状态：`skill_use_ledger.json`；变更影响与重做状态：`rework_log.jsonl`。

## 关键执行规则

### 审题

先做“结构化抽取”，再做“对抗式复读”。将题面拆成事实、决策变量、目标、硬约束、随机量、时间顺序、必须报告的输出和提交规则。对每个歧义记录候选解释、影响、快速反例和采用理由。具体协议见 `references/problem-forensics.md`。

### 检索与创新

先检索题目直接方法，再检索相邻领域和近年进展；正式论文、预印本、全文、摘要、元数据和搜索片段分级标注。检索记录必须保留中英关键词、渠道、版本、访问等级和交叉核验状态；只有摘要或片段时，不得声称已核验公式、实现细节、数值或局限。每项拟采用思想必须落到“哪一问、改哪一处、为何适配、如何验证、何时失效”。禁止用文献热度替代本题适配性。

### 外部数据与实验设计

只在题目确实需要时引入外部数据。先定义字段、时空范围和权威性，再取得并哈希保存原始响应；记录查询参数、发布日期或 vintage、许可、覆盖和联结基数。实时 API 返回值不能只留在笔记本状态中，搜索片段也不能充当数据集。

当项目控制数据采集、处理分配、算法比较或仿真运行时，在观察结果前定义 estimand、独立实验单位、随机化/阻断、样本量或最小可检测效应、分析模型、多重比较和停止规则。数据采集前的设计由 `experimental-design-and-inference` 负责，候选模型完成后的稳健性验证仍由验证模块负责。

### 建模与求解

每问至少包括：目标、输入、输出、符号与单位、假设、目标函数、约束、算法、停止条件、复杂度、可行性检查、基线、验证设计和交给下一问的接口。先构造合法基线，再增加复杂度。详见 `references/modeling-solver-playbook.md`。

遇到时间、空间、网络或随机系统时，加载对应专门模块，不把它们压缩成普通回归或一张示意图。预测必须尊重历史信息边界；仿真必须有独立重复与收敛证据；空间测量必须明确 CRS 和距离语义；网络结论必须追溯到节点、边、方向和权重定义。

当结论依赖非平凡公式链、定理、误差界、近似或算法保证时，加载推导证明模块。逐步区分恒等式、逻辑推论、外部定理、近似、数值证据和启发式；先尝试边界反例，再维护证明义务。符号计算和随机数值检验可以发现错误，但不能冒充一般性证明。

### 冻结与写作

验证通过后冻结数值。图、表、摘要、正文、结论和附录只能消费冻结结果。每个子问题末尾用一段直接回答题目：采用了什么、得到什么、如何验证、边界是什么。摘要最后写，并逐问覆盖题目要求的输出。

冻结不是永久不可改变，而是“当前 revision 下可消费”的状态。任何改变冻结结果来源、
定义、精度、比较对象、验证结论或适用边界的修改，必须先解冻并创建 rework 事件；修改后
重跑受影响的 G3.5–G7，并生成新的冻结文件、图表、表格、正文、评分和清单。

表格必须从机器可读冻结结果生成，明确单位、精度、比较方向、不确定性和缺失值含义。只有真正可比且差异有意义的结果才能被标为最佳。

### 图与流程图

先写图的证据句，再选图型。探索图与投稿图分离；数据图保留生成脚本与图数据，流程图保留可编辑源。默认输出矢量主文件和位图预览。详细标准见 `references/visual-evidence-design.md`。

### 评分与修订

使用 `references/judge-scorecard.md` 的 100 分量表和硬门槛。先给原始分、封顶原因、置信度和证据，再给“单位时间提分最高”的修改顺序。修改后只重评受影响维度和所有硬门槛，不为追求高分虚构改善。

评分发现不是只在 scorecard 中改字：每个问题必须指向最早责任阶段和修复 Skill。修复后先
重跑责任阶段及其下游，再重评受影响维度，并保留修订前后证据。

### 提交

当届官方规则决定模板、页数、匿名、文件名、附件和 AI 使用声明。最终包必须从干净副本编译，清除缓存与敏感信息，生成清单和 SHA-256，并抽样解压复核。详见 `references/submission-packaging.md`。

若项目使用生成式 AI、代码助手、翻译、图像工具或模型 API，在 G0 先核对当届规则并维护使用台账；G7 只根据官方格式和真实记录生成声明。规则禁止或关键条款不清时，不得自行推定允许。

## 失败与降级

- 工具不可用：说明未验证环节，保留可运行源文件，不冒充已执行。
- 文献只能核验元数据：降级证据等级，不据此声称方法细节或创新。
- 优化器只找到局部解：报告可行上界、多起点稳定性或合法下界，不写全局最优。
- 数据不足：区分“无法识别”与“结果为零”，给出最小补充数据需求。
- 评分材料不全：给区间分和置信度，不用缺失证据脑补高分。
- 编译或重跑失败：提交状态为未通过；保留日志与可恢复路径。

## 完成标准

只有同时满足以下条件，才能宣布完整项目完成：

- 所有子问题均被直接回答，目标、约束与题面一致；
- 原始数据未被静默修改，外部数据、主张和引用可追溯；
- 受控实验的独立单位、分配、样本量和推断计划与实际执行一致；
- 主模型有合法基线、验证、失败测试与适用边界；
- 关键推导与证明的假设、义务、近似区间和未证部分均与论文表述一致；
- 关键结果由代码生成并冻结，图表和论文与之逐项一致；
- 论文编译成功并完成逐页视觉检查；
- 评委式评分没有未处理的阻断项或诚信否决项；
- 从保护输入可重建关键结果和最终 PDF；
- 最终提交包通过匿名、文件名、清单、哈希和解压复核；
- 未解决限制被明确写出，而不是藏在措辞中。
- `skill_use_ledger.json` 中每个 canonical Skill 都有适用性结论，主动模块有当前 revision 的证据；
- `rework_log.jsonl` 无未关闭事件，所有交付产物属于同一 revision，且最后一次实质变更后完成了清洁重跑。

