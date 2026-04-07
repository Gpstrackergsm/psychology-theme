import os
import re

BASE_DIR = "/Users/khalidaitelmaati/Desktop/scrapy-master/psychology-theme-main"

faq_data = {
    36: {
        "questions": [
            {
                "q": "What is the main difference between a grandiose and a covert narcissist?",
                "a": "Grandiose narcissists are outwardly arrogant and seek the spotlight, while covert narcissists hide their need for admiration behind a mask of victimhood, introversion, and passive-aggression."
            },
            {
                "q": "How do you respond to a covert narcissist's silent treatment?",
                "a": "The best response is the 'Grey Rock' method: remain emotionally neutral, give short and non-committal answers, and do not show that their silence affects you."
            },
            {
                "q": "Can a covert narcissist ever change?",
                "a": "Change is extremely rare because it requires deep self-reflection and accountability—traits that narcissists are biologically and neurologically wired to avoid."
            }
        ]
    },
    37: {
        "questions": [
            {
                "q": "Why does my brain start overthinking specifically at night?",
                "a": "At night, the lack of external distractions activates the brain's 'Default Mode Network', which scans for unresolved emotional threats and social anxieties as a misfired survival mechanism."
            },
            {
                "q": "What is the 4-7-8 breathing technique for sleep anxiety?",
                "a": "Inhale for 4 seconds, hold for 7, and exhale forcefully for 8. This specific rhythm manually triggers the parasympathetic nervous system to lower your heart rate and break the anxiety loop."
            },
            {
                "q": "Does writing down worries before bed actually help?",
                "a": "Yes. A 'brain dump' externalizes worries, tricking the brain into believing the 'task' of worrying has been handled, which allows the mind to enter a restful state."
            }
        ]
    },
    38: {
        "questions": [
            {
                "q": "How long does a dopamine detox take to work?",
                "a": "A 24-hour 'hard reset' can begin the process of receptor re-sensitization, but a 30-day moderate 'unplugging' is recommended for permanent behavioral change."
            },
            {
                "q": "Can I listen to music during a dopamine detox?",
                "a": "In a strict detox, fast-paced or highly stimulating music is avoided. Calm, instrumental music is generally acceptable as it doesn't trigger massive dopamine spikes."
            },
            {
                "q": "Is dopamine the 'pleasure' chemical?",
                "a": "No, neuroscience shows dopamine is the 'motivation' and 'seeking' chemical. It drives you to pursue a reward rather than providing the pleasure of the reward itself."
            }
        ]
    },
    44: {
        "questions": [
            {
                "q": "Why is it so hard to break a trauma bond?",
                "a": "Trauma bonds mirror drug addiction neurobiology. The cycle of abuse (stress) and intermittent affection (dopamine) creates a physical chemical dependency on the abuser."
            },
            {
                "q": "What are the first steps to healing from a trauma bond?",
                "a": "The priority is 'No Contact' to stop the chemical spikes, followed by trauma-informed therapy like EMDR or Somatic Experiencing to regulate the nervous system."
            }
        ]
    }
}

def build_schema(questions):
    schema_items = []
    for item in questions:
        schema_items.append(f"""{{
      "@type": "Question",
      "name": "{item['q']}",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "{item['a']}"
      }}
    }}""")
    
    joined_items = ",".join(schema_items)
    return f"""
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [{joined_items}]
    }}
    </script>
    """

def build_visible_faq(questions):
    faq_html = '<section class="faq-section" style="margin-top: 4rem; border-top: 1px solid rgba(0,0,0,0.1); padding-top: 2rem;">'
    faq_html += '<h2 style="margin-bottom: 2rem;">Frequently Asked Questions</h2>'
    for item in questions:
        faq_html += f"""
        <div class="faq-item" style="margin-bottom: 2rem;">
            <h3 style="font-size: 1.2rem; color: var(--primary-color); margin-bottom: 0.5rem;">{item['q']}</h3>
            <p>{item['a']}</p>
        </div>"""
    faq_html += '</section>'
    return faq_html

def inject_faq(art_id, data):
    filepath = os.path.join(BASE_DIR, f"article{art_id}.html")
    if not os.path.exists(filepath): return
    
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Inject Schema into <head>
    if 'application/ld+json' in html and 'FAQPage' in html:
        print(f"Skipping article{art_id} - FAQ Schema already exists.")
    else:
        schema_code = build_schema(data['questions'])
        html = html.replace('</head>', f'{schema_code}\n</head>')

    # 2. Inject Visible FAQ before the Medical Disclaimer
    if 'faq-section' not in html:
        visible_faq = build_visible_faq(data['questions'])
        disclaimer_marker = '<!-- Medical Disclaimer -->'
        if disclaimer_marker in html:
            html = html.replace(disclaimer_marker, f'{visible_faq}\n{disclaimer_marker}')
        else:
             # Fallback to before footer
             html = html.replace('<footer', f'{visible_faq}\n<footer')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ Injected FAQ SEO into article{art_id}.html")

def main():
    for art_id, data in faq_data.items():
        inject_faq(art_id, data)

if __name__ == "__main__":
    main()
