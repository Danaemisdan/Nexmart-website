import bs4

def run():
    with open('magic-ai-search.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = bs4.BeautifulSoup(html, 'html.parser')
    
    # 1. Save the footer so it isn't deleted
    footer = soup.find('footer', class_='footer_component')
    if footer:
        footer = footer.extract()
    else:
        print("Warning: footer not found!")
        return

    # 2. Find the new main wrapper
    new_main = soup.find('main', class_='magic-wrapper')
    if not new_main:
        print("Warning: new magic-wrapper not found!")
        return

    # 3. Find the old main wrapper and completely remove it
    old_main = soup.find('main', class_='main-wrapper')
    if old_main:
        old_main.decompose()
        print("Success: Removed old main-wrapper (Tracking Agent, Earth, Cards, etc.)")
    else:
        print("Warning: old main-wrapper not found!")

    # 4. Append the footer to the end of the new main wrapper
    if footer and new_main:
        new_main.append(footer)
        print("Success: Appended footer to new magic-wrapper")

    # Save the file
    with open('magic-ai-search.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))

if __name__ == '__main__':
    run()
