import os

BASE_DIR = "/Users/khalidaitelmaati/Desktop/scrapy-master/psychology-theme-main"
SCRIPTS_SNIPPET = """    <!-- Google Analytics 4 -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-8KZ1C7KGQ3"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-8KZ1C7KGQ3');
    </script>
    <!-- End Google Analytics 4 -->
    <!-- Google Tag Manager -->
    <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
    new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
    'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
    })(window,document,'script','dataLayer','GTM-MWJD24QX');</script>
    <!-- End Google Tag Manager -->
    <!-- Google Search Console Placeholder -->
    <meta name="google-site-verification" content="ADD_YOUR_GSC_CODE_HERE" />
"""

def inject_tracking_to_articles():
    files = [f for f in os.listdir(BASE_DIR) if f.startswith("article") and f.endswith(".html")]
    print(f"Found {len(files)} articles to update.")
    
    for file_name in files:
        file_path = os.path.join(BASE_DIR, file_name)
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Avoid double injection
        if "G-8KZ1C7KGQ3" in content:
            continue
            
        # Target the top of the head
        if "<head>" in content:
            updated_content = content.replace("<head>", f"<head>\n{SCRIPTS_SNIPPET}")
            with open(file_path, 'w') as f:
                f.write(updated_content)
            print(f"Updated {file_name}")

if __name__ == "__main__":
    inject_tracking_to_articles()
