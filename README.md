# AI Coding 团队化实战

**AI Coding for Teams · 把个人经验变成团队可复制、可审查、可接管的工程能力。**

[![课程已完结](https://img.shields.io/badge/课程-已完结-16a34a)](docs/course/README.md)
[![完整文章](https://img.shields.io/badge/完整文章-14_篇-2563eb)](docs/course/README.md)
[![License](https://img.shields.io/badge/License-Apache--2.0-blue)](LICENSE)

面向技术负责人、架构师和研发效能团队的完整开源教程。14 篇全文沿着共享运行时、规则体系、复杂需求拆分、有界上下文、阶段交付、验证治理和团队协作展开，提供目录、流程、数据结构、反例和最小落地手册。

**[完整目录](docs/course/README.md) · [从总纲开始](00-overview.md) · [拿走最小落地包](12-minimal-playbook.md) · [参与贡献](CONTRIBUTING.md)**

## 团队会遇到的问题

- 少数人用 AI 很顺，其他同事的交付结果却不稳定。
- 每个应用重复建设 Agent、Prompt、Skill 和规则。
- 复杂 PRD 变成无法审查的大方案、大计划和大 diff。
- AI 判断测试失败与改动无关，团队缺少可以复查的证据。
- 一次交付的经验留在聊天里，下一次任务仍然从头开始。

这套内容把这些问题落实到共享状态、规则来源、上下文范围、交付产物、测试证据和协作边界。

## 学习路线

| 阶段 | 阅读范围 | 团队可以做出的改变 |
| --- | --- | --- |
| [从个人经验到团队系统](docs/course/README.md#module-01) | 00–02 | 建立共享运行时和可维护的规则体系 |
| [从复杂需求到可审查交付](docs/course/README.md#module-02) | 03–06 | 拆需求、控制上下文、按产物和任务推进 |
| [从一次成功到持续复用](docs/course/README.md#module-03) | 07–08 | 用验证证据判断回归，把经验沉淀为资产 |
| [从单 Agent 到团队协作](docs/course/README.md#module-04) | 09–11 | 划分职责、适配工具，支持审查和接管 |
| [最小试点与收官](docs/course/README.md#module-05) | 12–13 | 选择一个真实需求，落地最小团队流程 |

## 全部文章

| 编号 | 文章全文 |
| --- | --- |
| 00 | [个人会用 AI Coding，为什么团队还是用不好？](00-overview.md) |
| 01 | [共享运行时：不要让每个应用都重复建设 Agent](01-shared-runtime.md) |
| 02 | [SPEC 体系：把规则从 Prompt 里拿出来](02-spec-system.md) |
| 03 | [复杂需求拆分：大 PRD 不能直接丢给 Agent](03-requirement-slicing.md) |
| 04 | [有界上下文：不是给 Agent 更多，而是给得更准](04-bounded-context.md) |
| 05 | [阶段化交付：别让 AI 从一句话直接改代码](05-artifact-delivery.md) |
| 06 | [Task 化开发：把大 Diff 拆成可审查的工程任务](06-task-development-review.md) |
| 07 | [验证治理：AI 说“测试失败无关”是不够的](07-verification-governance.md) |
| 08 | [资产沉淀：让每次交付反哺下一次任务](08-asset-flywheel.md) |
| 09 | [Agent 分层：不要让一个万能 Agent 包办所有事](09-adapter-agent-layering.md) |
| 10 | [多工具适配：把共享语义放 Runtime，把工具差异放 Adapter](10-adapter-tooling.md) |
| 11 | [协作面：团队如何审查和接管 Agent 产物](11-workspace-collaboration.md) |
| 12 | [团队最小落地包：从一套目录、一条流程、三类规则开始](12-minimal-playbook.md) |
| 13 | [写在最后：AI Coding 团队化，最后还是工程问题](13-closing.md) |

## 从一个真实需求开始试点

1. 共读 [总纲](00-overview.md)，选定一个团队正在处理的需求，明确当前卡在需求、规则、上下文还是验证。
2. 按 [最小落地包](12-minimal-playbook.md) 建立目录、阶段产物、团队规则和验证记录。
3. 用 [需求切片](03-requirement-slicing.md) 和 [Task 化开发](06-task-development-review.md) 限定一次改动范围。
4. 按 [验证治理](07-verification-governance.md) 保存基线、执行结果和失败分类，再由另一位同事审查与接管。
5. 把本次确实有效的规则与案例放进 [可维护的团队资产](08-asset-flywheel.md)，用于后续需求。

可以直接在 GitHub 阅读和共读。需要离线查看时：

```bash
git clone https://github.com/DavidDingXu/ai-coding-for-teams.git
cd ai-coding-for-teams
```

## 使用方式与边界

正文中的目录、状态和流程使用通用示例，适配自己的 IDE、CLI、Agent 或研发平台即可。试点先保留真实需求、代码差异和验证结果，再决定是否需要自建运行时或平台。

原有文章地址保留在仓库根目录。文章内的 Mermaid 图可以直接由 GitHub 渲染，每篇文末提供前后章节与实践导航。

## 勘误与贡献

欢迎通过 [Issue](https://github.com/DavidDingXu/ai-coding-for-teams/issues) 提交问题和脱敏实践案例，或按 [贡献指南](CONTRIBUTING.md) 发起 Pull Request。全文与图示采用 [Apache License 2.0](LICENSE)，引用与转载见 [版权说明](COPYRIGHT.md)。

## 相关课程

| 课程 | 适合谁 | 学习重点 |
| --- | --- | --- |
| [程序员 AI Coding 进阶实战](https://github.com/DavidDingXu/learn-ai-coding) | 已有开发经验的程序员 | 上下文、SDD、测试调试、Skill 与完整需求交付 |
| [AI Coding 团队化实战](README.md) | 技术负责人、架构师、研发效能团队 | 共享运行时、团队规则、验证治理与协作 |
| [Java AI 应用开发实战](https://github.com/DavidDingXu/learn-java-ai) | Java / Spring Boot 后端工程师 | 模型调用、RAG、受控 Agent 与生产接入 |

## 公众号

本课程来自[《AI Coding 团队化实战》专栏](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzYzNTkzMDY0NA==&action=getalbum&album_id=4524444444661940224#wechat_redirect)。

<img src="./img/wechat_official_qrcode.png" alt="微信公众号" width="180" />
