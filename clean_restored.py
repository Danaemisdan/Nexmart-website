import re

files = ['agentic-commerce.html', 'advertiser-tracker.html']

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Clean the 3 tools menu items: Extension, Stores, Theme
    patterns_to_remove = [
        r'<li class="mega-nav__panel-item"[^>]*>\s*<a class="mega-nav__panel-link w-inline-block"[^>]*href="extension\.html"[^>]*>.*?</a>\s*</li>',
        r'<li class="mega-nav__panel-item"[^>]*>\s*<a class="mega-nav__panel-link w-inline-block"[^>]*href="stores\.html"[^>]*>.*?</a>\s*</li>',
        r'<li class="mega-nav__panel-item"[^>]*>\s*<a class="mega-nav__panel-link w-inline-block"[^>]*href="theme\.html"[^>]*>.*?</a>\s*</li>'
    ]
    for p in patterns_to_remove:
        html = re.sub(p, '', html, flags=re.DOTALL)
        
    # 2. Remove the nav video thumbnail (the img in the 'How it works' mega-nav section)
    html = re.sub(r'<img[^>]*class="wscp-img"[^>]*>', '', html, flags=re.DOTALL)
    
    # 3. Remove the footer graphic
    html = re.sub(r'<div class="footer_graphic-wrap">.*?</div>\s*<div class="container-large">', '<div class="container-large">', html, flags=re.DOTALL)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
        
print('Restored and cleaned safely with regex.')
