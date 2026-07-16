import re

with open('index.html', 'r', encoding='utf-8') as f:
    html1 = f.read()
with open('agentic-commerce.html', 'r', encoding='utf-8') as f:
    html2 = f.read()

head1 = re.search(r'<head>(.*?)</head>', html1, re.DOTALL | re.IGNORECASE).group(1)
head2 = re.search(r'<head>(.*?)</head>', html2, re.DOTALL | re.IGNORECASE).group(1)

css1 = re.findall(r'<link[^>]*rel="stylesheet"[^>]*>', head1)
css2 = re.findall(r'<link[^>]*rel="stylesheet"[^>]*>', head2)

print('CSS in index.html:')
for c in css1: print(' ', c)

print('CSS in agentic-commerce.html:')
for c in css2: print(' ', c)
