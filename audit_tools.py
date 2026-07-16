import json
import re

with open('audit_results.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print('--- Tools Mega Menu Links ---')
tools_items = []
for d in data:
    if 'mega-nav' in d['element'] and 'logo' not in d['element'] and 'panel-link' in d['element']:
        text = re.sub(r'(@keyframes.*?\}|\.[\w-]+\s*\{.*?\})', '', d['text'], flags=re.DOTALL)
        text = re.sub(r'\s+', ' ', text).strip()
        tools_items.append({
            'text': text,
            'href': d['destination']
        })

# Keep first 10, they are the Tools panel. Actually let's just print them all so I can manually verify.
for t in tools_items:
    print(f"TEXT: {t['text']} | HREF: {t['href']}")

print('\n--- Specific Links Requested ---')
specific = ['Watch', 'Chrome', 'Theme', 'Pre-built']
for t in tools_items:
    if any(s in t['text'] for s in specific):
        print(f"TEXT: {t['text']} | HREF: {t['href']}")

print('\n--- Logo ---')
for d in data:
    if 'mega-nav__bar-logo' in d['element']:
        print(f"TEXT: {d['text']} | HREF: {d['destination']}")
