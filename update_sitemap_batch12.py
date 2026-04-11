import os

SITEMAP_PATH = "sitemap.xml"

def update_sitemap():
    new_entries = '    <url>\n        <loc>https://leafanoo.com/neuroscience-hub.html</loc>\n        <changefreq>weekly</changefreq>\n        <priority>0.9</priority>\n    </url>\n'
    for i in range(226, 251):
        new_entries += f'    <url>\n        <loc>https://leafanoo.com/article{i}.html</loc>\n        <changefreq>monthly</changefreq>\n        <priority>0.8</priority>\n    </url>\n'
    
    with open(SITEMAP_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '</urlset>' in content and 'neuroscience-hub.html' not in content:
        content = content.replace('</urlset>', new_entries + '</urlset>')
        with open(SITEMAP_PATH, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated sitemap.xml with Hub and Batch 12.")

if __name__ == "__main__":
    update_sitemap()
