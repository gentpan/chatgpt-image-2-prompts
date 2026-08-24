#!/usr/bin/env python3
import re
from pathlib import Path

files = [
    ("prompts/电商/主图/Glossy Tonkatsu Food Photo.md", 1),
    ("prompts/电商/主图/Glowing Totoro Robot Figure Diorama.md", 2),
    ("prompts/电商/主图/Photorealistic Codex Token Coins.md", 3),
    ("prompts/电商/主图/Premium Skincare Product Photography.md", 4),
    ("prompts/电商/主图/Warm Minimalist Microwave Product Photo.md", 5),
    ("prompts/电商/包装/Premium Energy Drink Branding Concepts.md", 6),
    ("prompts/电商/包装/Realistic Unaju Grilled Eel Box.md", 7),
    ("prompts/电商/包装/Translucent Gummy Crocodile Render.md", 8),
    ("prompts/电商/包装/Transparent Earbuds on Stone Pedestal.md", 9),
    ("prompts/电商/包装/Wet Transparent Earbud Macro.md", 10),
    ("prompts/电商/场景种草/Commercial Product Photography.md", 11),
    ("prompts/电商/场景种草/Full-Body Studio Lifestyle Portrait.md", 12),
    ("prompts/电商/场景种草/Pastel Peach Lychee Rose Parfait.md", 13),
    ("prompts/电商/场景种草/Pink Tracksuit T-Shirt Mockup.md", 14),
    ("prompts/电商/场景种草/Realistic Indoor Fashion Portrait.md", 15),
    ("prompts/电商/模特上身/African Male Fashion Editorial.md", 16),
    ("prompts/电商/模特上身/Elegant South Asian Fashion Photoshoot.md", 17),
    ("prompts/电商/模特上身/Kids Premium Fashion Advertisement.md", 18),
    ("prompts/电商/模特上身/Luxury Fashion Mirror Selfie.md", 19),
    ("prompts/电商/模特上身/Realistic Teacher in Math Classroom.md", 20),
    ("prompts/电商/详情页/Cinematic Food Photography Menu.md", 21),
    ("prompts/电商/详情页/Feminine Casual Summer Outfit.md", 22),
    ("prompts/电商/详情页/High-End Skincare Brand Key Visual.md", 23),
    ("prompts/电商/详情页/Minimalist Product Promotional Poster.md", 24),
    ("prompts/电商/详情页/Outdoor Floral Dress Portrait.md", 25),
    ("prompts/电商/静物白底/Crispy Chicken Burger Product Photo.md", 26),
    ("prompts/电商/静物白底/Minimalist Japanese Cafe Product Poster.md", 27),
    ("prompts/电商/静物白底/Minimal Luxury Perfume Product Shot.md", 28),
    ("prompts/电商/静物白底/Sleek Studio Furniture Shot.md", 29),
    ("prompts/电商/静物白底/Vintage Brass Hanging Lantern.md", 30),
]

# Files already converted manually (have bilingual prompts)
converted_already = {1, 2, 3}

for fpath, num in files:
    if num in converted_already:
        print(f"Skip {num:04d}: already done manually")
        continue
    
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract source info
    repo_match = re.search(r'source_repo:\s*(.+)', content)
    url_match = re.search(r'source_url:\s*(.+)', content)
    lic_match = re.search(r'source_license:\s*(.+)', content)
    
    source_repo = repo_match.group(1).strip() if repo_match else ""
    source_url = url_match.group(1).strip() if url_match else ""
    source_license = lic_match.group(1).strip() if lic_match else ""
    
    # Extract prompts - check if bilingual version exists
    zh_match = re.search(r'## 提示词（中文）\s*```\s*(.+?)\s*```', content, re.DOTALL)
    en_match = re.search(r'## 提示词（英文）\s*```\s*(.+?)\s*```', content, re.DOTALL)
    
    if zh_match and en_match:
        zh_prompt = zh_match.group(1).strip()
        en_prompt = en_match.group(1).strip()
    else:
        # Extract English from old format
        en_match = re.search(r'## 提示词\s*```\s*(.+?)\s*```', content, re.DOTALL)
        if en_match:
            en_prompt = en_match.group(1).strip()
            zh_prompt = "[翻译待补充]"
        else:
            zh_prompt = "[未找到]"
            en_prompt = "[未找到]"
    
    output_path = f"prompts/电商/{num:04d}.md"
    new_content = f"""---
id: 电商-{num:04d}
category: 电商
model: gpt-image-2
source_repo: {source_repo}
source_url: {source_url}
source_license: {source_license}
organizer: Yep (gentpan)
---

## 中文

```
{zh_prompt}
```

## English

```
{en_prompt}
```
"""
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    fname = Path(fpath).name
    print(f"✓ {num:04d}: {fname[:50]}")

print(f"\n✓ Converted {len(files) - len(converted_already)} files (skipped {len(converted_already)} already done)")
