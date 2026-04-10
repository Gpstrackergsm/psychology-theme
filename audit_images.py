#!/usr/bin/env python3
"""Full HTTP audit of all card background-image URLs in index.html."""
import re, urllib.request, urllib.error, sys
from concurrent.futures import ThreadPoolExecutor, as_completed

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

card_pattern = re.compile(r'<article class="card[^>]*>([\s\S]*?)</article>', re.DOTALL)
art_urls = {}
for m in card_pattern.finditer(content):
    body = m.group(1)
    link = re.search(r'href="article(\d+)\.html"', body)
    bg = re.search(r'background-image:\s*url\(([^)]+)\)', body)
    if link and bg:
        art_id = int(link.group(1))
        img_url = bg.group(1).strip().strip("'\"")
        art_urls[art_id] = img_url

def check(art_id, img_url):
    try:
        req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
        resp = urllib.request.urlopen(req, timeout=8)
        return art_id, resp.status, img_url
    except urllib.error.HTTPError as e:
        return art_id, e.code, img_url
    except Exception as e:
        return art_id, 0, img_url

broken = []
print(f"Checking {len(art_urls)} image URLs in parallel...")
with ThreadPoolExecutor(max_workers=20) as ex:
    futures = {ex.submit(check, aid, url): aid for aid, url in art_urls.items()}
    for fut in as_completed(futures):
        art_id, status, url = fut.result()
        if status != 200:
            broken.append((art_id, status, url))

broken.sort()
if broken:
    print(f"\n❌ BROKEN ({len(broken)} articles):")
    for art_id, status, url in broken:
        print(f"  article{art_id:3d}: HTTP {status} — {url.split('photo-')[1][:30]}")
else:
    print("\n✅ All image URLs return HTTP 200!")
