content = open('index.html', encoding='utf-8').read()

old = 'href="https://app.nexmartshop.ai/"'
new = 'href="https://app.nexmartshop.ai"'

if old in content:
    updated = content.replace(old, new, 1)
    open('index.html', 'w', encoding='utf-8').write(updated)
    print('Updated Download App link successfully!')
else:
    print('Not found.')
