import sys

def replace_eb_section(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    start_idx = -1
    for i, line in enumerate(lines):
        if '.eb-sec {' in line:
            start_idx = i
            break
    
    if start_idx == -1:
        print(f"FAILED: .eb-sec not found in {filepath}")
        return
    
    # New content with "Vibrant Wellness" attractive background colors and deeper gradients
    new_eb_css = """  .eb-sec {
    padding: 120px 0;
    background: #ffffff;
  }

  .eb-grid {
    display: grid;
    grid-template-columns: 1.2fr 0.8fr;
    grid-template-rows: repeat(2, 1fr);
    gap: 32px;
    max-width: 1400px;
    margin: 0 auto;
    padding: 0 40px;
  }

  .eb-banner {
    border-radius: 48px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: stretch;
    cursor: pointer;
    transition: all .8s cubic-bezier(0.19, 1, 0.22, 1);
    border: 1px solid rgba(0, 0, 0, 0.04);
    box-shadow: 0 15px 45px rgba(0, 0, 0, 0.05);
  }

  /* Item 1 Vertical Layout */
  .eb-item-1 {
    flex-direction: column;
  }

  .eb-banner:hover {
    transform: translateY(-12px) scale(1.005);
    box-shadow: 0 60px 120px rgba(0, 0, 0, 0.1);
  }

  .eb-tall {
    grid-row: span 2;
  }

  .eb-banner-bg, .eb-banner-overlay {
    display: none;
  }

  /* Attractive "Vibrant Wellness" Image Backgrounds */
  .eb-banner-icon {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    overflow: hidden;
    z-index: 5;
    padding: 40px;
    transition: all 0.6s var(--ease);
  }

  /* Colorful and "Attractive" Studio Spotlights */
  .eb-item-1 .eb-banner-icon {
    background: radial-gradient(circle at center, #ffffff 0%, #e0f2f7 50%, #c5e6f0 100%);
    flex: 1.2;
  }
  
  .eb-item-2 .eb-banner-icon { 
    background: radial-gradient(circle at center, #ffffff 0%, #f4f8e6 50%, #e8efcf 100%);
  }
  
  .eb-item-3 .eb-banner-icon { 
    background: radial-gradient(circle at center, #ffffff 0%, #f9f4ec 50%, #f0e6d6 100%);
  }
  
  /* Accent light highlight on hover */
  .eb-banner-icon::before {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, rgba(255,255,255,0.6) 0%, transparent 40%);
    opacity: 0;
    transition: opacity 0.5s var(--ease);
    z-index: 2;
  }

  .eb-banner:hover .eb-banner-icon::before {
    opacity: 1;
  }

  .eb-banner-icon img {
    max-width: 85%;
    max-height: 80%;
    object-fit: contain;
    position: relative;
    z-index: 10;
    transition: transform 1s cubic-bezier(0.19, 1, 0.22, 1);
    filter: drop-shadow(0 24px 48px rgba(0, 0, 0, 0.12));
  }

  .eb-banner:hover .eb-banner-icon img {
    transform: scale(1.18) rotate(3deg) translateY(-12px);
    filter: drop-shadow(0 50px 80px rgba(0, 0, 0, 0.18));
  }

  .eb-banner-content {
    flex: 1.1;
    padding: 60px 52px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    z-index: 10;
    transition: all 0.4s var(--ease);
    border-top: 1px solid rgba(255, 255, 255, 0.05); /* Soft split line */
  }

  .eb-tall .eb-banner-content {
    padding: 80px 60px;
    text-align: center;
    align-items: center;
  }

  /* Vibrant Attractive Content Gradients */
  .eb-item-1 .eb-banner-content { background: linear-gradient(145deg, #00445a 0%, #004f69 50%, #006380 100%); }
  .eb-item-2 .eb-banner-content { background: linear-gradient(145deg, #3f4f1e 0%, #4a5d23 50%, #60792d 100%); }
  .eb-item-3 .eb-banner-content { background: linear-gradient(145deg, #8b6e5b 0%, #a0816c 50%, #ba9b85 100%); }

  .eb-banner-tag {
    font-size: 11px;
    font-weight: 800;
    letter-spacing: .4em;
    text-transform: uppercase;
    color: rgba(255, 255, 255, 0.6);
    margin-bottom: 28px;
    display: block;
  }

  .eb-banner-title {
    font-family: var(--serif);
    font-size: clamp(28px, 3.2vw, 48px);
    font-weight: 700;
    color: #ffffff;
    line-height: 1.1;
    margin-bottom: 40px;
    letter-spacing: -0.02em;
    text-shadow: 0 4px 12px rgba(0,0,0,0.1); /* Extra contrast */
  }

  .eb-item-2 .eb-banner-title,
  .eb-item-3 .eb-banner-title {
    font-size: clamp(22px, 2.5vw, 36px);
  }

  .eb-banner-link {
    display: inline-flex;
    align-items: center;
    gap: 12px;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: .25em;
    text-transform: uppercase;
    color: var(--gold);
    transition: all .4s var(--ease);
    position: relative;
    padding-bottom: 10px;
    text-decoration: none;
  }

  .eb-banner-link::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    width: 60px;
    height: 2.5px;
    background: currentColor;
    transition: width 0.4s var(--ease);
    opacity: 0.7;
  }

  .eb-banner:hover .eb-banner-link {
    color: #ffffff;
    gap: 24px;
    letter-spacing: .3em;
  }

  .eb-banner:hover .eb-banner-link::after {
    width: 100%;
    opacity: 1;
  }

  @media (max-width: 1100px) {
    .eb-grid {
      grid-template-columns: 1fr;
      padding: 0 24px;
    }
    .eb-tall {
      grid-row: span 1;
    }
    .eb-banner {
      min-height: 480px;
    }
  }

  @media (max-width: 600px) {
    .eb-banner {
      flex-direction: column;
    }
    .eb-banner-icon {
      height: 350px;
      flex: none;
    }
    .eb-banner-content {
      padding: 60px 40px;
      flex: none;
      text-align: center;
      align-items: center;
    }
  }
"""
    
    result_lines = lines[:start_idx] + [new_eb_css + "\n"]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(result_lines)
    print(f"SUCCESS: Updated {filepath}")

# Process all files
files = [
    r"c:\laragon\www\spaworld-me\assets\css\style02.css",
    r"c:\laragon\www\spaworld-me\spastore-v5\assets\css\style02.css",
    r"c:\laragon\www\spaworld-me\spastore-v6\assets\css\style02.css",
    r"c:\laragon\www\spaworld-me\spastore-v7\assets\css\style02.css"
]

for f in files:
    replace_eb_section(f)
