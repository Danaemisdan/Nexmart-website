import bs4
import shutil

s = bs4.BeautifulSoup(open('financial-inclusion.html', encoding='utf-8'), 'html.parser')
body = s.find('body')
if body:
    body['class'] = ['theme-color-blue']
    body['data-barba'] = 'wrapper'
    
main = s.find(class_='main-wrapper')
if main:
    main['data-barba'] = 'container'
    
with open('financial-inclusion-test.html', 'w', encoding='utf-8') as f:
    f.write(str(s))
    
print('Saved test file.')
