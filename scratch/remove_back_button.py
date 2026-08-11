import glob

def remove_back_button():
    html_files = glob.glob('*.html')
    
    new_button = '<a href="javascript:history.back()" style="margin-right: 16px; display: flex; align-items: center; justify-content: center; width: 36px; height: 36px; background-color: #fff; color: #000; border: 2px solid #000; border-radius: 50%; text-decoration: none; font-size: 20px; font-weight: bold; cursor: pointer; flex-shrink: 0; transition: transform 0.2s;" aria-label="Go back" onmouseover="this.style.transform=\'scale(1.1)\'" onmouseout="this.style.transform=\'scale(1)\'">&#8592;</a>'
    
    for file_path in html_files:
        if file_path == 'index.html':
            continue
            
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if new_button in content:
                content = content.replace(new_button, '')
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Removed back button from {file_path}")
            
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    remove_back_button()
