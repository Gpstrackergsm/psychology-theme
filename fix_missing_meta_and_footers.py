import os

BASE_DIR = "/Users/khalidaitelmaati/Desktop/scrapy-master/psychology-theme-main"

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

def fix_footers():
    files_to_fix = ["article277.html", "article278.html", "article279.html", "article280.html"]
    
    for filename in files_to_fix:
        filepath = os.path.join(BASE_DIR, filename)
        if not os.path.exists(filepath):
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Try to find the existing footer
        import re
        content_new = re.sub(r'<footer.*?</footer>', STANDARD_FOOTER, content, flags=re.DOTALL)
        
        if content_new == content:
            # If no footer tag, append before scripts
            content_new = content.replace('<script src="js/main.js"></script>', STANDARD_FOOTER + '\n<script src="js/main.js"></script>')
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content_new)
        print(f"Fixed footer in {filename}")

def fix_meta():
    files = {
        "terms.html": '<meta name="description" content="Terms and Conditions for using the Mind & Balance website. Read our policies regarding content usage, privacy, and user agreements."/>',
        "404.html": '<meta name="description" content="Page not found. Return to the Mind & Balance homepage to explore neuroscience and psychology articles."/>'
    }
    
    for filename, meta_tag in files.items():
        filepath = os.path.join(BASE_DIR, filename)
        if not os.path.exists(filepath):
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if '<meta name="description"' not in content:
            content_new = content.replace('</head>', f'    {meta_tag}\n</head>')
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content_new)
            print(f"Fixed meta description in {filename}")

if __name__ == "__main__":
    fix_footers()
    fix_meta()
