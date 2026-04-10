#!/usr/bin/env python3
"""
Batch 10: Articles 181–200
20 high-RPM trending neuroscience & mental health articles
Topics sourced from competitor_trends.csv (ScienceDaily feed)
"""
import os, re, datetime

BASE_DIR = "/Users/khalidaitelmaati/Desktop/scrapy-master/psychology-theme-main"
INDEX_PATH = os.path.join(BASE_DIR, "index.html")
SITEMAP_PATH = os.path.join(BASE_DIR, "sitemap.xml")

# All verified-working Unsplash IDs (HTTP 200 confirmed)
VERIFIED_IMGS = [
    "1544367567-0f2fcb009e0b",  # therapy session
    "1559757148-5c350d0d3c56",  # brain scan white
    "1541781774459-bb2af2f05b55", # anxious face
    "1506126613408-eca07ce68773",  # yoga / mindfulness
    "1507003211169-0a1dd7228f2d",  # man portrait
    "1543269865-cbf427effbad",    # hiking / growth
    "1558618666-fcd25c85cd64",    # neuron network blue
    "1507413245164-6160d8298b31",  # CT scan
    "1508739773434-c26b3d09e071",  # DNA / genetics
    "1499209974431-9dddcece7f88",  # thinking person
    "1515377905703-c4788e51af15",  # happy teens
    "1508214751196-bcfd4ca60f91",  # woman in sunlight
    "1552664730-d307ca884978",    # awake at night
    "1552053831-71594a27632d",    # golden retriever
    "1529156069898-49953e39b3ac",  # family in park
    "1484480974693-6ca0a78fb36b",  # alarm clock / time
    "1522202176988-66273c2fd55f",  # student studying
    "1573497491208-6b1acb260507",  # DNA strands
    "1573496359142-b8d87734a5a2",  # woman thinking
    "1531983412531-1f49a365ffed",  # brain MRI
]

