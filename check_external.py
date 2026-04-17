import glob
import re
import urllib.request
import concurrent.futures

html_files = glob.glob("*.html")
external_links = set()

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    links = re.findall(r'href="(http[s]?://[^"]+)"', content)
    for link in links:
        if "leafanoo.com" not in link and "unsplash.com" not in link:
            external_links.add(link)

print(f"Found {len(external_links)} unique external links.")

def check_link(url):
    try:
        req = urllib.request.Request(url, method='HEAD', headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req, timeout=5)
        if res.getcode() >= 400:
            return url
    except Exception:
        return url
    return None

with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
    results = list(executor.map(check_link, list(external_links)))

broken_external = [r for r in results if r]
print(f"Found {len(broken_external)} broken external links.")
for b in broken_external:
    print(b)
