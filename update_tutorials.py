import os
import glob
import bs4
import shutil

tutorials = [
    {
        "href": "getting-started.html",
        "title": "Getting Started",
        "desc": "Your first 10 minutes with Nexmart."
    },
    {
        "href": "agentic-commerce-101.html",
        "title": "Agentic Commerce 101",
        "desc": "Understand how AI shops for you."
    },
    {
        "href": "mastering-ai-prompts.html",
        "title": "Mastering AI Prompts",
        "desc": "Learn how to get the best results from your AI shopping assistant."
    },
    {
        "href": "shopping-workflows.html",
        "title": "Shopping Workflows",
        "desc": "From product discovery to delivery."
    },
    {
        "href": "orders-and-returns.html",
        "title": "Orders & Returns",
        "desc": "Track, manage, and return purchases with confidence."
    },
    {
        "href": "power-user-guide.html",
        "title": "Power User Guide",
        "desc": "Advanced tips and workflows for experienced Nexmart users."
    }
]

def build_tutorial_item(tut):
    return f'''<li class="mega-nav__panel-item" data-menu-fade="">
   <a class="mega-nav__panel-link w-inline-block" data-nav-link="" href="{tut['href']}">
    <div class="mega-nav__panel-text-wrap">
     <div class="mega-nav__panel-top-wrap">
      <span class="mega-nav__panel-link-text">
       {tut['title']}
      </span>
     </div>
     <span class="mega-nav__panel-link-desc">
      {tut['desc']}
     </span>
    </div>
    <div class="mega-nav__link-bg" data-nav-link-bg="">
    </div>
   </a>
  </li>'''

new_ul_content = "\n".join([build_tutorial_item(t) for t in tutorials])

html_files = glob.glob("*.html")
for file in html_files:
    if "backup" in file or file == "cta_template.html":
        continue
        
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = bs4.BeautifulSoup(html, 'html.parser')
    
    # Find Quick Tutorials section
    qt_label = soup.find(string=lambda text: text and 'Quick Tutorials' in text)
    if qt_label:
        panel_col = qt_label.find_parent('div', class_='mega-nav__panel-col')
        if panel_col:
            ul = panel_col.find('ul', class_='mega-nav__panel-list')
            if ul:
                # Replace content
                new_ul = bs4.BeautifulSoup(new_ul_content, 'html.parser')
                ul.clear()
                for child in new_ul.children:
                    ul.append(child)
                    
                with open(file, 'w', encoding='utf-8') as f:
                    f.write(str(soup))
                print(f"Updated tutorials in {file}")

# Create placeholder pages if they don't exist
# Use about.html as a base but strip out the semantic wrapper content
placeholder_base = "about.html"
if os.path.exists(placeholder_base):
    with open(placeholder_base, 'r', encoding='utf-8') as f:
        base_soup = bs4.BeautifulSoup(f.read(), 'html.parser')
        
    wrapper = base_soup.find('div', class_='semantic-about-wrapper')
    if wrapper:
        placeholder_content = bs4.BeautifulSoup('''
        <div class="semantic-placeholder-wrapper" style="padding: 180px 5%; text-align: center; min-height: 60vh; display: flex; align-items: center; justify-content: center; background: #ffffff;">
            <div>
                <h1 style="font-size: 48px; color: #111827; margin-bottom: 24px;">Content Coming Soon</h1>
                <p style="font-size: 20px; color: #4B5563;">This tutorial is currently being written by the Nexmart editorial team.</p>
            </div>
        </div>
        ''', 'html.parser')
        wrapper.replace_with(placeholder_content)
        
    base_html = str(base_soup)
    
    for t in tutorials:
        if not os.path.exists(t['href']):
            # Also update title
            page_soup = bs4.BeautifulSoup(base_html, 'html.parser')
            if page_soup.title:
                page_soup.title.string = f"Nexmart - {t['title']}"
            with open(t['href'], 'w', encoding='utf-8') as f:
                f.write(str(page_soup))
            print(f"Created placeholder page: {t['href']}")
