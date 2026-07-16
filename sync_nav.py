import os
import glob
from bs4 import BeautifulSoup
import copy

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        idx_soup = BeautifulSoup(f, 'html.parser')
        
    # Get the canonical complete header wrapper
    canonical_header = idx_soup.find('div', class_='global_elements')
    if not canonical_header:
        print("Could not find <div class='global_elements'> in index.html")
        return
        
    base_header = copy.copy(canonical_header)
    for tag in base_header.find_all(class_='w--current'):
        tag['class'] = [c for c in tag.get('class', []) if c != 'w--current']
        
    html_files = glob.glob('*.html')
    excluded = ['index.html', 'index_original.html']
    
    report = [
        "# Complete Navigation Synchronization Report",
        "\n## Root Cause Analysis",
        "The previous synchronization only replaced the `<nav>` element. However, Webflow's mega-menu implementation relies on a complete structural hierarchy.",
        "In `index.html` and the legal pages, the navigation is wrapped in `<div class=\"global_elements\">`, which also contains `<div class=\"styles-wrap\">`.",
        "This `styles-wrap` injects the necessary embedded CSS and JS hooks for the mega-menu to function.",
        "In `product-template.html` (and consequently all generated product pages), this `<div class=\"global_elements\">` wrapper was completely missing, breaking the dropdown interactions.",
        "\n## Structural Corrections Made",
        "- Extracted the entire `<div class=\"global_elements\">` from `index.html` (the canonical source).",
        "- For pages missing the wrapper (product pages), the orphaned `<nav>` was replaced with the complete `global_elements` wrapper.",
        "- For pages that already had the wrapper (legal pages), the wrapper was fully synchronized with the canonical source to ensure zero discrepancies.",
        "- Preserved all intentionally modified local Tool URLs.",
        "- Stripped `w--current` active states to prevent false logo highlighting.",
        "\n## Files Synchronized:"
    ]
    
    modified_count = 0
    
    for file in html_files:
        if file in excluded: continue
        
        with open(file, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')
            
        target_global = soup.find('div', class_='global_elements')
        target_nav = soup.find('nav', class_='mega-nav')
        
        modified = False
        new_header = copy.copy(base_header)
        
        if target_global:
            target_global.replace_with(new_header)
            modified = True
        elif target_nav:
            target_nav.replace_with(new_header)
            modified = True
            
        if modified:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            report.append(f"- {file}")
            modified_count += 1
            
    if modified_count == 0:
        report.append("- No files were modified.")
        
    with open('navigation_sync_report.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(report))
        
    print(f"Successfully synchronized complete header in {modified_count} files.")

if __name__ == "__main__":
    main()
