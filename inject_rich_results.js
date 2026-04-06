const fs = require('fs');
const path = require('path');

const dir = __dirname;

// ─────────────────────────────────────────────
// 1. HOMEPAGE: Organization + SitelinksSearchBox + BreadcrumbList
// ─────────────────────────────────────────────
const homepageExtraSchema = `
    <!-- Schema.org: Organization (triggers Knowledge Panel) -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Organization",
      "name": "Mind & Balance",
      "url": "https://leafanoo.com/",
      "logo": {
        "@type": "ImageObject",
        "url": "https://leafanoo.com/images/favicon.svg"
      },
      "sameAs": [],
      "description": "Mind & Balance is a psychology and mental wellness publication providing clear, compassionate, and scientifically grounded insights on mental health, cognitive psychology, and emotional well-being.",
      "foundingDate": "2026",
      "email": "contact@leafanoo.com",
      "contactPoint": {
        "@type": "ContactPoint",
        "contactType": "editorial",
        "email": "contact@leafanoo.com"
      }
    }
    </script>

    <!-- Schema.org: SitelinksSearchBox (triggers search box in Google results) -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "WebSite",
      "url": "https://leafanoo.com/",
      "name": "Mind & Balance",
      "potentialAction": {
        "@type": "SearchAction",
        "target": {
          "@type": "EntryPoint",
          "urlTemplate": "https://leafanoo.com/?q={search_term_string}"
        },
        "query-input": "required name=search_term_string"
      }
    }
    </script>

    <!-- Schema.org: ItemList (triggers sitelinks in Google results) -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "ItemList",
      "name": "Latest Psychology Articles",
      "url": "https://leafanoo.com/#articles",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "url": "https://leafanoo.com/article1.html", "name": "Understanding Anxiety in the Digital Age" },
        { "@type": "ListItem", "position": 2, "url": "https://leafanoo.com/article4.html", "name": "The Psychology of Habit Formation" },
        { "@type": "ListItem", "position": 3, "url": "https://leafanoo.com/article5.html", "name": "Understanding Imposter Syndrome" },
        { "@type": "ListItem", "position": 4, "url": "https://leafanoo.com/article11.html", "name": "The Neuroscience of Gratitude" },
        { "@type": "ListItem", "position": 5, "url": "https://leafanoo.com/article12.html", "name": "Boundaries: The Psychology of Saying No" },
        { "@type": "ListItem", "position": 6, "url": "https://leafanoo.com/about.html", "name": "About Mind & Balance" }
      ]
    }
    </script>`;

// ─────────────────────────────────────────────
// 2. ARTICLE PAGES — BreadcrumbList + FAQPage schemas
// ─────────────────────────────────────────────
const articleFAQs = {
  'article1.html': [
    { q: "What causes anxiety in the digital age?", a: "Constant notifications and social media create a low-grade stress response from dopamine-driven reward loops and information overload." },
    { q: "How can I reduce digital anxiety?", a: "Establish tech-free zones, batch check messages at set times, and deliberately embrace moments of boredom without reaching for your phone." }
  ],
  'article4.html': [
    { q: "How long does it take to form a habit?", a: "Research from University College London shows it takes an average of 66 days, not the commonly cited 21 days, for a behavior to become automatic." },
    { q: "What is the habit loop?", a: "The habit loop consists of three elements: a Cue (trigger), a Routine (the behavior), and a Reward (the benefit that reinforces the loop)." }
  ],
  'article5.html': [
    { q: "What is Imposter Syndrome?", a: "Imposter Syndrome is the persistent belief that you are a fraud despite clear evidence of success, causing you to attribute achievements to luck rather than ability." },
    { q: "Who gets Imposter Syndrome?", a: "Nearly 70% of people experience it. It disproportionately affects high achievers, academics, and those entering new roles or environments." }
  ],
  'article6.html': [
    { q: "How does sleep affect mental health?", a: "During REM sleep, the brain processes emotional memories and regulates mood. Chronic sleep deprivation amplifies amygdala reactivity by up to 60%, causing emotional dysregulation." },
    { q: "How much sleep do I need for good mental health?", a: "Most adults need 7-9 hours per night. Prioritizing consistent sleep timing and a cool bedroom are the two most impactful habits for sleep quality." }
  ],
  'article11.html': [
    { q: "What does gratitude do to the brain?", a: "Gratitude activates the release of dopamine and serotonin, the brain's mood-regulating neurotransmitters, and strengthens the medial prefrontal cortex over time." },
    { q: "How do I practice gratitude effectively?", a: "Write down three specific things you are grateful for daily, include people in your gratitude, and use mental subtraction to imagine life without what you value." }
  ],
  'article13.html': [
    { q: "Why do people procrastinate?", a: "Procrastination is primarily an emotion regulation problem. People avoid tasks because they trigger negative emotions like anxiety, boredom, or self-doubt—not because of poor time management." },
    { q: "How do I stop procrastinating?", a: "Practice self-compassion after procrastination episodes, use the 2-minute rule to lower the barrier to starting, and bundle dreaded tasks with enjoyable activities." }
  ],
};

function buildBreadcrumb(file, title) {
  return `
    <!-- Schema.org: BreadcrumbList -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://leafanoo.com/" },
        { "@type": "ListItem", "position": 2, "name": "Articles", "item": "https://leafanoo.com/#articles" },
        { "@type": "ListItem", "position": 3, "name": "${title}", "item": "https://leafanoo.com/${file}" }
      ]
    }
    </script>`;
}

function buildFAQ(faqs) {
  const items = faqs.map(f => `{ "@type": "Question", "name": "${f.q}", "acceptedAnswer": { "@type": "Answer", "text": "${f.a}" } }`).join(',\n        ');
  return `
    <!-- Schema.org: FAQPage (triggers FAQ rich snippets in Google) -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [
        ${items}
      ]
    }
    </script>`;
}

// ─── Apply to index.html ───────────────────────
let indexPath = path.join(dir, 'index.html');
let indexContent = fs.readFileSync(indexPath, 'utf8');
if (!indexContent.includes('"Organization"')) {
    indexContent = indexContent.replace('</head>', `${homepageExtraSchema}\n</head>`);
    fs.writeFileSync(indexPath, indexContent, 'utf8');
    console.log('✅ index.html — Organization + SitelinksSearchBox + ItemList schemas added');
} else {
    console.log('⏭  index.html — Already has Organization schema');
}

// ─── Apply BreadcrumbList + FAQPage to articles ──
const allArticleFiles = fs.readdirSync(dir).filter(f => /^article\d+\.html$/.test(f));

allArticleFiles.forEach(file => {
    const filePath = path.join(dir, file);
    let content = fs.readFileSync(filePath, 'utf8');

    if (content.includes('"BreadcrumbList"')) {
        console.log(`⏭  ${file} — BreadcrumbList already present`);
        return;
    }

    // Extract title for breadcrumb
    const titleMatch = content.match(/<title>(.*?)\s*\|\s*Mind/i);
    const title = titleMatch ? titleMatch[1].replace(/"/g, '\\"') : 'Article';

    let injection = buildBreadcrumb(file, title);

    // Add FAQ if defined
    if (articleFAQs[file]) {
        injection += buildFAQ(articleFAQs[file]);
    }

    content = content.replace('</head>', `${injection}\n</head>`);
    fs.writeFileSync(filePath, content, 'utf8');
    const hasFAQ = articleFAQs[file] ? ' + FAQPage' : '';
    console.log(`✅ ${file} — BreadcrumbList${hasFAQ} schema added`);
});

console.log('\n🎯 All Sitelink & Knowledge Panel schemas deployed!');
