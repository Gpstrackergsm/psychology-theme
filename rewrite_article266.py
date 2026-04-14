import re

with open('article266.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update Title and Meta Description
html = re.sub(
    r'<title>.*?</title>',
    r'<title>Dog Anxiety: Symptoms, Causes & How to Calm Your Pet | Mind &amp; Balance</title>',
    html
)
html = re.sub(
    r'<meta content="Why do dogs get anxious\?.*?" name="description"/>',
    r'<meta content="Is your dog pacing, panting, or destroying furniture? Learn the hidden causes of dog anxiety, common symptoms, and how to calm an anxious dog using science." name="description"/>',
    html
)

# Update H1 and Hero Text
html = re.sub(
    r'<h1.*?>Canine Cognition</h1>',
    r'<h1 style="font-size: 3.5rem; margin: 1.5rem 0;">Dog Anxiety</h1>',
    html
)
html = re.sub(
    r'<p style="font-size: 1.2rem; max-width: 700px; margin: 0 auto; opacity: 0.9;">The Deeper Science Behind Dog Anxiety and Emotional Contagion</p>',
    r'<p style="font-size: 1.2rem; max-width: 700px; margin: 0 auto; opacity: 0.9;">Symptoms, Hidden Causes, and How to Calm an Anxious Pet</p>',
    html
)

# Rewrite Body Content completely, retaining citations
new_body = """
<div class="eeat-badge" style="background: #fff3e0; color: #e65100; padding: 10px 20px; border-radius: 8px; display: inline-block; margin-bottom: 2rem; font-weight: 600;">✓ Veterinary Psychology Insight</div>
<p class="lead" style="font-size:1.2rem;color:#444;line-height:1.7;">Does your dog panic when you leave the house? Do they tremble during thunderstorms or pace restlessly for no apparent reason? <strong>Dog anxiety</strong> is a complex, neurobiological stress response that affects millions of pets, but it is highly treatable once you understand the underlying causes.</p>

<p>In this guide, you will learn exactly what triggers dog anxiety, how to spot the early warning signs, and evidence-based treatments to help your dog feel safe and secure.</p>

<img alt="Anxious dog looking stressed" loading="lazy" src="https://images.unsplash.com/photo-1518717758536-85ae29035b6d?auto=format&amp;fit=crop&amp;q=80&amp;w=1200&amp;fm=webp" style="width: 100%; border-radius: 12px; margin: 2rem 0;"/>

<h2>What is Dog Anxiety?</h2>
<p>Just like humans, dogs possess a highly developed amygdala—the brain's emotional threat-detection center. <strong>Dog anxiety</strong> occurs when a dog anticipates danger (whether real or imagined) and enters a state of persistent physiological arousal. This isn't just "bad behavior"; it is a neurological survival mechanism gone into overdrive.</p>

<h2>Dog Anxiety Symptoms</h2>
<p>Unlike humans, dogs cannot tell us when they are experiencing a panic attack. Instead, the signs of dog anxiety manifest physically and behaviorally. Watch for these common symptoms:</p>
<ul style="line-height:1.8; margin-bottom:2rem;">
  <li><strong>Vocalization:</strong> Excessive barking, whining, or howling when left alone.</li>
  <li><strong>Body Language:</strong> Pacing, trembling, tucked tail, flattened ears, or lip-licking.</li>
  <li><strong>Destructive Behavior:</strong> Chewing furniture, digging at doors, or destroying objects.</li>
  <li><strong>Physiological Signs:</strong> Excessive panting, drooling, or sudden bathroom accidents in a house-trained dog.</li>
</ul>

<h2>Causes of Dog Anxiety</h2>
<p>Understanding <em>why</em> your dog is stressed is the first step toward treating dog anxiety. The most common causes include:</p>
<ul style="line-height:1.8; margin-bottom:2rem;">
  <li><strong>Fear-Related Anxiety:</strong> Triggered by loud noises (fireworks, thunderstorms), strange people, or novel environments.</li>
  <li><strong>Age-Related Anxiety:</strong> Older dogs can develop Cognitive Dysfunction Syndrome (canine dementia), leading to confusion and anxiety.</li>
  <li><strong>Emotional Contagion:</strong> Dogs are masters of reading human cortisol levels. Studies show that a dog's long-term stress tightly mirrors their owner's stress levels. If you are highly anxious, your dog is likely absorbing that tension.</li>
</ul>

<section class="neuro-depth" style="background: #fdfae7; padding: 2.5rem; border-radius: 12px; margin: 3rem 0; border-left: 5px solid #f9a825;">
<h3>🧠 Dog Separation Anxiety</h3>
<p><strong>Dog separation anxiety</strong> is the most severe and common form of canine stress. It is a dysfunctional neuro-endocrine response where the dog's brain remains in constant hyper-arousal when separated from their primary attachment figure. Symptoms usually begin within 15 to 45 minutes of the owner's departure and can lead to severe structural damage to the home or self-injury by the dog.</p>
</section>

<h2>How to Calm an Anxious Dog & Treatment Options</h2>
<p>Treating dog anxiety requires patience and consistency. Here are the most effective, science-backed methods for providing dog anxiety relief:</p>

<h3>1. Counterconditioning and Desensitization</h3>
<p>This psychological technique involves exposing your dog to the source of their anxiety in very small, non-threatening doses, and rewarding them. Over time, you slowly increase the exposure, retraining the dog's amygdala to stop associating the trigger with fear.</p>

<h3>2. Exercise and Routine Predictability</h3>
<p>A tired dog is a calm dog. Adequate physical and mental stimulation (like puzzle toys) reduces baseline cortisol. Furthermore, predictability is the enemy of anxiety; establishing strict routines for walking and feeding makes the world feel safe and structured to a dog.</p>

<h3>3. Natural Remedies and Aids</h3>
<p>Many owners ask for natural remedies for dog anxiety. Calming coats (like the Thundershirt) apply gentle, constant pressure that simulates a hug, providing a calming sensory effect. Pheromone diffusers (like Adaptil) release synthetic versions of the calming message mother dogs emit to their puppies.</p>

<h3>4. Veterinary Interventions</h3>
<p>For severe cases—especially severe dog separation anxiety—speak to your veterinarian. They may prescribe FDA-approved canine anxiety medications (such as fluoxetine or clomipramine) to help lower the dog's panic threshold so that behavioral training can finally take effect.</p>

<section class="faq-section" style="margin-top: 4rem; border-top: 1px solid #eee; padding-top: 2rem;">
<h2>Frequently Asked Questions</h2>
<div class="faq-item" style="margin-bottom: 2rem;">
<h3 style="color: #f9a825;">Can I give my dog human anxiety medication?</h3>
<p><strong>NEVER</strong> administer human medication to pets without veterinary supervision. While dogs may be prescribed similar drugs by a vet, human dosages and metabolic pathways are completely different and can be fatal.</p>
</div>
<div class="faq-item">
<h3 style="color: #f9a825;">How to calm an anxious dog in the car?</h3>
<p>To treat car anxiety in dogs, start by feeding them near the car, then inside the parked car. Gradually take extremely short, positive trips (e.g., driving down the driveway and back) ending with high-value treats. Consider a pet seatbelt or crate to make them feel geographically secure.</p>
</div>
</section>
"""

# Replace body content between the eeat-badge and the next-step-box
html = re.sub(
    r'<div class="eeat-badge".*?</section>\s*<!-- Phase 8: Smart Recommendation -->',
    new_body + '\n<!-- Phase 8: Smart Recommendation -->',
    html,
    flags=re.DOTALL
)

with open('article266.html', 'w', encoding='utf-8') as f:
    f.write(html)
