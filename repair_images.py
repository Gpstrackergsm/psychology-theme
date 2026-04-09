#!/usr/bin/env python3
"""
Definitive Image Repair — replaces ALL article card backgrounds in index.html
and updates og/twitter/schema images in each article file.
Uses only VERIFIED HTTP-200 Unsplash photo IDs.
"""

import os, re

BASE_DIR = "/Users/khalidaitelmaati/Desktop/scrapy-master/psychology-theme-main"
INDEX_PATH = os.path.join(BASE_DIR, "index.html")

# 50 Verified working numeric Unsplash IDs
VERIFIED_POOL = [
    "1454165804606-c3d57bc86b40",  # writing desk
    "1455390582262-044cdead277a",  # brain abstract blue
    "1466471340190-98259d5a77c0",  # mushroom forest
    "1471864190281-a93a3070b6de",  # pills / health
    "1473641262803-ec5e10080644",  # couple outdoors
    "1484480974693-6ca0a78fb36b",  # alarm / time
    "1490730141103-6cac27aaab94",  # salad / gut health
    "1493132630797-4c5837dec5f0",  # mirror reflection / identity
    "1493836512294-502baa1986e2",  # meditation / calm
    "1494790108377-be9c29b29330",  # smiling woman portrait
    "1499209974431-9dddcece7f88",  # person deep in thought
    "1499750310107-5fef283666bb",  # laptop / productivity
    "1506126613408-eca07ce68773",  # yoga / mindfulness
    "1506784983877-45594efa4cbe",  # notebook journaling
    "1507003211169-0a1dd7228f2d",  # man portrait serious
    "1507413245164-6160d8298b31",  # CT brain scan
    "1508214751196-bcfd4ca60f91",  # woman in sunlight / joy
    "1508739773434-c26b3d09e071",  # DNA helix / genetics
    "1510832198440-a52376950479",  # hands / struggle / addiction
    "1512411546253-24151c727a81",  # food brain / appetite neuroscience
    "1512621776951-a57141f2eefd",  # healthy food bowl
    "1515377905703-c4788e51af15",  # laughing teens
    "1516251193007-45ef944ab0c6",  # sad alone silhouette
    "1516302752625-fcc3c50ae61f",  # broken relationship / chairs
    "1516589174184-c685ca33d2b0",  # couple holding hands
    "1517245386807-bb43f82c33c4",  # man laptop / career stress
    "1518133910546-b6c2fb7d79e3",  # abstract geometric / psych
    "1520206183501-b80af970d7eb",  # woman sleeping / rest
    "1521790797524-b2497295b8a0",  # father holding newborn
    "1522071820081-009f0129c71c",  # team meeting / collaboration
    "1522202176988-66273c2fd55f",  # student studying books
    "1526951521990-620dc14c214b",  # ocean / environment / plastic
    "1529156069898-49953e39b3ac",  # family in park
    "1530210124550-912dc1381cb8",  # dark mood silhouette / depression
    "1531983412531-1f49a365ffed",  # brain MRI imaging  
    "1532012197267-da84d127e765",  # sunset hope / resilience
    "1532938911079-1b06ac7ceec7",  # clinical infusion / therapy
    "1536640175698-daff1379bd44",  # cannabis leaves / drugs
    "1536640712-4d4c36ff0e4e",    # social media phone
    "1541781774459-bb2af2f05b55",  # woman worried face / anxiety
    "1543269865-cbf427effbad",     # hiking mountain / growth
    "1544367567-0f2fcb009e0b",     # therapy couch session
    "1552053831-71594a27632d",     # golden retriever dog
    "1552664730-d307ca884978",     # person awake at night
    "1558618666-fcd25c85cd64",     # neuron / blue network
    "1559757148-5c350d0d3c56",     # brain scan white
    "1559757175-5700dde675bc",     # neuroscience colorful brain
    "1573496359142-b8d87734a5a2",  # woman thinking hand on chin
    "1573497491208-6b1acb260507",  # DNA strands
    "1584030373083-d2361ac95da9",  # therapist and client
]

