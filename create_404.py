import copy
from bs4 import BeautifulSoup
from datetime import datetime

with open('product-template.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

body = soup.find('body')

# Find navigation - check for known Webflow nav structures
nav = None
for div in body.find_all('div', recursive=False):
    c = div.get('class', [])
    if any('nav' in cls.lower() for cls in c):
        nav = div
        break
if not nav:
    nav = body.find('div', class_='navbar-component') or body.find('div', class_='nav-container')

hero = soup.find('section', class_='is-hero')
cta = soup.find('section', class_='no-padding-bottom')
footer = soup.find('section', class_='is-footer')

# Rebuild body strictly with these 4 sections
if body:
    body.clear()
    if nav: body.append(nav)
    if hero: body.append(hero)
    if cta: body.append(cta)
    if footer: body.append(footer)

# Update Hero content
if hero:
    h1 = hero.find('h1')
    if h1: h1.string = "404 – Page Not Found"

    p = hero.find('p')
    if p: p.string = "We couldn't find the page you were looking for. It may have been moved or deleted."

    buttons = hero.find_all('a', class_='button-wrap')
    if len(buttons) >= 2:
        btn1 = buttons[0]
        btn2 = buttons[1]
        
        # Helper to update button text safely in Webflow structures
        def update_btn(btn, new_text, href):
            text_div = btn.find('div', class_='text-size-small') or btn.find('div')
            if text_div:
                text_div.string = new_text
            else:
                btn.string = new_text
            btn['href'] = href
            
        update_btn(btn1, "Return Home", "index.html")
        update_btn(btn2, "Explore Tools", "agentic-commerce.html")
        
        # Add third CTA
        btn3 = copy.copy(btn2)
        update_btn(btn3, "Open Nexmart App", "https://app.nexmartshop.ai/")
        
        # Insert btn3 right after btn2
        btn2.insert_after(btn3)
        
        # In Webflow, button wraps might be inside a layout div. If they are block level, we might need a wrapper. 
        # But copy.copy(btn2) and insert_after should put it right beside btn2 in the DOM.
        
# Update Metadata
head = soup.find('head')
if head:
    # Title
    title = head.find('title')
    title_text = "404 - Page Not Found | Nexmart"
    if title: title.string = title_text
    else:
        t = soup.new_tag('title')
        t.string = title_text
        head.append(t)

    # Desc
    desc = head.find('meta', attrs={'name': 'description'})
    desc_text = "The requested page could not be found on the Nexmart platform."
    if desc: desc['content'] = desc_text
    else:
        d = soup.new_tag('meta', attrs={'name':'description', 'content':desc_text})
        head.append(d)

    # Canonical
    canon = head.find('link', rel='canonical')
    if canon: canon['href'] = "https://www.nexmartshop.ai/404.html"
    else:
        c = soup.new_tag('link', rel='canonical', href="https://www.nexmartshop.ai/404.html")
        head.append(c)

    # Clean existing OG/Twitter
    for tag in head.find_all('meta', attrs={'property': lambda x: x and x.startswith('og:')}): tag.decompose()
    for tag in head.find_all('meta', attrs={'name': lambda x: x and x.startswith('twitter:')}): tag.decompose()

    # Add new OG/Twitter
    og_tags = [
        {'property': 'og:title', 'content': title_text},
        {'property': 'og:description', 'content': desc_text},
        {'property': 'og:type', 'content': 'website'},
        {'property': 'og:url', 'content': "https://www.nexmartshop.ai/404.html"},
        {'property': 'og:image', 'content': "https://www.nexmartshop.ai/nexmart_dashboard.png"}
    ]

    twitter_tags = [
        {'name': 'twitter:card', 'content': 'summary_large_image'},
        {'name': 'twitter:title', 'content': title_text},
        {'name': 'twitter:description', 'content': desc_text},
        {'name': 'twitter:image', 'content': "https://www.nexmartshop.ai/nexmart_dashboard.png"}
    ]

    for tag_data in og_tags + twitter_tags:
        m = soup.new_tag('meta', attrs=tag_data)
        head.append(m)
        
# Add Alts to Images
for img in soup.find_all('img'):
    if not img.get('alt'):
        src = img.get('src', '').lower()
        if 'logo' in src or 'pm.png' in src or 'am.png' in src:
            img['alt'] = "Nexmart Company Logo"
        elif img.find_parent('section', class_='is-hero'):
            img['alt'] = "404 Page Hero Graphic"
        else:
            img['alt'] = ""

with open('404.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
