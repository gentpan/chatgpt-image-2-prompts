#!/usr/bin/env python3
"""
整理电商提示词数据
从多个数据源提取、去重、分类电商相关的提示词
"""

import json
import hashlib
import re
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Set

# 电商关键词（用于分类和过滤）
ECOMMERCE_KEYWORDS = {
    '主图': ['main image', '主图', 'product listing', 'thumbnail', 'hero shot', '商品展示', '商品主图'],
    '详情页': ['detail page', '详情页', 'product detail', 'pdp', 'description', '产品描述'],
    '包装': ['packaging', '包装', 'box', 'wrap', '盒子', 'package'],
    '模特上身': ['model wearing', '模特', 'on model', 'wearing', '上身', 'person wearing'],
    '静物白底': ['white background', '白底', 'clean background', 'studio shot', 'isolated', '纯色背景'],
    '场景种草': ['lifestyle', '场景', 'in use', 'contextual', '使用场景', '生活方式', '种草'],
}

# 通用电商过滤关键词
GENERAL_ECOM_FILTERS = [
    'ecommerce', '电商', 'shop', 'shopping', 'product photo', 'commercial',
    '商品', '产品', 'listing', '详情', '主图', '包装', 'amazon', 'taobao',
    '淘宝', '天猫', '京东', 'catalog', '店铺'
]

def hash_content(text: str) -> str:
    """计算文本内容的 hash 用于去重"""
    normalized = re.sub(r'\s+', ' ', text.lower().strip())
    return hashlib.md5(normalized.encode()).hexdigest()

def classify_prompt(content: str, title: str = '', description: str = '') -> str:
    """根据内容分类提示词到不同的桶"""
    full_text = f"{title} {description} {content}".lower()
    
    scores = defaultdict(int)
    for category, keywords in ECOMMERCE_KEYWORDS.items():
        for kw in keywords:
            if kw.lower() in full_text:
                scores[category] += 1
    
    if scores:
        return max(scores.items(), key=lambda x: x[1])[0]
    return '主图'  # 默认分类

def is_ecommerce_related(content: str, title: str = '', description: str = '') -> bool:
    """判断是否为电商相关内容"""
    full_text = f"{title} {description} {content}".lower()
    return any(kw.lower() in full_text for kw in GENERAL_ECOM_FILTERS)

def process_source1(filepath: Path) -> List[Dict]:
    """处理 ecommerce-main-image.json (YouMind-OpenLab)"""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    results = []
    for item in data:
        prompt = {
            'id': f"youmind-ecom-{item['id']}",
            'title': item.get('title', ''),
            'content': item['content'],
            'description': item.get('description', ''),
            'model': 'gpt-image-2',
            'source_repo': 'YouMind-OpenLab/gpt-image-2-prompts-search',
            'source_url': 'https://github.com/YouMind-OpenLab/gpt-image-2-prompts-search',
            'source_license': 'CC BY 4.0',
            'category': '电商',
            'bucket': classify_prompt(item['content'], item.get('title', ''), item.get('description', '')),
            'hash': hash_content(item['content']),
            'needs_reference': item.get('needReferenceImages', False),
        }
        results.append(prompt)
    
    return results

def process_source2(filepath: Path, seen_ids: Set[int]) -> List[Dict]:
    """处理 product-marketing.json，过滤电商相关且未重复的条目"""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    results = []
    for item in data:
        # 跳过已有的 ID
        if item['id'] in seen_ids:
            continue
        
        # 只保留明确的电商内容
        content = item['content']
        title = item.get('title', '')
        description = item.get('description', '')
        
        if not is_ecommerce_related(content, title, description):
            continue
        
        prompt = {
            'id': f"youmind-product-{item['id']}",
            'title': title,
            'content': content,
            'description': description,
            'model': 'gpt-image-2',
            'source_repo': 'YouMind-OpenLab/gpt-image-2-prompts-search',
            'source_url': 'https://github.com/YouMind-OpenLab/gpt-image-2-prompts-search',
            'source_license': 'CC BY 4.0',
            'category': '电商',
            'bucket': classify_prompt(content, title, description),
            'hash': hash_content(content),
            'needs_reference': item.get('needReferenceImages', False),
        }
        results.append(prompt)
    
    return results

