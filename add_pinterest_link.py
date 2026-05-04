import glob, os
from bs4 import BeautifulSoup

BASE_DIR = '/Users/khalidaitelmaati/Desktop/scrapy-master/psychology-theme-main'
files = glob.glob(os.path.join(BASE_DIR, '*.html'))

updated_count = 0

for fp in files:
    try:
        html_content = open(fp, encoding='utf-8').read()
        soup = BeautifulSoup(html_content, 'html.parser')
        
        footer = soup.find('footer')
        if footer:
            # Check if pinterest is already in footer
            if 'pinterest.com' not in str(footer):
                # find the div inside the footer container that holds the links
                container = footer.find('div', class_='container')
                if container:
                    links_div = container.find('div', style=lambda value: value and 'margin-top: 1rem' in value)
                    if links_div:
                        # Create Pinterest link
                        pin_link = soup.new_tag('a', href='https://www.pinterest.com/leafanoo', target='_blank', rel='noopener noreferrer', style='color: #ccc; margin: 0 10px; text-decoration: none;')
                        pin_link.string = 'Pinterest'
                        links_div.append(pin_link)
                        
                        # Save
                        with open(fp, 'w', encoding='utf-8') as f:
                            f.write(str(soup))
                        updated_count += 1
    except Exception as e:
        print(f"Error processing {os.path.basename(fp)}: {e}")

print(f"Successfully added Pinterest link to {updated_count} files.")