ARTICLES = {
    181: {
        "title": "Alzheimer's Warning Sign You're Missing: Silent Brain Blood Flow Drops",
        "category": "Neuroscience",
        "img_idx": 1,
        "desc": "New research shows that subtle drops in brain blood flow may be Alzheimer's earliest detectable warning sign — years before memory problems begin.",
        "content": """<h2>The Vascular Link to Alzheimer's</h2>
        <p>For decades, the focus of Alzheimer's research has been on amyloid plaques and tau tangles. But a major new study is shifting attention to something more fundamental: <strong>blood flow</strong>. Researchers have found that subtle, measurable drops in cerebral blood flow appear years — possibly decades — before cognitive symptoms emerge.</p>
        <p>This discovery is significant because blood flow can be measured with simple, non-invasive MRI scans that are already widely available in hospitals. It could transform how we screen for Alzheimer's risk long before neurons begin to die.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        <h2>Why Blood Flow Matters to the Brain</h2>
        <p>The brain is extraordinarily energy-hungry, consuming roughly 20% of the body's total oxygen despite comprising only 2% of body weight. Even small reductions in blood flow create an energy crisis for neurons. Over time, this metabolic stress may trigger the inflammatory cascade that leads to plaque formation — meaning vascular problems might precede, not follow, the classic Alzheimer's pathology.</p>
        <h2>What This Means for You</h2>
        <p>The cardiovascular choices you make today — exercise, diet, blood pressure management, not smoking — directly protect your brain's blood supply. Managing heart health is now understood to be brain health. A cardiologist's advice and a neurologist's advice are, in this sense, the same.</p>
        <section class="faq-section" style="margin-top:4rem;border-top:1px solid rgba(0,0,0,0.1);padding-top:2rem;">
            <h2 style="margin-bottom:2rem;">Frequently Asked Questions</h2>
            <div class="faq-item" style="margin-bottom:2rem;">
                <h3 style="font-size:1.2rem;color:var(--primary-color);margin-bottom:0.5rem;">Can brain blood flow problems be reversed?</h3>
                <p>In many cases, yes. Aerobic exercise is the most potent known intervention for improving cerebral blood flow at any age.</p>
            </div>
            <div class="faq-item" style="margin-bottom:2rem;">
                <h3 style="font-size:1.2rem;color:var(--primary-color);margin-bottom:0.5rem;">How early can a blood flow problem be detected?</h3>
                <p>Advanced MRI perfusion imaging can detect flow changes up to 20 years before clinical Alzheimer's symptoms, according to new research.</p>
            </div>
        </section>""",
        "faq": [
            {"q": "What causes brain blood flow to drop?", "a": "High blood pressure, inflammation, arterial stiffness, and sedentary lifestyle are the main contributors."},
            {"q": "Is Alzheimer's a vascular disease?", "a": "There is growing evidence it has a significant vascular component, not just a protein accumulation disorder."}
        ]
    },
    182: {
        "title": "5-Day Depression Reset: How Intensive TMS is Changing Psychiatry",
        "category": "Mental Health",
        "img_idx": 0,
        "desc": "A new 5-day intensive TMS protocol is showing results comparable to 6 weeks of standard treatment. Could this be the future of depression care?",
        "content": """<h2>The Problem With 6 Weeks</h2>
        <p>Standard transcranial magnetic stimulation (TMS) for depression requires 30 sessions over 6 weeks. For people in crisis, that's a long time to wait. A UCLA-led study just tested something radical: <strong>five TMS sessions per day for five days</strong>. The results were striking — comparable outcomes to the traditional 6-week course.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        <h2>How TMS Works</h2>
        <p>TMS delivers precisely targeted magnetic pulses to specific regions of the prefrontal cortex — the area most associated with mood regulation. These pulses essentially "restart" sluggish neural circuits without the systemic side effects of antidepressant medications. It is FDA-approved, non-invasive, and performed while the patient is fully awake.</p>
        <h2>Who Benefits Most</h2>
        <p>This intensive protocol showed particular promise for people who had already failed multiple antidepressants. These treatment-resistant cases represent some of the most severe and enduring forms of depression, and for them, a rapid 5-day reset could be life-saving.</p>
        <section class="faq-section" style="margin-top:4rem;border-top:1px solid rgba(0,0,0,0.1);padding-top:2rem;">
            <h2 style="margin-bottom:2rem;">Frequently Asked Questions</h2>
            <div class="faq-item" style="margin-bottom:2rem;">
                <h3 style="font-size:1.2rem;color:var(--primary-color);margin-bottom:0.5rem;">Is TMS covered by insurance?</h3>
                <p>In the US, TMS is covered by most major insurers for treatment-resistant depression after two or more antidepressant failures.</p>
            </div>
        </section>""",
        "faq": [
            {"q": "What is TMS therapy?", "a": "Transcranial Magnetic Stimulation is a non-invasive treatment that uses magnetic pulses to stimulate specific brain regions."},
            {"q": "Does TMS hurt?", "a": "Most patients feel only a mild tapping sensation on the scalp and can drive themselves home after each session."}
        ]
    },
    183: {
        "title": "Stem Cells for Parkinson's: The Clinical Trial Giving Hope to Millions",
        "category": "Neuroscience",
        "img_idx": 7,
        "desc": "Doctors have begun implanting lab-grown dopamine-producing stem cells into Parkinson's patients. This is what the trial results show.",
        "content": """<h2>The Dopamine Problem</h2>
        <p>Parkinson's disease is, at its core, a loss of dopamine-producing neurons in a region of the brain called the substantia nigra. As these neurons die, the smooth, automatic control of movement breaks down — producing the tremors, rigidity, and slowness of movement that characterize the condition. Current treatments only manage symptoms. They don't replace what's lost.</p>
        <p>That's what makes this clinical trial so historic. Researchers are now implanting <strong>stem cell-derived dopamine neurons</strong> directly into the brains of Parkinson's patients, hoping the transplanted cells will integrate into the existing circuitry and restore function.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        <h2>Early Results Are Cautiously Optimistic</h2>
        <p>In early-stage trials, a subset of patients who received the implants showed meaningful improvements in motor function. Critically, the implanted cells appear to have survived and may be producing dopamine. Full results from randomized Phase 2 trials are expected within the next 3–5 years.</p>
        <section class="faq-section" style="margin-top:4rem;border-top:1px solid rgba(0,0,0,0.1);padding-top:2rem;">
            <h2 style="margin-bottom:2rem;">Frequently Asked Questions</h2>
            <div class="faq-item" style="margin-bottom:2rem;">
                <h3 style="font-size:1.2rem;color:var(--primary-color);margin-bottom:0.5rem;">Could stem cell therapy cure Parkinson's?</h3>
                <p>It is not a cure, but it may significantly slow progression and restore lost dopamine — a major quality-of-life improvement.</p>
            </div>
        </section>""",
        "faq": [
            {"q": "What causes Parkinson's disease?", "a": "The progressive loss of dopamine-producing neurons in the brain's motor control centers."},
            {"q": "Are stem cell treatments approved for Parkinson's?", "a": "Not yet — they are in active clinical trials but not yet a standard therapy."}
        ]
    },
    184: {
        "title": "Sugary Drinks and Teen Anxiety: The Overlooked Connection",
        "category": "Mental Health",
        "img_idx": 10,
        "desc": "A new multi-study review links high consumption of sodas and energy drinks to significantly elevated anxiety in adolescents. Here's the science.",
        "content": """<h2>More Than a Sugar Rush</h2>
        <p>We know sugary drinks are bad for teeth and waistlines. But a sweeping new review of multiple studies has found a consistent link between high consumption of sodas, energy drinks, and sweetened beverages and <strong>elevated anxiety symptoms in teenagers</strong>. This connection exists independently of overall diet quality.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        <h2>The Physiological Mechanism</h2>
        <p>Researchers point to several potential pathways. First, the extreme glucose spikes and crashes from high-sugar drinks cause cortisol surges that the adolescent brain — still developing its regulation systems — is poorly equipped to manage. Second, caffeine in energy drinks acts as a direct anxiogenic, amplifying the stress response. Third, chronic high-sugar intake promotes systemic inflammation, which is increasingly linked to anxiety and mood disorders.</p>
        <h2>A Critical Development Window</h2>
        <p>Adolescence is when the brain's emotional regulation systems are still being wired. Chronic stress during this period can reset the baseline of the HPA axis — the body's stress response system — to a higher, more reactive state. This could have lasting consequences for mental health into adulthood.</p>
        <section class="faq-section" style="margin-top:4rem;border-top:1px solid rgba(0,0,0,0.1);padding-top:2rem;">
            <h2 style="margin-bottom:2rem;">Frequently Asked Questions</h2>
            <div class="faq-item" style="margin-bottom:2rem;">
                <h3 style="font-size:1.2rem;color:var(--primary-color);margin-bottom:0.5rem;">Does sugar cause anxiety?</h3>
                <p>Sugar doesn't directly cause anxiety, but it creates blood glucose swings and inflammation that are significant anxiety triggers, especially in developing brains.</p>
            </div>
        </section>""",
        "faq": [
            {"q": "Which drinks are worst for teen anxiety?", "a": "Energy drinks combining caffeine and sugar are the most potent combination, followed by sodas consumed multiple times daily."},
            {"q": "How quickly can cutting sugary drinks reduce anxiety?", "a": "Studies show measurable reductions in anxious symptoms within 4–6 weeks of eliminating high-sugar beverages."}
        ]
    },
    185: {
        "title": "Your Brain Keeps Developing Into Your 30s — What That Means for You",
        "category": "Neuroscience",
        "img_idx": 16,
        "desc": "The popular belief that your brain is 'done' at 25 is wrong. New research shows meaningful development continues well into your 30s.",
        "content": """<h2>The '25 Years Old' Myth</h2>
        <p>You've probably heard it: your brain isn't fully developed until you're 25. This claim — popularized in psychology and neuroscience circles — turns out to be a significant oversimplification. A landmark new study using high-resolution brain imaging has found that meaningful structural development continues into the <strong>mid-to-late 30s</strong>, particularly in regions related to self-regulation, perspective-taking, and complex judgment.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        <h2>What's Still Changing</h2>
        <p>The prefrontal cortex — the brain's "executive suite" — continues refining its connections with the limbic system (the emotional brain) well into the 30s. This means your ability to regulate emotional responses, make complex moral judgments, and plan for the distant future is still being fine-tuned during this period. Experiences during your 20s and 30s literally shape the architecture of your adult brain.</p>
        <h2>The Mental Health Implications</h2>
        <p>This finding has profound implications: it means adults in their late 20s and 30s are still malleable. Mental health interventions, learning new skills, and even psychotherapy can reshape neural pathways in ways that were previously thought impossible for 'fully formed' adult brains.</p>
        <section class="faq-section" style="margin-top:4rem;border-top:1px solid rgba(0,0,0,0.1);padding-top:2rem;">
            <h2 style="margin-bottom:2rem;">Frequently Asked Questions</h2>
            <div class="faq-item" style="margin-bottom:2rem;">
                <h3 style="font-size:1.2rem;color:var(--primary-color);margin-bottom:0.5rem;">At what age is the human brain fully developed?</h3>
                <p>Based on the latest research, structural brain development shows meaningful changes through the mid-30s, though some regions continue subtle refinement throughout life.</p>
            </div>
        </section>""",
        "faq": [
            {"q": "Can you learn better in your 30s than your 20s?", "a": "In some respects yes — older brains are better at integrating complex knowledge and understanding context, even as raw processing speed declines."},
            {"q": "Does this mean the brain can heal from trauma in adulthood?", "a": "Yes, neuroplasticity means the brain retains capacity for healing and rewiring through therapy and experience throughout adulthood."}
        ]
    },
    186: {
        "title": "How Psychedelics Unlock Memory by Shutting Down Reality",
        "category": "Mental Health",
        "img_idx": 6,
        "desc": "New research reveals how psilocybin and LSD quiet the brain's reality-processing system, flooding conscious experience with vivid memory fragments.",
        "content": """<h2>The Neuroscience of the Trip</h2>
        <p>Scientists have long known that psychedelics produce vivid visual experiences. Now, for the first time, they've traced exactly how this happens at the neural level. Research shows that psychedelics suppress slow, rhythmic brain waves in the visual cortex — the waves that normally process incoming sensory data from the eyes. With this input suppressed, the brain doesn't go quiet. Instead, it fills the void with <strong>memories, emotions, and associations</strong>.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        <h2>Dreaming While Awake</h2>
        <p>The mechanism is remarkably similar to dreaming. During REM sleep, the brain is cut off from external sensory input and the visual cortex generates experience from internal memory banks. Psychedelics appear to recreate this state while the person is conscious and aware — which is why hallucinations often feature meaningful personal imagery rather than random noise.</p>
        <h2>Therapeutic Implications</h2>
        <p>This understanding explains why psychedelic therapy is so effective at processing trauma. When the brain's reality-suppression mode is activated, deeply stored memories — including traumatic ones — become accessible and can be re-examined with unusual emotional openness. This is the pharmacological basis of the healing that trials of MDMA and psilocybin therapy are demonstrating in PTSD patients.</p>
        <section class="faq-section" style="margin-top:4rem;border-top:1px solid rgba(0,0,0,0.1);padding-top:2rem;">
            <h2 style="margin-bottom:2rem;">Frequently Asked Questions</h2>
            <div class="faq-item" style="margin-bottom:2rem;">
                <h3 style="font-size:1.2rem;color:var(--primary-color);margin-bottom:0.5rem;">Are psychedelics legal for therapy?</h3>
                <p>In the US, psilocybin is legal for therapeutic use in Oregon and Colorado. MDMA-assisted therapy is under final FDA review. Multiple countries have approved compassionate-use programs.</p>
            </div>
        </section>""",
        "faq": [
            {"q": "Why do psychedelics cause hallucinations?", "a": "They suppress the brain's normal reality-processing waves, causing it to draw experience from memory rather than external input."},
            {"q": "Can psilocybin treat PTSD?", "a": "Clinical trials show highly significant results, with some studies reporting 70%+ PTSD symptom reduction after 2–3 sessions."}
        ]
    },
    187: {
        "title": "The Science of Savoring: Why Couples Who Celebrate Together, Stay Together",
        "category": "Relationships",
        "img_idx": 14,
        "desc": "Research from the University of Illinois shows that couples who actively savor positive shared experiences build dramatically more resilient, lasting bonds.",
        "content": """<h2>Beyond Conflict Management</h2>
        <p>Relationship psychology has long focused on how couples handle conflict. But new research suggests that what you do during the <em>good times</em> may matter just as much. A study from the University of Illinois found that partners who deliberately slow down to savor shared positive moments — whether reminiscing about a fond memory or fully immersing in a present enjoyment — reported <strong>significantly higher relationship satisfaction</strong> and were more likely to stay together over time.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        <h2>The Neurochemistry of Savoring</h2>
        <p>When you consciously savor a positive experience with your partner, your brain releases a cascade of oxytocin and dopamine — the bonding and reward chemicals. This creates rich, emotionally charged memories that function as a 'relationship reservoir' couples can draw on during difficult times. Couples with more positive shared memories show greater resilience when under stress.</p>
        <h2>The Practical Methodology</h2>
        <p>Savoring is a learnable skill. It involves deliberate practices like: taking "mental photographs" at happy moments, verbally appreciating your partner in the moment, and regularly revisiting positive shared memories together. These are not passive; they require intentional attention.</p>
        <section class="faq-section" style="margin-top:4rem;border-top:1px solid rgba(0,0,0,0.1);padding-top:2rem;">
            <h2 style="margin-bottom:2rem;">Frequently Asked Questions</h2>
            <div class="faq-item" style="margin-bottom:2rem;">
                <h3 style="font-size:1.2rem;color:var(--primary-color);margin-bottom:0.5rem;">What is 'savoring' in psychology?</h3>
                <p>Savoring is the deliberate act of attending to and appreciating a positive experience, prolonging and deepening its emotional impact.</p>
            </div>
        </section>""",
        "faq": [
            {"q": "How often should couples savor experiences?", "a": "Research suggests even brief, daily moments of deliberate appreciation have measurable effects on relationship quality."},
            {"q": "Can savoring help a struggling relationship?", "a": "Yes, deliberately revisiting shared positive memories can reactivate feelings of connection even during conflict periods."}
        ]
    },
    188: {
        "title": "Exercise Is Medicine: Why Running May Beat Antidepressants",
        "category": "Mental Health",
        "img_idx": 5,
        "desc": "A sweeping global review confirms what many therapists have long suspected: aerobic exercise is one of the most powerful interventions for depression and anxiety available.",
        "content": """<h2>The Definitive Review</h2>
        <p>A massive review analyzing data from tens of thousands of people aged 10 to 90 across dozens of countries has delivered a striking finding: <strong>exercise — especially aerobic activity — reduces depression and anxiety as effectively as medication</strong> in many cases, and more effectively than medication in some specific populations.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        <h2>The Biological Pathways</h2>
        <p>Exercise works on depression through multiple biological pathways simultaneously: it raises BDNF (brain-derived neurotrophic factor), which promotes neuronal growth; it reduces inflammatory cytokines linked to depression; it normalizes cortisol; it increases serotonin, dopamine, and norepinephrine; and it activates the endocannabinoid system. No single antidepressant medication targets all of these systems at once.</p>
        <h2>What Kind and How Much</h2>
        <p>The data suggests that almost any aerobic activity helps: running, swimming, cycling, dancing. The optimal dose appears to be 150–300 minutes of moderate aerobic activity per week — exactly in line with existing public health guidelines. More is better up to a point, with twice-weekly resistance training adding additional benefits for anxiety.</p>
        <section class="faq-section" style="margin-top:4rem;border-top:1px solid rgba(0,0,0,0.1);padding-top:2rem;">
            <h2 style="margin-bottom:2rem;">Frequently Asked Questions</h2>
            <div class="faq-item">
                <h3 style="font-size:1.2rem;color:var(--primary-color);margin-bottom:0.5rem;">How quickly does exercise improve depression?</h3>
                <p>Many people report mood improvements after a single session, but sustained improvement in clinical depression typically requires 4–6 weeks of consistent exercise.</p>
            </div>
        </section>""",
        "faq": [
            {"q": "Is exercise enough to treat clinical depression?", "a": "For mild-to-moderate depression, exercise alone can be highly effective. Severe depression typically requires exercise in combination with therapy and/or medication."},
            {"q": "What's the best exercise for anxiety?", "a": "Running and swimming (rhythmic aerobic exercise) show the strongest evidence for anxiety reduction, likely due to their meditative and breath-regulating qualities."}
        ]
    },
    189: {
        "title": "The Brain Implant That Beat Years of Treatment-Resistant Depression",
        "category": "Mental Health",
        "img_idx": 7,
        "desc": "Vagus nerve stimulation (VNS) is helping people who have lived with depression for decades find lasting relief. Here's how it works and who qualifies.",
        "content": """<h2>When Everything Fails</h2>
        <p>For a significant subset of people with major depression, medications, therapy, even TMS and ECT — none of it works. They have what clinicians call <em>treatment-resistant depression</em>, and they represent some of the most severe suffering in psychiatry. For them, a small implanted device stimulating the vagus nerve may be the breakthrough they've been waiting for.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        <h2>The Study Results</h2>
        <p>In a landmark study, researchers followed patients with decades-long treatment-resistant depression who received a vagus nerve stimulator (VNS). Most had lived with depression for 20+ years and had tried an average of 8 different treatments. Within two years, a meaningful subset reported significant, sustained improvement — some achieving full remission for the first time in their adult lives.</p>
        <h2>How Vagus Nerve Stimulation Works</h2>
        <p>The vagus nerve is a superhighway between the brain and the body. By sending gentle electrical pulses up this pathway, VNS appears to gradually recalibrate the brain's mood-regulation circuits, particularly in the frontal lobes and limbic system. Unlike ECT, it produces no memory disruption and can be continuously active long-term.</p>
        <section class="faq-section" style="margin-top:4rem;border-top:1px solid rgba(0,0,0,0.1);padding-top:2rem;">
            <h2 style="margin-bottom:2rem;">Frequently Asked Questions</h2>
            <div class="faq-item">
                <h3 style="font-size:1.2rem;color:var(--primary-color);margin-bottom:0.5rem;">Is vagus nerve stimulation FDA-approved for depression?</h3>
                <p>Yes, the FDA approved VNS for treatment-resistant depression in 2005, though it is still underutilized due to insurance coverage challenges.</p>
            </div>
        </section>""",
        "faq": [
            {"q": "What is the vagus nerve?", "a": "The longest cranial nerve, connecting the brainstem to most major organs and playing a vital role in mood, digestion, and stress regulation."},
            {"q": "How long does VNS take to work?", "a": "Unlike medications that work (if they work) in weeks, VNS benefits typically build over 6–12 months of continuous stimulation."}
        ]
    },
    190: {
        "title": "Autism and Emotions: Why Facial Expressions Work Differently in Autistic Brains",
        "category": "Neurodiversity",
        "img_idx": 9,
        "desc": "New research shows autistic people produce and read facial expressions differently — not because of a 'disorder,' but because of a distinct neural processing style.",
        "content": """<h2>Rethinking the 'Lack of Emotion' Myth</h2>
        <p>One of the most damaging misconceptions about autism is that autistic people lack empathy or emotional expression. In reality, research consistently shows that autistic individuals experience emotions just as deeply as neurotypical people — but their <strong>facial expression patterns are different</strong>. A new study found these patterns are distinct, not deficient.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        <h2>The Research Findings</h2>
        <p>Researchers filmed autistic and non-autistic participants expressing anger, happiness, and sadness, then used AI face-analysis tools to measure the muscle movements. Autistic participants produced more varied, idiosyncratic expressions — using different facial muscles and movement patterns than the neurotypical 'script.' This explained why neurotypical observers often struggle to 'read' autistic faces: it's a dialect mismatch, not an absence of emotion.</p>
        <h2>The Double Empathy Problem</h2>
        <p>This supports the 'Double Empathy Problem' theory — the idea that social communication difficulties between autistic and non-autistic people are mutual and bidirectional, not a one-sided 'deficit' in the autistic person. Non-autistic people are equally poor at reading autistic emotional expressions. This has profound implications for therapy, education, and social policy.</p>
        <section class="faq-section" style="margin-top:4rem;border-top:1px solid rgba(0,0,0,0.1);padding-top:2rem;">
            <h2 style="margin-bottom:2rem;">Frequently Asked Questions</h2>
            <div class="faq-item">
                <h3 style="font-size:1.2rem;color:var(--primary-color);margin-bottom:0.5rem;">Do autistic people feel less empathy?</h3>
                <p>No — research shows autistic people typically feel deep empathy, but may express and process it through different channels than neurotypical people.</p>
            </div>
        </section>""",
        "faq": [
            {"q": "What is the Double Empathy Problem?", "a": "The theory that social misunderstanding between autistic and neurotypical people is mutual, not a one-sided autistic deficit."},
            {"q": "Can autistic people learn to 'read' neurotypical expressions?", "a": "With effort, yes — but the research argues the neurotypical world should also adapt, not just the autistic person."}
        ]
    },
    191: {
        "title": "Teen Brain Secrets: The Hidden Synapse Boom of Adolescence",
        "category": "Neuroscience",
        "img_idx": 17,
        "desc": "Scientists have discovered that the teenage brain doesn't just prune old connections — it also builds explosive new synapse clusters that shape adult thinking.",
        "content": """<h2>Not Just Pruning</h2>
        <p>For years, neuroscience told a simple story of adolescent brain development: the teen brain prunes away unused synaptic connections to increase efficiency. This pruning is real, but new research adds a striking counterpoint: the teen brain simultaneously builds <strong>dense new clusters of synapses</strong> in specific areas — and these clusters are found nowhere else in development.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        <h2>What These New Synapses Do</h2>
        <p>The newly discovered synapse 'hotspots' emerge in the dendritic shafts of pyramidal neurons — a location not typically associated with synapse formation. Researchers believe these clusters are critical for developing higher-order thinking skills: abstract reasoning, moral judgment, complex social understanding. When the formation process is disrupted — by stress, trauma, or substance use — it may interfere with the development of these uniquely human cognitive capacities.</p>
        <h2>Why Teen Experiences Matter So Much</h2>
        <p>This discovery helps explain why adolescence is such a sensitive period. The good news: enriched environments, education, and positive relationships actively promote this synapse building. The bad news: trauma, substance abuse, and chronic stress can disrupt it in ways that last a lifetime.</p>
        <section class="faq-section" style="margin-top:4rem;border-top:1px solid rgba(0,0,0,0.1);padding-top:2rem;">
            <h2 style="margin-bottom:2rem;">Frequently Asked Questions</h2>
            <div class="faq-item">
                <h3 style="font-size:1.2rem;color:var(--primary-color);margin-bottom:0.5rem;">Why are teenagers so emotional and impulsive?</h3>
                <p>Because the prefrontal regulatory systems are still being built while the emotional limbic system is fully online — creating an imbalance that resolves through the 20s.</p>
            </div>
        </section>""",
        "faq": [
            {"q": "Does cannabis affect teen brain development?", "a": "Yes significantly — THC disrupts synaptic formation processes during this critical window, with effects on cognition that may last years."},
            {"q": "Can you build back lost synapses?", "a": "Not lost ones, but the brain maintains plasticity throughout life — experience, learning, and therapy can form new compensatory pathways."}
        ]
    },
    192: {
        "title": "Cancer's Hidden Cost: How Tumors Hijack Your Brain and Steal Your Sleep",
        "category": "Health",
        "img_idx": 12,
        "desc": "New research reveals that cancer can disrupt the brain's internal clock almost immediately after it begins — triggering anxiety, insomnia, and immune disruption.",
        "content": """<h2>The Brain-Body Alarm</h2>
        <p>When breast cancer appears in the body, it doesn't wait politely for the medical system to catch up. Researchers have found that tumors begin disrupting the brain's stress-hormone rhythms and internal clock — the circadian system — <strong>almost immediately</strong>, long before diagnosis. This has profound implications for the anxiety, insomnia, and fatigue that many cancer patients experience.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        <h2>The Circadian Disruption</h2>
        <p>In a groundbreaking mouse study, tumors flattened the natural daily rhythm of cortisol — the stress hormone that should peak in the morning and taper toward sleep. When this rhythm is disrupted, the brain loses its ability to properly regulate sleep, immunity, and emotional state. The anxiety and insomnia many cancer patients experience are not simply psychological reactions to the diagnosis — they may be direct biological consequences of the tumor itself.</p>
        <h2>Clinical Implications</h2>
        <p>This research suggests a new target for supportive cancer care: protecting circadian rhythm integrity through light therapy, sleep optimization, and schedule regularity alongside primary treatment. Patients who maintain stronger circadian rhythms during cancer treatment show better immune function and treatment outcomes.</p>
        <section class="faq-section" style="margin-top:4rem;border-top:1px solid rgba(0,0,0,0.1);padding-top:2rem;">
            <h2 style="margin-bottom:2rem;">Frequently Asked Questions</h2>
            <div class="faq-item">
                <h3 style="font-size:1.2rem;color:var(--primary-color);margin-bottom:0.5rem;">Why do cancer patients struggle to sleep?</h3>
                <p>Partly psychological stress, but also direct biological disruption from the tumor to the brain's sleep-regulating hormone systems.</p>
            </div>
        </section>""",
        "faq": [
            {"q": "Does poor sleep worsen cancer?", "a": "Emerging evidence suggests disrupted sleep impairs immune surveillance, potentially affecting cancer progression and treatment efficacy."},
            {"q": "Can light therapy help cancer patients sleep?", "a": "Clinical studies show structured light exposure therapy (morning bright light, evening darkness) significantly improves sleep quality in cancer patients."}
        ]
    },
    193: {
        "title": "The Tryptophan Protein Switch: Why Brain Chemistry Heals or Harms",
        "category": "Neuroscience",
        "img_idx": 8,
        "desc": "A single protein controls whether tryptophan builds your brain or destroys it. Scientists have finally mapped this critical fork in the road.",
        "content": """<h2>Tryptophan: More Than a Turkey Myth</h2>
        <p>Tryptophan is the precursor to serotonin — the neurotransmitter most associated with mood stability. But tryptophan is also the starting point for other biochemical pathways, some of which produce <strong>neurotoxic byproducts</strong> linked to memory loss, inflammation, and depression. A single regulatory protein decides which direction your tryptophan goes — and scientists have just mapped it in unprecedented detail.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        <h2>The Toxic Fork</h2>
        <p>When the brain is under chronic stress or in a state of inflammation, tryptophan is diverted away from the serotonin pathway and into the <em>kynurenine pathway</em>, producing quinolinic acid — a compound that is toxic to neurons. This diversion may explain why chronic stress and physical illness are both powerful risk factors for depression: they hijack brain chemistry at the root.</p>
        <h2>A New Target for Treatment</h2>
        <p>By identifying the protein that controls this switch, researchers have opened a new target for psychiatric drug development. A compound that keeps tryptophan in the serotonin pathway — rather than the neurotoxic kynurenine pathway — could represent a fundamentally new type of antidepressant.</p>
        <section class="faq-section" style="margin-top:4rem;border-top:1px solid rgba(0,0,0,0.1);padding-top:2rem;">
            <h2 style="margin-bottom:2rem;">Frequently Asked Questions</h2>
            <div class="faq-item">
                <h3 style="font-size:1.2rem;color:var(--primary-color);margin-bottom:0.5rem;">Can eating more tryptophan help with depression?</h3>
                <p>Dietary tryptophan does reach the brain, but chronically stressed individuals may benefit more from reducing inflammation (which reroutes tryptophan) than from eating more of it.</p>
            </div>
        </section>""",
        "faq": [
            {"q": "What foods are high in tryptophan?", "a": "Turkey, chicken, eggs, cheese, nuts, seeds, tofu, and oats all contain significant tryptophan."},
            {"q": "What is serotonin and why does it matter?", "a": "A neurotransmitter that regulates mood, sleep, appetite, and social bonding — low serotonin activity is associated with depression and anxiety."}
        ]
    },
    194: {
        "title": "Memory Loss Accelerated: What a Massive Brain Study Just Revealed",
        "category": "Neuroscience",
        "img_idx": 19,
        "desc": "Analyzing thousands of MRI scans, scientists have discovered that age-related memory decline isn't driven by one region — it's a widespread structural cascade.",
        "content": """<h2>The Scale of the Study</h2>
        <p>To understand why some people experience sharp memory decline while others stay sharp into their 80s, researchers pooled brain MRI data and memory test results from thousands of healthy adults across multiple countries. What they found challenges the long-held idea that memory loss centers on one or two specific brain regions like the hippocampus.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        <h2>It's a Network Problem</h2>
        <p>Memory decline, the study found, reflects a cascade of <strong>widespread structural changes across multiple interconnected brain regions</strong>. Think of it less like a single component failing and more like the whole communication network degrading simultaneously. The hippocampus is involved, but so are the prefrontal cortex, the thalamus, and the white matter tracts connecting them.</p>
        <h2>The Inflection Point</h2>
        <p>Critically, the study identified an 'inflection point' — a period typically in the late 50s to early 60s where the rate of structural deterioration appears to accelerate. Before this point, lifestyle interventions may be most effective at slowing decline. Knowing when this window opens is clinically valuable for preventive neurology.</p>
        <section class="faq-section" style="margin-top:4rem;border-top:1px solid rgba(0,0,0,0.1);padding-top:2rem;">
            <h2 style="margin-bottom:2rem;">Frequently Asked Questions</h2>
            <div class="faq-item">
                <h3 style="font-size:1.2rem;color:var(--primary-color);margin-bottom:0.5rem;">At what age does memory start to decline?</h3>
                <p>Measurable structural changes begin in the 30s and 40s, but the rate of decline typically accelerates significantly in the late 50s to early 60s.</p>
            </div>
        </section>""",
        "faq": [
            {"q": "Is memory loss inevitable with aging?", "a": "Some degree is normal, but the rate varies enormously based on lifestyle, genetics, and how mentally active a person remains."},
            {"q": "What's the best way to protect memory as you age?", "a": "Aerobic exercise, quality sleep, social engagement, and cognitively stimulating activities all show strong evidence for slowing age-related memory decline."}
        ]
    },
    195: {
        "title": "Musical Anhedonia: Why Some People Feel Nothing When Music Plays",
        "category": "Cognitive Psychology",
        "img_idx": 9,
        "desc": "Why does music move most people to tears — but leave some completely cold? Neuroscience has finally found the answer in the brain's reward circuitry.",
        "content": """<h2>The Strange Condition</h2>
        <p>Most people find it difficult to imagine being unmoved by music. Yet a small but real portion of the population — perhaps 3–5% — experience what researchers call <em>musical anhedonia</em>: a complete absence of emotional response to music. It's not a hearing problem. It's not a lack of emotion in general. It's a very specific disconnection in the brain, and scientists have now identified exactly what causes it.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        <h2>A Disconnect in the Reward Circuit</h2>
        <p>Brain imaging reveals that in people with musical anhedonia, the auditory cortex and the nucleus accumbens — the brain's 'reward hub' — fail to communicate effectively when music plays. The sound is processed perfectly, but the reward signal never fires. It's the neural equivalent of seeing food but not being hungry.</p>
        <h2>Why It Matters Clinically</h2>
        <p>This discovery has practical implications for therapy. Music therapy is increasingly used in clinical settings for depression, anxiety, dementia, and pain management. Understanding that some patients have a fundamental disconnect in the relevant brain circuitry helps therapists tailor treatment and explains why universal music therapy protocols don't work for everyone.</p>
        <section class="faq-section" style="margin-top:4rem;border-top:1px solid rgba(0,0,0,0.1);padding-top:2rem;">
            <h2 style="margin-bottom:2rem;">Frequently Asked Questions</h2>
            <div class="faq-item">
                <h3 style="font-size:1.2rem;color:var(--primary-color);margin-bottom:0.5rem;">Is musical anhedonia the same as tone deafness?</h3>
                <p>No — musically anhedonic people have normal hearing and can perceive music accurately; they simply don't experience a rewarding emotional response to it.</p>
            </div>
        </section>""",
        "faq": [
            {"q": "Is not liking music a disorder?", "a": "Musical anhedonia is a trait, not a pathology — it exists on a spectrum and doesn't negatively affect general emotional health."},
            {"q": "What do people with musical anhedonia enjoy instead?", "a": "Their reward circuitry is typically intact; they simply connect more strongly to other rewarding experiences like food, social connection, or visual beauty."}
        ]
    },
    196: {
        "title": "Middle Age Is a Mental Health Crisis in America — Here's the Data",
        "category": "Mental Health",
        "img_idx": 4,
        "desc": "Americans in their 40s and 50s report more loneliness, depression and cognitive decline than any previous generation at that age. What's happening?",
        "content": """<h2>The Midlife Reality Check</h2>
        <p>The concept of a 'midlife crisis' has long been treated as a cultural joke. New research suggests it's actually a public health emergency. Adults born in the 1960s and 70s are experiencing dramatically worse mental and physical health outcomes at midlife than their predecessors — reporting significantly higher rates of loneliness, depression, cognitive decline, and physical weakness.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        <h2>Why This Generation Is Struggling</h2>
        <p>Researchers point to a combination of structural factors: economic precarity (student debt, stagnant wages, delayed homeownership), social fragmentation (declining community ties, religious disaffiliation, digital substitution of real social contact), and the cumulative weight of decades of chronic stress exposure. The data shows this is not just a US trend — but the US shows the steepest decline internationally.</p>
        <h2>The Loneliness Epidemic at Its Core</h2>
        <p>Loneliness emerges as the single most consistent predictor of midlife mental health decline. Americans in their 40s and 50s report having fewer close friends and less trusted social contact than any comparable cohort measured in decades of survey data. The Surgeon General's declaration of a loneliness epidemic was directly informed by this kind of data.</p>
        <section class="faq-section" style="margin-top:4rem;border-top:1px solid rgba(0,0,0,0.1);padding-top:2rem;">
            <h2 style="margin-bottom:2rem;">Frequently Asked Questions</h2>
            <div class="faq-item">
                <h3 style="font-size:1.2rem;color:var(--primary-color);margin-bottom:0.5rem;">Is the midlife crisis real?</h3>
                <p>The research increasingly suggests that midlife — particularly in the US — is a genuine period of elevated psychological vulnerability, not just a cliché.</p>
            </div>
        </section>""",
        "faq": [
            {"q": "What causes the midlife mental health dip?", "a": "Research points to a combination of biological changes, accumulated chronic stress, shifting social roles, and shrinking social networks."},
            {"q": "Does midlife mental health improve again?", "a": "Yes — most research shows a 'happiness U-curve' where wellbeing rebounds significantly in the 60s and 70s."}
        ]
    },
    197: {
        "title": "The Blood Test That Could Detect Parkinson's Decades Early",
        "category": "Neuroscience",
        "img_idx": 18,
        "desc": "Swedish and Norwegian scientists have identified biological blood markers that appear up to 20 years before Parkinson's motor symptoms — opening a window for prevention.",
        "content": """<h2>The Diagnosis Problem</h2>
        <p>Parkinson's disease is currently diagnosed when a person already has motor symptoms — tremors, rigidity, slowness of movement. But research shows that by the time these symptoms appear, up to <strong>60–80% of dopamine-producing neurons are already dead</strong>. That's why despite decades of research, we've made little progress in slowing the disease: we arrive too late.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        <h2>The New Blood Biomarkers</h2>
        <p>A Swedish-Norwegian research team has identified a cluster of biological signals in the blood — related to cellular stress responses and DNA repair mechanisms — that appear measurably abnormal up to 20 years before Parkinson's motor symptoms emerge. In a study tracking thousands of individuals over decades, these markers predicted Parkinson's with striking accuracy.</p>
        <h2>The Prevention Window</h2>
        <p>The profound implication: if we can identify these biomarkers in healthy people in their 30s and 40s, we have a two-decade window to intervene — protecting the neurons before they're lost. Promising neuroprotective strategies include aerobic exercise, specific dietary patterns, and potentially early drug interventions once the biomarkers are validated in larger populations.</p>
        <section class="faq-section" style="margin-top:4rem;border-top:1px solid rgba(0,0,0,0.1);padding-top:2rem;">
            <h2 style="margin-bottom:2rem;">Frequently Asked Questions</h2>
            <div class="faq-item">
                <h3 style="font-size:1.2rem;color:var(--primary-color);margin-bottom:0.5rem;">Is this blood test available now?</h3>
                <p>Not yet — it is in the validation phase. Researchers expect clinical availability within 5–7 years if larger trials confirm the findings.</p>
            </div>
        </section>""",
        "faq": [
            {"q": "What causes Parkinson's disease?", "a": "A combination of genetic vulnerability and environmental exposures leading to the progressive death of dopamine-producing neurons."},
            {"q": "Can exercise prevent Parkinson's?", "a": "Multiple studies show vigorous aerobic exercise is associated with significantly lower Parkinson's risk and slower progression in those already diagnosed."}
        ]
    },
    198: {
        "title": "Long COVID Brain Fog: Why American Patients Suffer the Most",
        "category": "Mental Health",
        "img_idx": 3,
        "desc": "A massive 3,100-patient international study found dramatic differences in brain-related long COVID symptoms across countries — and American patients have it worst.",
        "content": """<h2>A Global Divide in Suffering</h2>
        <p>When researchers brought together long COVID data from more than 3,100 patients across multiple countries, they found a striking and unexplained disparity: American patients reported far higher rates of brain fog, depression, and anxiety compared to patients in Europe and Asia with similar COVID infection histories. The gap was not explained by severity of initial illness.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        <h2>The Neurological Dimension</h2>
        <p>Long COVID brain fog is now understood to have a direct neurological component. COVID-19 can trigger micro-strokes, disrupt the blood-brain barrier, and initiate ongoing neuroinflammation. It can also activate dormant viruses like Epstein-Barr. These mechanisms impair processing speed, working memory, and executive function — the cognitive powers underlying focus, planning, and emotional regulation.</p>
        <h2>Why Worse in the US?</h2>
        <p>Researchers hypothesize that pre-existing factors — higher baseline inflammation from metabolic disease, greater healthcare access inequity, higher chronic stress, and less social support — may amplify COVID's neurological damage. The US entered the pandemic with the highest rates of obesity, diabetes, and poor metabolic health in the developed world. These conditions directly amplify COVID's mechanisms of brain injury.</p>
        <section class="faq-section" style="margin-top:4rem;border-top:1px solid rgba(0,0,0,0.1);padding-top:2rem;">
            <h2 style="margin-bottom:2rem;">Frequently Asked Questions</h2>
            <div class="faq-item">
                <h3 style="font-size:1.2rem;color:var(--primary-color);margin-bottom:0.5rem;">How long does COVID brain fog last?</h3>
                <p>For most people, it resolves within 3–6 months. Approximately 15% of long COVID patients have cognitive symptoms lasting more than a year.</p>
            </div>
        </section>""",
        "faq": [
            {"q": "What helps COVID brain fog?", "a": "Current evidence supports pacing, anti-inflammatory lifestyle changes, cognitive rehabilitation, and addressing any underlying sleep disorders."},
            {"q": "Can COVID permanently damage the brain?", "a": "In a minority of severe cases, there is evidence of lasting structural changes, but most cognitive impairment from COVID appears reversible."}
        ]
    },
    199: {
        "title": "Brain-Computer Interface: The Breakthrough Helping Paralyzed Patients Move Again",
        "category": "Neuroscience",
        "img_idx": 6,
        "desc": "Scientists have successfully used EEG-based brain signals to detect movement intent and reroute those signals through spinal cord implants — restoring voluntary movement.",
        "content": """<h2>The Spinal Gap Problem</h2>
        <p>Spinal cord injury severs the signal cable between brain and body. The brain still generates perfect movement commands — those signals just never reach the muscles. For decades, the solution seemed obvious but technically impossible: intercept the brain's signals before the break, and reroute them past the injury. That's now happening, and it's working.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        <h2>How the System Works</h2>
        <p>Researchers fitted participants with EEG (electroencephalogram) caps that record electrical activity from the brain's motor cortex. Machine learning algorithms decode these signals in real time, identifying when the person <em>intends</em> to move. That decoded intention signal is then transmitted wirelessly to a spinal cord stimulator implanted below the injury site, triggering the muscles to move. It's not science fiction — it's running in clinical trials.</p>
        <h2>Current Limitations and Future Potential</h2>
        <p>The current system can detect gross movement intent reliably but struggles with fine motor control (individual finger movements, precise force). Researchers are confident that advances in signal decoding and electrode resolution will solve this progressively. The dream of restoring walking, grasping, and daily independence to paralyzed patients is closer than ever.</p>
        <section class="faq-section" style="margin-top:4rem;border-top:1px solid rgba(0,0,0,0.1);padding-top:2rem;">
            <h2 style="margin-bottom:2rem;">Frequently Asked Questions</h2>
            <div class="faq-item">
                <h3 style="font-size:1.2rem;color:var(--primary-color);margin-bottom:0.5rem;">Is this BCI available for paralysis patients now?</h3>
                <p>Currently in clinical trials. Parallel commercial development is underway at companies like Neuralink, Synchron, and BrainGate.</p>
            </div>
        </section>""",
        "faq": [
            {"q": "What is a brain-computer interface?", "a": "A device that reads brain electrical signals and translates them into commands for computers, prosthetics, or the body's own muscles."},
            {"q": "Does Neuralink work for paralysis?", "a": "Early results from Neuralink's first human trial showed a paralyzed individual controlling a computer cursor using thought alone."}
        ]
    },
    200: {
        "title": "The Brain Glitch Behind Auditory Hallucinations in Schizophrenia",
        "category": "Mental Health",
        "img_idx": 1,
        "desc": "New research reveals that voices heard in schizophrenia stem from a specific neural prediction error — the brain misidentifying its own inner speech as external sound.",
        "content": """<h2>Hearing Voices: A Prediction Error</h2>
        <p>Auditory hallucinations — hearing voices that aren't there — are one of the most distressing and misunderstood symptoms in psychiatry. New research has finally traced the neural mechanism that generates them: a failure of <strong>predictive processing</strong> in the auditory cortex.</p>
        <p>Normally, when we think in words or produce inner speech, the brain generates a 'corollary discharge' signal — essentially a prediction that says 'this sound is coming from you.' This prediction suppresses the auditory cortex's response to our own inner voice. But in people who hear voices, this suppression fails: the brain's own inner speech is treated as an unexpected external signal — a voice from somewhere else.</p>
        <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
        <h2>The Evidence</h2>
        <p>Using high-resolution neuroimaging during inner speech tasks, researchers could directly observe this misfiring in participants with schizophrenia. Brain activity ramped up rather than being suppressed when they produced inner speech — exactly what you'd expect if the brain was treating its own voice as an alien intrusion.</p>
        <h2>New Treatment Targets</h2>
        <p>This precise mechanism gives pharmacologists and neurostimulation researchers a specific target: the predictive circuitry between the prefrontal cortex and auditory areas. Treatments that specifically strengthen corollary discharge signaling could quiet the voices more selectively than current antipsychotics, which broadly suppress dopamine across the whole brain.</p>
        <section class="faq-section" style="margin-top:4rem;border-top:1px solid rgba(0,0,0,0.1);padding-top:2rem;">
            <h2 style="margin-bottom:2rem;">Frequently Asked Questions</h2>
            <div class="faq-item">
                <h3 style="font-size:1.2rem;color:var(--primary-color);margin-bottom:0.5rem;">Do all schizophrenia patients hear voices?</h3>
                <p>About 70% of people with schizophrenia experience auditory hallucinations, making it the most common symptom, but not universal.</p>
            </div>
        </section>""",
        "faq": [
            {"q": "Why do people with schizophrenia hear voices?", "a": "Due to a misfiring in predictive processing circuits — the brain fails to recognize its own inner speech as self-generated."},
            {"q": "Can voices in schizophrenia be treated?", "a": "Antipsychotic medications reduce voices in ~70% of patients; cognitive therapies help people change their relationship to the voices."}
        ]
    }
}

