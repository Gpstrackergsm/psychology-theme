import os

BASE_DIR = "/Users/khalidaitelmaati/Desktop/scrapy-master/psychology-theme-main"
OLD_URL = "https://images.unsplash.com/photo-1559839734-2b71f1536783?auto=format&fit=crop&q=80&w=200"
NEW_URL = "https://images.unsplash.com/photo-1643297654416-05795d62e39c?auto=format&fit=crop&q=80&w=200"

def fix_bio_images():
    files = [f for f in os.listdir(BASE_DIR) if f.startswith("article") and f.endswith(".html")]
    print(f"Checking {len(files)} articles for broken bio image...")
    
    count = 0
    for file_name in files:
        file_path = os.path.join(BASE_DIR, file_name)
        with open(file_path, 'r') as f:
            content = f.read()
        
        if OLD_URL in content:
            updated_content = content.replace(OLD_URL, NEW_URL)
            with open(file_path, 'w') as f:
                f.write(updated_content)
            count += 1
            if count % 20 == 0:
                print(f"Fixed {count} articles...")

    print(f"Success! Fixed broken image in {count} articles.")

if __name__ == "__main__":
    fix_bio_images()
