# 数据源索引

本文档记录本仓库收集 **GPT Image 2** 提示词的公开来源。所有提示词均保留原始许可和归属信息。

> **其他模型提示词**：  
> - Nano Banana 提示词收藏 → [gentpan/nano-banana-prompts](https://github.com/gentpan/nano-banana-prompts)  
> - Grok Imagine 提示词收藏 → [gentpan/grok-imagine-prompts](https://github.com/gentpan/grok-imagine-prompts)

---

## GPT Image 2 数据源

### 1. YouMind-OpenLab/gpt-image-2-prompts-search（完整语料）

- **仓库**: [YouMind-OpenLab/gpt-image-2-prompts-search](https://github.com/YouMind-OpenLab/gpt-image-2-prompts-search)
- **描述**: 15,949 个结构化提示词，来自上游 references/*.json（11 个分类文件）
- **许可**: CC BY 4.0
- **在本仓库的角色**: 
  - 已导入全部 15,949 个唯一提示词至 `data/gpt-image-2/` 目录
  - JSONL 格式（35.16 MB，仅文本字段）+ 分类索引 MD
  - 原始 JSON 文件总大小 ~57 MB（包含媒体字段），已删除媒体字段
  - 11 个分类：Social Media Post (4773), Product Marketing (2781), Profile/Avatar (2276) 等

---

### 1b. YouMind-OpenLab/gpt-image-2-prompts-search（电商精选）

- **仓库**: 同上
- **描述**: GPT Image 2 提示词搜索引擎的数据源，包含电商主图、产品营销等结构化提示词集合
- **许可**: CC BY 4.0
- **在本仓库的角色**: 
  - 已导入 1,508 个电商相关提示词至 `prompts/电商/` 目录
  - 数据来源：
    - `references/ecommerce-main-image.json` — 452 个电商主图提示词
    - `references/product-marketing.json` — 1,056 个产品营销提示词（已过滤电商相关）
  - 完整数据集：`data/ecommerce/gpt-image-2.jsonl`
  - 精选展示：30 个代表性提示词分布在 `prompts/电商/主图|包装|详情页|模特上身|场景种草|静物白底/`

---

### 2. freestylefly/awesome-gpt-image-2

- **仓库**: [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2)
- **描述**: 529 个结构化案例（上游 [data/cases.json](https://raw.githubusercontent.com/freestylefly/awesome-gpt-image-2/main/data/cases.json)）+ 22 个模板
- **许可**: MIT
- **在本仓库的角色**: 
  - 已导入全部 529 个案例至 `prompts/` 目录（按槽位分类）
  - CSV 索引：`data/freestylefly-cases.csv` 和 `data/freestylefly-cases-by-category.md`
  - 每个案例独立 Markdown 文件，包含完整提示词文本

---

### 3. ZeroLu/awesome-gpt-image

- **仓库**: [ZeroLu/awesome-gpt-image](https://github.com/ZeroLu/awesome-gpt-image)
- **描述**: 约 73 个精选案例，以 README 形式展示
- **许可**: MIT（README 中同时声明 CC BY，以仓库 LICENSE 为准）
- **在本仓库的角色**: 已导入全部 72 个精选提示词至 `prompts/` 目录

---

### 4. Anil-matcha/Awesome-GPT-Image-2-API-Prompts

- **仓库**: [Anil-matcha/Awesome-GPT-Image-2-API-Prompts](https://github.com/Anil-matcha/Awesome-GPT-Image-2-API-Prompts)
- **描述**: 49 个面向 API 调用的提示词，与 ZeroLu 仓库有重叠
- **许可**: 未明确声明（需谨慎标注）
- **在本仓库的角色**: 已导入 28 个独特提示词（与 ZeroLu 去重后），适合 API 集成场景

---

### 5. kadevin/ilab-conjure

- **仓库**: [kadevin/ilab-conjure](https://github.com/kadevin/ilab-conjure)
- **描述**: GPT Image 2 工作台，定义六个功能槽位模板（常用/人像/产品/修复/海报/电商）
- **许可**: AGPLv3
- **在本仓库的角色**: 
  - **消费者而非语料库**
  - 提供槽位分类标准，本仓库的 `prompts/` 目录结构对齐其六个槽位
  - 本仓库不导入其代码，仅参考其分类体系

---

---

## 附加 GPT Image 2 数据源（高价值补充）

### 6. Toolcentral-ai/awesome-gpt-image-2-prompts

- **仓库**: [Toolcentral-ai/awesome-gpt-image-2-prompts](https://github.com/Toolcentral-ai/awesome-gpt-image-2-prompts)
- **描述**: 7,902 个结构化提示词，来自 data/gpt-image-2-prompts.json（64 MB 原始文件）
- **许可**: MIT
- **在本仓库的角色**:
  - 已导入 7,483 条唯一提示词至 `data/gpt-image-2/toolcentral-prompts.jsonl`（24.44 MB）
  - 与 YouMind 去重后跳过 419 条
  - 10 个分类：Portrait & Character (1835), Graphic & Poster (1557), Anime & Game (1379) 等

---

### 7. moosl/awsome-gpt-image-2-prompts

- **仓库**: [moosl/awsome-gpt-image-2-prompts](https://github.com/moosl/awsome-gpt-image-2-prompts)
- **描述**: 1,791 个 X/Twitter 收集的提示词，独立于 freestylefly
- **许可**: MIT
- **在本仓库的角色**:
  - 已导入 1,675 条唯一提示词至 `data/gpt-image-2/moosl-prompts.jsonl`（2.85 MB）
  - 去重后跳过 116 条
  - 包含作者归属（@image2hub, @TechieBySA 等）

---

### 8. gptimage2prompts/gpt-image-2-prompts

- **仓库**: [gptimage2prompts/gpt-image-2-prompts](https://github.com/gptimage2prompts/gpt-image-2-prompts)
- **描述**: 874 个时尚专题中文提示词（Men's/Women's/Kids Fashion）
- **许可**: MIT
- **在本仓库的角色**:
  - 已导入 800 条唯一提示词至 `data/gpt-image-2/fashion-gptimage2prompts.jsonl`（1.99 MB）
  - 去重后跳过 74 条
  - 3 个分类：Men's Fashion (517), Women's Fashion (176), Kids Fashion (107)

---

### 9. BigPengSays/awesome-gpt-image-2-prompts

- **仓库**: [BigPengSays/awesome-gpt-image-2-prompts](https://github.com/BigPengSays/awesome-gpt-image-2-prompts)
- **描述**: 550 个精选提示词，带质量评级和归属
- **许可**: MIT
- **在本仓库的角色**:
  - 已导入 536 条唯一提示词至 `data/gpt-image-2/bigpeng-prompts.jsonl`（0.77 MB）
  - 去重后跳过 12 条
  - 全部为 A 级质量

---

---

## 使用建议

1. **浏览目录**: 按槽位浏览 `prompts/<分类>/` 查找所需提示词
2. **查阅索引**: 
   - freestylefly 案例：`data/freestylefly-cases-by-category.md`
   - 电商提示词：`data/ecommerce/gpt-image-2.jsonl`（1,508 条）
   - GPT Image 2 完整语料：`data/gpt-image-2/` 目录（26,443 条）
3. **批量检索**: 使用 `grep` 命令在 JSONL 文件中搜索关键词
4. **遵守许可**: 使用前务必查阅各文件的 `source_license` 字段
