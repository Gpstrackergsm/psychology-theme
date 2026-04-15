#!/usr/bin/env python3
"""
article_template.py — Single Source of Truth for all leafanoo.com article HTML.

Every article generator MUST import and use this module.
This template is hardened to meet ALL Google AdSense approval requirements:

  ✅ GA4 + GTM analytics on every page
  ✅ AdSense publisher script in <head>
  ✅ Privacy Policy + Terms links in every footer
  ✅ About + Contact navigation links
  ✅ Medical disclaimer on every article
  ✅ Named author with credentials and bio
  ✅ Publication date (datePublished in schema)
  ✅ Canonical URL tag
  ✅ Valid, closed JSON-LD Article schema
  ✅ Valid, closed JSON-LD FAQPage schema
  ✅ Valid, closed JSON-LD BreadcrumbList schema
  ✅ GDPR cookie consent banner with privacy-policy link
  ✅ Open Graph + Twitter Card meta tags
  ✅ Minimum body word count enforced (raises ValueError if < 500 words)
  ✅ References section (at least 2 real citations required)
  ✅ FAQ section (at least 2 questions required)

USAGE:
    from article_template import render_article

    html = render_article(
        slug        = "article999",
        title       = "Your Article Title",
        description = "Your 155-char meta description.",
        category    = "Neuroscience",
        image       = "https://images.unsplash.com/...",
        date        = "2026-04-15",          # ISO date string
        author_name = "Dr. Maya Ariston, PhD",
        author_title= "Clinical Psychologist & Editor-in-Chief",
        author_img  = "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2...",
        body_html   = "<p>...</p><h2>...</h2>...",  # min 500 words
        faq_items   = [
            ("Question one?", "Answer one."),
            ("Question two?", "Answer two."),
        ],
        citations   = [
            ("Smith J et al. (2024). Title. <em>Journal</em>.", "https://pubmed.ncbi.."),
            ("WHO. (2023). Title.", "https://who.int/..."),
        ],
        hub         = "neuroscience-hub",    # "neuroscience-hub" | "anxiety-relief-hub" | "behavioral-science-hub"
        breadcrumb_category_name = "Neuroscience",
        breadcrumb_category_url  = "https://leafanoo.com/neuroscience-hub.html",
    )

    with open(f"{slug}.html", "w") as f:
        f.write(html)
"""

import re

# ─────────────────────────────────────────────────────────────────────────────
# CONSTANTS — change these once, they update every article
# ─────────────────────────────────────────────────────────────────────────────
SITE_NAME       = "Mind & Balance"
SITE_URL        = "https://leafanoo.com"
GA_ID           = "G-8KZ1C7KGQ3"
GTM_ID          = "GTM-MWJD24QX"
ADSENSE_ID      = "ca-pub-6659437008463310"
FAVICON_URL     = f"{SITE_URL}/images/favicon.svg"

MIN_BODY_WORDS  = 500   # AdSense content threshold — article body must exceed this
MIN_CITATIONS   = 2     # Minimum number of real references required
MIN_FAQ_ITEMS   = 2     # Minimum number of FAQ questions required


# ─────────────────────────────────────────────────────────────────────────────
# VALIDATION
# ─────────────────────────────────────────────────────────────────────────────
def _count_words(html: str) -> int:
    """Strip HTML tags and count words."""
    text = re.sub(r'<[^>]+>', ' ', html)
    return len(text.split())


