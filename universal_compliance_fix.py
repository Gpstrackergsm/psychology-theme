import os
import re

BASE_DIR = "/Users/khalidaitelmaati/Desktop/scrapy-master/psychology-theme-main"
ADSENSE_CODE = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6659437008463310" crossorigin="anonymous"></script>'
FOOTER_LINKS = """
<div style="margin-top: 1rem;">
    <a href="index.html" style="color: #ccc; margin: 0 10px; text-decoration: none;">Home</a>
    <a href="about.html" style="color: #ccc; margin: 0 10px; text-decoration: none;">About</a>
    <a href="contact.html" style="color: #ccc; margin: 0 10px; text-decoration: none;">Contact</a>
    <a href="privacy-policy.html" style="color: white; margin: 0 10px; text-decoration: none;">Privacy Policy</a>
    <a href="terms.html" style="color: #ccc; margin: 0 10px; text-decoration: none;">Terms</a>
</div>"""

def universal_fix():
    files = [f for f in os.listdir(BASE_DIR) if f.endswith(".html")]
    print(f"Executing Universal Fix on {len(files)} files...")
    
    for file_name in files:
        file_path = os.path.join(BASE_DIR, file_name)
        with open(file_path, 'r') as f:
            content = f.read()

        # 1. FORCE ADSENSE CODE INTO HEAD
        if 'ca-pub-6659437008463310' not in content:
            if '</head>' in content:
                content = content.replace('</head>', f'    {ADSENSE_CODE}\n</head>')
        
        # 2. FORCE PRIVACY LINK INTO FOOTER
        if 'privacy-policy.html' not in content:
            if '</footer>' in content:
                # We find the container in the footer or just before </footer>
                content = content.replace('</footer>', f'    {FOOTER_LINKS}\n</footer>')
            elif '&copy;' in content:
                # Fallback for pages with simple footers
                content = re.sub(r'(&copy;.*?)(</body>)', f'\\1\n{FOOTER_LINKS}\n\\2', content, flags=re.DOTALL)

        with open(file_path, 'w') as f:
            f.write(content)

    print("Universal Fix complete. Re-auditing...")

if __name__ == "__main__":
    universal_fix()
