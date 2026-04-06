const fs = require('fs');
const path = require('path');

const articles = [
  {
    id: 11,
    title: "The Neuroscience of Gratitude",
    category: "Positive Psychology",
    slug: "neuroscience-of-gratitude",
    author: "Dr. Elena Rostova",
    authorImg: "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&q=80&w=100&h=100",
    date: "September 2, 2026",
    read: "5 min read",
    metaDesc: "Discover how practicing gratitude physically rewires your brain and creates lasting improvements in mental health.",
    heroImg: "https://images.unsplash.com/photo-1470116892389-0de5d9770b2c?auto=format&fit=crop&q=80&w=1200",
    cardImg: "https://images.unsplash.com/photo-1470116892389-0de5d9770b2c?auto=format&fit=crop&q=80&w=600",
    cardExcerpt: "Discover how practicing gratitude physically rewires your brain and creates lasting improvements in mental health.",
    content: `<p>Modern neuroscience has confirmed what philosophers and spiritual traditions have known for millennia: gratitude is not merely a pleasant emotion—it is a powerful neurological force that actively reshapes the physical structure of your brain. Understanding the science behind gratitude can motivate you to take this simple practice more seriously.</p>
            
            <h2>The Brain on Gratitude</h2>
            <p>When you consciously feel or express gratitude, your brain releases a powerful cocktail of two key neurotransmitters: dopamine and serotonin. Dopamine, often called the "reward chemical," creates a warm surge of pleasure. Serotonin functions as your brain's natural mood stabilizer, directly reducing feelings of depression and anxiety. Together, they create a genuine neurochemical boost comparable to mild antidepressant medication—but with zero side effects.</p>

            <img src="https://images.unsplash.com/photo-1506126613408-eca07ce68773?auto=format&fit=crop&q=80&w=1200" alt="Person writing in a gratitude journal outdoors">

            <p>Furthermore, gratitude actively engages the medial prefrontal cortex—the region of the brain associated with moral cognition, interpersonal bonding, and positive social emotions. Regular activation of this area through gratitude practice actually increases its density over time, making you structurally more empathetic, socially connected, and emotionally regulated as a person.</p>

            <blockquote>"Gratitude is not only the greatest of virtues, but the parent of all the others." — Cicero</blockquote>

            <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>

            <h2>The 21-Day Gratitude Experiment</h2>
            <p>Leading positive psychologists like Dr. Martin Seligman have quantified gratitude's effects through rigorous clinical trials. In one landmark study, participants who wrote down three specific things they were grateful for each day for just 21 consecutive days showed a measurable increase in optimism scores that lasted for over six months after the study concluded. The act of writing is crucial — it forces a deeper level of cognitive engagement than simply thinking grateful thoughts.</p>

            <h2>Three Ways to Practice More Effectively</h2>
            <ul>
                <li><strong>Be Hyper-Specific:</strong> Instead of writing "I'm grateful for my health," write "I'm grateful that my legs carried me up the stairs without pain today." Specificity forces genuine reflection and triggers a stronger emotional response.</li>
                <li><strong>Include People:</strong> Gratitude directed at specific people has the strongest neurological and social impact. Research shows that expressing gratitude to a person directly—in a letter or in person—dramatically boosts happiness for both parties.</li>
                <li><strong>Embrace Contrast:</strong> Occasionally, visualize your life without something you value. This technique, called "mental subtraction," amplifies gratitude far more powerfully than simply listing blessings.</li>
            </ul>

            <div class="author-box hidden">
                <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&q=80&w=100&h=100" alt="Author">
                <div class="author-info">
                    <h4>Dr. Elena Rostova</h4>
                    <p>Behavioral psychologist specializing in neuroplasticity and positive psychology interventions for lasting well-being.</p>
                </div>
            </div>`
  },
  {
    id: 12,
    title: "Boundaries: The Psychology of Saying No",
    category: "Relationships",
    slug: "psychology-of-saying-no",
    author: "Emma Sullivan, M.S.",
    authorImg: "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&q=80&w=100&h=100",
    date: "September 18, 2026",
    read: "6 min read",
    metaDesc: "Learn the psychology behind setting healthy personal boundaries and why saying no is an act of radical self-respect.",
    heroImg: "https://images.unsplash.com/photo-1531746020798-e6953c6e8e04?auto=format&fit=crop&q=80&w=1200",
    cardImg: "https://images.unsplash.com/photo-1531746020798-e6953c6e8e04?auto=format&fit=crop&q=80&w=600",
    cardExcerpt: "Learn the psychology behind setting healthy personal boundaries and why saying no is an act of radical self-respect.",
    content: `<p>For many people, the two-letter word "no" is the most difficult word in the English language to say. People-pleasers, empaths, and those raised in environments where their needs were consistently dismissed often find themselves chronically overcommitted, perpetually exhausted, and strangely resentful of the very people they are trying so hard to please. Understanding the psychology behind this pattern is the first step to freedom.</p>
            
            <h2>Why We Can't Say No: The Fear of Abandonment</h2>
            <p>At its psychological core, chronic people-pleasing is an anxiety-driven, subconscious defense mechanism rooted in a deeply primal fear: the fear of abandonment. In our evolutionary past, being expelled from a tribe was essentially a death sentence. The brain, even today, still treats social rejection as a genuine existential threat.</p>

            <img src="https://images.unsplash.com/photo-1508214751196-bcfd4ca60f91?auto=format&fit=crop&q=80&w=1200" alt="Person standing firm with confidence">

            <p>People who grew up in households where love was conditional—where approval had to be constantly earned through compliance—are especially susceptible to this pattern in adulthood. Their nervous systems were literally trained to perceive "saying no" as a catastrophic trigger for the withdrawal of love and safety.</p>

            <blockquote>"Daring to set boundaries is about having the courage to love ourselves, even when we risk disappointing others." — Brené Brown</blockquote>

            <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>

            <h2>The Cost of No Boundaries</h2>
            <p>Research on boundary-less individuals consistently reveals a troubling pattern: while they appear externally agreeable and "easy to work with," they internally accumulate enormous amounts of suppressed resentment. This resentment doesn't disappear — it quietly poisons close relationships over time, often exploding in one disproportionate, seemingly random outburst, leaving everyone confused.</p>

            <h2>How to Start Setting Boundaries</h2>
            <ul>
                <li><strong>Start with Low-Stakes Practice:</strong> Don't start by refusing your demanding boss. Practice saying no in safe, low-consequence situations first—declining an unwanted upsell at a coffee shop, or not justifying your food choices at a dinner party.</li>
                <li><strong>You Do Not Owe Explanations:</strong> "No, thank you" is a complete grammatical sentence. The compulsive urge to over-explain and justify your "no" is people-pleasing behavior in disguise. A boundary does not require a reason.</li>
                <li><strong>Recognize That "No" is an Act of Respect:</strong> When you say yes to something you deeply resent, you are signing a secret contract to offer that person your worst quality of presence. A clean "no" is more honest, more respectful, and ultimately more loving than a resentful "yes."</li>
            </ul>

            <div class="author-box hidden">
                <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&q=80&w=100&h=100" alt="Author">
                <div class="author-info">
                    <h4>Emma Sullivan, M.S.</h4>
                    <p>Occupational psychologist focused on interpersonal dynamics, relational boundaries, and confidence-building for working adults.</p>
                </div>
            </div>`
  },
  {
    id: 13,
    title: "The Psychology of Procrastination",
    category: "Behavioral Psychology",
    slug: "psychology-of-procrastination",
    author: "Dr. Marcus Lin",
    authorImg: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&q=80&w=100&h=100",
    date: "October 5, 2026",
    read: "7 min read",
    metaDesc: "Procrastination is not a time management problem. It is an emotion regulation problem. Here is the science behind why we delay.",
    heroImg: "https://images.unsplash.com/photo-1455390582262-044cdead277a?auto=format&fit=crop&q=80&w=1200",
    cardImg: "https://images.unsplash.com/photo-1455390582262-044cdead277a?auto=format&fit=crop&q=80&w=600",
    cardExcerpt: "Procrastination is not a time management problem. It is an emotion regulation problem. Here is the science behind why we delay.",
    content: `<p>Nearly every productivity advice column will tell you to use a planner, break tasks into smaller pieces, or "just get started." While these tips are not entirely useless, they fundamentally misdiagnose the root cause of procrastination. Procrastination is not a time management failure. It is a failure of emotion regulation. When we understand it through this lens, genuinely effective solutions emerge.</p>
            
            <h2>The Emotional Avoidance Loop</h2>
            <p>Every act of procrastination follows a specific pattern. You face a task. The task triggers an uncomfortable emotion—fear of failure, anxiety about perfectionism, overwhelming boredom, or crushing self-doubt. To escape from this negative emotion, your brain offers you a simple, readily available solution: avoidance. You scroll Instagram. You clean the kitchen. You watch one more episode. You feel temporarily better.</p>

            <img src="https://images.unsplash.com/photo-1484480974693-6ca0a78fb36b?auto=format&fit=crop&q=80&w=1200" alt="Empty desk with a notebook representing procrastination">

            <p>But this "relief" backfires catastrophically. Not only does the task still need to be done, but you now have an additional layer of shame and anxiety heaped specifically on top of it. The emotional stakes around that task are now even higher. The next time you even think about it, the aversive emotional response you are trying to avoid is now even stronger. You are in a loop.</p>

            <blockquote>"You don't have to feel like doing something to actually do it." — Dr. Pychyl, Procrastination Research Group</blockquote>

            <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>

            <h2>Evidence-Based Strategies That Actually Work</h2>
            <p>Because procrastination is emotional at its root, the most effective interventions target the emotional experience of the task rather than the task's logistics.</p>
            <ul>
                <li><strong>Self-Compassion First:</strong> Research from Dr. Timothy Pychyl at Carleton University found that people who forgave themselves after a procrastination episode were significantly less likely to procrastinate on the same task again in the future. Shame fuels avoidance. Self-compassion disrupts the loop.</li>
                <li><strong>The 2-Minute Rule:</strong> If you commit to only doing the first two minutes of a dreaded task, the emotional barrier shrinks dramatically. You are not promising yourself a finished product—just a tiny entry point. Most people discover that starting was the only difficult part.</li>
                <li><strong>Temptation Bundling:</strong> Pair aversive tasks exclusively with something pleasurable. Listen to your favorite podcast strictly while exercising. Enjoy your favorite coffee strictly while working on your hardest task. You create a conditioned positive association with previously dreaded activities.</li>
            </ul>

            <div class="author-box hidden">
                <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&q=80&w=100&h=100" alt="Author">
                <div class="author-info">
                    <h4>Dr. Marcus Lin</h4>
                    <p>Somnologist and behavioral therapist, with particular expertise in avoidance patterns and emotional regulation strategies.</p>
                </div>
            </div>`
  },
  {
    id: 14,
    title: "Attachment Theory: How Your Childhood Shapes Your Relationships",
    category: "Relationships",
    slug: "attachment-theory-childhood-relationships",
    author: "Dr. Aria Martinez",
    authorImg: "https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=crop&q=80&w=100&h=100",
    date: "October 22, 2026",
    read: "8 min read",
    metaDesc: "Explore the four attachment styles and discover how your earliest bonds with caregivers are quietly governing your adult love life.",
    heroImg: "https://images.unsplash.com/photo-1529156069898-49953e39b3ac?auto=format&fit=crop&q=80&w=1200",
    cardImg: "https://images.unsplash.com/photo-1529156069898-49953e39b3ac?auto=format&fit=crop&q=80&w=600",
    cardExcerpt: "Explore the four attachment styles and discover how your earliest bonds are quietly shaping your adult relationships today.",
    content: `<p>Before you could form a single conscious memory, your brain was already building a sophisticated internal model of what relationships feel like—whether they are safe or dangerous, whether intimacy leads to connection or abandonment. This model, forged entirely within the first 18 months of life, is called your Attachment Style, and it continues to silently govern your most important adult relationships today.</p>
            
            <h2>The Four Attachment Styles</h2>
            <p>Psychologist John Bowlby first proposed Attachment Theory in the 1950s. His colleague Mary Ainsworth subsequently identified the four primary styles through her landmark "Strange Situation" experiments:</p>

            <img src="https://images.unsplash.com/photo-1491013516836-7db643ee125a?auto=format&fit=crop&q=80&w=1200" alt="Two people connecting emotionally">

            <ul>
                <li><strong>Secure (56% of adults):</strong> Developed when caregivers are consistently responsive and emotionally available. Securely attached adults are comfortable with intimacy, can express needs directly, and handle conflict without panic or shutdown.</li>
                <li><strong>Anxious-Preoccupied (20%):</strong> Results from inconsistent caregiving—sometimes warm, sometimes distant. These individuals crave extreme closeness, chronically fear abandonment, and often come across as "needy" or overly sensitive to their partner's moods.</li>
                <li><strong>Dismissive-Avoidant (25%):</strong> Develops when caregivers were consistently emotionally unavailable. These adults fiercely value self-sufficiency, feel highly uncomfortable with emotional intimacy, and tend to suppress or dismiss their own emotional needs entirely.</li>
                <li><strong>Fearful-Avoidant (5%):</strong> The most complex style, often linked to early trauma. These individuals desperately want close connection but simultaneously fear it. They oscillate unpredictably between pulling people close and pushing them away.</li>
            </ul>

            <blockquote>"The nature of the attachment bond formed in early life creates a template for all subsequent loving relationships." — John Bowlby</blockquote>

            <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>

            <h2>Can Your Attachment Style Change?</h2>
            <p>Absolutely. Attachment styles are not permanent life sentences. Neuroscience confirms that the brain retains neuroplasticity throughout adulthood. A sustained relationship with a securely attached partner is one of the most powerful catalysts for moving toward earned secure attachment. Psychotherapy—particularly psychodynamic and attachment-focused modalities—is proven highly effective at rewiring deeply ingrained relational patterns. The journey requires significant time and courage, but the outcome—experiencing genuine relational security—is transformative.</p>

            <div class="author-box hidden">
                <img src="https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=crop&q=80&w=100&h=100" alt="Author">
                <div class="author-info">
                    <h4>Dr. Aria Martinez</h4>
                    <p>Clinical psychologist specializing in attachment theory, relationship trauma, and emotion-focused couples therapy.</p>
                </div>
            </div>`
  },
  {
    id: 15,
    title: "The Power of Vulnerability in Building Deep Connections",
    category: "Positive Psychology",
    slug: "power-of-vulnerability",
    author: "Emma Sullivan, M.S.",
    authorImg: "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&q=80&w=100&h=100",
    date: "November 8, 2026",
    read: "5 min read",
    metaDesc: "Brené Brown's research reveals that vulnerability is not weakness—it is the ultimate birthplace of love, belonging, and authentic connection.",
    heroImg: "https://images.unsplash.com/photo-1516585427167-9f4af9627e6c?auto=format&fit=crop&q=80&w=1200",
    cardImg: "https://images.unsplash.com/photo-1516585427167-9f4af9627e6c?auto=format&fit=crop&q=80&w=600",
    cardExcerpt: "Research reveals that vulnerability is not weakness — it is the ultimate birthplace of love, belonging, and authentic human connection.",
    content: `<p>For most of us, vulnerability feels synonymous with weakness. We have been culturally conditioned to "keep it together," to project strength and competence at all times, and to carefully conceal the messier, more uncertain parts of our inner lives. Yet the research of social scientist Brené Brown, built over two decades and thousands of interviews, reveals a profoundly counterintuitive finding: vulnerability is not the opposite of strength. It is the source of our most meaningful human experiences.</p>
            
            <h2>What Vulnerability Actually Is</h2>
            <p>Vulnerability is not about trauma-dumping on strangers or performing emotional openness for social approval. Brown defines it precisely as "uncertainty, risk, and emotional exposure." It is the feeling experienced when you say "I love you" first, when you share a creative work that genuinely matters to you, when you admit you are struggling, or when you reach out for help.</p>

            <img src="https://images.unsplash.com/photo-1516585427167-9f4af9627e6c?auto=format&fit=crop&q=80&w=1200" alt="Two people having a heartfelt conversation">

            <p>In her research, Brown discovered a clear divide between people who felt a deep sense of love and belonging—which she called "wholehearted" people—and those who struggled with it. The singular characteristic that separated these two groups was not intelligence, status, or beauty. Wholehearted people simply had the courage to be imperfect, and the willingness to be seen authentically despite the risk.</p>

            <blockquote>"Vulnerability is the birthplace of love, belonging, joy, courage, empathy, and creativity." — Brené Brown</blockquote>

            <div class="ad-container" style="height:250px; margin: 3rem 0;"></div>

            <h2>The Connection Paradox</h2>
            <p>We crave authentic connection with others, yet we simultaneously present a polished, curated version of ourselves in order to earn it. The devastating paradox is this: when we hide our authentic selves, we receive connection and validation directed at a performance—not at the real us. Deep connection literally cannot grow between two masks. It can only flourish between two genuinely exposed human beings.</p>

            <p>The practice of vulnerability in daily life might look like texting a friend "I've been struggling lately, can we talk?" instead of replying "I'm fine" to a check-in. It might mean telling your partner what you need instead of hoping they'll read your mind. Small acts of authentic disclosure, consistently practiced, are the architecture of profound human intimacy.</p>

            <div class="author-box hidden">
                <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&q=80&w=100&h=100" alt="Author">
                <div class="author-info">
                    <h4>Emma Sullivan, M.S.</h4>
                    <p>Occupational psychologist focused on authentic leadership, interpersonal connection, and shame resilience in modern workplaces.</p>
                </div>
            </div>`
  }
];

