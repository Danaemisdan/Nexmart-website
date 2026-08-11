import glob
import re

def fix_alignment():
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
            
            # 1. Update mega-nav__dropdown-inner to flex center
            panel_content = re.sub(
                r'(<div class="mega-nav__dropdown-inner"[^>]*>)',
                r'<div class="mega-nav__dropdown-inner" style="display: flex; justify-content: center; width: 100%; padding: 24px 40px; box-sizing: border-box;">',
                panel_content,
                count=1
            )
            
            # 2. Update is-products max-width
            panel_content = re.sub(
                r'class="mega-nav__panel-col is-products"[^>]*>',
                r'class="mega-nav__panel-col is-products" style="margin: 0 auto; width: 100%; max-width: 1400px;">',
                panel_content
            )
            
            # 3. Update mega-nav__panel-list gap and style
            panel_content = re.sub(
                r'class="mega-nav__panel-list" style="display: grid[^"]*"',
                r'class="mega-nav__panel-list" style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 40px;"',
                panel_content
            )
            
            new_content = content[:start] + panel_content + content[end:]
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
                
            print(f"Fixed alignment in {file_path}")
            
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    fix_alignment()
