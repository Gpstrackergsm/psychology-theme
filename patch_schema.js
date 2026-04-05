const fs = require('fs');
const path = require('path');

const dir = __dirname;

// Article metadata with correct ISO 8601 dates + author URLs
const articleMeta = {
  'article1.html':  { date: '2026-10-12T00:00:00+00:00', author: 'Dr. Sarah Jenkins',  authorUrl: 'https://leafanoo.com/about.html' },
  'article2.html':  { date: '2026-11-01T00:00:00+00:00', author: 'Dr. Elena Rostova',  authorUrl: 'https://leafanoo.com/about.html' },
  'article3.html':  { date: '2026-11-15T00:00:00+00:00', author: 'Emma Sullivan',       authorUrl: 'https://leafanoo.com/about.html' },
  'article4.html':  { date: '2026-03-15T00:00:00+00:00', author: 'Dr. Elena Rostova',  authorUrl: 'https://leafanoo.com/about.html' },
  'article5.html':  { date: '2026-02-22T00:00:00+00:00', author: 'Emma Sullivan',       authorUrl: 'https://leafanoo.com/about.html' },
  'article6.html':  { date: '2026-04-01T00:00:00+00:00', author: 'Dr. Marcus Lin',     authorUrl: 'https://leafanoo.com/about.html' },
  'article7.html':  { date: '2026-05-10T00:00:00+00:00', author: 'David Chen',         authorUrl: 'https://leafanoo.com/about.html' },
  'article8.html':  { date: '2026-06-08T00:00:00+00:00', author: 'Dr. Aria Martinez',  authorUrl: 'https://leafanoo.com/about.html' },
  'article9.html':  { date: '2026-07-21T00:00:00+00:00', author: 'Dr. Sarah Jenkins',  authorUrl: 'https://leafanoo.com/about.html' },
  'article10.html': { date: '2026-08-05T00:00:00+00:00', author: 'David Chen',         authorUrl: 'https://leafanoo.com/about.html' },
  'article11.html': { date: '2026-09-02T00:00:00+00:00', author: 'Dr. Elena Rostova',  authorUrl: 'https://leafanoo.com/about.html' },
  'article12.html': { date: '2026-09-18T00:00:00+00:00', author: 'Emma Sullivan',       authorUrl: 'https://leafanoo.com/about.html' },
  'article13.html': { date: '2026-10-05T00:00:00+00:00', author: 'Dr. Marcus Lin',     authorUrl: 'https://leafanoo.com/about.html' },
  'article14.html': { date: '2026-10-22T00:00:00+00:00', author: 'Dr. Aria Martinez',  authorUrl: 'https://leafanoo.com/about.html' },
  'article15.html': { date: '2026-11-08T00:00:00+00:00', author: 'Emma Sullivan',       authorUrl: 'https://leafanoo.com/about.html' },
};

let fixed = 0;

Object.entries(articleMeta).forEach(([file, meta]) => {
  const filePath = path.join(dir, file);
  if (!fs.existsSync(filePath)) return;

  let content = fs.readFileSync(filePath, 'utf8');

  // Fix 1 & 2: Replace short date strings with full ISO 8601 in JSON-LD blocks only
  // We target the pattern inside script[type="application/ld+json"] carefully
  // Replace "datePublished": "YYYY-MM-DD" with the full ISO version
  const shortDate = meta.date.split('T')[0]; // e.g. "2026-10-12"
  content = content
    .replace(
      `"datePublished": "${shortDate}"`,
      `"datePublished": "${meta.date}"`
    )
    .replace(
      `"dateModified": "${shortDate}"`,
      `"dateModified": "${meta.date}"`
    );

  // Fix 3: Add "url" to author object
  // Replace the author block (without url) with one that includes url
  const oldAuthor = `"author": {
        "@type": "Person",
        "name": "${meta.author}"
      }`;
  const newAuthor = `"author": {
        "@type": "Person",
        "name": "${meta.author}",
        "url": "${meta.authorUrl}"
      }`;

  if (content.includes(oldAuthor)) {
    content = content.replace(oldAuthor, newAuthor);
    fs.writeFileSync(filePath, content, 'utf8');
    console.log(`✅ Patched ${file} — ISO dates + author URL added`);
    fixed++;
  } else {
    // Try to find and patch any author block with this name
    const authorRegex = new RegExp(`"author":\\s*\\{\\s*"@type":\\s*"Person",\\s*"name":\\s*"${meta.author.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}"\\s*\\}`, 'g');
    if (authorRegex.test(content)) {
      content = content.replace(authorRegex, newAuthor);
      fs.writeFileSync(filePath, content, 'utf8');
      console.log(`✅ Patched ${file} (regex) — author URL added`);
      fixed++;
    } else {
      // Fix dates anyway even if author already has url
      fs.writeFileSync(filePath, content, 'utf8');
      console.log(`⚠️  ${file} — dates fixed, author block may already be correct`);
    }
  }
});

console.log(`\n🎯 Done! Patched ${fixed} article files with correct ISO dates and author URLs.`);
