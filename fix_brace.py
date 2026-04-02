filepath = r"c:\laragon\www\spaworld-me\assets\css\style02.css"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the missing brace before the editorial banners section
# The pattern is position: relative; followed by editorial banners comment
if 'position: relative;' in content and '/* --- EDITORIAL BANNERS (eb-*) --- */' in content:
    content = content.replace('position: relative;\n   /* --- EDITORIAL BANNERS (eb-*) --- */', 'position: relative;\n  }\n\n  /* --- EDITORIAL BANNERS (eb-*) --- */')
    content = content.replace('position: relative;\n  /* --- EDITORIAL BANNERS (eb-*) --- */', 'position: relative;\n  }\n\n  /* --- EDITORIAL BANNERS (eb-*) --- */')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("SUCCESS")
