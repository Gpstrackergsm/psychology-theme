import glob
import re
import os

html_files = glob.glob("*.html")
valid_pages = {f.replace('.html', '') for f in html_files}
valid_pages.add("") # root /
valid_pages.add("/")
for f in html_files:
    valid_pages.add(f)
    valid_pages.add("/" + f)

errors = []
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    links = re.findall(r'href=["\'](.*?)["\']', content)
    for link in links:
        if link.startswith('http') or link.startswith('mailto:') or link.startswith('tel:'):
            continue
        
        # Check resources
        if link.endswith('.css') or link.endswith('.ico') or link.endswith('.png') or link.endswith('.svg') or link.endswith('.xml'):
            # check if exists
            l = link.lstrip('/')
            if not os.path.exists(l):
                errors.append((file, link, "Resource missing"))
            continue

        base_link = link.split('#')[0]
        if base_link.startswith('/'):
            base_link = base_link[1:]
        
        if base_link not in valid_pages and base_link != "":
            errors.append((file, link, "Internal page missing"))

if len(errors) > 0:
    for e in errors[:20]:
        print(f"Error in {e[0]}: target '{e[1]}' ({e[2]})")
    print(f"Total broken links found: {len(errors)}")
else:
    print("Zero internal broken links found.")
