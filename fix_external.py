import glob
import re

broken_urls = [
    "https://www.sleepdiplomat.com/book",
    "https://doi.org/10.1207/S15327965PLI1401_01",
    "https://doi.org/10.1525/mp.2014.31.2.118",
    "https://doi.org/10.1177/0013916506295573",
    "https://doi.org/10.1080/15298860309032",
    "https://johnhari.com/",
    "https://doi.org/10.1111/spc3.12011",
    "https://www.taylorfrancis.com/books/mono/10.4324/9780203777381/compassion-fatigue-charles-figley",
    "https://doi.org/10.1207/S15327965PLI1104_01"
]

html_files = glob.glob("*.html")
updated = 0

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original = content
    for url in broken_urls:
        escape_url = re.escape(url)
        # Match <a href="broken_url"...>Text</a> and replace with Text
        pattern = r'<a[^>]*href="' + escape_url + r'"[^>]*>(.*?)</a>'
        content = re.sub(pattern, r'\1', content)
        
    if content != original:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        updated += 1

print(f"Stripped {len(broken_urls)} broken external links from {updated} pages.")
