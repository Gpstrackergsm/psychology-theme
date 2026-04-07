import os
import re
import datetime

BASE_DIR = "/Users/khalidaitelmaati/Desktop/scrapy-master/psychology-theme-main"
INDEX_PATH = os.path.join(BASE_DIR, "index.html")
SITEMAP_PATH = os.path.join(BASE_DIR, "sitemap.xml")

batch_2_articles = {
    66: {
        "title": "ADHD in Adults: Hidden Symptoms You Might Be Overlooking",
        "category": "Neurodiversity",
        "desc": "ADHD isn't just for kids. Discover how adult ADHD manifests as 'Executive Dysfunction' and chronic overwhelm.",
        "content": """<h2>Introduction</h2>
        <p>For decades, Attention Deficit Hyperactivity Disorder (ADHD) was viewed almost exclusively as a childhood condition characterized by "bouncing off the walls." But as our understanding of neurodiversity has evolved, we have realized that ADHD doesn't disappear in adulthood—it simply changes its mask.</p>
        <p>Adult ADHD rarely looks like physical hyperactivity. Instead, it manifests as <strong>Internal Restlessness</strong> and <strong>Executive Dysfunction</strong>. It is the person who has five half-finished projects, the one who constantly loses their keys, and the one who feels a crushing weight of "paralysis" when faced with a simple task like checking the mail. Understanding adult ADHD is the first step toward self-compassion and effective management.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        
        <h2>The Curse of 'Executive Dysfunction'</h2>
        <p>People with ADHD don't have a lack of willpower; they have a lack of dopamine regulation in the prefrontal cortex—the part of the brain responsible for planning and initiation. This leads to "ADHD Paralysis," where you know exactly what you need to do, but your brain physically cannot send the signal to start. It feels like trying to drive a car with no transmission. You're revving the engine (thinking about the task), but the wheels aren't turning.</p>
        
        <h2>Emotional Dysregulation in Adults</h2>
        <p>Recent research highlights that emotional sensitivity is a core component of adult ADHD. This often looks like "Rejection Sensitive Dysphoria" (RSD), where a minor criticism feels like a devastating personal attack. Because the ADHD brain has trouble filtering stimuli, emotions hit harder and faster than they do for neurotypical individuals.</p>

        <section class="faq-section" style="margin-top: 4rem; border-top: 1px solid rgba(0,0,0,0.1); padding-top: 2rem;">
            <h2 style="margin-bottom: 2rem;">Frequently Asked Questions</h2>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.2rem; color: var(--primary-color); margin-bottom: 0.5rem;">Can you develop ADHD as an adult?</h3>
                <p>Clinically, ADHD must be present in childhood to be diagnosed as an adult, but many people are highly intelligent and "mask" their symptoms until the complexities of adult life (jobs, bills, kids) make the coping mechanisms fail.</p>
            </div>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.2rem; color: var(--primary-color); margin-bottom: 0.5rem;">Is adult ADHD just being lazy?</h3>
                <p>No. ADHD is a structural and neurochemical difference in the brain. "Laziness" is a choice; ADHD is a physiological struggle with task initiation and focus.</p>
            </div>
        </section>""",
        "faq": [
            {"q": "What are the common signs of ADHD in adults?", "a": "Chronic procrastination, forgetfulness, internal restlessness, and difficulty with emotional regulation."},
            {"q": "What is executive dysfunction?", "a": "A struggle with the mental processes that enable us to plan, focus attention, and juggle multiple tasks."}
        ]
    },
    67: {
        "title": "Understanding Quiet BPD: The Internalized Struggle",
        "category": "Mental Health",
        "desc": "Borderline Personality Disorder isn't always explosive. Quiet BPD involves a hidden, internal storm of self-hatred and fear.",
        "content": """<h2>Introduction</h2>
        <p>In the public imagination, Borderline Personality Disorder (BPD) is often associated with explosive anger, outward volatility, and unstable relationships. But there is a large subset of the BPD population that never shows their rage to the world. They suffer from <strong>Quiet BPD</strong>, also known as "Discouraged BPD."</p>
        <p>Instead of lashing out at others, individuals with Quiet BPD lash in. They turn their intense emotional pain, fear of abandonment, and identity confusion against themselves. To the outside world, they may appear calm, high-achieving, and deeply empathetic, but internally, they are living through a "Category 5 hurricane" of self-destructive thoughts and emotional agony.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        
        <h2>The Internalized Storm</h2>
        <p>Because their struggle is invisible, people with Quiet BPD often go undiagnosed for years. They are the "oversharers" who suddenly go silent, the people who disappear from relationships because they are terrified of being rejected first, and the ones who feel a crushing sense of guilt for even existing. Their primary defense mechanism is "Splitting" against themselves—seeing themselves as fundamentally "evil" or "broken" the moment they make a mistake.</p>
        
        <h2>The Path to Healing</h2>
        <p>Dialectical Behavior Therapy (DBT) is the gold standard for Quiet BPD. It teaches the skills of emotional regulation and Distress Tolerance, helping the individual realize that their feelings are valid but their self-hatred is a distorted trauma response. Healing involves learning to be as kind to oneself as one is to others.</p>

        <section class="faq-section" style="margin-top: 4rem; border-top: 1px solid rgba(0,0,0,0.1); padding-top: 2rem;">
            <h2 style="margin-bottom: 2rem;">Frequently Asked Questions</h2>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.2rem; color: var(--primary-color); margin-bottom: 0.5rem;">How is Quiet BPD different from regular BPD?</h3>
                <p>The core symptoms are the same, but the "direction" of the arousal is different. Regular BPD is externalized (anger at others); Quiet BPD is internalized (shame and anger at the self).</p>
            </div>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.2rem; color: var(--primary-color); margin-bottom: 0.5rem;">Can Quiet BPD be cured?</h3>
                <p>While BPD is a personality structure, it is highly treatable. With consistent therapy like DBT, individuals can reach a state of "remission" where they no longer meet the clinical criteria for the disorder.</p>
            </div>
        </section>""",
        "faq": [
            {"q": "What is Quiet BPD?", "a": "A subtype of BPD where intense emotions and fears are internalized rather than expressed outwardly."},
            {"q": "Can Quiet BPD be diagnosed easily?", "a": "No, because the symptoms are hidden, it is often misdiagnosed as purely depression or anxiety."}
        ]
    },
    68: {
        "title": "How to Stop a Panic Attack: The 5-4-3-2-1 Grounding Method",
        "category": "Mental Health hacks",
        "desc": "Panic attacks feel like a heart attack. Learn the grounding technique that manually overrides your brain's fear circuit.",
        "content": """<h2>Introduction</h2>
        <p>If you have ever experienced a panic attack, you know the absolute terror of feeling like you are dying, having a heart attack, or losing your mind. Your heart races, your breath shortens, and your brain screams that you are in mortal danger. In that moment, logic is useless because the "thinking" part of your brain has been shut down by the amygdala.</p>
        <p>The only way to stop a panic attack is to use a <strong>Grounding Technique</strong> that manually forces your brain back into the present moment. The most effective tool ever developed for this is the 5-4-3-2-1 method.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        
        <h2>How the 5-4-3-2-1 Method Works</h2>
        <p>This technique works by engaging all five of your senses to pull your focus away from the internal panic and back to the physical world:</p>
        <ul>
            <li><strong>5 THINGS YOU CAN SEE:</strong> Look around and name five distinct objects. A blue pen, a leaf, a coffee mug, etc.</li>
            <li><strong>4 THINGS YOU CAN TOUCH:</strong> Feel the texture of your shirt, the coldness of a table, the weight of your shoes.</li>
            <li><strong>3 THINGS YOU CAN HEAR:</strong> Listen for distant traffic, a ticking clock, or the hum of a refrigerator.</li>
            <li><strong>2 THINGS YOU CAN SMELL:</strong> The scent of your skin, the air, or a nearby candle.</li>
            <li><strong>1 THING YOU CAN TASTE:</strong> The lingering taste of coffee or just the inside of your mouth.</li>
        </ul>
        
        <h2>The Science of Grounding</h2>
        <p>By forcing your brain to process sensory data, you are manually activating the prefrontal cortex. This sends a signal down to the amygdala that "The environment is safe. There is no predator here." It is the biological "off-switch" for the fight-or-flight response.</p>

        <section class="faq-section" style="margin-top: 4rem; border-top: 1px solid rgba(0,0,0,0.1); padding-top: 2rem;">
            <h2 style="margin-bottom: 2rem;">Frequently Asked Questions</h2>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.2rem; color: var(--primary-color); margin-bottom: 0.5rem;">Can a panic attack actually kill me?</h3>
                <p>No. While it feels physically devastating, a panic attack is not dangerous. It is simply a false alarm in your survival system.</p>
            </div>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.2rem; color: var(--primary-color); margin-bottom: 0.5rem;">How long does a panic attack typical last?</h3>
                <p>Most panic attacks peak within 10 minutes and subside within 20 to 30 minutes, though the physical exhaustion can last for hours.</p>
            </div>
        </section>""",
        "faq": [
            {"q": "What is the 5-4-3-2-1 grounding method?", "a": "A sensory engagement technique used to stop panic attacks by pulling focus back to the physical environment."},
            {"q": "Why does grounding work?", "a": "It manually activates the logical part of the brain, overriding the emotional fight-or-flight response."}
        ]
    },
    69: {
        "title": "The Gut-Brain Axis: How Your Diet Determines Your Mood",
        "category": "Mental Health",
        "desc": "Did you know 95% of your serotonin is produced in your gut? Discover the revolutionary link between digestion and anxiety.",
        "content": """<h2>Introduction</h2>
        <p>We often talk about mental health as if it is "all in your head." But modern neuroscience is discovering that most of your mental health is actually in your <strong>gut</strong>. The "Gut-Brain Axis" is a two-way communication highway between your gastrointestinal tract and your central nervous system, and it is the most exciting frontier in psychology today.</p>
        <p>The gut is often called the "second brain" because it contains its own nervous system—the enteric nervous system—and produces a massive amount of the neurotransmitters responsible for your mood, including 95% of your body's serotonin and 50% of your dopamine.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        
        <h2>Microbes and Mood</h2>
        <p>The trillions of bacteria living in your gut (the microbiome) aren't just there to digest fiber; they are chemical factories that produce metabolites that directly travel through the Vagus Nerve to your brain. Research shows that "Dysbiosis"—an imbalance of bad bacteria—is a primary driver of chronic anxiety and clinical depression.</p>
        
        <h2>The Psychobiotics Revolution</h2>
        <p>We are now entering the era of "Psychobiotics," where doctors may soon prescribe specific probiotic strains to treat mental illness alongside traditional therapy. Eating fermented foods (Kimchi, Kefir, Sauerkraut) and reducing ultra-processed sugar is no longer just about physical fitness; it is a direct intervention for psychological resilience.</p>

        <section class="faq-section" style="margin-top: 4rem; border-top: 1px solid rgba(0,0,0,0.1); padding-top: 2rem;">
            <h2 style="margin-bottom: 2rem;">Frequently Asked Questions</h2>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.2rem; color: var(--primary-color); margin-bottom: 0.5rem;">Can a bad diet cause anxiety?</h3>
                <p>Yes. Diets high in processed sugar and low in fiber cause inflammation in the gut, which signals the brain to increase cortisol production, leading to chronic anxiety.</p>
            </div>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.2rem; color: var(--primary-color); margin-bottom: 0.5rem;">What are the best foods for mental health?</h3>
                <p>Fermented foods (for probiotics), leafy greens (for folate), and fatty fish (for Omega-3s) are the "Big Three" for a healthy gut-brain connection.</p>
            </div>
        </section>""",
        "faq": [
            {"q": "What is the gut-brain axis?", "a": "The bidirectional communication network between the gastrointestinal system and the brain."},
            {"q": "Does serotonin come from the gut?", "a": "Yes, approximately 95% of the body's serotonin is produced in the gut by specialized cells and bacteria."}
        ]
    },
    70: {
        "title": "Seasonal Affective Disorder: More Than Just 'Winter Blues'",
        "category": "Mental Health",
        "desc": "Why do we feel depressed when the sun goes down? Discover the science of Seasonal Affective Disorder (SAD).",
        "content": """<h2>Introduction</h2>
        <p>Every year, as the days get shorter and the temperature drops, millions of people feel a heavy blanket of lethargy and sadness descend upon them. Many dismiss it as the "winter blues," but for about 5% of the population, it is a clinical condition known as <strong>Seasonal Affective Disorder (SAD)</strong>.</p>
        <p>SAD is not just about being sad because it's cold. It is a biological response to the lack of sunlight that disrupts your internal clock (circadian rhythm) and causes your brain to overproduce melatonin while underproducing serotonin.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        
        <h2>The Biology of Winter Depression</h2>
        <p>Sunlight is a trigger for the brain to stop producing melatonin (the sleep hormone) and start producing serotonin (the mood-lifting hormone). When the winter sunlight is too weak or too rare, the brain remains in a "sleep state" all day. This leads to the hallmark symptoms of SAD: excessive sleeping, carbohydrate cravings, and a total loss of interest in social activities.</p>
        
        <h2>Light Therapy: The First Line of Defense</h2>
        <p>The most effective treatment for SAD is "Phototherapy"—using a 10,000-lux light box for 30 minutes every morning. This mimics the intensity of outdoor sunlight and tricks the brain into resetting its circadian rhythm, effectively "waking up" the neurotransmitters responsible for happiness.</p>

        <section class="faq-section" style="margin-top: 4rem; border-top: 1px solid rgba(0,0,0,0.1); padding-top: 2rem;">
            <h2 style="margin-bottom: 2rem;">Frequently Asked Questions</h2>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.2rem; color: var(--primary-color); margin-bottom: 0.5rem;">Can you get SAD in the summer?</h3>
                <p>Yes. A rare form of "Summer-onset SAD" exists, often driven by excessive heat and high humidity which irritates the nervous system, but winter-onset is much more common.</p>
            </div>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.2rem; color: var(--primary-color); margin-bottom: 0.5rem;">Is Vitamin D helpful for SAD?</h3>
                <p>Vitamin D is crucial for serotonin production. Because we get less Vitamin D from the sun in winter, supplementation is almost always recommended for those with SAD.</p>
            </div>
        </section>""",
        "faq": [
            {"q": "What is Seasonal Affective Disorder?", "a": "A type of depression that occurs during specific seasons, most commonly when sunlight levels drop in winter."},
            {"q": "What is the best treatment for SAD?", "a": "Light therapy using a high-intensity lamp (10,000 lux) and Vitamin D supplementation are highly effective."}
        ]
    },
    71: {
        "title": "OCD Myths vs. Reality: It's Not Just About Cleaning",
        "category": "Behavioral Psychology",
        "desc": "Many people say 'I'm so OCD' because they like order. But real Obsessive-Compulsive Disorder is a living nightmare. Learn the truth.",
        "content": """<h2>Introduction</h2>
        <p>"I'm so OCD!" is a phrase we hear all the time to describe someone who likes a clean desk or a color-coded closet. But in the world of clinical psychology, this casual use of the term is deeply problematic. <strong>Obsessive-Compulsive Disorder (OCD)</strong> is not a quirk or a preference for neatness; it is a debilitating, chronic mental health condition that can completely paralyze a person's life.</p>
        <p>OCD is characterized by a "broken alarm system" in the brain. It is the presence of intrusive, distressing thoughts (Obsessions) and the temporary, ritualistic behaviors used to quiet them (Compulsions).</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        
        <h2>The Intrusive Thought Cycle</h2>
        <p>The "O" in OCD represents thoughts that the person *doesn't* want to have. These aren't just "worries." They are terrifying mental images of harm, contamination, or catastrophic failure. To get rid of the anxiety caused by these thoughts, the person engages in a "Compulsion." This might be hand-washing, but it could also be repeating a certain phrase in their head, checking the stove 50 times, or seeking constant reassurance from others.</p>
        
        <h2>ERP: The Gold Standard Therapy</h2>
        <p>Traditional talk therapy can actually make OCD worse. The correct treatment is "Exposure and Response Prevention" (ERP). This involves gradually exposing the patient to their fear (the obsession) and strictly preventing them from performing the compulsion. This retrains the brain's alarm system, proving that the catastrophe will not happen even if the ritual is ignored.</p>

        <section class="faq-section" style="margin-top: 4rem; border-top: 1px solid rgba(0,0,0,0.1); padding-top: 2rem;">
            <h2 style="margin-bottom: 2rem;">Frequently Asked Questions</h2>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.2rem; color: var(--primary-color); margin-bottom: 0.5rem;">What is 'Pure O' OCD?</h3>
                <p>Pure Obsessional OCD is a form where the compulsions are entirely mental. The person doesn't show outward behaviors, but they spend hours "ruminating" or checking their thoughts internally.</p>
            </div>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.2rem; color: var(--primary-color); margin-bottom: 0.5rem;">Can you grow out of OCD?</h3>
                <p>OCD is typically a chronic condition, but with proper ERP therapy and sometimes medication, victims can achieve a high level of functioning where the symptoms become negligible.</p>
            </div>
        </section>""",
        "faq": [
            {"q": "What is the primary symptom of OCD?", "a": "Distressing intrusive thoughts (obsessions) followed by repetitive behaviors (compulsions) to relieve the anxiety."},
            {"q": "Does OCD always involve cleaning?", "a": "No, OCD manifests in many forms, including obsessions about harm, morality, order, and symmetry."}
        ]
    },
    72: {
        "title": "Social Anxiety: How to Stop Fearing the Judgment of Others",
        "category": "Behavioral Psychology",
        "desc": "Social anxiety isn't just 'being shy.' Learn why your brain sees a dinner party as a survival threat and how to fix it.",
        "content": """<h2>Introduction</h2>
        <p>Almost everyone feels nervous before a big speech or a first date. But for someone with <strong>Social Anxiety Disorder</strong>, the fear isn't just about "performance." It is a fundamental, paralyzing fear of being humiliated, rejected, or scrutinized in every everyday social situation—from ordering coffee to answering a phone call.</p>
        <p>Social anxiety is driven by a "hyper-vigilant" amygdala that views other human beings not as friends, but as potential predators who will judge and cast you out of the tribe. In our evolutionary past, being cast out meant death, which is why social anxiety feels like a survival threat today.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        
        <h2>The Spotlight Effect</h2>
        <p>The core of social anxiety is a psychological bias called the "Spotlight Effect"—the belief that everyone is noticing your every move and mistake. In reality, everyone else is just as worried about *their* spotlight! Breaking social anxiety requires the "Outward Focus" technique: training your brain to observe the environment and the other person instead of obsessively monitoring your own heart rate or mistakes.</p>
        
        <h2>Social Skills vs. Social Confidence</h2>
        <p>Most socially anxious people actually have great social skills! The problem isn't that they don't know *what* to say; it's that the sheer intensity of their anxiety blocks their ability to say it. Recovery involves "Exposure Therapy"—purposefully putting yourself in slightly uncomfortable social situations to prove to your brain that the "catastrophe" of judgment rarely happens.</p>

        <section class="faq-section" style="margin-top: 4rem; border-top: 1px solid rgba(0,0,0,0.1); padding-top: 2rem;">
            <h2 style="margin-bottom: 2rem;">Frequently Asked Questions</h2>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.2rem; color: var(--primary-color); margin-bottom: 0.5rem;">Is social anxiety just shyness?</h3>
                <p>No. Shyness is a personality trait. Social anxiety is a clinical disorder that actively interferes with your ability to work, study, and form relationships.</p>
            </div>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.2rem; color: var(--primary-color); margin-bottom: 0.5rem;">Can social anxiety go away on its own?</h3>
                <p>Without treatment, social anxiety tends to persist and can lead to severe isolation. Cognitive Behavioral Therapy (CBT) is highly successful in resolving it.</p>
            </div>
        </section>""",
        "faq": [
            {"q": "What triggers social anxiety?", "a": "Situations where an individual feels they might be scrutinized, judged, or humiliated by others."},
            {"q": "What is the spotlight effect?", "a": "The psychological tendency to overestimate how much others notice and judge our appearance and actions."}
        ]
    },
    73: {
        "title": "The Psychology of Self-Harm: Understanding the Pain You Hidden",
        "category": "Clinical Psychology",
        "desc": "Self-harm is often misunderstood as a suicide attempt. In reality, it is a desperate coping mechanism for emotional numbness.",
        "content": """<h2>Introduction</h2>
        <p>Self-harm is one of the most stigmatized topics in mental health. Many assume it is a "cry for attention" or a failed suicide attempt. But in the world of clinical psychology, self-harm is understood as a <strong>Malformed Coping Mechanism</strong>. It is a way for individuals to manage overwhelming emotional pain that they don't have the tools to express verbally.</p>
        <p>For most, self-harm is not about wanting to die—it is a desperate attempt to feel *something* other than emotional numbness, or to turn an invisible internal agony into a visible external wound that they can actually "care for."</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        
        <h2>The Neurobiology of the Relief</h2>
        <p>When someone self-harms, the body responds to the physical injury by releasing a massive flood of Endorphins—the brain's natural painkillers. This causes a temporary, intense "high" and a feeling of calm. This chemical relief is addictive, creating a feedback loop where the person begins to rely on physical pain to silence emotional distress.</p>
        
        <h2>Finding Healthy Alternatives</h2>
        <p>Recovery from self-harm involves learning "Replacement Behaviors" that provide a similar sensory shock without the damage. This might include holding an ice cube until it melts, snapping a rubber band on the wrist, or listening to loud, aggressive music. Ultimately, the goal is to address the underlying trauma that makes the emotional pain feel so unmanageable.</p>

        <section class="faq-section" style="margin-top: 4rem; border-top: 1px solid rgba(0,0,0,0.1); padding-top: 2rem;">
            <h2 style="margin-bottom: 2rem;">Frequently Asked Questions</h2>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.2rem; color: var(--primary-color); margin-bottom: 0.5rem;">Is self-harm a sign of BPD?</h3>
                <p>It is a common symptom of Borderline Personality Disorder, but it also occurs in severe depression, PTSD, and eating disorders. It is a symptom of intense emotional dysregulation.</p>
            </div>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.2rem; color: var(--primary-color); margin-bottom: 0.5rem;">How do I help someone who self-harms?</h3>
                <p>The first step is non-judgmental empathy. Telling them to "just stop" is ineffective and shaming. Encourage professional therapy like DBT which is specifically designed for self-harm recovery.</p>
            </div>
        </section>""",
        "faq": [
            {"q": "Why do people self-harm?", "a": "As a coping mechanism to manage overwhelming emotional pain, numbness, or internal distress."},
            {"q": "Is self-harm always a suicide attempt?", "a": "No, for many, it is a survival tactic to cope with unbearable feelings, not an attempt to end their life."}
        ]
    },
    74: {
        "title": "Sleep Deprivation and Mental Health: The Dangerous Cycle",
        "category": "Mental Health",
        "desc": "Losing an hour of sleep doesn't just make you tired; it turns your brain into a factory of anxiety and paranoia.",
        "content": """<h2>Introduction</h2>
        <p>We live in a culture that prizes "the grind," often at the expense of sleep. But in the world of neuropsychology, sleep deprivation is considered a state of <strong>Acute Cognitive Impairment</strong>. Losing just one or two hours of sleep per night has a more profound impact on your mental health than almost any other lifestyle factor.</p>
        <p>Sleep is when the brain's "glymphatic system" flushes out the toxic proteins built up during the day. When you don't sleep, those toxins remain, leading to brain fog, extreme irritability, and a total collapse of emotional regulation.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        
        <h2>The Amygdala on No Sleep</h2>
        <p>Research using fMRI scans shows that when humans are sleep-deprived, the amygdala—the brain's emotional center—is 60% more reactive to negative stimuli. If your boss gives you a minor correction on a full night's sleep, you handle it. On 4 hours of sleep, your brain perceives that same correction as an existential threat, triggering intense rage or tears.</p>
        
        <h2>The Link to Paranoia and Psychosis</h2>
        <p>Prolonged sleep deprivation (more than 48 hours) can lead to auditory hallucinations and paranoid delusions that are indistinguishable from clinical schizophrenia. This proves that sleep is not a luxury; it is the fundamental "safety system" that keeps your brain anchored to reality.</p>

        <section class="faq-section" style="margin-top: 4rem; border-top: 1px solid rgba(0,0,0,0.1); padding-top: 2rem;">
            <h2 style="margin-bottom: 2rem;">Frequently Asked Questions</h2>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.2rem; color: var(--primary-color); margin-bottom: 0.5rem;">Can sleep deprivation cause permanent brain damage?</h3>
                <p>Chronic sleep deprivation is linked to a higher risk of Alzheimer’s and cognitive decline, but for most people, the immediate psychological symptoms resolve after a few nights of restorative sleep.</p>
            </div>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.2rem; color: var(--primary-color); margin-bottom: 0.5rem;">How many hours are actually necessary?</h3>
                <p>While individuals vary, the vast majority of humans require 7 to 9 hours for the glymphatic flush and emotional processing to complete.</p>
            </div>
        </section>""",
        "faq": [
            {"q": "How does sleep affect mental health?", "a": "Sleep deprivation increases amygdala reactivity, making emotions harder to regulate and increasing anxiety and irritability."},
            {"q": "What is the glymphatic system?", "a": "The brain's waste clearance system that actively flushes toxins during deep sleep."}
        ]
    },
    75: {
        "title": "The Power of Mindfulness: Rewiring Your Brain for Peace",
        "category": "Mental Health hacks",
        "desc": "Mindfulness isn't just for monks. It's a proven neuroplasticity tool to shrink your brain's fear center. Learn how.",
        "content": """<h2>Introduction</h2>
        <p>The term "Mindfulness" has reached buzzword status, often associated with expensive yoga retreats and incense. But beneath the marketing is a profound, clinically proven tool for <strong>Neuroplasticity</strong>. Mindfulness is simply the practice of observing the present moment—and your own thoughts—without judgment.</p>
        <p>By training your brain to be an "observer" rather than a "participant" in your anxious thoughts, you can physically change the structure of your brain. Frequent mindfulness practice has been proven to shrink the gray matter in the amygdala (the fear center) while thickening the prefrontal cortex (the logic center).</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        
        <h2>The "Observer" Effect</h2>
        <p>Most of us believe we *are* our thoughts. If we have an anxious thought ("What if I fail?"), we treat it as an emergency. Mindfulness teaches you to see the thought as a "passing cloud." You think, "Ah, there's a failed-based thought." By creating this small gap of distance, you prevent the physiological stress response from ever even starting.</p>
        
        <h2>8 Weeks to a New Brain</h2>
        <p>The famous Harvard study on MBSR (Mindfulness-Based Stress Reduction) showed that just 8 weeks of 20-minute daily practice resulted in permanent, measurable changes to brain density. It is the most effective drug-free intervention for chronic stress ever discovered.</p>

        <section class="faq-section" style="margin-top: 4rem; border-top: 1px solid rgba(0,0,0,0.1); padding-top: 2rem;">
            <h2 style="margin-bottom: 2rem;">Frequently Asked Questions</h2>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.2rem; color: var(--primary-color); margin-bottom: 0.5rem;">I can't clear my mind, so I fail at mindfulness. What now?</h3>
                <p>The goal of mindfulness is NOT to clear your mind—it is impossible. The goal is to notice when your mind has wandered and gently bring it back. Every time you notice you're distracted, that's a "mental rep" that builds brain muscle.</p>
            </div>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.2rem; color: var(--primary-color); margin-bottom: 0.5rem;">How many minutes a day do I need to meditate?</h3>
                <p>Research suggests that 10 to 12 minutes of consistent, daily practice is the "tipping point" for structural brain changes to begin.</p>
            </div>
        </section>""",
        "faq": [
            {"q": "What is mindfulness?", "a": "The practice of non-judgmental awareness of the present moment."},
            {"q": "How does mindfulness change the brain?", "a": "It shrinks the amygdala (fear center) and strengthens the prefrontal cortex (logic center)."}
        ]
    },
    76: {
        "title": "Flow State Productivity: The Psychology of 'The Zone'",
        "category": "Behavioral Psychology",
        "desc": "Have you ever lost track of time while working? You were in a Flow State. Learn how to trigger it on command.",
        "content": """<h2>Introduction</h2>
        <p>We have all had those rare moments where we are so focused on a task that everything else disappears. The hours fly by like minutes, your self-consciousness vanishes, and your performance reaches its absolute peak. In psychology, this is called a <strong>Flow State</strong>, popularized by researcher Mihaly Csikszentmihalyi. It is considered the "Optimal Human Experience."</p>
        <p>Flow is not a mystical occurrence; it is a specific state of deep neurochemistry where the brain shuts down the "inner critic Cog" (the prefrontal cortex) to allow for rapid-fire processing and total immersion.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        
        <h2>The Conditions for Flow</h2>
        <p>A flow state doesn't happen by accident. It requires a specific formula: the <strong>Challenge-Skill Balance</strong>. If a task is too easy, you are bored. If it is too hard, you are anxious. Flow occurs in the "sweet spot" where the difficulty slightly exceeds your current skills, forcing you to stretch without breaking.</p>
        
        <h2>Flow Triggers in the Modern World</h2>
        <p>The biggest enemy of flow is distraction. Every time your phone pings, your brain is yanked out of its deep focus, and it can take up to 20 minutes to re-enter a true flow state. To trigger flow, you must have "Deep Work" blocks of uninterrupted time, a clear and immediate goal, and rapid feedback on your performance.</p>

        <section class="faq-section" style="margin-top: 4rem; border-top: 1px solid rgba(0,0,0,0.1); padding-top: 2rem;">
            <h2 style="margin-bottom: 2rem;">Frequently Asked Questions</h2>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.2rem; color: var(--primary-color); margin-bottom: 0.5rem;">Why is flow so rare in the office?</h3>
                <p>Offices are designed for shallow work (emails, meetings, interruptions). Flow requires deep, singular focus which is the opposite of the modern corporate environment.</p>
            </div>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.2rem; color: var(--primary-color); margin-bottom: 0.5rem;">Does flow state make you tired?</h3>
                <p>Surprisingly, no. Flow is a high-dopamine state that often leaves you feeling energized and deeply satisfied, even after intense mental labor.</p>
            </div>
        </section>""",
        "faq": [
            {"q": "What is a flow state?", "a": "A mental state of complete immersion and peak performance in an activity."},
            {"q": "How can I get into a flow state?", "a": "By balancing the challenge of a task with your skill level and eliminating all external distractions."}
        ]
    },
    77: {
        "title": "Growth vs. Fixed Mindset: The Key to Professional Resilience",
        "category": "Behavioral Psychology",
        "desc": "Is intelligence a gift or a muscle? Discover why your mindset determines how far you can go in life.",
        "content": """<h2>Introduction</h2>
        <p>Why do some people crumble after a single failure, while others use that same failure as fuel to become even better? According to Stanford psychologist Carol Dweck, the difference is entirely in your <strong>Mindset</strong>. You either have a Fixed Mindset or a Growth Mindset.</p>
        <p>A "Fixed Mindset" is the belief that your intelligence, personality, and talents are static—you are born with a certain amount and that's it. A "Growth Mindset" is the belief that these traits are muscles that can be developed through hard work, strategy, and persistence. This simple shift in belief changes how you view every challenge in your life.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        
        <h2>The Danger of Being "Smart"</h2>
        <p>Paradoxically, being told you are "naturally smart" as a child often leads to a fixed mindset. You begin to fear challenges because if you struggle, it means you "aren't smart anymore." People with growth mindsets don't fear failure; they fear stagnation. They view a difficult problem not as a test of their worth, but as an opportunity to upgrade their brain.</p>
        
        <h2>Rewiring for Growth</h2>
        <p>The most powerful word in the Growth Mindset is "Yet." Instead of saying "I can't do this," you say "I can't do this *yet*." This tiny linguistic shift keeps the brain in an "active learning" state, significantly increasing neuroplasticity and the speed of skill acquisition.</p>

        <section class="faq-section" style="margin-top: 4rem; border-top: 1px solid rgba(0,0,0,0.1); padding-top: 2rem;">
            <h2 style="margin-bottom: 2rem;">Frequently Asked Questions</h2>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.2rem; color: var(--primary-color); margin-bottom: 0.5rem;">Can a fixed mindset be changed?</h3>
                <p>Yes. Awareness is the first step. By consciously noticing when you are avoiding a challenge out of "fear of looking stupid", you can choose to lean in instead.</p>
            </div>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.2rem; color: var(--primary-color); margin-bottom: 0.5rem;">Which mindset is better for leaders?</h3>
                <p>Growth mindset leaders build more innovative teams because they encourage experimentation and view "errors" as vital data points rather than personal failings.</p>
            </div>
        </section>""",
        "faq": [
            {"q": "What is a growth mindset?", "a": "The belief that abilities and intelligence can be developed through effort and learning."},
            {"q": "What is the difference between a fixed and growth mindset?", "a": "A fixed mindset sees talent as innate; a growth mindset sees it as something to be earned through practice."}
        ]
    }
}

