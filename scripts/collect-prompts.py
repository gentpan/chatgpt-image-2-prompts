#!/usr/bin/env python3
"""
收集 GPT Image 2 提示词数据
从 GitHub 仓库下载并转换为 JSONL 格式
"""
import json
import hashlib
import requests
import sys
from datetime import datetime
from pathlib import Path

def hash_prompt(text):
    """计算提示词的 SHA256 哈希"""
    return hashlib.sha256(text.encode('utf-8')).hexdigest()[:16]

def detect_language(text):
    """简单的语言检测"""
    if not text:
        return "unknown"
    # 检查是否包含中文字符
    chinese_chars = sum(1 for c in text if '\u4e00' <= c <= '\u9fff')
    if chinese_chars > len(text) * 0.3:
        return "zh"
    return "en"

def download_json(url):
    """下载 JSON 文件"""
    try:
        print(f"下载: {url}", file=sys.stderr)
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"下载失败 {url}: {e}", file=sys.stderr)
        return None

def process_evolinkai():
    """处理 EvoLinkAI/awesome-gpt-image-2-API-and-Prompts"""
    records = []
    base_url = "https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts/main"
    
    # 尝试多个数据文件
    files = [
        "data/curation_report_2026-06-08.json",
        "data/curation_report_2026-06-07.json",
        "data/curation_report_2026-06-02.json",
    ]
    
    for file in files:
        data = download_json(f"{base_url}/{file}")
        if not data:
            continue
        
        # 根据实际数据结构提取提示词
        if isinstance(data, list):
            for item in data:
                if isinstance(item, dict) and 'prompt' in item:
                    prompt_text = item.get('prompt', '')
                    if prompt_text:
                        records.append({
                            'id': hash_prompt(prompt_text),
                            'title': item.get('title', '')[:100],
                            'prompt': prompt_text,
                            'lang_guess': detect_language(prompt_text),
                            'source_repo': 'EvoLinkAI/awesome-gpt-image-2-API-and-Prompts',
                            'source_url': f'https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts',
                            'source_license': 'Unknown',
                            'collected_at': datetime.utcnow().isoformat() + 'Z'
                        })
        elif isinstance(data, dict) and 'prompts' in data:
            for item in data['prompts']:
                prompt_text = item.get('prompt', '') or item.get('text', '')
                if prompt_text:
                    records.append({
                        'id': hash_prompt(prompt_text),
                        'title': item.get('title', '')[:100],
                        'prompt': prompt_text,
                        'lang_guess': detect_language(prompt_text),
                        'source_repo': 'EvoLinkAI/awesome-gpt-image-2-API-and-Prompts',
                        'source_url': f'https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts',
                        'source_license': 'Unknown',
                        'collected_at': datetime.utcnow().isoformat() + 'Z'
                    })
    
    return records

def process_stimqq():
    """处理 stimQQ/gpt-image-2-prompts"""
    records = []
    url = "https://raw.githubusercontent.com/stimQQ/gpt-image-2-prompts/master/prompts.json"
    
    data = download_json(url)
    if not data:
        return records
    
    for item in data:
        # 优先使用英文提示词
        prompt_text = item.get('prompt_en', '') or item.get('prompt_zh', '')
        if prompt_text:
            records.append({
                'id': hash_prompt(prompt_text),
                'title': item.get('name_en', '') or item.get('name_zh', ''),
                'prompt': prompt_text,
                'lang_guess': detect_language(prompt_text),
                'source_repo': 'stimQQ/gpt-image-2-prompts',
                'source_url': 'https://github.com/stimQQ/gpt-image-2-prompts',
                'source_license': 'CC BY 4.0',
                'collected_at': datetime.utcnow().isoformat() + 'Z'
            })
    
    return records

def process_gptimage2prompts():
    """处理 gptimage2prompts/gpt-image-2-prompts"""
    records = []
    url = "https://raw.githubusercontent.com/gptimage2prompts/gpt-image-2-prompts/main/data/prompts.json"
    
    data = download_json(url)
    if not data:
        return records
    
    # 检查数据格式
    if isinstance(data, list):
        items = data
    elif isinstance(data, dict) and 'prompts' in data:
        items = data['prompts']
    else:
        print(f"  未知数据格式: {type(data)}", file=sys.stderr)
        return records
    
    for item in items:
        if not isinstance(item, dict):
            continue
        prompt_text = item.get('prompt', '') or item.get('prompt_text', '')
        if prompt_text:
            records.append({
                'id': hash_prompt(prompt_text),
                'title': item.get('title', '') or item.get('name', ''),
                'prompt': prompt_text,
                'lang_guess': detect_language(prompt_text),
                'source_repo': 'gptimage2prompts/gpt-image-2-prompts',
                'source_url': 'https://github.com/gptimage2prompts/gpt-image-2-prompts',
                'source_license': 'Other',
                'collected_at': datetime.utcnow().isoformat() + 'Z'
            })
    
    return records

