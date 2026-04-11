import os
import csv

BASE_DIR = "."
INDEX_PATH = "index.html"
CSV_PATH = "/Users/khalidaitelmaati/Desktop/scrapy-master/leafanoo_adsense_bot/leafanoo_content_calendar.csv"

def update_index():
    with open(CSV_PATH, 'r', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
    
    batch_rows = rows[20:45]
    new_cards = ""
    for i, row in enumerate(batch_rows):
        art_id = 226 + i
        title = row['Leafanoo_AdSense_Title']
        category = row['Category'] if row['Category'] else "Neuroscience"
        desc = row['Idea_Summary']
        
        new_cards += f'''
            <article class="card hidden delay-1">
                <div class="card-img" style="background-image: url('https://images.unsplash.com/photo-1559757148-5c350d0d3c56?auto=format&fit=crop&q=80&w=400');"></div>
                <div class="card-content">
                    <span class="card-category">{category}</span>
                    <h3 class="card-title">{title}</h3>
                    <p class="card-excerpt">{desc[:120]}...</p>
                    <a href="article{art_id}.html" class="card-link">Read More &rarr;</a>
                </div>
            </article>'''

    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    
    last_pos = content.rfind('</article>')
    if last_pos != -1:
        content = content[:last_pos + 10] + new_cards + content[last_pos + 10:]
        with open(INDEX_PATH, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated index.html with Batch 12 cards.")

if __name__ == "__main__":
    update_index()
