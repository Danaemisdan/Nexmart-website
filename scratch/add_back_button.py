import glob
import os

def add_back_button():
    html_files = glob.glob('*.html')
    
    back_button_html = '<a href="javascript:history.back()" style="margin-right: 15px; text-decoration: none; font-size: 24px; color: inherit; display: flex; align-items: center; cursor: pointer;" aria-label="Go back">&#8592;</a>'
    
    for file_path in html_files:
        if file_path == 'index.html':
            continue
            
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find the start of the logo link inside mega-nav__bar-start
            target = '<div class="mega-nav__bar-start"><a '
            
            if target in content and back_button_html not in content:
                content = content.replace(target, f'<div class="mega-nav__bar-start">{back_button_html}<a ')
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Added back button to {file_path}")
            else:
                # Some files might have different formatting
                target2 = '<div class="mega-nav__bar-start">\n<a '
                if target2 in content and back_button_html not in content:
                    content = content.replace(target2, f'<div class="mega-nav__bar-start">\n{back_button_html}\n<a ')
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Added back button to {file_path}")
                    
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    add_back_button()
