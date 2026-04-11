import json
import os

def inject_cta():
    with open('neuro_articles_meta.json', 'r', encoding='utf-8') as f:
        articles = json.load(f)

    cta_html = '''
    <section class="hub-cta" style="margin-top: 4rem; background: linear-gradient(135deg, #2c3e50, #3498db); color: white; padding: 3rem; border-radius: 12px; text-align: center;">
        <h2 style="color: white; margin-top: 0;">Explore the Neuroscience Hub</h2>
        <p style="font-size: 1.1rem; opacity: 0.9; margin-bottom: 2rem;">Deep-dive into 50+ research-backed articles on brain science, neuro-plasticity, and cognitive design.</p>
        <a href="neuroscience-hub.html" style="background: white; color: #2c3e50; padding: 12px 30px; border-radius: 30px; text-decoration: none; font-weight: bold; transition: transform 0.3s ease; display: inline-block;">Visit the Hub &rarr;</a>
    </section>
    '''

    for a in articles:
        fpath = a['file']
        if not os.path.exists(fpath): continue
        
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'Visit the Hub' in content: continue # Already injected
        
        # Inject before the medical disclaimer or before footer
        if '</main>' in content:
            content = content.replace('</main>', cta_html + '</main>')
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Injected CTA into {fpath}")

if __name__ == "__main__":
    inject_cta()
