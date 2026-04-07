import os
import re
import datetime

BASE_DIR = "/Users/khalidaitelmaati/Desktop/scrapy-master/psychology-theme-main"
INDEX_PATH = os.path.join(BASE_DIR, "index.html")
SITEMAP_PATH = os.path.join(BASE_DIR, "sitemap.xml")

batch_5_articles = {
    101: {
        "title": "The Science Behind How We Discover Hidden Brain Switch That Tells You to Stop Eating: A Psychological Perspective",
        "category": "Neuroscience",
        "desc": "Your brain's 'stop eating' signal may come from an unexpected source. Discover how astrocytes control appetite.",
        "content": """<h2>Introduction</h2>
        <p>For decades, we believed that appetite was almost exclusively controlled by specialized neurons in the hypothalamus. But a groundbreaking study has revealed a hidden player in the obesity epidemic: <strong>Astrocytes</strong>. These star-shaped cells, once thought to be simple "support cells," actually act as a critical "brain switch" that tells you when to put down the fork.</p>
        <p>Researchers have discovered that after a meal, glucose triggers specific cells called tanycytes, which then send signals to these astrocytes. The astrocytes, in turn, activate the neurons that produce the sensation of fullness. This discovery explains why some individuals never feel "full"—their brain switch might be stuck.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        
        <h2>The Astrocyte Revolution</h2>
        <p>This "Astrocyte Switch" represents a massive shift in how we view metabolic disorders. If the astrocytes are non-responsive, the neurons that signal satiety never get the message, even if the stomach is full. This creates a biological loop of overeating that has nothing to do with willpower and everything to do with neurochemistry.</p>
        
        <h2>Future Treatments</h2>
        <p>By targeting the astrocytes directly, scientists believe they can develop new treatments for obesity and eating disorders that work by "resetting" this fullness switch, finally giving hope to those struggling with chronic overeating.</p>

        <section class="faq-section" style="margin-top: 4rem; border-top: 1px solid rgba(0,0,0,0.1); padding-top: 2rem;">
            <h2 style="margin-bottom: 2rem;">Frequently Asked Questions</h2>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.2rem; color: var(--primary-color); margin-bottom: 0.5rem;">What are astrocytes?</h3>
                <p>Astrocytes are star-shaped glial cells in the brain that were traditionally thought to only provide structural support to neurons, but are now known to actively control brain signaling.</p>
            </div>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.2rem; color: var(--primary-color); margin-bottom: 0.5rem;">Can I fix my appetite switch naturally?</h3>
                <p>While research is ongoing, stabilizing blood sugar through high-fiber diets and consistent sleep is the best way to help tanycytes and astrocytes function correctly.</p>
            </div>
        </section>""",
        "faq": [
            {"q": "What is the hidden brain switch for appetite?", "a": "A network of astrocytes that receive signals from tanycytes to activate fullness neurons."},
            {"q": "How does glucose affect this switch?", "a": "Glucose triggers the cells to send a 'satisfied' signal to the brain's satiety center."}
        ]
    },
    102: {
        "title": "How The Science Behind How We Found a Protein That Drives Brain Aging: A Psychological Perspective",
        "category": "Neuroscience",
        "desc": "Scientists have uncovered a protein called FTL1 that may be the key to brain aging and memory decline.",
        "content": """<h2>Introduction</h2>
        <p>What if "getting old" isn't a natural decay, but a specific protein gone rogue? Scientists have recently pinpointed a single protein, <strong>FTL1</strong>, as a primary driver of brain aging and the cognitive decline that comes with it. This protein appears to build up in the aging brain, effectively "clogging" the communication lines between neurons.</p>
        <p>In high-profile mouse studies, elevated FTL1 levels led to weakened neural connections and severe memory loss. However, when researchers intervened and reduced this protein, the results were staggering—the brain's cognitive function actually began to rejuvenate.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        
        <h2>FTL1 and the 'Memory Clog'</h2>
        <p>The FTL1 protein affects the brain's plasticity—its ability to form new connections. As it accumulates, the prefrontal cortex becomes less flexible, making it harder to learn new things or recall old ones. It's the biological equivalent of a computer's processor being slowed down by excessive heat.</p>
        
        <h2>The End of Alzheimer's?</h2>
        <p>While it's too early to call this a cure for Alzheimer's, the discovery of FTL1 gives researchers a clear "target." By developing drugs that can safely flush this protein from the human brain, we may be able to significantly delay or even reverse the symptoms of dementia.</p>

        <section class="faq-section" style="margin-top: 4rem; border-top: 1px solid rgba(0,0,0,0.1); padding-top: 2rem;">
            <h2 style="margin-bottom: 2rem;">Frequently Asked Questions</h2>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.2rem; color: var(--primary-color); margin-bottom: 0.5rem;">What is the FTL1 protein?</h3>
                <p>FTL1 is a ferritin light chain protein that helps manage iron but can become toxic to brain connections when it builds up excessively with age.</p>
            </div>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.2rem; color: var(--primary-color); margin-bottom: 0.5rem;">Can exercise reduce FTL1?</h3>
                <p>Early data suggests that cardiovascular health helps the brain's waste-clearance system (the glymphatic system) move out toxic proteins, though specific FTL1 research is pending.</p>
            </div>
        </section>""",
        "faq": [
            {"q": "What causes brain aging?", "a": "The accumulation of specific proteins like FTL1 which disrupt communication between neurons."},
            {"q": "Is brain aging reversible?", "a": "New research suggests that by reducing specific aging proteins, some cognitive function can be restored."}
        ]
    },
    103: {
        "title": "Why Your Brain Does This: These Overlooked Brain Cells May Control Fear and PTSD",
        "category": "Mental Health",
        "desc": "Astrocytes are now revealed to be key players in fear memory and PTSD. Learn how they interact with neurons.",
        "content": """<h2>Introduction</h2>
        <p>If you suffer from PTSD or chronic anxiety, you know how a single smell or sound can trigger a full-body fear response years after the event. We've always blamed "malfunctioning neurons" for this. But new research shows that <strong>Astrocytes</strong>—the brain's long-ignored "support staff"—are actually the ones holding onto the keys of fear memories.</p>
        <p>Astrocytes don't just sit there; they actively help form, recall, and even weaken fear responses in real-time. By interacting with neurons at the synapse, they determine just how "loud" a fear memory should be heard.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        
        <h2>The Biology of Fear</h2>
        <p>When you experience a trauma, astrocytes in the amygdala become hyper-active. They effectively "lock" the fear memory into place. In patients with PTSD, these astrocytes remain in a state of high arousal, keeping the trauma as fresh as the day it happened. This is why tradition talk therapy often fails; the problem is at a cellular, non-neuronal level.</p>
        
        <h2>New Hope for Treatment</h2>
        <p>By discovering the role of astrocytes in fear, we open a new door for medication. Instead of just numbing the brain with antidepressants, we may soon have treatments that specifically target astrocyte activity to "soften" traumatic memories without erasing them.</p>

        <section class="faq-section" style="margin-top: 4rem; border-top: 1px solid rgba(0,0,0,0.1); padding-top: 2rem;">
            <h2 style="margin-bottom: 2rem;">Frequently Asked Questions</h2>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.2rem; color: var(--primary-color); margin-bottom: 0.5rem;">Do astrocytes store memories?</h3>
                <p>While neurons are the primary storage, astrocytes act as 'modulators' that control how accessible and intense those memories are.</p>
            </div>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.2rem; color: var(--primary-color); margin-bottom: 0.5rem;">How can I calm my astrocytes?</h3>
                <p>Vagus nerve stimulation and deep breathing exercises have been shown to lower generalized brain inflammation, which helps calm glial cell activity.</p>
            </div>
        </section>""",
        "faq": [
            {"q": "What is the role of astrocytes in PTSD?", "a": "They modulate the intensity of fear memories by interacting with neurons during the recall process."},
            {"q": "Can astrocytes be targeted for therapy?", "a": "Yes, pharmaceutical companies are researching glial-specific drugs to treat refractory anxiety disorders."}
        ]
    },
    104: {
        "title": "What A Gene Mutation May Trap the Brain in the Wrong Reality in Schizophrenia Patients Reveals About Our Behavior",
        "category": "Clinical Psychology",
        "desc": "A newly identified mutation explains why some patients struggle to update their understanding of reality.",
        "content": """<h2>Introduction</h2>
        <p>One of the most heart-breaking aspects of schizophrenia is the "loss of reality"—when a patient holds onto a delusion even in the face of overwhelming evidence. For a long time, we thought this was a failure of logic. But a new study suggests it's actually about a <strong>Gene Mutation</strong> that physically traps the brain in a static version of reality.</p>
        <p>This mutation disrupts a specific brain circuit involved in "flexible decision-making." In simple terms, it breaks the hardware that allows us to say, "The world has changed, so my belief must change too."</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        
        <h2>The 'Reality Update' Glitch</h2>
        <p>Most of our brains are constantly updating. If we see a "Wet Paint" sign, we update our reality and don't touch the wall. In patients with this specific mutation, the signal that "things are different" never reaches the decision-making center. They stay stuck in an outdated choice, which in humans manifests as a persistent delusion.</p>
        
        <h2>Implications for Psychosis</h2>
        <p>This research proves that many symptoms of psychosis are not "imaginary"—they are the result of a physical disconnect in the brain's update system. This shift from "mental failing" to "mechanical failure" is helping reduce the stigma around severe mental illness.</p>

        <section class="faq-section" style="margin-top: 4rem; border-top: 1px solid rgba(0,0,0,0.1); padding-top: 2rem;">
            <h2 style="margin-bottom: 2rem;">Frequently Asked Questions</h2>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.2rem; color: var(--primary-color); margin-bottom: 0.5rem;">Can everyone get this mutation?</h3>
                <p>No, this is a specific genetic marker found in a subset of the population with a family history of schizophrenic disorders.</p>
            </div>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.2rem; color: var(--primary-color); margin-bottom: 0.5rem;">Does this mean medicine can fix delusions?</h3>
                <p>By understanding the specific circuit that is broken, scientists can develop more targeted drugs that help "force" the reality update system back online.</p>
            </div>
        </section>""",
        "faq": [
            {"q": "What causes delusions in schizophrenia?", "a": "A genetic mutation that disrupts the brain's ability to update its understanding of current reality."},
            {"q": "What is flexible decision-making?", "a": "The cognitive ability to adjust behavior and beliefs based on new information from the environment."}
        ]
    },
    105: {
        "title": "A Therapist's View on: The Science Behind How We Discover Sleep Switch That Builds Muscle, Burns Fat, and Boosts Brainpower",
        "category": "Behavioral Psychology",
        "desc": "Deep sleep activates a system that controls growth hormone, fueling muscle strength and metabolism.",
        "content": """<h2>Introduction</h2>
        <p>We've always known that sleep is "good for you." But what if I told you there is a literal <strong>Sleep Switch</strong> in your brain that determines whether you build muscle or store fat? Groundbreaking research has mapped the exact neural circuit that triggers the release of Growth Hormone during deep sleep.</p>
        <p>This switch is the master controller for your metabolism, your muscle recovery, and even your cognitive processing speed. When you flip this switch through high-quality REM and Deep Sleep, you are effectively "upgrading" your body while you dream.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        
        <h2>The Growth Hormone Connection</h2>
        <p>90% of your daily Growth Hormone is released while you are in Stage 3 sleep. If your sleep is fragmented or short, the "switch" never fully flips. This leads to muscle wasting, weight gain around the midsection, and a foggy brain. It's the reason why athletes and high-performers treat sleep as their #1 performance-enhancing tool.</p>
        
        <h2>How to Flip the Switch</h2>
        <p>Your sleep switch is extremely sensitive to light and temperature. To ensure it flips correctly, you need a room at 65°F (18°C) and absolute darkness. Magnesium supplementation has also been shown to help "prime" this neural circuit for activation.</p>

        <section class="faq-section" style="margin-top: 4rem; border-top: 1px solid rgba(0,0,0,0.1); padding-top: 2rem;">
            <h2 style="margin-bottom: 2rem;">Frequently Asked Questions</h2>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.1rem; color: var(--primary-color); margin-bottom: 0.5rem;">How many hours to trigger the switch?</h3>
                <p>It's not just hours, it's cycles. Most people need uninterrupted blocks of at least 90 minutes to reach the deep sleep required for growth hormone release.</p>
            </div>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.1rem; color: var(--primary-color); margin-bottom: 0.5rem;">Does coffee interefere with the switch?</h3>
                <p>Yes. Caffeine blocks the adenosine receptors that help the brain flip the sleep switch, meaning you stay in 'shallow' sleep all night.</p>
            </div>
        </section>""",
        "faq": [
            {"q": "What is the brain's sleep switch?", "a": "A group of neurons in the hypothalamus that regulate the transition to deep, restorative sleep."},
            {"q": "Does deep sleep burn fat?", "a": "Yes, by triggering the release of growth hormone which facilitates fat metabolism and muscle repair."}
        ]
    },
    106: {
        "title": "The Hidden Connection Between What Teens Eat Could Be Affecting Their Mental Health More Than We Thought and Your Mind",
        "category": "Behavioral Psychology",
        "desc": "A new review of 20 studies finds a direct link between teen diet and symptoms of depression and anxiety.",
        "content": """<h2>Introduction</h2>
        <p>The "teenagers love junk food" stereotype is a staple of modern life. But a massive review of twenty separate studies has revealed that this diet is doing more than just causing breakouts—it is directly fueling the **Mental Health Crisis** in adolescents. What a teen eats today determines how they feel tomorrow.</p>
        <p>The research found a startlingly clear correlation: the higher the intake of ultra-processed foods, the higher the rates of depressive symptoms and anxiety disorders. The teen brain is still "under construction," and it is literally built out of the nutrients it consumes.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        
        <h2>The Inflammation Link</h2>
        <p>Processed sugars and fats trigger "Systemic Inflammation" in the body. In a growing brain, this inflammation irritates the neural circuits responsible for emotional regulation. This is why a "cranky" teen might actually be a brain-inflamed teen. By switching to a whole-food diet, researchers saw marked improvements in mood stability within weeks.</p>
        
        <h2>The 'Nutrient Gap'</h2>
        <p>Teens need massive amounts of Omega-3s and B-Vitamins for healthy brain development. When these are replaced by "empty" calories, the brain's survival system enters a state of panic, leading to the hallmark symptoms of generalized anxiety and lack of motivation.</p>

        <section class="faq-section" style="margin-top: 4rem; border-top: 1px solid rgba(0,0,0,0.1); padding-top: 2rem;">
            <h2 style="margin-bottom: 2rem;">Frequently Asked Questions</h2>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.1rem; color: var(--primary-color); margin-bottom: 0.5rem;">Can a diet cure depression?</h3>
                <p>While not a replacement for therapy, 'Nutritional Psychiatry' is now considered a vital first-line treatment for managing mood disorders in young people.</p>
            </div>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.1rem; color: var(--primary-color); margin-bottom: 0.5rem;">What is the best 'brain food' for teens?</h3>
                <p>Fatty fish, walnuts, avocados, and leafy greens provide the raw materials needed for structural brain maintenance and serotonin production.</p>
            </div>
        </section>""",
        "faq": [
            {"q": "Does diet affect teen mental health?", "a": "Yes, high intake of processed foods is significantly linked to increased depression and anxiety in adolescents."},
            {"q": "What is nutritional psychiatry?", "a": "A medical field that uses dietary interventions to treat and prevent mental health conditions."}
        ]
    },
    107: {
        "title": "Inside Stroke Triggers a Hidden Brain Change That Looks Like Rejuvenation: What the Brain Tells Us",
        "category": "Neuroscience",
        "desc": "Remarkable brain scans show that after a stroke, the unaffected side of the brain can actually look 'younger'.",
        "content": """<h2>Introduction</h2>
        <p>A stroke is usually seen as a devastating end to brain vitality. But researchers analyzing over 500 brain scans have found something that defies logic: while the damaged side of the brain ages rapidly, the **unaffected side** can actually undergo a "hidden rejuvenation."</p>
        <p>This biological "Refresh" happens as the brain enters a state of hyper-plasticity to compensate for the lost function. It's as if the brain realizes it's in an emergency and switches on an ancient "repair mode" that normally stays dormant in adults.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        
        <h2>The 'Plasticity Burst'</h2>
        <p>In the months following a stroke, the healthy hemisphere begins to mimic the neural density of a younger brain. It forms new connections at a rate usually only seen in children. This "Burst" is what allows stroke survivors to learn how to walk or speak again, proving that the brain's ability to rewire itself is much stronger than we previously believed.</p>
        
        <h2>Unlocking the Signal</h2>
        <p>Now, scientists are trying to figure out the exact chemical "signal" that triggers this rejuvenation. If we can activate this repair mode *without* needing a stroke to trigger it, we may have found the holy grail of anti-aging for the human mind.</p>

        <section class="faq-section" style="margin-top: 4rem; border-top: 1px solid rgba(0,0,0,0.1); padding-top: 2rem;">
            <h2 style="margin-bottom: 2rem;">Frequently Asked Questions</h2>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.1rem; color: var(--primary-color); margin-bottom: 0.5rem;">What is brain plasticity?</h3>
                <p>The ability of the brain to change its structure and function in response to experience or injury.</p>
            </div>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.1rem; color: var(--primary-color); margin-bottom: 0.5rem;">Can a healthy brain rejuvenate?</h3>
                <p>Yes, through intense learning of new skills (like a language or instrument), you can trigger similar, though less intense, 'youthful' changes in your neural density.</p>
            </div>
        </section>""",
        "faq": [
            {"q": "Can a brain look younger after a stroke?", "a": "Yes, the healthy hemisphere often exhibits increased neural density and plasticity as it compensates for the damaged side."},
            {"q": "How long does post-stroke plasticity last?", "a": "The 'peak' window for rejuvenation is typically 3-6 months after the event, but plasticity continues for life."}
        ]
    },
    108: {
        "title": "The Hidden Connection Between Metformin’s Hidden Brain Pathway Revealed After 60 Years and Your Mind",
        "category": "Behavioral Psychology",
        "desc": "The world's most popular diabetes drug works in the brain, not just the body. Discover how it controls sugar through neurons.",
        "content": """<h2>Introduction</h2>
        <p>Metformin has been the "Gold Standard" for diabetes for over sixty years. We always thought it worked by simply making the liver and muscles more sensitive to insulin. But a massive discovery has revealed its **Hidden Brain Pathway**. It turns out that much of Metformin's power comes from switching off a specific protein in the brain and activating specialized "Sugar-Sensing" neurons.</p>
        <p>This discovery proves that blood sugar is not just a metabolic issue—it is a neurological one. Your brain is the "Thermostat" that regulates your energy, and Metformin is one of the few tools that can reach in and adjust the dial.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        
        <h2>The 'Thermostat' neurons</h2>
        <p>By activating neurons in the hypothalamus, Metformin signals the body to lower glucose levels from the "top down." This explains why the drug has such profound impacts on other brain-related conditions, including a reduced risk of dementia and a stabilizing effect on mood in some patients. It's essentially "cleaning up" the brain's energy signaling.</p>
        
        <h2>A New Frontier for Brain Health</h2>
        <p>We are now exploring Metformin as a "Geroprotector"—a drug that protects against aging. By stabilizing the brain's metabolic pathways, it may prevent the "Neuro-inflammation" that leads to cognitive decline and depression in our later years.</p>

        <section class="faq-section" style="margin-top: 4rem; border-top: 1px solid rgba(0,0,0,0.1); padding-top: 2rem;">
            <h2 style="margin-bottom: 2rem;">Frequently Asked Questions</h2>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.1rem; color: var(--primary-color); margin-bottom: 0.5rem;">Does Metformin affect mood?</h3>
                <p>Because it regulates glucose signaling in the brain's hypothalamus, many patients report more stable energy and fewer 'sugar-related' mood swings.</p>
            </div>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.1rem; color: var(--primary-color); margin-bottom: 0.5rem;">Is diabetes a brain disease?</h3>
                <p>New evidence suggests that 'Type 3 Diabetes' is a real condition where the brain becomes insulin-resistant, leading to Alzheimer's symptoms.</p>
            </div>
        </section>""",
        "faq": [
            {"q": "How does Metformin affect the brain?", "a": "It activates specific neurons in the hypothalamus that help regulate blood sugar through the central nervous system."},
            {"q": "Why was this discovery important?", "a": "It reveals that metabolic health is deeply tied to brain-cell signaling, not just physical organs like the liver."}
        ]
    },
    109: {
        "title": "Mental Health Break: Fathers Face Rising Depression Risk a Year After Baby Arrives",
        "category": "Relationships",
        "desc": "Postpartum depression isn't just for moms. New research finds a delayed risk for fathers that often goes unnoticed.",
        "content": """<h2>Introduction</h2>
        <p>We've spent decades rightfully focusing on postpartum depression in mothers. But a sweeping study of new parents has found a **Staggering Silent Crisis**: new fathers are actually *more* at risk for depression and anxiety exactly one year after the baby arrives. While they often stay stable during the initial "survival mode" of the first few months, the emotional toll hits them with a delay.</p>
        <p>Because we don't expect it, fathers often suffer in silence, dismissing their fatigue and irritability as "just part of being a dad." In reality, they are facing a clinical shift in their role and their neurochemistry.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        
        <h2>The 'Fatherhood Hormonal Shift'</h2>
        <p>Research shows that men's testosterone levels actually drop when they become fathers, while their prolactin and oxytocin levels rise. This "sobering" of the male system is designed to make them better caregivers, but for some, the drop in testosterone leads to clinical depression and a loss of identity.</p>
        
        <h2>The One-Year Wall</h2>
        <p>By the one-year mark, the community support for new parents usually disappears. The father is often back at work, dealing with sleep deprivation, financial stress, and a changed relationship with his partner. This is when the "Wall" is hit. Recognizing this delayed risk is the first step toward better family health.</p>

        <section class="faq-section" style="margin-top: 4rem; border-top: 1px solid rgba(0,0,0,0.1); padding-top: 2rem;">
            <h2 style="margin-bottom: 2rem;">Frequently Asked Questions</h2>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.1rem; color: var(--primary-color); margin-bottom: 0.5rem;">Do men get postpartum depression?</h3>
                <p>Yes, 'Paternal Postpartum Depression' affects about 10% of new fathers, and the symptoms are often different than in women (more anger and avoidance).</p>
            </div>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.1rem; color: var(--primary-color); margin-bottom: 0.5rem;">How can fathers prevent burnout?</h3>
                <p>By prioritizing 'Micro-Rest' and maintaining social connections with other fathers to normalize the struggle of new parenthood.</p>
            </div>
        </section>""",
        "faq": [
            {"q": "When is the highest risk of depression for new fathers?", "a": "About one year after the birth of their child, rather than the initial few months."},
            {"q": "What are the symptoms of paternal depression?", "a": "Irritability, withdrawal from family, increased work hours, and chronic fatigue."}
        ]
    },
    110: {
        "title": "Inside Weight Loss Drug Ozempic Cuts Depression, Anxiety, and Addiction Risk: What the Brain Tells Us",
        "category": "Behavioral Psychology",
        "desc": "GLP-1 drugs like Ozempic are showing massive benefits for mental health, reducing psychiatric hospital visits.",
        "content": """<h2>Introduction</h2>
        <p>Ozempic and Wegovy are famous for taking over Hollywood and the fitness world. But their most profound impact might not be on the waistline—it might be on the **Brain**. A massive study found that people on GLP-1 medications saw significant drops in depression, generalized anxiety, and even substance use disorders.</p>
        <p>This "Hidden Side Effect" is turning the world of psychiatry upside down. We are realizing that the same hormones that control hunger also control the "Reward Circuit" that drives addiction and the "Dread Circuit" that causes anxiety.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        
        <h2>Rewiring the Craving Center</h2>
        <p>GLP-1 receptors are found throughout the brain's reward centers. By stabilizing these receptors, Ozempic doesn't just stop the craving for food; it stops the craving for alcohol, nicotine, and even obsessive online shopping. It's effectively giving the "Logical Brain" back the remote control over impulsive urges.</p>
        
        <h2>A Future in Psychiatry?</h2>
        <p>We are already seeing the first clinical trials for using Ozempic as a primary treatment for Binge Eating Disorder and Alcoholism. For many, the weight loss is just the beginning; the real prize is the newfound mental "Quiet" they experience for the first time in their lives.</p>

        <section class="faq-section" style="margin-top: 4rem; border-top: 1px solid rgba(0,0,0,0.1); padding-top: 2rem;">
            <h2 style="margin-bottom: 2rem;">Frequently Asked Questions</h2>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.1rem; color: var(--primary-color); margin-bottom: 0.5rem;">Can Ozempic cause depression in some people?</h3>
                <p>Early reports suggested a risk, but large-scale data actually shows the opposite for the majority of users—a significant improvement in overall mood and stability.</p>
            </div>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.1rem; color: var(--primary-color); margin-bottom: 0.5rem;">How long for mental health effects to start?</h3>
                <p>Most patients report a reduction in 'food noise' and anxiety within the first two weeks of reaching their effective dose.</p>
            </div>
        </section>""",
        "faq": [
            {"q": "Does Ozempic help with anxiety?", "a": "New research shows a significant reduction in anxiety and depression symptoms for many users of GLP-1 medications."},
            {"q": "What is 'Food Noise'?", "a": "The constant intrusive thoughts about eating that many people find is silenced when using GLP-1 drugs."}
        ]
    },
    111: {
        "title": "Mental Health Break: Huge Study Finds No Evidence Cannabis Helps Anxiety, Depression, or PTSD",
        "category": "Behavioral Psychology",
        "desc": "The largest review to date finds that cannabis doesn't actually treat mental health—it might make it worse.",
        "content": """<h2>Introduction</h2>
        <p>In the "Green Revolution," millions of people have turned to cannabis to treat their "Sunday Scaries," their chronic depression, or their trauma. But the **Largest Scientific Review to Date** has delivered a sobering verdict: there is zero evidence that cannabis effectively treats anxiety, depression, or PTSD.</p>
        <p>In fact, for many, the drug was found to be a "False Friend"—providing a temporary feeling of calm while actually increasing the risk of psychosis, social withdrawal, and long-term addiction. It's the psychological equivalent of putting a band-aid on a broken leg.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        
        <h2>The 'Numbing' Fallacy</h2>
        <p>Cannabis works by slowing down the central nervous system. This feels like relief, but it is actually **Avoidance**. Because the brain never learns how to process the anxiety, the anxiety grows stronger in the background. When the drug wears off, the "Rebound Effect" often makes the original mental health symptoms even more severe.</p>
        
        <h2>Delayed Recovery</h2>
        <p>The most dangerous part of using cannabis for mental health is the "Delay of Care." People wait years to seek proven therapies like CBT or EMDR because they think the cannabis is "managing" the problem. This delays true healing and allows the mental health condition to become chronic and harder to treat.</p>

        <section class="faq-section" style="margin-top: 4rem; border-top: 1px solid rgba(0,0,0,0.1); padding-top: 2rem;">
            <h2 style="margin-bottom: 2rem;">Frequently Asked Questions</h2>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.1rem; color: var(--primary-color); margin-bottom: 0.5rem;">Why do people think it helps?</h3>
                <p>Because it provides immediate sensory distraction and can help with 'falling' asleep, though it significantly reduces the quality of that sleep (REM suppression).</p>
            </div>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.1rem; color: var(--primary-color); margin-bottom: 0.5rem;">Is CBD different than THC?</h3>
                <p>Yes. CBD shows more promise for physical inflammation, but the high-dose 'Street THC' used by most self-medicating patients is what carries the psychiatric risk.</p>
            </div>
        </section>""",
        "faq": [
            {"q": "Does cannabis treat PTSD?", "a": "Large-scale reviews found no consistent evidence for its efficacy; some results showed it actually complicates recovery."},
            {"q": "What is the rebound effect?", "a": "The phenomenon where symptoms return with greater intensity once a drug wears off."}
        ]
    },
    112: {
        "title": "Inside The Science Behind How We Link Childhood Stress to Lifelong Digestive Issues: What the Brain Tells Us",
        "category": "Behavioral Psychology",
        "desc": "Early life stress rewires the gut-brain axis, leading to chronic pain and IBS in adulthood.",
        "content": """<h2>Introduction</h2>
        <p>We've always known that stress gives you a "stomach ache." But new research has linked **Childhood Trauma** to a lifetime of chronic digestive issues like IBS and constipation. It turns out that stressful events early in life literally "set the sensitivity dial" for your entire gastrointestinal system for decades to come.</p>
        <p>When a child experiences chronic stress, their brain and gut go into a "Permanent Alarm State." The gut-brain axis becomes hypersensitive, meaning a normal sandwich in adulthood can be perceived by the body as a full-blown emergency.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        
        <h2>The 'Alarm Dial'</h2>
        <p>By studying both humans and animals, researchers found that different types of stress affect different pathways. Some stress causes the gut to move too fast (IBS-D), while others cause it to "freeze" (Constipation). This proves that your digestive health isn't just about what you eat; it's about what you **experienced** as a child.</p>
        
        <h2>Healing the Connection</h2>
        <p>The good news? Because the connection is neurological, we can use "Brain-Gut Psychotherapy" to heal the damage. Techniques like Gut-Directed Hypnosis and specific forms of CBT have been shown to "reset" the sensitivity dial, providing relief even where traditional diets and medicines have failed.</p>

        <section class="faq-section" style="margin-top: 4rem; border-top: 1px solid rgba(0,0,0,0.1); padding-top: 2rem;">
            <h2 style="margin-bottom: 2rem;">Frequently Asked Questions</h2>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.1rem; color: var(--primary-color); margin-bottom: 0.5rem;">What is the gut-brain axis?</h3>
                <p>The two-way communication network between your central nervous system and your enteric (gut) nervous system.</p>
            </div>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.1rem; color: var(--primary-color); margin-bottom: 0.5rem;">Can childhood stress be healed in the gut?</h3>
                <p>Yes. Addressing the trauma through somatic therapy and relaxation techniques can physically reduce the inflammation and sensitivity in the digestive tract.</p>
            </div>
        </section>""",
        "faq": [
            {"q": "Is IBS linked to childhood trauma?", "a": "Yes, chronic stress in childhood can predispose individuals to develop IBS and other digestive disorders in adulthood."},
            {"q": "What is gut-directed hypnosis?", "a": "A specialized therapy that uses relaxation and imagery to soothe the gut's nervous system."}
        ]
    },
    113: {
        "title": "Why Microplastics May Be Quietly Damaging Your Brain and Fueling Alzheimer’s and Parkinson’s Matters for Mental Health",
        "category": "Neuroscience",
        "desc": "Tiny plastic particles are bypassing the blood-brain barrier and triggering chronic neuro-inflammation.",
        "content": """<h2>Introduction</h2>
        <p>We are living in a plastic world, and now, that plastic is living in us. Groundbreaking research has discovered that **Microplastics** are now bypassing the blood-brain barrier—the body's most secure defense system—and entering individual brain cells. Once inside, they act as a "Permanent Irritant," triggering the chronic inflammation that fuels Alzheimer's and Parkinson's.</p>
        <p>The average adult may now be consuming up to a credit card's worth of plastic every single year through food, water, and even the dust we breathe. This isn't just an environmental crisis; it is a neurological one.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        
        <h2>The 'Brain Spark'</h2>
        <p>In the brain, microplastics trigger an immune response from "Microglia"—the brain's cleanup crew. But because the plastics cannot be broken down, the microglia stay in a constant "Attack Mode," accidentally damaging healthy brain tissue in the process. This "immuno-burn" is a primary driver of the rapid cognitive decline seen in modern populations.</p>
        
        <h2>How to Protect Your Brain</h2>
        <p>While you cannot avoid microplastics entirely, you can significantly reduce your intake by avoiding plastic-bottled water, never microwaving food in plastic containers, and using a high-quality air purifier at home. Protecting your brain now is essential for your mental health in thirty years.</p>

        <section class="faq-section" style="margin-top: 4rem; border-top: 1px solid rgba(0,0,0,0.1); padding-top: 2rem;">
            <h2 style="margin-bottom: 2rem;">Frequently Asked Questions</h2>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.1rem; color: var(--primary-color); margin-bottom: 0.5rem;">How do microplastics enter the brain?</h3>
                <p>They are so small (often nano-sized) that they can slip through the gaps in the blood-brain barrier or actually be 'carried' in by hitching a ride on proteins.</p>
            </div>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.1rem; color: var(--primary-color); margin-bottom: 0.5rem;">Are certain plastics more dangerous?</h3>
                <p>Plastics that contain BPA and phthalates are particularly neuro-toxic as they also mimic hormones in the brain, disrupting the delicate chemical balance.</p>
            </div>
        </section>""",
        "faq": [
            {"q": "Can microplastics reach the brain?", "a": "Yes, recent studies have confirmed the presence of nano-plastics inside brain tissue samples."},
            {"q": "What is the blood-brain barrier?", "a": "A protective layer of cells that restricts which substances can enter the brain from the blood."}
        ]
    },
    114: {
        "title": "The Science of Depression May Start With an Energy Problem in Brain Cells",
        "category": "Behavioral Psychology",
        "desc": "A breakthrough discover finds that depression is linked to a 'Mitochondrial Glitch' that makes cells fail under stress.",
        "content": """<h2>Introduction</h2>
        <p>We've always talked about depression as a "chemical imbalance" or a "social problem." But new research has found a startling commonality in the brains of people with Major Depressive Disorder: an **Energy Crisis**. It turns out that the mitochondria (the power plants of your cells) in depressed individuals are malfunctioning—they are working too hard at rest and failing to provide energy when it's actually needed.</p>
        <p>This explains the hallmark symptoms of depression: the bone-deep fatigue, the "brain fog," and the inability to simply get out of bed. It's not that the person doesn't *want* to; their cells literally don't have the fuel to execute the command.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        
        <h2>The 'Mitochondrial Burnout'</h2>
        <p>In depressed young adults, their cells were "redlining" all the time, even when they were sitting still. This meant that when they faced a real-world stressor, their cells had zero "reserve" left. They entered a state of "Metabolic Shutoff," which we experience as the emotional and physical numbing of clinical depression.</p>
        
        <h2>Treating the Power Plant</h2>
        <p>This discovery is leading to a new class of treatments called **Mitochondrial Boosters**. By using specific nutrients like CoQ10, Creatine, and Magnesium, doctors are seeing success in "recharging" the brain cells, allowing the traditional therapy and antidepressants to finally work effectively.</p>

        <section class="faq-section" style="margin-top: 4rem; border-top: 1px solid rgba(0,0,0,0.1); padding-top: 2rem;">
            <h2 style="margin-bottom: 2rem;">Frequently Asked Questions</h2>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.1rem; color: var(--primary-color); margin-bottom: 0.5rem;">Is depression a metabolism problem?</h3>
                <p>New evidence suggests 'Metabolic Psychiatry' is a major frontier, as your brain uses 20% of your body's energy to regulate your mood.</p>
            </div>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.1rem; color: var(--primary-color); margin-bottom: 0.5rem;">Can a keto diet help depression?</h3>
                <p>Some studies show that ketogenic diets provide the brain with 'cleaner' fuel (ketones), which may help stabilize mitochondrial function in some types of clinical depression.</p>
            </div>
        </section>""",
        "faq": [
            {"q": "What is the link between depression and energy?", "a": "Depression is associated with mitochondrial dysfunction, where cells fail to produce and manage energy efficiently."},
            {"q": "What are mitochondria?", "a": "The organelles within cells responsible for producing ATP, the body's primary energy currency."}
        ]
    },
    115: {
        "title": "The Brain Scans Reveal How Ketamine Quickly Lifts Severe Depression: A Psychological Perspective",
        "category": "Behavioral Psychology",
        "desc": "See how ketamine reshapes critical brain receptors to lift treatment-resistant depression in hours.",
        "content": """<h2>Introduction</h2>
        <p>Traditional antidepressants take weeks or months to work. But **Ketamine** can lift a severe, suicidal depression in just a few hours. Until now, we didn't know *why*. A new brain-imaging study has finally caught the process in action: ketamine actually reshapes the "Communication Receptors" between your neurons, effectively bypasses the broken circuits of depression.</p>
        <p>It's like finding a detour when the main highway is blocked. Ketamine allows the brain to "talk to itself" again in regions that have been silent for years.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        
        <h2>The 'Synapse Repair'</h2>
        <p>Depression causes a literal "thinning" of connections in the prefrontal cortex. Brain scans show that within 24 hours of a ketamine treatment, these connections begin to regrow. It is the most rapid form of **Neuroplasticity** ever observed in human subjects. It's not just a mood boost; it's a physical reconstruction of the brain's hardware.</p>
        
        <h2>A Bridge to Long-Term Health</h2>
        <p>Ketamine is not a magic pill, but it acts as a "Bridge." It stops the immediate crisis, providing a window of 7 to 10 days where the brain is hyper-receptive to new learning. If you pair this window with traditional therapy, you can build permanent, healthy neural pathways that remain long after the ketamine has left your system.</p>

        <section class="faq-section" style="margin-top: 4rem; border-top: 1px solid rgba(0,0,0,0.1); padding-top: 2rem;">
            <h2 style="margin-bottom: 2rem;">Frequently Asked Questions</h2>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.1rem; color: var(--primary-color); margin-bottom: 0.5rem;">Is ketamine therapy safe?</h3>
                <p>When administered in a clinical setting by doctors, it is highly safe and effective. It is NOT the same as recreational ketamine use.</p>
            </div>
            <div class="faq-item" style="margin-bottom: 2rem;">
                <h3 style="font-size: 1.1rem; color: var(--primary-color); margin-bottom: 0.5rem;">Does the effect wear off?</h3>
                <p>Yes, the acute effects usually last 1-2 weeks. This is why it is used as an 'induction' tool alongside traditional therapeutic work.</p>
            </div>
        </section>""",
        "faq": [
            {"q": "How fast does ketamine work for depression?", "a": "Many patients report significant improvement in suicidal thoughts and mood within 2-4 hours."},
            {"q": "Does ketamine grow brain cells?", "a": "It triggers 'synaptogenesis'—the growth of new connections between existing brain cells, specifically in the prefrontal cortex."}
        ]
    }
}

