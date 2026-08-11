import os
import glob
import re

def update_nav():
    html_files = glob.glob('*.html')
    
    for file_path in html_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # We only want to modify the products dropdown panel, not the resources panel.
            # Find the products panel start and end to isolate modifications
            start = content.find('<div aria-label="products menu"')
            if start == -1:
                # Some files might not have the aria-label on the panel, fallback
                start = content.find('data-nav-content="products"')
                if start == -1:
                    continue
                # back up to the <div
                start = content.rfind('<div', 0, start)
                
            # Find the start of the resources menu to bound our search
            end = content.find('data-nav-content="resources"', start)
            if end == -1:
                end = len(content)
                
            panel_content = content[start:end]
            
            # Remove is-video
            panel_content = re.sub(r'<div class="mega-nav__panel-col is-video".*?</ul></div>', '', panel_content, flags=re.DOTALL)
            
            # Remove all is-bottom
            panel_content = re.sub(r'<div class="mega-nav__panel-col is-bottom".*?</ul></div>', '', panel_content, flags=re.DOTALL)
            
            # Center the is-products column
            panel_content = panel_content.replace('class="mega-nav__panel-col is-products"', 'class="mega-nav__panel-col is-products" style="margin: 0 auto; width: 100%; max-width: 1200px;"')
            
            # Change _3-column to a 5 column grid for perfect alignment of the 10 items
            panel_content = panel_content.replace('class="mega-nav__panel-list _3-column"', 'class="mega-nav__panel-list" style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 24px;"')
            
            # Reconstruct content
            new_content = content[:start] + panel_content + content[end:]
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
                
            print(f"Updated {file_path}")
            
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    update_nav()