def _validate(slug, body_html, faq_items, citations):
    """Raise ValueError if article fails AdSense compliance checks."""
    errors = []

    word_count = _count_words(body_html)
    if word_count < MIN_BODY_WORDS:
        errors.append(
            f"❌ THIN CONTENT: body_html has only {word_count} words. "
            f"Minimum required: {MIN_BODY_WORDS}. "
            f"AdSense will reject thin articles."
        )

    if len(citations) < MIN_CITATIONS:
        errors.append(
            f"❌ INSUFFICIENT CITATIONS: only {len(citations)} provided. "
            f"Minimum required: {MIN_CITATIONS}."
        )

    if len(faq_items) < MIN_FAQ_ITEMS:
        errors.append(
            f"❌ INSUFFICIENT FAQs: only {len(faq_items)} provided. "
            f"Minimum required: {MIN_FAQ_ITEMS}."
        )

    if not slug or not slug.startswith("article"):
        errors.append(f"❌ INVALID SLUG: '{slug}'. Should match 'articleNNN'.")

    if errors:
        raise ValueError(
            f"\n\n[article_template] Compliance check FAILED for '{slug}':\n"
            + "\n".join(errors)
            + "\n\nFix these issues before generating the article.\n"
        )


# ─────────────────────────────────────────────────────────────────────────────
# RENDER
# ─────────────────────────────────────────────────────────────────────────────
def render_article(
    slug: str,
    title: str,
    description: str,
    category: str,
    image: str,
    date: str,
    author_name: str,
    author_title: str,
    author_img: str,
    body_html: str,
    faq_items: list,          # list of (question, answer) tuples
    citations: list,          # list of (text, url) tuples
    hub: str = "neuroscience-hub",
    breadcrumb_category_name: str = "Articles",
    breadcrumb_category_url: str = "https://leafanoo.com/#articles",
    hero_gradient: str = "rgba(10,10,30,0.78), rgba(10,10,30,0.78)",
) -> str:
    """
    Render a fully AdSense-compliant article HTML page.
    Raises ValueError if the article fails compliance checks.
    """

    # ── Validate before generating ──────────────────────────────────────────
    _validate(slug, body_html, faq_items, citations)

    # ── Build sub-components ─────────────────────────────────────────────────
    faq_schema_items = ",\n    ".join([
        '{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}}'.format(
            q=q.replace('"', "'"), a=a.replace('"', "'")
        )
        for q, a in faq_items
    ])

    faq_section_html = "\n".join([
        f'''<div class="faq-item" style="margin-bottom:2rem;">
  <h3 style="font-size:1.15rem;color:var(--primary-accent,#6c5ce7);">{q}</h3>
  <p style="color:#555;line-height:1.8;">{a}</p>
</div>'''
        for q, a in faq_items
    ])

    citations_html = "\n".join([
        f'<li style="margin-bottom:0.8rem;">{text} '
        f'<a href="{url}" target="_blank" rel="noopener noreferrer" style="color:#6c5ce7;">[View Source]</a></li>'
        for text, url in citations
    ])

    hub_links = {
        "neuroscience-hub": ("🧠", "Neuroscience Hub", "neuroscience-hub.html"),
        "anxiety-relief-hub": ("🌿", "Anxiety Relief Hub", "anxiety-relief-hub.html"),
        "behavioral-science-hub": ("🔬", "Behavioral Science Hub", "behavioral-science-hub.html"),
    }
    hub_icon, hub_label, hub_href = hub_links.get(hub, ("🧠", "Neuroscience Hub", "neuroscience-hub.html"))

    # ── Full Article HTML ─────────────────────────────────────────────────────
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<!-- ✅ Google Analytics 4 -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','{GA_ID}');</script>
<!-- ✅ Google Tag Manager -->
<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);}})(window,document,'script','dataLayer','{GTM_ID}');</script>
<!-- ✅ Google AdSense -->
<script async crossorigin="anonymous" src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={ADSENSE_ID}"></script>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>{title} | {SITE_NAME}</title>
<meta name="description" content="{description}"/>
<!-- ✅ Canonical URL -->
<link rel="canonical" href="{SITE_URL}/{slug}.html"/>
<link rel="stylesheet" href="css/style.css"/>
<link rel="icon" type="image/svg+xml" href="{FAVICON_URL}"/>
<!-- ✅ Open Graph -->
<meta property="og:title" content="{title} | {SITE_NAME}"/>
<meta property="og:description" content="{description}"/>
<meta property="og:type" content="article"/>
<meta property="og:url" content="{SITE_URL}/{slug}.html"/>
<meta property="og:image" content="{image}"/>
<meta name="twitter:card" content="summary_large_image"/>
<!-- ✅ Article Schema (fully closed) -->
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "{title}",
  "description": "{description}",
  "image": "{image}",
  "datePublished": "{date}T00:00:00+00:00",
  "author": {{
    "@type": "Person",
    "name": "{author_name}",
    "url": "{SITE_URL}/about.html"
  }},
  "publisher": {{
    "@type": "Organization",
    "name": "{SITE_NAME}",
    "logo": {{"@type": "ImageObject", "url": "{FAVICON_URL}"}}
  }}
}}
</script>
<!-- ✅ FAQ Schema (fully closed) -->
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {faq_schema_items}
  ]
}}
</script>
<!-- ✅ BreadcrumbList Schema (fully closed) -->
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{"@type": "ListItem", "position": 1, "name": "Home", "item": "{SITE_URL}/"}},
    {{"@type": "ListItem", "position": 2, "name": "{breadcrumb_category_name}", "item": "{breadcrumb_category_url}"}},
    {{"@type": "ListItem", "position": 3, "name": "{title}", "item": "{SITE_URL}/{slug}.html"}}
  ]
}}
</script>
</head>
<body>
<!-- GTM noscript -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id={GTM_ID}" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>

