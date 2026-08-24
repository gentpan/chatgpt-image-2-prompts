# chatgpt-image-2-prompts Schema

本仓库采用标准化的文件结构来组织 GPT Image 2 提示词库。

## 目录结构

```
prompts/
  ├── 电商/
  │   ├── 0001.md
  │   ├── 0002.md
  │   └── ...
  ├── 人像/
  ├── 产品/
  ├── 海报/
  ├── 常用/
  └── 修复/
data/
  └── *.jsonl    (批量语料库)
```

## 文件命名规则

- 每个类别目录下的文件使用 **4位数字编号**：`0001.md`, `0002.md`, `0003.md`, ...
- 每个类别独立编号，从 `0001` 开始
- 零填充确保文件排序一致

## Markdown 文件格式

每个 `.md` 文件包含一个双语提示词，格式如下：

```markdown
---
id: 电商-0001
category: 电商
model: gpt-image-2
source_repo: owner/repo-name
source_url: https://github.com/owner/repo-name
source_license: MIT / CC BY 4.0 / etc.
organizer: gentpan
---

## 中文

\`\`\`
中文提示词内容
\`\`\`

## English

\`\`\`
English prompt content
\`\`\`
```

### 字段说明

| 字段 | 说明 | 必填 |
|------|------|------|
| `id` | 唯一标识符，格式：`类别-编号` | ✓ |
| `category` | 所属类别（电商/人像/产品/海报/常用/修复等） | ✓ |
| `model` | 模型名称（通常为 `gpt-image-2`） | ✓ |
| `source_repo` | 来源仓库（GitHub 格式：owner/repo） | 可选 |
| `source_url` | 来源 URL | 可选 |
| `source_license` | 来源许可证 | 可选 |
| `organizer` | 整理人员（gentpan） | ✓ |

### 内容规则

1. **双语必备**：每个提示词必须同时包含中文和英文版本
2. **纯提示词**：内容区域只包含提示词本身，不包含：
   - 图片链接或嵌入
   - 解释性注释
   - Emoji 表情（除非提示词本身需要）
   - 其他语言（日语/韩语等需翻译为中英文）
3. **语言处理**：
   - 如果原始提示词为日语/韩语/其他语言，翻译为**中文和英文**双语
   - 如果只有单一语言，补充翻译另一种语言

## JSONL 语料库格式

`data/` 目录下的 `.jsonl` 文件用于存储批量提示词语料，每行一个 JSON 对象：

```jsonl
{"id":"电商-0001","category":"电商","model":"gpt-image-2","prompt_zh":"中文提示词","prompt_en":"English prompt","source_repo":"owner/repo","source_url":"https://...","source_license":"MIT","organizer":"gentpan"}
```

### 使用场景

- **Markdown 文件**：精选整理的编号提示词库（便于浏览和引用）
- **JSONL 文件**：批量语料（用于数据分析、批量处理、API 调用等）

## 示例

### 电商类别示例

**文件**：`prompts/电商/0001.md`

```markdown
---
id: 电商-0001
category: 电商
model: gpt-image-2
source_repo: YouMind-OpenLab/gpt-image-2-prompts-search
source_url: https://github.com/YouMind-OpenLab/gpt-image-2-prompts-search
source_license: CC BY 4.0
organizer: gentpan
---

## 中文

\`\`\`
创作一张逼真的日式炸猪排特写美食照片...
\`\`\`

## English

\`\`\`
Create a realistic close-up food photograph of Japanese tonkatsu...
\`\`\`
```

## 贡献指南

向本仓库添加新提示词时：

1. 确定类别（电商/人像/产品等）
2. 使用下一个可用编号（如 `0031.md`）
3. 按照上述格式创建 Markdown 文件
4. 确保中英文提示词完整且准确
5. 注明来源信息（如有）

---

整理：gentpan  
仓库：https://github.com/gentpan/chatgpt-image-2-prompts
