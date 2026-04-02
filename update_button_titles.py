import re
import os

html_files = [
    r"c:\laragon\www\spaworld-me\index.html",
    r"c:\laragon\www\spaworld-me\spastore-v5\index.html",
    r"c:\laragon\www\spaworld-me\spastore-v6\index.html",
    r"c:\laragon\www\spaworld-me\spastore-v7\index.html"
]

def update_titles(filepath):
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return
        
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # 1. Specifically add title to bss-card-list if missing
    # <button class="bss-card-list">📋</button>
    content = re.sub(r'(<button class="bss-card-list")([^>]*)>(📋</button>)', 
                     r'\1\2 title="Add to Quick List">\3', content)
    
    # 2. Update any title="Add to List" to title="Add to Quick List"
    content = content.replace('title="Add to List"', 'title="Add to Quick List"')
    
    # 3. Handle cases where bss-card-list already has a title but it's "Add to List"
    # (Regex 2 already handles this if it's identical, but let's be safe)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"SUCCESS: Updated titles in {filepath}")

for f in html_files:
    update_titles(f)
