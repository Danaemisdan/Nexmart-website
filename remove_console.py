import bs4

with open('agentic-commerce.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = bs4.BeautifulSoup(html, 'html.parser')

# Find and remove the neural-ledger div
neural_ledger = soup.find('div', class_='neural-ledger')

if neural_ledger:
    neural_ledger.decompose()
    print('SUCCESS: neural-ledger div removed.')
else:
    print('ERROR: neural-ledger div not found.')

# Verify it is gone
verify = soup.find('div', class_='neural-ledger')
if verify:
    print('ERROR: neural-ledger still exists in the DOM.')
else:
    print('VERIFIED: neural-ledger no longer exists in the DOM.')

with open('agentic-commerce.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print('File saved.')
