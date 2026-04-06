const fs = require('fs');
const path = require('path');

const dir = __dirname;
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

const ga4Script = `
    <!-- Google Analytics 4 -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-8KZ1C7KGQ3"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-8KZ1C7KGQ3');
    </script>
    <!-- End Google Analytics 4 -->`;

let injected = 0;
let skipped = 0;

files.forEach(file => {
    const filePath = path.join(dir, file);
    let content = fs.readFileSync(filePath, 'utf8');

    if (content.includes('G-8KZ1C7KGQ3')) {
        console.log(`⏭  Skipping ${file} - GA4 already installed.`);
        skipped++;
        return;
    }

    // Inject right after <head>
    content = content.replace(/<head>/i, `<head>${ga4Script}`);

    fs.writeFileSync(filePath, content, 'utf8');
    console.log(`✅ Injected GA4 into ${file}`);
    injected++;
});

console.log(`\n🎉 Done! Injected: ${injected} files | Skipped: ${skipped} files`);
