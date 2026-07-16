import bs4

def fix_global_elements():
    with open('index.html', 'r', encoding='utf-8') as f:
        index_soup = bs4.BeautifulSoup(f.read(), 'html.parser')
        
    correct_ge = index_soup.find('div', class_='global_elements')
    
    with open('advertiser-tracker.html', 'r', encoding='utf-8') as f:
        target_soup = bs4.BeautifulSoup(f.read(), 'html.parser')
        
    corrupt_ge = target_soup.find('div', class_='global_elements')
    
    if correct_ge and corrupt_ge:
        corrupt_ge.replace_with(correct_ge)
        with open('advertiser-tracker.html', 'w', encoding='utf-8') as f:
            f.write(str(target_soup))
        print("Successfully replaced global_elements block.")
    else:
        print("Could not find global_elements.")

if __name__ == "__main__":
    fix_global_elements()
