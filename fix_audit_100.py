import os
import glob
import re
import urllib.request
import concurrent.futures

BASE_DIR = "/Users/khalidaitelmaati/Desktop/scrapy-master/psychology-theme-main"
FALLBACK_IMG = "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&q=80&w=1200"

def is_valid_url(url):
    try:
        # Some URLs might be local, but we are looking for Unsplash
        if "unsplash.com" not in url:
            return True # Assume valid for now
            
        req = urllib.request.Request(url, method='HEAD', headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req, timeout=5)
        return response.getcode() == 200
    except Exception:
        return False

def truncate_text(text, max_len):
    if len(text) <= max_len:
        return text
    # Truncate at last space before max_len
    truncated = text[:max_len-3]
    last_space = truncated.rfind(' ')
    if last_space > 0:
        truncated = truncated[:last_space]
    return truncated + "..."

def fix_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # 1. Fix leftover .html links
    content = re.sub(r'href="[\./]*index\.html#(.*?)"', r'href="/#\1"', content)
    content = re.sub(r'href="/([a-zA-Z0-9_-]+)\.html"', r'href="/\1"', content)
    content = re.sub(r'href="[\./]*contact\.html"', 'href="/contact"', content)
    content = re.sub(r'href="[\./]*about\.html"', 'href="/about"', content)
    content = re.sub(r'href="[\./]*terms\.html"', 'href="/terms"', content)
    content = re.sub(r'href="[\./]*privacy-policy\.html"', 'href="/privacy-policy"', content)

    # 2. Fix Title length (max 60 recommended, but we'll do 60)
    def title_repl(match):
        title = match.group(1)
        return f"<title>{truncate_text(title, 60)}</title>"
    content = re.sub(r'<title>(.*?)</title>', title_repl, content)
    
    content = re.sub(r'<meta content="([^"]*)" name="twitter:title"/>', lambda m: f'<meta content="{truncate_text(m.group(1), 60)}" name="twitter:title"/>', content)
    content = re.sub(r'<meta content="([^"]*)" property="og:title"/>', lambda m: f'<meta content="{truncate_text(m.group(1), 60)}" property="og:title"/>', content)

    # 3. Fix Meta Description length (max 160)
    # <meta content="..." name="description"/>
    def desc_repl(match):
        desc = match.group(1)
        return f'<meta content="{truncate_text(desc, 155)}" name="description"/>'
    content = re.sub(r'<meta content="([^"]*)" name="description"/>', desc_repl, content)
    content = re.sub(r'<meta content="([^"]*)" name="twitter:description"/>', lambda m: f'<meta content="{truncate_text(m.group(1), 155)}" name="twitter:description"/>', content)
    content = re.sub(r'<meta content="([^"]*)" property="og:description"/>', lambda m: f'<meta content="{truncate_text(m.group(1), 155)}" property="og:description"/>', content)

    # 4. Check for broken images (basic check)
    # Find all Unsplash images and replace if broken
    images = re.findall(r'src="(https://images[^"]+)"', content)
    for img in images:
        if not is_valid_url(img):
            content = content.replace(img, FALLBACK_IMG)

    bg_images = re.findall(r'url\(\'(https://images[^>]+)\'\)', content)
    for bg_img in bg_images:
        if not is_valid_url(bg_img):
            content = content.replace(bg_img, FALLBACK_IMG)

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def run():
    html_files = glob.glob(os.path.join(BASE_DIR, "*.html"))
    updated = 0
    
    print(f"Starting audit and fix for {len(html_files)} files... This may take a minute due to image checking.")
    
    # We can use ThreadPoolExecutor to speed up image validation
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(fix_html_file, html_files)
        updated = sum(1 for r in results if r)
            
    print(f"Successfully fixed {updated} files.")

if __name__ == "__main__":
    run()
