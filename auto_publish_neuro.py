import os
import re
import datetime
import csv

BASE_DIR = "/Users/khalidaitelmaati/Desktop/scrapy-master/psychology-theme-main"
INDEX_PATH = os.path.join(BASE_DIR, "index.html")
SITEMAP_PATH = os.path.join(BASE_DIR, "sitemap.xml")

articles_to_generate = {
    39: {
        "title": "What Psychology Says About: The Hidden Brain Switch That Tells You to Stop Eating",
        "category": "Neuropsychology",
        "desc": "Neuroscientists have discovered that astrocytes, once thought to be simple support cells, actually control your brain's satiety signals. Learn how this impacts binge eating.",
        "content": """<h2>Introduction</h2>
        <p>For decades, the psychological understanding of overeating was rooted in a lack of willpower, emotional distress, or poor habit formation. People struggling with binge eating were prescribed cognitive behavioral tools, but neuroscientists have recently made a groundbreaking discovery that flips this paradigm on its head: the "stop eating" signal is not purely a psychological choice, it is a neurochemical domino effect triggered by a specific, previously overlooked brain cell.</p>
        <p>A recent 2026 study in neuro-metabolism revealed that <strong>astrocytes</strong>—cells in the brain that scientists previously dismissed as mere "glue" to support neurons—actually play the primary role in controlling your appetite and satiety. When you eat, glucose levels rise and hit specialized sensors called tanycytes. These tanycytes then send an urgent message to the astrocytes, which physically command the fullness neurons to fire, shutting down the urge to keep eating.</p>
        <p>This is a revolutionary finding for clinical psychology and weight management. It proves that the feeling of bottomless hunger isn't just an emotional void—it might be a physical miscommunication in your brain's astrocyte network.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        
        <h2>Astrocytes: The Brain's Hidden Appetite Regulators</h2>
        <p>In traditional neuropsychology models, neurons were the stars of the show. We believed that hunger was controlled purely by the hypothalamus releasing hormones like ghrelin (the hunger hormone) and leptin (the fullness hormone) directly to neurons. But the brain is far more complex. Astrocytes make up a massive percentage of brain volume, and we now know they act as the biological middle-manager between your stomach and your hunger neurons.</p>
        <p>When you consume a meal, particularly one high in simple carbohydrates, the rapid spike in glucose hits the tanycytes rapidly. If the communication channel between tanycytes and astrocytes is damaged—perhaps by chronic stress, sleep deprivation, or a long-term hyper-processed diet—the "stop eating" signal gets delayed. This delayed signal explains the psychological phenomenon of <em>hyperphagia</em>, where an individual feels the intense urge to keep consuming food even when their stomach is physically stretched to its limit.</p>
        
        <h2>The Psychology of Binge Eating Re-Evaluated</h2>
        <p>Understanding this biological mechanism is incredibly freeing for individuals suffering from Binge Eating Disorder (BED). The profound guilt and shame that follows a binge episode often stems from the belief that they simply "lacked discipline." Knowing that a delayed astrocyte response is responsible for the uncontrollable urge removes the moral failing from the equation.</p>
        <p>Therapists are now beginning to integrate this neuroscience into traditional cognitive behavioral therapy (CBT). By understanding that your brain's braking mechanism is simply 'lagging,' patients can employ mindful eating tactics—such as the 20-minute rule (waiting 20 minutes before taking a second helping)—to intentionally give their delayed astrocyte network the time it needs to finally trigger the satiety neurons.</p>

        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        
        <h2>Key Takeaways for Mental Health and Diet</h2>
        <ul>
            <li><strong>You Are Not Broken:</strong> The inability to stop eating is often a neurochemical delay in your astrocyte network, not a failure of willpower.</li>
            <li><strong>The 20-Minute Window:</strong> Astrocytes can take time to process the glucose signals from tanycytes. Slowing down your eating gives the biological "stop" signal time to activate.</li>
            <li><strong>Stress Damages the Signal:</strong> Chronic psychological stress creates rampant inflammation in the brain, which physically degrades how efficiently astrocytes can communicate with your fullness neurons. Managing anxiety is a direct requirement for managing appetite.</li>
        </ul>"""
    },
    40: {
        "title": "Mental Health Hacks: The Protein That Drives Brain Aging (And How to Stop It)",
        "category": "Cognitive Health",
        "desc": "A single protein known as FTL1 has been identified as a primary driver of memory decline and brain aging. Discover the science behind cognitive longevity.",
        "content": """<h2>Introduction</h2>
        <p>The fear of cognitive decline—losing our memories, our sharp wit, and our sense of self—is one of the most universal psychological anxieties as we age. For years, science has told us that brain aging was simply a consequence of time. It was an inevitable wearing down of the machine. But a groundbreaking new study has isolated a specific culprit: a single protein called <strong>FTL1</strong>.</p>
        <p>In extensive aging models, neuroscientists discovered that as the brain grows older, the accumulation of FTL1 actively destroys the synaptic connections between neurons. These connections are the literal physical pathways of your memories and thoughts. However, the true breakthrough was not discovering the damage, but discovering the reversal. When researchers artificially reduced FTL1 levels in aging models, the brain did not just stop deteriorating—it actively rejuvenated, rebuilding the lost connections and restoring youthful memory capacity.</p>
        <p>This revelation completely changes how we approach cognitive psychology and neuro-longevity. It shifts the paradigm from "coping with decline" to "actively preventing it."</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>

        <h2>How FTL1 Erodes Memory and Focus</h2>
        <p>To understand the devastating psychological impact of FTL1, you have to understand how a memory is formed. When you learn an instrument, remember a conversation, or navigate a new city, your neurons reach out and connect to one another across gaps called synapses. The strength of these synapses is what makes a memory permanent.</p>
        <p>As FTL1 builds up in the brain, it acts like rust on a set of gears. It causes inflammation that makes the synapses brittle and weak. From a psychological perspective, this manifests as "brain fog," the frustrating inability to recall a word on the tip of your tongue, or walking into a room and forgetting why you went there. Previously, we accepted this as normal 'senior moments,' but we now recognize it as the active neurotoxicity of the FTL1 protein.</p>

        <h2>The Psychology of Neuroplasticity</h2>
        <p>The most exciting psychological implication of this discovery is the reinforcement of <em>Neuroplasticity</em>—the brain's ability to heal and rewire itself at any age. For decades, the dogma was that once brain cells died off, they were gone forever. The FTL1 reversal trial proves that the aging brain retains its youthful capacity to grow new connections, it is simply being suppressed by toxic proteins.</p>
        <p>While targeted FTL1-blocking drugs are still in development, the psychiatric community is utilizing this knowledge to promote neuro-protective behaviors. High-intensity aerobic exercise, intermittent fasting, and deep restorative sleep have all been clinically proven to activate the brain's "glymphatic system"—the cellular waste-removal process that actively flushes toxic proteins like FTL1 out of the cerebral cortex.</p>

        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        
        <h2>Key Takeaways for Cognitive Longevity</h2>
        <ul>
            <li><strong>Aging is Not Inevitable:</strong> Cognitive decline is driven by specific biological mechanisms, like the accumulation of the FTL1 protein, rather than the mere passage of time.</li>
            <li><strong>Reversible Damage:</strong> The brain retains profound neuroplasticity well into old age. If toxic burdens are lifted, the brain can rebuild corrupted memory pathways.</li>
            <li><strong>Flush the Toxins:</strong> Prioritizing deep sleep and cardiovascular exercise acts as a mechanical flush for the brain, helping clear out the proteins that drive age-related brain fog.</li>
        </ul>"""
    },
    41: {
        "title": "The Psychological Reason For: These Overlooked Brain Cells Control Fear and PTSD",
        "category": "Trauma & PTSD",
        "desc": "Astrocytes do more than support the brain—they are central to how we form, process, and ultimately overcome traumatic fear memories.",
        "content": """<h2>Introduction</h2>
        <p>Post-Traumatic Stress Disorder (PTSD) is one of the most notoriously difficult psychological conditions to treat. When a person experiences a severe trauma, the fear memory burns so brightly into their brain circuits that everyday triggers—like a loud noise or a specific smell—can induce violent panic attacks years later. For decades, psychiatrists focused entirely on the amygdala and its neurons to explain this phenomenon. But they were missing half the picture.</p>
        <p>Recent neurobiological studies have uncovered a radical truth: <strong>Astrocytes</strong>, the star-shaped cells long believed to be nothing more than the scaffolding holding the brain together, are actually the master controllers of fear. Researchers have discovered that these overlooked cells actively dictate how strong a fear memory becomes, how vividly it is recalled, and most importantly, how easily it can be erased.</p>
        <p>This discovery provides immense hope. It opens up an entirely new avenue for targeted PTSD treatments and fundamentally changes our psychological understanding of how trauma physically anchors itself in the human mind.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>

        <h2>The Mechanism of a Traumatic Memory</h2>
        <p>In a healthy brain, experiencing a terrifying event triggers a memory that is eventually "extinguished." For example, if you are bitten by a dog, you develop a fear of dogs. But after encountering hundreds of friendly dogs over the next few years, your brain overwrites the fear, realizing the threat has passed. This is known in psychology as <em>Fear Extinction</em>.</p>
        <p>In a brain suffering from PTSD, fear extinction fails. The brain remains trapped in the exact moment of the trauma. We now know that astrocytes are the key regulators of this extinction process. During a traumatic event, astrocytes surge with calcium, releasing chemical signals that essentially "superglue" the fear neurons together. In individuals with PTSD, these astrocytes become hyper-reactive, refusing to let the metaphorical superglue dissolve, making it neurologically impossible to move on from the fear.</p>

        <h2>A New Frontier for Trauma Therapy</h2>
        <p>Currently, the gold standard for treating PTSD is Exposure Therapy, where patients are repeatedly exposed to their triggers in a safe environment until the fear subsides. It is grueling, psychologically painful work, and it doesn't work for everyone. Why? Because if the astrocytes in that patient's brain are hyper-locked, no amount of talk therapy alone can easily break the chemical bond of the fear memory.</p>
        <p>By understanding astrocyte behavior, neuro-pharmacologists are now developing interventions designed to temporarily suppress astrocyte calcium signaling during therapy sessions. This chemical "loosening" of the fear network could allow traditional exposure therapies to work ten times faster, finally giving severe trauma survivors a reliable path to processing their past and reclaiming their future.</p>

        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        
        <h2>Key Takeaways for Understanding Trauma</h2>
        <ul>
            <li><strong>Trauma is Physical:</strong> PTSD is not a failure to "get over it." It is a profound physical restructuring of the brain's fear network, heavily mediated by astrocyte cells.</li>
            <li><strong>The Fear Superglue:</strong> Overactive astrocytes effectively lock traumatic memories in place, preventing the natural psychological process of fear extinction.</li>
            <li><strong>The Future of Healing:</strong> By targeting astrocytes alongside traditional cognitive behavioral exposure therapy, we are entering a revolutionary new era of rapid trauma healing.</li>
        </ul>"""
    }
}

