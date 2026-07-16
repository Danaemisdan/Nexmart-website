import os
from bs4 import BeautifulSoup
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
    if not os.path.exists(filename):
        report.append(f"**Status**: ERROR - File not found.\n")
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    
    issues = []
    
    # 1. Broken HTML/Nesting
    if not soup.find('title'):
        issues.append("Missing <title> tag (Invalid HTML structure).")
        
    # 2. Images & Alt text
    images = soup.find_all('img')
    missing_alts = 0
    empty_srcs = 0
    for img in images:
        # Check if attribute literally doesn't exist
        if not img.has_attr('alt'):
            missing_alts += 1
        if not img.get('src') or img.get('src') == "":
            empty_srcs += 1
    if missing_alts > 0: issues.append(f"{missing_alts} images missing 'alt' attributes entirely.")
    if empty_srcs > 0: issues.append(f"{empty_srcs} images missing 'src' attributes.")
    
    # 3. Placeholders remaining (brackets)
    placeholders = re.findall(r'\[.*?\]', html)
    if placeholders:
        text_placeholders = [p for p in placeholders if "Product Name" in p or "Feature" in p or "Step" in p or "Use Case" in p]
        if text_placeholders:
            issues.append(f"Found unresolved template placeholders: {set(text_placeholders)}")
            
    # 4. Empty or '#' links
    links = soup.find_all('a')
    empty_links = 0
    hash_links = 0
    todo_links = 0
    for link in links:
        href = link.get('href', '')
        if href == "": empty_links += 1
        if href == "#": hash_links += 1
        if "#TODO" in href: todo_links += 1
        
    if empty_links > 0: issues.append(f"{empty_links} links with empty href.")
    if hash_links > 0: issues.append(f"{hash_links} links pointing to '#'.")
    if todo_links > 0: issues.append(f"{todo_links} #TODO links found.")
    
    # 5. Heading Hierarchy
    h1s = soup.find_all('h1')
    if len(h1s) != 1:
        issues.append(f"Incorrect H1 count: Found {len(h1s)} H1 tags (should be exactly 1).")
        
    # 6. Duplicate IDs
    all_tags_with_id = soup.find_all(id=True)
    ids = [tag['id'] for tag in all_tags_with_id]
    duplicate_ids = set([x for x in ids if ids.count(x) > 1])
    if duplicate_ids:
        issues.append(f"Duplicate IDs found: {duplicate_ids}")
        
    # 7. SEO
    meta_desc = soup.find('meta', attrs={'name': 'description'})
    if not meta_desc or not meta_desc.get('content'):
        issues.append("Missing or empty meta description.")
        
    # 8. Unchanged Images (Placeholder graphics)
    hero = soup.find('section', class_='is-hero')
    if hero:
        hero_img = hero.find('img')
        if hero_img and "ChatGPT Image" in hero_img.get('src', ''):
            issues.append("Hero image is still using the default placeholder graphic from the homepage.")
            
    if not issues:
        report.append("**Status**: PASS - No critical structural issues detected.\n")
    else:
        report.append("**Status**: ISSUES DETECTED")
        for i in issues:
            report.append(f"- {i}")
        report.append("\n")

with open('qa_report.md', 'w', encoding='utf-8') as f:
    f.write("# Page-by-Page QA Report\n\n" + '\n'.join(report))