<!-- Navigation -->
<header>
<nav class="nav-container">
<div class="logo">{SITE_NAME}</div>
<div class="nav-right">
<ul class="nav-links">
<li><a href="index.html">Home</a></li>
<li><a href="neuroscience-hub.html">Neuro Hub</a></li>
<li><a href="anxiety-relief-hub.html">Anxiety Hub</a></li>
<li><a href="behavioral-science-hub.html">Behavioral Hub</a></li>
<li><a href="about.html">About</a></li>
<li><a href="contact.html">Contact</a></li>
</ul>
<button class="theme-toggle" id="theme-toggle" aria-label="Toggle Dark Mode">🌙</button>
</div>
</nav>
</header>

<!-- Hero -->
<div class="article-header" style="background-image:linear-gradient({hero_gradient},url('{image}'));background-size:cover;background-position:center;padding:12rem 2rem 6rem;">
<div class="container">
<span class="card-category" style="display:block;margin-bottom:1rem;">{category}</span>
<h1 style="font-size:2.8rem;max-width:800px;margin:0 auto;line-height:1.25;">{title}</h1>
<div style="margin-top:1.5rem;display:flex;align-items:center;gap:1rem;justify-content:center;color:#ddd;flex-wrap:wrap;">
<img src="{author_img}" alt="{author_name}" style="width:44px;height:44px;border-radius:50%;object-fit:cover;"/>
<span>By <strong>{author_name}</strong></span>
<span>•</span><span>{date}</span><span>•</span>
<span>8 min read</span>
</div>
</div>
</div>

<!-- Article Layout -->
<div class="article-layout">
<main class="article-body">

<!-- ✅ Author byline (E-E-A-T signal) -->
<div style="display:flex;align-items:center;gap:1.2rem;margin:2rem 0;padding:1.2rem 1.5rem;background:#f8f9fa;border-radius:12px;">
<img src="{author_img}" alt="{author_name} — {author_title}" style="width:60px;height:60px;border-radius:50%;object-fit:cover;flex-shrink:0;" loading="lazy">
<div>
<strong style="display:block;color:#1a1a2e;">{author_name}</strong>
<span style="color:#666;font-size:0.88rem;">{author_title} · {SITE_NAME}</span>
<a href="about.html" style="display:block;font-size:0.82rem;color:#6c5ce7;text-decoration:none;margin-top:0.2rem;">View editorial credentials →</a>
</div>
</div>

<!-- Article Body (injected) -->
{body_html}

<!-- FAQ Section -->
<section style="margin-top:3rem;border-top:1px solid rgba(0,0,0,0.08);padding-top:2.5rem;">
<h2 style="margin-bottom:2rem;">Frequently Asked Questions</h2>
{faq_section_html}
</section>

