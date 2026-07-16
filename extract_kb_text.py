from bs4 import BeautifulSoup
import json

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

text_elements = soup.find_all(string=True)
visible_texts = []

for t in text_elements:
    if t.parent.name not in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        txt = t.strip()
        if len(txt) > 0:
            visible_texts.append(txt)

with open('extracted_text.txt', 'w', encoding='utf-8') as out:
    out.write('\n'.join(visible_texts))

head = soup.find('head')
schema = head.find('script', type='application/ld+json') if head else None
if schema:
    with open('extracted_text.txt', 'a', encoding='utf-8') as out:
        out.write('\n\n--- SCHEMA ---\n')
        out.write(schema.string)

meta_tags = head.find_all('meta') if head else []
with open('extracted_text.txt', 'a', encoding='utf-8') as out:
    out.write('\n\n--- META ---\n')
    for m in meta_tags:
        if m.get('content'):
            name = m.get('name') or m.get('property') or 'unknown'
            out.write(f"{name}: {m.get('content')}\n")
