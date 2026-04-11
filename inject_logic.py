import sys

INDEX_PATH = 'index.html'

def inject_logic():
    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # 1. Insert load-more button after grid
    # 2. Insert script at end
    
    new_lines = []
    grid_found = False
    
    # We find the END of the articles-grid.
    # The articles-grid starts at line ~194. 
    # Let's look for the first </div> that isn't inside an <article>.
    
    in_grid = False
    in_article = False
    
    for i, line in enumerate(lines):
        new_lines.append(line)
        if '<div class="articles-grid">' in line:
            in_grid = True
        if '<article' in line:
            in_article = True
        if '</article>' in line:
            in_article = False
        
        # If we are in the grid, not in an article, and we hit a </div>, it's the end of the grid.
        if in_grid and not in_article and '</div>' in line:
            # Insert button here
            new_lines.append('''
        <div id="load-more-container" style="text-align: center; margin: 4rem 0;">
            <button id="load-more-btn" style="background: var(--primary-color, #3498db); color: white; border: none; padding: 1rem 3rem; font-size: 1.1rem; font-weight: bold; border-radius: 50px; cursor: pointer; transition: all 0.3s; box-shadow: 0 4px 15px rgba(52, 152, 219, 0.3);">
                Load More Articles
            </button>
        </div>
''')
            in_grid = False

    # Insert script before </body>
    final_lines = []
    script_inserted = False
    for line in new_lines:
        if '</body>' in line and not script_inserted:
            final_lines.append('''
    <script>
        document.addEventListener("DOMContentLoaded", function() {
            const grid = document.querySelector('.articles-grid');
            if (!grid) return;
            const cards = Array.from(grid.querySelectorAll('.card'));
            const filterBtns = document.querySelectorAll('.topic-tag');
            const loadMoreBtn = document.getElementById('load-more-btn');
            const itemsPerPage = 12;
            let currentFilter = 'all';
            let currentlyShown = itemsPerPage;

            function updateDisplay() {
                const filtered = cards.filter(card => {
                    if (currentFilter === 'all') return true;
                    const catSpan = card.querySelector('.card-category');
                    if (!catSpan) return false;
                    const catText = catSpan.textContent.toLowerCase();
                    return catText.includes(currentFilter.toLowerCase());
                });

                cards.forEach(card => {
                    card.style.display = 'none';
                    card.classList.remove('hidden'); // Remove the hidden class to allow display
                });
                
                filtered.slice(0, currentlyShown).forEach(card => {
                    card.style.display = 'flex';
                });

                if (loadMoreBtn) {
                    loadMoreBtn.style.display = (currentlyShown >= filtered.length) ? 'none' : 'inline-block';
                }
            }

            filterBtns.forEach(btn => {
                btn.addEventListener('click', () => {
                    filterBtns.forEach(b => b.classList.remove('active'));
                    btn.classList.add('active');
                    currentFilter = btn.getAttribute('data-topic') || 'all';
                    currentlyShown = itemsPerPage;
                    updateDisplay();
                    
                    // Scroll to articles
                    document.getElementById('articles').scrollIntoView({ behavior: 'smooth' });
                });
            });

            if (loadMoreBtn) {
                loadMoreBtn.addEventListener('click', () => {
                    currentlyShown += itemsPerPage;
                    updateDisplay();
                });
            }

            updateDisplay();
        });
    </script>
''')
            script_inserted = True
        final_lines.append(line)

    with open(INDEX_PATH, 'w', encoding='utf-8') as f:
        f.writelines(final_lines)
    print("Injected filtering logic into index.html.")

if __name__ == "__main__":
    inject_logic()