def process_tiange():
    """处理 TIANGE2211123/gpt-image-2-prompts"""
    records = []
    url = "https://raw.githubusercontent.com/TIANGE2211123/gpt-image-2-prompts/main/data/prompts.json"
    
    data = download_json(url)
    if not data:
        return records
    
    if not isinstance(data, list):
        print(f"  未知数据格式: {type(data)}", file=sys.stderr)
        return records
    
    for item in data:
        if not isinstance(item, dict):
            continue
        prompt_text = item.get('prompt', '')
        if prompt_text:
            records.append({
                'id': hash_prompt(prompt_text),
                'title': item.get('title', ''),
                'prompt': prompt_text,
                'lang_guess': detect_language(prompt_text),
                'source_repo': 'TIANGE2211123/gpt-image-2-prompts',
                'source_url': 'https://github.com/TIANGE2211123/gpt-image-2-prompts',
                'source_license': 'MIT',
                'collected_at': datetime.utcnow().isoformat() + 'Z'
            })
    
    return records

def process_peterroo():
    """处理 peterRooo/awesome-gpt-image-2-prompts (BigPengSays)"""
    records = []
    url = "https://raw.githubusercontent.com/peterRooo/awesome-gpt-image-2-prompts/main/data/gpt-image-2-prompts.json"
    
    data = download_json(url)
    if not data:
        return records
    
    if not isinstance(data, list):
        print(f"  未知数据格式: {type(data)}", file=sys.stderr)
        return records
    
    for item in data:
        if not isinstance(item, dict):
            continue
        prompt_text = item.get('prompt', '') or item.get('prompt_text', '')
        if prompt_text:
            records.append({
                'id': hash_prompt(prompt_text),
                'title': item.get('title', '') or item.get('name', ''),
                'prompt': prompt_text,
                'lang_guess': detect_language(prompt_text),
                'source_repo': 'peterRooo/awesome-gpt-image-2-prompts',
                'source_url': 'https://github.com/peterRooo/awesome-gpt-image-2-prompts',
                'source_license': 'Unknown',
                'collected_at': datetime.utcnow().isoformat() + 'Z'
            })
    
    return records

def process_peterhacker():
    """处理 peterhacker-ai/gpt-image-2-prompts-library"""
    records = []
    url = "https://raw.githubusercontent.com/peterhacker-ai/gpt-image-2-prompts-library/main/data/prompts.json"
    
    data = download_json(url)
    if not data:
        return records
    
    if not isinstance(data, list):
        print(f"  未知数据格式: {type(data)}", file=sys.stderr)
        return records
    
    for item in data:
        if not isinstance(item, dict):
            continue
        prompt_text = item.get('prompt', '') or item.get('prompt_text', '')
        if prompt_text:
            records.append({
                'id': hash_prompt(prompt_text),
                'title': item.get('title', '') or item.get('name', ''),
                'prompt': prompt_text,
                'lang_guess': detect_language(prompt_text),
                'source_repo': 'peterhacker-ai/gpt-image-2-prompts-library',
                'source_url': 'https://github.com/peterhacker-ai/gpt-image-2-prompts-library',
                'source_license': 'Other',
                'collected_at': datetime.utcnow().isoformat() + 'Z'
            })
    
    return records

def process_starroadlu():
    """处理 StarRoadlu/gpt-image-2-gallery"""
    records = []
    url = "https://raw.githubusercontent.com/StarRoadlu/gpt-image-2-gallery/main/data/items.json"
    
    data = download_json(url)
    if not data:
        return records
    
    if isinstance(data, list):
        items = data
    elif isinstance(data, dict) and 'items' in data:
        items = data['items']
    else:
        return records
    
    for item in items:
        prompt_text = item.get('prompt', '') or item.get('text', '')
        if prompt_text:
            records.append({
                'id': hash_prompt(prompt_text),
                'title': item.get('title', '') or item.get('name', ''),
                'prompt': prompt_text,
                'lang_guess': detect_language(prompt_text),
                'source_repo': 'StarRoadlu/gpt-image-2-gallery',
                'source_url': 'https://github.com/StarRoadlu/gpt-image-2-gallery',
                'source_license': 'Unknown',
                'collected_at': datetime.utcnow().isoformat() + 'Z'
            })
    
    return records

def main():
    print("开始收集提示词...", file=sys.stderr)
    
    all_records = []
    
    # 处理各个来源
    processors = [
        ("stimQQ", process_stimqq),
        ("gptimage2prompts", process_gptimage2prompts),
        ("TIANGE2211123", process_tiange),
        ("peterRooo", process_peterroo),
        ("peterhacker-ai", process_peterhacker),
        ("StarRoadlu", process_starroadlu),
        ("EvoLinkAI", process_evolinkai),
    ]
    
    for name, processor in processors:
        print(f"\n处理 {name}...", file=sys.stderr)
        records = processor()
        print(f"  收集到 {len(records)} 条记录", file=sys.stderr)
        all_records.extend(records)
    
    # 去重（基于 prompt hash）
    seen = set()
    unique_records = []
    for record in all_records:
        if record['id'] not in seen:
            seen.add(record['id'])
            unique_records.append(record)
    
    print(f"\n总计: {len(all_records)} 条记录", file=sys.stderr)
    print(f"去重后: {len(unique_records)} 条记录", file=sys.stderr)
    
    # 输出 JSONL
    for record in unique_records:
        print(json.dumps(record, ensure_ascii=False))

if __name__ == '__main__':
    main()
