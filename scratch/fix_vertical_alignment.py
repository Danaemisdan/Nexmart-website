import glob
import re

def fix_vertical_alignment():
    html_files = glob.glob('*.html')
    
    for file_path in html_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Bound search to products menu
            start = content.find('<div aria-label="products menu"')
            if start == -1:
                start = content.find('data-nav-content="products"')
                if start == -1: continue
                start = content.rfind('<div', 0, start)
                
            end = content.find('data-nav-content="resources"', start)
            if end == -1: end = len(content)
                
            panel_content = content[start:end]
            
            # 1. Update mega-nav__dropdown-inner to have larger vertical padding
            panel_content = panel_content.replace(
                'padding: 24px 40px;',
                'padding: 64px 40px;'
            )
            
            # 2. Update mega-nav__panel-list to have larger row gap
            panel_content = panel_content.replace(
                'gap: 40px;',
                'row-gap: 64px; column-gap: 40px;'
            )
            
            new_content = content[:start] + panel_content + content[end:]
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
                
            print(f"Fixed vertical alignment in {file_path}")
            
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    fix_vertical_alignment()
