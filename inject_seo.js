const fs = require('fs');
const path = require('path');

const dir = __dirname;
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

files.forEach(file => {
    const filePath = path.join(dir, file);
    let content = fs.readFileSync(filePath, 'utf8');
    
    // Skip if already injected to avoid duplicating tags if run twice
    if (content.includes('property="og:title"')) {
        console.log(`Skipping ${file} - OG tags already exist.`);
        return;
    }

    // Extract title and description
    const titleMatch = content.match(/<title>(.*?)<\/title>/i);
    const descMatch = content.match(/<meta[^>]*name=["']description["'][^>]*content=["'](.*?)["']/i);
    
    const title = titleMatch ? titleMatch[1] : 'Mind & Balance | Psychology & Wellness';
    const description = descMatch ? descMatch[1] : 'Explore insights on psychology, mental health, and emotional well-being.';
    const url = `https://leafanoo.com/${file === 'index.html' ? '' : file}`;
    // For articles we could use a specific image, but using the hero image is a solid fallback for all pages.
    const image = 'https://leafanoo.com/images/hero.png';

    const ogTags = `
    <!-- Open Graph / SEO Meta Tags -->
    <meta property="og:title" content="${title}">
    <meta property="og:description" content="${description}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="${url}">
    <meta property="og:image" content="${image}">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="${title}">
    <meta name="twitter:description" content="${description}">
    <meta name="twitter:image" content="${image}">`;

    // Inject just before </head>
    content = content.replace('</head>', `${ogTags}\n</head>`);
    
    fs.writeFileSync(filePath, content, 'utf8');
    console.log(`Successfully injected SEO tags into ${file}`);
});
