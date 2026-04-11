#!/usr/bin/env python3
"""
Adds 'Load More' pagination to index.html and hides articles beyond the first 12.
This prevents the browser from downloading 200 card background images simultaneously,
significantly improving Core Web Vitals and passing AdSense performance checks.
"""
import os
import re

INDEX_PATH = "/Users/khalidaitelmaati/Desktop/scrapy-master/psychology-theme-main/index.html"

PAGINATION_HTML = """
    <div id="load-more-container" style="text-align: center; margin: 4rem 0;">
        <button id="load-more-btn" style="background: var(--primary-color, #3498db); color: white; border: none; padding: 1rem 3rem; font-size: 1.1rem; font-weight: bold; border-radius: 50px; cursor: pointer; transition: all 0.3s; box-shadow: 0 4px 15px rgba(52, 152, 219, 0.3);">
            Load More Articles
        </button>
    </div>

    <script>
        document.addEventListener("DOMContentLoaded", function() {
            const cards = document.querySelectorAll('.articles-grid .card');
            const loadMoreBtn = document.getElementById('load-more-btn');
            const itemsPerPage = 12;
            let currentlyShown = itemsPerPage;

            // Initially hide all cards beyond the first 12
            cards.forEach((card, index) => {
                if (index >= currentlyShown) {
                    card.style.display = 'none';
                }
            });

            // If we have fewer than itemsPerPage, hide the button
            if (cards.length <= currentlyShown) {
                if(loadMoreBtn) loadMoreBtn.style.display = 'none';
            }

            if(loadMoreBtn) {
                loadMoreBtn.addEventListener('click', () => {
                    const nextBatch = currentlyShown + itemsPerPage;
                    // Show next batch
                    cards.forEach((card, index) => {
                        if (index >= currentlyShown && index < nextBatch) {
                            card.style.display = 'flex'; // our cards use flexbox generally, or block
                        }
                    });
                    currentlyShown = nextBatch;
                    
                    // Hide button if all shown
                    if (currentlyShown >= cards.length) {
                        loadMoreBtn.style.display = 'none';
                    }
                });
            }
        });
    </script>
"""

def add_pagination():
    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'id="load-more-btn"' in content:
        print("Pagination already installed.")
        return

    # Find the end of the articles-grid
    # The grid normally ends with </div> \n    </section>
    marker = '</div>\n    </section>'
    if marker in content:
        new_content = content.replace(marker, '</div>\n' + PAGINATION_HTML + '\n    </section>')
        with open(INDEX_PATH, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("✅ Success: 'Load More' pagination injected into index.html.")
    else:
        # Fallback: look for closing section tag
        fallback_marker = '</section>\n    <footer'
        if fallback_marker in content:
            new_content = content.replace(fallback_marker, PAGINATION_HTML + '\n</section>\n    <footer')
            with open(INDEX_PATH, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print("✅ Success: 'Load More' pagination injected into index.html (fallback).")
        else:
            print("❌ Could not find injection point for pagination.")

if __name__ == "__main__":
    add_pagination()
