import bs4

with open('agentic-commerce.html', 'r', encoding='utf-8') as f:
    soup = bs4.BeautifulSoup(f, 'html.parser')
    
main = soup.find('main')
for idx, child in enumerate(main.find_all(recursive=False)):
    if not hasattr(child, 'get'): continue
    classes = child.get("class", [])
    text_preview = child.text[:200].replace('\n', ' ').strip()
    print(f"--- Section {idx} ({classes}) ---")
    print(f"Text Preview: {text_preview}")
    
    # Let's also print the immediate children of this section
    for child_idx, section_child in enumerate(child.find_all(recursive=False)):
        if hasattr(section_child, 'get'):
            print(f"  Child {child_idx}: {section_child.name} {section_child.get('class', [])}")
