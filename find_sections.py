from bs4 import BeautifulSoup
import re
import json

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

sections = []

# Find common structural elements in webflow
for tag in soup.find_all(['section', 'header', 'div']):
    classes = tag.get('class', [])
    class_str = ' '.join(classes)
    
    # Heuristics for a "Section"
    is_section = False
    if tag.name == 'section' or tag.name == 'header':
        is_section = True
    elif any('section' in c.lower() for c in classes):
        is_section = True
        
    if is_section:
        # Ignore mega-nav and footer as they are global
        if 'mega-nav' in class_str or 'footer' in class_str:
            continue
            
        # Try to find a heading to name the section
        heading = tag.find(['h1', 'h2', 'h3'])
        name = heading.get_text(strip=True) if heading else "Unnamed Section"
        if len(name) > 40: name = name[:37] + "..."
        
        # Determine purpose based on classes or content
        purpose = []
        if 'hero' in class_str.lower(): purpose.append('Hero')
        if tag.find_all(class_=re.compile(r'grid|list', re.I)): purpose.append('Grid/List Layout')
        if tag.find_all(class_=re.compile(r'card', re.I)): purpose.append('Cards')
        if 'cta' in class_str.lower() or tag.find_all(string=re.compile(r'start|download', re.I)): purpose.append('CTA')
        if 'faq' in class_str.lower() or tag.find_all(class_=re.compile(r'accordion|faq', re.I)): purpose.append('FAQ')
        if 'testimonial' in class_str.lower() or 'review' in class_str.lower(): purpose.append('Testimonial')
        if 'pricing' in class_str.lower(): purpose.append('Pricing')
        if 'slider' in class_str.lower() or 'swiper' in class_str.lower(): purpose.append('Slider/Carousel')
        if tag.find('form'): purpose.append('Form')
        if tag.find_all('img') and len(tag.find_all('p')) > 0: purpose.append('Image + Text')
        
        sections.append({
            'name': name,
            'classes': class_str,
            'purpose': ", ".join(purpose) if purpose else "General Content",
            'tag': tag.name
        })

# Output unique sections based on classes to avoid duplicates (like inner sections)
unique_sections = {}
for s in sections:
    # Use the primary section class as key if it exists
    key = s['classes'].split()[0] if s['classes'] else s['name']
    if key not in unique_sections:
        unique_sections[key] = s

print("--- Identified Sections ---")
for k, v in unique_sections.items():
    print(f"Name: {v['name']}\nClasses: {v['classes']}\nPurpose: {v['purpose']}\n")
