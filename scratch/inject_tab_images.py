from bs4 import BeautifulSoup

def inject_tab_images():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
        
    soup = BeautifulSoup(content, 'html.parser')
    
    mapping = {
        'Discovery Agent': './discovery_preview.png',
        'Research Agent': './research_preview.png',
        'Tracking Agent': './tracking_preview.png',
        'Price Agent': './price_preview.jpg',
        'Quality Agent': './quality_preview.jpg',
        'Coupon Agent': './coupon_preview.jpg',
        'Negotiation Agent': './negotiation_preview.jpg',
        'Checkout Agent': './checkout_preview.jpg',
        'Support Agent': './support_preview.jpg'
    }
    
    updated_count = 0
    for pane in soup.find_all('div', class_='home-tab_pane'):
        h3 = pane.find('h3')
        if not h3: continue
        
        title = h3.text.strip()
        img = pane.find('img', class_='home-tab_image')
        
        if img and title in mapping:
            img['src'] = mapping[title]
            print(f"Updated '{title}' with image: {mapping[title]}")
            updated_count += 1
            
    if updated_count > 0:
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"Successfully updated {updated_count} tabs in index.html.")
    else:
        print("No tabs were updated.")

if __name__ == "__main__":
    inject_tab_images()
