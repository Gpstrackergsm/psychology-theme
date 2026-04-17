import os
import re

BASE_DIR = "/Users/khalidaitelmaati/Desktop/scrapy-master/psychology-theme-main"
HUB_FILE = os.path.join(BASE_DIR, "neuroscience-hub.html")

orphans = [
    'article268.html', 'article263.html', 'article261.html', 'article271.html', 
    'article272.html', 'article254.html', 'article269.html', 'article281.html', 
    'article270.html', 'article255.html'
]

def extract_meta(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
        title = title_match.group(1) if title_match else "Latest Research Article"
        
        desc_match = re.search(r'<meta[^>]*name="description"[^>]*content="([^"]*)"', content, re.IGNORECASE)
        if not desc_match:
            desc_match = re.search(r'<meta[^>]*content="([^"]*)"[^>]*name="description"', content, re.IGNORECASE)
        desc = desc_match.group(1) if desc_match else "Read our latest peer-reviewed breakdown."
        
        img_match = re.search(r'src="(https://images\.unsplash\.com/[^"]+)"', content, re.IGNORECASE)
        img = img_match.group(1) if img_match else "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&q=80&w=400"
        
        return title, desc, img
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return None, None, None

def main():
    new_cards_html = ""
    for filename in orphans:
        filepath = os.path.join(BASE_DIR, filename)
        if not os.path.exists(filepath):
            continue
            
        title, desc, img = extract_meta(filepath)
        clean_url = filename.replace('.html', '')
        
        card_html = f"""
                <div class="hub-card">
                    <div class="hub-card-img" style="background-image: url('{img}');" loading="lazy"></div>
                    <div class="hub-card-content">
                        <h3 class="hub-card-title">{title}</h3>
                        <p class="hub-card-desc">{desc}</p>
                        <a href="{clean_url}" class="hub-card-link">Read Research &rarr;</a>
                    </div>
                </div>"""
        new_cards_html += card_html

    with open(HUB_FILE, 'r', encoding='utf-8') as f:
        hub_content = f.read()
        
    # Inject right before the end of the clinical-grid
    target_tag = '</div>\n        </div>\n    </section>\n\n    <section class="hub-section" style="background: #f8f9fa;">'
    
    if target_tag in hub_content:
        new_hub_content = hub_content.replace(target_tag, new_cards_html + '\n' + target_tag)
        with open(HUB_FILE, 'w', encoding='utf-8') as f:
            f.write(new_hub_content)
        print("Successfully injected 10 orphan articles into the Neuroscience Hub.")
    else:
        # Fallback target
        fallback_target = 'id="clinical-grid">'
        if fallback_target in hub_content:
             new_hub_content = hub_content.replace(fallback_target, fallback_target + new_cards_html)
             with open(HUB_FILE, 'w', encoding='utf-8') as f:
                 f.write(new_hub_content)
             print("Successfully injected 10 orphan articles into the Neuroscience Hub (fallback location).")
        else:
             print("Failed to find insertion point in neuroscience-hub.html")

if __name__ == "__main__":
    main()
