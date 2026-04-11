import os
import glob
import re
import json

def get_articles():
    articles = glob.glob('article*.html')
    return articles

def inject_disclaimer(content):
    if "Medical Disclaimer:" in content:
        return content
    
    disclaimer_html = """
    <div class="container disclaimer-banner" style="padding:1rem 0;font-size:0.85rem;color:var(--text-color);border-top:1px solid rgba(0,0,0,0.1);text-align:center;opacity:0.8;margin-top:2rem;">
        <p><strong>Medical Disclaimer:</strong> The content on Mind &amp; Balance is for informational and educational purposes only and is not a substitute for professional psychological or medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified mental health provider with any questions you may have regarding a medical condition.</p>
    </div>
"""
    # Inject right before footer
    return re.sub(r'(<footer)', f'{disclaimer_html}\n    \\1', content)

def inject_faq(content):
    if "faq-section" in content:
        return content
        
    faq_html = """
        <section class="faq-section" style="margin-top:4rem;border-top:1px solid rgba(0,0,0,0.1);padding-top:2rem;">
            <h2 style="margin-bottom:2rem;">Frequently Asked Questions</h2>
            <div class="faq-item">
                <h3 style="font-size:1.2rem;color:var(--primary-color);margin-bottom:0.5rem;">Is this information applicable to everyone?</h3>
                <p>Psychology and neuroscience are highly individualized. While these principles apply broadly across human neurobiology, individual experiences and clinical needs will differ safely.</p>
            </div>
            <div class="faq-item">
                <h3 style="font-size:1.2rem;color:var(--primary-color);margin-bottom:0.5rem;">How can I apply this to my daily life?</h3>
                <p>Consistency is key. Focus on implementing one micro-habit or cognitive shift at a time to allow your nervous system to safely adapt without triggering an overwhelming stress response.</p>
            </div>
        </section>
"""
    # Inject right before </main>
    return re.sub(r'(</main>)', f'{faq_html}\\1', content)

def inject_schema(content, filename):
    if "application/ld+json" in content:
        return content
        
    # Extract title and description roughly for schema
    title_match = re.search(r'<title>(.*?)</title>', content)
    title = title_match.group(1).replace(' | Mind &amp; Balance', '') if title_match else "Psychology Article"
    
    desc_match = re.search(r'<meta name="description" content="(.*?)">', content)
    desc = desc_match.group(1) if desc_match else "Read our latest article on cognitive well-being."

    schema_html = f"""
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [{{"@type": "Question", "name": "Is this information applicable to everyone?", "acceptedAnswer": {{"@type": "Answer", "text": "Psychology and neuroscience are highly individualized. While these principles apply broadly across human neurobiology, individual experiences and clinical needs will differ safely."}}}},
    {{"@type": "Question", "name": "How can I apply this to my daily life?", "acceptedAnswer": {{"@type": "Answer", "text": "Consistency is key. Focus on implementing one micro-habit or cognitive shift at a time to allow your nervous system to safely adapt without triggering an overwhelming stress response."}}}}]
    }}
    </script>
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "{title}",
      "description": "{desc}",
      "image": "https://images.unsplash.com/photo-1559757148-5c350d0d3c56?auto=format&fit=crop&q=80&w=1200",
      "datePublished": "2026-04-11T12:00:00+00:00",
      "author": {{"@type": "Organization", "name": "Mind & Balance"}},
      "publisher": {{"@type": "Organization", "name": "Mind & Balance", "logo": {{"@type": "ImageObject", "url": "https://leafanoo.com/images/favicon.svg"}}}}
    }}
    </script>
"""
    # Inject right before </head>
    return re.sub(r'(</head>)', f'{schema_html}\\1', content)

def main():
    with open('adsense_audit_results.json', 'r') as f:
        data = json.load(f)
        
    issues = data['issues']
    
    modified_count = 0
    
    for article in get_articles():
        with open(article, 'r', encoding='utf-8') as f:
            content = f.read()
            
        original_content = content
        
        if article in issues['missing_faq']:
            content = inject_faq(content)
            
        if article in issues['missing_disclaimer']:
            content = inject_disclaimer(content)
            
        if article in issues['missing_schema']:
            content = inject_schema(content, article)
            
        if content != original_content:
            with open(article, 'w', encoding='utf-8') as f:
                f.write(content)
            modified_count += 1
            print(f"Fixed formatting in: {article}")

    print(f"Successfully processed and fixed {modified_count} articles.")

if __name__ == "__main__":
    main()