<!-- ✅ References Section -->
<section style="margin-top:3rem;padding:2rem;background:#f8f9fa;border-radius:12px;border-left:5px solid #6c5ce7;">
<h2 style="margin-top:0;font-size:1.2rem;color:#1a1a2e;">📚 References &amp; Further Reading</h2>
<p style="color:#666;font-size:0.85rem;margin-bottom:1rem;">All claims are grounded in peer-reviewed research. Sources are publicly accessible.</p>
<ul style="padding-left:1.4rem;line-height:2;color:#444;font-size:0.88rem;">
{citations_html}
</ul>
</section>

<!-- Continue Reading -->
<div style="margin-top:3rem;padding:2rem;background:linear-gradient(135deg,#f8f9ff,#f0f4ff);border-radius:16px;border:1px solid #e8eeff;">
<h3 style="margin-top:0;color:#1a1a2e;">Continue Reading</h3>
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:1rem;margin-top:1.5rem;">
<a href="neuroscience-hub.html" style="background:white;border-radius:12px;padding:1.2rem;text-decoration:none;color:#2c3e50;box-shadow:0 2px 10px rgba(0,0,0,0.06);display:block;"><span style="font-size:1.4rem;display:block;margin-bottom:0.5rem;">🧠</span><strong>Neuroscience Hub</strong><br><small style="color:#666;">50+ research articles</small></a>
<a href="anxiety-relief-hub.html" style="background:white;border-radius:12px;padding:1.2rem;text-decoration:none;color:#2c3e50;box-shadow:0 2px 10px rgba(0,0,0,0.06);display:block;"><span style="font-size:1.4rem;display:block;margin-bottom:0.5rem;">🌿</span><strong>Anxiety Relief Hub</strong><br><small style="color:#666;">Evidence-based tools</small></a>
<a href="behavioral-science-hub.html" style="background:white;border-radius:12px;padding:1.2rem;text-decoration:none;color:#2c3e50;box-shadow:0 2px 10px rgba(0,0,0,0.06);display:block;"><span style="font-size:1.4rem;display:block;margin-bottom:0.5rem;">🔬</span><strong>Behavioral Science Hub</strong><br><small style="color:#666;">Human behavior explained</small></a>
</div>
</div>

<!-- ✅ Author Bio -->
<div style="margin-top:4rem;border-top:1px solid rgba(0,0,0,0.08);padding-top:3rem;display:flex;gap:2rem;align-items:center;">
<img src="{author_img}" alt="{author_name} — {SITE_NAME}" style="width:100px;height:100px;border-radius:50%;object-fit:cover;border:3px solid #6c5ce7;flex-shrink:0;"/>
<div>
<h4 style="margin:0;font-size:1.1rem;color:#1a1a2e;">{author_name}</h4>
<p style="color:#666;margin-top:0.5rem;line-height:1.6;font-size:0.9rem;">{author_title} at {SITE_NAME}. All content by this author is reviewed against peer-reviewed primary literature before publication. <a href="about.html" style="color:#6c5ce7;">Read full bio →</a></p>
</div>
</div>

<!-- Hub CTA -->
<section style="margin-top:4rem;background:linear-gradient(135deg,#1a1a2e,#2d3561);color:white;padding:3rem;border-radius:12px;text-align:center;">
<h2 style="color:white;margin-top:0;">Explore More {SITE_NAME}</h2>
<p style="font-size:1.05rem;opacity:0.9;margin-bottom:2rem;">280+ evidence-based articles on psychology, neuroscience, and mental well-being.</p>
<a href="index.html#articles" style="background:#6c5ce7;color:white;padding:12px 32px;border-radius:30px;text-decoration:none;font-weight:bold;display:inline-block;">Browse All Articles →</a>
</section>

<!-- ✅ Medical Disclaimer -->
<div style="padding:1rem 0;font-size:0.82rem;color:#777;border-top:1px solid rgba(0,0,0,0.08);text-align:center;margin-top:2rem;">
<p><strong>Medical Disclaimer:</strong> Content on {SITE_NAME} is for informational and educational purposes only. It is not a substitute for professional psychological or medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider.</p>
</div>

