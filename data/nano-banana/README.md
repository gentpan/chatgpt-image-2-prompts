# ImgEdify Nano Banana Pro Prompts

**来源**: [ImgEdify/awesome-nano-banana-pro-prompts](https://github.com/ImgEdify/awesome-nano-banana-pro-prompts)  
**许可**: MIT  
**数量**: 8990 条提示词  
**导入日期**: 2026-08-23

## 文件说明

### imgedify-prompts.jsonl

完整语料的 JSONL 格式（14.89 MB），每行一个 JSON 对象。保留字段：

- `id`, `title`, `prompt`, `author`, `author_url`, `source_url`
- `language`, `category`, `tags`, `style`, `description`

已删除 `images` 等二进制引用字段。

### imgedify-cat-*.md

按 ImgEdify 原始分类拆分的 12 个 Markdown 文件，包含完整提示词文本：

| 分类 | 数量 | 文件大小 | CONJURE 槽位映射 |
|------|------|----------|------------------|
| portrait | 4398 | 7.95 MB | 人像 |
| product | 1132 | 1.43 MB | 产品 |
| character | 929 | 1.14 MB | 人像 |
| landscape | 572 | 0.70 MB | 常用 |
| other | 649 | 0.56 MB | - |
| (空) | 466 | 0.46 MB | - |
| architecture | 207 | 0.30 MB | 常用 |
| food | 257 | 0.29 MB | 产品 |
| abstract | 239 | 0.22 MB | 常用 |
| animal | 135 | 0.11 MB | 常用 |
| illustration | 4 | 0.00 MB | - |
| artistic | 2 | 0.00 MB | - |

**总计**: 8990 条

## 与 CONJURE 槽位的映射关系

本仓库暂不将这 8990 条提示词直接移动到 `prompts/` 目录。分类映射仅供参考：

- `portrait` + `character` → 人像 (5327 条)
- `product` + `food` → 产品 (1389 条)
- `landscape` + `architecture` + `abstract` + `animal` → 常用 (1153 条)
- 其他 (1121 条)

用户可根据需要从分类文件中选取提示词，按 `CONTRIBUTING.md` 规范添加到 `prompts/` 目录。

## 许可声明

本数据来源于 ImgEdify/awesome-nano-banana-pro-prompts 仓库（MIT 许可）。使用时请遵守原仓库的 MIT 许可条款。
