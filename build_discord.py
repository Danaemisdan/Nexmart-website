import bs4

with open('discord-community.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = bs4.BeautifulSoup(html, 'html.parser')

# 1. Update Title
if soup.title:
    soup.title.string = "Nexmart - Discord Community"

# 2. Update Hero
hero = soup.find('section', class_=lambda c: c and 'is-hero' in c)
if hero:
    hero['style'] = hero.get('style', '') + '; background-color: #ffffff; color: #111827;'
    h1 = hero.find('h1')
    if h1:
        h1.string = "Join The Nexmart Community"
        h1['style'] = h1.get('style', '') + '; color: #111827 !important;'
    p = hero.find('p')
    if p:
        p.string = "Connect with builders, sellers, creators, and early adopters shaping the future of Agentic Commerce together."
        p['style'] = p.get('style', '') + '; color: #4B5563 !important;'

# 3. Build Discord Community Content HTML
discord_html = """
<div class="semantic-discord-wrapper" style="width: 100%; display: flex; flex-direction: column;">
  
  <!-- SECTION 1: WHY JOIN (White Background) -->
  <section style="background-color: #ffffff; padding: 80px 5% 180px 5%; width: 100%; box-sizing: border-box;">
    <div style="max-width: 1400px; margin: 0 auto; text-align: center;">
      <h2 style="font-size: 44px; font-weight: 600; color: #111827; margin-bottom: 24px; letter-spacing: -0.03em;">More Than A Community</h2>
      <p style="font-size: 20px; color: #4B5563; line-height: 1.7; margin: 0 auto 80px auto; max-width: 680px;">The Nexmart Community is where ideas become products, feedback shapes features, and members gain early access to the future of commerce.</p>
      
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 32px; text-align: left;">
        <!-- Card 1 -->
        <div class="feature-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px; box-shadow: 0 12px 32px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="background: rgba(37,99,235,0.05); width: 64px; height: 64px; border-radius: 20px; display: flex; align-items: center; justify-content: center; margin-bottom: 32px; color: #2563EB;">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
          </div>
          <h3 style="font-size: 24px; font-weight: 600; color: #111827; margin-bottom: 12px; line-height: 1.3; letter-spacing: -0.01em;">Early Access</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.7; margin: 0;">Get first access to new AI tools before public release.</p>
        </div>
        <!-- Card 2 -->
        <div class="feature-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px; box-shadow: 0 12px 32px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="background: rgba(37,99,235,0.05); width: 64px; height: 64px; border-radius: 20px; display: flex; align-items: center; justify-content: center; margin-bottom: 32px; color: #2563EB;">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
          </div>
          <h3 style="font-size: 24px; font-weight: 600; color: #111827; margin-bottom: 12px; line-height: 1.3; letter-spacing: -0.01em;">Direct Product Team</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.7; margin: 0;">Share feedback directly with the people building Nexmart.</p>
        </div>
        <!-- Card 3 -->
        <div class="feature-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px; box-shadow: 0 12px 32px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="background: rgba(37,99,235,0.05); width: 64px; height: 64px; border-radius: 20px; display: flex; align-items: center; justify-content: center; margin-bottom: 32px; color: #2563EB;">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>
          </div>
          <h3 style="font-size: 24px; font-weight: 600; color: #111827; margin-bottom: 12px; line-height: 1.3; letter-spacing: -0.01em;">Learn Together</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.7; margin: 0;">Exchange workflows, prompts, and best practices with other members.</p>
        </div>
        <!-- Card 4 -->
        <div class="feature-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px; box-shadow: 0 12px 32px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="background: rgba(37,99,235,0.05); width: 64px; height: 64px; border-radius: 20px; display: flex; align-items: center; justify-content: center; margin-bottom: 32px; color: #2563EB;">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="m22 2-7 20-4-9-9-4Z"/><path d="M22 2 11 13"/></svg>
          </div>
          <h3 style="font-size: 24px; font-weight: 600; color: #111827; margin-bottom: 12px; line-height: 1.3; letter-spacing: -0.01em;">Exclusive Announcements</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.7; margin: 0;">Receive product launches, roadmap updates, and community events before anyone else.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 2: COMMUNITY CHANNELS (Light Gray Background) -->
  <section style="background-color: #f8fafc; padding: 180px 5%; width: 100%; box-sizing: border-box; border-top: 1px solid rgba(0,0,0,0.03); border-bottom: 1px solid rgba(0,0,0,0.03);">
    <div style="max-width: 1400px; margin: 0 auto;">
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 64px; letter-spacing: -0.03em; text-align: center;">Inside The Server</h2>
      
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 32px;">
        <!-- Card 1 -->
        <div class="channel-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 20px; padding: 40px; box-shadow: 0 8px 24px rgba(0,0,0,0.02); display: flex; align-items: flex-start; gap: 20px; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);">
          <div style="color: #2563EB; margin-top: 4px;"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/></svg></div>
          <div>
            <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 8px;">Announcements</h3>
            <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Official product updates and release notes.</p>
          </div>
        </div>
        <!-- Card 2 -->
        <div class="channel-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 20px; padding: 40px; box-shadow: 0 8px 24px rgba(0,0,0,0.02); display: flex; align-items: flex-start; gap: 20px; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);">
          <div style="color: #2563EB; margin-top: 4px;"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m2 9 3-3 3 3"/><path d="M13 18H7a2 2 0 0 1-2-2V6"/><path d="m22 15-3 3-3-3"/><path d="M11 6h6a2 2 0 0 1 2 2v10"/></svg></div>
          <div>
            <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 8px;">AI Prompts</h3>
            <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Discover and share effective shopping and automation prompts.</p>
          </div>
        </div>
        <!-- Card 3 -->
        <div class="channel-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 20px; padding: 40px; box-shadow: 0 8px 24px rgba(0,0,0,0.02); display: flex; align-items: flex-start; gap: 20px; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);">
          <div style="color: #2563EB; margin-top: 4px;"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg></div>
          <div>
            <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 8px;">Feature Requests</h3>
            <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Help shape Nexmart by proposing new ideas.</p>
          </div>
        </div>
        <!-- Card 4 -->
        <div class="channel-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 20px; padding: 40px; box-shadow: 0 8px 24px rgba(0,0,0,0.02); display: flex; align-items: flex-start; gap: 20px; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);">
          <div style="color: #2563EB; margin-top: 4px;"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg></div>
          <div>
            <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 8px;">Seller Strategies</h3>
            <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Learn from successful sellers and business operators.</p>
          </div>
        </div>
        <!-- Card 5 -->
        <div class="channel-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 20px; padding: 40px; box-shadow: 0 8px 24px rgba(0,0,0,0.02); display: flex; align-items: flex-start; gap: 20px; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);">
          <div style="color: #2563EB; margin-top: 4px;"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg></div>
          <div>
            <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 8px;">Community Support</h3>
            <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Get help from members and moderators.</p>
          </div>
        </div>
        <!-- Card 6 -->
        <div class="channel-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 20px; padding: 40px; box-shadow: 0 8px 24px rgba(0,0,0,0.02); display: flex; align-items: flex-start; gap: 20px; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);">
          <div style="color: #2563EB; margin-top: 4px;"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg></div>
          <div>
            <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 8px;">Events & Workshops</h3>
            <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Live sessions, AMAs, tutorials, and product demonstrations.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 3: WHO SHOULD JOIN (White Background) -->
  <section style="background-color: #ffffff; padding: 180px 5%; width: 100%; box-sizing: border-box;">
    <div style="max-width: 1400px; margin: 0 auto;">
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 64px; letter-spacing: -0.03em; text-align: center;">Built For Everyone Building The Future</h2>
      
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 24px;">
        <!-- Card 1 -->
        <div class="who-card" style="background: #f8fafc; border: 1px solid rgba(0,0,0,0.04); border-radius: 24px; padding: 40px; transition: all 0.3s ease; text-align: center; display: flex; flex-direction: column; align-items: center;">
          <div style="color: #2563EB; margin-bottom: 20px;"><svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg></div>
          <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 12px;">Shoppers</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Discover smarter ways to shop with AI.</p>
        </div>
        <!-- Card 2 -->
        <div class="who-card" style="background: #f8fafc; border: 1px solid rgba(0,0,0,0.04); border-radius: 24px; padding: 40px; transition: all 0.3s ease; text-align: center; display: flex; flex-direction: column; align-items: center;">
          <div style="color: #2563EB; margin-bottom: 20px;"><svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg></div>
          <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 12px;">Sellers</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Grow your business using Agentic Commerce.</p>
        </div>
        <!-- Card 3 -->
        <div class="who-card" style="background: #f8fafc; border: 1px solid rgba(0,0,0,0.04); border-radius: 24px; padding: 40px; transition: all 0.3s ease; text-align: center; display: flex; flex-direction: column; align-items: center;">
          <div style="color: #2563EB; margin-bottom: 20px;"><svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg></div>
          <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 12px;">Developers</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Explore the future of AI-powered commerce.</p>
        </div>
        <!-- Card 4 -->
        <div class="who-card" style="background: #f8fafc; border: 1px solid rgba(0,0,0,0.04); border-radius: 24px; padding: 40px; transition: all 0.3s ease; text-align: center; display: flex; flex-direction: column; align-items: center;">
          <div style="color: #2563EB; margin-bottom: 20px;"><svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="m21.64 3.68-1.25-1.25a1.78 1.78 0 0 0-2.5 0l-9.35 9.35a1.76 1.76 0 0 0-.46 1l-.54 3.16a1.76 1.76 0 0 0 2.05 2.05l3.16-.54a1.76 1.76 0 0 0 1-.46l9.35-9.35a1.78 1.78 0 0 0 0-2.5M10.15 10.15l3.7 3.7"/><path d="m20.24 6.46-3.7-3.7"/></svg></div>
          <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 12px;">Creators</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Learn how AI can help build your audience and business.</p>
        </div>
        <!-- Card 5 -->
        <div class="who-card" style="background: #f8fafc; border: 1px solid rgba(0,0,0,0.04); border-radius: 24px; padding: 40px; transition: all 0.3s ease; text-align: center; display: flex; flex-direction: column; align-items: center;">
          <div style="color: #2563EB; margin-bottom: 20px;"><svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect width="16" height="20" x="4" y="2" rx="2" ry="2"/><path d="M9 22v-4h6v4"/><path d="M8 6h.01"/><path d="M16 6h.01"/><path d="M12 6h.01"/><path d="M12 10h.01"/><path d="M12 14h.01"/><path d="M16 10h.01"/><path d="M16 14h.01"/><path d="M8 10h.01"/><path d="M8 14h.01"/></svg></div>
          <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 12px;">Enterprise Teams</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Connect with Nexmart to transform commerce at scale.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 4: COMMUNITY STATS (Light Gray Background) -->
  <section style="background-color: #f8fafc; padding: 180px 5%; width: 100%; box-sizing: border-box; border-top: 1px solid rgba(0,0,0,0.03); border-bottom: 1px solid rgba(0,0,0,0.03);">
    <div style="max-width: 1400px; margin: 0 auto; text-align: center;">
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 80px; letter-spacing: -0.03em;">Growing Every Day</h2>
      
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 32px;">
        <!-- Stat 1 -->
        <div class="stat-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.05); border-radius: 24px; padding: 48px 32px; box-shadow: 0 8px 32px rgba(0,0,0,0.02); transition: all 0.3s ease;">
          <div style="font-size: 56px; font-weight: 700; color: #2563EB; margin-bottom: 16px; letter-spacing: -0.02em;">15,000+</div>
          <div style="font-size: 18px; font-weight: 600; color: #111827;">Growing Global Community</div>
        </div>
        <!-- Stat 2 -->
        <div class="stat-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.05); border-radius: 24px; padding: 48px 32px; box-shadow: 0 8px 32px rgba(0,0,0,0.02); transition: all 0.3s ease;">
          <div style="font-size: 56px; font-weight: 700; color: #2563EB; margin-bottom: 16px; letter-spacing: -0.02em;">40,000+</div>
          <div style="font-size: 18px; font-weight: 600; color: #111827;">Product Discussions</div>
        </div>
        <!-- Stat 3 -->
        <div class="stat-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.05); border-radius: 24px; padding: 48px 32px; box-shadow: 0 8px 32px rgba(0,0,0,0.02); transition: all 0.3s ease;">
          <div style="font-size: 56px; font-weight: 700; color: #2563EB; margin-bottom: 16px; letter-spacing: -0.02em;">Weekly</div>
          <div style="font-size: 18px; font-weight: 600; color: #111827;">Events & AMAs</div>
        </div>
        <!-- Stat 4 -->
        <div class="stat-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.05); border-radius: 24px; padding: 48px 32px; box-shadow: 0 8px 32px rgba(0,0,0,0.02); transition: all 0.3s ease;">
          <div style="font-size: 56px; font-weight: 700; color: #2563EB; margin-bottom: 16px; letter-spacing: -0.02em;">200+</div>
          <div style="font-size: 18px; font-weight: 600; color: #111827;">Feature Requests Implemented</div>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 5: FINAL CTA (White Background) -->
  <section style="background-color: #ffffff; padding: 180px 5% 240px 5%; width: 100%; box-sizing: border-box;">
    <div style="max-width: 1000px; margin: 0 auto; text-align: center;">
      <h2 style="font-size: 48px; font-weight: 600; color: #111827; margin-bottom: 24px; letter-spacing: -0.03em;">Become Part Of The Future</h2>
      <p style="font-size: 22px; color: #4B5563; line-height: 1.7; margin: 0 0 16px 0;">The next generation of commerce won't be built by one company.</p>
      <p style="font-size: 22px; color: #4B5563; line-height: 1.7; margin: 0 0 48px 0;">It will be built by an ecosystem of innovators, businesses, creators, and shoppers working together.</p>
      
      <div style="display: flex; gap: 16px; justify-content: center; flex-wrap: wrap;">
        <a href="#" class="btn-primary" style="text-decoration: none; background: #2563EB; color: #ffffff; padding: 18px 40px; border-radius: 100px; font-size: 18px; font-weight: 600; transition: all 0.3s ease; display: inline-flex; align-items: center; gap: 12px;">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
            Join Discord
        </a>
        <a href="#" class="btn-secondary" style="text-decoration: none; background: #f8fafc; border: 1px solid rgba(0,0,0,0.1); color: #111827; padding: 18px 40px; border-radius: 100px; font-size: 18px; font-weight: 600; transition: all 0.3s ease;">Explore Nexmart</a>
      </div>
    </div>
  </section>

  <style>
    .feature-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 24px 48px rgba(0,0,0,0.06) !important;
        border-color: rgba(0,0,0,0.1) !important;
    }
    .channel-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 16px 32px rgba(0,0,0,0.04) !important;
        border-color: rgba(37,99,235,0.2) !important;
    }
    .who-card:hover {
        transform: translateY(-4px);
        background: #ffffff !important;
        border-color: rgba(0,0,0,0.1) !important;
        box-shadow: 0 12px 32px rgba(0,0,0,0.04) !important;
    }
    .stat-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 24px 48px rgba(37,99,235,0.08) !important;
        border-color: rgba(37,99,235,0.2) !important;
    }
    .btn-primary:hover {
        background: #1d4ed8 !important;
        transform: translateY(-2px);
    }
    .btn-secondary:hover {
        background: #ffffff !important;
        border-color: rgba(0,0,0,0.2) !important;
        transform: translateY(-2px);
    }
    
    @media (max-width: 900px) {
        .semantic-discord-wrapper section {
            padding: 100px 5% !important;
        }
        .semantic-discord-wrapper h2 {
            font-size: 40px !important;
        }
        .feature-card, .channel-card, .stat-card {
            padding: 40px !important;
        }
    }
    @media (max-width: 600px) {
        .semantic-discord-wrapper section {
            padding: 80px 5% !important;
        }
        .semantic-discord-wrapper h2 {
            font-size: 32px !important;
        }
        .semantic-discord-wrapper .btn-primary, .semantic-discord-wrapper .btn-secondary {
            width: 100%;
            justify-content: center;
        }
    }
  </style>
</div>
"""

# Replace placeholder section
placeholder = soup.find(string=lambda text: text and 'Content Coming Soon' in text)
if placeholder:
    section_to_replace = placeholder.find_parent('section')
    if section_to_replace:
        new_section = bs4.BeautifulSoup(discord_html, 'html.parser')
        section_to_replace.replace_with(new_section)

# Make sure CTA section has white background to match the final section
sections = soup.find_all('section')
if len(sections) > 1:
    cta = sections[-1]
    cta['style'] = cta.get('style', '') + '; background-color: #ffffff;'
    for h in cta.find_all(['h2', 'h3']):
        h['style'] = h.get('style', '') + '; color: #111827 !important;'
    for p in cta.find_all('p'):
        p['style'] = p.get('style', '') + '; color: #4B5563 !important;'

with open('discord-community.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Successfully built the Discord Community page.")
