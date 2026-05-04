import glob, os
from bs4 import BeautifulSoup

BASE_DIR = '/Users/khalidaitelmaati/Desktop/scrapy-master/psychology-theme-main'
files = glob.glob(os.path.join(BASE_DIR, 'article*.html'))

fixed_count = 0

for fp in files:
    try:
        html_content = open(fp, encoding='utf-8').read()
        soup = BeautifulSoup(html_content, 'html.parser')
        changed = False
        
        main = soup.find('main')
        if main and main.get('class') and 'article-layout' in main.get('class'):
            body_div = main.find('div', class_='article-body')
            if body_div:
                # 1. Extract all injected sections to preserve order at the bottom
                injected_classes = [
                    'article-intro', 'neuroscience-section', 'psychological-framework', 
                    'case-study', 'research-evidence', 'myths-section', 
                    'action-guide', 'expert-insights', 'conclusion-section', 'faq-section'
                ]
                
                injected_sections = []
                for cls in injected_classes:
                    sec = soup.find('section', class_=cls)
                    if sec:
                        sec.extract()
                        injected_sections.append(sec)
                
                # 2. Extract all dangling children of main (the rest of the old content)
                # and append them to body_div so everything is properly wrapped.
                children_to_move = [c for c in list(main.children) if c != body_div]
                for child in children_to_move:
                    child.extract()
                    body_div.append(child)
                
                # 3. Re-append the injected sections to the very bottom of body_div
                for sec in injected_sections:
                    body_div.append(sec)
                    
                changed = True
                fixed_count += 1

        if changed:
            with open(fp, 'w', encoding='utf-8') as f:
                f.write(str(soup))
                
    except Exception as e:
        print(f"Error processing {os.path.basename(fp)}: {e}")

print(f"Deep fixed layout in {fixed_count} files.")