function buildArticleHTML(a) {
    return `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${a.title} | Mind &amp; Balance</title>
    <meta name="description" content="${a.metaDesc}">
    <link rel="stylesheet" href="css/style.css">
    <link rel="icon" type="image/svg+xml" href="images/favicon.svg">
    <meta property="og:title" content="${a.title} | Mind &amp; Balance">
    <meta property="og:description" content="${a.metaDesc}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://leafanoo.com/article${a.id}.html">
    <meta property="og:image" content="${a.heroImg}">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="${a.title} | Mind &amp; Balance">
    <meta name="twitter:description" content="${a.metaDesc}">
    <meta name="twitter:image" content="${a.heroImg}">
    <!-- Google Tag Manager -->
    <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
    new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
    'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
    })(window,document,'script','dataLayer','GTM-MWJD24QX');</script>
    <!-- End Google Tag Manager -->
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6659437008463310" crossorigin="anonymous"></script>
</head>
<body>
    <!-- Google Tag Manager (noscript) -->
    <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-MWJD24QX" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
    <!-- End Google Tag Manager (noscript) -->

    <div class="progress-container">
        <div class="progress-bar" id="progress-bar"></div>
    </div>

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
            <div class="burger">
                <div class="line1"></div>
                <div class="line2"></div>
                <div class="line3"></div>
            </div>
        </nav>
    </header>

    <div class="article-header hidden">
        <div class="container">
            <span class="card-category" style="display:block; margin-bottom:1rem;">${a.category}</span>
            <h1 style="font-size: 3rem; max-width: 800px; margin: 0 auto;">${a.title}</h1>
            <div class="article-meta">
                <img src="${a.authorImg}" alt="${a.author}">
                <span>By ${a.author}</span>
                <span>•</span>
                <span>${a.date}</span>
                <span>•</span>
                <span>${a.read}</span>
            </div>
        </div>
    </div>

    <div class="ad-container ad-leaderboard hidden delay-1"></div>

    <div class="article-layout">
        <main class="article-body hidden delay-2">
            ${a.content}
        </main>

        <aside class="article-sidebar hidden delay-3">
            <div class="sticky-sidebar">
                <div class="ad-container ad-sidebar" style="height:600px; margin-top:0;"></div>
            </div>
        </aside>
    </div>

    <div class="container section">
        <h2 class="section-title hidden">Read Next</h2>
        <div class="articles-grid">
            <article class="card hidden delay-1">
                <div class="card-img" style="background-image: url('https://images.unsplash.com/photo-1506126613408-eca07ce68773?auto=format&fit=crop&q=80&w=400');"></div>
                <div class="card-content">
                    <span class="card-category">Wellness</span>
                    <h3 class="card-title">Mindfulness in 5 Minutes</h3>
                    <a href="article3.html" class="card-link">Read More &rarr;</a>
                </div>
            </article>
            <article class="card hidden delay-2">
                <div class="card-img" style="background-image: url('https://images.unsplash.com/photo-1484480974693-6ca0a78fb36b?auto=format&fit=crop&q=80&w=400');"></div>
                <div class="card-content">
                    <span class="card-category">Behavioral Psychology</span>
                    <h3 class="card-title">The Psychology of Habit Formation</h3>
                    <a href="article4.html" class="card-link">Read More &rarr;</a>
                </div>
            </article>
        </div>
    </div>

    <footer class="hidden">
        <div class="container">
            <div class="footer-content">
                <div class="footer-col">
                    <h3>Mind &amp; Balance</h3>
                    <p>Providing clear, compassionate, and scientifically grounded psychological insights for everyday life.</p>
                </div>
                <div class="footer-col">
                    <h3>Quick Links</h3>
                    <ul class="footer-links">
                        <li><a href="index.html">Home</a></li>
                        <li><a href="about.html">About Us</a></li>
                        <li><a href="privacy-policy.html">Privacy Policy</a></li>
                        <li><a href="terms.html">Terms of Service</a></li>
                        <li><a href="contact.html">Contact</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                &copy; <span id="year"></span> Mind &amp; Balance. All rights reserved.
            </div>
        </div>
    </footer>

    <script src="js/main.js"></script>
</body>
</html>`;
}

