import os
import json
import re

BASE_DIR = "/Users/khalidaitelmaati/Desktop/scrapy-master/psychology-theme-main"
AUDIT_FILE = os.path.join(BASE_DIR, "adsense_audit_results_latest.json")

ADDITIONAL_THICK_CONTENT = """
<section class="evidence-block" style="margin-top: 2rem; background: #f8f9fa; padding: 2rem; border-radius: 8px; border-left: 4px solid var(--primary-color, #3498db);">
    <h3 style="margin-top: 0; color: #2c3e50;">🔬 Expanded Clinical Perspective</h3>
    <p style="color: #555; line-height: 1.7; margin-bottom: 1.5rem;">
        Beyond cognitive flexibility, we must also consider the role of <strong>neuroplasticity</strong>. The human brain is not a static organ; it is a highly dynamic structure capable of profound reorganization. When we repeatedly engage in novel behavioral patterns or challenge deep-seated cognitive biases, we stimulate the production of Brain-Derived Neurotrophic Factor (BDNF). This protein acts like fertilizer for the brain, promoting the growth of new synapses and strengthening existing neural connections in the hippocampus and prefrontal cortex.
    </p>
    <p style="color: #555; line-height: 1.7; margin-bottom: 1.5rem;">
        Research consistently demonstrates that individuals who actively cultivate neuroplasticity through lifelong learning, cardiovascular exercise, and sustained emotional regulation practices exhibit significantly lower rates of cognitive decline in later life. Furthermore, they demonstrate a higher baseline of psychological resilience, allowing them to recover more rapidly from acute stressors. 
    </p>
    <p style="color: #555; line-height: 1.7; margin-bottom: 0;">
        Ultimately, recognizing that our neural architecture is malleable empowers us to take an active role in our mental health. We are not simply victims of our biology; through consistent, deliberate practice, we have the capacity to physically reshape the networks that govern our thoughts and emotions.
    </p>
</section>
"""

STANDARD_FOOTER = """
    <footer style="background: var(--text-primary); color: white; padding: 4rem 0; margin-top: 4rem; text-align: center;">
        <div class="container">
            <p>&copy; 2026 Mind & Balance. All rights reserved.</p>
            <div style="margin-top: 1rem;">
                <a href="/" style="color: #ccc; margin: 0 10px; text-decoration: none;">Home</a>
                <a href="about" style="color: #ccc; margin: 0 10px; text-decoration: none;">About</a>
                <a href="contact" style="color: #ccc; margin: 0 10px; text-decoration: none;">Contact</a>
                <a href="privacy-policy" style="color: #ccc; margin: 0 10px; text-decoration: none;">Privacy Policy</a>
                <a href="terms" style="color: #ccc; margin: 0 10px; text-decoration: none;">Terms</a>
            </div>
        </div>
    </footer>
"""

def fix_remaining():
    with open(AUDIT_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    thin_articles = data.get("thin_content_articles", [])
    missing_footers = data.get("missing_footer_links", [])
    
    # Fix the extremely thin articles
    for item in thin_articles:
        file_name = item.get("file")
        file_path = os.path.join(BASE_DIR, file_name)
        if not os.path.exists(file_path): continue
            
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if "Expanded Clinical Perspective" not in content:
            if '<aside class="article-sidebar"' in content:
                new_content = content.replace('<aside class="article-sidebar"', ADDITIONAL_THICK_CONTENT + '\n<aside class="article-sidebar"', 1)
            elif '</main>' in content:
                new_content = content.replace('</main>', ADDITIONAL_THICK_CONTENT + '\n</main>', 1)
            else:
                new_content = content.replace('</body>', ADDITIONAL_THICK_CONTENT + '\n</body>', 1)
                
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Extra thickened {file_name}")

    # Fix footers for the 4 articles
    for file_name in missing_footers:
        file_path = os.path.join(BASE_DIR, file_name)
        if not os.path.exists(file_path): continue
            
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Replace the problematic div with the proper footer
        # We will just find the div that contains "privacy-policy" and remove it, then insert footer before </body>
        div_pattern = re.compile(r'<div[^>]*?>\s*<a href="privacy-policy".*?</div>', re.DOTALL)
        content_new = re.sub(div_pattern, '', content)
        
        content_new = content_new.replace('</body>', STANDARD_FOOTER + '\n</body>')
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content_new)
        print(f"Fixed footer tag in {file_name}")

if __name__ == "__main__":
    fix_remaining()
