# 数据源索引

本文档记录本仓库收集提示词的公开来源。所有提示词均保留原始许可和归属信息。

---

## GPT Image 2 数据源

## 1. YouMind-OpenLab/gpt-image-2-prompts-search

- **仓库**: [YouMind-OpenLab/gpt-image-2-prompts-search](https://github.com/YouMind-OpenLab/gpt-image-2-prompts-search)
- **描述**: 15,949 个结构化提示词，来自上游 references/*.json（11 个分类文件）
- **许可**: CC BY 4.0
- **在本仓库的角色**: 
  - 已导入全部 15,949 个唯一提示词至 `data/gpt-image-2/` 目录
  - JSONL 格式（35.16 MB，仅文本字段）+ 分类索引 MD
  - 原始 JSON 文件总大小 ~57 MB（包含媒体字段），已删除媒体字段
  - 11 个分类：Social Media Post (4773), Product Marketing (2781), Profile/Avatar (2276) 等

---

## 2. freestylefly/awesome-gpt-image-2

- **仓库**: [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2)
- **描述**: 529 个结构化案例（上游 [data/cases.json](https://raw.githubusercontent.com/freestylefly/awesome-gpt-image-2/main/data/cases.json)）+ 22 个模板
- **许可**: MIT
- **在本仓库的角色**: 
  - 已导入全部 529 个案例至 `prompts/` 目录（按槽位分类）
  - CSV 索引：`data/freestylefly-cases.csv` 和 `data/freestylefly-cases-by-category.md`
  - 每个案例独立 Markdown 文件，包含完整提示词文本

---

## 3. ZeroLu/awesome-gpt-image

- **仓库**: [ZeroLu/awesome-gpt-image](https://github.com/ZeroLu/awesome-gpt-image)
- **描述**: 约 73 个精选案例，以 README 形式展示
- **许可**: MIT（README 中同时声明 CC BY，以仓库 LICENSE 为准）
- **在本仓库的角色**: 已导入全部 72 个精选提示词至 `prompts/` 目录

---

## 4. Anil-matcha/Awesome-GPT-Image-2-API-Prompts

- **仓库**: [Anil-matcha/Awesome-GPT-Image-2-API-Prompts](https://github.com/Anil-matcha/Awesome-GPT-Image-2-API-Prompts)
- **描述**: 49 个面向 API 调用的提示词，与 ZeroLu 仓库有重叠
- **许可**: 未明确声明（需谨慎标注）
- **在本仓库的角色**: 已导入 28 个独特提示词（与 ZeroLu 去重后），适合 API 集成场景

---

## 5. kadevin/ilab-conjure

- **仓库**: [kadevin/ilab-conjure](https://github.com/kadevin/ilab-conjure)
- **描述**: GPT Image 2 工作台，定义六个功能槽位模板（常用/人像/产品/修复/海报/电商）
- **许可**: AGPLv3
- **在本仓库的角色**: 
  - **消费者而非语料库**
  - 提供槽位分类标准，本仓库的 `prompts/` 目录结构对齐其六个槽位
  - 本仓库不导入其代码，仅参考其分类体系

---

---

---

## Nano Banana 数据源

### 6. ImgEdify/awesome-nano-banana-pro-prompts

- **仓库**: [ImgEdify/awesome-nano-banana-pro-prompts](https://github.com/ImgEdify/awesome-nano-banana-pro-prompts)
- **描述**: 8990 个结构化提示词，来自上游 [data/prompts.json](https://raw.githubusercontent.com/ImgEdify/awesome-nano-banana-pro-prompts/main/data/prompts.json)
- **许可**: MIT
- **在本仓库的角色**: 
  - 已导入全部 8990 个有效提示词至 `data/nano-banana/` 目录
  - JSONL 格式（14.89 MB）+ 按分类拆分的 12 个 Markdown 文件
  - 最大分类 portrait（4398 条），product（1132 条）
  - **未写入 images 等二进制引用字段**

---

### 7. ZeroLu/awesome-nanobanana-pro

- **仓库**: [ZeroLu/awesome-nanobanana-pro](https://github.com/ZeroLu/awesome-nanobanana-pro)
- **描述**: 70 个精选案例，以 README 形式展示
- **许可**: MIT
- **在本仓库的角色**: 已导入全部 70 个提示词至 `data/nano-banana/zerolu-awesome-nanobanana-pro.md`

---

### 8. YouMind-OpenLab/awesome-nano-banana-pro-prompts

- **仓库**: [YouMind-OpenLab/awesome-nano-banana-pro-prompts](https://github.com/YouMind-OpenLab/awesome-nano-banana-pro-prompts)
- **描述**: CMS 驱动的在线画廊，约 10000+ 个案例，Git 仓库为预览版
- **许可**: CC BY 4.0
- **在本仓库的角色**: 
  - 已导入 GitHub README 预览切片的 129 条提示词至 `data/nano-banana/youmind-nanobanana-preview.md`
  - 完整集合约 10000+ 条，仅在 [youmind.com](https://youmind.com) 可见（CMS 驱动）

---

---

## Grok Imagine 数据源

### 9. that-cod/awesome-grok-imagine-prompts

- **仓库**: [that-cod/awesome-grok-imagine-prompts](https://github.com/that-cod/awesome-grok-imagine-prompts)
- **描述**: 200+ 个结构化提示词，涵盖 12 个分类
- **许可**: MIT
- **在本仓库的角色**: 
  - 已导入 199 条 SFW 提示词至 `data/grok/that-cod-awesome-grok-imagine.md`
  - **已排除 nsfw.md**，仅收录 SFW 内容

---

### 10. seaimagine/awesome-grok-imagine-1-5-prompts

- **仓库**: [seaimagine/awesome-grok-imagine-1-5-prompts](https://github.com/seaimagine/awesome-grok-imagine-1-5-prompts)
- **描述**: 40 个原创提示词，8 个分类
- **许可**: MIT
- **在本仓库的角色**: 已导入全部 40 个提示词至 `data/grok/seaimagine-grok-1-5.md`

---

### 11. YouMind-OpenLab/awesome-grok-imagine-prompts

- **仓库**: [YouMind-OpenLab/awesome-grok-imagine-prompts](https://github.com/YouMind-OpenLab/awesome-grok-imagine-prompts)
- **描述**: CMS 驱动的在线画廊，约 2573+ 个案例，Git 仓库为预览版
- **许可**: CC BY 4.0
- **在本仓库的角色**: 
  - 已导入 GitHub README 预览切片的 3 条精选提示词至 `data/grok/youmind-grok-prompts-preview.md`
  - 完整集合约 2573+ 条，仅在 [youmind.com/grok-imagine-prompts](https://youmind.com/grok-imagine-prompts) 可见（CMS 驱动）

---

---

## 使用建议

1. **浏览目录**: 按槽位浏览 `prompts/<分类>/` 查找所需提示词
2. **查阅索引**: 参见 `data/freestylefly-cases-by-category.md` 快速查找 freestylefly 的 529 个案例
3. **遵守许可**: 使用前务必查阅各文件 YAML front matter 中的 `source_license` 字段

## 附加 GPT Image 2 数据源（高价值补充）

### 12. Toolcentral-ai/awesome-gpt-image-2-prompts

- **仓库**: [Toolcentral-ai/awesome-gpt-image-2-prompts](https://github.com/Toolcentral-ai/awesome-gpt-image-2-prompts)
- **描述**: 7,902 个结构化提示词，来自 data/gpt-image-2-prompts.json（64 MB 原始文件）
- **许可**: MIT
- **在本仓库的角色**:
  - 已导入 7,483 条唯一提示词至 `data/gpt-image-2/toolcentral-prompts.jsonl`（24.44 MB）
  - 与 YouMind 去重后跳过 419 条
  - 10 个分类：Portrait & Character (1835), Graphic & Poster (1557), Anime & Game (1379) 等

---

### 13. moosl/awsome-gpt-image-2-prompts

- **仓库**: [moosl/awsome-gpt-image-2-prompts](https://github.com/moosl/awsome-gpt-image-2-prompts)
- **描述**: 1,791 个 X/Twitter 收集的提示词，独立于 freestylefly
- **许可**: MIT
- **在本仓库的角色**:
  - 已导入 1,675 条唯一提示词至 `data/gpt-image-2/moosl-prompts.jsonl`（2.85 MB）
  - 去重后跳过 116 条
  - 包含作者归属（@image2hub, @TechieBySA 等）

---

### 14. gptimage2prompts/gpt-image-2-prompts

- **仓库**: [gptimage2prompts/gpt-image-2-prompts](https://github.com/gptimage2prompts/gpt-image-2-prompts)
- **描述**: 874 个时尚专题中文提示词（Men's/Women's/Kids Fashion）
- **许可**: MIT
- **在本仓库的角色**:
  - 已导入 800 条唯一提示词至 `data/gpt-image-2/fashion-gptimage2prompts.jsonl`（1.99 MB）
  - 去重后跳过 74 条
  - 3 个分类：Men's Fashion (517), Women's Fashion (176), Kids Fashion (107)

---

### 15. BigPengSays/awesome-gpt-image-2-prompts

- **仓库**: [BigPengSays/awesome-gpt-image-2-prompts](https://github.com/BigPengSays/awesome-gpt-image-2-prompts)
- **描述**: 550 个精选提示词，带质量评级和归属
- **许可**: MIT
- **在本仓库的角色**:
  - 已导入 536 条唯一提示词至 `data/gpt-image-2/bigpeng-prompts.jsonl`（0.77 MB）
  - 去重后跳过 12 条
  - 全部为 A 级质量

---

---

## 附加 Nano Banana 数据源

### 16. Banana-Prompts/awesome-nano-banana-prompts

- **仓库**: [Banana-Prompts/awesome-nano-banana-prompts](https://github.com/Banana-Prompts/awesome-nano-banana-prompts)
- **描述**: 294 个精选 Nano Banana Pro 提示词，来自 bananaprompts.fun
- **许可**: MIT
- **在本仓库的角色**:
  - 已导入 276 条唯一提示词至 `data/nano-banana/banana-prompts.jsonl`（0.29 MB）
  - 与 ImgEdify 等去重后跳过 18 条
  - 14 个分类：Portrait, Landscape, Architecture, Sci-Fi 等

---

## 使用建议

1. **浏览目录**: 按槽位浏览 `prompts/<分类>/` 查找所需提示词
2. **查阅索引**: 参见 `data/` 目录下的 README 和 JSONL 文件
3. **批量检索**: 使用 `grep` 命令在 JSONL 文件中搜索关键词
4. **遵守许可**: 使用前务必查阅各文件的 `source_license` 字段
