// --- Navigation Burger Menu ---
const burger = document.querySelector('.burger');
const navRight = document.querySelector('.nav-right');
const navLinks = document.querySelectorAll('.nav-links li');

if (burger) {
    burger.addEventListener('click', () => {
        // Toggle Nav
        navRight.classList.toggle('nav-active');

        // Animate Links
        navLinks.forEach((link, index) => {
            if (link.style.animation) {
                link.style.animation = '';
            } else {
                link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 0.3}s`;
            }
        });

        // Burger Animation
        burger.classList.toggle('toggle');
    });
}

// Add CSS keyframes dynamically for navLinks
const style = document.createElement('style');
style.innerHTML = `
    @keyframes navLinkFade {
        from {
            opacity: 0;
            transform: translateX(50px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
`;
document.head.appendChild(style);

// --- Set current year in footer ---
const yearSpan = document.getElementById('year');
if (yearSpan) {
    yearSpan.textContent = new Date().getFullYear();
}

// --- Theme Toggle (Dark Mode) ---
const themeToggle = document.getElementById('theme-toggle');
const rootElement = document.documentElement;

// Check local storage for preference
const currentTheme = localStorage.getItem('theme');
if (currentTheme) {
    rootElement.setAttribute('data-theme', currentTheme);
    if(themeToggle) themeToggle.textContent = currentTheme === 'dark' ? '☀️' : '🌙';
}

if(themeToggle) {
    themeToggle.addEventListener('click', () => {
        let theme = rootElement.getAttribute('data-theme');
        if (theme === 'dark') {
            rootElement.removeAttribute('data-theme');
            localStorage.setItem('theme', 'light');
            themeToggle.textContent = '🌙';
        } else {
            rootElement.setAttribute('data-theme', 'dark');
            localStorage.setItem('theme', 'dark');
            themeToggle.textContent = '☀️';
        }
    });
}

// --- Scroll Reveal Animations ---
const observerOptions = {
    threshold: 0.1,
    rootMargin: "0px 0px -50px 0px"
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('show');
            observer.unobserve(entry.target); // Optional: only animate once
        }
    });
}, observerOptions);

const hiddenElements = document.querySelectorAll('.hidden');
hiddenElements.forEach((el) => observer.observe(el));

// --- Reading Progress Bar ---
const progressBar = document.getElementById('progress-bar');
window.addEventListener('scroll', () => {
    if (progressBar) {
        const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
        const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const scrolled = (winScroll / height) * 100;
        progressBar.style.width = scrolled + "%";
    }
});

// --- Parallax Effect on Hero ---
const heroImg = document.querySelector('.hero-img');
window.addEventListener('scroll', () => {
    if(heroImg) {
        let scrollPos = window.scrollY;
        heroImg.style.transform = `translateY(${scrollPos * 0.4}px)`;
    }
});

// --- Mood Widget Logic ---
function initMoodWidget() {
    const buttons = document.querySelectorAll('.mood-btn');
    const resultText = document.getElementById('mood-result-text');
    
    if(!buttons.length || !resultText) return;

    const insights = {
        'stressed': "Take a deep breath. Focus on what you can control right now.",
        'anxious': "It's okay to feel this way. Try the 5-4-3-2-1 grounding technique.",
        'unmotivated': "Action often precedes motivation. Try doing just one small thing for 5 minutes.",
        'okay': "Maintenance is progress. Enjoy the calm and stay present.",
        'great': "Wonderful! Channel this energy into something creative or share it with others."
    };

    buttons.forEach(btn => {
        btn.addEventListener('click', () => {
            const mood = btn.getAttribute('data-mood');
            if(insights[mood]) {
                resultText.style.opacity = 0;
                setTimeout(() => {
                    resultText.textContent = insights[mood];
                    resultText.style.opacity = 1;
                }, 300);
            }
        });
    });
}
initMoodWidget();

// --- Cookie Consent Banner ---
function initCookieBanner() {
    if (!localStorage.getItem('cookieConsent')) {
        const bannerHTML = `
            <div id="cookie-banner" class="cookie-banner">
                <div class="cookie-content">
                    <p>We use cookies and similar technologies to enhance your browsing experience, serve personalized ads, and analyze our traffic. By clicking "Accept All", you consent to our use of cookies as described in our <a href="privacy-policy.html">Privacy Policy</a>.</p>
                </div>
                <div class="cookie-buttons">
                    <button id="accept-cookies" class="btn-primary" style="padding: 0.5rem 1.5rem; font-size: 0.9rem;">Accept All</button>
                </div>
            </div>
        `;
        document.body.insertAdjacentHTML('beforeend', bannerHTML);

        document.getElementById('accept-cookies').addEventListener('click', () => {
            localStorage.setItem('cookieConsent', 'true');
            const banner = document.getElementById('cookie-banner');
            banner.style.opacity = '0';
            setTimeout(() => banner.remove(), 400);
        });
    }
}
document.addEventListener('DOMContentLoaded', initCookieBanner);

// --- Lazy-Load AdSense for Core Web Vitals Optimization ---
function initLazyAds() {
    const adContainers = document.querySelectorAll('.ad-container ins.adsbygoogle');
    if ('IntersectionObserver' in window && adContainers.length > 0) {
        let adObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    // Load the AdSense script if not already present
                    if (!window.adsbygoogle_loaded) {
                        const script = document.createElement('script');
                        script.src = "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6659437008463310";
                        script.async = true;
                        script.crossOrigin = "anonymous";
                        document.head.appendChild(script);
                        window.adsbygoogle_loaded = true;
                    }
                    // Initialize the specific ad unit
                    (adsbygoogle = window.adsbygoogle || []).push({});
                    observer.unobserve(entry.target);
                }
            });
        }, { rootMargin: "200px" });

        adContainers.forEach(ad => adObserver.observe(ad));
    } else {
        // Fallback for older browsers
        adContainers.forEach(ad => (adsbygoogle = window.adsbygoogle || []).push({}));
    }
}
document.addEventListener('DOMContentLoaded', initLazyAds);
