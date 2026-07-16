import bs4

with open('faqs.html', 'r', encoding='utf-8') as f:
    soup = bs4.BeautifulSoup(f.read(), 'html.parser')

print("HERO:")
hero = soup.find('section', class_=lambda c: c and 'is-hero' in c)
if hero:
    print(hero.prettify())

print("\nFAQ:")
faq = soup.find('section', class_=lambda c: c and 'resources-faq-section' in c)
if faq:
    print(faq.prettify()[:1500])
