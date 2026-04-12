import os
import re
import json

BASE_DIR = "."
INDEX_FILE = "index.html"

def inject_rich_results():
    article_files = [f for f in os.listdir(BASE_DIR) if f.startswith('article') and f.endswith('.html')]
    
    # 1. Update index.html with Enhanced Sitelinks Schema
    if os.path.exists(INDEX_FILE):
        with open(INDEX_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Define SiteNavigationElement Schema
        navigation_schema = '''
    <!-- Schema.org: SiteNavigationElement (Prompts Rich Sitelinks in Google) -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "ItemList",
      "name": "Main Navigation",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Neuroscience Hub",
          "url": "https://leafanoo.com/neuroscience-hub.html"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "Essential Reads",
          "url": "https://leafanoo.com/#articles"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "About Dr. Aria Martinez",
          "url": "https://leafanoo.com/about.html"
        },
        {
          "@type": "ListItem",
          "position": 4,
          "name": "Contact Us",
          "url": "https://leafanoo.com/contact.html"
        },
        {
          "@type": "ListItem",
          "position": 5,
          "name": "Privacy & Compliance",
          "url": "https://leafanoo.com/privacy-policy.html"
        }
      ]
    }
    </script>
'''
        # Inject before </head>
        if '</head>' in content and 'Main Navigation' not in content:
            content = content.replace('</head>', navigation_schema + '\n</head>')
            with open(INDEX_FILE, 'w', encoding='utf-8') as f:
                f.write(content)
            print("Successfully injected Navigation Schema into index.html")

    # 2. Inject BreadcrumbList into all Articles
    print(f"Injecting Breadcrumbs into {len(article_files)} articles...")
    for fname in article_files:
        fpath = os.path.join(BASE_DIR, fname)
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip if already has BreadcrumbList
        if 'BreadcrumbList' in content:
            continue
            
        # Extract Title and Category for Breadcrumbs
        title_match = re.search(r'<title>(.*?) \| Mind &amp; Balance</title>', content) or re.search(r'<title>(.*?)</title>', content)
        cat_match = re.search(r'<span class="card-category"[^>]*>(.*?)</span>', content)
        
        title = title_match.group(1).split('|')[0].strip() if title_match else "Article"
        category = cat_match.group(1).strip() if cat_match else "Psychology"
        
        breadcrumb_schema = f'''
    <!-- Schema.org: BreadcrumbList (Rich Results in Google) -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": [
        {{
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://leafanoo.com/"
        }},
        {{
          "@type": "ListItem",
          "position": 2,
          "name": "{category}",
          "item": "https://leafanoo.com/#articles"
        }},
        {{
          "@type": "ListItem",
          "position": 3,
          "name": "{title}",
          "item": "https://leafanoo.com/{fname}"
        }}
      ]
    }}
    </script>
'''
        # Inject before </head>
        if '</head>' in content:
            content = content.replace('</head>', breadcrumb_schema + '\n</head>')
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)

    print("Successfully injected Breadcrumb Schema into all articles.")

if __name__ == "__main__":
    inject_rich_results()
