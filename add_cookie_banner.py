#!/usr/bin/env python3
"""
Adds a GDPR/CCPA compliant Cookie Consent banner to all HTML files.
Required for Google AdSense approval in EU/UK regions.
"""
import os
import re

BASE_DIR = "/Users/khalidaitelmaati/Desktop/scrapy-master/psychology-theme-main"

COOKIE_BANNER_HTML = """
    <!-- GDPR Cookie Consent Banner -->
    <div id="cookie-consent-banner" style="position: fixed; bottom: 0; left: 0; width: 100%; background: #2c3e50; color: #fff; padding: 1.5rem; z-index: 9999; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 -4px 10px rgba(0,0,0,0.1); font-size: 0.95rem; flex-wrap: wrap; gap: 1rem;">
        <div style="flex: 1; min-width: 300px;">
            <strong style="font-size: 1.1rem; display: block; margin-bottom: 0.5rem; color: #ecf0f1;">We value your privacy</strong>
            We use cookies to enhance your browsing experience, serve personalized ads, and analyze our traffic. By clicking "Accept All", you consent to our use of cookies in accordance with our <a href="privacy-policy.html" style="color: #3498db; text-decoration: underline;">Privacy Policy</a>.
        </div>
        <div style="display: flex; gap: 1rem; align-items: center;">
            <button id="reject-cookies" style="background: transparent; border: 1px solid #7f8c8d; color: #ecf0f1; padding: 0.75rem 1.5rem; border-radius: 6px; cursor: pointer; font-weight: bold; transition: all 0.3s;">Reject Non-Essential</button>
            <button id="accept-cookies" style="background: #3498db; border: none; color: white; padding: 0.75rem 1.5rem; border-radius: 6px; cursor: pointer; font-weight: bold; transition: background 0.3s;">Accept All</button>
        </div>
    </div>
    <script>
        document.addEventListener("DOMContentLoaded", function() {
            if (!localStorage.getItem("cookieConsent")) {
                document.getElementById("cookie-consent-banner").style.display = "flex";
            } else {
                document.getElementById("cookie-consent-banner").style.display = "none";
            }
            
            document.getElementById("accept-cookies").addEventListener("click", function() {
                localStorage.setItem("cookieConsent", "accepted");
                document.getElementById("cookie-consent-banner").style.display = "none";
                // Trigger AdSense or Analytics if held back
            });
            
            document.getElementById("reject-cookies").addEventListener("click", function() {
                localStorage.setItem("cookieConsent", "rejected");
                document.getElementById("cookie-consent-banner").style.display = "none";
            });
        });
    </script>
</body>
"""

def add_cookie_banner():
    files = [f for f in os.listdir(BASE_DIR) if f.endswith(".html")]
    count = 0
    for file_name in files:
        file_path = os.path.join(BASE_DIR, file_name)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        if 'id="cookie-consent-banner"' in content:
            continue

        if '</body>' in content:
            new_content = content.replace('</body>', COOKIE_BANNER_HTML)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1

    print(f"✅ Added GDPR Cookie Consent banner to {count} HTML files.")

if __name__ == "__main__":
    add_cookie_banner()
