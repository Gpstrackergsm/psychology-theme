import glob, os
from bs4 import BeautifulSoup

BASE_DIR = '/Users/khalidaitelmaati/Desktop/scrapy-master/psychology-theme-main'
files = glob.glob(os.path.join(BASE_DIR, 'article*.html'))

fixed_layout_count = 0
fixed_js_count = 0

for fp in files:
    try:
        html_content = open(fp, encoding='utf-8').read()
        soup = BeautifulSoup(html_content, 'html.parser')
        changed = False
        
        # Fix Layout: Move sections from <main class="article-layout"> into <div class="article-body">
        main = soup.find('main')
        if main and main.get('class') and 'article-layout' in main.get('class'):
            body_div = main.find('div', class_='article-body')
            if body_div:
                # Get all section tags that are direct children of main
                sections_to_move = [child for child in main.find_all('section', recursive=False)]
                if sections_to_move:
                    for sec in sections_to_move:
                        sec.extract()
                        body_div.append(sec)
                    changed = True
                    fixed_layout_count += 1
                    
        # Fix Missing JS
        if not soup.find('script', src='js/main.js'):
            # Only add it if it's not present
            body = soup.find('body')
            if body:
                script_tag = soup.new_tag('script', src='js/main.js')
                # Insert right before the closing body tag, or append
                body.append(script_tag)
                changed = True
                fixed_js_count += 1

        if changed:
            with open(fp, 'w', encoding='utf-8') as f:
                f.write(str(soup))
                
    except Exception as e:
        print(f"Error processing {os.path.basename(fp)}: {e}")

print(f"Fixed flexbox layout in {fixed_layout_count} files.")
print(f"Added missing js/main.js in {fixed_js_count} files.")
