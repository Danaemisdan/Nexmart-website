import os
import bs4

def update_nav_menu():
    files_updated = 0
    # Process all HTML files in the current directory
    for filename in os.listdir('.'):
        if not filename.endswith('.html'):
            continue
            
        with open(filename, 'r', encoding='utf-8') as f:
            html = f.read()
            
        soup = bs4.BeautifulSoup(html, 'html.parser')
        modified = False
        
        # 1. Remove the bottom row items (Extension, Stores, Theme)
        bottom_cols = soup.find_all('div', class_=lambda c: c and 'mega-nav__panel-col' in c and 'is-bottom' in c)
        for col in bottom_cols:
            col.decompose()
            modified = True
            
        # 2. Remove the video thumbnail (white logo on blue box)
        thumbnails = soup.find_all('img', class_='mega-nav__video-thumbnail')
        for thumb in thumbnails:
            thumb.decompose()
            modified = True
            
        if modified:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            files_updated += 1
            
    print(f'Successfully updated {files_updated} HTML files.')

if __name__ == "__main__":
    update_nav_menu()
