import bs4

with open('about.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = bs4.BeautifulSoup(html, 'html.parser')

about_html = """
<div class="semantic-about-wrapper" style="width: 100%; display: flex; flex-direction: column;">
  
  <!-- SECTION 1: OUR VISION (White Background) -->
  <section style="background-color: #ffffff; padding: 180px 5%; width: 100%; box-sizing: border-box; position: relative; overflow: hidden;">
    <!-- Background subtle graphic -->
    <svg width="800" height="800" viewBox="0 0 800 800" style="position: absolute; right: -200px; top: -100px; opacity: 0.03; pointer-events: none;"><circle cx="400" cy="400" r="380" fill="none" stroke="#000" stroke-width="40"/><circle cx="400" cy="400" r="280" fill="none" stroke="#000" stroke-width="40"/></svg>
    
    <div style="max-width: 1400px; margin: 0 auto; display: flex; flex-direction: column; align-items: center; text-align: center; position: relative; z-index: 2;">
      <h2 style="font-size: 56px; font-weight: 600; color: #111827; margin-bottom: 56px; letter-spacing: -0.04em; line-height: 1.1; max-width: 800px;">We Believe Shopping Should Think For You</h2>
      
      <div style="font-size: 24px; color: #4B5563; line-height: 1.7; max-width: 720px; display: flex; flex-direction: column; gap: 40px;">
        <p style="margin: 0; font-weight: 400;">The internet has made products limitless, but decisions exhausting.</p>
        <p style="margin: 0; font-weight: 400;">Every purchase requires opening dozens of tabs, comparing prices, reading reviews, checking delivery dates, and wondering whether you're making the right decision.</p>
        <p style="margin: 0; font-weight: 400;">We believe technology should eliminate this cognitive overload.</p>
        <p style="margin: 0; font-weight: 400;">Nexmart introduces Agentic Commerce, where intelligent AI agents understand what you need, perform the research on your behalf, and recommend the best purchasing decisions in seconds.</p>
        <p style="margin: 0; font-weight: 500; color: #111827; font-size: 28px; letter-spacing: -0.02em; padding-top: 24px;">Instead of searching for products, you simply describe your intent.</p>
      </div>
    </div>
  </section>

  <!-- SECTION 2: THE PROBLEM (Light Gray Background) -->
  <section style="background-color: #f8fafc; padding: 180px 5%; width: 100%; box-sizing: border-box; border-top: 1px solid rgba(0,0,0,0.03); border-bottom: 1px solid rgba(0,0,0,0.03);">
    <div style="max-width: 1400px; margin: 0 auto;">
      <div style="text-align: center; margin-bottom: 80px;">
        <h2 style="font-size: 48px; font-weight: 600; color: #111827; letter-spacing: -0.03em;">Commerce Has Become Too Complex</h2>
      </div>
      
      <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 40px; max-width: 1200px; margin: 0 auto;">
        <!-- Card 1 -->
        <div style="background: #ffffff; border: 1px solid rgba(0,0,0,0.05); border-radius: 32px; padding: 64px; box-shadow: 0 12px 48px rgba(0,0,0,0.03); display: flex; flex-direction: column;">
          <h3 style="font-size: 32px; font-weight: 600; color: #111827; margin-bottom: 24px; line-height: 1.2; letter-spacing: -0.02em;">Too Many Choices</h3>
          <p style="font-size: 20px; color: #4B5563; line-height: 1.7; margin: 0;">Millions of products create more confusion than confidence. The paradox of choice paralyzes buyers instead of empowering them.</p>
        </div>
        <!-- Card 2 -->
        <div style="background: #ffffff; border: 1px solid rgba(0,0,0,0.05); border-radius: 32px; padding: 64px; box-shadow: 0 12px 48px rgba(0,0,0,0.03); display: flex; flex-direction: column;">
          <h3 style="font-size: 32px; font-weight: 600; color: #111827; margin-bottom: 24px; line-height: 1.2; letter-spacing: -0.02em;">Endless Research</h3>
          <p style="font-size: 20px; color: #4B5563; line-height: 1.7; margin: 0;">Hours are spent comparing stores, reviews, prices, and specifications across fragmented platforms that refuse to speak to each other.</p>
        </div>
        <!-- Card 3 -->
        <div style="background: #ffffff; border: 1px solid rgba(0,0,0,0.05); border-radius: 32px; padding: 64px; box-shadow: 0 12px 48px rgba(0,0,0,0.03); display: flex; flex-direction: column;">
          <h3 style="font-size: 32px; font-weight: 600; color: #111827; margin-bottom: 24px; line-height: 1.2; letter-spacing: -0.02em;">Decision Fatigue</h3>
          <p style="font-size: 20px; color: #4B5563; line-height: 1.7; margin: 0;">The more options people have, the harder good decisions become. Anxiety replaces excitement when making high-value purchases.</p>
        </div>
        <!-- Card 4 -->
        <div style="background: #ffffff; border: 1px solid rgba(0,0,0,0.05); border-radius: 32px; padding: 64px; box-shadow: 0 12px 48px rgba(0,0,0,0.03); display: flex; flex-direction: column;">
          <h3 style="font-size: 32px; font-weight: 600; color: #111827; margin-bottom: 24px; line-height: 1.2; letter-spacing: -0.02em;">Disconnected Shopping</h3>
          <p style="font-size: 20px; color: #4B5563; line-height: 1.7; margin: 0;">Products, payments, subscriptions, and logistics all exist in separate, siloed systems that break the continuous flow of commerce.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 3: THE SOLUTION (White Background) -->
  <section style="background-color: #ffffff; padding: 200px 5%; width: 100%; box-sizing: border-box;">
    <div style="max-width: 1400px; margin: 0 auto; display: flex; flex-direction: column; align-items: center; text-align: center;">
      <h2 style="font-size: 56px; font-weight: 600; color: #111827; margin-bottom: 56px; letter-spacing: -0.04em; line-height: 1.1;">Meet Agentic Commerce</h2>
      <div style="font-size: 24px; color: #4B5563; line-height: 1.8; max-width: 760px; display: flex; flex-direction: column; gap: 40px;">
        <p style="margin: 0; font-weight: 500; color: #111827; font-size: 32px; letter-spacing: -0.02em; line-height: 1.3;">Nexmart replaces manual searching with intelligent decision-making.</p>
        <p style="margin: 0;">Instead of spending hours comparing products, AI Shopping Agents analyze suppliers, pricing, delivery speed, reviews, availability, and value before presenting the best recommendations.</p>
        <p style="margin: 0;">The result is faster purchasing, better decisions, and dramatically less effort.</p>
      </div>
    </div>
  </section>

  <!-- SECTION 4: THE ECOSYSTEM (Light Blue Tint Background) -->
  <section style="background-color: #f0f9ff; padding: 180px 5%; width: 100%; box-sizing: border-box; position: relative; overflow: hidden; border-top: 1px solid rgba(0,0,0,0.03);">
    <!-- Abstract AI Graphic -->
    <svg width="600" height="600" viewBox="0 0 24 24" fill="none" stroke="#2563EB" stroke-width="0.5" style="position: absolute; left: -100px; top: -100px; opacity: 0.05; pointer-events: none;"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="3.29 7 12 12 20.71 7"/><line x1="12" y1="22" x2="12" y2="12"/></svg>
    
    <div style="max-width: 1400px; margin: 0 auto; position: relative; z-index: 2;">
      <div style="text-align: center; margin-bottom: 100px; max-width: 800px; margin-left: auto; margin-right: auto;">
        <h2 style="font-size: 56px; font-weight: 600; color: #111827; margin-bottom: 32px; letter-spacing: -0.04em; line-height: 1.1;">One Intelligent Ecosystem</h2>
        <p style="font-size: 24px; color: #3b82f6; line-height: 1.6; margin: 0; font-weight: 500;">Every Nexmart product works together as part of a unified commerce platform.</p>
      </div>
      
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 32px;">
        <!-- Item 1 -->
        <a href="#" class="ecosystem-premium-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 32px; padding: 56px; box-shadow: 0 12px 32px rgba(37,99,235,0.04); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); min-height: 360px;">
          <div style="background: #f0f9ff; width: 64px; height: 64px; border-radius: 20px; display: flex; align-items: center; justify-content: center; margin-bottom: 32px; color: #2563EB;">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>
          </div>
          <h3 style="font-size: 28px; font-weight: 600; color: #111827; margin-bottom: 16px; line-height: 1.2; letter-spacing: -0.02em;">Magic AI Search</h3>
          <p style="font-size: 18px; color: #64748b; line-height: 1.7; margin: 0; flex-grow: 1;">Natural language product discovery powered by deep reasoning models.</p>
          <div class="card-link" style="display: flex; align-items: center; color: #2563EB; font-weight: 600; font-size: 18px; margin-top: 32px; transition: transform 0.3s ease;">Learn More <span style="margin-left: 8px;">→</span></div>
        </a>
        <!-- Item 2 -->
        <a href="#" class="ecosystem-premium-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 32px; padding: 56px; box-shadow: 0 12px 32px rgba(37,99,235,0.04); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); min-height: 360px;">
          <div style="background: #f0f9ff; width: 64px; height: 64px; border-radius: 20px; display: flex; align-items: center; justify-content: center; margin-bottom: 32px; color: #2563EB;">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m12 14 4-4"/><path d="M3.34 19a10 10 0 1 1 17.32 0"/></svg>
          </div>
          <h3 style="font-size: 28px; font-weight: 600; color: #111827; margin-bottom: 16px; line-height: 1.2; letter-spacing: -0.02em;">Agentic Commerce</h3>
          <p style="font-size: 18px; color: #64748b; line-height: 1.7; margin: 0; flex-grow: 1;">Autonomous purchasing powered by our proprietary AI agents.</p>
          <div class="card-link" style="display: flex; align-items: center; color: #2563EB; font-weight: 600; font-size: 18px; margin-top: 32px; transition: transform 0.3s ease;">Learn More <span style="margin-left: 8px;">→</span></div>
        </a>
        <!-- Item 3 -->
        <a href="#" class="ecosystem-premium-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 32px; padding: 56px; box-shadow: 0 12px 32px rgba(37,99,235,0.04); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); min-height: 360px;">
          <div style="background: #f0f9ff; width: 64px; height: 64px; border-radius: 20px; display: flex; align-items: center; justify-content: center; margin-bottom: 32px; color: #2563EB;">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3v18h18"/><path d="m19 9-5 5-4-4-3 3"/></svg>
          </div>
          <h3 style="font-size: 28px; font-weight: 600; color: #111827; margin-bottom: 16px; line-height: 1.2; letter-spacing: -0.02em;">Advertiser Tracker</h3>
          <p style="font-size: 18px; color: #64748b; line-height: 1.7; margin: 0; flex-grow: 1;">Competitive advertising intelligence for modern businesses.</p>
          <div class="card-link" style="display: flex; align-items: center; color: #2563EB; font-weight: 600; font-size: 18px; margin-top: 32px; transition: transform 0.3s ease;">Learn More <span style="margin-left: 8px;">→</span></div>
        </a>
        <!-- Item 4 -->
        <a href="#" class="ecosystem-premium-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 32px; padding: 56px; box-shadow: 0 12px 32px rgba(37,99,235,0.04); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); min-height: 360px;">
          <div style="background: #f0f9ff; width: 64px; height: 64px; border-radius: 20px; display: flex; align-items: center; justify-content: center; margin-bottom: 32px; color: #2563EB;">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
          </div>
          <h3 style="font-size: 28px; font-weight: 600; color: #111827; margin-bottom: 16px; line-height: 1.2; letter-spacing: -0.02em;">Creator Library</h3>
          <p style="font-size: 18px; color: #64748b; line-height: 1.7; margin: 0; flex-grow: 1;">Find high-performing creators for scalable partnerships.</p>
          <div class="card-link" style="display: flex; align-items: center; color: #2563EB; font-weight: 600; font-size: 18px; margin-top: 32px; transition: transform 0.3s ease;">Learn More <span style="margin-left: 8px;">→</span></div>
        </a>
        <!-- Item 5 -->
        <a href="#" class="ecosystem-premium-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 32px; padding: 56px; box-shadow: 0 12px 32px rgba(37,99,235,0.04); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); min-height: 360px;">
          <div style="background: #f0f9ff; width: 64px; height: 64px; border-radius: 20px; display: flex; align-items: center; justify-content: center; margin-bottom: 32px; color: #2563EB;">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
          </div>
          <h3 style="font-size: 28px; font-weight: 600; color: #111827; margin-bottom: 16px; line-height: 1.2; letter-spacing: -0.02em;">Sales Tracker</h3>
          <p style="font-size: 18px; color: #64748b; line-height: 1.7; margin: 0; flex-grow: 1;">Monitor products, revenue, and market velocity globally.</p>
          <div class="card-link" style="display: flex; align-items: center; color: #2563EB; font-weight: 600; font-size: 18px; margin-top: 32px; transition: transform 0.3s ease;">Learn More <span style="margin-left: 8px;">→</span></div>
        </a>
        <!-- Item 6 -->
        <a href="#" class="ecosystem-premium-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 32px; padding: 56px; box-shadow: 0 12px 32px rgba(37,99,235,0.04); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); min-height: 360px;">
          <div style="background: #f0f9ff; width: 64px; height: 64px; border-radius: 20px; display: flex; align-items: center; justify-content: center; margin-bottom: 32px; color: #2563EB;">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="7.5 4.21 12 6.81 16.5 4.21"/><polyline points="7.5 19.79 12 17.19 16.5 19.79"/><polyline points="3.29 7 12 12 20.71 7"/><line x1="12" y1="22" x2="12" y2="12"/></svg>
          </div>
          <h3 style="font-size: 28px; font-weight: 600; color: #111827; margin-bottom: 16px; line-height: 1.2; letter-spacing: -0.02em;">Product Library</h3>
          <p style="font-size: 18px; color: #64748b; line-height: 1.7; margin: 0; flex-grow: 1;">Explore winning products across global marketplaces.</p>
          <div class="card-link" style="display: flex; align-items: center; color: #2563EB; font-weight: 600; font-size: 18px; margin-top: 32px; transition: transform 0.3s ease;">Learn More <span style="margin-left: 8px;">→</span></div>
        </a>
        <!-- Item 7 -->
        <a href="#" class="ecosystem-premium-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 32px; padding: 56px; box-shadow: 0 12px 32px rgba(37,99,235,0.04); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); min-height: 360px;">
          <div style="background: #f0f9ff; width: 64px; height: 64px; border-radius: 20px; display: flex; align-items: center; justify-content: center; margin-bottom: 32px; color: #2563EB;">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9h18v10a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V9Z"/><path d="m3 9 2.45-4.9A2 2 0 0 1 7.24 3h9.52a2 2 0 0 1 1.8 1.1L21 9"/><path d="M12 3v6"/></svg>
          </div>
          <h3 style="font-size: 28px; font-weight: 600; color: #111827; margin-bottom: 16px; line-height: 1.2; letter-spacing: -0.02em;">Shop Library</h3>
          <p style="font-size: 18px; color: #64748b; line-height: 1.7; margin: 0; flex-grow: 1;">Search stores and analyze supplier reliability directly.</p>
          <div class="card-link" style="display: flex; align-items: center; color: #2563EB; font-weight: 600; font-size: 18px; margin-top: 32px; transition: transform 0.3s ease;">Learn More <span style="margin-left: 8px;">→</span></div>
        </a>
        <!-- Item 8 -->
        <a href="#" class="ecosystem-premium-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 32px; padding: 56px; box-shadow: 0 12px 32px rgba(37,99,235,0.04); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); min-height: 360px;">
          <div style="background: #f0f9ff; width: 64px; height: 64px; border-radius: 20px; display: flex; align-items: center; justify-content: center; margin-bottom: 32px; color: #2563EB;">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="3" rx="2" ry="2"/><line x1="3" x2="21" y1="9" y2="9"/><line x1="9" x2="9" y1="21" y2="9"/></svg>
          </div>
          <h3 style="font-size: 28px; font-weight: 600; color: #111827; margin-bottom: 16px; line-height: 1.2; letter-spacing: -0.02em;">Chrome Extension</h3>
          <p style="font-size: 18px; color: #64748b; line-height: 1.7; margin: 0; flex-grow: 1;">Research products and compare prices anywhere online.</p>
          <div class="card-link" style="display: flex; align-items: center; color: #2563EB; font-weight: 600; font-size: 18px; margin-top: 32px; transition: transform 0.3s ease;">Learn More <span style="margin-left: 8px;">→</span></div>
        </a>
      </div>
    </div>
  </section>

  <!-- SECTION 5: OUR VALUES (White Background) -->
  <section style="background-color: #ffffff; padding: 180px 5% 240px 5%; width: 100%; box-sizing: border-box;">
    <div style="max-width: 1400px; margin: 0 auto;">
      <h2 style="font-size: 48px; font-weight: 600; color: #111827; margin-bottom: 80px; letter-spacing: -0.03em; text-align: center;">What Drives Nexmart</h2>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 40px;">
        <!-- Value 1 -->
        <div class="value-card" style="border: 1px solid rgba(0,0,0,0.06); border-radius: 32px; padding: 64px 48px; box-shadow: 0 12px 32px rgba(0,0,0,0.02); text-align: center; display: flex; flex-direction: column; align-items: center; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="margin-bottom: 40px; background: #f8fafc; width: 96px; height: 96px; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #111827; border: 1px solid rgba(0,0,0,0.03);">
            <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
          </div>
          <h3 style="font-size: 28px; font-weight: 600; color: #111827; margin-bottom: 20px; line-height: 1.3; letter-spacing: -0.01em;">Innovation</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.8; margin: 0;">We challenge how commerce has always worked.</p>
        </div>
        <!-- Value 2 -->
        <div class="value-card" style="border: 1px solid rgba(0,0,0,0.06); border-radius: 32px; padding: 64px 48px; box-shadow: 0 12px 32px rgba(0,0,0,0.02); text-align: center; display: flex; flex-direction: column; align-items: center; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="margin-bottom: 40px; background: #f8fafc; width: 96px; height: 96px; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #111827; border: 1px solid rgba(0,0,0,0.03);">
            <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
          </div>
          <h3 style="font-size: 28px; font-weight: 600; color: #111827; margin-bottom: 20px; line-height: 1.3; letter-spacing: -0.01em;">Trust</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.8; margin: 0;">AI should always help users make informed decisions.</p>
        </div>
        <!-- Value 3 -->
        <div class="value-card" style="border: 1px solid rgba(0,0,0,0.06); border-radius: 32px; padding: 64px 48px; box-shadow: 0 12px 32px rgba(0,0,0,0.02); text-align: center; display: flex; flex-direction: column; align-items: center; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="margin-bottom: 40px; background: #f8fafc; width: 96px; height: 96px; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #111827; border: 1px solid rgba(0,0,0,0.03);">
            <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>
          </div>
          <h3 style="font-size: 28px; font-weight: 600; color: #111827; margin-bottom: 20px; line-height: 1.3; letter-spacing: -0.01em;">Simplicity</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.8; margin: 0;">Technology should remove complexity, not create it.</p>
        </div>
        <!-- Value 4 -->
        <div class="value-card" style="border: 1px solid rgba(0,0,0,0.06); border-radius: 32px; padding: 64px 48px; box-shadow: 0 12px 32px rgba(0,0,0,0.02); text-align: center; display: flex; flex-direction: column; align-items: center; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="margin-bottom: 40px; background: #f8fafc; width: 96px; height: 96px; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #111827; border: 1px solid rgba(0,0,0,0.03);">
            <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
          </div>
          <h3 style="font-size: 28px; font-weight: 600; color: #111827; margin-bottom: 20px; line-height: 1.3; letter-spacing: -0.01em;">Global Accessibility</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.8; margin: 0;">Commerce should work for everyone, everywhere.</p>
        </div>
      </div>
    </div>
  </section>

  <style>
    .ecosystem-premium-card:hover {
        transform: translateY(-12px);
        box-shadow: 0 24px 48px rgba(37,99,235,0.08) !important;
        border-color: rgba(37,99,235,0.2) !important;
    }
    .ecosystem-premium-card:hover .card-link {
        transform: translateX(8px);
    }
    .value-card:hover {
        transform: translateY(-12px);
        box-shadow: 0 24px 48px rgba(0,0,0,0.06) !important;
        border-color: rgba(0,0,0,0.1) !important;
    }
    @media (max-width: 900px) {
        .semantic-about-wrapper section {
            padding: 100px 5% !important;
        }
        .semantic-about-wrapper h2 {
            font-size: 40px !important;
        }
    }
    @media (max-width: 600px) {
        .semantic-about-wrapper section {
            padding: 80px 5% !important;
        }
        .semantic-about-wrapper h2 {
            font-size: 32px !important;
        }
        .semantic-about-wrapper .ecosystem-premium-card {
            padding: 32px !important;
        }
    }
  </style>
</div>
"""

wrapper = soup.find('div', class_='semantic-about-wrapper')
if wrapper:
    wrapper.replace_with(bs4.BeautifulSoup(about_html, 'html.parser'))
    with open('about.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print("Successfully injected V2 layout.")
else:
    print("Error: Could not find semantic wrapper.")