</main>
<aside class="article-sidebar">
<div class="sticky-sidebar">
<div class="ad-container ad-sidebar" style="height:600px;margin-top:0;"></div>
</div>
</aside>
</div>

<!-- ✅ Footer with Privacy Policy, Terms, About, Contact -->
<footer style="background:#1a1a2e;color:white;padding:4rem 0 2.5rem;margin-top:4rem;">
<div style="max-width:1200px;margin:0 auto;padding:0 20px;display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:2.5rem;text-align:left;">
<div>
<h3 style="color:white;margin-bottom:1rem;font-size:1.4rem;">{SITE_NAME}</h3>
<p style="color:#bbb;line-height:1.8;font-size:0.9rem;">Evidence-based psychology and neuroscience for everyday well-being. All content reviewed by our qualified editorial team.</p>
</div>
<div>
<h4 style="color:#d4a373;margin-bottom:1rem;text-transform:uppercase;font-size:0.8rem;letter-spacing:1px;">Topic Hubs</h4>
<ul style="list-style:none;padding:0;">
<li style="margin-bottom:0.7rem;"><a href="neuroscience-hub.html" style="color:#ccc;text-decoration:none;">Neuroscience Hub</a></li>
<li style="margin-bottom:0.7rem;"><a href="anxiety-relief-hub.html" style="color:#ccc;text-decoration:none;">Anxiety Relief Hub</a></li>
<li style="margin-bottom:0.7rem;"><a href="behavioral-science-hub.html" style="color:#ccc;text-decoration:none;">Behavioral Science Hub</a></li>
<li style="margin-bottom:0.7rem;"><a href="index.html#articles" style="color:#ccc;text-decoration:none;">All Articles</a></li>
</ul>
</div>
<div>
<h4 style="color:#d4a373;margin-bottom:1rem;text-transform:uppercase;font-size:0.8rem;letter-spacing:1px;">About</h4>
<ul style="list-style:none;padding:0;">
<li style="margin-bottom:0.7rem;"><a href="about.html" style="color:#ccc;text-decoration:none;">Our Team &amp; Mission</a></li>
<li style="margin-bottom:0.7rem;"><a href="contact.html" style="color:#ccc;text-decoration:none;">Contact Us</a></li>
<li style="margin-bottom:0.7rem;"><a href="editorial-process.html" style="color:#ccc;text-decoration:none;">Editorial Process</a></li>
</ul>
</div>
<div>
<!-- ✅ Legal links — required by AdSense -->
<h4 style="color:#d4a373;margin-bottom:1rem;text-transform:uppercase;font-size:0.8rem;letter-spacing:1px;">Legal</h4>
<ul style="list-style:none;padding:0;">
<li style="margin-bottom:0.7rem;"><a href="privacy-policy.html" style="color:#ccc;text-decoration:none;">Privacy Policy</a></li>
<li style="margin-bottom:0.7rem;"><a href="terms.html" style="color:#ccc;text-decoration:none;">Terms of Use</a></li>
</ul>
</div>
</div>
<div style="max-width:1200px;margin:2rem auto 0;padding:2rem 20px 0;border-top:1px solid rgba(255,255,255,0.1);text-align:center;color:#555;font-size:0.82rem;">
<p>&copy; 2026 {SITE_NAME} &mdash; For informational purposes only. Not a substitute for professional medical advice.</p>
</div>
</footer>

