import re

html_files = [
    r"c:\laragon\www\spaworld-me\index.html",
    r"c:\laragon\www\spaworld-me\spastore-v5\index.html",
    r"c:\laragon\www\spaworld-me\spastore-v6\index.html",
    r"c:\laragon\www\spaworld-me\spastore-v7\index.html"
]

new_html_content = """    <!-- EDITORIAL BANNERS -->
    <section class="eb-sec eb-sec-white" style="padding-top:0;">
      <div class="w">
        <div class="eb-grid">
          <!-- Banner 1: Primary -->
          <div class="eb-banner eb-tall eb-item-1 reveal">
            <div class="eb-banner-icon">
              <img src="assets/img/png/professiona-massage.png" alt="Professional Massage Beds">
            </div>
            <div class="eb-banner-content">
              <span class="eb-banner-tag">NEW COLLECTION 2025</span>
              <h3 class="eb-banner-title">Professional<br>Massage Beds<br>& Spa Tables</h3>
              <a href="#" class="eb-banner-link">Shop the Range</a>
            </div>
          </div>

          <!-- Banner 2: Secondary 1 -->
          <div class="eb-banner eb-item-2 reveal d1">
            <div class="eb-banner-icon">
              <img src="assets/img/png/Finnish-Grade.png" alt="Sauna Kits">
            </div>
            <div class="eb-banner-content">
              <span class="eb-banner-tag">SAUNA SEASON</span>
              <h3 class="eb-banner-title">Finnish-Grade<br>Sauna Kits</h3>
              <a href="#" class="eb-banner-link">Explore</a>
            </div>
          </div>

          <!-- Banner 3: Secondary 2 -->
          <div class="eb-banner eb-item-3 reveal d2">
            <div class="eb-banner-icon">
              <img src="assets/img/png/Bathrobes, Towels.png" alt="Hotel Essentials">
            </div>
            <div class="eb-banner-content">
              <span class="eb-banner-tag">HOTEL ESSENTIALS</span>
              <h3 class="eb-banner-title">Bathrobes, Towels<br>& Linen Packs</h3>
              <a href="#" class="eb-banner-link">View Collection</a>
            </div>
          </div>
        </div>
      </div>
    </section>"""

def fix_html_section(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Simple replacement from comment to closing tag
    pattern = re.compile(r'<!-- EDITORIAL BANNERS -->.*?<section class="eb-sec.*?</section>', re.DOTALL)
    
    if pattern.search(content):
        new_content = pattern.sub(new_html_content, content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"SUCCESS: Updated {filepath}")
    else:
        print(f"FAILED: Pattern not found in {filepath}")

for f in html_files:
    fix_html_section(f)
