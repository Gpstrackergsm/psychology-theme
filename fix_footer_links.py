import os

BASE_DIR = "/Users/khalidaitelmaati/Desktop/scrapy-master/psychology-theme-main"

def fix_links_in_file(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    # Define the standardized footer block
    # We look for the closing footer or the footer link section
    # Most articles have a simple footer at the bottom
    
    # We want to replace the existing footer links with standardized ones
    standard_footer = """    <footer style="background: var(--text-primary); color: white; padding: 4rem 0; margin-top: 4rem; text-align: center;">
        <div class="container">
            <p>&copy; 2026 Mind & Balance. All rights reserved.</p>
            <div style="margin-top: 1rem;">
                <a href="index.html" style="color: #ccc; margin: 0 10px; text-decoration: none;">Home</a>
                <a href="about.html" style="color: #ccc; margin: 0 10px; text-decoration: none;">About</a>
                <a href="contact.html" style="color: #ccc; margin: 0 10px; text-decoration: none;">Contact</a>
                <a href="privacy-policy.html" style="color: #ccc; margin: 0 10px; text-decoration: none;">Privacy Policy</a>
                <a href="terms.html" style="color: #ccc; margin: 0 10px; text-decoration: none;">Terms</a>
            </div>
        </div>
    </footer>"""

    # Target the entire footer tag and its content
    if "<footer" in content and "</footer>" in content:
        import re
        # This regex matches the entire footer block
        new_content = re.sub(r'<footer.*?>.*?</footer>', standard_footer, content, flags=re.DOTALL)
        
        with open(file_path, 'w') as f:
            f.write(new_content)
        return True
    return False

def fix_all_links():
    files = [f for f in os.listdir(BASE_DIR) if f.endswith(".html")]
    print(f"Standardizing footer links in {len(files)} files...")
    
    count = 0
    for file_name in files:
        file_path = os.path.join(BASE_DIR, file_name)
        if fix_links_in_file(file_path):
            count += 1
            if count % 20 == 0:
                print(f"Fixed {count} files...")

    print(f"Success! Standardized footer links in {count} files.")

if __name__ == "__main__":
    fix_all_links()
