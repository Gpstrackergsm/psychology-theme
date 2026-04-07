import os
import re

BASE_DIR = "/Users/khalidaitelmaati/Desktop/scrapy-master/psychology-theme-main"

articles = {
    36: {
        "intro_expansion": """<p>Ecopsychology, the study of the psychological connection between humans and the natural world, reveals that understanding nature's survival mechanisms can profoundly impact our own mental resilience. When we observe the extraordinary defenses of plants, our brains subconsciously parallel these mechanisms with our own psychological boundaries. From chemical defenses to physical barriers, the resilience of flora offers a living metaphor for healthy emotional boundaries.</p>
<p>In modern therapy, drawing parallels between human psychology and natural ecology is a growing trend. We often expect ourselves to be completely defenseless and open at all times, a recipe for emotional burnout. However, nature shows us that boundaries—sometimes sharp, sometimes invisible—are a fundamental requirement for growth and survival. By studying how plants protect their energy and resources, we allow our minds to accept that saying 'no' and protecting our internal peace is a completely natural phenomenon.</p>
<p>Furthermore, exposure to these fascinating natural concepts has been scientifically proven to act as a 'cognitive reset'. When your brain focuses on complex natural phenomena, it interrupts cycles of anxious rumination.</p>""",
        "takeaways": """<li><strong>Boundaries are Natural:</strong> Just as plants have physical and chemical boundaries to protect their growth, human psychological boundaries are essential for emotional survival.</li>
<li><strong>Cognitive Interruption:</strong> Engaging with complex botanical facts interrupts anxiety loops in the brain, offering a natural form of grounding.</li>
<li><strong>Adaptive Resilience:</strong> Plants adapt their defenses to specific environmental threats, offering a psychological metaphor for adapting our coping mechanisms to current stressors rather than relying on outdated habits.</li>"""
    },
    37: {
        "intro_expansion": """<p>The intersection of nutritional psychology and botany is a rapidly expanding field. What we eat directly influences our neurochemistry, and the visual aesthetics of our food play a massive psychological role in satiety and mood regulation. Introducing vibrant, edible flowers into your diet is not just a culinary trick; it is a proven method to engage the brain's visual reward centers, triggering dopamine release before the food even reaches your mouth.</p>
<p>Psychologically, breaking dietary monotony with surprising, natural elements like edible flowers disrupts the 'hedonic treadmill' of eating. When meals become a vibrant visual experience, we transition from mindless consumption to mindful eating. This heightened state of sensory awareness reduces binge eating behaviors, lowers cortisol levels during meals, and improves overall digestion through the parasympathetic nervous system.</p>
<p>Moreover, many edible flowers contain unique flavonoids and antioxidants that directly pass the blood-brain barrier, providing neuroprotective benefits that lower the long-term risk of cognitive decline.</p>""",
        "takeaways": """<li><strong>Visual Dopamine:</strong> The bright colors of edible flowers trigger immediate dopamine responses, elevating mood before eating begins.</li>
<li><strong>Mindful Eating Trigger:</strong> Surprising aesthetic elements in food force the brain out of autopilot, encouraging mindful, present-moment consumption.</li>
<li><strong>Neuroprotective Flavonoids:</strong> Beyond aesthetics, the physical compounds in these natural additions directly support brain health and emotional regulation.</li>"""
    },
    38: {
        "intro_expansion": """<p>Human beings possess a deep-seated psychological need for awe. Awe is an emotion characterized by the perception of vastness and a need to accommodate new information. Encountering record-breaking plants—whether it is the oldest, the largest, or the most resilient—triggers this exact psychological state. Research shows that experiencing awe dramatically reduces markers of systemic inflammation and diminishes the prominence of the 'self', leading to reduced anxiety and greater prosocial behavior.</p>
<p>Therapists frequently prescribe 'awe walks' in nature to combat depressive symptoms. When we learn about a tree that has survived for 5,000 years or a plant that can resurrect itself from complete dehydration, it forces a cognitive perspective shift. Our personal stressors, which feel overwhelmingly large to our ego, are suddenly shrunk when compared to the vast, resilient timeline of the botanical world.</p>
<p>This perspective shift is essential for cognitive flexibility. By marveling at these botanical extremes, we subconsciously train our brains to recognize that 'impossible' boundaries can be broken, fostering a growth mindset in our personal lives.</p>""",
        "takeaways": """<li><strong>The Psychology of Awe:</strong> Learning about extreme natural phenomena triggers the emotion of awe, which is scientifically proven to reduce anxiety and stress.</li>
<li><strong>Perspective Shifting:</strong> Observing ancient or massive natural entities shrinks the psychological weight of daily human stressors.</li>
<li><strong>Cognitive Flexibility:</strong> Witnessing nature break perceived boundaries inspires a subconscious 'growth mindset' within our own problem-solving frameworks.</li>"""
    }
}

for art_id, content in articles.items():
    filepath = os.path.join(BASE_DIR, f"article{art_id}.html")
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Replace expansion placeholder
    html = re.sub(
        r'<p>\[PLACEHOLDER: Deepen the article here based on the excerpt\. Write 5 paragraphs expanding on the psychological implications\.\]</p>',
        content["intro_expansion"],
        html
    )
    
    # Replace takeaways
    takeaway_pattern = r'<ul>\s*<li>\[Write takeaway 1\]</li>\s*<li>\[Write takeaway 2\]</li>\s*<li>\[Write takeaway 3\]</li>\s*</ul>'
    html = re.sub(takeaway_pattern, f'<ul>\n{content["takeaways"]}\n</ul>', html)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Filled article{art_id}.html")
