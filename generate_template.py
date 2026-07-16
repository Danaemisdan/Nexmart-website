from bs4 import BeautifulSoup

def replace_text(element, new_text):
    if element:
        # Clear existing content and set new text
        element.string = new_text

def build_template():
    with open('index.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
    
    # 1. Base Structure (copy head, scripts, body wrapper)
    template_soup = BeautifulSoup('<!DOCTYPE html><html data-wf-page="69c4a4d640fdca68c1cc9689" data-wf-site="69c4a4d640fdca68c1cc9685" lang="en"><head></head><body class="body"></body></html>', 'html.parser')
    
    # Copy <head> contents
    head = soup.find('head')
    if head:
        template_soup.head.append(BeautifulSoup(str(head.encode_contents().decode('utf-8')), 'html.parser'))
        # Update title
        title = template_soup.head.find('title')
        if title: title.string = "[Product Name] - Nexmart"
        # Update meta description
        meta_desc = template_soup.head.find('meta', attrs={'name': 'description'})
        if meta_desc: meta_desc['content'] = "[Product Meta Description]"

    body = template_soup.body

    # Extract required sections from index.html
    nav = soup.find('nav', class_='mega-nav')
    hero = soup.find('section', class_='is-hero')
    two_column = soup.find('section', class_='is-ai')
    
    # The grid and process sections share the generic 'section' class. We find them by heading text.
    grid_section = None
    process_section = None
    for s in soup.find_all('section', class_='section'):
        classes = s.get('class', [])
        if len(classes) == 1 and classes[0] == 'section':
            h2 = s.find('h2')
            if h2:
                if 'Why Nexmart?' in h2.get_text():
                    grid_section = s
                elif 'How Agentic Commerce Works' in h2.get_text():
                    process_section = s

    tabs_section = soup.find('section', class_='is-tabs')
    cta_banner = soup.find('section', class_='no-padding-bottom')
    footer = soup.find('footer', class_='footer_component')
    
    # Add hidden scripts / div at the beginning of body if present in index
    body_div = soup.body.find('div', class_='page-wrapper')
    if not body_div:
        body_div = template_soup.new_tag('div', attrs={'class': 'page-wrapper'})
        body.append(body_div)
    else:
        # Create a fresh page-wrapper
        body_div = template_soup.new_tag('div', attrs={'class': 'page-wrapper'})
        body.append(body_div)
        
    # Assemble
    if nav: body_div.append(BeautifulSoup(str(nav), 'html.parser'))
    
    # Hero
    if hero:
        hero_clone = BeautifulSoup(str(hero), 'html.parser')
        replace_text(hero_clone.find('h1'), "[Product Name]")
        replace_text(hero_clone.find('div', class_='margin-bottom-32'), "[Hero Description / Tagline]")
        cta_btn = hero_clone.find('a', class_='button is-primary w-button')
        if cta_btn: replace_text(cta_btn, "[Primary CTA]")
        body_div.append(hero_clone)
        
    # Two-Column
    if two_column:
        two_col_clone = BeautifulSoup(str(two_column), 'html.parser')
        replace_text(two_col_clone.find('h2'), "[Product Overview Heading]")
        replace_text(two_col_clone.find('p'), "[Detailed Product Overview Description explaining the core value proposition.]")
        # Just update the first button
        btn = two_col_clone.find('a', class_='button is-secondary w-button')
        if btn: replace_text(btn, "[Learn More CTA]")
        body_div.append(two_col_clone)
        
    # Grid
    if grid_section:
        grid_clone = BeautifulSoup(str(grid_section), 'html.parser')
        replace_text(grid_clone.find('h2'), "[Key Features]")
        replace_text(grid_clone.find('p', class_='text-size-large'), "[Subtitle explaining why these features matter]")
        cards = grid_clone.find_all('div', class_='why-card')
        for i, card in enumerate(cards):
            replace_text(card.find('h3'), f"[Feature {i+1} Title]")
            replace_text(card.find('p'), f"[Feature {i+1} detailed description emphasizing value.]")
        body_div.append(grid_clone)
        
    # Process
    if process_section:
        process_clone = BeautifulSoup(str(process_section), 'html.parser')
        replace_text(process_clone.find('h2'), "[How It Works]")
        replace_text(process_clone.find('p', class_='text-size-large'), "[Step-by-step product workflow explanation]")
        steps = process_clone.find_all('div', class_='how_it_works-item')
        for i, step in enumerate(steps):
            replace_text(step.find('h3'), f"[Step {i+1} Name]")
            replace_text(step.find('p'), f"[Step {i+1} explanation]")
        body_div.append(process_clone)
        
    # Tabs
    if tabs_section:
        tabs_clone = BeautifulSoup(str(tabs_section), 'html.parser')
        replace_text(tabs_clone.find('h2'), "[Use Cases / Industries]")
        replace_text(tabs_clone.find('p', class_='text-size-large'), "[Explore how different teams use this product]")
        
        tab_links = tabs_clone.find_all('a', class_='tab-link')
        for i, link in enumerate(tab_links):
            # Try to find the inner text div
            txt_div = link.find('div', class_='text-size-large text-weight-semibold')
            if txt_div: replace_text(txt_div, f"[Use Case {i+1}]")
            
        tab_panes = tabs_clone.find_all('div', class_='w-tab-pane')
        for i, pane in enumerate(tab_panes):
            replace_text(pane.find('h3'), f"[Use Case {i+1} Benefit]")
            replace_text(pane.find('p'), f"[Explanation of how the product solves problems for Use Case {i+1}]")
            btn = pane.find('a', class_='button')
            if btn: replace_text(btn, "[View Use Case CTA]")
            
        body_div.append(tabs_clone)
        
    # CTA Banner
    if cta_banner:
        cta_clone = BeautifulSoup(str(cta_banner), 'html.parser')
        replace_text(cta_clone.find('h2'), "[Ready to get started?]")
        replace_text(cta_clone.find('p'), "[Final compelling reason to sign up right now]")
        btn = cta_clone.find('a', class_='button')
        if btn: replace_text(btn, "[Final CTA Button]")
        body_div.append(cta_clone)
        
    # Footer
    if footer:
        body_div.append(BeautifulSoup(str(footer), 'html.parser'))
        
    # Append trailing scripts from body
    for script in soup.body.find_all('script', recursive=False):
        body.append(BeautifulSoup(str(script), 'html.parser'))

    with open('product-template.html', 'w', encoding='utf-8') as out:
        out.write(str(template_soup))

build_template()
