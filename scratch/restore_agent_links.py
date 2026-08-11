import re

def revert_home_links():
    file_path = 'index.html'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # The structure is roughly:
    # <h3>Research Agent</h3> ... <a ... href="https://app.nexmartshop.ai/solutions/portfolio">
    
    mappings = {
        'Research Agent': ('https://app.nexmartshop.ai/solutions/portfolio', 'research-agent.html'),
        'Price Agent': ('https://app.nexmartshop.ai/solutions/shop-library', 'price-agent.html'),
        'Quality Agent': ('https://app.nexmartshop.ai/solutions/advertiser-library', 'quality-agent.html'),
        'Tracking Agent': ('https://app.nexmartshop.ai/solutions/advertiser-tracker', 'tracking-agent.html'),
        'Discovery Agent': ('https://app.nexmartshop.ai/solutions/magic-ai-search', 'discovery-agent.html')
    }
    
    # Wait, I don't know the exact external links for Discovery, Quality, and Tracking.
    # It's safer to use BeautifulSoup to find the exact buttons.
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')
    
    updated = 0
    for a_tag in soup.find_all('a', class_='button-wrap'):
        parent_div = a_tag.parent
        if parent_div and parent_div.parent:
            h3 = parent_div.parent.find('h3')
            if h3:
                title = h3.text.strip()
                for key in mappings:
                    if key in title: # In case of weird spacing
                        target_html = mappings[key][1]
                        if a_tag.get('href') != target_html:
                            a_tag['href'] = target_html
                            updated += 1
                            print(f"Updated {title} to {target_html}")
    
    if updated > 0:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"Successfully restored {updated} links.")
    else:
        print("No links needed updating.")

if __name__ == "__main__":
    revert_home_links()
