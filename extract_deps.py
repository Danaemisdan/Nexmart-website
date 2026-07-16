import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print('--- CSS Links ---')
for match in re.findall(r'<link[^>]+rel="stylesheet"[^>]*>', html, re.IGNORECASE):
    print(match)

print('\n--- JS Scripts ---')
for match in re.findall(r'<script[^>]*>.*?</script>', html, re.DOTALL | re.IGNORECASE):
    if 'src=' in match:
        tag = re.search(r'<script[^>]+>', match).group(0)
        print(tag)
    else:
        print('<script> [Inline script] </script>')
