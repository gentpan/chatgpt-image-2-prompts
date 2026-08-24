#!/usr/bin/env python3
"""
Convert existing prompts to new canonical format:
- Rename to 0001.md, 0002.md, etc.
- Simplify frontmatter
- Keep only Chinese and English prompts
"""

import os
import re
from pathlib import Path

# List of files in order
files = [
    "prompts/电商/主图/Glossy Tonkatsu Food Photo.md",
    "prompts/电商/主图/Glowing Totoro Robot Figure Diorama.md",
    "prompts/电商/主图/Photorealistic Codex Token Coins.md",
    "prompts/电商/主图/Premium Skincare Product Photography.md",
    "prompts/电商/主图/Warm Minimalist Microwave Product Photo.md",
    "prompts/电商/包装/Premium Energy Drink Branding Concepts.md",
    "prompts/电商/包装/Realistic Unaju Grilled Eel Box.md",
    "prompts/电商/包装/Translucent Gummy Crocodile Render.md",
    "prompts/电商/包装/Transparent Earbuds on Stone Pedestal.md",
    "prompts/电商/包装/Wet Transparent Earbud Macro.md",
    "prompts/电商/场景种草/Commercial Product Photography.md",
    "prompts/电商/场景种草/Full-Body Studio Lifestyle Portrait.md",
    "prompts/电商/场景种草/Pastel Peach Lychee Rose Parfait.md",
    "prompts/电商/场景种草/Pink Tracksuit T-Shirt Mockup.md",
    "prompts/电商/场景种草/Realistic Indoor Fashion Portrait.md",
    "prompts/电商/模特上身/African Male Fashion Editorial.md",
    "prompts/电商/模特上身/Elegant South Asian Fashion Photoshoot.md",
    "prompts/电商/模特上身/Kids Premium Fashion Advertisement.md",
    "prompts/电商/模特上身/Luxury Fashion Mirror Selfie.md",
    "prompts/电商/模特上身/Realistic Teacher in Math Classroom.md",
    "prompts/电商/详情页/Cinematic Food Photography Menu.md",
    "prompts/电商/详情页/Feminine Casual Summer Outfit.md",
    "prompts/电商/详情页/High-End Skincare Brand Key Visual.md",
    "prompts/电商/详情页/Minimalist Product Promotional Poster.md",
    "prompts/电商/详情页/Outdoor Floral Dress Portrait.md",
    "prompts/电商/静物白底/Crispy Chicken Burger Product Photo.md",
    "prompts/电商/静物白底/Minimalist Japanese Cafe Product Poster.md",
    "prompts/电商/静物白底/Minimal Luxury Perfume Product Shot.md",
    "prompts/电商/静物白底/Sleek Studio Furniture Shot.md",
    "prompts/电商/静物白底/Vintage Brass Hanging Lantern.md",
]

def extract_prompt_content(content):
    """Extract Chinese and English prompts from various formats"""
    # Try to find Chinese prompt
    zh_match = re.search(r'## 提示词（中文）\s*```\s*(.+?)\s*```', content, re.DOTALL)
    if not zh_match:
        zh_match = re.search(r'## 提示词\s*```\s*(.+?)\s*```', content, re.DOTALL)
    
    # Try to find English prompt  
    en_match = re.search(r'## 提示词（英文）\s*```\s*(.+?)\s*```', content, re.DOTALL)
    if not en_match:
        en_match = re.search(r'## 提示词\s*```\s*(.+?)\s*```', content, re.DOTALL)
    
    zh_prompt = zh_match.group(1).strip() if zh_match else ""
    en_prompt = en_match.group(1).strip() if en_match else ""
    
    return zh_prompt, en_prompt

def extract_source_info(content):
    """Extract source repo, url, and license"""
    source_repo = ""
    source_url = ""
    source_license = ""
    
    repo_match = re.search(r'source_repo:\s*(.+)', content)
    url_match = re.search(r'source_url:\s*(.+)', content)
    license_match = re.search(r'source_license:\s*(.+)', content)
    
    if repo_match:
        source_repo = repo_match.group(1).strip()
    if url_match:
        source_url = url_match.group(1).strip()
    if license_match:
        source_license = license_match.group(1).strip()
    
    return source_repo, source_url, source_license

def convert_file(input_path, output_path, file_num, category="电商"):
    """Convert a single file to new format"""
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    source_repo, source_url, source_license = extract_source_info(content)
    zh_prompt, en_prompt = extract_prompt_content(content)
    
    # Create new content
    new_content = f"""---
id: {category}-{file_num:04d}
category: {category}
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
    
    print(f"Converted {file_num:04d}: {input_path}")

# Create output directory if needed
output_dir = Path("prompts/电商")
output_dir.mkdir(parents=True, exist_ok=True)

# Convert all files
for i, file_path in enumerate(files, start=1):
    input_path = Path(file_path)
    if input_path.exists():
        output_path = output_dir / f"{i:04d}.md"
        convert_file(input_path, output_path, i)

print(f"\n✓ Converted {len(files)} files")
