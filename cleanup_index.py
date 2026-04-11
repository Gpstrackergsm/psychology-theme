import sys

INDEX_PATH = 'index.html'

def cleanup_index():
    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # We want to remove the sections from approximately line 158 to 268
    # But specifically targeting the load-more blocks.
    
    new_lines = []
    skip = False
    
    for i, line in enumerate(lines):
        # Target the top load-more blocks which are misplaced
        if i+1 >= 158 and i+1 <= 201:
            continue
        if i+1 >= 219 and i+1 <= 264: # Range for second block
            continue
        new_lines.append(line)
        
    with open(INDEX_PATH, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print("Cleaned up redundant index.html blocks.")

if __name__ == "__main__":
    cleanup_index()
