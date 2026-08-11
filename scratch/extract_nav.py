import re
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start = html.find('<nav class="mega-nav"')
end = html.find('</nav>', start) + len('</nav>')
if start != -1 and end != -1:
    with open('scratch/nav.txt', 'w', encoding='utf-8') as f:
        f.write(html[start:end])
    print('Saved nav to scratch/nav.txt')
else:
    print('Nav not found')
