import bs4
import shutil

# Make a backup just in case
shutil.copy('about.html', 'about_backup.html')

with open('about.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = bs4.BeautifulSoup(html, 'html.parser')

# 1. Update Title
if soup.title:
    soup.title.string = "Nexmart - About Us"

# 2. Update Hero
hero = soup.find('section', class_=lambda c: c and 'is-hero' in c)
if hero:
    hero['style'] = hero.get('style', '') + '; background-color: #ffffff; color: #111827;'
    h1 = hero.find('h1')
    if h1:
        h1.string = "The Future of Commerce Starts Here"
        h1['style'] = h1.get('style', '') + '; color: #111827 !important;'
    p = hero.find('p')
    if p:
        p.string = "Nexmart is building the world's first Agentic Commerce ecosystem, where intelligent AI agents understand your intent, make informed purchasing decisions, and remove the friction from modern shopping."
        p['style'] = p.get('style', '') + '; color: #4B5563 !important;'

# 3. Build About Content HTML
about_html = """
<div class="semantic-about-wrapper" style="background-color: #ffffff; padding-top: 40px; padding-bottom: 120px; width: 100%;">
  <div style="max-width: 1000px; margin: 0 auto; padding: 0 5%; width: 100%; box-sizing: border-box; display: flex; flex-direction: column; gap: 120px;">
    
    <!-- SECTION 1: OUR VISION -->
    <div style="max-width: 800px; margin: 0 auto; text-align: center;">
      <h2 style="font-size: 36px; font-weight: 600; color: #111827; margin-bottom: 32px; letter-spacing: -0.02em; line-height: 1.2;">We Believe Shopping Should Think For You</h2>
      <div style="font-size: 18px; color: #4B5563; line-height: 1.7; display: flex; flex-direction: column; gap: 24px;">
        <p style="margin: 0;">The internet has made products limitless, but decisions exhausting.</p>
        <p style="margin: 0;">Every purchase requires opening dozens of tabs, comparing prices, reading reviews, checking delivery dates, and wondering whether you're making the right decision.</p>
        <p style="margin: 0;">We believe technology should eliminate this cognitive overload.</p>
        <p style="margin: 0;">Nexmart introduces Agentic Commerce, where intelligent AI agents understand what you need, perform the research on your behalf, and recommend the best purchasing decisions in seconds.</p>
        <p style="margin: 0; font-weight: 500; color: #111827;">Instead of searching for products, you simply describe your intent.</p>
      </div>
    </div>

    <!-- SECTION 2: THE PROBLEM -->
    <div>
      <h2 style="font-size: 32px; font-weight: 600; color: #111827; margin-bottom: 48px; letter-spacing: -0.02em; text-align: center;">Commerce Has Become Too Complex</h2>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 24px;">
        <!-- Card 1 -->
        <div style="background: rgba(255,255,255,0.7); backdrop-filter: blur(12px); border: 1px solid rgba(0,0,0,0.08); border-radius: 16px; padding: 32px; box-shadow: 0 4px 12px rgba(0,0,0,0.02);">
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin-bottom: 16px; line-height: 1.3;">Too Many Choices</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Millions of products create more confusion than confidence.</p>
        </div>
        <!-- Card 2 -->
        <div style="background: rgba(255,255,255,0.7); backdrop-filter: blur(12px); border: 1px solid rgba(0,0,0,0.08); border-radius: 16px; padding: 32px; box-shadow: 0 4px 12px rgba(0,0,0,0.02);">
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin-bottom: 16px; line-height: 1.3;">Endless Research</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Hours are spent comparing stores, reviews, prices, and specifications.</p>
        </div>
        <!-- Card 3 -->
        <div style="background: rgba(255,255,255,0.7); backdrop-filter: blur(12px); border: 1px solid rgba(0,0,0,0.08); border-radius: 16px; padding: 32px; box-shadow: 0 4px 12px rgba(0,0,0,0.02);">
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin-bottom: 16px; line-height: 1.3;">Decision Fatigue</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">The more options people have, the harder good decisions become.</p>
        </div>
        <!-- Card 4 -->
        <div style="background: rgba(255,255,255,0.7); backdrop-filter: blur(12px); border: 1px solid rgba(0,0,0,0.08); border-radius: 16px; padding: 32px; box-shadow: 0 4px 12px rgba(0,0,0,0.02);">
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin-bottom: 16px; line-height: 1.3;">Disconnected Shopping</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Products, payments, subscriptions, and logistics all exist in separate systems.</p>
        </div>
      </div>
    </div>

    <!-- SECTION 3: THE SOLUTION -->
    <div style="max-width: 800px; margin: 0 auto; text-align: center;">
      <h2 style="font-size: 36px; font-weight: 600; color: #111827; margin-bottom: 32px; letter-spacing: -0.02em; line-height: 1.2;">Meet Agentic Commerce</h2>
      <div style="font-size: 18px; color: #4B5563; line-height: 1.7; display: flex; flex-direction: column; gap: 24px;">
        <p style="margin: 0; font-weight: 500; color: #111827;">Nexmart replaces manual searching with intelligent decision-making.</p>
        <p style="margin: 0;">Instead of spending hours comparing products, AI Shopping Agents analyze suppliers, pricing, delivery speed, reviews, availability, and value before presenting the best recommendations.</p>
        <p style="margin: 0;">The result is faster purchasing, better decisions, and dramatically less effort.</p>
      </div>
    </div>

    <!-- SECTION 4: THE ECOSYSTEM -->
    <div>
      <div style="text-align: center; margin-bottom: 48px; max-width: 600px; margin-left: auto; margin-right: auto;">
        <h2 style="font-size: 32px; font-weight: 600; color: #111827; margin-bottom: 16px; letter-spacing: -0.02em;">One Intelligent Ecosystem</h2>
        <p style="font-size: 18px; color: #4B5563; line-height: 1.6; margin: 0;">Every Nexmart product works together as part of a unified commerce platform.</p>
      </div>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px;">
        <!-- Item 1 -->
        <div style="background: rgba(255,255,255,0.7); backdrop-filter: blur(12px); border: 1px solid rgba(0,0,0,0.08); border-radius: 16px; padding: 32px; box-shadow: 0 4px 12px rgba(0,0,0,0.02);">
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin-bottom: 12px; line-height: 1.3;">Magic AI Search</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Natural language product discovery.</p>
        </div>
        <!-- Item 2 -->
        <div style="background: rgba(255,255,255,0.7); backdrop-filter: blur(12px); border: 1px solid rgba(0,0,0,0.08); border-radius: 16px; padding: 32px; box-shadow: 0 4px 12px rgba(0,0,0,0.02);">
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin-bottom: 12px; line-height: 1.3;">Agentic Commerce</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Autonomous purchasing powered by AI agents.</p>
        </div>
        <!-- Item 3 -->
        <div style="background: rgba(255,255,255,0.7); backdrop-filter: blur(12px); border: 1px solid rgba(0,0,0,0.08); border-radius: 16px; padding: 32px; box-shadow: 0 4px 12px rgba(0,0,0,0.02);">
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin-bottom: 12px; line-height: 1.3;">Advertiser Tracker</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Competitive advertising intelligence.</p>
        </div>
        <!-- Item 4 -->
        <div style="background: rgba(255,255,255,0.7); backdrop-filter: blur(12px); border: 1px solid rgba(0,0,0,0.08); border-radius: 16px; padding: 32px; box-shadow: 0 4px 12px rgba(0,0,0,0.02);">
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin-bottom: 12px; line-height: 1.3;">Creator Library</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Find high-performing creators.</p>
        </div>
        <!-- Item 5 -->
        <div style="background: rgba(255,255,255,0.7); backdrop-filter: blur(12px); border: 1px solid rgba(0,0,0,0.08); border-radius: 16px; padding: 32px; box-shadow: 0 4px 12px rgba(0,0,0,0.02);">
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin-bottom: 12px; line-height: 1.3;">Sales Tracker</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Monitor products and revenue.</p>
        </div>
        <!-- Item 6 -->
        <div style="background: rgba(255,255,255,0.7); backdrop-filter: blur(12px); border: 1px solid rgba(0,0,0,0.08); border-radius: 16px; padding: 32px; box-shadow: 0 4px 12px rgba(0,0,0,0.02);">
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin-bottom: 12px; line-height: 1.3;">Product Library</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Explore winning products.</p>
        </div>
        <!-- Item 7 -->
        <div style="background: rgba(255,255,255,0.7); backdrop-filter: blur(12px); border: 1px solid rgba(0,0,0,0.08); border-radius: 16px; padding: 32px; box-shadow: 0 4px 12px rgba(0,0,0,0.02);">
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin-bottom: 12px; line-height: 1.3;">Shop Library</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Search stores and marketplaces.</p>
        </div>
        <!-- Item 8 -->
        <div style="background: rgba(255,255,255,0.7); backdrop-filter: blur(12px); border: 1px solid rgba(0,0,0,0.08); border-radius: 16px; padding: 32px; box-shadow: 0 4px 12px rgba(0,0,0,0.02);">
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin-bottom: 12px; line-height: 1.3;">Chrome Extension</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Research products anywhere online.</p>
        </div>
      </div>
    </div>

    <!-- SECTION 5: OUR VALUES -->
    <div>
      <h2 style="font-size: 32px; font-weight: 600; color: #111827; margin-bottom: 48px; letter-spacing: -0.02em; text-align: center;">What Drives Nexmart</h2>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 24px;">
        <!-- Value 1 -->
        <div style="background: rgba(255,255,255,0.7); backdrop-filter: blur(12px); border: 1px solid rgba(0,0,0,0.08); border-radius: 16px; padding: 32px; box-shadow: 0 4px 12px rgba(0,0,0,0.02); text-align: center;">
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin-bottom: 16px; line-height: 1.3;">Innovation</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">We challenge how commerce has always worked.</p>
        </div>
        <!-- Value 2 -->
        <div style="background: rgba(255,255,255,0.7); backdrop-filter: blur(12px); border: 1px solid rgba(0,0,0,0.08); border-radius: 16px; padding: 32px; box-shadow: 0 4px 12px rgba(0,0,0,0.02); text-align: center;">
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin-bottom: 16px; line-height: 1.3;">Trust</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">AI should always help users make informed decisions.</p>
        </div>
        <!-- Value 3 -->
        <div style="background: rgba(255,255,255,0.7); backdrop-filter: blur(12px); border: 1px solid rgba(0,0,0,0.08); border-radius: 16px; padding: 32px; box-shadow: 0 4px 12px rgba(0,0,0,0.02); text-align: center;">
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin-bottom: 16px; line-height: 1.3;">Simplicity</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Technology should remove complexity, not create it.</p>
        </div>
        <!-- Value 4 -->
        <div style="background: rgba(255,255,255,0.7); backdrop-filter: blur(12px); border: 1px solid rgba(0,0,0,0.08); border-radius: 16px; padding: 32px; box-shadow: 0 4px 12px rgba(0,0,0,0.02); text-align: center;">
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin-bottom: 16px; line-height: 1.3;">Global Accessibility</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Commerce should work for everyone, everywhere.</p>
        </div>
      </div>
    </div>

  </div>
</div>
"""

# Replace placeholder section
placeholder = soup.find(string=lambda text: text and 'Content Coming Soon' in text)
if placeholder:
    section_to_replace = placeholder.find_parent('section')
    if section_to_replace:
        new_section = bs4.BeautifulSoup(about_html, 'html.parser')
        section_to_replace.replace_with(new_section)

# Make sure CTA section has white background to match
sections = soup.find_all('section')
if len(sections) > 1:
    cta = sections[-1]
    cta['style'] = cta.get('style', '') + '; background-color: #ffffff;'
    # Darken CTA text if it was white
    for h in cta.find_all(['h2', 'h3']):
        h['style'] = h.get('style', '') + '; color: #111827 !important;'
    for p in cta.find_all('p'):
        p['style'] = p.get('style', '') + '; color: #4B5563 !important;'

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Successfully injected About page content.")
