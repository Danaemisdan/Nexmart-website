from bs4 import BeautifulSoup

with open('index_original.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'lxml')

with open('img_srcs.txt', 'w', encoding='utf-8') as f:
    for img in soup.find_all('img'):
        f.write(img.get('src', '') + '\n')

with open('p_texts.txt', 'w', encoding='utf-8') as f:
    for p in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        if p.string and len(p.string.strip()) > 0:
            f.write(p.name + ": " + p.string.strip() + '\n')
