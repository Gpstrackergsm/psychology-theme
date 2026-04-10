#!/usr/bin/env python3
"""
Replace the 8 broken Unsplash IDs with verified-working alternatives across
all 180 article cards in index.html and all article HTML files.
"""
import os, re

BASE_DIR = "/Users/khalidaitelmaati/Desktop/scrapy-master/psychology-theme-main"
INDEX_PATH = os.path.join(BASE_DIR, "index.html")

# Broken ID → Working replacement (all verified HTTP 200)
REPLACEMENTS = {
    "1466471340190-98259d5a77c0": "1543269865-cbf427effbad",   # mushroom→hiking
    "1473641262803-ec5e10080644": "1552664730-d307ca884978",   # couple→night awake
    "1493132630797-4c5837dec5f0": "1507003211169-0a1dd7228f2d", # mirror→portrait
    "1512411546253-24151c727a81": "1544367567-0f2fcb009e0b",   # appetite→therapy couch
    "1520206183501-b80af970d7eb": "1558618666-fcd25c85cd64",   # sleep→neuron network
    "1536640175698-daff1379bd44": "1552053831-71594a27632d",   # cannabis→golden retriever
    "1584030373083-d2361ac95da9": "1541781774459-bb2af2f05b55", # therapy→anxiety face
    "1516589174184-c685ca33d2b0": "1508739773434-c26b3d09e071", # couple hands→DNA
    "1499750310107-5fef283666bb": "1484480974693-6ca0a78fb36b", # laptop→alarm clock
}

def patch_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    for old_id, new_id in REPLACEMENTS.items():
        content = content.replace(old_id, new_id)
    if content != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

# Patch index.html
changed = patch_file(INDEX_PATH)
print(f"index.html: {'✅ patched' if changed else 'no change'}")

# Patch all article files
files = [f for f in os.listdir(BASE_DIR) if re.match(r'article\d+\.html', f)]
patched = 0
for fname in files:
    if patch_file(os.path.join(BASE_DIR, fname)):
        patched += 1

print(f"Article files: ✅ {patched} patched")
print("\nDone! Run audit_images.py to verify.")
