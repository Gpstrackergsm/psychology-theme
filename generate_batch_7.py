import os
import re
import datetime

BASE_DIR = "/Users/khalidaitelmaati/Desktop/scrapy-master/psychology-theme-main"
INDEX_PATH = os.path.join(BASE_DIR, "index.html")
SITEMAP_PATH = os.path.join(BASE_DIR, "sitemap.xml")

batch_7_articles = [
    {
        "id": 131,
        "title": "What Clogged Brain Drains Reveal: An Early Warning for Alzheimer’s",
        "category": "Neuroscience",
        "image": "https://images.unsplash.com/photo-1559757175-5700dde675bc?auto=format&fit=crop&q=80&w=600",
        "excerpt": "Clogged brain drainage systems are appearing on MRI scans years before traditional Alzheimer's symptoms, offering a new hope for early detection.",
        "content": "Scientists have discovered that the brain's 'waste removal' system—the glymphatic network—can show signs of blockage long before memory loss begins. These 'clogged drains' prevent the clearing of toxic proteins like amyloid-beta, which eventually lead to Alzheimer's disease. Using advanced MRI imaging, researchers can now spot these blockages in high-risk individuals, providing a critical window for intervention. Maintaining a healthy lifestyle, including deep sleep (when the brain's drainage system is most active) and cardiovascular health, might be the key to keeping your brain's 'plumbing' clear and your mind sharp for decades.",
        "qa": [
            {"q": "What are brain drains?", "a": "They are the glymphatic vessels that clear metabolic waste and toxic proteins from the brain during sleep."},
            {"q": "Can I improve my brain's drainage?", "a": "Getting enough deep sleep and regular exercise are the best ways to support the brain's waste removal system."}
        ]
    },
    {
        "id": 132,
        "title": "A Therapist's View on: Mini Brains and the Electrical Signals of Schizophrenia",
        "category": "Clinical Psychology",
        "image": "https://images.unsplash.com/photo-1507413245164-6160d8298b31?auto=format&fit=crop&q=80&w=600",
        "excerpt": "Tiny lab-grown human brains are revealing the unique electrical 'firing' patterns associated with schizophrenia and bipolar disorder.",
        "content": "Using stem cells from patients with schizophrenia and bipolar disorder, researchers have grown 'mini-brains' in the lab to study their neural activity. They found that these brains exhibit distinct electrical firing patterns compared to healthy controls. Specifically, the interactions between the thalamus and the cortex were disrupted, identifying clear 'signals' of the disorders long before they manifest behaviorally. This breakthrough allows scientists to test new medications on these lab-grown circuits to see which ones restore normal electrical balance, paving the way for truly personalized psychiatric medicine.",
        "qa": [
            {"q": "What is a mini-brain?", "a": "It is a three-dimensional cluster of human brain cells grown in a lab to mimic real brain structure and function."},
            {"q": "How does this help treat schizophrenia?", "a": "It allows doctors to see the biological 'glitch' in the brain's circuitry and test treatments without risking patient health."}
        ]
    },
    {
        "id": 133,
        "title": "A Therapist's View on: Why Warm Hugs Feel So Good to Your Brain",
        "category": "Behavioral Psychology",
        "image": "https://images.unsplash.com/photo-1516589174184-c685ca33d2b0?auto=format&fit=crop&q=80&w=600",
        "excerpt": "Warmth isn't just a physical sensation—it's a psychological signal of safety and connection that heals the emotional brain.",
        "content": "Research shows that our perception of physical temperature is deeply linked to our emotional well-being. When we experience physical warmth, such as a warm hug or a hot drink, our brain's insular cortex—the region responsible for body awareness and empathy—is activated. This signals a state of 'social safety,' lowering cortisol and increasing feelings of trust and connection. In contrast, feeling physically cold can exacerbate feelings of loneliness and isolation. Understanding this 'thermal-emotional' link helps us realize that self-care often involves simple, sensory-rich interactions that tell our brain we are safe.",
        "qa": [
            {"q": "Why do hugs reduce stress?", "a": "They trigger the release of oxytocin and activate the brain's warmth-sensing regions, which counteract the fight-or-flight response."},
            {"q": "Can physical warmth help with depression?", "a": "While not a cure, 'thermal therapy' like warm baths or cozy environments can help regulate the nervous system and slightly lift mood."}
        ]
    },
    {
        "id": 134,
        "title": "The Science of the Yueju Pill: Can Traditional Medicine Outperform SSRIs?",
        "category": "Clinical Psychology",
        "image": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&q=80&w=600",
        "excerpt": "A traditional medicine known as the Yueju Pill is showing similar efficacy to standard antidepressants, but with a unique impact on brain proteins.",
        "content": "Researchers at the Second Affiliated Hospital of Guangzhou University of Chinese Medicine compared the Yueju Pill—a centuries-old traditional remedy—with fluoxetine (Prozac). While both reduced depression symptoms, only the Yueju Pill significantly boosted the levels of BDNF, a critical 'brain-growth' protein in the hippocampus. Brain imaging revealed that the pill improved communication in neural networks responsible for mood and memory. This discovery bridge the gap between ancient wisdom and modern neuroscience, suggesting that some traditional therapies may offer faster relief with fewer side effects than current SSRIs.",
        "qa": [
            {"q": "What is the Yueju Pill?", "a": "It is a traditional Chinese medicine formula often used to 'unblock' stagnation and treat digestive and emotional issues."},
            {"q": "Is it safe to replace my antidepressants with herbal pills?", "a": "No, you should never change your medication without professional medical supervision, even if research is promising."}
        ]
    },
    {
        "id": 135,
        "title": "What the Hidden Timing System Reveals About How You Think",
        "category": "Cognitive Psychology",
        "image": "https://images.unsplash.com/photo-1559757175-5700dde675bc?auto=format&fit=crop&q=80&w=600",
        "excerpt": "Your brain operates on multiple internal 'clocks' simultaneously. Discover how this hidden timing system shapes your perception of reality.",
        "content": "The human brain doesn't have one single clock. Instead, it relies on a complex 'multi-timescale' system. Fast-acting regions process immediate sensory data (like a sudden noise), while slower regions handle deep thought and complex planning. New research shows that white matter connections—the brain's high-speed cables—are the key to syncing these different clocks. Disruptions in this timing system are linked to conditions like schizophrenia and ADHD, where the mind feels 'out of sync' with reality. Learning to manage your mental pace through meditation or focused tasks can help 're-align' your internal clocks for better clarity and focus.",
        "qa": [
            {"q": "How many clocks does the brain have?", "a": "Thousands of neural circuits operate on their own timescales, from milliseconds for hearing to hours for hormone regulation."},
            {"q": "Can I feel my brain's timing system?", "a": "Yes, when you are 'in the zone' or 'flow state,' your brain regions are perfectly synced across all timescales."}
        ]
    },
    {
        "id": 136,
        "title": "Inside Why Women in STEM Feel Like Impostors: What the Brain Tells Us",
        "category": "Career Psychology",
        "image": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&q=80&w=600",
        "excerpt": "Imposter syndrome is exceptionally common among women in STEM, leading to burnout and talent loss. Learn the psychological roots of this 'success fear.'",
        "content": "Despite high achievement, nearly all women in STEM graduate programs report feeling like 'frauds.' This imposter syndrome is more than just humility—on a neurological level, it manifests as a hyper-active 'threat response' to one's own success. The fear of being 'found out' creates a chronic state of stress that leads to burnout and a desire to drop out of the field. Research suggests that this isn't a failure of the individual, but a result of a social environment that subtly questions their belonging. Tackling imposter syndrome requires both personal 'reframing' and structural changes in how success is validated in high-pressure careers.",
        "qa": [
            {"q": "Why is imposter syndrome so common in STEM?", "a": "High-stakes environments and subtle gender biases can lead even the most capable people to doubt their worth."},
            {"q": "How can I overcome imposter feelings?", "a": "Focus on gathering objective evidence of your success and find mentors who can provide honest, external validation."}
        ]
    },
    {
        "id": 137,
        "title": "The Genetic Anxiety Link in Canines & Humans: Are You Born to Worry?",
        "category": "Neurodiversity",
        "image": "https://images.unsplash.com/photo-1552053831-71594a27632d?auto=format&fit=crop&q=80&w=600",
        "excerpt": "Anxiety isn't just 'all in your head'—it's in your genes. Discover the shared biological threads between anxious dogs and humans.",
        "content": "A new genetic study in Golden Retrievers has identified several genes linked to anxiety and high energy that are almost identical in humans. These genes regulate how the brain's amygdala responds to potential threats. If you find yourself constantly 'on edge,' you may have a biological 'anxiety-prone' baseline. While environmental factors matter, understanding your genetic temperament can be empowering. It moves the conversation from 'what is wrong with me?' to 'how do I manage my unique nervous system?'. Research in dogs is helping us develop targeted behavioral therapies that help both mammals lead calmer, more regulated lives.",
        "qa": [
            {"q": "Can I test for 'anxiety genes'?", "a": "While research is growing, standard consumer genetic tests aren't yet reliable for diagnosing clinical anxiety traits."},
            {"q": "If I'm born anxious, can I ever change?", "a": "Yes, neuroplasticity means your brain can learn new coping mechanisms that override your 'genetic baseline' over time."}
        ]
    },
    {
        "id": 138,
        "title": "Cocaine Protein & Brain Memory Rewiring: The Biological Hook of Addiction",
        "category": "Clinical Psychology",
        "image": "https://images.unsplash.com/photo-1559757175-5700dde675bc?auto=format&fit=crop&q=80&w=600",
        "excerpt": "Addiction isn't just a habit; it's a physical rewrite of the brain's memory. Scientists have found the specific protein that 'locks' the addiction circuit.",
        "content": "Researchers at Michigan State University have identified a protein that acts like 'glue' for addiction in the brain. Repeated cocaine use triggers the production of this protein, which physically rewires the connection between the reward system and the memory-heavy hippocampus. This makes the craving for the drug a 'survival memory' that the brain prioritizes over everything else. This biological discovery explains why relapse is so frequent even years after sobriety—the 'hook' is physically etched into the brain's anatomy. New therapies are now being developed to target this protein and 'unlock' the addiction-memory circuit once and for all.",
        "qa": [
            {"q": "Is addiction permanent?", "a": "The memories are permanent, but the 'hook' can be weakened through therapy, medication, and behavioral changes."},
            {"q": "Why is heroin or cocaine so addictive?", "a": "They trigger the brain to produce 'structural' proteins that rapidly build high-speed pathways for craving."}
        ]
    },
    {
        "id": 139,
        "title": "Alzheimer’s Chemical Atlas: How AI Imaging is Changing Cognitive Health",
        "category": "Cognitive Health",
        "image": "https://images.unsplash.com/photo-1507413245164-6160d8298b31?auto=format&fit=crop&q=80&w=600",
        "excerpt": "AI is creating the first molecular maps of the Alzheimer's brain, revealing that chemical changes happen long before plaques are visible.",
        "content": "Rice University scientists have produced the first full atlas of chemical changes in an Alzheimer's brain using laser-based imaging and machine learning. This 'molecular atlas' shows that the disease isn't just about protein plaques; it involves systematic shifts in the chemical balance of neurons across the entire brain. Interestingly, some regions showed major changes while neighboring areas remained normal. This AI-driven insight tells us that Alzheimer's is a 'chemical mosaic,' and that successful treatment will likely require a targeted approach that boosts health in specific brain regions rather than the whole organ at once.",
        "qa": [
            {"q": "What is a 'chemical atlas'?", "a": "It is a map showing the distribution and balance of molecules and chemicals across the entire brain structure."},
            {"q": "How does AI help Alzheimer's patients?", "a": "It helps researchers identify 'high-risk' chemical shifts years earlier, allowing for earlier intervention and better clinical trials."}
        ]
    },
    {
        "id": 140,
        "title": "The Biological Cost of Aging Anxiety: Accelerating Your Cellular Clock",
        "category": "Personality Psychology",
        "image": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&q=80&w=600",
        "excerpt": "The more you worry about aging, the faster your body may actually age. Learn the science of psychosomatic aging acceleration.",
        "content": "A study of over 700 women by NYU has found a striking link between 'aging anxiety' and physical aging. Women who felt highly anxious about future health problems showed faster biological aging in their blood samples, measured by DNA methylation 'clocks.' Chronic fear and anxiety about aging trigger low-level systemic inflammation, which is a primary driver of 'inflamm-aging'—the physical decline of the body. In contrast, those with a positive outlook on aging tended to have 'younger' cells. This research proves that mental health isn't just about feeling good; it is a critical component of physical longevity and biological health.",
        "qa": [
            {"q": "Can anxiety make you look older?", "a": "Yes, chronic stress and high cortisol levels are proven to damage skin collagen and accelerate overall biological aging."},
            {"q": "What is 'psychosomatic' aging?", "a": "It is when a mental state (like chronic worry) causes measurable physical decline and faster cellular aging."}
        ]
    },
    {
        "id": 141,
        "title": "Mental Health Break: Why MS Slowly Steals Balance and Movement",
        "category": "Clinical Psychology",
        "image": "https://images.unsplash.com/photo-1559757175-5700dde675bc?auto=format&fit=crop&q=80&w=600",
        "excerpt": "Multiple Sclerosis doesn't just damage the nerves; it starves them of energy. Discover the 'mitochondrial failure' link to MS disability.",
        "content": "For people with Multiple Sclerosis (MS), the loss of balance and coordination is often the most disabling symptom. New research has discovered a hidden reason: inflammation in the brain disrupts the energy supply of movement-controlling neurons. As the 'mitochondria' (the power plants) of these cells fail, the neurons weaken and eventually die, leading to progressive disability. This discovery shifts the focus of MS research from just 'stopping inflammation' to also 'protecting energy production.' Supporting brain energy through specific nutrients and metabolic health may become a core part of managing the psychological and physical burden of MS in the future.",
        "qa": [
            {"q": "What is the primary cause of MS symptoms?", "a": "It is an autoimmune attack on 'myelin' (nerve insulation), but new research shows energy failure in neurons is also critical."},
            {"q": "Can exercise help MS balance?", "a": "Yes, specialized balance and strength training can help the brain 'rewire' around damaged areas, though it cannot cure the disease."}
        ]
    },
    {
        "id": 142,
        "title": "Why The Weekend Sleep Shield Matters for Teen Mental Health",
        "category": "Behavioral Psychology",
        "image": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&q=80&w=600",
        "excerpt": "Teens who 'sleep in' on weekends are actually protecting themselves from depression. Discover the science of 'weekend catch-up' sleep.",
        "content": "Adolescents are notoriously sleep-deprived due to early school starts and homework. A new study found that teens who made up for lost weekday sleep on the weekends had a significantly lower risk of clinical depression. While consistent sleep is ideal, this 'weekend shield' provides a biological safety net, allowing the brain to clear toxic waste and stabilize mood. For parents, this research suggests that letting your teen sleep in on a Saturday isn't 'laziness'—it's an essential mental health intervention that helps their developing brain recover from the stress of a busy week.",
        "qa": [
            {"q": "Is weekend catch-up sleep as good as daily sleep?", "a": "No, consistent 8-10 hours is best, but catching up is much better for mental health than staying chronically sleep-deprived."},
            {"q": "Why do teens need more sleep?", "a": "Their brains are undergoing massive remodeling, which requires deep sleep to process information and regulate emotions."}
        ]
    },
    {
        "id": 143,
        "title": "What Generosity and Brain Wave Syncing Reveals About Our Behavior",
        "category": "Social Psychology",
        "image": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&q=80&w=600",
        "excerpt": "Generosity isn't just a moral choice; it's a neurological state. Scientists have successfully used brain wave syncing to increase kindness.",
        "content": "Is kindness biological? A new study suggests it might be. By gently stimulating the brain to 'sync' its electrical waves, researchers were able to make participants significantly more generous and willing to share resources with others. The researchers found that when the regions of the brain responsible for empathy and reward were in perfect electrical sync, the person's natural instinct to help others became the dominant path. This research suggests that social behaviors like cooperation and altruism are fundamental biological strategies for human survival, hard-wired into our neural circuitry.",
        "qa": [
            {"q": "Does this mean kindness is 'forced'?", "a": "No, it means the brain's internal 'cooperation circuit' was simply optimized, allowing natural empathy to flow more easily."},
            {"q": "Can we use this to treat social disorders?", "a": "Potentially. In the future, non-invasive brain stimulation could help individuals who struggle with social cues or empathy-related behaviors."}
        ]
    },
    {
        "id": 144,
        "title": "The Science of Music Anhedonia: Why Music Brings No Joy to Some People",
        "category": "Personality Psychology",
        "image": "https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&q=80&w=600",
        "excerpt": "A small group of people experience no pleasure from music despite normal hearing and emotions. Discover the 'reward-input' disconnect.",
        "content": "For about 5% of the population, music is just 'organized noise' that fails to trigger any emotional response—a condition known as musical anhedonia. Brain imaging reveals that their auditory cortex (hearing) and their reward system (pleasure) simply fail to communicate properly when music is playing. Interestingly, these individuals still experience pleasure from other things like food or sex; the disconnect is specific to music. This unique condition helps neuroscientists understand how the brain's 'pleasure circuits' are partitioned, showing that our emotional life is a complex mosaic of independent neural pathways.",
        "qa": [
            {"q": "What is musical anhedonia?", "a": "It is a condition where a person cannot feel pleasure from music, even though their hearing and general emotions are normal."},
            {"q": "Is there a cure for musical anhedonia?", "a": "There is no 'cure' as it's not a disease, but rather a unique neurological variation in how pleasure is processed."}
        ]
    },
    {
        "id": 145,
        "title": "What The 1-Hour TV Swap Data Reveals About Your Depression Risk",
        "category": "Mental Health hacks",
        "image": "https://images.unsplash.com/photo-1484480974693-6ca0a78fb36b?auto=format&fit=crop&q=80&w=600",
        "excerpt": "Swapping 60 minutes of passive screen time for an active hobby can significantly lower your risk of clinical depression. Learn the science of engagement.",
        "content": "A massive Dutch study of 65,000 adults has found that replacing just one hour of TV a day with an active hobby—like gardening, walking, or crafts—slashed the risk of major depression. The reason is the 'rumination loop.' Passive screen time often allows the brain to fall into circular negative thinking, while active hobbies force cognitive engagement and 'flow.' This active focus naturally breaks the depressive patterns of the mind. For anyone feeling low, this 'one-hour swap' is one of the most evidence-based, low-cost ways to shield your mental health and reclaim your daily energy.",
        "qa": [
            {"q": "Is all TV bad for depression?", "a": "No, but long stretches of 'passive' consumption are linked to higher risk. An hour of active engagement is much better for your mood."},
            {"q": "What's the best replacement hobby?", "a": "Anything that requires physical movement and focus is ideal, as it effectively interrupts depressive thought patterns."}
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
    for article in batch_7_articles:
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
        print("Updated index.html with Batch 7.")

def update_sitemap():
    with open(SITEMAP_PATH, 'r') as f:
        content = f.read()
    
    new_urls = ""
    for article in batch_7_articles:
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
    for art in batch_7_articles:
        generate_article(art)
    update_index()
    update_sitemap()
