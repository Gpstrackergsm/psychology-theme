import os
import re
import datetime

BASE_DIR = "/Users/khalidaitelmaati/Desktop/scrapy-master/psychology-theme-main"
INDEX_PATH = os.path.join(BASE_DIR, "index.html")
SITEMAP_PATH = os.path.join(BASE_DIR, "sitemap.xml")

batch_6_articles = [
    {
        "id": 116,
        "title": "The Genetic Anxiety Link in 100 Golden Retrievers: A Psychological Perspective",
        "category": "Biological Psychology",
        "image": "https://images.unsplash.com/photo-1552053831-71594a27632d?auto=format&fit=crop&q=80&w=600",
        "excerpt": "New genetic research in Golden Retrievers has uncovered biological clues that explain why some are more anxious than others—and how these same genes affect human mental health.",
        "content": "Neuroscientists have long suspected that anxiety has a deep biological root. A groundbreaking study of 100 Golden Retrievers has finally identified specific genetic markers linked to anxiety, energy levels, and social aggression. Remarkably, many of these same 'anxiety genes' are virtually identical in the human genome. This discovery suggests that our feelings of worry or dread may be less about our daily stress and more about our inherited neurobiology. By understanding how these genes are expressed, therapists can better tailor treatments for people who are genetically predisposed to 'high-alert' nervous systems.",
        "qa": [
            {"q": "Can dogs really have the same anxiety genes as humans?", "a": "Yes, research shows that several genes linked to canine anxiety are also tied to human traits like depression and social intelligence."},
            {"q": "Does this mean anxiety is purely genetic?", "a": "No, but it shows that some individuals have a higher biological 'baseline' for anxiety, making environmental stressors feel more intense."}
        ]
    },
    {
        "id": 117,
        "title": "Mental Health Break: The Science Behind How a Brain Protein Drives Addiction Relapse",
        "category": "Neuroscience",
        "image": "https://images.unsplash.com/photo-1559757175-5700dde675bc?auto=format&fit=crop&q=80&w=600",
        "excerpt": "Cocaine addiction changes the brain's physical wiring. Researchers have discovered a specific protein that 'locks' these changes in place, driving the risk of relapse.",
        "content": "Addiction is often misunderstood as a failure of willpower, but recent neuroscience shows it is a deep structural change in the brain. Researchers at Michigan State University have identified a protein that rewires the communication pathways between the reward system and the hippocampus—the brain's memory center. This protein essentially 'burns' the memory of the drug into the brain's architecture, making relapse feel like a survival instinct rather than a choice. This breakthrough opens the door for new pharmacological treatments that could 'unlock' these pathways and help the brain reset to its pre-addiction state.",
        "qa": [
            {"q": "Why is relapse so common in addiction?", "a": "Repeated drug use creates physical 'shortcuts' in the brain's reward system that are hard to override through willpower alone."},
            {"q": "Can the brain be 'rewired' after addiction?", "a": "Yes, neuroplasticity allows the brain to form new pathways, though biological interventions may be needed for severe cases."}
        ]
    },
    {
        "id": 118,
        "title": "Why Beyond Amyloid Plaques Matters for Mental Health: The AI Brain Atlas",
        "category": "Clinical Psychology",
        "image": "https://images.unsplash.com/photo-1507413245164-6160d8298b31?auto=format&fit=crop&q=80&w=600",
        "excerpt": "AI has just mapped the Alzheimer's brain in higher detail than ever before, revealing hidden chemical changes that go far beyond standard plaque detection.",
        "content": "For decades, Alzheimer's research focused almost exclusively on amyloid plaques. However, a new AI-powered molecular atlas from Rice University has revealed that the disease involves a complex web of chemical changes that spread unevenly across the brain. This 'molecular dye-free' mapping shows that key memory regions experience major chemical shifts long before plaques are visible. This suggests that dementia is a whole-brain event, requiring treatments that address systemic chemical balance rather than just 'clearing out' protein buildup. This AI breakthrough could significantly accelerate the development of personalized mental health care for the elderly.",
        "qa": [
            {"q": "Is Alzheimer's just about memory loss?", "a": "No, it involves widespread chemical changes that affect mood, personality, and biological regulation."},
            {"q": "How does AI help in brain research?", "a": "AI can process massive amounts of laser-imaging data to spot patterns and chemical anomalies that are invisible to the human eye."}
        ]
    },
    {
        "id": 119,
        "title": "The More You Fear Aging, the Faster Your Body May Age: A Psychological Perspective",
        "category": "Positive Psychology",
        "image": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&q=80&w=600",
        "excerpt": "Worrying about getting older may actually speed up the biological clock at a cellular level, according to new research on aging anxiety.",
        "content": "Does our mindset affect our lifespan? A new study of over 700 women by NYU suggests that the answer is yes. Researchers found that women who felt high levels of 'aging anxiety'—specifically fear of future health problems—showed signs of faster biological aging in their blood samples. This 'psychosomatic acceleration' occurs because chronic worry triggers low-level inflammation and cellular stress, which literally wears down the body's repair mechanisms. This highlights the importance of positive psychology and mindfulness as critical tools for long-term physical health, showing that 'feeling young' is more than just a cliché—it is a biological protective factor.",
        "qa": [
            {"q": "What is aging anxiety?", "a": "It is a chronic fear of the physical, social, or mental decline associated with growing older."},
            {"q": "Can changing my mindset stop physical aging?", "a": "While you cannot stop time, reducing stress and anxiety is proven to slow down 'biological' aging at the cellular level."}
        ]
    },
    {
        "id": 120,
        "title": "A Therapist's View on: Does Alzheimer’s Begin with a Silent Drop in Brain Blood Flow?",
        "category": "Neuroscience",
        "image": "https://images.unsplash.com/photo-1559757175-5700dde675bc?auto=format&fit=crop&q=80&w=600",
        "excerpt": "New clinical research suggests that the earliest signs of Alzheimer's isn't memory loss, but a 'silent' reduction in how blood flows through the brain.",
        "content": "The search for early Alzheimer's markers has shifted from the mind to the blood vessels. Subtle drops in brain blood flow and oxygen efficiency are now being linked to the earliest stages of cognitive decline, often occurring years before a patient notices symptoms. These 'silent drops' appear to trigger a cascade of inflammation that leads to plaque buildup. This discovery suggests that maintaining vascular health—through cardiovascular exercise and blood pressure management—might be the most effective way to protect the brain later in life. Non-invasive blood-flow scans may soon become a standard 'preventative checkup' for mental longevity.",
        "qa": [
            {"q": "Can I have Alzheimer's symptoms without losing my memory?", "a": "Yes, early stages often manifest as confusion, mood swings, or 'brain fog' caused by reduced blood flow before memory cells die."},
            {"q": "How can I improve brain blood flow naturally?", "a": "Aerobic exercise, a Mediterranean-style diet, and staying hydrated are all linked to healthier cerebral circulation."}
        ]
    },
    {
        "id": 121,
        "title": "The Science of New Brain Stimulation Approach: Treating Depression in Just 5 Days",
        "category": "Mental Health hacks",
        "image": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&q=80&w=600",
        "excerpt": "Standard depression treatments can take weeks. A new high-intensity TMS protocol is achieving meaningful results in as little as 5 days.",
        "content": "Traditional Transcranial Magnetic Stimulation (TMS) requires six weeks of daily sessions—a huge commitment for patients in crisis. However, a new study from UCLA has validated a high-intensity, five-day version of the therapy. By delivering multiple stimulation sessions per day, researchers achieved symptom relief comparable to the standard six-week protocol. This 'rapid-reset' approach could revolutionize emergency mental health care, providing an alternative to long-term medication for patients who need immediate stabilization. For many, this five-day protocol didn't just ease their depression; it 'woke up' regions of the brain that had been dormant for years.",
        "qa": [
            {"q": "Is rapid TMS safe?", "a": "Yes, clinical trials show it is generally safe, though side effects like mild headaches can occur during the high-intensity phase."},
            {"q": "Who is a good candidate for 5-day TMS?", "a": "It is often used for treatment-resistant depression where standard SSRIs have failed to provide relief."}
        ]
    },
    {
        "id": 122,
        "title": "The Doctors Implant Dopamine Stem Cells: A Psychological Perspective on Parkinson's",
        "category": "Clinical Psychology",
        "image": "https://images.unsplash.com/photo-1507413245164-6160d8298b31?auto=format&fit=crop&q=80&w=600",
        "excerpt": "A groundbreaking clinical trial is testing whether engineered stem cells can help the brain regenerate its own dopamine supply to treat Parkinson's.",
        "content": "Parkinson's Disease is primarily a failure of the brain's dopamine-producing cells, leading to physical tremors and psychological depression. A new clinical trial is making waves by implanting 'specially engineered stem cells' directly into the brains of patients. The goal is to allow the brain to 're-grow' its own chemical factory. If successful, this would move Parkinson's care from 'managing symptoms' with drugs to 'actually restoring function.' Psychologically, this represents a massive shift in hope for patients, as dopamine is not just for movement—it is the chemical of motivation, reward, and the will to thrive.",
        "qa": [
            {"q": "How do stem cells help Parkinson's?", "a": "They are designed to replace the neurons that have died, potentially restoring natural dopamine levels."},
            {"q": "When will this treatment be available?", "a": "It is currently in human clinical trials to ensure safety and long-term efficacy before wider release."}
        ]
    },
    {
        "id": 123,
        "title": "A Therapist's View on: Why Sugary Drinks Are Linked to Rising Anxiety in Teens",
        "category": "Behavioral Psychology",
        "image": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&r=80&w=600",
        "excerpt": "Is soda making our teens anxious? A new review explains the physiological link between liquid sugar and adolescent anxiety spikes.",
        "content": "Teenagers are reporting record levels of anxiety, and researchers are looking beyond social media for answers. A major review of dietary studies has found a consistent link between the consumption of sugary drinks (sodas, energy drinks, and juices) and increased anxiety symptoms in adolescents. The reason is biological: sudden spikes and drops in blood sugar trigger 'cortisol releases' that the brain interprets as environmental danger. In an adolescent brain that is already highly sensitive to stress, these daily 'sugar crashes' can manifest as panic attacks, social avoidance, and chronic dread. Cutting liquid sugar might be one of the simplest mental health interventions for modern teens.",
        "qa": [
            {"q": "Why does sugar cause anxiety?", "a": "Sugar spikes lead to insulin surges followed by crashes, which trigger the body's 'fight-or-flight' stress response (adrenaline and cortisol)."},
            {"q": "Are diet sodas better for anxiety?", "a": "While they avoid the sugar crash, some artificial sweeteners are also being studied for their potential impact on gut-brain communication and anxiety."}
        ]
    },
    {
        "id": 124,
        "title": "The Science of Brain Development: Why Your Brain Doesn't Stop Developing at 25",
        "category": "Neuroscience",
        "image": "https://images.unsplash.com/photo-1559757175-5700dde675bc?auto=format&fit=crop&q=80&w=600",
        "excerpt": "The viral claim that the brain is 'fully developed' at 25 is more myth than science. New research shows the brain continues to evolve well into your 30s.",
        "content": "We've all heard the meme: 'Your frontal lobe isn't developed until 25.' While the early 20s are a major milestone, new neuroimaging research shows that human brain development is far more fluid. Scientists have discovered that white matter—the insulation that allows neurons to communicate faster—continues to thicken and specialize through our late 20s and well into our mid-30s. This means our capacity for emotional regulation, complex decision-making, and wisdom continues to grow longer than previously thought. The brain is not a static object that 'finishes' at 25; it is a dynamic organ that reshapes itself based on our experiences and environment for most of our adult life.",
        "qa": [
            {"q": "Where did the 'age 25' myth come from?", "a": "Early studies on brain development stopped looking at participants after age 21 or 25, leading to the assumption that development ended there."},
            {"q": "How can I keep my brain developing in my 30s?", "a": "Neuroplasticity is fueled by 'novelty'—learning new skills, traveling, and engaging in complex problem-solving all keep the brain evolving."}
        ]
    },
    {
        "id": 125,
        "title": "What Psychedelics Reveal: How Reality Shuts Down and Unlocks Internal Memory",
        "category": "Personality Psychology",
        "image": "https://images.unsplash.com/photo-1506126613408-eca07ce68773?auto=format&fit=crop&q=80&w=600",
        "excerpt": "Psychedelics don't just add hallucinations; they actively shut down the brain's 'reality filters,' allowing the mind to replace the outside world with vivid internal memories.",
        "content": "Why do people on psychedelics see things that aren't there? Conventional wisdom says it's just 'random firing,' but new brain scans show something more structured. Psychedelics actually quiet down the brain's sensory input filters—the systems that normally prioritize the outside world. When this 'reality feed' is cut off, the brain automatically fills the void with vivid fragments of internal memory. It is almost like dreaming while awake. This shift allows patients in therapy to 'see' and re-process old memories as if they were current events, which is why these substances are becoming such powerful tools for treating deep-seated PTSD and clinical depression.",
        "qa": [
            {"q": "Are psychedelic visions real?", "a": "They are biologically real in terms of neural activity, but they are internally generated by the brain's memory systems rather than the eyes."},
            {"q": "Why is this used for therapy?", "a": "By accessing 'locked' memories without the usual emotional defenses, patients can process trauma in a safe, clinical environment."}
        ]
    },
    {
        "id": 126,
        "title": "The Couples Who Savor Happy Moments Together: A Psychological Shield",
        "category": "Relationships",
        "image": "https://images.unsplash.com/photo-1516589174184-c685ca33d2b0?auto=format&fit=crop&q=80&w=600",
        "excerpt": "Building a lasting relationship might be as simple as 'soaking in' the good times. Learn the science of shared savoring.",
        "content": "We often think that solving problems is the key to a happy marriage, but 'savoring' may be even more important. Researchers at the University of Illinois found that couples who intentionally slow down and soaking in their happy moments together—whether it's an old memory or a morning coffee—create a 'psychological shield' that protects them from future conflicts. This act of 'shared savoring' builds a reservoir of positive emotion that the couple can draw on when times get tough. It's a proactive way to build trust and intimacy, showing that focusing on what is *right* with your relationship is just as important as fixing what is *wrong*.",
        "qa": [
            {"q": "What is 'savoring' in a relationship?", "a": "It is the act of consciously noticing and appreciating a positive experience with your partner, effectively prolonging the pleasure of the moment."},
            {"q": "Can savoring fix a toxic relationship?", "a": "No, it is a tool for building health in safe relationships; it cannot override fundamental issues like abuse or chronic disrespect."}
        ]
    },
    {
        "id": 127,
        "title": "A Therapist's View on: Why Exercise Is One of the Most Powerful Treatments for Anxiety",
        "category": "Behavioral Psychology",
        "image": "https://images.unsplash.com/photo-1506126613408-eca07ce68773?auto=format&fit=crop&q=80&w=600",
        "excerpt": "A sweeping global review suggests that aerobic exercise matches standard medication for many people suffering from moderate depression and anxiety.",
        "content": "Moving the body is moving the mind. A massive review of international research across 65,000 adults has confirmed that aerobic exercise—running, swimming, and even dancing—is one of the most powerful 'biological' treatments for anxiety. Exercise works by metabolizing excess cortisol and increasing the production of BDNF, a protein that acts like 'brain fertilizer' for the hippocampus. For many patients with moderate anxiety, a consistent exercise routine provided relief that was comparable to standard SSRIs, but without the physiological side effects. Physical activity is essentially 'manual mood regulation' for the brain.",
        "qa": [
            {"q": "How much exercise do I need for mental health benefits?", "a": "Research suggests that just 150 minutes of moderate aerobic activity per week can significantly lower anxiety and depression scores."},
            {"q": "Why does exercise help anxiety specifically?", "a": "It gives the 'fight-or-flight' energy a physical outlet, signaling to the brain that the 'threat' has been dealt with."}
        ]
    },
    {
        "id": 128,
        "title": "The Science Behind How Brain Stimulation Can Make People More Generous",
        "category": "Social Psychology",
        "image": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&q=80&w=600",
        "excerpt": "Generosity isn't just a choice; it's a neurological state. Scientists have successfully increased kindness using gentle brain stimulation.",
        "content": "Is kindness a moral lesson or a neural circuit? New research suggests it's both. By and syncing their activity with gentle, non-invasive brain stimulation, researchers were able to make participants significantly more generous and willing to share resources. The study found that when the 'empathy regions' of the brain are in sync with the 'decision-making regions,' the natural human instinct to help others becomes the dominant path. This research isn't just about 'making people nicer'—it helps us understand how social behaviors like cooperation and altruism evolved as fundamental biological strategies for human survival.",
        "qa": [
            {"q": "Does this mean my generosity is 'forced'?", "a": "No, the stimulation simply 'lowers the noise' of self-interest, allowing your natural capacity for empathy to take the lead."},
            {"q": "Can this be used to treat behavioral disorders?", "a": "Potentially. In the future, this could help individuals with disorders that impair social cooperation or empathy."}
        ]
    },
    {
        "id": 129,
        "title": "Why Swapping Just One Hour of TV for Activity Could Slash Depression Risk",
        "category": "Mental Health hacks",
        "image": "https://images.unsplash.com/photo-1484480974693-6ca0a78fb36b?auto=format&fit=crop&q=80&w=600",
        "excerpt": "A simple daily swap of 60 minutes of TV for any active hobby is linked to a massive drop in the risk of developing clinical depression.",
        "content": "Our sedentary 'screen habits' are taking a toll on our brains. A large-scale longitudinal study found that adults who replaced just one hour of television per day with a physically active hobby—gardening, walking, or even cooking while standing—slashed their risk of developing major depression by significantly. The reason isn't just the exercise; it's the 'cognitive engagement.' Passive screen time tends to fuel rumination (circular negative thinking), while active hobbies force the brain to focus on the present moment. This 'intentional activity' prevents the brain from falling into the grooves of depressive thought patterns.",
        "qa": [
            {"q": "Is all TV bad for depression?", "a": "No, but 'passive' or 'numbing' consumption for long stretches is what leads to the highest risk. Active, engaged viewing is less harmful."},
            {"q": "What is the best 'swap' activity?", "a": "Anything that requires focus and light physical movement is best, as it breaks the sedentary loop."}
        ]
    },
    {
        "id": 130,
        "title": "The Neurology of Trust: How Your Brain Decides Who to Believe in an Instant",
        "category": "Social Psychology",
        "image": "https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&q=80&w=600",
        "excerpt": "Trust is formed in milliseconds. Discover the brain's rapid 'friend-or-foe' calculation and how it shapes your social reality.",
        "content": "Before someone finishes their first sentence, your brain has already decided whether to trust them. This 'rapid trust calculation' happens in the amygdala and the prefrontal cortex. Our ancestors needed this 'millisecond judgment' to survive social interactions in the wild. Today, this same system can lead to unconscious bias—or it can help us form instant, deep connections. Trust is a biological handshake between your brain's emotional center and its logic center. By understanding how 'micro-expressions' and tone of voice trigger these trust responses, we can navigate social situations with more awareness and build more authentic human bonds.",
        "qa": [
            {"q": "Can I overcome a bad 'first impression'?", "a": "Yes, but it requires consistent 'counter-evidence' to override the amygdala's initial millisecond judgment."},
            {"q": "Why do some people seem naturally 'trustworthy'?", "a": "It often comes down to 'facial symmetry' and 'open body language,' which our brains evolved to read as signs of safety and honesty."}
        ]
    }
]

