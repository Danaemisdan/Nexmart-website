import glob
from bs4 import BeautifulSoup
import re
import json

html_files = glob.glob('*.html')
all_sections = {}

for file in html_files:
    if file == 'index_original.html':
        continue # Skip backup file to avoid duplicates

    with open(file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
    
    sections = []
    # Find all major semantic layout blocks
    for tag in soup.find_all(['section', 'header', 'nav', 'footer', 'main']):
        # If it's a 'main' tag, look at its immediate children instead
        if tag.name == 'main':
            for child in tag.find_all(['section', 'div'], recursive=False):
                classes = " ".join(child.get('class', []))
                # Only include divs that look like major sections
                if child.name == 'div' and 'section' not in classes.lower() and 'container' not in classes.lower():
                    continue
                h = child.find(['h1', 'h2', 'h3'])
                name = h.get_text(strip=True)[:50] if h else "No heading"
                
                features = []
                if child.find_all(class_=re.compile(r'grid|list', re.I)): features.append('Grid')
                if child.find_all(class_=re.compile(r'card', re.I)): features.append('Card')
                if child.find_all(class_=re.compile(r'cta|button-wrap', re.I)): features.append('CTA')
                if 'policy' in file.lower() or 'terms' in file.lower(): features.append('Legal Text Content')
                if child.find_all('img') and child.find_all('p'): features.append('Image+Text')
                
                sections.append({
                    'tag': child.name,
                    'classes': classes,
                    'heading': name,
                    'features': ", ".join(features) if features else "Standard Layout"
                })
        else:
            classes = " ".join(tag.get('class', []))
            h = tag.find(['h1', 'h2', 'h3'])
            name = h.get_text(strip=True)[:50] if h else "No heading"
            
            features = []
            if tag.find_all(class_=re.compile(r'grid|list', re.I)): features.append('Grid')
            if tag.find_all(class_=re.compile(r'card', re.I)): features.append('Card')
            if tag.find_all(class_=re.compile(r'cta|button-wrap', re.I)): features.append('CTA')
            if tag.find_all('img') and tag.find_all('p'): features.append('Image+Text')
            
            sections.append({
                'tag': tag.name,
                'classes': classes,
                'heading': name,
                'features': ", ".join(features) if features else "Standard Layout"
            })
            
    # Clean up redundant nested sections
    unique_classes = set()
    filtered_sections = []
    for s in sections:
        if s['classes'] and s['classes'] not in unique_classes:
            unique_classes.add(s['classes'])
            filtered_sections.append(s)
        elif not s['classes']:
            filtered_sections.append(s)
            
    all_sections[file] = filtered_sections

for file, sects in all_sections.items():
    print(f"\n================ {file} ================")
    for i, s in enumerate(sects):
        print(f"[{i+1}] <{s['tag']} class='{s['classes']}'>")
        print(f"    Heading: {s['heading']}")
        print(f"    Features: {s['features']}")
