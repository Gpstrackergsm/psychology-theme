import os

BASE_DIR = "/Users/khalidaitelmaati/Desktop/scrapy-master/psychology-theme-main"
PINTEREST_META_TAG = '<meta name="p:domain_verify" content="ee9e9d21f7483e60e6c3ea9e20578269"/>'

def inject_pinterest_meta():
    files = [f for f in os.listdir(BASE_DIR) if f.endswith(".html")]
    print(f"Found {len(files)} HTML files to update.")
    
    updated_count = 0
    for file_name in files:
        file_path = os.path.join(BASE_DIR, file_name)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Avoid double injection
            if PINTEREST_META_TAG in content:
                continue
                
            # Target the bottom of the head section just before </head>
            if "</head>" in content:
                updated_content = content.replace("</head>", f"    {PINTEREST_META_TAG}\n</head>")
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                updated_count += 1
        except Exception as e:
            print(f"Error processing {file_name}: {e}")
            
    print(f"Successfully updated {updated_count} files.")

if __name__ == "__main__":
    inject_pinterest_meta()