def generate_article(article):
    file_name = f"article{article['id']}.html"
    file_path = os.path.join(BASE_DIR, file_name)
    
    faq_schema = ""
    for qa in article['qa']:
        faq_schema += f"""{{
                "@type": "Question",
                "name": "{qa['q']}",
                "acceptedAnswer": {{
                    "@type": "Answer",
                    "text": "{qa['a']}"
                }}
            }},"""
    faq_schema = faq_schema.rstrip(',')

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{article['title']} | Mind & Balance</title>
    <meta name="description" content="{article['excerpt']}">
    <link rel="stylesheet" href="css/style.css">
    <link rel="icon" type="image/svg+xml" href="images/favicon.svg">
    <link rel="canonical" href="https://leafanoo.com/{file_name}">
    
    <!-- Schema.org JSON-LD -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "{article['title']}",
      "description": "{article['excerpt']}",
      "image": "{article['image']}",
      "author": {{
        "@type": "Person",
        "name": "Dr. Aris"
      }},
      "publisher": {{
        "@type": "Organization",
        "name": "Mind & Balance",
        "logo": {{
          "@type": "ImageObject",
          "url": "https://leafanoo.com/images/favicon.svg"
        }}
      }},
      "datePublished": "{datetime.date.today().isoformat()}"
    }}
    </script>
    
    <!-- FAQ Schema -->
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {faq_schema}
        ]
    }}
    </script>
