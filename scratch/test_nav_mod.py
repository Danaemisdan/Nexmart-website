import os
from bs4 import BeautifulSoup
import shutil

# Make a copy of index.html for testing
shutil.copy('index.html', 'scratch/index_test.html')

with open('scratch/index_test.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

products_panel = soup.find('div', class_='mega-nav__dropdown-panel', attrs={'data-nav-content': 'products'})

if products_panel:
    # 1. Remove How it works (is-video)
    video_col = products_panel.find('div', class_='mega-nav__panel-col is-video')
    if video_col:
        video_col.decompose()
        
    # 2. Remove Extension, Theme, Stores (is-bottom)
    bottom_cols = products_panel.find_all('div', class_='mega-nav__panel-col is-bottom')
    for col in bottom_cols:
        col.decompose()
        
    # 3. Align perfectly
    # Find the inner container
    inner = products_panel.find('div', class_='mega-nav__dropdown-inner')
    if inner:
        # Instead of grid, we can just use flex and center it
        inner['style'] = "display: flex; justify-content: center; align-items: flex-start; width: 100%; gap: 40px; padding: 20px 0;"

with open('scratch/index_test.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
print("Done modifying scratch/index_test.html")
