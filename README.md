# AI Coding 团队化实战

把个人 AI Coding 经验，变成团队可复制、可审查、可接管的工程能力。从一个真实需求出发，建立规则、上下文、任务、验证和协作的共同约定。

**[在线阅读](https://daviddingxu.github.io/ai-coding-for-teams/) · [完整目录](docs/course/README.md) · [落地实践](#落地实践) · [反馈与勘误](https://github.com/DavidDingXu/ai-coding-for-teams/issues)**

**课程已完结 · 14 篇完整文章 · 5 个模块 · 团队最小落地手册**

## 适合谁学

适合正在推动 AI Coding 的技术负责人、架构师、研发效能团队，以及已有个人使用经验、希望开展团队协作的开发者。

课程讨论一套团队共同使用的工程流程：需求如何进入任务、规则由谁维护、上下文如何选择、交付怎样验证、其他人如何审查和接管。仓库提供完整正文、流程图、目录模板、数据结构与实践清单。

## 学完能做什么

- 划清共享运行时、团队规则、应用规则与工具适配的职责。
- 将复杂需求拆成范围明确的任务，让设计、实现和审查有稳定产物可依据。
- 区分历史失败与本次回归，保留验证记录，支持交付审查、任务接管和经验复用。

## 课程路线

| 模块 | 文章 | 学习重点 |
| --- | --- | --- |
| [从个人经验到团队系统](docs/course/README.md#module-01) | 00–02 | 共享运行时、团队与应用 SPEC、规则所有权 |
| [从复杂需求到可审查交付](docs/course/README.md#module-02) | 03–06 | 需求拆分、有界上下文、阶段产物与 Task 化开发 |
| [从一次成功到持续复用](docs/course/README.md#module-03) | 07–08 | 验证基线、失败归因、规则与案例沉淀 |
| [从单 Agent 到团队协作](docs/course/README.md#module-04) | 09–11 | Agent 分工、多工具适配、审查与接管 |
| [最小试点与收官](docs/course/README.md#module-05) | 12–13 | 选择试点，把目录、流程和规则带回团队 |

第一次阅读建议从 [课程总览](00-overview.md) 开始；准备组织试点时，可以先读 [团队最小落地包](12-minimal-playbook.md)，再按具体问题回查对应模块。

## 落地实践

选择一个中低风险、范围清晰、有回归手段的真实需求，沿着下面的流程完成一次团队试点：

**需求确认 → 选择规则与上下文 → 设计与任务拆分 → 小步实现 → 验证与审查 → 总结归档**

| 实践入口 | 可以带走什么 |
| --- | --- |
| [团队最小落地包](12-minimal-playbook.md) | `.team-agent/` 目录模板、任务状态、PRD、设计、计划与归档结构 |
| [SPEC 体系](02-spec-system.md) | 团队、领域、业务与工程规则的分层方法 |
| [验证治理](07-verification-governance.md) | 基线记录、失败分类和交付判断依据 |
| [协作与接管](11-workspace-collaboration.md) | 任务、产物、代码变更与审查记录的协作方式 |

把示例中的目录、命令和规则替换成团队现有约定，先让一个需求完整走通，再决定哪些步骤值得自动化。

## 交流与许可

欢迎通过 [Issue](https://github.com/DavidDingXu/ai-coding-for-teams/issues) 分享实践问题或反馈勘误，提交改进前请阅读 [贡献指南](CONTRIBUTING.md)。

- 文章、图示与课程文档：[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)，署名、非商业使用、相同方式共享。
- 示例代码、脚本与网站代码：[PolyForm Noncommercial 1.0.0](LICENSE)。

商业使用需另行授权；具体范围与第三方内容说明见 [许可说明](LICENSING.md)。
