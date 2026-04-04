const fs = require('fs');
const path = require('path');

const dir = __dirname;
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

// Article metadata for rich schema
const articleMeta = {
  'article1.html':  { title: 'Understanding Anxiety in the Digital Age', author: 'Dr. Sarah Jenkins', date: '2026-10-12', image: 'https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&q=80&w=1200', desc: 'How constant digital connectivity impacts our nervous system and what to do about it.' },
  'article2.html':  { title: 'The Power of Reframing Thoughts', author: 'Dr. Elena Rostova', date: '2026-11-01', image: 'https://images.unsplash.com/photo-1499209974431-9dddcece7f88?auto=format&fit=crop&q=80&w=1200', desc: 'Cognitive behavioral techniques that can shift your perspective and improve your daily mood.' },
  'article3.html':  { title: 'Mindfulness in 5 Minutes', author: 'Emma Sullivan', date: '2026-11-15', image: 'https://images.unsplash.com/photo-1506126613408-eca07ce68773?auto=format&fit=crop&q=80&w=1200', desc: 'A simple, evidence-based guide to integrating mindfulness into a busy schedule.' },
  'article4.html':  { title: 'The Psychology of Habit Formation', author: 'Dr. Elena Rostova', date: '2026-03-15', image: 'https://images.unsplash.com/photo-1484480974693-6ca0a78fb36b?auto=format&fit=crop&q=80&w=1200', desc: 'Discover the science behind habit formation and learn practical strategies to break bad habits.' },
  'article5.html':  { title: 'Understanding Imposter Syndrome', author: 'Emma Sullivan', date: '2026-02-22', image: 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&q=80&w=1200', desc: 'Explore the psychological roots of Imposter Syndrome and learn how to overcome feelings of inadequacy.' },
  'article6.html':  { title: 'The Science of Sleep and Mental Health', author: 'Dr. Marcus Lin', date: '2026-04-01', image: 'https://images.unsplash.com/photo-1541781774459-bb2af2f05b55?auto=format&fit=crop&q=80&w=1200', desc: 'Discover the profound link between sleep architecture and psychological well-being.' },
  'article7.html':  { title: 'Emotional Intelligence in the Workplace', author: 'David Chen', date: '2026-05-10', image: 'https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&q=80&w=1200', desc: 'Why Emotional Intelligence is often more critical for career success than IQ.' },
  'article8.html':  { title: 'Overcoming Perfectionism', author: 'Dr. Aria Martinez', date: '2026-06-08', image: 'https://images.unsplash.com/photo-1499209974431-9dddcece7f88?auto=format&fit=crop&q=80&w=1200', desc: 'How perfectionism sabotages mental health and strategies for embracing good enough.' },
  'article9.html':  { title: 'The Impact of Social Media on Self-Esteem', author: 'Dr. Sarah Jenkins', date: '2026-07-21', image: 'https://images.unsplash.com/photo-1516251193007-45ef944ab0c6?auto=format&fit=crop&q=80&w=1200', desc: 'The psychological effects of social media comparison and how to protect your mental health.' },
  'article10.html': { title: 'Cognitive Biases That Shape Our Reality', author: 'David Chen', date: '2026-08-05', image: 'https://images.unsplash.com/photo-1506126613408-eca07ce68773?auto=format&fit=crop&q=80&w=1200', desc: 'How confirmation bias and the halo effect manipulate your daily decision making.' },
  'article11.html': { title: 'The Neuroscience of Gratitude', author: 'Dr. Elena Rostova', date: '2026-09-02', image: 'https://images.unsplash.com/photo-1470116892389-0de5d9770b2c?auto=format&fit=crop&q=80&w=1200', desc: 'Discover how practicing gratitude physically rewires your brain for lasting mental health improvements.' },
  'article12.html': { title: 'Boundaries: The Psychology of Saying No', author: 'Emma Sullivan', date: '2026-09-18', image: 'https://images.unsplash.com/photo-1531746020798-e6953c6e8e04?auto=format&fit=crop&q=80&w=1200', desc: 'Learn why saying no is an act of radical self-respect and how to set healthy personal boundaries.' },
  'article13.html': { title: 'The Psychology of Procrastination', author: 'Dr. Marcus Lin', date: '2026-10-05', image: 'https://images.unsplash.com/photo-1455390582262-044cdead277a?auto=format&fit=crop&q=80&w=1200', desc: 'Procrastination is not a time management problem. It is an emotion regulation problem.' },
  'article14.html': { title: 'Attachment Theory: How Your Childhood Shapes Your Relationships', author: 'Dr. Aria Martinez', date: '2026-10-22', image: 'https://images.unsplash.com/photo-1529156069898-49953e39b3ac?auto=format&fit=crop&q=80&w=1200', desc: 'Explore the four attachment styles and discover how your earliest bonds govern your adult love life.' },
  'article15.html': { title: 'The Power of Vulnerability in Building Deep Connections', author: 'Emma Sullivan', date: '2026-11-08', image: 'https://images.unsplash.com/photo-1516585427167-9f4af9627e6c?auto=format&fit=crop&q=80&w=1200', desc: 'Vulnerability is not weakness—it is the ultimate birthplace of authentic human connection.' },
};

const nonArticlePages = ['index.html','about.html','contact.html','privacy-policy.html','terms.html'];

files.forEach(file => {
    const filePath = path.join(dir, file);
    let content = fs.readFileSync(filePath, 'utf8');

    if (content.includes('rel="canonical"')) {
        console.log(`⏭  Skipping ${file} - canonical already present.`);
        return;
    }

    const isArticle = articleMeta[file] !== undefined;
    const pageUrl = `https://leafanoo.com/${file === 'index.html' ? '' : file}`;

    // 1. CANONICAL TAG
    const canonicalTag = `    <link rel="canonical" href="${pageUrl}">`;

    // 2. FIX og:type for articles
    if (isArticle) {
        content = content.replace(
            '<meta property="og:type" content="website">',
            '<meta property="og:type" content="article">'
        );
    }

    // 3. JSON-LD SCHEMA
    let schema = '';
    if (isArticle) {
        const meta = articleMeta[file];
        schema = `
    <!-- Schema.org JSON-LD: Article -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "${meta.title}",
      "description": "${meta.desc}",
      "image": "${meta.image}",
      "datePublished": "${meta.date}",
      "dateModified": "${meta.date}",
      "author": {
        "@type": "Person",
        "name": "${meta.author}"
      },
      "publisher": {
        "@type": "Organization",
        "name": "Mind & Balance",
        "logo": {
          "@type": "ImageObject",
          "url": "https://leafanoo.com/images/favicon.svg"
        }
      },
      "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://leafanoo.com/${file}"
      }
    }
    </script>
    <!-- End Schema.org -->`;
    } else if (file === 'index.html') {
        schema = `
    <!-- Schema.org JSON-LD: WebSite -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "WebSite",
      "name": "Mind & Balance",
      "url": "https://leafanoo.com/",
      "description": "Explore insights on psychology, mental health, and emotional well-being.",
      "potentialAction": {
        "@type": "SearchAction",
        "target": "https://leafanoo.com/?s={search_term_string}",
        "query-input": "required name=search_term_string"
      }
    }
    </script>
    <!-- End Schema.org -->`;
    }

    // Inject canonical + schema just before </head>
    const injection = `${canonicalTag}${schema}`;
    content = content.replace('</head>', `${injection}\n</head>`);

    fs.writeFileSync(filePath, content, 'utf8');
    console.log(`✅ Fixed SEO on ${file}${isArticle ? ' [Article Schema + Canonical + og:type fix]' : ' [WebSite Schema + Canonical]'}`);
});

console.log('\n🚀 SEO Audit Fixes Complete!');