def generate_article_html(art_id, data):
    date_str = datetime.datetime.now().strftime("%B %d, %Y")
    title = data["title"]
    desc = data["desc"]
    cat = data["category"]
    content = data["content"]
    
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Mind &amp; Balance</title>
    <meta name="description" content="{desc}">
    <link rel="stylesheet" href="css/style.css">
    <link rel="icon" type="image/svg+xml" href="images/favicon.svg">
    <meta property="og:title" content="{title} | Mind &amp; Balance">
    <meta property="og:description" content="{desc}">
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://leafanoo.com/article{art_id}.html">
    <meta property="og:image" content="https://images.unsplash.com/photo-1559757175-5700dde675bc?auto=format&fit=crop&q=80&w=1200">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <link rel="canonical" href="https://leafanoo.com/article{art_id}.html">
    <!-- Google Tag Manager -->
    <script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':
    new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
    'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
    }})(window,document,'script','dataLayer','GTM-MWJD24QX');</script>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6659437008463310" crossorigin="anonymous"></script>
</head>
<body>
    <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-MWJD24QX" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
    <div class="progress-container"><div class="progress-bar" id="progress-bar"></div></div>
    <header>
        <nav class="nav-container">
            <div class="logo">Mind &amp; Balance</div>
            <div class="nav-right">
                <ul class="nav-links">
                    <li><a href="index.html">Home</a></li>
                    <li><a href="index.html#articles" class="active">Articles</a></li>
                    <li><a href="about.html">About</a></li>
                    <li><a href="contact.html">Contact</a></li>
                </ul>
                <button id="theme-toggle" class="theme-toggle" aria-label="Toggle Dark Mode">🌙</button>
            </div>
        </nav>
    </header>

    <div class="article-header hidden">
        <div class="container">
            <span class="card-category" style="display:block; margin-bottom:1rem;">{cat}</span>
            <h1 style="font-size: 3rem; max-width: 800px; margin: 0 auto;">{title}</h1>
            <div class="article-meta">
                <img src="https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&q=80&w=100&h=100" alt="Mind & Balance Editorial Team">
                <span>By Mind &amp; Balance Editorial Team</span>
                <span>•</span><span>{date_str}</span><span>•</span><span>7 min read</span>
            </div>
        </div>
    </div>
    
    <div class="ad-container ad-leaderboard hidden delay-1"></div>

    <div class="article-layout">
        <main class="article-body hidden delay-2">
            {content}
        </main>
        <aside class="article-sidebar hidden delay-3">
            <div class="sticky-sidebar">
                <div class="ad-container ad-sidebar" style="height:600px; margin-top:0;"></div>
            </div>
        </aside>
    </div>

    <!-- Medical Disclaimer -->
    <div class="container disclaimer-banner" style="padding: 1rem 0; font-size: 0.85rem; color: var(--text-color); border-top: 1px solid rgba(0,0,0,0.1); text-align: center; opacity: 0.8; margin-top: 2rem;">
        <p><strong>Medical Disclaimer:</strong> The content on Mind &amp; Balance is for informational and educational purposes only and is not a substitute for professional psychological or medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified mental health provider with any questions you may have regarding a medical condition.</p>
    </div>
    
    <footer class="hidden">
        <div class="container">
            <div class="footer-content">
                <div class="footer-col">
                    <h3>Mind &amp; Balance</h3>
                    <p>Providing clear, compassionate, and scientifically grounded psychological insights for everyday life.</p>
                </div>
            </div>
        </div>
    </footer>
    <script src="js/main.js"></script>
