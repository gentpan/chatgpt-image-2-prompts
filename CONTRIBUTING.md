# 贡献指南

## 提示词文件规范

每个提示词对应 `prompts/<分类>/` 下的一个 Markdown 文件，采用 YAML front matter 记录元信息。

### 文件命名

- 小写字母、数字、连字符
- 简短描述性名称，例如 `studio-still-life.md`、`portrait-soft-light.md`

### YAML Front Matter 字段

```yaml
---
id: 唯一标识符（建议用 slug 格式）
title_zh: 中文标题
title_en: 英文标题
category: 分类槽位（常用|人像|产品|修复|海报|电商）
tags:
  - 标签1
  - 标签2
model: gpt-image-2
mode: t2i  # t2i（文生图）| i2i（图生图）| edit（编辑）
source_repo: 来源仓库（如 freestylefly/awesome-gpt-image-2）
source_url: 原始链接（完整 URL）
source_license: 原始许可协议（如 MIT、CC BY 4.0）
---

提示词正文内容。
```

### 必填字段

- `id`、`title_zh`、`category`、`model`、`mode`
- **必须标注来源**：`source_repo`、`source_url`、`source_license`

### 分类槽位

对应 iLab CONJURE 工作台：

- `常用` — 通用场景
- `人像` — 人物肖像
- `产品` — 产品摄影
- `修复` — 图像修复/编辑
- `海报` — 海报设计
- `电商` — 电商视觉

暂未分类的提示词放入 `_inbox`。

## 许可协议注意事项

**关键原则**：本仓库不改写他人提示词的许可协议。

1. **记录原始许可**：在 `source_license` 字段如实标注来源许可
2. **不得声称为己有**：转录他人提示词时，保留原作者归属
3. **尊重 Copyleft**：若原提示词采用 AGPLv3、CC BY-SA 等 Copyleft 许可，衍生作品需遵循相同协议

## 提交流程

1. Fork 本仓库并创建新分支
2. 按规范添加 Markdown 文件
3. 提交 PR，说明提示词来源和许可信息
4. 等待审查合并
