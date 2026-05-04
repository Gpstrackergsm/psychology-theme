#!/usr/bin/env python3
"""
fix_adsense_rejection.py
========================
Fixes the 4 causes of Google AdSense rejection on leafanoo.com:

1. ❌ Removes template-spam sections injected by generate_content.py
   (These make every article look identical — the #1 AdSense rejection cause)

2. ❌ Fixes the author image bug (hero image used as author photo in byline)

3. ❌ Standardizes author name to Dr. Maya Ariston, PhD everywhere

4. ❌ Removes duplicate footer blocks

Run: python3 fix_adsense_rejection.py
"""

import os
import glob
from bs4 import BeautifulSoup

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# The correct author photo (a real-looking portrait from Unsplash)
AUTHOR_IMG = "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&q=80&w=80&h=80"
AUTHOR_NAME = "Dr. Maya Ariston, PhD"
AUTHOR_TITLE = "Clinical Psychologist & Editor-in-Chief"
AUTHOR_URL = "https://leafanoo.com/about"

# CSS classes that identify the template-spam sections added by generate_content.py
SPAM_CLASSES = [
    "article-intro",
    "neuroscience-section",
    "psychological-framework",
    "case-study",
    "research-evidence",
    "myths-section",
    "action-guide",
    "expert-insights",
    "conclusion-section",
]

def fix_article(filepath):
    """Apply all fixes to a single article HTML file."""
    filename = os.path.basename(filepath)
    changes = []

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    soup = BeautifulSoup(content, "html.parser")

    # ── FIX 1: Remove template-spam sections ──────────────────────────────────
    removed_count = 0
    for cls in SPAM_CLASSES:
        # Match sections with exact class or class as one of multiple classes
        for tag in soup.find_all("section", class_=cls):
            tag.decompose()
            removed_count += 1

    if removed_count > 0:
        changes.append(f"removed {removed_count} template-spam section(s)")

    # ── FIX 2: Fix author image in byline (article-meta section) ─────────────
    # The bug: article hero image URL is used as author photo in the byline
    meta_div = soup.find("div", class_="article-meta")
    if meta_div:
        author_img = meta_div.find("img")
        if author_img:
            current_src = author_img.get("src", "")
            # Check if it's a landscape/hero image being used as author photo
            # (all hero images are wide format: w=1200; author photos use w=80 or w=100)
            if "w=1200" in current_src or ("w=" not in current_src and current_src != AUTHOR_IMG):
                author_img["src"] = AUTHOR_IMG
                author_img["alt"] = f"{AUTHOR_NAME} — {AUTHOR_TITLE}"
                author_img["style"] = "width:44px;height:44px;border-radius:50%;object-fit:cover;"
                changes.append("fixed author photo in byline")

        # Fix author name in byline span
        for span in meta_div.find_all("span"):
            text = span.get_text()
            if "Editorial Team" in text or (
                "By " in text and AUTHOR_NAME not in text
            ):
                span.string = f"By {AUTHOR_NAME}"
                changes.append("fixed author name in byline")
                break

    # ── FIX 3: Fix author name in JSON-LD schema ──────────────────────────────
    import re, json
    for script in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(script.string)
            modified = False
            # Handle single object or array
            items = data if isinstance(data, list) else [data]
            for item in items:
                if item.get("@type") == "Article":
                    author = item.get("author", {})
                    if author.get("name") and author["name"] != AUTHOR_NAME:
                        author["name"] = AUTHOR_NAME
                        author["url"] = AUTHOR_URL
                        modified = True
            if modified:
                script.string = json.dumps(data if isinstance(data, list) else items[0], indent=2)
                changes.append("fixed author name in JSON-LD schema")
        except Exception:
            pass

    # ── FIX 4: Remove duplicate footer blocks ────────────────────────────────
    footers = soup.find_all("footer")
    if len(footers) > 1:
        # Keep first footer, remove the rest
        for extra_footer in footers[1:]:
            extra_footer.decompose()
        changes.append(f"removed {len(footers)-1} duplicate footer(s)")

    # ── FIX 4b: Remove duplicate privacy/terms link divs after footer ─────────
    # Look for the pattern: <div style="margin-top:1rem;text-align:center;"><a href="privacy-policy.html">
    for div in soup.find_all("div"):
        style = div.get("style", "")
        if "margin-top:1rem" in style.replace(" ", "") and "text-align:center" in style.replace(" ", ""):
            links = div.find_all("a")
            hrefs = [a.get("href", "") for a in links]
            if any("privacy-policy" in h for h in hrefs) and any("terms" in h for h in hrefs):
                # This is a duplicate legal links div inside or after footer
                div.decompose()
                changes.append("removed duplicate legal links div")
                break

    # ── Write output only if changes were made ────────────────────────────────
    if changes:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(str(soup))
        print(f"✅ {filename}: {', '.join(changes)}")
        return True
    else:
        print(f"⏭️  {filename}: no changes needed")
        return False


def run():
    files = sorted(glob.glob(os.path.join(BASE_DIR, "article*.html")))
    print(f"🔍 Found {len(files)} article files\n")

    fixed = 0
    unchanged = 0
    for fp in files:
        result = fix_article(fp)
        if result:
            fixed += 1
        else:
            unchanged += 1

    print(f"\n{'='*60}")
    print(f"✅ Fixed:     {fixed} articles")
    print(f"⏭️  Unchanged: {unchanged} articles")
    print(f"\n🚀 Next steps:")
    print(f"   1. Review a few articles manually to confirm the fix looks right")
    print(f"   2. git add -A && git commit -m 'fix: remove template spam, fix author info'")
    print(f"   3. git push  →  Vercel will auto-deploy")
    print(f"   4. Wait 48h, then re-submit in your AdSense dashboard")


if __name__ == "__main__":
    run()
