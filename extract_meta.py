import os
import re
import json

def extract_neuro_meta():
    results = []
    for f in os.listdir('.'):
        if f.startswith('article') and f.endswith('.html'):
            try:
                with open(f, 'r', encoding='utf-8') as file:
                    content = file.read()
                    if 'Neuroscience' in content or 'Neuro-Science' in content:
                        title_match = re.search(r'<title>(.*?)</title>', content)
                        desc_match = re.search(r'<meta name="description" content="(.*?)">', content)
                        img_match = re.search(r'property="og:image" content="(.*?)"', content)
                        
                        title = title_match.group(1).replace(' | Mind & Balance', '').replace(' | Mind &amp; Balance', '') if title_match else f
                        desc = desc_match.group(1) if desc_match else ""
                        img = img_match.group(1) if img_match else ""
                        
                        results.append({
                            'file': f,
                            'title': title,
                            'desc': desc,
                            'img': img
                        })
            except Exception as e:
                print(f"Error reading {f}: {e}")
    
    with open('neuro_articles_meta.json', 'w', encoding='utf-8') as jf:
        json.dump(results, jf, indent=4)
    print(f"Extracted meta for {len(results)} articles.")

if __name__ == "__main__":
    extract_neuro_meta()
