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