# Specific thematic overrides for key articles
CURATED = {
    161: "1512411546253-24151c727a81",  # Stop Eating Switch
    162: "1559757148-5c350d0d3c56",     # FTL1 / Brain Aging
    163: "1584030373083-d2361ac95da9",  # Astrocytes / PTSD
    164: "1518133910546-b6c2fb7d79e3",  # Schizophrenia mutation
    165: "1520206183501-b80af970d7eb",  # Sleep Switch
    166: "1512621776951-a57141f2eefd",  # Teen diet
    167: "1531983412531-1f49a365ffed",  # Stroke / Brain scans
    168: "1471864190281-a93a3070b6de",  # Metformin
    169: "1521790797524-b2497295b8a0",  # Paternal depression
    170: "1544367567-0f2fcb009e0b",     # Ozempic
    171: "1536640175698-daff1379bd44",  # Cannabis
    172: "1490730141103-6cac27aaab94",  # Gut health
    173: "1526951521990-620dc14c214b",  # Microplastics
    174: "1530210124550-912dc1381cb8",  # Depression energy
    175: "1532938911079-1b06ac7ceec7",  # Ketamine
    176: "1466471340190-98259d5a77c0",  # Magic mushrooms
    177: "1552053831-71594a27632d",     # Golden Retriever gene
    178: "1510832198440-a52376950479",  # Addiction protein
    179: "1507413245164-6160d8298b31",  # AI Alzheimer's atlas
    180: "1493132630797-4c5837dec5f0",  # Fear of aging
    43:  "1516302752625-fcc3c50ae61f",
    44:  "1541781774459-bb2af2f05b55",
    45:  "1508739773434-c26b3d09e071",
    46:  "1516589174184-c685ca33d2b0",
    47:  "1516251193007-45ef944ab0c6",
    48:  "1530210124550-912dc1381cb8",
    49:  "1543269865-cbf427effbad",
    50:  "1506784983877-45594efa4cbe",
    51:  "1573496359142-b8d87734a5a2",
    65:  "1517245386807-bb43f82c33c4",
    66:  "1522071820081-009f0129c71c",
    67:  "1558618666-fcd25c85cd64",
    68:  "1455390582262-044cdead277a",
    69:  "1490730141103-6cac27aaab94",
    70:  "1532012197267-da84d127e765",
    74:  "1552664730-d307ca884978",
    75:  "1506126613408-eca07ce68773",
    76:  "1484480974693-6ca0a78fb36b",
    77:  "1499750310107-5fef283666bb",
}

def get_id(art_id):
    return CURATED.get(art_id, VERIFIED_POOL[art_id % len(VERIFIED_POOL)])

def url(img_id, w=400):
    return f"https://images.unsplash.com/photo-{img_id}?auto=format&fit=crop&q=80&w={w}"

def repair_index():
    print("→ Patching index.html…")
    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    content = content.replace('\\n', '')

    # Two-pass approach: find each article card block, get the art_id,
    # then replace the background-image URL within that specific block.
    
    # Pattern to find the full card block (from <article> to </article>)
    card_pattern = re.compile(r'(<article class="card[^>]*>)([\s\S]*?)(</article>)', re.DOTALL)
    
    def replace_card(m):
        prefix = m.group(1)
        body = m.group(2)
        suffix = m.group(3)
        
        # Extract article ID from href
        link_match = re.search(r'href="article(\d+)\.html"', body)
        if not link_match:
            return m.group(0)
        
        art_id = int(link_match.group(1))
        new_url = url(get_id(art_id), w=400)
        
        # Replace the background-image URL in this card
        body = re.sub(
            r"(background-image:\s*url\()['\"]?[^)'\"]*['\"]?(\))",
            f"\\1'{new_url}'\\2",
            body
        )
        return prefix + body + suffix
    
    content = card_pattern.sub(replace_card, content)

    with open(INDEX_PATH, 'w', encoding='utf-8') as f:
        f.write(content)
    print("  ✅ index.html done.")


def repair_articles():
    files = sorted(
        [f for f in os.listdir(BASE_DIR) if re.match(r'article\d+\.html', f)],
        key=lambda x: int(re.search(r'\d+', x).group())
    )
    print(f"→ Patching {len(files)} article files…")
    for fname in files:
        art_id = int(re.search(r'\d+', fname).group())
        img_id = get_id(art_id)
        full = url(img_id, w=1200)
        path = os.path.join(BASE_DIR, fname)

        with open(path, 'r', encoding='utf-8') as f:
            c = f.read()

        # OG + Twitter
        c = re.sub(r'(meta property="og:image" content=")[^"]*"', f'\\g<1>{full}"', c)
        c = re.sub(r'(meta name="twitter:image" content=")[^"]*"', f'\\g<1>{full}"', c)
        # JSON-LD
        c = re.sub(r'("image":\s*")[^"]*"', f'\\g<1>{full}"', c)

        # Hero image in body
        if '<main class="article-body' in c:
            body_open_end = c.index('<main class="article-body')
            body_end = c.index('</main>', body_open_end)
            body = c[body_open_end:body_end]

            img_tag = f'<img src="{full}" alt="Article illustration" style="width:100%;border-radius:12px;margin-bottom:2rem;" loading="lazy">'

            if '<img' not in body:
                # Insert after first </p> within body
                first_p_end = body.find('</p>')
                if first_p_end != -1:
                    insert_pos = body_open_end + first_p_end + len('</p>')
                    c = c[:insert_pos] + '\n            ' + img_tag + c[insert_pos:]
            else:
                # Replace first unsplash img in body
                c_before = c[:body_open_end]
                c_after = c[body_end:]
                body_fixed = re.sub(
                    r'<img[^>]*src="https://images\.unsplash\.com[^"]*"[^>]*>',
                    img_tag, body, count=1
                )
                c = c_before + body_fixed + c_after

        with open(path, 'w', encoding='utf-8') as f:
            f.write(c)

    print(f"  ✅ {len(files)} articles done.")


if __name__ == "__main__":
    repair_index()
    repair_articles()

    # Quick audit
    with open(INDEX_PATH) as f:
        idx = f.read()
    imgs = re.findall(r"background-image: url\('([^']+)'\)", idx)
    unique = len(set(imgs))
    print(f"\n📊 Index cards: {len(imgs)} total, {unique} unique images.")
    from collections import Counter
    top = Counter(imgs).most_common(3)
    print("   Top repeats:", [(u.split('photo-')[1][:20], n) for u, n in top])
    print("🎉 Done!")
