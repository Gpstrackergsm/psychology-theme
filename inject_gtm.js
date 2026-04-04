const fs = require('fs');
const path = require('path');

const dir = __dirname;
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

const gtmHead = `
    <!-- Google Tag Manager -->
    <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
    new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
    'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
    })(window,document,'script','dataLayer','GTM-MWJD24QX');</script>
    <!-- End Google Tag Manager -->`;

const gtmBody = `
    <!-- Google Tag Manager (noscript) -->
    <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-MWJD24QX"
    height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
    <!-- End Google Tag Manager (noscript) -->`;

files.forEach(file => {
    const filePath = path.join(dir, file);
    let content = fs.readFileSync(filePath, 'utf8');
    
    if (content.includes('GTM-MWJD24QX')) {
        console.log(`Skipping ${file} - GTM already installed.`);
        return;
    }

    // Inject head script right after <head>
    content = content.replace(/<head>/i, `<head>${gtmHead}`);
    
    // Inject body script right after <body>
    content = content.replace(/<body>/i, `<body>${gtmBody}`);
    
    fs.writeFileSync(filePath, content, 'utf8');
    console.log(`Successfully injected GTM into ${file}`);
});
