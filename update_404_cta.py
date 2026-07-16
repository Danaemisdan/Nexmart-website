from bs4 import BeautifulSoup

def update_404():
    # 1. Inspect index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        index_soup = BeautifulSoup(f, 'html.parser')
        
    # Search for an anchor that looks like tools, products, features, etc.
    tools_anchor = None
    
    # Let's look for sections or divs with ids like 'tools', 'products', 'features'
    # Also check the navigation links to see where 'Tools' points on the homepage
    
    nav_links = index_soup.find_all('a')
    for link in nav_links:
        if link.string and "Tools" in link.string:
            href = link.get('href', '')
            if href.startswith('#'):
                tools_anchor = href[1:] # remove #
                break
                
    if not tools_anchor:
        # Fallback to scanning sections
        for tag in index_soup.find_all(id=True):
            tag_id = tag.get('id', '').lower()
            if 'tool' in tag_id or 'product' in tag_id or 'feature' in tag_id:
                tools_anchor = tag_id
                break

    final_href = f"index.html#{tools_anchor}" if tools_anchor else "index.html"
    
    # 2. Update 404.html
    with open('404.html', 'r', encoding='utf-8') as f:
        html_404 = f.read()
        
    soup_404 = BeautifulSoup(html_404, 'html.parser')
    
    # Find the "Explore Tools" button
    for a in soup_404.find_all('a', class_='button-wrap'):
        text = a.get_text().strip()
        if text == "Explore Tools":
            a['href'] = final_href
            break
            
    with open('404.html', 'w', encoding='utf-8') as f:
        f.write(str(soup_404))
        
    print(f"ANCHOR_FOUND: {bool(tools_anchor)}")
    print(f"FINAL_HREF: {final_href}")

if __name__ == "__main__":
    update_404()
