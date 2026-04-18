import os
from bs4 import BeautifulSoup
import json

BASE_DIR = "/Users/khalidaitelmaati/Desktop/scrapy-master/psychology-theme-main"

def audit_adsense():
    files = [f for f in os.listdir(BASE_DIR) if f.endswith(".html")]
    
    report = {
        "total_files": len(files),
        "articles": 0,
        "thin_content_articles": [],
        "missing_titles": [],
        "missing_descriptions": [],
        "missing_footer_links": []
    }
    
    for file_name in files:
        file_path = os.path.join(BASE_DIR, file_name)
        with open(file_path, 'r', encoding='utf-8') as f:
            html = f.read()
            
        soup = BeautifulSoup(html, 'html.parser')
        
        if file_name.startswith("article"):
            report["articles"] += 1
            
            # Check word count of the main article body
            article_body = soup.find('main')
            if article_body:
                text = article_body.get_text(separator=' ')
                word_count = len(text.split())
                if word_count < 500:
                    report["thin_content_articles"].append({"file": file_name, "words": word_count})
            else:
                report["thin_content_articles"].append({"file": file_name, "words": 0, "reason": "No main.article-body tag found"})
        
        # Check meta tags
        title = soup.find('title')
        if not title or not title.get_text(strip=True):
            report["missing_titles"].append(file_name)
            
        desc = soup.find('meta', attrs={'name': 'description'})
        if not desc or not desc.get('content', '').strip():
            report["missing_descriptions"].append(file_name)
            
        # Check footer links (Privacy Policy, Terms)
        footer = soup.find('footer')
        if footer:
            footer_html = str(footer).lower()
            if "privacy policy" not in footer_html or "terms" not in footer_html:
                report["missing_footer_links"].append(file_name)
        else:
            report["missing_footer_links"].append(file_name)
            
    with open("adsense_audit_results_latest.json", "w") as f:
        json.dump(report, f, indent=4)
        
    print(f"Audit complete. Thin articles: {len(report['thin_content_articles'])}")
    print(f"Missing Footer Links: {len(report['missing_footer_links'])}")

if __name__ == "__main__":
    audit_adsense()
