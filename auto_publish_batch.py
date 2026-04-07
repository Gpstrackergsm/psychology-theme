import os
import re
import datetime

BASE_DIR = "/Users/khalidaitelmaati/Desktop/scrapy-master/psychology-theme-main"
INDEX_PATH = os.path.join(BASE_DIR, "index.html")
SITEMAP_PATH = os.path.join(BASE_DIR, "sitemap.xml")

articles_batch = {
    42: {
        "title": "BPD or Bipolar? Understanding the Psychological Differences",
        "category": "Clinical Psychology",
        "desc": "Borderline Personality Disorder and Bipolar Disorder are frequently confused. Learn the critical neurological and behavioral differences.",
        "content": """<h2>Introduction</h2>
        <p>One of the most common misdiagnoses in modern clinical psychology involves confusing Borderline Personality Disorder (BPD) with Bipolar Disorder. Because both conditions feature intense mood swings and impulsive behavior, they can look identical to the untrained eye. However, the root causes, the duration of the mood swings, and the psychological triggers are completely different.</p>
        <p>Understanding these differences is crucial not just for clinicians, but for individuals trying to make sense of their own emotional turbulence. While Bipolar Disorder is primarily a mood disorder driven by neurochemical imbalances, BPD is a personality disorder deeply rooted in trauma and a profound fear of abandonment.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        
        <h2>The Core Difference: Triggers vs. Biology</h2>
        <p>The most defining difference between the two is the concept of <em>triggers</em>. In BPD, mood swings are intensely reactive to interpersonal events. A perceived slight, such as a friend taking too long to text back, can trigger a devastating depressive spiral or a bout of extreme anger within minutes. In Bipolar Disorder, episodes of mania or depression operate independently of the environment. A person can enter a manic episode even when their life is perfectly stable, and the episode might last for weeks or months, rather than shifting from hour to hour.</p>
        <p>Furthermore, BPD is characterized by an unstable sense of identity and chronic feelings of emptiness, whereas individuals with Bipolar generally maintain their core personality traits regardless of their fluctuating mood state.</p>
        
        <h2>Key Takeaways</h2>
        <ul>
            <li><strong>Duration of Swings:</strong> BPD mood swings happen rapidly (hours or days). Bipolar mood swings are sustained (weeks or months).</li>
            <li><strong>Interpersonal Sensitivity:</strong> BPD is heavily triggered by relationship dynamics and fears of abandonment.</li>
            <li><strong>Treatment Differences:</strong> Bipolar is primarily managed with mood-stabilizing medication, while BPD requires rigorous psychotherapy, notably Dialectical Behavior Therapy (DBT).</li>
        </ul>"""
    },
    43: {
        "title": "The Psychology of Imposter Syndrome: Why High Achievers Feel Like Frauds",
        "category": "Career Psychology",
        "desc": "Are you successful but secretly terrified someone will expose you as a fraud? Discover the psychological roots of Imposter Syndrome.",
        "content": """<h2>Introduction</h2>
        <p>You got the promotion, completed the degree, or launched the successful business. Yet, instead of feeling pride, you lie awake at night terrified that it was all a fluke, and that soon, everyone will discover you are a complete fraud. This is the hallmark of <strong>Imposter Syndrome</strong>.</p>
        <p>First identified by psychologists Pauline Clance and Suzanne Imes in the 1970s, Imposter Syndrome predominantly affects high-achieving individuals. Rather than internalizing their success as a result of their own competence, they attribute it to external factors like luck, timing, or simply "fooling" others.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        
        <h2>The Dunning-Kruger Effect vs. Imposter Syndrome</h2>
        <p>Imposter Syndrome is essentially the dark inverse of the Dunning-Kruger effect. While incompetent people often grossly overestimate their abilities because they lack the knowledge to recognize their errors, highly competent people underestimate their abilities because they assume that if something is easy for them, it must be easy for everyone else.</p>
        <p>This psychological blind spot prevents high achievers from accurately assessing their own expertise, leading to chronic anxiety and overworking as a defense mechanism to prevent being "found out."</p>
        
        <h2>Key Takeaways</h2>
        <ul>
            <li><strong>It Targets Competence:</strong> Feeling like an imposter is paradoxically one of the strongest indicators that you are actually highly competent.</li>
            <li><strong>The Attribution Error:</strong> Sufferers constantly attribute their failures internally ("I am bad at this") and their successes externally ("I just got lucky").</li>
            <li><strong>The Antidote:</strong> Documenting undeniable external evidence of your competence (metrics, glowing reviews, objective wins) helps logically rewire the feeling of fraudulence.</li>
        </ul>"""
    },
    44: {
        "title": "Trauma Bonding: The Neuroscience of Why We Can't Leave Bad Relationships",
        "category": "Relationships",
        "desc": "A trauma bond is not love; it is an addiction. Learn the chemical hooks that keep victims tied to abusive toxic partners.",
        "content": """<h2>Introduction</h2>
        <p>When someone remains in a deeply abusive or toxic relationship, outsiders often ask, "Why don't they just leave?" What classical societal views fail to understand is that the victim is not staying out of weakness or stupidity; they are staying because their brain has been hijack by a profound neurobiological addiction known as a <strong>Trauma Bond</strong>.</p>
        <p>A trauma bond occurs when an abuser cycles irregularly between extreme punishment (abuse, gaslighting, screaming) and extreme reward (apologies, affection, promises to change). This creates the most powerful reinforcement schedule in behavioral psychology.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        
        <h2>The Chemical Cocktail of Abuse</h2>
        <p>During the abusive phase, the victim's brain is flooded with high levels of cortisol and adrenaline. They are in a state of terror. When the abuser suddenly pivots to the "honeymoon" phase, offering comfort and love, the victim's brain unleashes a massive surge of dopamine and oxytocin.</p>
        <p>Because the relief from the terror came from the abuser themselves, the victim's brain begins to associate the abuser as the <em>only</em> source of safety. Over time, the victim develops a literal chemical dependency on this cycle, severely mirroring the neurobiology of heroin addiction.</p>
        
        <h2>Key Takeaways</h2>
        <ul>
            <li><strong>Intermittent Reinforcement:</strong> The unpredictable cycle of abuse and affection creates a stronger psychological bond than consistent love.</li>
            <li><strong>Chemical Addiction:</strong> A trauma bond is driven by extreme fluctuations in cortisol (stress) and dopamine (reward).</li>
            <li><strong>Leaving is Withdrawal:</strong> Breaking a trauma bond requires treating it like drug addiction rehabilitation, complete with strict No Contact and severe emotional withdrawal symptoms.</li>
        </ul>"""
    },
    45: {
        "title": "Gaslighting in the Workplace: Identifying the Subtle Signs of Professional Abuse",
        "category": "Career Psychology",
        "desc": "Gaslighting isn't just for romantic relationships. Learn how toxic managers use psychological warfare to manipulate you at work.",
        "content": """<h2>Introduction</h2>
        <p>While gaslighting is well-known in the context of romantic narcissism, it is equally prevalent and highly destructive in professional environments. Workplace gaslighting occurs when a toxic manager or coworker uses deliberate psychological manipulation to make you question your memory, competence, and sanity in order to maintain power and control over you.</p>
        <p>Because your livelihood depends on your job, the stakes in workplace gaslighting are incredibly high. It can lead to severe burnout, clinical depression, and a complete collapse of professional confidence.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        
        <h2>Common Tactics of the Corporate Gaslighter</h2>
        <p>A gaslighting boss might explicitly give you instructions in a meeting, only to aggressively reprimand you a week later for following them, claiming they "never said that." They might systematically exclude you from vital emails and then publicly criticize you for being "out of the loop."</p>
        <p>The goal is to keep you off-balance. When an employee is desperately trying to figure out what they did wrong, they are not asking raises, they are not seeking promotions elsewhere, and they are easily controlled.</p>
        
        <h2>Key Takeaways</h2>
        <ul>
            <li><strong>The "Memory" Game:</strong> The fundamental tactic of a gaslighter is confidently denying that events or conversations took place.</li>
            <li><strong>The Goal is Control:</strong> By dismantling your confidence, the toxic manager ensures you will not challenge their authority or outshine them.</li>
            <li><strong>The Solution is Documentation:</strong> The only way to survive workplace gaslighting is maintaining an aggressive paper trail. Get every verbal instruction confirmed via a follow-up email.</li>
        </ul>"""
    },
    46: {
        "title": "Somatic Experiencing: How Your Body Remembers Trauma When Your Mind Forgets",
        "category": "Trauma & PTSD",
        "desc": "Psychological trauma is not just a mental issue; it gets trapped in the nervous system. Discover the science of Somatic Experiencing.",
        "content": """<h2>Introduction</h2>
        <p>In his groundbreaking book, <em>The Body Keeps the Score</em>, Dr. Bessel van der Kolk revolutionized modern psychology by proving that trauma does not solely live as a memory in the brain; it physically anchors itself within the body's nervous system. When a person fails to process a traumatic event, the high survival energy generated in that moment (the fight-or-flight response) becomes chemically locked in their muscles, organs, and fascia.</p>
        <p>This is why talk therapy alone often fails to 'cure' severe PTSD. You cannot logically talk a nervous system out of believing it is under attack.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        
        <h2>Releasing the Trapped Energy</h2>
        <p>Somatic Experiencing (SE), developed by Dr. Peter Levine, is an alternative clinical therapy that focuses on the body's physical sensations rather than the narrative of the trauma. By slowly and safely guiding a patient to 'pendulate' between sensations of safety and sensations of distress, the nervous system is finally allowed to complete the fight-or-flight cycle that was interrupted during the traumatic event.</p>
        
        <h2>Key Takeaways</h2>
        <ul>
            <li><strong>Trauma is Physical:</strong> Symptoms like chronic pain, digestive issues, and muscle tension are often the direct physical manifestations of unprocessed psychological trauma.</li>
            <li><strong>Logic Fails Trauma:</strong> The amygdala (the brain's fear center) operates faster than the prefrontal cortex (logic center). You cannot rationalize away a somatic fear response.</li>
            <li><strong>Completing the Cycle:</strong> Somatic therapy allows the body to physically release the survival energy it held onto during the trauma, allowing the nervous system to finally return to baseline.</li>
        </ul>"""
    },
    47: {
        "title": "The Anxious Attachment Style: Why You Cling When You Feel Ignored",
        "category": "Relationships",
        "desc": "Are you terrified of abandonment? Anxious Attachment drives relationship anxiety. Learn where it comes from and how to heal it.",
        "content": """<h2>Introduction</h2>
        <p>If a delayed text message from your partner causes you to spiral into a state of severe panic, desperately trying to figure out what you did wrong and assuming the relationship is over, you are likely suffering from an <strong>Anxious Attachment Style</strong>.</p>
        <p>Attachment Theory, pioneered by John Bowlby, explains that our adult relationship patterns are entirely molded by the consistency of care we received as infants. Individuals with an anxious attachment style typically had caregivers who were inconsistent—sometimes deeply loving, but other times emotionally distant or unavailable. This inconsistency taught the child that love is terrifyingly conditional and can disappear at any moment.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        
        <h2>Protest Behaviors and The Anxious Cycle</h2>
        <p>When an anxiously attached person feels their partner pulling away, their nervous system registers it as a literal threat to their survival. To regain closeness, they engage in <em>Protest Behaviors</em>. This might look like calling ten times in a row, intentionally trying to make the partner jealous, or picking a fight just to force an emotional connection.</p>
        <p>Paradoxically, these clinging behaviors often push the partner further away, inadvertently fulfilling the exact abandonment the anxious person was terrified of.</p>
        
        <h2>Key Takeaways</h2>
        <ul>
            <li><strong>Rooted in Childhood:</strong> Anxious attachment stems from inconsistent caregiving, leading to an adult hyper-vigilance toward any signs of rejection.</li>
            <li><strong>Protest Behaviors:</strong> Acting out, over-communicating, and manipulative tests are desperate attempts to force reassurance from a pulling-away partner.</li>
            <li><strong>The Path to Secure:</strong> Healing requires deep self-soothing work, learning to emotionally regulate without requiring the partner to stabilize your mood.</li>
        </ul>"""
    },
    48: {
        "title": "The Avoidant Attachment Style: The Fear of Intimacy Explained",
        "category": "Relationships",
        "desc": "Why do some people pull away the moment a relationship gets serious? Discover the psychology of the Avoidant Attachment style.",
        "content": """<h2>Introduction</h2>
        <p>Have you ever dated someone who seemed incredibly invested in the relationship, but the absolute moment things got serious, they suddenly became cold, distant, and hyper-critical? They didn't lose feelings overnight; their psychological defense mechanisms were violently triggered. This is the hallmark of the <strong>Avoidant Attachment Style</strong>.</p>
        <p>Unlike the anxious attacher who fears abandonment, the avoidant attacher fears <em>engulfment</em>. Often raised by caregivers who were emotionally invasive, dismissive, or pushed independence far too early, the avoidant relies on extreme self-reliance. To an avoidant, intimacy equates to a loss of autonomy.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        
        <h2>Deactivation Strategies</h2>
        <p>When true intimacy looms, the avoidant's brain perceives it as a threat. They deploy <em>Deactivation Strategies</em> to subconsciously sabotage the connection and restore their comfort zone of isolation.</p>
        <p>These strategies include focusing obsessively on their partner's minor flaws (e.g., the way they chew), idealizing an ex-partner, or engaging in 'phantom ex' syndrome, where they convince themselves their true soulmate is still out there, giving them a psychological excuse to flee the current relationship.</p>
        
        <h2>Key Takeaways</h2>
        <ul>
            <li><strong>Fear of Engulfment:</strong> Avoidants equate emotional intimacy and vulnerability with a total loss of their freedom and self-determination.</li>
            <li><strong>Deactivation:</strong> They subconsciously search for minor flaws in their partner to justify pulling away when the connection deepens.</li>
            <li><strong>The Myth of the 'Loner':</strong> Avoidants still deeply desire connection, but their nervous system prevents them from safely embracing it without therapy.</li>
        </ul>"""
    },
    49: {
        "title": "High-Functioning Depression: The Invisible Weight of Smiling Through the Pain",
        "category": "Mental Health",
        "desc": "Depression doesn't always look like staying in bed all day. High-functioning depression hides behind success, perfectionism, and smiles.",
        "content": """<h2>Introduction</h2>
        <p>When society pictures clinical depression, the image is almost always the same: someone unable to get out of bed, weeping, neglecting their hygiene, and failing at work. But there is an entirely different presentation that is arguably more dangerous because it is completely invisible: <strong>High-Functioning Depression</strong>.</p>
        <p>Also known clinically as Dysthymia or Persistent Depressive Disorder (PDD), a person with high-functioning depression goes to work, hits the gym, raises their kids, and runs a successful business. To the outside world, they are thriving. But internally, every single action requires immense, exhausting psychological effort. The world has lost its color, and they are simply acting out the motions of living.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        
        <h2>The Danger of Hyper-Competence</h2>
        <p>Because they are highly competent, no one checks on them. Their success becomes their prison. When they finally do express feelings of emptiness, friends and family often dismiss it: "But you have such a great job! You have nothing to be depressed about!"</p>
        <p>This dismissal forces the individual to suppress their pain even deeper, relying on toxic perfectionism to prove their worth, eventually leading to catastrophic burnout or acute suicidal ideation that shocks everyone around them.</p>
        
        <h2>Key Takeaways</h2>
        <ul>
            <li><strong>The Exhaustion of Faking It:</strong> People with high-functioning depression spend massive amounts of energy acting "normal", leaving them with nothing at the end of the day.</li>
            <li><strong>The Mask of Perfectionism:</strong> Success is often used as a desperate coping mechanism to outrun the internal feelings of worthlessness.</li>
            <li><strong>It Is Clinically Valid:</strong> Just because you can get out of bed does not mean you do not deserve and require clinical intervention and therapy.</li>
        </ul>"""
    },
    50: {
        "title": "Emotional Dysregulation: When Every Feeling is a Category 5 Hurricane",
        "category": "Behavioral Psychology",
        "desc": "Do minor inconveniences make you want to break things? Learn about emotional dysregulation and how to rebuild your psychological brakes.",
        "content": """<h2>Introduction</h2>
        <p>Imagine driving a sports car that has a 500-horsepower engine but absolutely no brakes. This is what it is like to live with <strong>Emotional Dysregulation</strong>. It is the inability to manage, process, and control the intensity of your emotional responses to environmental stimuli.</p>
        <p>For someone with emotional dysregulation—common in ADHD, Autism, BPD, and C-PTSD—a minor frustration like spilling coffee doesn't just cause a flash of annoyance; it registers in the brain as a catastrophic event, triggering an immediate, violent surge of rage or collapsing despair.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        
        <h2>The Neurobiology of the 'Overreaction'</h2>
        <p>In a neurotypical brain, the amygdala (the emotional alarm system) fires, but the prefrontal cortex (the logical manager) quickly steps in to say, "Calm down, it's just spilled coffee." In a dysregulated brain, the connection between the prefrontal cortex and the amygdala is severely compromised.</p>
        <p>The alarm rings indefinitely, and the person completely loses access to logic until the neurochemical storm physically exhausts itself. People who suffer from this are often deeply ashamed of their "overreactions" and suffer immense guilt once logic returns.</p>
        
        <h2>Key Takeaways</h2>
        <ul>
            <li><strong>It is Biological, Not Behavioral:</strong> Emotional dysregulation is a failure of the brain's "brakes" (the prefrontal cortex), not an intentional adult temper tantrum.</li>
            <li><strong>The Shame Spiral:</strong> The violent emotional outburst is almost always followed by crippling guilt and shame, further damaging self-esteem.</li>
            <li><strong>Dialectical Behavior Therapy (DBT):</strong> DBT is explicitly designed to teach the brain the 'distress tolerance' skills required to physically rebuild the neurological brakes.</li>
        </ul>"""
    },
    51: {
        "title": "Toxic Positivity: Why Forced Optimism is Actually Emotional Abuse",
        "category": "Mental Health",
        "desc": "Telling someone to 'just look on the bright side' during a tragedy isn't helpful; it's deeply invalidating. Explore the harm of Toxic Positivity.",
        "content": """<h2>Introduction</h2>
        <p>"Everything happens for a reason!" "Just think good thoughts!" "Others have it worse." We see these quotes plastered across social media and printed on throw pillows, framed as ultimate wisdom. But in reality, when deployed during moments of genuine human suffering, these phrases are the core weapons of <strong>Toxic Positivity</strong>.</p>
        <p>Toxic positivity is the belief that no matter how dire or tragic a situation is, people should maintain a positive mindset. While optimism is generally healthy, forcing it unconditionally results in the denial, minimization, and invalidation of authentic human emotional experience.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        
        <h2>The Psychological Harm of Invalidation</h2>
        <p>When you tell someone who is going through a horrific divorce or a devastating loss to "just look on the bright side," you are not comforting them. You are psychologically shutting them down. You are sending the message that their pain is unacceptable and makes you uncomfortable.</p>
        <p>This forces the grieving person to suppress their negative emotions to accommodate your comfort. Suppressed negative emotions do not disappear; they manifest internally as cortisol spikes, anxiety, depression, and severe isolation. True psychological resilience comes from acknowledging pain, not pretending it doesn't exist.</p>
        
        <h2>Key Takeaways</h2>
        <ul>
            <li><strong>Invalidation of Reality:</strong> Toxic positivity gaslights the sufferer into believing their completely valid negative emotions are 'wrong'.</li>
            <li><strong>It is About the Listener's Comfort:</strong> People often use toxic positivity because they lack the emotional maturity to sit in discomfort with a grieving friend.</li>
            <li><strong>Tragic Empathy:</strong> True support sounds like: "This is deeply unfair, and it makes total sense that you are furious right now. I am here with you."</li>
        </ul>"""
    },
    52: {
        "title": "The Dark Triad: Identifying the Most Dangerous Personalities in Psychology",
        "category": "Behavioral Psychology",
        "desc": "Narcissism, Machiavellianism, and Psychopathy. Understand the 'Dark Triad' to protect yourself from malevolent social predators.",
        "content": """<h2>Introduction</h2>
        <p>Not everyone you meet has good intentions. While humanistic psychology focuses heavily on growth, empathy, and healing, forensic and behavioral psychology deal with the grim reality of malevolent personalities. The apex of this research is a framework known as the <strong>Dark Triad</strong>.</p>
        <p>The Dark Triad consists of three distinct but overlapping personality traits: Narcissism, Machiavellianism, and Psychopathy. Individuals who score high on these traits are socially destructive, deeply manipulative, and fundamentally lack the capacity for genuine human empathy. They view other people not as human beings, but as chess pieces to be used for their own advancement or amusement.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        
        <h2>Breaking Down the Triad</h2>
        <p><strong>1. Narcissism:</strong> Characterized by extreme grandiosity, an insatiable need for admiration, and a deeply internalized belief that they are fundamentally superior to the rest of the human race.<br>
        <strong>2. Machiavellianism:</strong> Named after the political philosopher, this trait embodies cold, calculating manipulation. They are strategic, cynical, and believe that the end always justifies the means.<br>
        <strong>3. Psychopathy:</strong> The most dangerous of the three traits. Characterized by high impulsivity, thrill-seeking behavior, and an absolute zero-point of empathy or remorse for the pain they inflict on others.</p>
        
        <h2>Key Takeaways</h2>
        <ul>
            <li><strong>The Illusion of Charm:</strong> Dark Triad individuals are universally highly charming and charismatic upon first meeting. They use charm as a weapon to disarm victims.</li>
            <li><strong>Exploitative Nature:</strong> They are drawn to positions of power—corporate leadership, politics, and finance—where their ruthlessness is often rewarded rather than punished.</li>
            <li><strong>Unchangeable:</strong> Attempting to "fix" or love a Dark Triad individual into empathy is impossible and highly dangerous; the only clinical recommendation is total avoidance.</li>
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
    <meta property="og:image" content="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&q=80&w=1200">
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
                <span>•</span><span>{date_str}</span><span>•</span><span>5 min read</span>
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
    
    for art_id, data in articles_batch.items():
        html_content = generate_article_html(art_id, data)
        filepath = os.path.join(BASE_DIR, f"article{art_id}.html")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"Created {filepath}")
        
        # Build Card
        new_cards_html += f"""
            <article class="card hidden delay-1">
                <div class="card-img" style="background-image: url('https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&q=80&w=400');"></div>
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
            print("✅ Updated index.html with 11 new articles.")
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