def generate_article_html(art_id, data):
    date_str = datetime.datetime.now().strftime("%B %d, %Y")
    title = data["title"]
    desc = data["desc"]
    cat = data["category"] if data["category"] else "Trending Psychology"
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
    <div class="progress-bar" id="progress-bar"></div>
    <header>
        <nav class="nav-container">
            <div class="logo">Mind &amp; Balance</div>
            <div class="nav-right">
                <ul class="nav-links">
                    <li><a href="index.html">Home</a></li>
                    <li><a href="index.html#articles">Articles</a></li>
                    <li><a href="about.html">About</a></li>
                    <li><a href="contact.html">Contact</a></li>
                </ul>
                <button id="theme-toggle" class="theme-toggle" aria-label="Toggle Dark Mode">🌙</button>
            </div>
        </nav>
    </header>

    <div class="article-header hidden">
        <div class="container">
            <span class="card-category" style="display:block; margin-bottom:1rem; background: var(--accent-gradient); color: white; padding: 0.2rem 0.8rem; border-radius: 20px; width: fit-content;">TRENDING</span>
            <h1 style="font-size: 2.5rem; max-width: 900px; margin: 0 auto; line-height: 1.2;">{title}</h1>
            <div class="article-meta">
                <img src="https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&q=80&w=100&h=100" alt="Mind & Balance Editorial Team">
                <span>By Leafanoo Research Team</span>
                <span>•</span><span>{date_str}</span><span>•</span><span>{len(content)//500 + 3} min read</span>
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
    
    for art_id, data in batch_5_articles.items():
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
                    <span class="card-category" style="background: var(--accent-gradient); color: white; padding: 0.1rem 0.5rem; border-radius: 4px;">TRENDING</span>
                    <h3 class="card-title">{data['title']}</h3>
                    <p class="card-excerpt">{data['desc']}...</p>
                    <a href="article{art_id}.html" class="card-link">Read More &rarr;</a>
                </div>
            </article>\n"""
            
        # Build Sitemap
        new_sitemap_xml += f"""    <url>\n        <loc>https://leafanoo.com/article{art_id}.html</loc>\n        <changefreq>weekly</changefreq>\n        <priority>0.9</priority>\n    </url>\n"""

    # 1. Inject cards into index.html
    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        idx_content = f.read()
    try:
        # Find the last article card and append after it
        parts = idx_content.rsplit('<article class="card', 1)
        if len(parts) == 2:
            card_end = parts[1].find('</article>') + len('</article>')
            pre = parts[0] + '<article class="card' + parts[1][:card_end]
            post = parts[1][card_end:]
            idx_content = pre + new_cards_html + post
            with open(INDEX_PATH, 'w', encoding='utf-8') as f:
                f.write(idx_content)
            print("✅ Updated index.html with Batch 5.")
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
