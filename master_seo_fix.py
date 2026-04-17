#!/usr/bin/env python3
"""
============================================================
  MASTER SEO FIX — leafanoo.com / Mind & Balance
  Fixes all 6 critical bugs identified in the SEO audit
============================================================
  Fix 1: Title tag truncation (Mind &amp;... → Mind & Balance)
  Fix 2: article281 canonical URL (remove .html extension)
  Fix 3: article281 nav links (.html → extensionless)
  Fix 4: article281 Ahrefs Analytics tag injection
  Fix 5: Sitemap duplicate entry for article281 + update lastmod
  Fix 6: Homepage duplicate WebSite schema removal
  Bonus: vercel.json cleanup for clean URL routing
  Bonus: Twitter card titles truncation fix
============================================================
"""

import os
import re
import glob
import shutil
from datetime import date

BASE = os.path.dirname(os.path.abspath(__file__))
TODAY = date.today().isoformat()

counters = {
    "titles_fixed": 0,
    "twitter_titles_fixed": 0,
    "og_titles_fixed": 0,
    "canonical_fixed": 0,
    "ahrefs_added": 0,
    "nav_html_fixed": 0,
    "sitemap_fixed": False,
    "schema_fixed": False,
    "vercel_fixed": False,
}

# ─────────────────────────────────────────────────────────
# HELPER
# ─────────────────────────────────────────────────────────
def read(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✅ Saved: {os.path.basename(path)}")

# ─────────────────────────────────────────────────────────
# FIX 1 + BONUS: Title tag truncation across ALL articles
# Pattern: "Mind &amp;..." → "Mind & Balance"
# Also fixes og:title and twitter:title truncation
# ─────────────────────────────────────────────────────────
print("\n" + "="*60)
print("FIX 1: Repairing truncated title tags across all articles")
print("="*60)

article_files = sorted(glob.glob(os.path.join(BASE, "article*.html")))

for filepath in article_files:
    content = read(filepath)
    original = content

    # Fix <title> truncation — "Mind &amp;..." or "Mind &..."
    # Pattern 1: ends with Mind &amp;...
    content = re.sub(
        r'(<title>[^<]+?\|\s*)Mind\s*&amp;\.\.\.',
        r'\1Mind &amp; Balance',
        content
    )
    # Pattern 2: ends with Mind &...  (unencoded)
    content = re.sub(
        r'(<title>[^<]+?\|\s*)Mind\s*&\.\.\.',
        r'\1Mind &amp; Balance',
        content
    )
    # Pattern 3: title ends with just "..." after the pipe
    content = re.sub(
        r'(<title>[^<]+?\|\s*Mind\s*&amp;)\.\.\.',
        r'\1 Balance',
        content
    )
    # Pattern 4: title just ends with "..."  no Mind at all (catch-all)
    content = re.sub(
        r'(<title>[^<]{30,}?)\.\.\.(</title>)',
        r'\1\2',
        content
    )

    # Fix og:title truncation
    content = re.sub(
        r'(property="og:title"\s+content="[^"]+?\|\s*)Mind\s*&amp;\.\.\."',
        r'\1Mind &amp; Balance"',
        content
    )
    content = re.sub(
        r'(content="[^"]+?\|\s*Mind\s*&amp;)\.\.\."(\s+property="og:title")',
        r'\1 Balance"\2',
        content
    )
    # og:title alternate attribute order
    content = re.sub(
        r'(property="og:title"[^>]*content="[^"]*)\.\.\."',
        r'\1"',
        content
    )

    # Fix twitter:title truncation
    content = re.sub(
        r'(name="twitter:title"\s+content="[^"]+?\|\s*)Mind\s*&amp;\.\.\."',
        r'\1Mind &amp; Balance"',
        content
    )
    content = re.sub(
        r'(name="twitter:title"[^>]*content="[^"]*)\.\.\."',
        r'\1"',
        content
    )
    # alternate order
    content = re.sub(
        r'(content="[^"]*)\.\.\."(\s+name="twitter:title")',
        r'\1"\2',
        content
    )

    if content != original:
        write(filepath, content)
        counters["titles_fixed"] += 1

print(f"  → Fixed title truncation in {counters['titles_fixed']} article files")


# ─────────────────────────────────────────────────────────
# FIX 2: article281 canonical — remove .html from URL
# ─────────────────────────────────────────────────────────
print("\n" + "="*60)
print("FIX 2: Fixing article281 canonical URL (remove .html)")
print("="*60)

a281_path = os.path.join(BASE, "article281.html")
if os.path.exists(a281_path):
    content = read(a281_path)
    original = content

    # Fix canonical
    content = content.replace(
        'href="https://leafanoo.com/article281.html"',
        'href="https://leafanoo.com/article281"'
    )
    # Fix og:url
    content = content.replace(
        'content="https://leafanoo.com/article281.html"',
        'content="https://leafanoo.com/article281"'
    )
    # Fix schema @id and item URLs
    content = content.replace(
        '"https://leafanoo.com/article281.html"',
        '"https://leafanoo.com/article281"'
    )
    # Fix breadcrumb schema URL
    content = content.replace(
        '"item": "https://leafanoo.com/article281.html"',
        '"item": "https://leafanoo.com/article281"'
    )
    # Fix about.html link in schema
    content = content.replace(
        '"url": "https://leafanoo.com/about.html"',
        '"url": "https://leafanoo.com/about"'
    )

    if content != original:
        write(a281_path, content)
        counters["canonical_fixed"] += 1
        print(f"  → article281.html canonical URLs fixed")
    else:
        print(f"  → article281.html canonical already correct")


# ─────────────────────────────────────────────────────────
# FIX 3: article281 nav links — remove .html extensions
# ─────────────────────────────────────────────────────────
print("\n" + "="*60)
print("FIX 3: Fixing article281 nav links (remove .html)")
print("="*60)

if os.path.exists(a281_path):
    content = read(a281_path)
    original = content

    # Fix nav links
    nav_html_map = {
        'href="index.html"': 'href="/"',
        'href="index.html#articles"': 'href="/#articles"',
        'href="neuroscience-hub.html"': 'href="neuroscience-hub"',
        'href="anxiety-relief-hub.html"': 'href="anxiety-relief-hub"',
        'href="behavioral-science-hub.html"': 'href="behavioral-science-hub"',
        'href="about.html"': 'href="about"',
        'href="contact.html"': 'href="contact"',
        'href="privacy-policy.html"': 'href="privacy-policy"',
        'href="terms.html"': 'href="terms"',
        'href="editorial-process.html"': 'href="editorial-process"',
    }

    for old, new in nav_html_map.items():
        if old in content:
            content = content.replace(old, new)
            counters["nav_html_fixed"] += 1

    if content != original:
        write(a281_path, content)
        print(f"  → Fixed {counters['nav_html_fixed']} nav link(s) in article281.html")
    else:
        print(f"  → article281.html nav links already correct")


# ─────────────────────────────────────────────────────────
# FIX 4: Add Ahrefs Analytics to article281
# ─────────────────────────────────────────────────────────
print("\n" + "="*60)
print("FIX 4: Adding Ahrefs Analytics to article281.html")
print("="*60)

AHREFS_TAG = '<!-- Ahrefs Analytics -->\n<script src="https://analytics.ahrefs.com/analytics.js" data-key="2qwvH/2JEccPb3SmA4RU5Q" async></script>\n<!-- End Ahrefs Analytics -->\n'

if os.path.exists(a281_path):
    content = read(a281_path)

    if 'analytics.ahrefs.com' not in content:
        # Insert before first GA4 script
        ga4_marker = '<!-- ✅ Google Analytics 4 -->'
        if ga4_marker in content:
            content = content.replace(ga4_marker, AHREFS_TAG + ga4_marker)
        else:
            # Fallback: insert after <head>
            content = content.replace('<head>\n', '<head>\n' + AHREFS_TAG)
        write(a281_path, content)
        counters["ahrefs_added"] += 1
        print(f"  → Ahrefs tag added to article281.html")
    else:
        print(f"  → Ahrefs tag already present in article281.html")


# ─────────────────────────────────────────────────────────
# FIX 5: Sitemap — remove duplicate article281.html entry
#         and update lastmod for article281 to today
# ─────────────────────────────────────────────────────────
print("\n" + "="*60)
print("FIX 5: Fixing sitemap.xml (duplicate article281 + lastmod)")
print("="*60)

sitemap_path = os.path.join(BASE, "sitemap.xml")
if os.path.exists(sitemap_path):
    content = read(sitemap_path)
    original = content

    # Remove the entire <url> block for article281.html (the .html duplicate)
    # Keep only the extensionless one
    dup_block_pattern = re.compile(
        r'\s*<url>\s*<loc>https://leafanoo\.com/article281\.html</loc>.*?</url>',
        re.DOTALL
    )
    content = dup_block_pattern.sub('', content)

    # Update lastmod for article281 (extensionless) to today
    content = re.sub(
        r'(<loc>https://leafanoo\.com/article281</loc>\s*<lastmod>)[^<]*(</lastmod>)',
        rf'\g<1>{TODAY}\g<2>',
        content
    )

    # Ensure article281 is in the sitemap if not present (add after article280)
    if 'leafanoo.com/article281<' not in content:
        insert_after = '</url>\n    <url>\n        <loc>https://leafanoo.com/article280</loc>'
        new_entry = f'''</url>
    <url>
        <loc>https://leafanoo.com/article281</loc>
        <lastmod>{TODAY}</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.9</priority>
    </url>
    <url>
        <loc>https://leafanoo.com/article280</loc>'''
        content = content.replace(insert_after.lstrip('</url>\n    '), new_entry.lstrip('</url>\n    '), 1)

    if content != original:
        write(sitemap_path, content)
        counters["sitemap_fixed"] = True
        print(f"  → sitemap.xml cleaned (duplicate removed, lastmod updated)")
    else:
        print(f"  → sitemap.xml already correct")


# ─────────────────────────────────────────────────────────
# FIX 6: Homepage — remove duplicate WebSite schema
# ─────────────────────────────────────────────────────────
print("\n" + "="*60)
print("FIX 6: Removing duplicate WebSite schema from index.html")
print("="*60)

index_path = os.path.join(BASE, "index.html")
if os.path.exists(index_path):
    content = read(index_path)
    original = content

    # Find all WebSite schema script blocks
    # Pattern: <!-- Schema.org: SitelinksSearchBox ... --> ... </script>
    sitelinks_block = re.compile(
        r'\s*<!--\s*Schema\.org:\s*SitelinksSearchBox[^>]*-->.*?</script>',
        re.DOTALL
    )
    matches = sitelinks_block.findall(content)

    if len(matches) >= 1:
        # Remove the SitelinksSearchBox block (duplicate of WebSite schema)
        content = sitelinks_block.sub('', content, count=1)
        write(index_path, content)
        counters["schema_fixed"] = True
        print(f"  → Duplicate SitelinksSearchBox WebSite schema removed from index.html")
    else:
        print(f"  → No duplicate WebSite schema found (already clean)")


# ─────────────────────────────────────────────────────────
# BONUS FIX A: vercel.json — ensure cleanUrls handles .html
# ─────────────────────────────────────────────────────────
print("\n" + "="*60)
print("BONUS: Updating vercel.json for clean URL handling")
print("="*60)

vercel_path = os.path.join(BASE, "vercel.json")
vercel_config = '''{
  "cleanUrls": true,
  "trailingSlash": false,
  "redirects": [
    { "source": "/article281.html", "destination": "/article281", "permanent": true },
    { "source": "/index.html", "destination": "/", "permanent": true },
    { "source": "/about.html", "destination": "/about", "permanent": true },
    { "source": "/contact.html", "destination": "/contact", "permanent": true },
    { "source": "/privacy-policy.html", "destination": "/privacy-policy", "permanent": true },
    { "source": "/terms.html", "destination": "/terms", "permanent": true },
    { "source": "/neuroscience-hub.html", "destination": "/neuroscience-hub", "permanent": true },
    { "source": "/anxiety-relief-hub.html", "destination": "/anxiety-relief-hub", "permanent": true },
    { "source": "/behavioral-science-hub.html", "destination": "/behavioral-science-hub", "permanent": true },
    { "source": "/editorial-process.html", "destination": "/editorial-process", "permanent": true }
  ],
  "routes": [
    { "handle": "filesystem" },
    { "src": "/(.*)", "dest": "/404.html", "status": 404 }
  ]
}
'''
write(vercel_path, vercel_config)
counters["vercel_fixed"] = True
print("  → vercel.json updated with 301 redirects for all .html pages")


# ─────────────────────────────────────────────────────────
# BONUS FIX B: Add hreflang to index.html
# ─────────────────────────────────────────────────────────
print("\n" + "="*60)
print("BONUS: Adding hreflang tags to index.html")
print("="*60)

if os.path.exists(index_path):
    content = read(index_path)

    if 'hreflang' not in content:
        hreflang = '''    <link rel="alternate" hreflang="en" href="https://leafanoo.com/" />
    <link rel="alternate" hreflang="x-default" href="https://leafanoo.com/" />
'''
        content = content.replace('<link rel="canonical"', hreflang + '    <link rel="canonical"', 1)
        write(index_path, content)
        print("  → hreflang tags added to index.html")
    else:
        print("  → hreflang already present in index.html")


# ─────────────────────────────────────────────────────────
# SUMMARY REPORT
# ─────────────────────────────────────────────────────────
print("\n" + "="*60)
print("✅  MASTER SEO FIX COMPLETE — SUMMARY")
print("="*60)
print(f"  📋 Title tags fixed:           {counters['titles_fixed']} article files")
print(f"  🔗 article281 canonical fixed:  {'Yes' if counters['canonical_fixed'] else 'Already OK'}")
print(f"  🔗 article281 nav links fixed:  {counters['nav_html_fixed']} links")
print(f"  📊 Ahrefs tag added:            {'Yes' if counters['ahrefs_added'] else 'Already present'}")
print(f"  🗺️  Sitemap fixed:               {'Yes' if counters['sitemap_fixed'] else 'Already OK'}")
print(f"  📑 Schema duplicate removed:    {'Yes' if counters['schema_fixed'] else 'Already OK'}")
print(f"  ⚙️  vercel.json updated:         {'Yes' if counters['vercel_fixed'] else 'Already OK'}")
print("\n  ⚠️  NEXT: Run expand_thin_articles.py to fix the 6 thin content pages")
print("  ⚠️  NEXT: git add -A && git commit -m 'fix: critical SEO fixes' && git push")
print("="*60)
