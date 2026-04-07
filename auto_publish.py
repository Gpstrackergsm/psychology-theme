import csv
import os
import datetime

# Paths
BASE_DIR = "/Users/khalidaitelmaati/Desktop/scrapy-master/psychology-theme-main"
CSV_PATH = "/Users/khalidaitelmaati/Desktop/scrapy-master/leafanoo_adsense_bot/leafanoo_content_calendar.csv"
INDEX_PATH = os.path.join(BASE_DIR, "index.html")
SITEMAP_PATH = os.path.join(BASE_DIR, "sitemap.xml")

def get_next_article_id():
    files = os.listdir(BASE_DIR)
    max_id = 0
    for f in files:
        if f.startswith("article") and f.endswith(".html"):
            try:
                num = int(f.replace("article", "").replace(".html", ""))
                max_id = max(max_id, num)
            except:
                pass
    return max_id + 1

def build_article_html(article_id, title, category, meta_desc, content):
    date_str = datetime.datetime.now().strftime("%B %d, %Y")
    
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Mind &amp; Balance</title>
    <meta name="description" content="{meta_desc.replace('"', '&quot;')}">
    <link rel="stylesheet" href="css/style.css">
    <link rel="icon" type="image/svg+xml" href="images/favicon.svg">
    <meta property="og:title" content="{title} | Mind &amp; Balance">
    <meta property="og:description" content="{meta_desc.replace('"', '&quot;')}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://leafanoo.com/article{article_id}.html">
    <meta property="og:image" content="https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&q=80&w=1200">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title} | Mind &amp; Balance">
    <!-- Google Tag Manager -->
    <script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':
    new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
    'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
    }})(window,document,'script','dataLayer','GTM-MWJD24QX');</script>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6659437008463310" crossorigin="anonymous"></script>
</head>
<body>
    <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-MWJD24QX" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
    <div class="progress-container"><div class="progress-bar" id="progress-bar"></div></div>
    <header>
        <nav class="nav-container">
            <div class="logo">Mind &amp; Balance</div>
            <div class="nav-right">
                <ul class="nav-links">
                    <li><a href="index.html">Home</a></li>
                    <li><a href="index.html#articles" class="active">Articles</a></li>
                </ul>
                <button id="theme-toggle" class="theme-toggle" aria-label="Toggle Dark Mode">🌙</button>
            </div>
        </nav>
    </header>

    <div class="article-header hidden">
        <div class="container">
            <span class="card-category" style="display:block; margin-bottom:1rem;">{category}</span>
            <h1 style="font-size: 3rem; max-width: 800px; margin: 0 auto;">{title}</h1>
            <div class="article-meta">
                <span>Auto-Curated Trend</span>
                <span>•</span>
                <span>{date_str}</span>
            </div>
        </div>
    </div>

    <div class="ad-container ad-leaderboard hidden delay-1"></div>

    <div class="article-layout">
        <main class="article-body hidden delay-2">
            <h2>Introduction</h2>
            <p>We tracked this trending psychological concept based on what audiences are deeply concerned about today. Here is the framework:</p>
            <blockquote>{content}</blockquote>
            <p>[PLACEHOLDER: Deepen the article here based on the excerpt. Write 5 paragraphs expanding on the psychological implications.]</p>
            
            <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
            
            <h2>Key Takeaways</h2>
            <ul>
                <li>[Write takeaway 1]</li>
                <li>[Write takeaway 2]</li>
                <li>[Write takeaway 3]</li>
            </ul>
        </main>
    </div>
    <script src="js/main.js"></script>
</body>
</html>"""

def main():
    if not os.path.exists(CSV_PATH):
        print(f"Missing {CSV_PATH}")
        return
        
    articles_data = []
    with open(CSV_PATH, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            if i >= 3: break
            articles_data.append(row)
            
    if not articles_data: return
        
    start_id = get_next_article_id()
    new_cards_html = ""
    new_sitemap_xml = ""
    
    for idx, data in enumerate(articles_data):
        curr_id = start_id + idx
        title = data.get("Leafanoo_AdSense_Title", "")
        cat = data.get("Category", "Psychology")
        summary = data.get("Idea_Summary", "Summary text.")
        
        # Write HTML
        html_content = build_article_html(curr_id, title, cat, summary[:150], summary)
        filename = os.path.join(BASE_DIR, f"article{curr_id}.html")
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"✅ Generated article{curr_id}.html")
        
        # Build Card
        new_cards_html += f"""
            <article class="card hidden delay-1">
                <div class="card-img" style="background-image: url('https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&q=80&w=400');"></div>
                <div class="card-content">
                    <span class="card-category">{cat}</span>
                    <h3 class="card-title">{title}</h3>
                    <p class="card-excerpt">{summary[:100]}...</p>
                    <a href="article{curr_id}.html" class="card-link">Read More &rarr;</a>
                </div>
            </article>"""
            
        # Build Sitemap
        new_sitemap_xml += f"""    <url>\n        <loc>https://leafanoo.com/article{curr_id}.html</loc>\n        <changefreq>monthly</changefreq>\n        <priority>0.9</priority>\n    </url>\n"""
            
    # Inject into index.html
    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        idx_content = f.read()
    
    try:
        parts = idx_content.rsplit('<article class="card', 1)
        if len(parts) == 2:
            card_end = parts[1].find('</article>') + len('</article>')
            pre = parts[0] + '<article class="card' + parts[1][:card_end]
            post = parts[1][card_end:]
            idx_content = pre + new_cards_html + post
            with open(INDEX_PATH, 'w', encoding='utf-8') as f:
                f.write(idx_content)
            print("✅ Updated index.html with new articles!")
        else:
             print("Could not parse index.html")
    except Exception as e:
        print("Error with index.html injection", e)

    # Inject into sitemap
    with open(SITEMAP_PATH, 'r', encoding='utf-8') as f:
        sitemap = f.read()
    sitemap = sitemap.replace('</urlset>', f'{new_sitemap_xml}</urlset>')
    with open(SITEMAP_PATH, 'w', encoding='utf-8') as f:
        f.write(sitemap)
    print("✅ Updated sitemap.xml!")

if __name__ == "__main__":
    main()
