import glob
import re
import os

legal_items = [
    ("Privacy Policy", "privacy-policy.html"),
    ("Terms &amp; Conditions", "terms-and-conditions.html"),
    ("Refund Policy", "refund-policy.html"),
    ("Return Policy", "return-policy.html"),
    ("Cancellation Policy", "cancellation-policy.html"),
    ("Checkout Policy", "checkout-policy.html")
]

item_template = '<li class="footer_link-list-item"><a class="footer_link w-inline-block" data-footer-link="" href="{href}"><img alt="" class="footer_link-icon" data-footer-icon="" loading="lazy" src="https://cdn.prod.website-files.com/69c4a4d640fdca68c1cc9685/69d1ce53a28ce00ec75c1f97_Arrow%20Right%20-%20White%20-%20Small.svg"/><div class="footer_link_text">{text}</div></a></li>'

items_html = "".join([item_template.format(text=text, href=href) for text, href in legal_items])

legal_column = f'<div class="footer_link-wrap"><div class="heading-style-x w-variant-f484ff60-942c-2ce3-cd91-21603741d6f8 w-richtext" data-number="30" data-wf--heading--heading-style="text-r"><p>Legal</p></div><ul class="footer_link-list">{items_html}</ul></div>'

html_files = glob.glob('*.html')

for file in html_files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            html = f.read()

        # Insert Legal Column after Resources
        # Match the Resources block
        res_pattern = r'(<div class="footer_link-wrap">[^<]*<div[^>]*><p>Resources</p></div>.*?</ul></div>)'
        
        # Only replace if Legal is not already there to prevent duplicates
        if '<p>Legal</p>' not in html:
            html = re.sub(res_pattern, r'\1' + legal_column, html)

        # Remove the bottom legal links
        bottom_links_pattern = r'<ul class="footer_legal-link-list">.*?</ul>'
        html = re.sub(bottom_links_pattern, '', html)

        with open(file, 'w', encoding='utf-8') as f:
            f.write(html)
            
        print(f"Successfully processed {file}")
    except Exception as e:
        print(f"Error processing {file}: {e}")