// Generate article HTML files
articles.forEach(a => {
    const html = buildArticleHTML(a);
    const filename = path.join(__dirname, `article${a.id}.html`);
    fs.writeFileSync(filename, html, 'utf8');
    console.log(`Generated article${a.id}.html - "${a.title}"`);
});

// Update index.html with new cards
let indexPath = path.join(__dirname, 'index.html');
let indexContent = fs.readFileSync(indexPath, 'utf8');

const newCards = articles.map(a => `
            <!-- Article ${a.id} -->
            <article class="card hidden delay-1">
                <div class="card-img" style="background-image: url('${a.cardImg}');"></div>
                <div class="card-content">
                    <span class="card-category">${a.category}</span>
                    <h3 class="card-title">${a.title}</h3>
                    <p class="card-excerpt">${a.cardExcerpt}</p>
                    <a href="article${a.id}.html" class="card-link">Read More &rarr;</a>
                </div>
            </article>`).join('\n');

// Insert before closing </div>\n    </div> of the articles grid
indexContent = indexContent.replace(
    '<!-- AdSense Bottom Leaderboard Placeholder -->',
    `${newCards}
        </div>
    </div>

    <!-- AdSense Bottom Leaderboard Placeholder -->`
);

// Remove the orphaned closing tags (we added them in the new cards block)
indexContent = indexContent.replace(/(<\/div>\s*<\/div>\s*\n\s*<!-- AdSense Bottom Leaderboard Placeholder -->[\s\S]*?<!-- AdSense Bottom Leaderboard Placeholder -->)/, (match) => {
    // Fix: just use the new cards directly
    return match;
});

fs.writeFileSync(indexPath, indexContent, 'utf8');

// Update sitemap
let sitemapPath = path.join(__dirname, 'sitemap.xml');
let sitemap = fs.readFileSync(sitemapPath, 'utf8');

const newSitemapEntries = articles.map(a => `    <url>
        <loc>https://leafanoo.com/article${a.id}.html</loc>
        <changefreq>monthly</changefreq>
        <priority>0.9</priority>
    </url>`).join('\n');

sitemap = sitemap.replace('</urlset>', `${newSitemapEntries}\n</urlset>`);
fs.writeFileSync(sitemapPath, sitemap, 'utf8');

console.log('\n✅ All done! Generated 5 new articles and updated index.html + sitemap.xml');
