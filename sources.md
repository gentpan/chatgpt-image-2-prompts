# 数据源索引

本文档记录已索引的公开 GPT Image 2 提示词来源，仅保留元信息和链接，**不批量复制完整提示词内容**。

---

## 1. YouMind-OpenLab/awesome-gpt-image-2

- **仓库**: [YouMind-OpenLab/awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2)
- **描述**: CMS 驱动的在线画廊，约 15985 个案例，Git 仓库为预览版
- **许可**: CC BY 4.0
- **在本仓库的角色**: 外部语料索引，不直接导入

---

## 2. freestylefly/awesome-gpt-image-2

- **仓库**: [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2)
- **描述**: 529 个结构化案例（上游 [data/cases.json](https://raw.githubusercontent.com/freestylefly/awesome-gpt-image-2/main/data/cases.json)）+ 22 个模板
- **许可**: MIT
- **在本仓库的角色**: 
  - 通过 CSV 索引：`data/freestylefly-cases.csv` 和 `data/freestylefly-cases-by-category.md`
  - 仅元信息索引（ID、分类、标题、标签），未包含完整提示词文本
  - 可根据此索引选择性精选至 `prompts/` 目录

---

## 3. ZeroLu/awesome-gpt-image

- **仓库**: [ZeroLu/awesome-gpt-image](https://github.com/ZeroLu/awesome-gpt-image)
- **描述**: 约 73 个精选案例，以 README 形式展示
- **许可**: MIT（README 中同时声明 CC BY，以仓库 LICENSE 为准）
- **在本仓库的角色**: 外部语料索引，可按需选择性精选

---

## 4. Anil-matcha/Awesome-GPT-Image-2-API-Prompts

- **仓库**: [Anil-matcha/Awesome-GPT-Image-2-API-Prompts](https://github.com/Anil-matcha/Awesome-GPT-Image-2-API-Prompts)
- **描述**: 49 个面向 API 调用的提示词，与 ZeroLu 仓库有重叠
- **许可**: 未明确声明（需谨慎标注）
- **在本仓库的角色**: 外部语料索引，适合 API 集成场景参考

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

## 使用建议

1. **查阅分类统计**: 参见 `data/freestylefly-cases-by-category.md` 快速浏览 freestylefly 的 529 个案例
2. **精选至 prompts/**: 从上述来源选择高质量提示词，按 [CONTRIBUTING.md](CONTRIBUTING.md) 规范录入
3. **标注原始许可**: 务必在 YAML front matter 中记录 `source_license`，不得改写他人提示词的许可协议
