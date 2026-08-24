#!/usr/bin/env python3
"""
整理电商类提示词：从 jsonl 转换为编号的双语 markdown 文件
"""
import json
import os
import re
from pathlib import Path

def translate_to_chinese(english_prompt):
    """
    将英文提示词翻译为中文
    注意：这是一个简化的翻译模板，实际应该使用更好的翻译
    """
    # 基础映射表
    translations = {
        "Create a": "创作一张",
        "Create an": "创作一张",
        "Generate a": "生成一张",
        "Generate an": "生成一张",
        "photorealistic": "超写实的",
        "high-end": "高端",
        "luxury": "奢华",
        "minimalist": "极简主义",
        "product photo": "产品摄影",
        "product shot": "产品照片",
        "studio lighting": "影棚灯光",
        "background": "背景",
        "centered": "居中",
        "composition": "构图",
        "perfume bottle": "香水瓶",
        "with": "带有",
        "and": "和",
    }
    
    # 这里返回一个占位符，表示需要翻译
    return "[需要人工翻译或使用翻译API]"

def create_markdown_file(item, file_num, output_dir):
    """
    创建编号的 markdown 文件
    """
    filename = f"{file_num:04d}.md"
    filepath = output_dir / filename
    
    # 构建 ID
    item_id = f"电商-{file_num:04d}"
    
    # 提取英文提示词
    english_prompt = item.get("content", "[未找到]")
    
    # 生成中文（这里先放占位符）
    chinese_prompt = "[待翻译]"
    
    # 如果标题中有中文内容，可以尝试提取
    title = item.get("title", "")
    
    # 生成 YAML frontmatter
    yaml_lines = [
        "---",
        f"id: {item_id}",
        f"category: {item.get('category', '电商')}",
        f"model: {item.get('model', 'gpt-image-2')}",
    ]
    
    if item.get("source_repo"):
        yaml_lines.append(f"source_repo: {item['source_repo']}")
    if item.get("source_url"):
        yaml_lines.append(f"source_url: {item['source_url']}")
    if item.get("source_license"):
        yaml_lines.append(f"source_license: {item['source_license']}")
    
    yaml_lines.append("organizer: Yep (gentpan)")
    yaml_lines.append("---")
    
    # 构建完整内容
    content = "\n".join(yaml_lines) + "\n\n"
    content += "## 中文\n\n```\n"
    content += chinese_prompt + "\n"
    content += "```\n\n"
    content += "## English\n\n```\n"
    content += english_prompt + "\n"
    content += "```\n"
    
    return filename, content

def main():
    # 路径设置
    base_dir = Path("/workspace")
    jsonl_file = base_dir / "data" / "ecommerce" / "gpt-image-2.jsonl"
    output_dir = base_dir / "prompts" / "电商"
    
    # 读取 jsonl
    items = []
    with open(jsonl_file, "r", encoding="utf-8") as f:
        for line in f:
            items.append(json.loads(line.strip()))
    
    print(f"共读取 {len(items)} 条记录")
    
    # 生成前 60 个文件（0001-0060）
    for i in range(60):
        if i < len(items):
            item = items[i]
            filename, content = create_markdown_file(item, i + 1, output_dir)
            
            filepath = output_dir / filename
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            
            print(f"创建: {filename} - {item.get('title', 'N/A')}")
        else:
            break

if __name__ == "__main__":
    main()
