import re
with open('magic-ai-search.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace <main class="magic-wrapper" data-barba="container"> with <main class="main-wrapper magic-wrapper" data-barba="container">
# Or if it doesn't have data-barba yet:
html = re.sub(r'<main class="magic-wrapper"[^>]*>', r'<main class="main-wrapper magic-wrapper" data-barba="container">', html)

with open('magic-ai-search.html', 'w', encoding='utf-8') as f:
    f.write(html)
