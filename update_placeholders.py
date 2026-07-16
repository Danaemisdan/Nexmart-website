import bs4

pages_data = {
    'blog.html': {
        'title': 'Nexmart Blog',
        'desc': 'Insights, product updates, and thought leadership on the future of commerce.'
    },
    'faqs.html': {
        'title': 'Frequently Asked Questions',
        'desc': 'Everything you need to know about navigating the Nexmart ecosystem.'
    },
    'nexmart-university.html': {
        'title': 'Nexmart University',
        'desc': 'Master the AI shopping ecosystem with comprehensive tutorials and guides.'
    },
    'about.html': {
        'title': 'About Nexmart',
        'desc': 'We are building the intelligence layer for global commerce.'
    },
    'contact.html': {
        'title': 'Contact Us',
        'desc': 'Our support team is here to help you scale.'
    },
    'discord-community.html': {
        'title': 'Discord Community',
        'desc': 'Join the conversation with thousands of Nexmart users and partners.'
    }
}

template_hero = """
<section class="section is-hero" style="padding-top: 160px; padding-bottom: 60px;">
  <div class="container-large">
    <div class="heading-wrap w-variant-8f3c9782-a221-5903-b5cc-b92b540e7e17" data-wf--heading-block--layout="center-aligned" style="max-width: 800px; margin: 0 auto; text-align: center;">
      <h1 class="heading-style-x" style="font-size: 56px; line-height: 1.1; margin-bottom: 24px; font-weight: 600; color: #fff; letter-spacing: -0.02em;">{title}</h1>
      <p class="paragraph-style-x" style="font-size: 20px; line-height: 1.5; color: #94A3B8;">{desc}</p>
    </div>
  </div>
</section>
"""

template_placeholder = """
<section class="section" style="padding-bottom: 120px;">
  <div class="container-large" style="display: flex; justify-content: center;">
    <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.05); border-radius: 24px; padding: 100px 40px; text-align: center; width: 100%; max-width: 800px;">
        <h2 style="font-size: 28px; font-weight: 500; margin-bottom: 16px; color: #fff;">Content Coming Soon</h2>
        <p style="color: #94A3B8; font-size: 18px; margin: 0;">We are currently designing the flagship experience for this page.<br/>Check back shortly.</p>
    </div>
  </div>
</section>
"""

template_cta = """
<section class="section" style="padding: 100px 5%; background-color: #0b1120; border-top: 1px solid rgba(255,255,255,0.05);">
  <div class="container-large" style="display: flex; flex-direction: column; align-items: center; text-align: center;">
    <h2 style="color: #FFFFFF; font-size: 42px; font-weight: 700; margin-bottom: 32px; letter-spacing: -0.02em;">Ready to explore the ecosystem?</h2>
    <a aria-label="Start Free Trial" class="button-wrap w-inline-block" data-wf--button-main--style-variant="brand" href="https://app.nexmartshop.ai/sign-up" target="_blank">
        <div class="button">
            <div class="button-content">Start Shopping With AI</div>
            <div class="button-bg-wrap">
                <div class="button-bg"></div>
                <div class="button-bg-hover"></div>
            </div>
        </div>
    </a>
  </div>
</section>
"""

for file, data in pages_data.items():
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = bs4.BeautifulSoup(html, 'html.parser')
    main = soup.find('main')
    
    if main:
        footer = main.find('footer', class_='footer_component')
        main.clear()
        
        # Inject the new sections
        hero_html = template_hero.format(title=data['title'], desc=data['desc'])
        main.append(bs4.BeautifulSoup(hero_html, 'html.parser'))
        
        main.append(bs4.BeautifulSoup(template_placeholder, 'html.parser'))
        main.append(bs4.BeautifulSoup(template_cta, 'html.parser'))
        
        if footer:
            main.append(footer)
            
    with open(file, 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
print("Updated all placeholder pages with structured content.")
