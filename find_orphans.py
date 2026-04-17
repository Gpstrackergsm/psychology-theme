import glob
import re
import os

html_files = glob.glob("*.html")
valid_pages = {f.replace('.html', '') for f in html_files} | {""}

incoming_links = {p: 0 for p in valid_pages}

for file in html_files:
    file_base = file.replace('.html', '')
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    links = re.findall(r'href="(/?(?:[a-zA-Z0-9_-]+)(?:#[a-zA-Z0-9_-]+)?)?"', content)
    
    for link in links:
        if link.startswith('http') or link.startswith('#'): continue
        base_link = link.split('#')[0].strip('/')
        
        if base_link in incoming_links:
            if base_link != file_base: # ignoring self links
                incoming_links[base_link] += 1
                
orphans = [p for p, count in incoming_links.items() if count == 0 and p != ""]
print(f"Total orphan pages found: {len(orphans)}")
print(f"Orphan pages: {orphans}")
