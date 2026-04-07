import os
import re

BASE_DIR = "/Users/khalidaitelmaati/Desktop/scrapy-master/psychology-theme-main"

expansions = {
    36: """<main class="article-body hidden delay-2">
            <h2>Introduction</h2>
            <p>When most people hear the word "narcissist," they picture someone who is loud, arrogant, and constantly demanding the center of attention. They imagine the grandiose type—the CEO who demands absolute loyalty, or the relative who hijacks every conversation to brag about their achievements. However, psychology recognizes a far more insidious and deeply destructive subtype: the <strong>Covert Narcissist</strong> (also known as a vulnerable narcissist).</p>
            <p>Covert narcissists possess the exact same underlying pathology as their loud counterparts—a profound lack of empathy, a desperate need for external admiration, and an internalized sense of superiority. But instead of hiding their insecurities behind a mask of bravado, they hide them behind a mask of victimhood, introversion, and passive-aggression. Because they do not fit the classic cinematic stereotype, they are incredibly difficult to spot. You might spend years feeling perpetually guilty, confused, or exhausted in the relationship without ever understanding why.</p>
            
            <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
            
            <h2>1. The Perpetual Victim Narrative</h2>
            <p>The most defining characteristic of a covert narcissist is their complete inability to take accountability, which manifests as a perpetual victim narrative. No matter what happens, they are never at fault. If they make a mistake at work, their boss is out to get them. If your relationship is failing, it is because you are not supportive enough.</p>
            <p>Psychologically, taking responsibility requires a solid sense of self-worth—something narcissists entirely lack. To protect their fragile ego from the 'injury' of being wrong, their brains automatically rewrite the narrative so that they are the innocent party. This forces the people around them into the exhausting role of constantly validating their pain, apologizing for things they did not do, and walking on eggshells.</p>

            <h2>2. Passive-Aggressive Hostility</h2>
            <p>Grandiose narcissists get angry and yell when their ego is threatened. Covert narcissists, however, view direct conflict as too vulnerable and exposing. Instead, they weaponize <em>passive-aggression</em>. This looks like giving you the silent treatment for three days without explaining why, making subtle backhanded compliments ("I wish I was brave enough to wear something that unflattering"), or deliberately 'forgetting' to do something important for you.</p>
            <p>This is a particularly destructive form of psychological abuse. Because their hostility is constantly wrapped in plausible deniability ("I was just joking, why are you so sensitive?"), you begin to question your own perception of reality—a classic form of gaslighting. Over time, this erodes your self-trust and mental health.</p>

            <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>

            <h2>3. Hypersensitivity to Criticism</h2>
            <p>While everyone dislikes criticism, covert narcissists experience it as a devastating psychological injury. Even the mildest, most respectful constructive feedback—such as asking them to move their shoes from the hallway—can trigger an intense emotional reaction. But instead of exploding in rage, they often implode. They will sulk aggressively, withdraw affection, or launch into a self-deprecating monologue ("I guess I'm just the worst partner in the world then"), forcing <em>you</em> to comfort <em>them</em> for a boundary you tried to set.</p>
            
            <h2>4. Weaponized Incompetence</h2>
            <p>Weaponized incompetence is a manipulation tactic where a person deliberately performs a task poorly so that they will not be asked to do it again. A covert narcissist uses this to maintain their sense of entitlement without looking outwardly demanding. By pretending they simply "don't know how" to load the dishwasher correctly or manage the finances, they force you into a parental, caretaking role, absorbing all of your energy while maintaining their facade of innocence and fragility.</p>

            <h2>How to Protect Your Peace</h2>
            <p>If you recognize these signs in a partner, parent, or colleague, the clinical recommendation is clear: boundaries. You cannot love a covert narcissist into having empathy. Therapy can only work if a person takes accountability for their actions—the one thing a covert narcissist is wired to avoid. Protect your reality by keeping a journal, lean on a strong support system outside the relationship, and utilize the 'Grey Rock' method—giving them zero emotional reaction to their passive-aggressive provocations until they seek supply elsewhere.</p>
        </main>""",
    37: """<main class="article-body hidden delay-2">
            <h2>Introduction</h2>
            <p>It is 2 AM. The house is completely silent, your body is physically exhausted, and you have to be awake for work in four hours. Yet, the moment your head hit the pillow, your brain decided this was the perfect opportunity to review an embarrassing conversation from 2018, meticulously calculate your financial anxieties, and catastrophize about an upcoming meeting that might go wrong. If this sounds intimately familiar, you are suffering from the deeply frustrating psychological cycle of nighttime overthinking and highly functioning anxiety.</p>
            <p>For decades, people were told to "just relax" or count sheep, but modern neuroscience reveals that overthinking is not a conscious choice. It is a biological survival mechanism that is catastrophically misfiring. Understanding exactly why your brain tortures you at night is the first, vital step to dismantling the anxiety loop and finally getting the deep, restorative sleep you deserve.</p>
            
            <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
            
            <h2>1. The Default Mode Network (DMN) Activation</h2>
            <p>To understand why this happens specifically at night, we have to look at brain topography. When you are distracted during the day—working, watching TikTok, talking to friends—your brain is engaged in the 'Task-Positive Network'. But the moment the lights go out and distractions disappear, your brain switches to its idle state, known as the <em>Default Mode Network (DMN)</em>.</p>
            <p>The DMN is responsible for self-reflection, planning for the future, and analyzing the past. For a calm brain, the DMN might trigger a daydream. But for a highly stressed or anxious brain, the DMN acts like a hyper-vigilant security guard. The lack of external stimuli is interpreted as an opportunity to desperately scan for unresolved threats. Because there are no immediate physical threats in your bedroom, it latches onto social and emotional threats instead.</p>

            <h2>2. The Illusion of Control and "Worry as Work"</h2>
            <p>One of the most profound psychological discoveries about chronic overthinkers is that they subconsciously believe that worrying is a form of productive work. Deep down, your brain is convinced that if you analyze a potential future disaster long enough from every possible angle, you will somehow prevent it from happening.</p>
            <p>This creates the <em>Illusion of Control</em>. Ruminating over your finances at 3 AM does not generate more money, but the physical act of mental spinning makes the brain feel like it is "doing something" about the danger. Letting go and going to sleep feels terrifying to the anxious brain because it registers as dropping your guard in a warzone.</p>

            <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>

            <h2>3. The Negativity Bias Expansion</h2>
            <p>Evolutionarily speaking, human beings have a powerful 'Negativity Bias'. Our ancestors who remembered the location of the poisonous berries survived, while those who focused on the beautiful sunset did not. Your brain is a descendant of those hyper-vigilant survivors, meaning it is hardwired to attach like velcro to negative thoughts and slide like Teflon past positive ones.</p>
            <p>At night, when the prefrontal cortex (the logical part of your brain) is tired, this negativity bias goes into overdrive. A neutral interaction with your boss earlier that day is suddenly reinterpreted by your fatigued brain as a sign you are going to be fired. The threat feels completely real, triggering a cortisol and adrenaline release that physically prevents your body from entering REM sleep.</p>

            <h2>Clinically Proven Strategies to Break the Loop</h2>
            <p>Telling an overthinking brain to "stop thinking" is like trying to put out a fire with gasoline. Instead, therapists recommend specific cognitive interrupters:</p>
            <ul>
                <li><strong>The Brain Dump:</strong> An hour before bed, physically write down every single uncompleted task and worry on a piece of paper. This externalizes the 'threats', tricking the DMN into believing they have been handled and no longer need to be actively monitored.</li>
                <li><strong>Cognitive Defusion:</strong> When the anxious thoughts start spinning, do not fight them. Instead, distance yourself by adding a prefix. Change "I am going to fail my presentation" to "I am noticing that my brain is having the thought that I am going to fail." It removes the emotional sting of the thought.</li>
                <li><strong>Sensory Grounding (The 4-7-8 Breath):</strong> Because anxiety lives in the future, you must force the brain back into the present body. Breathe in for 4 seconds, hold for 7, and exhale heavily for 8. This specific rhythm manually engages the parasympathetic nervous system, chemically lowering your heart rate and forcing the anxiety loop to break.</li>
            </ul>
        </main>""",
    38: """<main class="article-body hidden delay-2">
            <h2>Introduction</h2>
            <p>If you find it increasingly impossible to read a book for ten minutes without impulsively reaching for your phone, to sit in silence without tossing on a podcast, or to finish a deep work project without checking your notifications, you do not have a discipline problem. You have a neurochemical problem. We belong to the first generation in human history living in an attention economy—a digital society architected by thousands of software engineers whose exclusive job is to hijack your brain's evolutionary reward pathways.</p>
            <p>The core of this hijacking centers around one specific neurotransmitter: Dopamine. For years, pop psychology misunderstood dopamine as the brain's "pleasure" or "happiness" chemical. In reality, modern neuroscience has shown us that dopamine is the "motivation and seeking" chemical. It is the evolutionary fuel that makes you pursue a goal, whether that is hunting for food, studying for a degree, or, fatally, scrolling for the next interesting video.</p>
            <p>When you understand how your dopamine baseline has been sabotaged, the concept of a 'Dopamine Detox' transforms from a trendy silicon valley buzzword into a vital, scientifically backed survival mechanism for reclaiming your focus and your life.</p>
            
            <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>
            
            <h2>1. Variable Reward Schedules and The Slot Machine Brain</h2>
            <p>Why is social media so much more addictive than reading a textbook? It comes down to a psychological concept called intermittent reinforcement, or the Variable Reward Schedule. When you pull to refresh your Instagram feed, you do not know if you will see something boring (no reward) or a funny video/message from a friend (high reward). This unpredictability causes a massive, unnatural spike in dopamine anticipation.</p>
            <p>This is the exact same psychological mechanism used in casino slot machines. Your smartphone is a slot machine sitting in your pocket. By constantly flooding your brain with these cheap, effortless, artificially high dopamine spikes all day, your brain's receptors begin to down-regulate (reduce in sensitivity) to protect themselves from the overload.</p>

            <h2>2. The Collapse of Your Dopamine Baseline</h2>
            <p>Once your dopamine receptors down-regulate, your baseline tolerance skyrockets. This is where the true damage occurs. Suddenly, the amount of dopamine released by "normal" activities—like going for a walk, having a deep conversation with a friend, or doing the hard work required to build a business—pales in comparison to the artificial spikes generated by your smartphone.</p>
            <p>Because these healthy activities cannot compete neurochemically, they begin to feel agonizingly boring. You find yourself lacking the motivation to pursue long-term goals simply because the neurological reward is too delayed and too weak compared to the immediate hit of checking TikTok. Chronic procrastination is rarely a character flaw; it is a symptom of a blown-out dopamine baseline.</p>

            <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>

            <h2>3. The Science Behind the Dopamine Detox</h2>
            <p>A Dopamine Detox (or Dopamine Fast) is a cognitive behavioral protocol designed to starve the brain of cheap, hyper-stimulating inputs, allowing the down-regulated dopamine receptors time to heal and re-sensitize. By removing the artificial spikes, you intentionally lower your tolerance, making hard work and subtle, delayed rewards feel satisfying and motivating once again.</p>

            <h2>How to Execute a Proper Dopamine Detox</h2>
            <p>A true detox is not about never experiencing joy, but rather about severing the connection between boredom and instant digital gratification. Here is the clinical protocol:</p>
            <ul>
                <li><strong>The 24-Hour Hard Reset:</strong> For one full day (typically a Sunday), you abstain entirely from screens, highly processed sugary foods, video games, and fast-paced music. You are allowed to read physical books, write, walk in nature, and talk to people face-to-face. The intense boredom you feel in the first 4 hours is the literal feeling of withdrawal. Push through it.</li>
                <li><strong>The "Untethering" Rule:</strong> Stop bringing outside stimulation into the bathroom, the shower, or the commute. Allow your brain to experience baseline boredom. Boredom is the evolutionary precursor to creativity; if you never allow yourself to be bored, you will never have an original thought.</li>
                <li><strong>Grayscale Mode:</strong> Turn your smartphone screen permanently to black and white (usually found in Accessibility settings). You will be shocked by how significantly the removal of bright, saturated colors reduces your subconscious urge to aimlessly tap on apps.</li>
            </ul>
        </main>"""
}

for art_id, new_main in expansions.items():
    filepath = os.path.join(BASE_DIR, f"article{art_id}.html")
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Use regex to replace everything from <main> to </main>
    pattern = r'<main class="article-body hidden delay-2">.*?</main>'
    # re.DOTALL makes . match newlines
    html = re.sub(pattern, new_main, html, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        
print("Expansion complete.")
