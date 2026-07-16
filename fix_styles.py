import bs4
import os

def fix_file(filename, global_styles):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = bs4.BeautifulSoup(html, 'html.parser')
    
    # Get all styles in head
    head_styles = soup.head.find_all('style')
    page_specific_styles = []
    
    for style in head_styles:
        content = style.string if style.string else ""
        # If this style is not exactly one of the global styles, it's page specific
        if content.strip() not in global_styles:
            page_specific_styles.append(style.extract()) # Remove from head
            
    if page_specific_styles:
        # Find the barba container
        container = soup.find(attrs={"data-barba": "container"})
        if container:
            # Insert styles at the beginning of the container
            for style in reversed(page_specific_styles):
                container.insert(0, style)
            
            # Write back
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            print(f"Fixed {filename}: Moved {len(page_specific_styles)} style blocks.")
        else:
            print(f"Skipped {filename}: No barba container found.")
    else:
        print(f"Skipped {filename}: No page-specific styles found in head.")


def main():
    # 1. Gather global styles from index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        index_soup = bs4.BeautifulSoup(f.read(), 'html.parser')
    
    global_styles = set([s.string.strip() if s.string else "" for s in index_soup.head.find_all('style')])
    
    # 2. Fix target files
    files_to_fix = ['agentic-commerce.html', 'magic-ai-search.html', 'advertiser-tracker.html']
    
    for file in files_to_fix:
        if os.path.exists(file):
            fix_file(file, global_styles)
        else:
            print(f"File not found: {file}")

if __name__ == "__main__":
    main()
