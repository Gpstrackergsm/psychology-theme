import glob, os, csv
from bs4 import BeautifulSoup

BASE_DIR = '/Users/khalidaitelmaati/Desktop/scrapy-master/psychology-theme-main'
files = sorted(glob.glob(os.path.join(BASE_DIR, 'article*.html')))

csv_file = os.path.join(BASE_DIR, 'pinterest_all_pins.csv')

with open(csv_file, mode='w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Article File', 'Title', 'Description', 'Link', 'Board', 'Image Generation Prompt (DALL-E/Midjourney)'])
    
    for fp in files:
        fname = os.path.basename(fp)
        html = open(fp, encoding='utf-8').read()
        soup = BeautifulSoup(html, 'html.parser')
        
        # Get Title
        title_tag = soup.find('h1')
        if title_tag:
            title = title_tag.get_text(strip=True)
        else:
            title_tag = soup.find('title')
            title = title_tag.get_text(strip=True).split('|')[0].strip() if title_tag else "Psychology Article"
            
        # Get Description snippet
        intro = soup.find('section', class_='article-intro')
        snippet = ""
        if intro:
            p_tags = intro.find_all('p')
            if p_tags:
                snippet = p_tags[0].get_text(strip=True)
                # Keep it under ~300 characters for a punchy Pinterest description
                if len(snippet) > 250:
                    snippet = snippet[:247] + "..."
        
        description = f"{title}. {snippet} Click to read the full comprehensive guide on the neuroscience and psychology behind this. 🧠✨ #MentalHealth #Psychology #SelfCare #Wellness"
        
        link = f"https://leafanoo.com/{fname.replace('.html', '')}"
        board = "Mental Health & Psychology"
        
        # Image prompt
        prompt = f'A vertical 2:3 ratio Pinterest pin design. The background is a beautiful, serene abstract digital art piece representing mental clarity and peace. At the top center of the image, the text "{title}" is written in bold, large, clean, modern white typography. Below it, the text "leafanoo.com" is written in small, elegant font. The typography must be perfectly legible, spell the words exactly as provided, and stand out clearly against the background.'
        
        writer.writerow([fname, title, description, link, board, prompt])

print(f"Successfully generated {csv_file} with {len(files)} rows!")
