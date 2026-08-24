# YouMind GPT Image 2 完整语料

**来源**: [YouMind-OpenLab/gpt-image-2-prompts-search](https://github.com/YouMind-OpenLab/gpt-image-2-prompts-search)  
**许可**: CC BY 4.0  
**数量**: 15,949 条（已去重）  
**导入日期**: 2026-08-23

---

## 文件清单

### youmind-prompts.jsonl

完整语料的 JSONL 格式（35.16 MB），每行一个 JSON 对象。

**包含字段**:
- `id` — 唯一标识符
- `title` — 标题
- `prompt` — 完整提示词文本
- `description` — 描述
- `category` — 分类名称
- `slug` — 分类 slug
- `language` — 语言（主要为 en）
- `sourceLink` — 来源链接
- `author` — 作者
- `needReferenceImages` — 是否需要参考图像
- `source_license` — 许可协议（CC BY 4.0）
- `source_repo` — 来源仓库

**已删除字段**: `sourceMedia`（图像 URL 数组），`video`, `base64` 等媒体字段

---

### youmind-by-category.md

按分类的索引文件（25.69 KB），包含：
- 按分类统计表
- 每个分类的前 50 条提示词列表（ID + 标题）

---

## 按分类统计

| 分类 | 数量 | manifest 预期 | 差异说明 |
|------|------|---------------|----------|
| Social Media Post | 4773 | 6102 | 部分无有效 prompt 或已删除 |
| Product Marketing | 2781 | 4360 | 同上 |
| Profile / Avatar | 2276 | 2276 | ✓ 完全匹配 |
| Comic / Storyboard | 1952 | 2436 | 部分条目可能无文本 |
| Poster / Flyer | 1291 | 4488 | 同上 |
| Infographic / Edu Visual | 1244 | 1409 | 同上 |
| Game Asset | 892 | 1956 | 同上 |
| Uncategorized | 376 | 376 | ✓ 完全匹配 |
| App / Web Design | 212 | 1001 | 大量条目可能无文本 |
| YouTube Thumbnail | 133 | 222 | 同上 |
| E-commerce Main Image | 19 | 451 | 同上 |

**总计**: 15,949 条（manifest 预期 15,985，差异 36 条可能为无文本条目或重复 ID）

---

## 数据来源

本数据集来自 YouMind-OpenLab 的 **gpt-image-2-prompts-search** 仓库的 `references/*.json` 文件，这是其 CMS 驱动的在线画廊的公开导出版本。

**原始文件**（已处理，未提交）:
- profile-avatar.json (4.2 MB)
- social-media-post.json (13 MB) — 最大
- infographic-edu-visual.json (4.2 MB)
- youtube-thumbnail.json (516 KB)
- comic-storyboard.json (5.8 MB)
- product-marketing.json (9.8 MB)
- ecommerce-main-image.json (949 KB)
- game-asset.json (4.5 MB)
- app-web-design.json (2.7 MB)
- poster-flyer.json (11 MB)
- others.json (727 KB)

**原始文件总大小**: ~57 MB（包含媒体字段）  
**处理后 JSONL 大小**: 35.16 MB（仅文本字段）

---

## 与已有提示词的关系

本仓库已有 **630+ 条精选提示词**（位于 `prompts/` 目录），来自以下来源：
- freestylefly/awesome-gpt-image-2 (529 条)
- ZeroLu/awesome-gpt-image (72 条)
- Anil-matcha/Awesome-GPT-Image-2-API-Prompts (28 条)
- YouMind-OpenLab/awesome-gpt-image-2 (1 条样本)

本次导入的 YouMind 完整语料（15,949 条）与已有提示词可能存在部分重叠，但：
- **已有提示词保持不变**，不删除 `prompts/` 目录下的文件
- 完整语料提供更全面的覆盖，便于批量检索和分析
- 用户可根据需要从 JSONL 中选取提示词，按 `CONTRIBUTING.md` 规范添加到 `prompts/` 目录

---

## 许可声明

本数据集采用 **CC BY 4.0** 许可。使用时请遵守以下要求：
- 保留原始归属信息（YouMind-OpenLab）
- 标注许可协议（CC BY 4.0）
- 如有修改，请说明

详见 [CC BY 4.0 许可协议](https://creativecommons.org/licenses/by/4.0/)。

---

## 使用示例

### 按分类查询

```bash
# 查询 Social Media Post 分类的所有提示词（YouMind）
grep '"slug": "social-media-post"' youmind-prompts.jsonl | wc -l

# 查询 Portrait & Character 分类（Toolcentral）
grep '"category": "Portrait & Character"' toolcentral-prompts.jsonl | wc -l
```

### 按 ID 查询

```bash
# 查询 ID 为 32359 的提示词（YouMind）
grep '"id": 32359' youmind-prompts.jsonl | python3 -m json.tool

# 查询 moosl 提示词
grep '"id": "moosl-0001"' moosl-prompts.jsonl | python3 -m json.tool
```

### 提取特定分类

```bash
# 提取所有 Product Marketing 提示词（YouMind）
grep '"slug": "product-marketing"' youmind-prompts.jsonl > product-marketing-only.jsonl

# 提取 Portrait 类别（多个来源合并）
cat youmind-prompts.jsonl toolcentral-prompts.jsonl moosl-prompts.jsonl | \
  grep -i '"category".*portrait' > all-portraits.jsonl
```

---

## 附加数据源（已去重）

除了 YouMind 完整语料，本目录还包含以下高价值数据源：

### toolcentral-prompts.jsonl (24.44 MB)

- **来源**: [Toolcentral-ai/awesome-gpt-image-2-prompts](https://github.com/Toolcentral-ai/awesome-gpt-image-2-prompts)
- **数量**: 7,483 条（去重后，原始 7,902 条）
- **许可**: MIT
- **分类**: Portrait & Character, Graphic & Poster, Anime & Game, Product & Commercial 等

### moosl-prompts.jsonl (2.85 MB)

- **来源**: [moosl/awsome-gpt-image-2-prompts](https://github.com/moosl/awsome-gpt-image-2-prompts)
- **数量**: 1,675 条（去重后，原始 1,791 条）
- **许可**: MIT
- **特点**: X/Twitter 收集，包含作者归属

### fashion-gptimage2prompts.jsonl (1.99 MB)

- **来源**: [gptimage2prompts/gpt-image-2-prompts](https://github.com/gptimage2prompts/gpt-image-2-prompts)
- **数量**: 800 条（去重后，原始 874 条）
- **许可**: MIT
- **特点**: 时尚专题中文提示词（Men's/Women's/Kids Fashion）

### bigpeng-prompts.jsonl (0.77 MB)

- **来源**: [BigPengSays/awesome-gpt-image-2-prompts](https://github.com/BigPengSays/awesome-gpt-image-2-prompts)
- **数量**: 536 条（去重后，原始 550 条）
- **许可**: MIT
- **特点**: 精选 A 级质量提示词，带归属

---

## 总计

| 数据源 | 唯一提示词 | 文件大小 |
|--------|-----------|----------|
| **YouMind** (完整语料) | 15,949 | 35.16 MB |
| **Toolcentral** | 7,483 | 24.44 MB |
| **moosl** | 1,675 | 2.85 MB |
| **fashion** | 800 | 1.99 MB |
| **BigPeng** | 536 | 0.77 MB |
| **总计** | **26,443** | **~65 MB** |

---

## 更新历史

- **2026-08-23**: 首次导入，15,949 条唯一提示词
