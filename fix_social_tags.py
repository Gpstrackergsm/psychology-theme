import os
import glob
import re

BASE_DIR = "/Users/khalidaitelmaati/Desktop/scrapy-master/psychology-theme-main"
FALLBACK_IMG = "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&q=80&w=1200"

def get_title(content):
    match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
    return match.group(1) if match else "Mind & Balance"

def get_desc(content):
    match = re.search(r'<meta[^>]*name="description"[^>]*content="([^"]*)"', content, re.IGNORECASE)
    if not match:
        match = re.search(r'<meta[^>]*content="([^"]*)"[^>]*name="description"', content, re.IGNORECASE)
    return match.group(1) if match else "Explore the latest insights in cognitive psychology, mental health, and neuroscience."

def get_image(content):
    # Try to find og:image first
    match = re.search(r'<meta[^>]*property="og:image"[^>]*content="([^"]*)"', content, re.IGNORECASE)
    if match:
        return match.group(1)
    # Then try the first image in an article
    match = re.search(r'<img[^>]*src="(https://images\.unsplash\.com/[^"]+)"', content, re.IGNORECASE)
    if match:
        return match.group(1)
    return FALLBACK_IMG

def fix_social_tags():
    html_files = glob.glob(os.path.join(BASE_DIR, "*.html"))
    updated = 0
    
    for file_path in html_files:
        filename = os.path.basename(file_path)
        base_name = filename.replace('.html', '')
        # Handle index.html mapped to /
        clean_url = "" if filename == "index.html" else base_name
        full_url = f"https://leafanoo.com/{clean_url}"
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        original_content = content
        
        title = get_title(content)
        desc = get_desc(content)
        image = get_image(content)
        
        # 1. Check and inject Canonical (Fix for "Duplicate pages without canonical")
        if '<link href="https://leafanoo.com/' not in content and 'rel="canonical"' not in content:
            canonical_tag = f'\n<link href="{full_url}" rel="canonical"/>'
            if '</head>' in content:
                content = content.replace('</head>', f'{canonical_tag}\n</head>')
        else:
            # Maybe the canonical got messed up, let's just make sure it exists
            pass

        # 2. Check and inject OG Tags
        og_tags = []
        if 'property="og:title"' not in content:
            og_tags.append(f'<meta property="og:title" content="{title}"/>')
        if 'property="og:description"' not in content:
            og_tags.append(f'<meta property="og:description" content="{desc}"/>')
        if 'property="og:image"' not in content:
            og_tags.append(f'<meta property="og:image" content="{image}"/>')
        if 'property="og:url"' not in content:
            og_tags.append(f'<meta property="og:url" content="{full_url}"/>')
        if 'property="og:type"' not in content:
            og_tags.append(f'<meta property="og:type" content="article"/>')
            
        # 3. Check and inject Twitter Tags
        tw_tags = []
        if 'name="twitter:card"' not in content:
            tw_tags.append(f'<meta name="twitter:card" content="summary_large_image"/>')
        if 'name="twitter:title"' not in content:
            tw_tags.append(f'<meta name="twitter:title" content="{title}"/>')
        if 'name="twitter:description"' not in content:
            tw_tags.append(f'<meta name="twitter:description" content="{desc}"/>')
        if 'name="twitter:image"' not in content:
            tw_tags.append(f'<meta name="twitter:image" content="{image}"/>')
            
        if og_tags or tw_tags:
            all_tags = "\n<!-- Auto-Injected Social Tags -->\n" + "\n".join(og_tags + tw_tags)
            if '</head>' in content:
                content = content.replace('</head>', f'{all_tags}\n</head>')

        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            updated += 1
            
    print(f"Injected missing Canonical / OG / Twitter tags into {updated} files.")

if __name__ == "__main__":
    fix_social_tags()
