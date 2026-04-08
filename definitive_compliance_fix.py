import os
import re

BASE_DIR = "/Users/khalidaitelmaati/Desktop/scrapy-master/psychology-theme-main"
# Fixed AdSense snippet that matches what's already there or needs to be there
ADSENSE_CODE = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6659437008463310" crossorigin="anonymous"></script>'
FOOTER_LINKS = """
<footer style="background: var(--text-primary); color: white; padding: 4rem 0; margin-top: 4rem; text-align: center;">
    <div class="container">
        <p>&copy; 2026 Mind & Balance. All rights reserved.</p>
        <div style="margin-top: 1rem;">
            <a href="index.html" style="color: #ccc; margin: 0 10px; text-decoration: none;">Home</a>
            <a href="about.html" style="color: #ccc; margin: 0 10px; text-decoration: none;">About</a>
            <a href="contact.html" style="color: #ccc; margin: 0 10px; text-decoration: none;">Contact</a>
            <a href="privacy-policy.html" style="color: white; margin: 0 10px; text-decoration: none;">Privacy Policy</a>
            <a href="terms.html" style="color: #ccc; margin: 0 10px; text-decoration: none;">Terms</a>
        </div>
    </div>
</footer>"""

def definitive_fix():
    files = [f for f in os.listdir(BASE_DIR) if f.endswith(".html")]
    print(f"Executing Definitive Fix on {len(files)} files...")
    
    for file_name in files:
        file_path = os.path.join(BASE_DIR, file_name)
        with open(file_path, 'r') as f:
            content = f.read()

        # 1. ADSENSE CHECK
        if 'ca-pub-6659437008463310' not in content:
            if '</head>' in content:
                content = content.replace('</head>', f'    {ADSENSE_CODE}\n</head>')
        
        # 2. PRIVACY LINK CHECK (AGGRESSIVE)
        if 'privacy-policy.html' not in content:
            # First try to replace existing footer
            if '<footer' in content and '</footer>' in content:
                content = re.sub(r'<footer.*?>.*?</footer>', FOOTER_LINKS, content, flags=re.DOTALL)
            # Second try: Replace copyright block
            elif '&copy;' in content:
                 content = re.sub(r'(&copy;.*?)(</body>)', f'\\1\n{FOOTER_LINKS}\n\\2', content, flags=re.DOTALL)
            # Final fallback: Just before body close
            elif '</body>' in content:
                content = content.replace('</body>', f'{FOOTER_LINKS}\n</body>')

        with open(file_path, 'w') as f:
            f.write(content)

    print("Definitive Fix complete. Re-auditing...")

if __name__ == "__main__":
    definitive_fix()
