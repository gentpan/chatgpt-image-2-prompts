# GPT Image 2 提示词收藏库

Yep 的 ChatGPT GPT Image 2 提示词个人收藏，为后续项目复用而整理。

## 仓库结构

本仓库采用三层模型管理提示词：

### 1. 公共语料层（Corpus）

位于 `data/` 和 `sources.md`，索引公开的 GPT Image 2 提示词来源：

- **不批量复制**完整提示词内容
- 保留元信息、链接和分类统计
- 参见 [sources.md](sources.md) 了解各数据源及其许可

### 2. 精选层（Curated）

位于 `prompts/<分类>/`，每个经审查的提示词独立存为 Markdown 文件：

- 采用 YAML front matter 记录元信息
- **严格标注来源和原始许可**，不改写他人提示词的许可协议
- 分类对齐 iLab CONJURE 工作台的六个槽位

### 3. 运行时槽位（Runtime Slots）

对应 [kadevin/ilab-conjure](https://github.com/kadevin/ilab-conjure) 的六个功能槽位：

- `prompts/常用/` — 通用场景
- `prompts/人像/` — 人物肖像
- `prompts/产品/` — 产品摄影
- `prompts/修复/` — 图像修复/编辑
- `prompts/海报/` — 海报设计
- `prompts/电商/` — 电商视觉

待分类的提示词暂存在 `prompts/_inbox/`。

## 如何添加提示词

1. 在对应分类目录下创建 Markdown 文件（或先放入 `_inbox/`）
2. 遵循 [CONTRIBUTING.md](CONTRIBUTING.md) 中的 YAML front matter 规范
3. **必须**标注 `source_repo`、`source_url` 和 `source_license`
4. 提交时说明提示词来源

## 许可声明

**本仓库骨架**（目录结构、README、CONTRIBUTING、.gitkeep 等）采用 MIT 许可，版权归 gentpan 所有（2026）。

**第三方提示词内容**保留其原始许可协议，**本仓库不重新授权他人的提示词**。使用前请查阅各提示词文件中的 `source_license` 字段。

参见 [LICENSE](LICENSE) 了解详情。

## 数据来源

参见 [sources.md](sources.md) 了解已索引的公开来源。
