# 参与方式

这个仓库主要用于沉淀《AI Coding 团队化实战》专栏的 GitHub 版本。欢迎通过 Issue 或 Pull Request 反馈问题、补充案例和改进表达。

## 适合提交的内容

- 错别字、链接错误、格式问题。
- 文章中不准确或容易误解的表述。
- 来自真实团队实践的补充问题和案例。
- 能让文章更容易落地的目录、流程、数据结构或检查清单建议。

## 文章修改原则

- 保持实践导向，少写概念铺垫，多写可执行动作。
- 不绑定单一 AI Coding 工具，优先使用通用命名和可替换示例。
- 不把单个团队的实现写成唯一标准。
- 新增文章使用 `NN-topic.md` 命名，并同步更新 `README.md` 目录。

## 提交建议

提交 Pull Request 前，请确认：

- Markdown 链接可打开。
- 表格、代码块和 Mermaid 图在 GitHub 上可正常阅读。
- 修改范围聚焦，不顺手重写无关段落。

## 课程正文与导航

完整课程入口在 [课程目录](docs/course/README.md)。文章、插图或顺序调整后，同步该目录、`docs/course/catalog.json` 和受影响的前后章节导航。

在仓库根目录使用 Node.js 20 或更高版本运行：

```bash
node scripts/check-course.mjs
```

它核对全文数量、文章标题、实践入口、图片和仓库内链接。文案或图片修改运行此检查即可；涉及代码行为时，仍需执行相应项目测试。命令适用于 macOS、Windows 和 Linux。

贡献的文章与插图采用 CC BY-NC-SA 4.0，贡献的代码采用 PolyForm Noncommercial 1.0.0；详见 [许可说明](LICENSING.md)。

## 目录与内容维护

根目录保留 14 篇文章及其稳定链接；`docs/course/` 维护完整目录和章节清单；`site/`、`book/` 分别构建阅读站和电子书。

文章顺序和链接以 `docs/course/catalog.json` 为准，根目录 README 展示每篇文章。修改文章后运行课程检查；书稿编排与电子书构建见 [电子书维护说明](book/README.md)。
