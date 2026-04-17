import os
import glob
import re

BASE_DIR = "/Users/khalidaitelmaati/Desktop/scrapy-master/psychology-theme-main"

def fix_html_content(content):
    # Fix index.html specific cases to point to root /
    content = content.replace('href="index.html"', 'href="/"')
    content = content.replace('href="https://leafanoo.com/index.html"', 'href="https://leafanoo.com/"')
    content = content.replace('"https://leafanoo.com/index.html"', '"https://leafanoo.com/"')
    content = content.replace('<loc>https://leafanoo.com/index.html</loc>', '<loc>https://leafanoo.com/</loc>')

    # 1. Fix relative internal links: href="article1.html" -> href="article1"
    content = re.sub(r'href="([a-zA-Z0-9_-]+)\.html"', r'href="\1"', content)
    
    # 2. Fix absolute internal links: href="https://leafanoo.com/article1.html" -> href="https://leafanoo.com/article1"
    content = re.sub(r'href="https://leafanoo\.com/([a-zA-Z0-9_-]+)\.html"', r'href="https://leafanoo.com/\1"', content)
    
    # 3. Fix JSON-LD Schema / OG Meta tags: "https://leafanoo.com/article1.html" -> "https://leafanoo.com/article1"
    content = re.sub(r'"https://leafanoo\.com/([a-zA-Z0-9_-]+)\.html"', r'"https://leafanoo.com/\1"', content)
    
    # 4. Fix Sitemap <loc> tags: <loc>https://leafanoo.com/article1.html</loc> -> <loc>https://leafanoo.com/article1</loc>
    content = re.sub(r'<loc>https://leafanoo\.com/([a-zA-Z0-9_-]+)\.html</loc>', r'<loc>https://leafanoo.com/\1</loc>', content)

    return content

def run():
    # Process all HTML files
    html_files = glob.glob(os.path.join(BASE_DIR, "*.html"))
    updated_html = 0
    for file_path in html_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = fix_html_content(content)
        
        if content != new_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            updated_html += 1

    print(f"Updated {updated_html} HTML files.")

    # Process sitemap.xml
    sitemap_path = os.path.join(BASE_DIR, "sitemap.xml")
    if os.path.exists(sitemap_path):
        with open(sitemap_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = fix_html_content(content)
        
        if content != new_content:
            with open(sitemap_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print("Updated sitemap.xml")

if __name__ == "__main__":
    run()
