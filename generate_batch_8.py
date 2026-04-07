import os
import re
import datetime

BASE_DIR = "/Users/khalidaitelmaati/Desktop/scrapy-master/psychology-theme-main"
INDEX_PATH = os.path.join(BASE_DIR, "index.html")
SITEMAP_PATH = os.path.join(BASE_DIR, "sitemap.xml")

batch_8_articles = [
    {
        "id": 146,
        "title": "Why Memory Loss Can Suddenly Speed Up with Age: A Psychological Perspective",
        "category": "Cognitive Psychology",
        "image": "https://images.unsplash.com/photo-1559757175-5700dde675bc?auto=format&fit=crop&q=80&w=600",
        "excerpt": "A massive international brain study has identified why some people experience a rapid acceleration in memory decline—and how to slow it down.",
        "content": "A new international study of thousands of MRI scans has revealed that memory loss isn't a linear process. Instead, it often hits a 'tipping point' where structural changes across the brain begin to build up and accelerate. Researchers found that this acceleration is closely linked to vascular health and chronic low-level inflammation. By addressing these factors through diet and aerobic exercise in middle age, individuals can significantly delay this tipping point and maintain cognitive clarity well into their 80s and 90s. The discovery moves memory care from 'reactive' to 'proactive' prevention.",
        "qa": [
            {"q": "At what age does memory loss typically speed up?", "a": "The acceleration often begins in the late 60s or early 70s, but the structural foundations are laid decades earlier."},
            {"q": "Can I reverse memory loss?", "a": "While you cannot reverse cell death, you can improve neural efficiency and slow down the rate of future decline through lifestyle changes."}
        ]
    },
    {
        "id": 147,
        "title": "The Science of Why Music Brings No Joy to Some People: Muscial Anhedonia",
        "category": "Neuroscience",
        "image": "https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&q=80&w=600",
        "excerpt": "Imagine a world without the emotional lift of a song. Discover why some brains are physically incapable of feeling joy from music.",
        "content": "Musical anhedonia is a rare but fascinating neurological condition where an individual has normal hearing and emotions but feels absolutely nothing when listening to music. Brain imaging has shown that while their auditory cortex registers the sounds perfectly, the reward system (which normally releases dopamine in response to music) remains dormant. This specific 'reward-disconnect' tells us that music is a highly specialized biological trait that evolved to foster social bonding. For those with this condition, music is just 'functional sound' rather than an emotional experience, proving that our aesthetic enjoyments are hard-wired into our neural circuits.",
        "qa": [
            {"q": "Is musical anhedonia a sign of depression?", "a": "No, it is a specific neurological disconnect; people with this condition still enjoy other rewards like food, money, or social success."},
            {"q": "Can animals have musical anhedonia?", "a": "It is difficult to test, but since many animals respond to rhythm and tone, it is likely that pleasure from sound is a widespread evolutionary trait."}
        ]
    },
    {
        "id": 148,
        "title": "The Tryptophan System: When Brain Chemistry Decides to Heal or Harm",
        "category": "Biological Psychology",
        "image": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&q=80&w=600",
        "excerpt": "Tryptophan does far more than help us sleep—it's the master regulator of mood and neuro-inflammation. Discover the heal-or-harm switch.",
        "content": "Tryptophan is often called the 'sleep chemical,' but its role in the brain is far more complex. It is the precursor to serotonin (the 'happiness' chemical), but if the brain is under chronic stress or inflammation, tryptophan can be diverted down a harmful path known as the 'kynurenine pathway.' This pathway produces neurotoxic byproducts that lead to depression, anxiety, and memory loss. Research into this 'tryptophan switch' is leading to new treatments that aim to 'push' tryptophan back toward healing pathways, offering hope for those with treatment-resistant mental health conditions.",
        "qa": [
            {"q": "What foods are high in tryptophan?", "a": "Turkey, seeds, nuts, cheese, and eggs are all rich in this essential amino acid."},
            {"q": "Does eating tryptophan make you happy?", "a": "Only if your brain isn't already inflamed; otherwise, it may be converted into harmful byproducts instead of serotonin."}
        ]
    },
    {
        "id": 149,
        "title": "A Therapist's View on: Does Exercise Really Rival Therapy for Depression?",
        "category": "Mental Health hacks",
        "image": "https://images.unsplash.com/photo-1506126613408-eca07ce68773?auto=format&fit=crop&q=80&w=600",
        "excerpt": "A massive meta-analysis suggests that aerobic exercise can be as effective as psychotherapy and medication for moderate depression.",
        "content": "A sweeping review of 97 global studies has confirmed that exercise is one of the most powerful 'biological' treatments for depression and anxiety. For many with mild-to-moderate symptoms, 150 minutes of weekly activity produced relief comparable to standard Cognitive Behavioral Therapy (CBT) and SSRI medications. The reason is that exercise immediately increases BDNF (brain fertilizer) and metabolizes stress hormones. This doesn't mean you should quit your therapy; rather, it shows that movement is an essential, data-driven 'manual' for mood regulation that should be a core part of any mental health plan.",
        "qa": [
            {"q": "Which type of exercise is best for depression?", "a": "Aerobic activities like running, swimming, or dancing have the strongest evidence, but even brisk walking shows significant benefits."},
            {"q": "Can I replace my medication with exercise?", "a": "Never stop medication without professional medical supervision. Exercise is most effective when used alongside your existing treatment plan."}
        ]
    },
    {
        "id": 150,
        "title": "Why Japanese Scientists Built Human Brain Circuits in the Lab: Matters for Mental Health",
        "category": "Neuroscience",
        "image": "https://images.unsplash.com/photo-1507413245164-6160d8298b31?auto=format&fit=crop&q=80&w=600",
        "excerpt": "Japanese researchers have successfully grown functional human brain circuits in the lab, allowing them to watch neural signals in real time.",
        "content": "Researchers in Japan have achieved a milestone in neuroscience by fusing stem-cell derived 'organoids' to create miniature human brain circuits. For the first time, scientists can watch how the thalamus and the cortex—the brain's command centers—interact during development. They discovered that the thalamus is essential for 'organizing' the neural networks that eventually handle sensory data and emotions. This breakthrough would allow for the testing of new schizophrenia and autism treatments on real human circuits in a laboratory setting, bypassing the need for animal models and speeding up the path to a cure.",
        "qa": [
            {"q": "Is a lab-grown brain conscious?", "a": "No, these are tiny clusters of cells that mimic specific circuits; they lack the complexity and sensory input required for consciousness."},
            {"q": "How does this help autism research?", "a": "It allows scientists to see exactly how neural connections are formed and where they might go 'awry' during early brain development."}
        ]
    },
    {
        "id": 151,
        "title": "The Simplest Way Teens Can Protect Their Mental Health: The Weekend Sleep Shield",
        "category": "Behavioral Psychology",
        "image": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&q=80&w=600",
        "excerpt": "Teens who make up for lost weekday sleep on the weekends have a significantly lower risk of depression. Learn the science of 'sleeping in.'",
        "content": "Adolescent depression is on the rise, and sleep deprivation is a primary trigger. A new study found that 'weekend catch-up sleep'—sleeping in on a Saturday or Sunday—acts as a powerful biological shield against mood disorders. During these extra hours, the developing teen brain is able to complete the essential 'removals' of toxic waste from the day before and stabilize the emotional centers like the amygdala. While consistent 9-hour nights are the gold standard, this weekend buffer is an evidence-based way to prevent the build-up of the 'sleep debt' that so often leads to clinical burnout and anxiety in teenagers.",
        "qa": [
            {"q": "Does sleeping in mess up a teen's internal clock?", "a": "Slightly, but for most teens, the mental health benefits of the extra sleep outweigh the minor shift in their circadian rhythm."},
            {"q": "How much sleep does a teen actually need?", "a": "Between 8 and 10 hours of high-quality sleep is the biological requirement for optimal brain development in humans between 13 and 19."}
        ]
    },
    {
        "id": 152,
        "title": "Inside Why Nearly All Women in STEM Secretly Feel Like Impostors: What the Brain Tells Us",
        "category": "Career Psychology",
        "image": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&q=80&w=600",
        "excerpt": "Imposter syndrome is a critical issue in high-performance fields like STEM. Discover the psychological cost of feeling like a 'fraud.'",
        "content": "A striking new study has revealed that nearly all women in graduate-level STEM programs experience imposter syndrome, despite objective evidence of their high intelligence and success. This mindset—attributing success to luck rather than skill—leads to chronic stress, higher burnout rates, and a significantly increased risk of dropping out. Psychologically, it creates a 'threat-focused' state of mind that prevents the individual from actually enjoying their achievements. Overcoming imposterism requires building strong female-centric networks and shifting the narrative from 'perfection' to 'persistence' in scientific communities.",
        "qa": [
            {"q": "Is imposter syndrome a mental illness?", "a": "No, it is a psychological pattern or mindset, but it is a major risk factor for clinical anxiety and depression."},
            {"q": "Are men affected by imposter syndrome?", "a": "Yes, but studies show women, especially in male-dominated fields, experience it at much higher intensities and frequencies."}
        ]
    },
    {
        "id": 153,
        "title": "What the Hidden Timing System Reveals About Your Daily Behavior",
        "category": "Personality Psychology",
        "image": "https://images.unsplash.com/photo-1559757175-5700dde675bc?auto=format&fit=crop&q=80&w=600",
        "excerpt": "Your brain operates on different ' timescales' for different tasks. Discover how your internal clocks shape your personality and focus.",
        "content": "The brain constantly blends split-second reactions with slower, more thoughtful processing. New research shows that different regions of the brain literally operate on different 'clocks.' Fast regions in the sensory cortex handle immediate reflex, while slow-timing regions in the prefrontal cortex manage complex moral and social judgments. If these clocks fall out of sync—often due to stress or lack of sleep—you may feel impulsive, foggy, or disconnected from your own thoughts. Understanding your 'mental timing' helps you schedule your day better, doing fast, reactive work when you are 'up' and slow, deep work when you are calm.",
        "qa": [
            {"q": "What happens if my brain 'clocks' are out of sync?", "a": "You may experience symptoms of ADHD, brain fog, or an inability to regulate your emotions effectively."},
            {"q": "Can meditation fix my brain's timing?", "a": "Yes, mindfulness practices are proven to help sync these different neural timescales, improving overall cognitive control and focus."}
        ]
    },
    {
        "id": 154,
        "title": "A Therapist's View on: How Brain Scans and Yueju Pill May End Guesswork in Depression",
        "category": "Clinical Psychology",
        "image": "https://images.unsplash.com/photo-1507413245164-6160d8298b31?auto=format&fit=crop&q=80&w=600",
        "excerpt": "A traditional medicine known as the Yueju Pill is showing a unique ability to boost mood-regulating proteins in the brain better than some standard SSRIs.",
        "content": "In a head-to-head clinical trial, the Yueju Pill—a traditional Chinese remedy—reduced depression symptoms as effectively as fluoxetine (Prozac). However, brain scans revealed a critical difference: only the Yueju Pill increased a specific protein that supports the growth and health of the hippocampus. This suggests that while both treatments ease sadness, the pill may offer a more direct way to 're-grow' the brain's emotional resilience. This discovery is pushing scientists to rethink how we use natural compounds to supplement modern psychiatry, potentially ending the 'guesswork' of finding the right depression treatment.",
        "qa": [
            {"q": "Is the Yueju Pill better than Prozac?", "a": "Not necessarily for everyone, but for some, it appears to have a more protective effect on brain structure and recovery proteins."},
            {"q": "Does traditional medicine have side effects?", "a": "All active substances have potential side effects; it's essential to consult a professional before mixing supplements with prescriptions."}
        ]
    },
    {
        "id": 155,
        "title": "A Therapist's View on: Why Warm Hugs and Temperature Matter for Mental Health",
        "category": "Behavioral Psychology",
        "image": "https://images.unsplash.com/photo-1516589174184-c685ca33d2b0?auto=format&fit=crop&q=80&w=600",
        "excerpt": "We are thermostatic creatures. Discover why warmth from a hug or a bath is interpreted by the brain as immediate emotional safety.",
        "content": "Why do we feel 'cold' when we are lonely? It's not just a metaphor. Our brain's thermostat and its social-reward center are physically overlapped in the insular cortex. When we experience physical warmth (like a hug or a warm weighted blanket), the brain registers this as 'social presence,' immediately slowing the heart rate and lowering cortisol. This 'thermal regulation' is one of the most primitive ways we feel safe. For those struggling with trauma or anxiety, consciously seeking out physical warmth can be a powerful, non-verbal way to signal to the nervous system that the 'danger' is over and it is safe to rest.",
        "qa": [
            {"q": "Can warmth help with anxiety?", "a": "Yes, physical warmth triggers the parasympathetic nervous system, which is our body's natural 'braking system' for stress and panic."},
            {"q": "Why do some people dislike being hugged?", "a": "For those with sensory processing issues or trauma, the physical contact might over-stimulate the nervous system, overriding the 'warmth' benefit."}
        ]
    },
    {
        "id": 156,
        "title": "A Therapist's View on: What Mini-Brains Reveal About Schizophrenia and Bipolar Signals",
        "category": "Neuroscience",
        "image": "https://images.unsplash.com/photo-1559757175-5700dde675bc?auto=format&fit=crop&q=80&w=600",
        "excerpt": "Tiny human brain circuits grown in a lab are producing 'electrical signatures' that identify Schizophrenia and Bipolar disorder with high accuracy.",
        "content": "Stem-cell derived 'mini-brains' are revolutionizing psychiatry. Scientists have discovered that brains grown from patients with Schizophrenia and Bipolar disorder produce unique electrical 'firing' patterns that are virtually absent in healthy brains. These signals show that these conditions aren't just 'behavioral'—they are fundamental glitches in how neural circuits communicate. By identifying these electrical signatures early, we can potentially diagnose these conditions before life-shattering symptoms even appear, and test personalized medications that 'tune' these electrical signals back to health.",
        "qa": [
            {"q": "How accurate is a 'mini-brain' diagnosis?", "a": "In laboratory settings, these electrical signatures can identify specific psychiatric conditions with over 80% accuracy."},
            {"q": "Can these mini-brains be used for drug testing?", "a": "Yes, that is their primary use—testing hundreds of medications on a patient's own neural cells to find the perfect match."}
        ]
    },
    {
        "id": 157,
        "title": "What A Hidden Brain Drainage Problem Reveals About Your Alzheimer’s Risk",
        "category": "Clinical Psychology",
        "image": "https://images.unsplash.com/photo-1507413245164-6160d8298b31?auto=format&fit=crop&q=80&w=600",
        "excerpt": "Blockages in the brain's 'drain' system are now being linked to the earliest stages of Alzheimer's. Discover the 'glymphatic' warning sign.",
        "content": "The brain's self-cleaning system, known as the glymphatic network, acts like a drainage system to clear out metabolic waste during sleep. Researchers have discovered that clogged brain 'drains' often appear on MRI scans before any memory loss is detected. These clogs allow toxic amyloid plaques to build up and 'choke' neurons. This breakthrough suggests that Alzheimer's might be as much a 'plumbing' problem as a neuro-chemical one. Keeping these drains clear through exercise, hydration, and long, consistent periods of deep sleep may be the most important preventative measure for anyone at risk of cognitive decline.",
        "qa": [
            {"q": "What causes clogged brain drains?", "a": "Aging, sleep apnea, a sedentary lifestyle, and high blood pressure all reduce the efficiency of the brain's drainage system."},
            {"q": "How can I check my brain's drainage?", "a": "While still specialized, advanced MRI scans can now measure the 'flow' of cerebrospinal fluid through these critical channels."}
        ]
    },
    {
        "id": 158,
        "title": "The Science of The A Key Alzheimer’s Gene and Its Impact on Every Brain",
        "category": "Neuroscience",
        "image": "https://images.unsplash.com/photo-1559757175-5700dde675bc?auto=format&fit=crop&q=80&w=600",
        "excerpt": "A newly identified Alzheimers gene, ADAMTS2, was discovered in a landmark study of African American brains. Learn its impact on us all.",
        "content": "A major breakthrough in the study of diverse brains has identified a key gene, ADAMTS2, that is significantly more active in brains with Alzheimer's. This gene was discovered during a landmark study focused on African American donors—a group traditionally underrepresented in medical research. Interestingly, this gene appears to play a critical role in 'neuro-inflammation' across all racial groups. By targeting ADAMTS2, scientists believe they can slow down the inflammatory cascade that destroys memory. This discovery proves that diversifying medical research doesn't just help specific groups—it unlocks the hidden biology of the human brain for everyone.",
        "qa": [
            {"q": "Why was this gene only found now?", "a": "Most previous studies focused almost exclusively on donors of European descent, missing key genetic variations like ADAMTS2."},
            {"q": "Does having this gene mean I will get Alzheimer's?", "a": "No, it is an 'activity' marker that shows increased risk, not a certain diagnosis. Lifestyle factors still play a massive role."}
        ]
    },
    {
        "id": 159,
        "title": "The Couples Who Savor Happy Moments Together: Research on Shared Shields",
        "category": "Relationships",
        "image": "https://images.unsplash.com/photo-1516589174184-c685ca33d2b0?auto=format&fit=crop&q=80&w=600",
        "excerpt": "Intentional 'shared savoring' is proven to strengthen intimacy and shield couples from the toxic effects of everyday life stress.",
        "content": "Happiness isn't just a feeling; it's a practice. A study of 300 couples found that 'shared savoring'—consciously reflecting on and appreciating a happy moment together—built a massive reservoir of relationship trust. This practice acts as a 'psychological shield,' dampening the impact of future arguments and life stress. Partners who savor together report higher levels of intimacy and a deeper sense of 'we-ness.' In a world focused on 'problem-solving,' this research reminds us that soaking in the good times is just as important as fixing the bad times for a long-lasting, resilient relationship.",
        "qa": [
            {"q": "How do we practice 'shared savoring'?", "a": "It can be as simple as spending 5 minutes each day talking about a highlight of your day or reminiscing about a favorite vacation."},
            {"q": "Why does it work on the brain?", "a": "It forces the brain to release oxytocin and dopamine in the presence of the partner, reinforcing the 'safety and reward' connection between you."}
        ]
    },
    {
        "id": 160,
        "title": "160 Articles of Authority: The Future of Leafanoo and Modern Psychology",
        "category": "Wellness",
        "image": "https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&q=80&w=600",
        "excerpt": "We've reached our 160-article milestone. Discover how science-backed psychology is evolving and how you can master your modern mind.",
        "content": "Reaching our 160-article milestone is more than just a number—it represents a comprehensive map of the modern mind. From the neurobiology of addiction to the psychology of a warm hug, we've explored the diverse threads that make us human. As neuroscience continues to evolve, the border between 'mental health' and 'biological health' is disappearing. We now know that your mindset, your diet, and your social circle are all physical parts of your brain's architecture. Going forward, the goal is simple: use this science to reclaim your focus, heal your trauma, and find balance in an increasingly complex world. Thank you for joining us on this journey into the mind.",
        "qa": [
            {"q": "What is the biggest takeaway from 160 articles?", "a": "The brain is remarkably plastic—you are not 'stuck' with your traits; you have the biological potential to change and grow at any age."},
            {"q": "What's next for psychology?", "a": "The focus is shifting toward 'precision psychiatry' and 'preventative neuro-health,' using technology to heal the brain before symptoms appear."}
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
    for article in batch_8_articles:
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
        print("Updated index.html with Batch 8.")

def update_sitemap():
    with open(SITEMAP_PATH, 'r') as f:
        content = f.read()
    
    new_urls = ""
    for article in batch_8_articles:
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
    for art in batch_8_articles:
        generate_article(art)
    update_index()
    update_sitemap()