def process_source3(filepath: Path) -> List[Dict]:
    """处理 gptimage2prompts 数据源"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if not data:
            return []
        
        results = []
        # 尝试不同的数据结构
        items = data if isinstance(data, list) else data.get('prompts', [])
        
        for idx, item in enumerate(items):
            # 尝试提取内容
            content = ''
            if isinstance(item, str):
                content = item
            elif isinstance(item, dict):
                content = item.get('prompt', item.get('content', item.get('text', '')))
            
            if not content or not is_ecommerce_related(content):
                continue
            
            title = item.get('title', '') if isinstance(item, dict) else ''
            
            prompt = {
                'id': f"gptimage2prompts-{idx}",
                'title': title,
                'content': content,
                'description': '',
                'model': 'gpt-image-2',
                'source_repo': 'gptimage2prompts/gpt-image-2-prompts',
                'source_url': 'https://github.com/gptimage2prompts/gpt-image-2-prompts',
                'source_license': 'MIT',
                'category': '电商',
                'bucket': classify_prompt(content, title),
                'hash': hash_content(content),
                'needs_reference': False,
            }
            results.append(prompt)
        
        return results
    
    except Exception as e:
        print(f"Warning: Failed to process source3: {e}")
        return []

def deduplicate(prompts: List[Dict]) -> List[Dict]:
    """根据内容 hash 去重"""
    seen_hashes = set()
    unique = []
    
    for prompt in prompts:
        if prompt['hash'] not in seen_hashes:
            seen_hashes.add(prompt['hash'])
            unique.append(prompt)
    
    return unique

def select_featured(prompts: List[Dict], target: int = 30) -> List[Dict]:
    """选择精选示例：每个桶选择最清晰、最有代表性的提示词"""
    by_bucket = defaultdict(list)
    for p in prompts:
        by_bucket[p['bucket']].append(p)
    
    featured = []
    buckets = list(by_bucket.keys())
    per_bucket = max(3, target // len(buckets))
    
    for bucket in buckets:
        items = by_bucket[bucket]
        # 简单评分：标题完整、描述完整、内容适中长度的优先
        scored = []
        for item in items:
            score = 0
            if item['title']:
                score += 2
            if item['description']:
                score += 2
            content_len = len(item['content'])
            if 200 < content_len < 2000:
                score += 3
            elif content_len < 5000:
                score += 1
            scored.append((score, item))
        
        scored.sort(reverse=True, key=lambda x: x[0])
        featured.extend([item for _, item in scored[:per_bucket]])
    
    return featured[:target]

def main():
    base_dir = Path('/workspace')
    tmp_dir = base_dir / 'tmp' / 'sources'
    
    print("开始处理电商提示词数据...")
    
    # 处理数据源1: ecommerce-main-image.json
    print("\n处理数据源 1: ecommerce-main-image.json")
    prompts1 = process_source1(tmp_dir / 'ecommerce-main-image.json')
    print(f"  提取 {len(prompts1)} 条")
    
    # 收集 ID 用于去重
    seen_ids = {int(p['id'].split('-')[-1]) for p in prompts1 if p['id'].startswith('youmind-ecom-')}
    
    # 处理数据源2: product-marketing.json (过滤电商)
    print("\n处理数据源 2: product-marketing.json")
    prompts2 = process_source2(tmp_dir / 'product-marketing.json', seen_ids)
    print(f"  过滤出电商相关 {len(prompts2)} 条")
    
    # 处理数据源3: gptimage2prompts
    print("\n处理数据源 3: gptimage2prompts")
    prompts3 = process_source3(tmp_dir / 'gptimage2prompts.json')
    print(f"  过滤出电商相关 {len(prompts3)} 条")
    
    # 合并并去重
    all_prompts = prompts1 + prompts2 + prompts3
    print(f"\n合并前总数: {len(all_prompts)}")
    
    all_prompts = deduplicate(all_prompts)
    print(f"去重后总数: {len(all_prompts)}")
    
    # 统计各桶数量
    bucket_stats = defaultdict(int)
    source_stats = defaultdict(int)
    for p in all_prompts:
        bucket_stats[p['bucket']] += 1
        source_stats[p['source_repo']] += 1
    
    print("\n按桶分类统计:")
    for bucket, count in sorted(bucket_stats.items(), key=lambda x: -x[1]):
        print(f"  {bucket}: {count}")
    
    print("\n按数据源统计:")
    for source, count in sorted(source_stats.items()):
        print(f"  {source}: {count}")
    
    # 保存完整数据到 JSONL
    output_dir = base_dir / 'data' / 'ecommerce'
    output_dir.mkdir(parents=True, exist_ok=True)
    
    jsonl_path = output_dir / 'gpt-image-2.jsonl'
    with open(jsonl_path, 'w', encoding='utf-8') as f:
        for prompt in all_prompts:
            f.write(json.dumps(prompt, ensure_ascii=False) + '\n')
    print(f"\n完整数据已保存到: {jsonl_path}")
    
    # 选择精选示例
    featured = select_featured(all_prompts, target=30)
    print(f"\n选出精选示例: {len(featured)} 条")
    
    # 保存精选列表（用于后续生成 markdown）
    featured_path = tmp_dir / 'featured.json'
    with open(featured_path, 'w', encoding='utf-8') as f:
        json.dump(featured, f, ensure_ascii=False, indent=2)
    
    # 输出统计信息
    stats = {
        'total': len(all_prompts),
        'featured': len(featured),
        'by_bucket': dict(bucket_stats),
        'by_source': dict(source_stats),
    }
    
    stats_path = tmp_dir / 'stats.json'
    with open(stats_path, 'w', encoding='utf-8') as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)
    
    print(f"\n统计信息已保存到: {stats_path}")
    print("\n处理完成！")

if __name__ == '__main__':
    main()
