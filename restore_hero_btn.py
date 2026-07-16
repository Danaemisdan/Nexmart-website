import bs4

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = bs4.BeautifulSoup(html, 'html.parser')
hero = soup.find('section', class_=lambda c: c and 'is-hero' in c)

if hero:
    buttons = hero.find_all('a', class_=lambda c: c and 'button-wrap' in c)
    if len(buttons) > 1:
        target_btn = buttons[1]
        
        # The user wants exact original styling but text "Download App"
        # We will reconstruct it from what was found in index_original.html, adjusted for Nexmart
        
        new_btn_html = """
<a aria-label="Download App" class="button-wrap w-variant-fdd894b6-a4c6-5062-b405-6cbc95c85455 w-inline-block" data-video-lightbox-control="" data-video-lightbox-src="" data-wf--button-main--style-variant="white" href="https://chromewebstore.google.com/detail/nexmart-product-research/pgccoaecgcgnhffkjjcaonjoockggmng?pli=1" target="_blank"><div class="button w-variant-fdd894b6-a4c6-5062-b405-6cbc95c85455"><div class="button-content"><img alt="" class="button-icon-main is-left" loading="lazy" src="./ChatGPT Image May 31, 2026, 01_17_29 PM.png"/><div>Download App</div></div><div class="button-bg-wrap"><div class="button-bg w-variant-fdd894b6-a4c6-5062-b405-6cbc95c85455"></div><div class="button-bg-hover w-variant-fdd894b6-a4c6-5062-b405-6cbc95c85455"></div></div></div></a>
        """.strip()
        
        new_btn_soup = bs4.BeautifulSoup(new_btn_html, 'html.parser').a
        
        target_btn.replace_with(new_btn_soup)
        
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(str(soup))
            
        print('Successfully restored the Download App button in the Hero section.')
    else:
        print('Could not find the second button in the hero section.')
else:
    print('Could not find the hero section.')
