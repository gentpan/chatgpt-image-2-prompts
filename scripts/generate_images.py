#!/usr/bin/env python3
"""
Generate images from prompts in the repository.

This script walks through all prompt markdown files and will call an image generation API
to create images for each prompt.

Status: STUB / TODO
- Currently just scans and reports prompt files
- TODO: Integrate with image generation API (ChatGPT Image 2 or similar)
"""

import sys
from pathlib import Path
import re


def extract_prompts_from_md(file_path):
    """Extract Chinese and English prompts from a markdown file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract metadata
    id_match = re.search(r'^id:\s*(.+)$', content, re.MULTILINE)
    category_match = re.search(r'^category:\s*(.+)$', content, re.MULTILINE)
    
    # Extract prompts
    zh_match = re.search(r'## 中文\s*```\s*(.+?)\s*```', content, re.DOTALL)
    en_match = re.search(r'## English\s*```\s*(.+?)\s*```', content, re.DOTALL)
    
    return {
        'id': id_match.group(1).strip() if id_match else None,
        'category': category_match.group(1).strip() if category_match else None,
        'prompt_zh': zh_match.group(1).strip() if zh_match else None,
        'prompt_en': en_match.group(1).strip() if en_match else None,
        'file': str(file_path)
    }


def scan_prompts(prompts_dir='prompts'):
    """Scan all prompt markdown files in the prompts directory."""
    prompts_path = Path(prompts_dir)
    
    if not prompts_path.exists():
        print(f"Error: Directory '{prompts_dir}' not found")
        return []
    
    all_prompts = []
    
    # Walk through all categories
    for category_dir in sorted(prompts_path.iterdir()):
        if not category_dir.is_dir():
            continue
        
        category_name = category_dir.name
        print(f"\n📁 Category: {category_name}")
        
        # Find all numbered markdown files
        md_files = sorted(category_dir.glob('[0-9]*.md'))
        
        for md_file in md_files:
            try:
                prompt_data = extract_prompts_from_md(md_file)
                all_prompts.append(prompt_data)
                
                # Display summary
                file_num = md_file.stem
                has_zh = "✓" if prompt_data['prompt_zh'] and len(prompt_data['prompt_zh']) > 10 else "✗"
                has_en = "✓" if prompt_data['prompt_en'] and len(prompt_data['prompt_en']) > 10 else "✗"
                print(f"  {file_num}: 中文 {has_zh} | English {has_en} | {prompt_data['id']}")
                
            except Exception as e:
                print(f"  Error reading {md_file.name}: {e}")
    
    return all_prompts


def generate_images(prompts, output_dir='images'):
    """
    TODO: Generate images for each prompt using an image generation API.
    
    Args:
        prompts: List of prompt dictionaries from scan_prompts()
        output_dir: Directory to save generated images
    
    Implementation ideas:
    - Use OpenAI API for DALL-E / ChatGPT Image generation
    - Use local Stable Diffusion API
    - Batch processing with rate limiting
    - Save images with naming convention: {category}-{id}.png
    - Generate metadata JSON alongside images
    """
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    print(f"\n🚧 TODO: Image generation not yet implemented")
    print(f"📊 Found {len(prompts)} prompts ready for image generation")
    print(f"📁 Images would be saved to: {output_path.absolute()}")
    
    # TODO: Implement actual image generation here
    # for prompt in prompts:
    #     image = call_image_api(prompt['prompt_en'])  # or prompt_zh
    #     image.save(f"{output_dir}/{prompt['id']}.png")


def main():
    print("=" * 60)
    print("GPT Image 2 Prompts - Image Generator (STUB)")
    print("=" * 60)
    
    # Scan all prompts
    prompts = scan_prompts('prompts')
    
    if not prompts:
        print("\n❌ No prompts found")
        return 1
    
    print(f"\n✓ Total prompts scanned: {len(prompts)}")
    
    # TODO: Uncomment when ready to generate images
    # generate_images(prompts)
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