def generate_article_html(art_id, data):
    date_str = datetime.datetime.now().strftime("%B %d, %Y")
    title = data["title"]
    desc = data["desc"]
    cat = data["category"]
    content = data["content"]
    
    # FAQ Schema
    schema_items = []
    for item in data['faq']:
        schema_items.append(f"""{{
      "@type": "Question",
      "name": "{item['q']}",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "{item['a']}"
      }}
    }}""")
    joined_items = ",".join(schema_items)
    faq_schema = f"""
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [{joined_items}]
    }}
    </script>
    """

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
    {faq_schema}
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
    
    for art_id, data in batch_2_articles.items():
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
        new_sitemap_xml += f"""    <url>\n        <loc>https://leafanoo.com/article{art_id}.html</loc>\n        <changefreq>monthly</changefreq>\n        <priority>0.8</priority>\n    </url>\n"""

    # 1. Inject cards into index.html
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
            print("✅ Updated index.html with Batch 2.")
    except Exception as e:
        print("Error index.html", e)

    # 2. Inject priority into sitemap.xml
    with open(SITEMAP_PATH, 'r', encoding='utf-8') as f:
        sitemap = f.read()
    sitemap = sitemap.replace('</urlset>', f'{new_sitemap_xml}</urlset>')
    with open(SITEMAP_PATH, 'w', encoding='utf-8') as f:
        f.write(sitemap)
    print("✅ Updated sitemap.xml")

if __name__ == "__main__":
    main()
