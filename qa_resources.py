import bs4

files = ['blog.html', 'faqs.html', 'nexmart-university.html', 'about.html', 'contact.html', 'discord-community.html']

def check_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        soup = bs4.BeautifulSoup(f.read(), 'html.parser')
    
    issues = []
    
    # 1. Barba structure
    body = soup.find('body')
    if not body or body.get('data-barba') != 'wrapper':
        issues.append('Missing data-barba=wrapper on body')
        
    main = soup.find('main')
    if not main or main.get('data-barba') != 'container':
        issues.append('Missing data-barba=container on main')
        
    # 2. Global Nav & Footer
    if not soup.find('nav', class_='mega-nav'):
        issues.append('Missing global navigation')
    if not soup.find('footer', class_='footer_component'):
        issues.append('Missing global footer')
        
    # 3. Dropdowns
    nav = soup.find('nav', class_='mega-nav')
    if nav:
        tools = nav.find(lambda t: t.name == 'button' and t.get('data-dropdown-toggle') == 'products')
        if not tools: issues.append('Missing Tools dropdown toggle')
        resources = nav.find(lambda t: t.name == 'button' and t.get('data-dropdown-toggle') == 'resources')
        if not resources: issues.append('Missing Resources dropdown toggle')
        
    # 4. Shared CSS / JS
    scripts = soup.find_all('script')
    has_barba = any('barba' in str(s) for s in scripts)
    if not has_barba: issues.append('Missing Barba script')
    has_gsap = any('gsap' in str(s) for s in scripts)
    if not has_gsap: issues.append('Missing GSAP script')
    
    # 5. Duplicate IDs
    ids = []
    duplicates = []
    for tag in soup.find_all(id=True):
        if tag['id'] in ids:
            if tag['id'] not in duplicates:
                duplicates.append(tag['id'])
        else:
            ids.append(tag['id'])
    
    if duplicates:
        # Ignore webflow default duplicate IDs if they're standard across the site (like w-node)
        # but let's log them to be sure
        issues.append(f'Duplicate IDs found: {duplicates}')
        
    if not issues:
        print(f'{filename}: OK')
    else:
        print(f'{filename}: ERRORS -> {issues}')

for f in files:
    check_file(f)
