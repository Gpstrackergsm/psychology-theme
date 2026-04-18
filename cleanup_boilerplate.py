import os
import glob
from bs4 import BeautifulSoup

BASE_DIR = "/Users/khalidaitelmaati/Desktop/scrapy-master/psychology-theme-main"

def clean_boilerplate():
    files = glob.glob(os.path.join(BASE_DIR, "article*.html"))
    cleaned_count = 0
    
    classes_to_remove = [
        "cognitive-flexibility",
        "neuro-depth",
        "evidence-block",
        "action-guide",
        "author-bio"
    ]
    
    for file_path in files:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        soup = BeautifulSoup(content, "html.parser")
        modified = False
        
        for cls in classes_to_remove:
            # Find all elements (section, div, etc) that have this class
            elements = soup.find_all(class_=cls)
            for el in elements:
                el.decompose()  # Remove the tag and its contents from the tree
                modified = True
                
        if modified:
            # We want to format it back nicely
            # Instead of prettify() which can mess up formatting, we will convert back to string
            new_html = str(soup)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_html)
            cleaned_count += 1
            
    print(f"✅ Successfully removed boilerplate content from {cleaned_count} articles.")

if __name__ == "__main__":
    clean_boilerplate()
