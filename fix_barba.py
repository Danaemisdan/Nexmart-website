with open('magic-ai-search.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
html = re.sub(r'<main class="magic-wrapper">', r'<main class="magic-wrapper" data-barba="container">', html)

with open('magic-ai-search.html', 'w', encoding='utf-8') as f:
    f.write(html)
