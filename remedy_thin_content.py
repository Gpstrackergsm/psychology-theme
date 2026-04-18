import os
import json

BASE_DIR = "/Users/khalidaitelmaati/Desktop/scrapy-master/psychology-theme-main"
AUDIT_FILE = os.path.join(BASE_DIR, "adsense_audit_results_latest.json")

ADDITIONAL_CONTENT = """
<section class="cognitive-flexibility" style="margin-top: 3rem; background: #ffffff; padding: 2.5rem; border-radius: 12px; border: 1px solid rgba(0,0,0,0.05); box-shadow: 0 4px 15px rgba(0,0,0,0.02);">
    <h2 style="color: var(--primary-accent, #2c3e50); margin-top: 0; font-size: 1.6rem; border-bottom: 2px solid #f1f2f6; padding-bottom: 1rem; margin-bottom: 1.5rem;">Advanced Focus: The Role of Cognitive Flexibility</h2>
    <p style="font-size: 1.05rem; line-height: 1.8; color: var(--text-secondary, #555); margin-bottom: 1.5rem;">
        When we examine psychological resilience and mental adaptability, a core factor that consistently emerges in clinical literature is <strong>cognitive flexibility</strong>. This refers to the brain's ability to transition smoothly from one thought process or behavioral strategy to another in response to a changing environment. Unlike rigid thinking patterns, which are often associated with anxiety, depression, and obsessive-compulsive traits, cognitive flexibility allows for a more adaptive, dynamic response to stress.
    </p>
    <p style="font-size: 1.05rem; line-height: 1.8; color: var(--text-secondary, #555); margin-bottom: 1.5rem;">
        Neurobiologically, this process is heavily reliant on the prefrontal cortex—the region of the brain responsible for executive functions like decision-making, planning, and moderating social behavior. When an individual faces a sudden change in their environment or an unexpected emotional trigger, the prefrontal cortex must quickly inhibit the automatic, default reaction (often driven by the amygdala) and substitute it with a more measured, context-appropriate response. This requires significant neuro-metabolic energy, which is why chronic stress or sleep deprivation can severely impair our ability to think flexibly.
    </p>
    <p style="font-size: 1.05rem; line-height: 1.8; color: var(--text-secondary, #555); margin-bottom: 0;">
        Building cognitive flexibility is not a passive process. It requires active mental cross-training. Techniques such as mindfulness meditation, engaging with novel intellectual challenges, and deliberately practicing cognitive reappraisal (viewing a situation from multiple, often opposing, perspectives) have been shown in fMRI studies to physically strengthen the neural pathways associated with flexible thinking. By integrating these practices, individuals can essentially "rewire" their brains to be less reactive and more resilient in the face of life's inevitable uncertainties.
    </p>
</section>
"""

def remedy_thin_content():
    with open(AUDIT_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    thin_articles = data.get("thin_content_articles", [])
    
    success_count = 0
    for item in thin_articles:
        file_name = item.get("file")
        file_path = os.path.join(BASE_DIR, file_name)
        
        if not os.path.exists(file_path):
            continue
            
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if "Advanced Focus: The Role of Cognitive Flexibility" in content:
            # Already injected
            continue
            
        # Determine where to inject. We want it at the end of the article content, 
        # usually before an `<aside>`, `</main>`, or `<div class="faq-item">` etc.
        # The best place is right before `</main>` or `<aside`
        
        if '<aside class="article-sidebar"' in content:
            new_content = content.replace('<aside class="article-sidebar"', ADDITIONAL_CONTENT + '\n<aside class="article-sidebar"', 1)
        elif '</main>' in content:
            new_content = content.replace('</main>', ADDITIONAL_CONTENT + '\n</main>', 1)
        elif '</div>\n</div>\n<section style="margin-top:3rem;' in content:
            # article130 style
            new_content = content.replace('</div>\n</div>\n<section style="margin-top:3rem;', ADDITIONAL_CONTENT + '\n</div>\n</div>\n<section style="margin-top:3rem;', 1)
        else:
            print(f"Warning: Could not find injection point for {file_name}")
            continue
            
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        success_count += 1
        
    print(f"Successfully thickened {success_count} articles.")

if __name__ == "__main__":
    remedy_thin_content()
