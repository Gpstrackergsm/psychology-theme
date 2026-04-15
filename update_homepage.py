import re

with open('/Users/khalidaitelmaati/Desktop/scrapy-master/psychology-theme-main/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_cards = """
            <article data-topic="Neuroscience" class="card">
                <div class="card-img" style="background-image: url('https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&q=80&w=400&fm=webp');" loading="lazy"></div>
                <div class="card-content">
                    <span class="card-category">Neuroscience</span>
                    <h3 class="card-title">Plant-Based Diet and Dementia: Can Food Prevent Decline?</h3>
                    <p class="card-excerpt">Discover the powerful link between a plant-based diet and dementia, and the best foods for brain health.</p>
                    <a href="article278.html" class="card-link">Read More &rarr;</a>
                </div>
            </article>

            <article data-topic="Behavioral Psychology" class="card">
                <div class="card-img" style="background-image: url('https://images.unsplash.com/photo-1521791136064-7986c2920216?auto=format&fit=crop&q=80&w=400&fm=webp');" loading="lazy"></div>
                <div class="card-content">
                    <span class="card-category">Behavioral Science</span>
                    <h3 class="card-title">Small Talk Anxiety: Why Boring Conversations Hurt</h3>
                    <p class="card-excerpt">Learn exactly what triggers small talk anxiety and how to rewire your brain to handle social moments.</p>
                    <a href="article277.html" class="card-link">Read More &rarr;</a>
                </div>
            </article>

            <article data-topic="Trauma Healing" class="card">
                <div class="card-img" style="background-image: url('https://images.unsplash.com/photo-1541199249251-f713e6145474?auto=format&fit=crop&q=80&w=400&fm=webp');" loading="lazy"></div>
                <div class="card-content">
                    <span class="card-category">Trauma Healing</span>
                    <h3 class="card-title">Women and PTSD: How Hormones Affect Trauma Responses</h3>
                    <p class="card-excerpt">Why do women experience PTSD at twice the rate of men? Learn how estrogen levels predict symptom severity.</p>
                    <a href="article279.html" class="card-link">Read More &rarr;</a>
                </div>
            </article>

            <article data-topic="Anxiety Relief" class="card">
                <div class="card-img" style="background-image: url('https://images.unsplash.com/photo-1559757175-5700dde675bc?auto=format&fit=crop&q=80&w=400&fm=webp');" loading="lazy"></div>
                <div class="card-content">
                    <span class="card-category">Anxiety Relief</span>
                    <h3 class="card-title">Predictive Processing: How Your Brain Guesses the Future</h3>
                    <p class="card-excerpt">Your brain is a prediction machine. Learn the science of predictive processing and how it explains chronic anxiety.</p>
                    <a href="article280.html" class="card-link">Read More &rarr;</a>
                </div>
            </article>

            <article data-topic="Neuroscience" class="card">
                <div class="card-img" style="background-image: url('https://images.unsplash.com/photo-1516245834210-c4c017d83296?auto=format&fit=crop&q=80&w=400&fm=webp');" loading="lazy"></div>
                <div class="card-content">
                    <span class="card-category">Neuroscience</span>
                    <h3 class="card-title">Treating Hearing Loss Could Halt Dementia</h3>
                    <p class="card-excerpt">Emerging neuroscience confirms a massive link between untreated hearing loss and cognitive decline.</p>
                    <a href="article273.html" class="card-link">Read More &rarr;</a>
                </div>
            </article>

            <article data-topic="Behavioral Psychology" class="card">
                <div class="card-img" style="background-image: url('https://images.unsplash.com/photo-1525338078858-d762b5e32f2c?auto=format&fit=crop&q=80&w=400&fm=webp');" loading="lazy"></div>
                <div class="card-content">
                    <span class="card-category">Behavioral Science</span>
                    <h3 class="card-title">Why Teens Struggle to Break Up with AI Chatbots</h3>
                    <p class="card-excerpt">Psychologists warn about the dangers of frictionless AI relationships and emotional attachment.</p>
                    <a href="article274.html" class="card-link">Read More &rarr;</a>
                </div>
            </article>
            
            <article data-topic="Anxiety Relief" class="card">
                <div class="card-img" style="background-image: url('https://images.unsplash.com/photo-1518717758536-85ae29035b6d?auto=format&fit=crop&q=80&w=400&fm=webp');" loading="lazy"></div>
                <div class="card-content">
                    <span class="card-category">Anxiety Relief</span>
                    <h3 class="card-title">Dog Anxiety: Symptoms, Causes & How to Calm Your Pet</h3>
                    <p class="card-excerpt">Is your dog pacing or destroying furniture? Learn the hidden causes and treatment of dog anxiety.</p>
                    <a href="article266.html" class="card-link">Read More &rarr;</a>
                </div>
            </article>

            <article data-topic="Neuroscience" class="card">
                <div class="card-img" style="background-image: url('https://images.unsplash.com/photo-1542838685-64bc9ba020ea?auto=format&fit=crop&q=80&w=400&fm=webp');" loading="lazy"></div>
                <div class="card-content">
                    <span class="card-category">Neuroscience</span>
                    <h3 class="card-title">The Brain’s Emotion Center Redefines Hazardous Drinking</h3>
                    <p class="card-excerpt">Neuroscientists have mapped exactly how binge drinking alters the amygdala and induces panic.</p>
                    <a href="article276.html" class="card-link">Read More &rarr;</a>
                </div>
            </article>
            
            <article data-topic="Trauma Healing" class="card">
                <div class="card-img" style="background-image: url('https://images.unsplash.com/photo-1518152006812-edab29b069ac?auto=format&fit=crop&q=80&w=400&fm=webp');" loading="lazy"></div>
                <div class="card-content">
                    <span class="card-category">Trauma Healing</span>
                    <h3 class="card-title">How Enriched Environments Could Blunt Opioid Addiction</h3>
                    <p class="card-excerpt">Evidence suggests social connection and a stimulating environment physically alter the brain's reward circuits.</p>
                    <a href="article275.html" class="card-link">Read More &rarr;</a>
                </div>
            </article>
            
            """

pattern = r'(<div class="articles-grid">).*?(<!-- Article 148 -->)'
new_html = re.sub(pattern, r'\1\n' + new_cards + r'\n            \2', html, flags=re.DOTALL)

with open('/Users/khalidaitelmaati/Desktop/scrapy-master/psychology-theme-main/index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Homepage updated!")
