#!/usr/bin/env python3
"""
生成精选电商提示词的 markdown 文件
"""

import json
from pathlib import Path
from collections import defaultdict
from typing import Dict

def sanitize_filename(text: str) -> str:
    """生成安全的文件名"""
    # 移除或替换特殊字符
    safe = text.replace('/', '-').replace('\\', '-').replace(':', '-')
    safe = safe.replace('"', '').replace("'", '').replace('?', '')
    # 限制长度
    return safe[:80]

def generate_markdown(prompt: dict, index: int) -> str:
    """为单个提示词生成 markdown 内容"""
    lines = [
        '---',
        f"id: {prompt['id']}",
        f"title: {prompt['title'] or '电商提示词'}",
        f"model: {prompt['model']}",
        f"category: 电商",
        f"bucket: {prompt['bucket']}",
    ]
    
    if prompt.get('description'):
        lines.append(f"description: {prompt['description']}")
    
    lines.extend([
        f"source_repo: {prompt['source_repo']}",
        f"source_url: {prompt['source_url']}",
        f"source_license: {prompt['source_license']}",
    ])
    
    if prompt.get('needs_reference'):
        lines.append('needs_reference: true')
    
    lines.extend([
        '---',
        '',
        f"# {prompt['title'] or '电商提示词'}",
        '',
    ])
    
    if prompt.get('description'):
        lines.extend([
            f"**说明**: {prompt['description']}",
            '',
        ])
    
    lines.extend([
        '## 提示词',
        '',
        '```',
        prompt['content'],
        '```',
        '',
    ])
    
    # 添加标签和元数据
    tags = [prompt['bucket'], '电商', prompt['model']]
    lines.extend([
        '---',
        '',
        f"**分类**: {prompt['bucket']}  ",
        f"**模型**: {prompt['model']}  ",
        f"**来源**: [{prompt['source_repo']}]({prompt['source_url']})  ",
        f"**许可**: {prompt['source_license']}  ",
    ])
    
    if prompt.get('needs_reference'):
        lines.append('**需要参考图**: 是  ')
    
    return '\n'.join(lines)

def main():
    base_dir = Path('/workspace')
    tmp_dir = base_dir / 'tmp' / 'sources'
    
    # 读取精选数据
    with open(tmp_dir / 'featured.json', 'r', encoding='utf-8') as f:
        featured = json.load(f)
    
    print(f"生成 {len(featured)} 个精选提示词的 markdown 文件...")
    
    # 按桶分组
    by_bucket = defaultdict(list)
    for prompt in featured:
        by_bucket[prompt['bucket']].append(prompt)
    
    # 为每个桶创建子目录
    prompts_dir = base_dir / 'prompts' / '电商'
    
    # 生成 markdown 文件
    for bucket, prompts in by_bucket.items():
        bucket_dir = prompts_dir / bucket
        bucket_dir.mkdir(parents=True, exist_ok=True)
        
        for idx, prompt in enumerate(prompts, 1):
            # 生成文件名
            title_part = sanitize_filename(prompt['title']) if prompt['title'] else f"prompt-{idx}"
            filename = f"{title_part}.md"
            
            # 避免文件名冲突
            filepath = bucket_dir / filename
            counter = 1
            while filepath.exists():
                filename = f"{title_part}-{counter}.md"
                filepath = bucket_dir / filename
                counter += 1
            
            # 生成并写入内容
            content = generate_markdown(prompt, idx)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
        
        print(f"  {bucket}: {len(prompts)} 个文件")
    
    print(f"\n所有 markdown 文件已生成到: {prompts_dir}")

if __name__ == '__main__':
    main()