</body>
</html>"""

def main():
    new_cards_html = ""
    new_sitemap_xml = ""
    
    for art_id, data in articles_to_generate.items():
        html_content = generate_article_html(art_id, data)
        filepath = os.path.join(BASE_DIR, f"article{art_id}.html")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"Created {filepath}")
        
        # Build Card
        new_cards_html += f"""
            <article class="card hidden delay-1">
                <div class="card-img" style="background-image: url('https://images.unsplash.com/photo-1559757175-5700dde675bc?auto=format&fit=crop&q=80&w=400');"></div>
                <div class="card-content">
                    <span class="card-category">{data['category']}</span>
                    <h3 class="card-title">{data['title']}</h3>
                    <p class="card-excerpt">{data['desc']}...</p>
                    <a href="article{art_id}.html" class="card-link">Read More &rarr;</a>
                </div>
            </article>\n"""
            
        # Build Sitemap
        new_sitemap_xml += f"""    <url>\n        <loc>https://leafanoo.com/article{art_id}.html</loc>\n        <changefreq>monthly</changefreq>\n        <priority>0.9</priority>\n    </url>\n"""

    # Inject into index.html
    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        idx_content = f.read()
    try:
        parts = idx_content.rsplit('<article class="card', 1)
        if len(parts) == 2:
            card_end = parts[1].find('</article>') + len('</article>')
            pre = parts[0] + '<article class="card' + parts[1][:card_end]
            post = parts[1][card_end:]
            idx_content = pre + new_cards_html + post
            with open(INDEX_PATH, 'w', encoding='utf-8') as f:
                f.write(idx_content)
            print("✅ Updated index.html")
    except Exception as e:
        print("Error with index.html injection", e)

    # Inject into sitemap.xml
    with open(SITEMAP_PATH, 'r', encoding='utf-8') as f:
        sitemap = f.read()
    sitemap = sitemap.replace('</urlset>', f'{new_sitemap_xml}</urlset>')
    with open(SITEMAP_PATH, 'w', encoding='utf-8') as f:
        f.write(sitemap)
    print("✅ Updated sitemap.xml")

if __name__ == "__main__":
    main()
