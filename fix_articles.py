import os
import re

BASE_DIR = "/Users/khalidaitelmaati/Desktop/scrapy-master/psychology-theme-main"
INDEX_PATH = os.path.join(BASE_DIR, "index.html")

new_articles = {
    36: {
        "title": "7 Signs You Are Dealing with a Covert Narcissist",
        "category": "Relationships",
        "desc": "Unlike grandiose narcissists, covert narcissists hide in plain sight. Learn the psychological red flags of passive-aggressive manipulation and protect your peace.",
        "content": """<h2>Introduction</h2>
        <p>When most people hear the word "narcissist," they picture someone who is loud, arrogant, and constantly demanding the center of attention. However, psychology recognizes a far more insidious subtype: the Covert Narcissist. Covert narcissists possess the same lack of empathy and need for admiration, but they hide it behind a mask of victimhood, introversion, and passive-aggression.</p>
        <p>Because they do not fit the classic stereotype, they are incredibly difficult to spot. You might spend years feeling perpetually guilty, confused, or exhausted in the relationship without understanding why. They use subtle manipulation tactics to make you question your own reality, a technique known as gaslighting.</p>
        <p>In this guide, we break down the clinical markers of covert narcissism. Understanding these hidden signs is the first crucial step to protecting your emotional boundaries and breaking free from the cycle of subtle emotional abuse.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        <h2>Key Takeaways</h2>
        <ul>
            <li><strong>The Perpetual Victim:</strong> They constantly cast themselves as the victim in every situation, refusing to take accountability for their actions.</li>
            <li><strong>Passive-Aggressive Hostility:</strong> Instead of outward anger, they use backhanded compliments, silent treatments, and weaponized incompetence.</li>
            <li><strong>Hypersensitivity to Criticism:</strong> Even the mildest constructive feedback triggers an intense, defensive sulking or a counter-attack disguised as hurt feelings.</li>
        </ul>"""
    },
    37: {
        "title": "The Psychology of Overthinking: Why You Can't Sleep at Night",
        "category": "Anxiety & Stress",
        "desc": "Discover the neurological reasons your brain activates intrusive thoughts at 2 AM, and learn the therapist-approved technique to stop overthinking.",
        "content": """<h2>Introduction</h2>
        <p>It is 2 AM. You are physically exhausted, yet your brain has decided this is the perfect time to review an embarrassing conversation from five years ago or catastrophize about an upcoming meeting. If this sounds familiar, you are experiencing the deeply frustrating cycle of anxiety-driven overthinking.</p>
        <p>Psychologically, overthinking is actually a distorted attempt at problem-solving. When the lights go out and daily distractions disappear, your brain's Default Mode Network (DMN) takes over. Without immediate tasks to focus on, the brain scans for uncompleted loops and potential threats. For someone with anxiety, this ancient survival mechanism misfires, interpreting social worries as literal life-or-death threats.</p>
        <p>Fortunately, you are not at the mercy of your neurochemistry. By understanding the concept of 'Cognitive Defusion' and implementing specific bedtime wind-down routines, you can train your brain to release these mental loops and finally get the rest you deserve.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        <h2>Key Takeaways</h2>
        <ul>
            <li><strong>The Default Mode Network:</strong> Nighttime overthinking happens because the lack of external stimuli allows your brain's internal 'problem-finding' network to run wild.</li>
            <li><strong>Illusion of Control:</strong> Worrying feels productive, giving you a false sense of control over an unpredictable future.</li>
            <li><strong>Cognitive Defusion:</strong> Creating distance by saying 'I am having the thought that...' neutralizes the emotional impact of midnight anxiety.</li>
        </ul>"""
    },
    38: {
        "title": "Dopamine Detox: How to Reset Your Brain and Reignite Your Focus",
        "category": "Behavioral Psychology",
        "desc": "Constant scrolling has hijacked your brain's reward system. Learn the science of the dopamine detox and reclaim your ability to focus on hard tasks.",
        "content": """<h2>Introduction</h2>
        <p>If you find it impossible to read a book for ten minutes without reaching for your phone, you do not have a discipline problem—you have a neurochemical problem. We live in an attention economy designed by engineers to constantly hijack our brain's dopamine pathways through infinite scrolls, bright notifications, and instant gratification.</p>
        <p>Dopamine is not the 'pleasure' chemical; it is the 'motivation' chemical. It is the drive that makes you pursue a goal. When you flood your brain with cheap, effortless dopamine from social media, your baseline tolerance skyrockets. Suddenly, doing actual work, reading, or studying feels agonizingly boring because it cannot compete with the artificial spikes generated by your smartphone.</p>
        <p>The concept of a 'Dopamine Detox' involves intentionally depriving yourself of these cheap stimuli to let your neuroreceptors reset. By fasting from high-stimulation activities, you can lower your dopamine tolerance, making hard work and deep focus feel rewarding once again.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        <h2>Key Takeaways</h2>
        <ul>
            <li><strong>Dopamine is Motivation:</strong> It drives seeking behavior, not pleasure. Cheap dopamine hijacks your baseline, destroying your natural drive to work.</li>
            <li><strong>The Attention Economy:</strong> Apps are algorithmically engineered using variable reward schedules—the same psychology used in slot machines.</li>
            <li><strong>The Reset Protocol:</strong> A 24-hour fast from screens, sugar, and hyper-stimulating media can reset your receptor sensitivity, curing chronic procrastination.</li>
        </ul>"""
    }
}

