#!/usr/bin/env python3
"""
Gemini AI Article Rewriter — uses google-genai (latest SDK)
Generates 4,000+ word unique SEO articles. FREE tier: 1,500 req/day.
Get your free key at: https://aistudio.google.com/apikey
"""
import os
import glob
import time
from bs4 import BeautifulSoup
from google import genai
from google.genai import types

# ============================================================
# YOUR FREE GEMINI API KEY
# Get one free at: https://aistudio.google.com/apikey
# ============================================================
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
BASE_DIR = "/Users/khalidaitelmaati/Desktop/scrapy-master/psychology-theme-main"
MIN_WORDS_TO_SKIP = 3000

client = genai.Client(api_key=GEMINI_API_KEY)

PROMPT_TEMPLATE = """You are a world-class clinical psychologist and expert health writer.
Write an extremely detailed 4,000-word research-backed HTML article on: "{topic}"

STRICT RULES:
- Output ONLY raw HTML — no markdown fences, no <html>/<head>/<body> tags
- Use <h2>, <h3>, <p>, <ul>, <ol>, <li>, <blockquote>, <section>, <strong>
- NO <h1> tags (page already has one)
- Minimum 4,000 words total — be comprehensive and thorough
- Structure these sections in order:
  1. Introduction (300+ words): what this topic means and why it matters deeply
  2. The Neuroscience (400+ words): brain regions, hormones, circuits involved
  3. Psychological Framework (400+ words): clinical theories explaining this phenomenon
  4. Case Study (300+ words): hypothetical realistic patient story showing real impact
  5. The Research (400+ words): cite real or plausible studies with journal names, years
  6. Common Myths Debunked (300+ words): 5 myths with evidence-based corrections
  7. Step-by-Step Action Guide (400+ words): 7 concrete evidence-backed strategies
  8. Expert Insights (300+ words): quotes and perspectives from field experts
  9. FAQ (300+ words): 5 detailed Q&A pairs about this specific topic
  10. Conclusion (200+ words): powerful closing summary
- Every sentence must be SPECIFIC to this exact topic. Absolutely NO generic filler.
- Include inline citations like: (Smith et al., 2023, Journal of Neuroscience)
- Use <blockquote> for expert quotes
- Use <ul> and <li> for lists in action guide and myths sections
"""


def get_topic(soup):
    h1 = soup.find("h1")
    if h1 and h1.get_text(strip=True):
        return h1.get_text(strip=True)
    title = soup.find("title")
    if title:
        return title.get_text(strip=True).split("|")[0].strip()
    return None


def generate_content(topic):
    prompt = PROMPT_TEMPLATE.format(topic=topic)
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                max_output_tokens=8192,
                temperature=0.8,
            )
        )
        text = response.text.strip()
        # Strip markdown fences if model adds them anyway
        if text.startswith("```"):
            text = text.split("\n", 1)[-1]
        if text.endswith("```"):
            text = text.rsplit("```", 1)[0]
        return text
    except Exception as e:
        print(f"  ⚠️  API error: {e}")
        return None


def inject_content(soup, new_html):
    main = soup.find("main", class_="article-body") or soup.find("main")
    if not main:
        return False
    author_box = main.find("div", class_="author-box")
    faq_section = main.find("section", class_="faq-section")
    anchor = author_box or faq_section
    new_soup = BeautifulSoup(new_html, "html.parser")
    if anchor:
        anchor.insert_before(new_soup)
    else:
        main.append(new_soup)
    return True


def rewrite_all():
    files = sorted(glob.glob(os.path.join(BASE_DIR, "article*.html")))
    total = len(files)
    done = skipped = errors = 0

    print(f"🚀 Starting rewrite of {total} articles with Gemini AI...\n")

    for i, file_path in enumerate(files):
        fname = os.path.basename(file_path)
        with open(file_path, "r", encoding="utf-8") as f:
            html = f.read()

        soup = BeautifulSoup(html, "html.parser")
        main = soup.find("main", class_="article-body") or soup.find("main")

        if main and len(main.get_text().split()) >= MIN_WORDS_TO_SKIP:
            print(f"⏭  {fname}: already long enough — skipping.")
            skipped += 1
            continue

        topic = get_topic(soup)
        if not topic:
            print(f"⚠️  {fname}: no topic — skipping.")
            skipped += 1
            continue

        print(f"✍️  [{i+1}/{total}] Generating for: '{topic[:65]}'...")
        new_html = generate_content(topic)
        if not new_html:
            errors += 1
            time.sleep(5)
            continue

        wc = len(BeautifulSoup(new_html, "html.parser").get_text().split())
        print(f"   → {wc} words generated")

        if not inject_content(soup, new_html):
            print(f"   ❌ Could not inject into {fname}")
            errors += 1
            continue

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(str(soup))

        done += 1
        print(f"   ✅ {fname} saved")
        # Gemini free tier: ~15 rpm, sleep 4s to be safe
        time.sleep(4)

    print(f"\n🎉 Complete! Rewritten: {done} | Skipped: {skipped} | Errors: {errors}")


if __name__ == "__main__":
    if GEMINI_API_KEY == "PASTE_YOUR_FREE_KEY_HERE":
        print("\n🔑 You need a FREE Gemini API key!")
        print("   1. Go to: https://aistudio.google.com/apikey")
        print("   2. Click 'Create API Key'")
        print("   3. Run: GEMINI_API_KEY=your_key_here python3 gemini_rewrite.py\n")
    else:
        rewrite_all()
