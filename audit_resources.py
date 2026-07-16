import json
import re

with open('audit_results.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print('--- Resources Mega Menu Links ---')
tools_items = []
for d in data:
    if 'mega-nav' in d['element'] and 'logo' not in d['element'] and 'panel-link' in d['element']:
        text = re.sub(r'(@keyframes.*?\}|\.[\w-]+\s*\{.*?\})', '', d['text'], flags=re.DOTALL)
        text = re.sub(r'\s+', ' ', text).strip()
        # Resources are generally: Blog, Nexmart University, FAQs, About Us, Discord Community, Contact
        if any(keyword in text for keyword in ['Blog', 'University', 'FAQs', 'About Us', 'Discord', 'Contact']):
            tools_items.append({
                'text': text,
                'href': d['destination']
            })

for t in tools_items:
    print(f"TEXT: {t['text']} | HREF: {t['href']}")
