import re

def fix():
    with open('magic-ai-search.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    start = content.find('<style>', content.find('twitter:image'))
    end = content.find('</style>', start) + len('</style>')
    
    if start != -1 and end != -1:
        style_content = content[start:end]
        if '.magic-wrapper' in style_content:
            print("Found style block!")
            content = content[:start] + content[end:]
            
            target = '<main class="magic-wrapper" data-barba="container">'
            t_pos = content.find(target)
            if t_pos != -1:
                insert_pos = t_pos + len(target)
                content = content[:insert_pos] + '\n' + style_content + content[insert_pos:]
                
                with open('magic-ai-search.html', 'w', encoding='utf-8') as f:
                    f.write(content)
                print("Fixed magic-ai-search.html")
            else:
                print("Could not find target main tag")
        else:
            print("Could not find magic-wrapper in style block")
    else:
        print("Could not find style block")

if __name__ == "__main__":
    fix()
