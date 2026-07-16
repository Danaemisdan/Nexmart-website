import bs4

with open('agentic-commerce.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = bs4.BeautifulSoup(html, 'html.parser')

print('--- HEADINGS ---')
for h in ['h1', 'h2', 'h3']:
    tags = soup.find_all(h)
    for tag in tags[:5]:
        print(f'{h}: class={tag.get("class", [])} text={tag.text.strip()[:40]}')

print('\n--- SECTIONS ---')
sections = soup.find_all('section')
for i, s in enumerate(sections):
    print(f'section {i}: class={s.get("class", [])} id={s.get("id")}')

print('\n--- CARDS ---')
cards = soup.find_all(class_=lambda c: c and 'card' in c)
for c in cards[:5]:
    print(f'card class={c.get("class", [])}')

print('\n--- BUTTONS ---')
btns = soup.find_all(class_=lambda c: c and 'button' in c)
for b in btns[:5]:
    print(f'button class={b.get("class", [])}')
