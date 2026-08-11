import glob
import re

def update_back_button():
    html_files = glob.glob('*.html')
    
    # The old back button we injected
    old_button = '<a href="javascript:history.back()" style="margin-right: 15px; text-decoration: none; font-size: 24px; color: inherit; display: flex; align-items: center; cursor: pointer;" aria-label="Go back">&#8592;</a>'
    
    # The new back button we want to inject
    # It will sit at top: 120px to align with the eyebrow tabs, left: 4vw for good alignment on all screens
    new_button = '<a href="javascript:history.back()" style="position: absolute; top: 130px; left: 5vw; text-decoration: none; font-size: 32px; mix-blend-mode: difference; color: white; z-index: 999; transition: transform 0.2s ease; cursor: pointer;" aria-label="Go back" onmouseover="this.style.transform=\'scale(1.2)\'" onmouseout="this.style.transform=\'scale(1)\'">&#8592;</a>'
    
    for file_path in html_files:
        if file_path == 'index.html':
            continue
            
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 1. Remove old button
            if old_button in content:
                content = content.replace(f'<div class="mega-nav__bar-start">{old_button}<a ', '<div class="mega-nav__bar-start"><a ')
                content = content.replace(f'<div class="mega-nav__bar-start">\n{old_button}\n<a ', '<div class="mega-nav__bar-start">\n<a ')
                
            # 2. Inject new button at the very beginning of the <main> tag (or body if main doesn't exist)
            if new_button not in content:
                if '<main' in content:
                    # Find the end of the <main ...> opening tag
                    main_start = content.find('<main')
                    main_close = content.find('>', main_start)
                    
                    if main_close != -1:
                        content = content[:main_close+1] + new_button + content[main_close+1:]
                else:
                    # Fallback to body
                    body_start = content.find('<body')
                    body_close = content.find('>', body_start)
                    if body_close != -1:
                        content = content[:body_close+1] + new_button + content[body_close+1:]
                        
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated back button in {file_path}")
            
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    update_back_button()