# 1. Update the actual article pages
for art_id, data in new_articles.items():
    filepath = os.path.join(BASE_DIR, f"article{art_id}.html")
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Update title tags and meta
    html = re.sub(r'<title>.*?</title>', f'<title>{data["title"]} | Mind &amp; Balance</title>', html)
    html = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{data["desc"]}">', html)
    html = re.sub(r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{data["title"]} | Mind &amp; Balance">', html)
    html = re.sub(r'<meta property="og:description" content=".*?">', f'<meta property="og:description" content="{data["desc"]}">', html)
    html = re.sub(r'<meta name="twitter:title" content=".*?">', f'<meta name="twitter:title" content="{data["title"]} | Mind &amp; Balance">', html)
    
    # Update H1 and Category
    html = re.sub(r'<span class="card-category" style=".*?">.*?</span>', f'<span class="card-category" style="display:block; margin-bottom:1rem;">{data["category"]}</span>', html)
    html = re.sub(r'<h1 style=".*?">.*?</h1>', f'<h1 style="font-size: 3rem; max-width: 800px; margin: 0 auto;">{data["title"]}</h1>', html)
    
    # Update Body Content
    body_start = html.find('<main class="article-body hidden delay-2">') + len('<main class="article-body hidden delay-2">')
    body_end = html.find('</main>')
    
    new_html = html[:body_start] + "\n" + data["content"] + "\n        " + html[body_end:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_html)

# 2. Update index.html cards
with open(INDEX_PATH, 'r', encoding='utf-8') as f:
    idx_content = f.read()

for art_id, data in new_articles.items():
    # We need to find the specific card link `articleX.html` and replace its Category, Title, and Excerpt
    card_pattern = r'(<span class="card-category">)[^<]+(</span>\s*<h3 class="card-title">)[^<]+(</h3>\s*<p class="card-excerpt">)[^<]+(</p>\s*<a href="article' + str(art_id) + r'\.html")'
    replacement = r'\g<1>' + data["category"] + r'\g<2>' + data["title"] + r'\g<3>' + data["desc"] + r'\g<4>'
    idx_content = re.sub(card_pattern, replacement, idx_content)

with open(INDEX_PATH, 'w', encoding='utf-8') as f:
    f.write(idx_content)

print("SUCCESS: Articles rewritten with pure psychology content!")
