import bs4

with open('about.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = bs4.BeautifulSoup(html, 'html.parser')

about_html = """
<div class="semantic-about-wrapper" style="background-color: #ffffff; padding-top: 60px; padding-bottom: 160px; width: 100%;">
  <div style="max-width: 1200px; margin: 0 auto; padding: 0 5%; width: 100%; box-sizing: border-box; display: flex; flex-direction: column; gap: 180px;">
    
    <!-- SECTION 1: OUR VISION -->
    <div style="max-width: 680px; margin: 0 auto; text-align: center;">
      <h2 style="font-size: 48px; font-weight: 600; color: #111827; margin-bottom: 40px; letter-spacing: -0.03em; line-height: 1.1;">We Believe Shopping Should Think For You</h2>
      <div style="font-size: 20px; color: #4B5563; line-height: 1.8; display: flex; flex-direction: column; gap: 28px;">
        <p style="margin: 0;">The internet has made products limitless, but decisions exhausting.</p>
        <p style="margin: 0;">Every purchase requires opening dozens of tabs, comparing prices, reading reviews, checking delivery dates, and wondering whether you're making the right decision.</p>
        <p style="margin: 0;">We believe technology should eliminate this cognitive overload.</p>
        <p style="margin: 0;">Nexmart introduces Agentic Commerce, where intelligent AI agents understand what you need, perform the research on your behalf, and recommend the best purchasing decisions in seconds.</p>
        <p style="margin: 0; font-weight: 500; color: #111827; font-size: 22px;">Instead of searching for products, you simply describe your intent.</p>
      </div>
    </div>

    <!-- SECTION 2: THE PROBLEM -->
    <div>
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 64px; letter-spacing: -0.03em; text-align: center; max-width: 800px; margin-left: auto; margin-right: auto;">Commerce Has Become Too Complex</h2>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 32px;">
        <!-- Card 1 -->
        <div style="background: rgba(255,255,255,0.8); backdrop-filter: blur(16px); border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px; box-shadow: 0 8px 32px rgba(0,0,0,0.03); min-height: 280px; display: flex; flex-direction: column;">
          <h3 style="font-size: 24px; font-weight: 600; color: #111827; margin-bottom: 20px; line-height: 1.3; letter-spacing: -0.01em;">Too Many Choices</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.7; margin: 0;">Millions of products create more confusion than confidence.</p>
        </div>
        <!-- Card 2 -->
        <div style="background: rgba(255,255,255,0.8); backdrop-filter: blur(16px); border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px; box-shadow: 0 8px 32px rgba(0,0,0,0.03); min-height: 280px; display: flex; flex-direction: column;">
          <h3 style="font-size: 24px; font-weight: 600; color: #111827; margin-bottom: 20px; line-height: 1.3; letter-spacing: -0.01em;">Endless Research</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.7; margin: 0;">Hours are spent comparing stores, reviews, prices, and specifications.</p>
        </div>
        <!-- Card 3 -->
        <div style="background: rgba(255,255,255,0.8); backdrop-filter: blur(16px); border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px; box-shadow: 0 8px 32px rgba(0,0,0,0.03); min-height: 280px; display: flex; flex-direction: column;">
          <h3 style="font-size: 24px; font-weight: 600; color: #111827; margin-bottom: 20px; line-height: 1.3; letter-spacing: -0.01em;">Decision Fatigue</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.7; margin: 0;">The more options people have, the harder good decisions become.</p>
        </div>
        <!-- Card 4 -->
        <div style="background: rgba(255,255,255,0.8); backdrop-filter: blur(16px); border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px; box-shadow: 0 8px 32px rgba(0,0,0,0.03); min-height: 280px; display: flex; flex-direction: column;">
          <h3 style="font-size: 24px; font-weight: 600; color: #111827; margin-bottom: 20px; line-height: 1.3; letter-spacing: -0.01em;">Disconnected Shopping</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.7; margin: 0;">Products, payments, subscriptions, and logistics all exist in separate systems.</p>
        </div>
      </div>
    </div>

    <!-- SECTION 3: THE SOLUTION -->
    <div style="max-width: 680px; margin: 0 auto; text-align: center;">
      <h2 style="font-size: 48px; font-weight: 600; color: #111827; margin-bottom: 40px; letter-spacing: -0.03em; line-height: 1.1;">Meet Agentic Commerce</h2>
      <div style="font-size: 20px; color: #4B5563; line-height: 1.8; display: flex; flex-direction: column; gap: 28px;">
        <p style="margin: 0; font-weight: 500; color: #111827; font-size: 24px; letter-spacing: -0.01em;">Nexmart replaces manual searching with intelligent decision-making.</p>
        <p style="margin: 0;">Instead of spending hours comparing products, AI Shopping Agents analyze suppliers, pricing, delivery speed, reviews, availability, and value before presenting the best recommendations.</p>
        <p style="margin: 0;">The result is faster purchasing, better decisions, and dramatically less effort.</p>
      </div>
    </div>

    <!-- SECTION 4: THE ECOSYSTEM -->
    <div>
      <div style="text-align: center; margin-bottom: 80px; max-width: 680px; margin-left: auto; margin-right: auto;">
        <h2 style="font-size: 44px; font-weight: 600; color: #111827; margin-bottom: 24px; letter-spacing: -0.03em; line-height: 1.1;">One Intelligent Ecosystem</h2>
        <p style="font-size: 22px; color: #4B5563; line-height: 1.6; margin: 0;">Every Nexmart product works together as part of a unified commerce platform.</p>
      </div>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 32px;">
        <!-- Item 1 -->
        <a href="#" class="ecosystem-card" style="text-decoration: none; background: rgba(255,255,255,0.8); backdrop-filter: blur(16px); border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px; box-shadow: 0 8px 32px rgba(0,0,0,0.03); min-height: 300px; display: flex; flex-direction: column; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);">
          <h3 style="font-size: 26px; font-weight: 600; color: #111827; margin-bottom: 16px; line-height: 1.3; letter-spacing: -0.01em;">Magic AI Search</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.7; margin: 0; flex-grow: 1;">Natural language product discovery.</p>
          <div style="display: flex; align-items: center; color: #2563EB; font-weight: 500; font-size: 16px; margin-top: 24px;">Learn More <span style="margin-left: 8px;">→</span></div>
        </a>
        <!-- Item 2 -->
        <a href="#" class="ecosystem-card" style="text-decoration: none; background: rgba(255,255,255,0.8); backdrop-filter: blur(16px); border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px; box-shadow: 0 8px 32px rgba(0,0,0,0.03); min-height: 300px; display: flex; flex-direction: column; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);">
          <h3 style="font-size: 26px; font-weight: 600; color: #111827; margin-bottom: 16px; line-height: 1.3; letter-spacing: -0.01em;">Agentic Commerce</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.7; margin: 0; flex-grow: 1;">Autonomous purchasing powered by AI agents.</p>
          <div style="display: flex; align-items: center; color: #2563EB; font-weight: 500; font-size: 16px; margin-top: 24px;">Learn More <span style="margin-left: 8px;">→</span></div>
        </a>
        <!-- Item 3 -->
        <a href="#" class="ecosystem-card" style="text-decoration: none; background: rgba(255,255,255,0.8); backdrop-filter: blur(16px); border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px; box-shadow: 0 8px 32px rgba(0,0,0,0.03); min-height: 300px; display: flex; flex-direction: column; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);">
          <h3 style="font-size: 26px; font-weight: 600; color: #111827; margin-bottom: 16px; line-height: 1.3; letter-spacing: -0.01em;">Advertiser Tracker</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.7; margin: 0; flex-grow: 1;">Competitive advertising intelligence.</p>
          <div style="display: flex; align-items: center; color: #2563EB; font-weight: 500; font-size: 16px; margin-top: 24px;">Learn More <span style="margin-left: 8px;">→</span></div>
        </a>
        <!-- Item 4 -->
        <a href="#" class="ecosystem-card" style="text-decoration: none; background: rgba(255,255,255,0.8); backdrop-filter: blur(16px); border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px; box-shadow: 0 8px 32px rgba(0,0,0,0.03); min-height: 300px; display: flex; flex-direction: column; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);">
          <h3 style="font-size: 26px; font-weight: 600; color: #111827; margin-bottom: 16px; line-height: 1.3; letter-spacing: -0.01em;">Creator Library</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.7; margin: 0; flex-grow: 1;">Find high-performing creators.</p>
          <div style="display: flex; align-items: center; color: #2563EB; font-weight: 500; font-size: 16px; margin-top: 24px;">Learn More <span style="margin-left: 8px;">→</span></div>
        </a>
        <!-- Item 5 -->
        <a href="#" class="ecosystem-card" style="text-decoration: none; background: rgba(255,255,255,0.8); backdrop-filter: blur(16px); border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px; box-shadow: 0 8px 32px rgba(0,0,0,0.03); min-height: 300px; display: flex; flex-direction: column; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);">
          <h3 style="font-size: 26px; font-weight: 600; color: #111827; margin-bottom: 16px; line-height: 1.3; letter-spacing: -0.01em;">Sales Tracker</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.7; margin: 0; flex-grow: 1;">Monitor products and revenue.</p>
          <div style="display: flex; align-items: center; color: #2563EB; font-weight: 500; font-size: 16px; margin-top: 24px;">Learn More <span style="margin-left: 8px;">→</span></div>
        </a>
        <!-- Item 6 -->
        <a href="#" class="ecosystem-card" style="text-decoration: none; background: rgba(255,255,255,0.8); backdrop-filter: blur(16px); border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px; box-shadow: 0 8px 32px rgba(0,0,0,0.03); min-height: 300px; display: flex; flex-direction: column; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);">
          <h3 style="font-size: 26px; font-weight: 600; color: #111827; margin-bottom: 16px; line-height: 1.3; letter-spacing: -0.01em;">Product Library</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.7; margin: 0; flex-grow: 1;">Explore winning products.</p>
          <div style="display: flex; align-items: center; color: #2563EB; font-weight: 500; font-size: 16px; margin-top: 24px;">Learn More <span style="margin-left: 8px;">→</span></div>
        </a>
        <!-- Item 7 -->
        <a href="#" class="ecosystem-card" style="text-decoration: none; background: rgba(255,255,255,0.8); backdrop-filter: blur(16px); border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px; box-shadow: 0 8px 32px rgba(0,0,0,0.03); min-height: 300px; display: flex; flex-direction: column; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);">
          <h3 style="font-size: 26px; font-weight: 600; color: #111827; margin-bottom: 16px; line-height: 1.3; letter-spacing: -0.01em;">Shop Library</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.7; margin: 0; flex-grow: 1;">Search stores and marketplaces.</p>
          <div style="display: flex; align-items: center; color: #2563EB; font-weight: 500; font-size: 16px; margin-top: 24px;">Learn More <span style="margin-left: 8px;">→</span></div>
        </a>
        <!-- Item 8 -->
        <a href="#" class="ecosystem-card" style="text-decoration: none; background: rgba(255,255,255,0.8); backdrop-filter: blur(16px); border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px; box-shadow: 0 8px 32px rgba(0,0,0,0.03); min-height: 300px; display: flex; flex-direction: column; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);">
          <h3 style="font-size: 26px; font-weight: 600; color: #111827; margin-bottom: 16px; line-height: 1.3; letter-spacing: -0.01em;">Chrome Extension</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.7; margin: 0; flex-grow: 1;">Research products anywhere online.</p>
          <div style="display: flex; align-items: center; color: #2563EB; font-weight: 500; font-size: 16px; margin-top: 24px;">Learn More <span style="margin-left: 8px;">→</span></div>
        </a>
      </div>
    </div>

    <!-- SECTION 5: OUR VALUES -->
    <div>
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 64px; letter-spacing: -0.03em; text-align: center; max-width: 800px; margin-left: auto; margin-right: auto;">What Drives Nexmart</h2>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 32px;">
        <!-- Value 1 -->
        <div class="value-card" style="background: rgba(255,255,255,0.8); backdrop-filter: blur(16px); border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 56px 48px; box-shadow: 0 8px 32px rgba(0,0,0,0.03); text-align: center; display: flex; flex-direction: column; align-items: center; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);">
          <div style="margin-bottom: 32px; background: rgba(0,0,0,0.03); width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #111827;">
            <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
          </div>
          <h3 style="font-size: 24px; font-weight: 600; color: #111827; margin-bottom: 16px; line-height: 1.3; letter-spacing: -0.01em;">Innovation</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.7; margin: 0;">We challenge how commerce has always worked.</p>
        </div>
        <!-- Value 2 -->
        <div class="value-card" style="background: rgba(255,255,255,0.8); backdrop-filter: blur(16px); border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 56px 48px; box-shadow: 0 8px 32px rgba(0,0,0,0.03); text-align: center; display: flex; flex-direction: column; align-items: center; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);">
          <div style="margin-bottom: 32px; background: rgba(0,0,0,0.03); width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #111827;">
            <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
          </div>
          <h3 style="font-size: 24px; font-weight: 600; color: #111827; margin-bottom: 16px; line-height: 1.3; letter-spacing: -0.01em;">Trust</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.7; margin: 0;">AI should always help users make informed decisions.</p>
        </div>
        <!-- Value 3 -->
        <div class="value-card" style="background: rgba(255,255,255,0.8); backdrop-filter: blur(16px); border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 56px 48px; box-shadow: 0 8px 32px rgba(0,0,0,0.03); text-align: center; display: flex; flex-direction: column; align-items: center; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);">
          <div style="margin-bottom: 32px; background: rgba(0,0,0,0.03); width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #111827;">
            <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>
          </div>
          <h3 style="font-size: 24px; font-weight: 600; color: #111827; margin-bottom: 16px; line-height: 1.3; letter-spacing: -0.01em;">Simplicity</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.7; margin: 0;">Technology should remove complexity, not create it.</p>
        </div>
        <!-- Value 4 -->
        <div class="value-card" style="background: rgba(255,255,255,0.8); backdrop-filter: blur(16px); border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 56px 48px; box-shadow: 0 8px 32px rgba(0,0,0,0.03); text-align: center; display: flex; flex-direction: column; align-items: center; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);">
          <div style="margin-bottom: 32px; background: rgba(0,0,0,0.03); width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #111827;">
            <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
          </div>
          <h3 style="font-size: 24px; font-weight: 600; color: #111827; margin-bottom: 16px; line-height: 1.3; letter-spacing: -0.01em;">Global Accessibility</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.7; margin: 0;">Commerce should work for everyone, everywhere.</p>
        </div>
      </div>
    </div>

  </div>
  
  <style>
    .ecosystem-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.08) !important;
        border-color: rgba(0,0,0,0.1) !important;
        background: rgba(255,255,255,0.95) !important;
    }
    .value-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.06) !important;
    }
  </style>
</div>
"""

wrapper = soup.find('div', class_='semantic-about-wrapper')
if wrapper:
    wrapper.replace_with(bs4.BeautifulSoup(about_html, 'html.parser'))
    with open('about.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print("Successfully replaced semantic wrapper.")
else:
    print("Error: Could not find semantic wrapper.")
