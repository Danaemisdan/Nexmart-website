from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

sections = soup.find_all(lambda tag: tag.name == 'section' or (tag.name == 'div' and any('section' in c for c in tag.get('class', []))))

print(f"Found {len(sections)} sections")

for i, s in enumerate(sections):
    classes = " ".join(s.get('class', []))
    if 'mega-nav' in classes or 'footer' in classes: continue
    
    # Try to find a heading
    h = s.find(['h1', 'h2', 'h3'])
    name = h.get_text(strip=True) if h else "No heading"
    
    print(f"\n--- Section {i+1} ---")
    print(f"Classes: {classes}")
    print(f"Heading: {name}")
    
    # check for certain structures
    if s.find_all(class_=lambda x: x and 'grid' in x): print("- Contains Grid")
    if s.find_all(class_=lambda x: x and 'card' in x): print("- Contains Cards")
    if s.find_all(class_=lambda x: x and 'faq' in x or x and 'accordion' in x): print("- Contains FAQ/Accordion")
    if s.find_all(class_=lambda x: x and 'testimonial' in x): print("- Contains Testimonials")