</head>
<body>
    <header>
        <nav class="nav-container">
            <div class="logo">Mind & Balance</div>
            <ul class="nav-links">
                <li><a href="index.html">Home</a></li>
                <li><a href="index.html#articles">Articles</a></li>
                <li><a href="about.html">About</a></li>
                <li><a href="contact.html">Contact</a></li>
            </ul>
        </nav>
    </header>

    <article class="article-header" style="background-image: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('{article['image']}'); background-size: cover; background-position: center; color: white; padding: 12rem 2rem 6rem;">
        <div class="container">
            <span class="card-category" style="color: var(--secondary-accent); font-weight: bold;">{article['category']}</span>
            <h1 style="font-size: 3rem; margin: 1rem 0;">{article['title']}</h1>
            <div class="article-meta" style="color: #ddd;">
                <span>By Dr. Aris</span> • <span>{datetime.date.today().strftime('%B %d, %Y')}</span>
            </div>
        </div>
    </article>

    <main class="container article-layout">
        <div class="article-body">
            <p class="lead" style="font-size: 1.4rem; color: var(--text-secondary); margin-bottom: 2rem;">{article['excerpt']}</p>
            {article['content']}
            
            <div class="faq-section" style="margin-top: 4rem; background: var(--bg-secondary); padding: 2rem; border-radius: 12px;">
                <h2 style="margin-top: 0;">Frequently Asked Questions</h2>
                {''.join([f"<div class='faq-item' style='margin-bottom: 1.5rem;'><strong>{qa['q']}</strong><p>{qa['a']}</p></div>" for qa in article['qa']])}
            </div>
        </div>
        
        <aside class="article-sidebar">
            <div class="sticky-sidebar">
                <div class="ad-container ad-sidebar">
                    <!-- AdSense Placeholder -->
                </div>
                <div class="card" style="padding: 1.5rem; margin-top: 2rem;">
                    <h3>Related Topics</h3>
                    <ul style="list-style: none; padding: 0;">
                        <li style="margin-bottom: 1rem;"><a href="article115.html" style="color: var(--primary-accent);">Ketamine & Depression</a></li>
                        <li style="margin-bottom: 1rem;"><a href="article110.html" style="color: var(--primary-accent);">Ozempic & Emotional Health</a></li>
                        <li style="margin-bottom: 1rem;"><a href="article101.html" style="color: var(--primary-accent);">The Brain's Appetite Switch</a></li>
                    </ul>
                </div>
            </div>
        </aside>
    </main>

    <footer style="background: var(--text-primary); color: white; padding: 4rem 0; margin-top: 4rem; text-align: center;">
        <div class="container">
            <p>&copy; 2026 Mind & Balance. All rights reserved.</p>
        </div>
    </footer>
    <script src="js/main.js"></script>
