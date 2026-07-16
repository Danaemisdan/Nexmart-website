import os
from bs4 import BeautifulSoup, Comment
import re

files_to_check = [
    "agentic-commerce.html",
    "magic-ai-search.html",
    "advertiser-tracker.html",
    "advertiser-library.html",
    "portfolio.html",
    "creator-library.html",
    "financial-inclusion.html",
    "competitor-research.html",
    "chrome-extension.html",
    "pre-built-stores.html",
    "theme-detector.html"
]

report = []

for filename in files_to_check:
    report.append(f"## {filename}")
    
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    
    # 1. Duplicate IDs
    all_tags_with_id = soup.find_all(id=True)
    seen_ids = {}
    for tag in all_tags_with_id:
        id_val = tag['id']
        if id_val in seen_ids:
            seen_ids[id_val] += 1
            new_id = f"{id_val}_{seen_ids[id_val]}"
            tag['id'] = new_id
            report.append(f"- Replaced duplicate ID '{id_val}' with '{new_id}'")
        else:
            seen_ids[id_val] = 0
            
    # 2. Image Accessibility & 3. Hero Images
    product_name = soup.title.string.split('-')[0].strip() if soup.title else "Product"
    
    images = soup.find_all('img')
    for img in images:
        if not img.get('alt'):
            src = img.get('src', '').lower()
            
            # Check if it's the hero image
            in_hero = img.find_parent('section', class_='is-hero')
            in_overview = img.find_parent('section', class_='is-ai')
            
            if in_hero:
                img['alt'] = f"{product_name} Hero Display"
                report.append(f"- Added descriptive alt '{img['alt']}' to hero image.")
                
                # Check if it's a placeholder hero image
                if "chatgpt image" in src:
                    comment = Comment(" TODO: Replace with product-specific hero image ")
                    img.insert_before(comment)
                    report.append(f"- Inserted TODO comment for placeholder hero image.")
                    
            elif in_overview:
                img['alt'] = f"{product_name} Interface Overview"
                report.append(f"- Added descriptive alt '{img['alt']}' to overview image.")
                
            elif 'logo' in src or 'pm.png' in src or 'am.png' in src: # Known logo files
                img['alt'] = "Nexmart Company Logo"
                report.append(f"- Added descriptive alt 'Nexmart Company Logo' to {img.get('src')}")
                
            else:
                img['alt'] = ""
                report.append(f"- Added alt='' (decorative) to {img.get('src')}")
                
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
with open('cleanup_report.md', 'w', encoding='utf-8') as f:
    f.write("# Production Cleanup Report\n\n" + '\n'.join(report))