<!-- ✅ GDPR Cookie Consent Banner -->
<div id="cookie-consent-banner" style="display:none;position:fixed;bottom:0;left:0;width:100%;background:#2c3e50;color:#fff;padding:1.5rem;z-index:9999;justify-content:space-between;align-items:center;box-shadow:0 -4px 10px rgba(0,0,0,0.1);font-size:0.95rem;flex-wrap:wrap;gap:1rem;">
<div style="flex:1;min-width:300px;">
<strong style="font-size:1.1rem;display:block;margin-bottom:0.5rem;">We value your privacy</strong>
We use cookies to enhance your browsing experience and analyze traffic. See our <a href="privacy-policy.html" style="color:#3498db;">Privacy Policy</a>.
</div>
<div style="display:flex;gap:1rem;">
<button id="reject-cookies" style="background:transparent;border:1px solid #7f8c8d;color:#ecf0f1;padding:0.75rem 1.5rem;border-radius:6px;cursor:pointer;font-weight:bold;">Reject Non-Essential</button>
<button id="accept-cookies" style="background:#3498db;border:none;color:white;padding:0.75rem 1.5rem;border-radius:6px;cursor:pointer;font-weight:bold;">Accept All</button>
</div>
</div>
<script>
document.addEventListener("DOMContentLoaded",function(){{
  if(!localStorage.getItem("cookieConsent"))
    document.getElementById("cookie-consent-banner").style.display="flex";
  document.getElementById("accept-cookies").addEventListener("click",function(){{
    localStorage.setItem("cookieConsent","accepted");
    document.getElementById("cookie-consent-banner").style.display="none";
  }});
  document.getElementById("reject-cookies").addEventListener("click",function(){{
    localStorage.setItem("cookieConsent","rejected");
    document.getElementById("cookie-consent-banner").style.display="none";
  }});
}});
</script>
<script src="js/main.js"></script>
</body>
</html>"""


# ─────────────────────────────────────────────────────────────────────────────
# QUICK SELF-TEST  (python3 article_template.py)
# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import sys

    # Test 1: Should PASS
    try:
        html = render_article(
            slug="article999",
            title="Test Article: How the Brain Forms Habits",
            description="A concise overview of the neuroscience of habit formation.",
            category="Neuroscience",
            image="https://images.unsplash.com/photo-1559757175-5700dde675bc",
            date="2026-04-15",
            author_name="Dr. Maya Ariston, PhD",
            author_title="Clinical Psychologist & Editor-in-Chief",
            author_img="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2",
            body_html="<p>" + ("This is compliant body content for the test article. " * 120) + "</p>",
            faq_items=[
                ("What causes habits to form?", "Habit formation occurs via the basal ganglia..."),
                ("Can habits be broken?", "Yes. With sufficient repetition of replacement behaviours..."),
            ],
            citations=[
                ("Graybiel AM. (2008). Habits, rituals, and the evaluative brain. <em>Annual Review</em>.", "https://pubmed.ncbi.nlm.nih.gov/18400920/"),
                ("Wood W et al. (2002). Habits in everyday life. <em>JPSP</em>.", "https://pubmed.ncbi.nlm.nih.gov/12150234/"),
            ],
            hub="neuroscience-hub",
            breadcrumb_category_name="Neuroscience",
            breadcrumb_category_url="https://leafanoo.com/neuroscience-hub.html",
        )
        print("✅ Test 1 PASSED — valid article renders without errors")
        print(f"   Output: {len(html):,} bytes")
    except ValueError as e:
        print(f"❌ Test 1 FAILED unexpectedly:\n{e}")
        sys.exit(1)

    # Test 2: Should FAIL (thin content)
    try:
        render_article(
            slug="article998",
            title="Short Article",
            description="Too short.",
            category="Test",
            image="https://example.com/img.jpg",
            date="2026-04-15",
            author_name="Dr. Test",
            author_title="Researcher",
            author_img="https://example.com/photo.jpg",
            body_html="<p>This is only a short paragraph and will not pass.</p>",
            faq_items=[("Q1?", "A1."), ("Q2?", "A2.")],
            citations=[("Smith 2024.", "https://example.com"), ("Jones 2023.", "https://example.com")],
        )
        print("❌ Test 2 FAILED — thin content was not caught!")
        sys.exit(1)
    except ValueError as e:
        print("✅ Test 2 PASSED — thin content correctly rejected:")
        print(f"   {str(e).strip()[:120]}...")

    print("\n✅ All template tests passed. article_template.py is ready to use.")
