import glob

def update_back_button():
    html_files = glob.glob('*.html')
    
    floating_button = '<a href="javascript:history.back()" style="position: absolute; top: 130px; left: 5vw; text-decoration: none; font-size: 32px; mix-blend-mode: difference; color: white; z-index: 999; transition: transform 0.2s ease; cursor: pointer;" aria-label="Go back" onmouseover="this.style.transform=\'scale(1.2)\'" onmouseout="this.style.transform=\'scale(1)\'">&#8592;</a>'
    
    new_button = '<a href="javascript:history.back()" style="margin-right: 16px; display: flex; align-items: center; justify-content: center; width: 36px; height: 36px; background-color: #fff; color: #000; border: 2px solid #000; border-radius: 50%; text-decoration: none; font-size: 20px; font-weight: bold; cursor: pointer; flex-shrink: 0; transition: transform 0.2s;" aria-label="Go back" onmouseover="this.style.transform=\'scale(1.1)\'" onmouseout="this.style.transform=\'scale(1)\'">&#8592;</a>'
    
    for file_path in html_files:
        if file_path == 'index.html':
            continue
            
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 1. Remove floating button from anywhere in the document
            content = content.replace(floating_button, '')
            
            # 2. Inject new button into the navbar (mega-nav__bar-start)
            target = '<div class="mega-nav__bar-start"><a '
            target2 = '<div class="mega-nav__bar-start">\n<a '
            
            if new_button not in content:
                if target in content:
                    content = content.replace(target, f'<div class="mega-nav__bar-start">{new_button}<a ')
                elif target2 in content:
                    content = content.replace(target2, f'<div class="mega-nav__bar-start">\n{new_button}\n<a ')
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated back button in {file_path}")
            
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    update_back_button()
