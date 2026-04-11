import os
import glob
import json
import re

def count_words(text):
    # Quick strip of HTML tags
    clean_text = re.sub(r'<[^>]+>', ' ', text)
    return len(clean_text.split())

def audit_articles():
    articles = glob.glob('article*.html')
    # Sort files naturally
    try:
        articles.sort(key=lambda x: int(re.search(r'\d+', x).group()) if re.search(r'\d+', x) else 0)
    except:
        pass
        
    total_articles = len(articles)
    
    issues = {
        'thin_content': [], # < 400 words
        'missing_author': [],
        'missing_faq': [],
        'missing_schema': [],
        'missing_evidence': [],
        'missing_adsense': [],
        'missing_disclaimer': []
    }
    
    total_words = 0
    
    for article in articles:
        with open(article, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 1. Word Count (approx)
        word_count = count_words(content)
        total_words += word_count
        if word_count < 400:
            issues['thin_content'].append((article, word_count))
            
        # 2. Author Bio
        if 'author-bio' not in content:
            issues['missing_author'].append(article)
            
        # 3. FAQ Section
        if 'faq-section' not in content:
            issues['missing_faq'].append(article)
            
        # 4. Schema Markup
        if 'application/ld+json' not in content:
            issues['missing_schema'].append(article)
            
        # 5. Evidence/Scientific blocks (Good for E-E-A-T)
        if 'evidence-block' not in content and 'neuro-depth' not in content:
            issues['missing_evidence'].append(article)
            
        # 6. AdSense Elements
        if 'adsbygoogle.js' not in content:
            issues['missing_adsense'].append(article)
            
        # 7. Medical Disclaimer
        if 'Medical Disclaimer' not in content:
            issues['missing_disclaimer'].append(article)

    avg_words = total_words / total_articles if total_articles > 0 else 0
    
    report = {
        'total_articles': total_articles,
        'average_word_count': round(avg_words),
        'issues': issues
    }
    
    with open('adsense_audit_results.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=4)
        
    print(f"Audit complete." )
    print(f"Total Articles Processed: {total_articles}")
    print(f"Average Words per Article: {round(avg_words)}")
    print("--------------------------------------------------")
    print(f"Thin Content (<400 words): {len(issues['thin_content'])} articles")
    print(f"Missing Author Bio (E-E-A-T): {len(issues['missing_author'])} articles")
    print(f"Missing FAQs: {len(issues['missing_faq'])} articles")
    print(f"Missing Schema JSON-LD: {len(issues['missing_schema'])} articles")
    print(f"Missing Evidence Blocks: {len(issues['missing_evidence'])} articles")
    print(f"Missing AdSense Script: {len(issues['missing_adsense'])} articles")
    print(f"Missing Medical Disclaimer: {len(issues['missing_disclaimer'])} articles")

if __name__ == "__main__":
    audit_articles()
