import re

with open('magic-ai-search.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Cleanly remove the glowing cube graphic from the footer
html = re.sub(r'<div class="footer_graphic-wrap">.*?</div>\s*<div class="container-large">', '<div class="container-large">', html, flags=re.DOTALL)

# Add a purple-themed footer background overriding the black one
footer_override = """
    /* Magic AI Search Footer */
    .footer_component {
        background: linear-gradient(180deg, #1b0a3d 0%, #050505 100%) !important;
        position: relative;
    }
    .footer_component::before {
        content: ''; position: absolute; top: 0; left: 0; right: 0; height: 1px;
        background: linear-gradient(90deg, transparent, rgba(91, 61, 245, 0.4), transparent);
    }
"""

# Only add if we haven't already
if "Magic AI Search Footer" not in html:
    html = html.replace('</style>', f'{footer_override}</style>')

with open('magic-ai-search.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Applied safe purple footer & removed graphic.')
