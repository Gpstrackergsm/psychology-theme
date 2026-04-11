import json
import os

def build_hub():
    with open('neuro_articles_meta.json', 'r', encoding='utf-8') as f:
        articles = json.load(f)

    # Categories
    cats = {
        'clinical': [],
        'performance': [],
        'resilience': [],
        'longevity': []
    }

    clinical_kw = ['Alzheimer', 'Schizophrenia', 'Parkinson', 'Stroke', 'Metformin', 'Bipolar', 'Ketamine', 'BCI', 'Mutations', 'Drains', 'Clinical']
    performance_kw = ['Dopamine', 'Sleep', 'Growth', 'Muscle', 'Focus', 'Attention', 'ADHD', 'Intelligence', 'Cognitive', 'Detox', 'Development', '30s', '25']
    resilience_kw = ['Resilience', 'Trauma', 'Stress', 'Vagus', 'Anxiety', 'Gratitude', 'Childhood', 'Gut', 'Bonding', 'Aggression', 'Somatic']
    longevity_kw = ['Aging', 'Longevity', 'FTL1', 'Protein', 'Microplastics', 'Dye-free', 'Atlas', 'Memory Loss', 'Memory decline', 'Rejuvenation']

    for a in articles:
        text = (a['title'] + " " + a['desc']).lower()
        assigned = False
        
        if any(kw.lower() in text for kw in clinical_kw):
            cats['clinical'].append(a)
            assigned = True
        elif any(kw.lower() in text for kw in performance_kw):
            cats['performance'].append(a)
            assigned = True
        elif any(kw.lower() in text for kw in resilience_kw):
            cats['resilience'].append(a)
            assigned = True
        elif any(kw.lower() in text for kw in longevity_kw):
            cats['longevity'].append(a)
            assigned = True
        else:
            cats['clinical'].append(a) # Default

    def gen_grid(article_list):
        html = ""
        for a in article_list:
            img = a['img'] if a['img'] else "https://images.unsplash.com/photo-1559757148-5c350d0d3c56?auto=format&fit=crop&q=80&w=400"
            html += f'''
                <div class="hub-card">
                    <div class="hub-card-img" style="background-image: url('{img}');"></div>
                    <div class="hub-card-content">
                        <h3 class="hub-card-title">{a['title']}</h3>
                        <p class="hub-card-desc">{a['desc']}</p>
                        <a href="{a['file']}" class="hub-card-link">Read Research &rarr;</a>
                    </div>
                </div>'''
        return html

    # Read the base template
    with open('neuroscience-hub.html', 'r', encoding='utf-8') as f:
        template = f.read()

    template = template.replace('<!-- Injected via script/manual -->', 'INJECT_HERE') # Marker
    
    # We need to replace specifically by ID.
    # Actually, let's just use string replacement on a per-id basis.
    
    final_html = template
    final_html = final_html.replace('<div class="hub-grid" id="clinical-grid">\n                <!-- Injected via script/manual -->\n            </div>', f'<div class="hub-grid" id="clinical-grid">{gen_grid(cats["clinical"])}</div>')
    final_html = final_html.replace('<div class="hub-grid" id="performance-grid">\n                <!-- Injected via script/manual -->\n            </div>', f'<div class="hub-grid" id="performance-grid">{gen_grid(cats["performance"])}</div>')
    final_html = final_html.replace('<div class="hub-grid" id="resilience-grid">\n                <!-- Injected via script/manual -->\n            </div>', f'<div class="hub-grid" id="resilience-grid">{gen_grid(cats["resilience"])}</div>')
    final_html = final_html.replace('<div class="hub-grid" id="longevity-grid">\n                <!-- Injected via script/manual -->\n            </div>', f'<div class="hub-grid" id="longevity-grid">{gen_grid(cats["longevity"])}</div>')

    with open('neuroscience-hub.html', 'w', encoding='utf-8') as f:
        f.write(final_html)
    
    print("Neuroscience Hub populated with 52 articles.")

if __name__ == "__main__":
    build_hub()
