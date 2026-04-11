import os
import re

BASE_DIR = "."

def ultimate_repair():
    files = [f for f in os.listdir(BASE_DIR) if f.startswith('article') and f.endswith('.html')]
    
    hub_link_html = '<li><a href="neuroscience-hub.html">Neuro Hub</a></li>'
    
    cta_template = '''
    <section class="hub-cta" style="margin-top: 4rem; background: linear-gradient(135deg, #2c3e50, #3498db); color: white; padding: 3rem; border-radius: 12px; text-align: center;">
        <h2 style="color: white; margin-top: 0;">Explore the Neuroscience Hub</h2>
        <p style="font-size: 1.1rem; opacity: 0.9; margin-bottom: 2rem;">Deep-dive into 50+ research-backed articles on brain science, neuro-plasticity, and cognitive design.</p>
        <a href="neuroscience-hub.html" style="background: white; color: #2c3e50; padding: 12px 30px; border-radius: 30px; text-decoration: none; font-weight: bold; transition: transform 0.3s ease; display: inline-block;">Visit the Hub &rarr;</a>
    </section>
'''

    for fname in files:
        fpath = os.path.join(BASE_DIR, fname)
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. Navigation Fix
        if 'neuroscience-hub.html' not in content or 'Neuro Hub' not in content:
            content = content.replace('<li><a href="index.html">Home</a></li>', 
                                     '<li><a href="index.html">Home</a></li>\n                ' + hub_link_html)
        
        # 2. Extract and Remove any existing Hub CTA (wherever it is)
        # We target the class "hub-cta" specifically
        content = re.sub(r'<section class="hub-cta".*?</section>', '', content, flags=re.DOTALL)
        
        # 3. Clean up the messed up markup from previous runs
        # Fix the </div> closures that were misplaced
        content = re.sub(r'</div><div class=\'faq-item\'', r"<div class='faq-item'", content)
        content = content.replace('</div>\n            </div>\n        </div>\n        \n        <aside', '            </div>\n        </div>\n        \n        <aside')

        # 4. Relocate Hub CTA to a safe full-width spot
        # Safe spot is right before the disclaimer or the footer
        if '<div class="container disclaimer-banner"' in content:
            content = content.replace('<div class="container disclaimer-banner"', cta_template + '\n    <div class="container disclaimer-banner"')
        elif '<footer' in content:
            content = content.replace('<footer', cta_template + '\n    <footer')

        # 5. One more safety: Ensure content isn't squeezed
        # If article-body is still unclosed, it will bleed.
        # But moving CTA out of article-layout is the primary fix for the squeeze.
        
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
            
    print(f"Ultimate repair completed for {len(files)} articles.")

if __name__ == "__main__":
    ultimate_repair()