def generate_html(art_id, data):
    date_str = datetime.datetime.now().strftime("%B %d, %Y")
    img_id = VERIFIED_IMGS[data["img_idx"]]
    img_full = f"https://images.unsplash.com/photo-{img_id}?auto=format&fit=crop&q=80&w=1200"
    
    faq_items = ",\n    ".join([
        f'{{"@type": "Question", "name": "{f["q"]}", "acceptedAnswer": {{"@type": "Answer", "text": "{f["a"]}"}}}}'
        for f in data["faq"]
    ])

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{data["title"]} | Mind &amp; Balance</title>
    <meta name="description" content="{data["desc"]}">
    <link rel="stylesheet" href="css/style.css">
    <link rel="icon" type="image/svg+xml" href="images/favicon.svg">
    <meta property="og:title" content="{data["title"]} | Mind &amp; Balance">
    <meta property="og:description" content="{data["desc"]}">
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://leafanoo.com/article{art_id}.html">
    <meta property="og:image" content="{img_full}">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{data["title"]}">
    <meta name="twitter:image" content="{img_full}">
    <link rel="canonical" href="https://leafanoo.com/article{art_id}.html">
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [{faq_items}]
    }}
    </script>
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "{data["title"]}",
      "description": "{data["desc"]}",
      "image": "{img_full}",
      "datePublished": "{datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S+00:00")}",
      "author": {{"@type": "Organization", "name": "Mind & Balance"}},
      "publisher": {{"@type": "Organization", "name": "Mind & Balance", "logo": {{"@type": "ImageObject", "url": "https://leafanoo.com/images/favicon.svg"}}}}
    }}
    </script>
    <script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);}})(window,document,'script','dataLayer','GTM-MWJD24QX');</script>
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
            <span class="card-category" style="display:block;margin-bottom:1rem;">{data["category"]}</span>
            <h1 style="font-size:3rem;max-width:800px;margin:0 auto;">{data["title"]}</h1>
            <div class="article-meta">
                <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&q=80&w=80&h=80" alt="Mind & Balance Editorial Team">
                <span>By Mind &amp; Balance Editorial Team</span>
                <span>•</span><span>{date_str}</span><span>•</span><span>6 min read</span>
            </div>
        </div>
    </div>

    <div class="ad-container ad-leaderboard hidden delay-1"></div>

    <div class="article-layout">
        <main class="article-body hidden delay-2">
            <img src="{img_full}" alt="{data["title"]}" style="width:100%;border-radius:12px;margin-bottom:2rem;" loading="lazy">
            {data["content"]}
        </main>
        <aside class="article-sidebar hidden delay-3">
            <div class="sticky-sidebar">
                <div class="ad-container ad-sidebar" style="height:600px;margin-top:0;"></div>
            </div>
        </aside>
    </div>

    <div class="container disclaimer-banner" style="padding:1rem 0;font-size:0.85rem;color:var(--text-color);border-top:1px solid rgba(0,0,0,0.1);text-align:center;opacity:0.8;margin-top:2rem;">
        <p><strong>Medical Disclaimer:</strong> The content on Mind &amp; Balance is for informational and educational purposes only and is not a substitute for professional psychological or medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified mental health provider with any questions you may have regarding a medical condition.</p>
    </div>

    <footer style="background:var(--text-primary);color:white;padding:4rem 0;margin-top:4rem;text-align:center;">
        <div class="container">
            <p>&copy; 2026 Mind &amp; Balance. All rights reserved.</p>
            <div style="margin-top:1rem;">
                <a href="index.html" style="color:#ccc;margin:0 10px;text-decoration:none;">Home</a>
                <a href="about.html" style="color:#ccc;margin:0 10px;text-decoration:none;">About</a>
                <a href="contact.html" style="color:#ccc;margin:0 10px;text-decoration:none;">Contact</a>
                <a href="privacy-policy.html" style="color:#ccc;margin:0 10px;text-decoration:none;">Privacy Policy</a>
                <a href="terms.html" style="color:#ccc;margin:0 10px;text-decoration:none;">Terms</a>
            </div>
        </div>
    </footer>
    <script src="js/main.js"></script>
