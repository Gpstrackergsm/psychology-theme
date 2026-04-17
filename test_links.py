import glob
import re
import os

html_files = set(glob.glob("*.html"))
valid_pages = {f.replace('.html', '') for f in html_files} | {"/"}

errors = []
orphans = set(html_files)

# Exclude index, 404, etc from orphan check
for f in ["index.html", "404.html", "about.html", "contact.html", "terms.html", "privacy-policy.html"]:
    if f in orphans: orphans.remove(f)

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    links = re.findall(r'href="(/?(?:[a-zA-Z0-9_-]+(?:#[a-zA-Z0-9_-]+)?)?)"', content)
    for link in links:
        if link == "" or link.startswith("http"): continue
        
        # Strip hash
        base_link = link.split('#')[0]
        if base_link.startswith('/'):
            base_link = base_link[1:]
            
        if base_link == "":
            pass # root link
        elif base_link not in valid_pages and base_link + ".html" not in html_files:
            errors.append((file, link))
        else:
            if base_link + ".html" in orphans:
                orphans.remove(base_link + ".html")
            
print(f"Total broken local links found: {len(errors)}")
print(f"Total orphan pages found: {len(orphans)}")

if len(errors) > 0:
    print("Example broken links:", errors[:5])
