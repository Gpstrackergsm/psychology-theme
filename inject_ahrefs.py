import os
import glob

BASE_DIR = "/Users/khalidaitelmaati/Desktop/scrapy-master/psychology-theme-main"
AHREFS_SNIPPET = """    <!-- Ahrefs Analytics -->
    <script src="https://analytics.ahrefs.com/analytics.js" data-key="2qwvH/2JEccPb3SmA4RU5Q" async></script>
    <!-- End Ahrefs Analytics -->"""

def inject_ahrefs_script():
    # Find all HTML files in the base directory
    html_files = glob.glob(os.path.join(BASE_DIR, "*.html"))
    print(f"Found {len(html_files)} HTML files to update.")
    
    updated_count = 0
    for file_path in html_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Avoid double injection
        if "analytics.ahrefs.com/analytics.js" in content:
            continue
            
        # Target the top of the head
        if "<head>" in content:
            updated_content = content.replace("<head>", f"<head>\n{AHREFS_SNIPPET}")
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            updated_count += 1
            print(f"Updated {os.path.basename(file_path)}")
        elif "<head " in content: 
            # some templates might have <head... >
            pass # we'll ignore this for now unless missed
            
    print(f"Successfully added Ahrefs tracking to {updated_count} files.")

if __name__ == "__main__":
    inject_ahrefs_script()
