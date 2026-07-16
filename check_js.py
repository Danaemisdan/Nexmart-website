import re
with open('agentic-commerce.html', 'r', encoding='utf-8') as f:
    html = f.read()

scripts = re.findall(r'<script[^>]*src="[^"]*dropship[^"]*"[^>]*></script>', html)
for s in scripts:
    print('agentic-commerce JS:', s)

with open('magic-ai-search.html', 'r', encoding='utf-8') as f:
    html = f.read()
scripts = re.findall(r'<script[^>]*src="[^"]*dropship[^"]*"[^>]*></script>', html)
for s in scripts:
    print('magic JS:', s)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
scripts = re.findall(r'<script[^>]*src="[^"]*dropship[^"]*"[^>]*></script>', html)
for s in scripts:
    print('index JS:', s)
