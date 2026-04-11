import os
import re

BASE_DIR = "."

def fix_layout():
    files = [f for f in os.listdir(BASE_DIR) if f.startswith('article') and f.endswith('.html')]
    
    hub_link_html = '<li><a href="neuroscience-hub.html">Neuro Hub</a></li>'
    
    cta_pattern = re.compile(r'(<section class="hub-cta".*?</section>)', re.DOTALL)
    nav_pattern = re.compile(r'(<ul class="nav-links">.*?<li><a href="index.html">Home</a></li>)', re.DOTALL)
    
    for fname in files:
        fpath = os.path.join(BASE_DIR, fname)
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. Fix Navigation (Add Neuro Hub if missing)
        if hub_link_html not in content:
            content = content.replace('<li><a href="index.html">Home</a></li>', 
                                     '<li><a href="index.html">Home</a></li>\n                ' + hub_link_html)

        # 2. Extract CTA and relocate it outside the main flex container
        cta_match = cta_pattern.search(content)
        if cta_match:
            cta_html = cta_match.group(1)
            # Remove from original position
            content = content.replace(cta_html, "")
            # Re-insert after </main> but before disclaimer/footer
            if '</main>' in content:
                content = content.replace('</main>', '</main>\n\n' + cta_html)

        # 3. Fix the malformed </div> tags blocking content
        # I saw </div><div class='faq-item' ... in the middle of lines
        content = re.sub(r'</div><div class=\'faq-item\'', r"<div class='faq-item'", content)
        # Also fix double container closures
        content = content.replace('</div>\n            </div>\n        </div>\n        \n        <aside', '            </div>\n        </div>\n        \n        <aside')

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
            
    print(f"Fixed layout and navigation for {len(files)} articles.")

if __name__ == "__main__":
    fix_layout()
