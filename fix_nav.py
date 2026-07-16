import bs4

def fix_navigation():
    # 1. Get the pure, correct navigation from index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        index_soup = bs4.BeautifulSoup(f.read(), 'html.parser')
    
    # We find the outermost navigation element by 'mega-nav' in class
    correct_nav = index_soup.find('div', class_=lambda c: c and 'mega-nav' in c)
    
    if not correct_nav:
        print("Error: Could not find correct nav in index.html")
        return
        
    # 2. Open the corrupted advertiser-tracker.html
    with open('advertiser-tracker.html', 'r', encoding='utf-8') as f:
        target_soup = bs4.BeautifulSoup(f.read(), 'html.parser')
        
    corrupt_nav = target_soup.find('div', class_=lambda c: c and 'mega-nav' in c)
    if not corrupt_nav:
        print("Error: Could not find nav in advertiser-tracker.html")
        return
        
    # 3. Replace the corrupt nav with the correct nav
    corrupt_nav.replace_with(correct_nav)
    
    # 4. Save
    with open('advertiser-tracker.html', 'w', encoding='utf-8') as f:
        f.write(str(target_soup))
        
    print("Successfully restored navigation in advertiser-tracker.html from index.html.")

if __name__ == "__main__":
    fix_navigation()
