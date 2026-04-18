import os
import glob
import time
from bs4 import BeautifulSoup

import openai
from openai import OpenAI
# ==========================================
# CONFIGURATION
# ==========================================
# IMPORTANT: Put your OpenAI API key here, or set it in your environment
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")

client = OpenAI(api_key=OPENAI_API_KEY)
BASE_DIR = "/Users/khalidaitelmaati/Desktop/scrapy-master/psychology-theme-main"

def generate_article(title):
    """
    Calls the OpenAI API to generate a massive, 4,000+ word article.
    """
    system_prompt = (
        "You are Dr. Aris, a renowned clinical neuro-psychologist and expert copywriter. "
        "Your task is to write an extremely comprehensive, definitive, 4,000-word article on the requested topic. "
        "The content MUST meet Google AdSense standards for E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness). "
        "Format the entire output as clean HTML (without ```html wrappers or body/head tags), using semantic tags like <h2>, <h3>, <ul>, <p>, <blockquote>, and <section>. "
        "DO NOT use <h1> as the page already has one. "
        "Include deep neuro-clinical context, experimental evidence, case studies (hypothetical), and professional action guides. "
        "Make it exceptionally long, incredibly detailed, and highly engaging."
    )
    
    user_prompt = f"Write a definitive, 4,000-word SEO-optimized HTML article on the topic: '{title}'. Remember, DO NOT include <html>, <head>, or <body> tags. Just the raw HTML content to go inside a <main> tag."

    try:
        response = client.chat.completions.create(
            model="gpt-4o",  # gpt-4o is excellent for long-form content
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7,
            max_tokens=4000  # Allows for very long output
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error generating content for {title}: {e}")
        return None

def rewrite_all():
    files = glob.glob(os.path.join(BASE_DIR, "article*.html"))
    
    # We will process one by one
    for file_path in files:
        filename = os.path.basename(file_path)
        
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        soup = BeautifulSoup(content, "html.parser")
        
        # Get the title to give the AI context
        title_tag = soup.find('title')
        h1_tag = soup.find('h1')
        
        topic = None
        if h1_tag and h1_tag.text:
            topic = h1_tag.text.strip()
        elif title_tag and title_tag.text:
            topic = title_tag.text.strip()
            
        if not topic:
            print(f"Skipping {filename}: Could not determine topic.")
            continue
            
        main_tag = soup.find('main', class_="article-body") or soup.find('main')
        if not main_tag:
            print(f"Skipping {filename}: Could not find <main> tag.")
            continue
            
        # Check if we've already rewritten it (to avoid re-running over hours if script crashes)
        # We can check word count of main tag
        if len(main_tag.get_text().split()) > 2500:
            print(f"Skipping {filename}: Already seems to be long-form ({len(main_tag.get_text().split())} words).")
            continue
            
        print(f"Generating 4,000 word article for: {topic} ({filename})...")
        new_html_content = generate_article(topic)
        
        if new_html_content:
            # Clear existing content inside main and replace with new
            main_tag.clear()
            
            # Since new_html_content is string, we parse it and append
            new_soup = BeautifulSoup(new_html_content, "html.parser")
            main_tag.append(new_soup)
            
            # Save back
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(str(soup))
                
            print(f"✅ Successfully updated {filename}.")
            
            # Sleep to respect API rate limits
            time.sleep(10)

if __name__ == "__main__":
    if OPENAI_API_KEY == "your-openai-api-key-here":
        print("🚨 Please edit this script and add your actual OPENAI_API_KEY!")
    else:
        rewrite_all()
