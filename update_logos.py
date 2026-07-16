import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            html = f.read()
        
        # Regex to find the header logo link
        # It looks something like: <a ... class="...mega-nav__bar-logo..." ... href="https://app.nexmartshop.ai/" ...>
        # We can just match the anchor tag containing the class and replace the href.
        
        def replace_href(match):
            tag = match.group(0)
            if 'mega-nav__bar-logo' in tag or 'footer_logo-link' in tag:
                # Replace the href inside this specific tag
                tag = re.sub(r'href="https://app\.nexmartshop\.ai/?"', 'href="index.html"', tag)
            return tag
            
        # Match all anchor tags
        html_updated = re.sub(r'<a\s+[^>]*>', replace_href, html)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(html_updated)
            
        print(f"Successfully processed {file}")
    except Exception as e:
        print(f"Error processing {file}: {e}")
