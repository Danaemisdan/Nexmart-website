import os
import bs4
import glob

html_files = glob.glob('*.html')

# 1. First, create a blank placeholder template
with open('index.html', 'r', encoding='utf-8') as f:
    template_soup = bs4.BeautifulSoup(f.read(), 'html.parser')

main = template_soup.find('main')
if main:
    main.clear()
    
# We want to keep the footer, so let's put the footer back if it was cleared
footer = template_soup.find('footer', class_='footer_component')
if not footer and main:
    # Maybe it was inside main?
    pass

# Re-read to rebuild properly
with open('index.html', 'r', encoding='utf-8') as f:
    template_soup = bs4.BeautifulSoup(f.read(), 'html.parser')

# Find main and empty it, but keep the footer if it's inside main
main_element = template_soup.find('main')
if main_element:
    footer_element = main_element.find('footer', class_='footer_component')
    main_element.clear()
    if footer_element:
         main_element.append(footer_element)

placeholder_html = str(template_soup)

pages_to_create = [
    'blog.html',
    'faqs.html',
    'nexmart-university.html',
    'about.html',
    'contact.html',
    'discord-community.html'
]

for page in pages_to_create:
    with open(page, 'w', encoding='utf-8') as f:
        f.write(placeholder_html)
        
html_files.extend(pages_to_create)
html_files = list(set(html_files)) # deduplicate

# Link mapping
resource_links = {
    'Blog': 'blog.html',
    'Nexmart University': 'nexmart-university.html',
    'FAQs': 'faqs.html',
    'About Us': 'about.html',
    'Discord Community': 'discord-community.html',
    'Contact': 'contact.html'
}

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = bs4.BeautifulSoup(html, 'html.parser')
    
    # Remove Pricing from global nav
    nav = soup.find('nav', class_='mega-nav')
    if nav:
        pricing_labels = nav.find_all(string=lambda t: t and 'Pricing' in t)
        for label in pricing_labels:
            if 'Pricing' == label.strip():
                # Find the parent li
                li = label.find_parent('li', class_='mega-nav__bar-list-item')
                if li:
                    li.decompose()
                    
    # Download App -> Coming Soon
    download_texts = soup.find_all(string=lambda t: t and 'Download App' in t)
    for t in download_texts:
        if 'Download App' == t.strip():
            t.replace_with(t.replace('Download App', 'Coming Soon'))
            # Find closest a tag and disable it
            a_tag = t.find_parent('a')
            if a_tag:
                a_tag['href'] = '#'
                # Add pointer-events none to make it completely non-functional if you want, but href="#" is standard.
                a_tag['onclick'] = 'return false;'

    # Update Resources Dropdown
    res_panel = soup.find(lambda tag: tag.name == 'div' and tag.get('data-nav-content') == 'resources')
    if res_panel:
        for a in res_panel.find_all('a'):
            text_span = a.find('span', class_='mega-nav__panel-link-text')
            if text_span:
                text = text_span.text.strip()
                if text in resource_links:
                    a['href'] = resource_links[text]
                    
    # Update Footer Resources too, just in case
    footer_links = soup.find_all('div', class_='footer_link_text')
    for f_link in footer_links:
        text = f_link.text.strip()
        if text in resource_links:
            a_tag = f_link.find_parent('a')
            if a_tag:
                a_tag['href'] = resource_links[text]
                
    # Update Footer Company links (About, Contact, Pricing)
    # The user asked to remove pricing from global nav. I will also point About/Contact to the new pages
    for f_link in footer_links:
        text = f_link.text.strip()
        if text == 'About':
            a_tag = f_link.find_parent('a')
            if a_tag: a_tag['href'] = 'about.html'
        elif text == 'Contact':
            a_tag = f_link.find_parent('a')
            if a_tag: a_tag['href'] = 'contact.html'

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
print('Done processing all files.')
