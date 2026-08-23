# GPT Image 2 提示词收藏库

Yep 的 ChatGPT GPT Image 2 提示词个人收藏，为后续项目复用而整理。**包含完整提示词文本**，严格标注来源和原始许可。

## 仓库结构

本仓库存储完整的提示词内容，按六个运行时槽位分类管理：

### 提示词文件

位于 `prompts/<分类>/`，每个提示词独立存为 Markdown 文件：

- 采用 YAML front matter 记录完整元信息
- **包含完整提示词正文**，可直接用于项目
- **严格标注来源和原始许可**，不改写他人提示词的许可协议
- 分类对齐 iLab CONJURE 工作台的六个槽位

### 索引数据

位于 `data/` 和 `sources.md`：

- `data/freestylefly-cases.csv` — freestylefly 仓库 529 个案例的元信息索引
- `data/freestylefly-cases-by-category.md` — 按分类汇总统计
- `sources.md` — 数据源清单及其许可信息

### 运行时槽位

对应 [kadevin/ilab-conjure](https://github.com/kadevin/ilab-conjure) 的六个功能槽位：

| 槽位 | 数量 | 说明 |
|------|------|------|
| `prompts/常用/` | 327 | 通用场景、UI、游戏、图表等 |
| `prompts/人像/` | 85 | 人物肖像、角色 |
| `prompts/产品/` | 36 | 产品摄影 |
| `prompts/修复/` | 100 | 图像修复/编辑/风格转换 |
| `prompts/海报/` | 82 | 海报设计、排版 |
| `prompts/电商/` | 0 | 电商视觉（待补充） |

待分类的提示词暂存在 `prompts/_inbox/`。

**总计**: 630+ 个精选提示词

## 数据来源

本仓库从以下公开来源收集并整理提示词：

- **freestylefly/awesome-gpt-image-2** (MIT) — 529 个案例
- **ZeroLu/awesome-gpt-image** (MIT) — 72 个精选提示词
- **Anil-matcha/Awesome-GPT-Image-2-API-Prompts** (CC BY 4.0) — 28 个 API 导向提示词（已去重）
- **YouMind-OpenLab/awesome-gpt-image-2** (CC BY 4.0) — 1 个样本（完整集合约 15985 个，见 [youmind.com](https://youmind.com)）

详细来源信息参见 [sources.md](sources.md)。

## 如何使用

1. 浏览 `prompts/<槽位>/` 目录查找所需提示词
2. 阅读文件 YAML front matter 了解元信息
3. 复制提示词正文用于你的项目
4. **务必遵守原始许可协议**（见 `source_license` 字段）

## 如何贡献

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
