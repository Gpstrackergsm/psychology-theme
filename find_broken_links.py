import os
import glob
import re

BASE_DIR = "."
html_files = glob.glob("*.html")
valid_pages = [f.replace('.html', '') for f in html_files] + ['/']

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # find local hrefs
    links = re.findall(r'href="([^"]+)"', content)
    for link in links:
        if link.startswith('http') or link.startswith('#') or link.startswith('mailto:') or link.startswith('tel:'):
            continue
        if link.endswith('.css') or link.endswith('.js') or link.endswith('.svg') or link.endswith('.ico') or link.endswith('.png'):
            continue
        
        # It's an internal link
        # Vercel handles /about, check if "about" is in valid pages
        link_base = link.split('#')[0]
        if link_base == "":
            continue
            
        if link_base not in valid_pages and link_base + ".html" not in html_files and link_base != "/":
            print(f"Broken link in {file}: {link}")