</body>
</html>'''

def inject_index_cards(new_cards_html):
    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    marker = '</div>\n    </section>\n    <footer'
    if marker in content:
        content = content.replace(marker, new_cards_html + marker)
    else:
        # fallback: inject before closing section tag
        content = content.replace('</section>\n    <footer', new_cards_html + '</section>\n    <footer')
    with open(INDEX_PATH, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    new_cards = ""
    new_sitemap = ""

    for art_id, data in ARTICLES.items():
        # Generate article file
        html = generate_html(art_id, data)
        path = os.path.join(BASE_DIR, f"article{art_id}.html")
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Created article{art_id}.html")

        img_id = VERIFIED_IMGS[data["img_idx"]]
        card_url = f"https://images.unsplash.com/photo-{img_id}?auto=format&fit=crop&q=80&w=400"

        new_cards += f'''
            <article class="card hidden delay-1">
                <div class="card-img" style="background-image: url('{card_url}');"></div>
                <div class="card-content">
                    <span class="card-category">{data["category"]}</span>
                    <h3 class="card-title">{data["title"]}</h3>
                    <p class="card-excerpt">{data["desc"]}</p>
                    <a href="article{art_id}.html" class="card-link">Read More &rarr;</a>
                </div>
            </article>
'''

        new_sitemap += f"""    <url>
        <loc>https://leafanoo.com/article{art_id}.html</loc>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>
"""

    # Inject cards
    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        idx = f.read()

    if 'article181.html' in idx:
        print("Batch 10 already in index.html — skipping card injection.")
    else:
        # Find last article card closing tag and append after it
        last_pos = idx.rfind('</article>')
        if last_pos != -1:
            idx = idx[:last_pos + len('</article>')] + '\n' + new_cards + idx[last_pos + len('</article>'):]
            with open(INDEX_PATH, 'w', encoding='utf-8') as f:
                f.write(idx)
            print("✅ Injected 20 cards into index.html")

    # Update sitemap
    with open(SITEMAP_PATH, 'r', encoding='utf-8') as f:
        sitemap = f.read()
    if 'article181.html' not in sitemap:
        sitemap = sitemap.replace('</urlset>', new_sitemap + '</urlset>')
        with open(SITEMAP_PATH, 'w', encoding='utf-8') as f:
            f.write(sitemap)
        print("✅ Updated sitemap.xml")

    print(f"\n🎉 Batch 10 complete — 20 articles created (181–200).")

if __name__ == "__main__":
    main()