</body>
</html>"""
    
    with open(file_path, 'w') as f:
        f.write(html)
    print(f"Created {file_path}")

def update_index():
    with open(INDEX_PATH, 'r') as f:
        content = f.read()
    
    new_cards = ""
    for article in batch_6_articles:
        new_cards += f"""
            <!-- Article {article['id']} -->
            <article class="card hidden delay-1">
                <div class="card-img" style="background-image: url('{article['image']}');"></div>
                <div class="card-content">
                    <span class="card-category" style="background: var(--accent-gradient); color: white; padding: 0.1rem 0.5rem; border-radius: 4px;">TRENDING</span>
                    <h3 class="card-title">{article['title']}</h3>
                    <p class="card-excerpt">{article['excerpt']}</p>
                    <a href="article{article['id']}.html" class="card-link">Read More &rarr;</a>
                </div>
            </article>"""
    
    # Insert after the articles-grid start
    marker = '<div class="articles-grid">'
    if marker in content:
        content = content.replace(marker, marker + new_cards)
        with open(INDEX_PATH, 'w') as f:
            f.write(content)
        print("Updated index.html with Batch 6.")

def update_sitemap():
    with open(SITEMAP_PATH, 'r') as f:
        content = f.read()
    
    new_urls = ""
    for article in batch_6_articles:
        new_urls += f"""    <url>
        <loc>https://leafanoo.com/article{article['id']}.html</loc>
        <lastmod>{datetime.date.today().isoformat()}</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.9</priority>
    </url>\n"""
    
    if "</urlset>" in content:
        content = content.replace("</urlset>", new_urls + "</urlset>")
        with open(SITEMAP_PATH, 'w') as f:
            f.write(content)
        print("Updated sitemap.xml")

if __name__ == "__main__":
    for art in batch_6_articles:
        generate_article(art)
    update_index()
    update_sitemap()
