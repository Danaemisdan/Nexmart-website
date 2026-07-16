import bs4

with open('blog.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = bs4.BeautifulSoup(html, 'html.parser')

# 1. Update Title
if soup.title:
    soup.title.string = "Nexmart - Journal"

# 2. Update Hero
hero = soup.find('section', class_=lambda c: c and 'is-hero' in c)
if hero:
    hero['style'] = hero.get('style', '') + '; background-color: #ffffff; color: #111827;'
    h1 = hero.find('h1')
    if h1:
        h1.string = "Nexmart Journal"
        h1['style'] = h1.get('style', '') + '; color: #111827 !important;'
    p = hero.find('p')
    if p:
        p.string = "Ideas, product updates, industry insights, and thought leadership shaping the future of Agentic Commerce."
        p['style'] = p.get('style', '') + '; color: #4B5563 !important;'

# 3. Build Blog Content HTML
blog_html = """
<div class="semantic-blog-wrapper" style="width: 100%; display: flex; flex-direction: column;">
  
  <!-- SECTION 1: FEATURED STORY (White Background) -->
  <section style="background-color: #ffffff; padding: 80px 5% 180px 5%; width: 100%; box-sizing: border-box;">
    <div style="max-width: 1400px; margin: 0 auto;">
      <a href="#" class="featured-card" style="text-decoration: none; display: flex; flex-direction: column; background: #f8fafc; border: 1px solid rgba(0,0,0,0.05); border-radius: 32px; padding: 80px; box-shadow: 0 12px 48px rgba(0,0,0,0.02); transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
        <div style="color: #2563EB; font-size: 14px; font-weight: 700; letter-spacing: 0.05em; text-transform: uppercase; margin-bottom: 24px;">Featured Story</div>
        <h2 style="font-size: 56px; font-weight: 600; color: #111827; margin-bottom: 32px; line-height: 1.1; letter-spacing: -0.03em; max-width: 1000px;">The End of Manual Shopping Has Begun</h2>
        <p style="font-size: 22px; color: #4B5563; line-height: 1.7; margin-bottom: 48px; max-width: 800px;">Commerce has evolved from search engines to marketplaces. The next evolution is autonomous shopping, where intelligent AI agents understand intent, compare options, negotiate pricing, and execute purchases on your behalf.</p>
        
        <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 24px;">
            <div style="display: flex; align-items: center; gap: 24px; color: #64748b; font-size: 16px; font-weight: 500;">
                <div style="display: flex; align-items: center; gap: 8px;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg> 8 min read</div>
                <div style="width: 4px; height: 4px; border-radius: 50%; background: #cbd5e1;"></div>
                <div>July 2026</div>
                <div style="width: 4px; height: 4px; border-radius: 50%; background: #cbd5e1;"></div>
                <div style="color: #2563EB; background: rgba(37,99,235,0.1); padding: 4px 12px; border-radius: 100px;">Agentic Commerce</div>
            </div>
            <div class="card-link" style="display: flex; align-items: center; color: #111827; font-weight: 600; font-size: 18px; transition: transform 0.3s ease;">Read Article <span style="margin-left: 8px;">→</span></div>
        </div>
      </a>
    </div>
  </section>

  <!-- SECTION 2: CATEGORIES (Light Gray Background) -->
  <section style="background-color: #f8fafc; padding: 180px 5%; width: 100%; box-sizing: border-box; border-top: 1px solid rgba(0,0,0,0.03); border-bottom: 1px solid rgba(0,0,0,0.03);">
    <div style="max-width: 1400px; margin: 0 auto;">
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 64px; letter-spacing: -0.03em; text-align: center;">Explore Topics</h2>
      
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px;">
        <a href="#" class="category-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 16px; padding: 32px; display: flex; align-items: center; gap: 16px; transition: all 0.3s ease; box-shadow: 0 4px 12px rgba(0,0,0,0.02);">
          <div style="color: #2563EB;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div>
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin: 0;">Agentic Commerce</h3>
        </a>
        <a href="#" class="category-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 16px; padding: 32px; display: flex; align-items: center; gap: 16px; transition: all 0.3s ease; box-shadow: 0 4px 12px rgba(0,0,0,0.02);">
          <div style="color: #2563EB;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m2 9 3-3 3 3"/><path d="M13 18H7a2 2 0 0 1-2-2V6"/><path d="m22 15-3 3-3-3"/><path d="M11 6h6a2 2 0 0 1 2 2v10"/></svg></div>
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin: 0;">Product Updates</h3>
        </a>
        <a href="#" class="category-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 16px; padding: 32px; display: flex; align-items: center; gap: 16px; transition: all 0.3s ease; box-shadow: 0 4px 12px rgba(0,0,0,0.02);">
          <div style="color: #2563EB;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg></div>
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin: 0;">Industry Insights</h3>
        </a>
        <a href="#" class="category-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 16px; padding: 32px; display: flex; align-items: center; gap: 16px; transition: all 0.3s ease; box-shadow: 0 4px 12px rgba(0,0,0,0.02);">
          <div style="color: #2563EB;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="4" rx="2" ry="2"/><line x1="16" x2="16" y1="2" y2="6"/><line x1="8" x2="8" y1="2" y2="6"/><line x1="3" x2="21" y1="10" y2="10"/><path d="M8 14h.01"/><path d="M12 14h.01"/><path d="M16 14h.01"/><path d="M8 18h.01"/><path d="M12 18h.01"/><path d="M16 18h.01"/></svg></div>
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin: 0;">AI Research</h3>
        </a>
        <a href="#" class="category-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 16px; padding: 32px; display: flex; align-items: center; gap: 16px; transition: all 0.3s ease; box-shadow: 0 4px 12px rgba(0,0,0,0.02);">
          <div style="color: #2563EB;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg></div>
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin: 0;">Seller Success</h3>
        </a>
        <a href="#" class="category-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 16px; padding: 32px; display: flex; align-items: center; gap: 16px; transition: all 0.3s ease; box-shadow: 0 4px 12px rgba(0,0,0,0.02);">
          <div style="color: #2563EB;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg></div>
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin: 0;">Engineering</h3>
        </a>
        <a href="#" class="category-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 16px; padding: 32px; display: flex; align-items: center; gap: 16px; transition: all 0.3s ease; box-shadow: 0 4px 12px rgba(0,0,0,0.02);">
          <div style="color: #2563EB;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="3.29 7 12 12 20.71 7"/><line x1="12" y1="22" x2="12" y2="12"/></svg></div>
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin: 0;">Company News</h3>
        </a>
        <a href="#" class="category-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 16px; padding: 32px; display: flex; align-items: center; gap: 16px; transition: all 0.3s ease; box-shadow: 0 4px 12px rgba(0,0,0,0.02);">
          <div style="color: #2563EB;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg></div>
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin: 0;">Case Studies</h3>
        </a>
      </div>
    </div>
  </section>

  <!-- SECTION 3: LATEST ARTICLES (White Background) -->
  <section style="background-color: #ffffff; padding: 180px 5%; width: 100%; box-sizing: border-box;">
    <div style="max-width: 1400px; margin: 0 auto;">
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 64px; letter-spacing: -0.03em;">Latest Articles</h2>
      
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 40px;">
        <!-- Article 1 -->
        <a href="#" class="article-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px; box-shadow: 0 8px 32px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); min-height: 380px;">
          <div style="color: #2563EB; font-size: 14px; font-weight: 700; letter-spacing: 0.05em; text-transform: uppercase; margin-bottom: 24px;">Agentic Commerce</div>
          <h3 style="font-size: 28px; font-weight: 600; color: #111827; margin-bottom: 16px; line-height: 1.3; letter-spacing: -0.01em;">Why Agentic Commerce Changes Everything</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.7; margin: 0 0 32px 0; flex-grow: 1;">A deep dive into how AI agents are removing the friction from global marketplaces.</p>
          <div style="display: flex; align-items: center; justify-content: space-between; border-top: 1px solid rgba(0,0,0,0.05); padding-top: 24px;">
              <span style="color: #64748b; font-size: 15px; font-weight: 500; display: flex; align-items: center; gap: 8px;"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg> 6 min read</span>
              <div class="card-link" style="display: flex; align-items: center; color: #111827; font-weight: 600; font-size: 16px; transition: transform 0.3s ease;">Read Article <span style="margin-left: 8px;">→</span></div>
          </div>
        </a>
        <!-- Article 2 -->
        <a href="#" class="article-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px; box-shadow: 0 8px 32px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); min-height: 380px;">
          <div style="color: #2563EB; font-size: 14px; font-weight: 700; letter-spacing: 0.05em; text-transform: uppercase; margin-bottom: 24px;">Product Updates</div>
          <h3 style="font-size: 28px; font-weight: 600; color: #111827; margin-bottom: 16px; line-height: 1.3; letter-spacing: -0.01em;">Introducing Magic AI Search</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.7; margin: 0 0 32px 0; flex-grow: 1;">Experience the power of reasoning-based natural language product discovery.</p>
          <div style="display: flex; align-items: center; justify-content: space-between; border-top: 1px solid rgba(0,0,0,0.05); padding-top: 24px;">
              <span style="color: #64748b; font-size: 15px; font-weight: 500; display: flex; align-items: center; gap: 8px;"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg> 4 min read</span>
              <div class="card-link" style="display: flex; align-items: center; color: #111827; font-weight: 600; font-size: 16px; transition: transform 0.3s ease;">Read Article <span style="margin-left: 8px;">→</span></div>
          </div>
        </a>
        <!-- Article 3 -->
        <a href="#" class="article-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px; box-shadow: 0 8px 32px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); min-height: 380px;">
          <div style="color: #2563EB; font-size: 14px; font-weight: 700; letter-spacing: 0.05em; text-transform: uppercase; margin-bottom: 24px;">Engineering</div>
          <h3 style="font-size: 28px; font-weight: 600; color: #111827; margin-bottom: 16px; line-height: 1.3; letter-spacing: -0.01em;">Behind Nexmart's AI Shopping Agents</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.7; margin: 0 0 32px 0; flex-grow: 1;">How we engineered autonomous systems that accurately understand user intent.</p>
          <div style="display: flex; align-items: center; justify-content: space-between; border-top: 1px solid rgba(0,0,0,0.05); padding-top: 24px;">
              <span style="color: #64748b; font-size: 15px; font-weight: 500; display: flex; align-items: center; gap: 8px;"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg> 9 min read</span>
              <div class="card-link" style="display: flex; align-items: center; color: #111827; font-weight: 600; font-size: 16px; transition: transform 0.3s ease;">Read Article <span style="margin-left: 8px;">→</span></div>
          </div>
        </a>
        <!-- Article 4 -->
        <a href="#" class="article-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px; box-shadow: 0 8px 32px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); min-height: 380px;">
          <div style="color: #2563EB; font-size: 14px; font-weight: 700; letter-spacing: 0.05em; text-transform: uppercase; margin-bottom: 24px;">Seller Success</div>
          <h3 style="font-size: 28px; font-weight: 600; color: #111827; margin-bottom: 16px; line-height: 1.3; letter-spacing: -0.01em;">How Sellers Can Prepare For AI Commerce</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.7; margin: 0 0 32px 0; flex-grow: 1;">Actionable steps to optimize your listings for autonomous agents instead of human eyes.</p>
          <div style="display: flex; align-items: center; justify-content: space-between; border-top: 1px solid rgba(0,0,0,0.05); padding-top: 24px;">
              <span style="color: #64748b; font-size: 15px; font-weight: 500; display: flex; align-items: center; gap: 8px;"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg> 7 min read</span>
              <div class="card-link" style="display: flex; align-items: center; color: #111827; font-weight: 600; font-size: 16px; transition: transform 0.3s ease;">Read Article <span style="margin-left: 8px;">→</span></div>
          </div>
        </a>
        <!-- Article 5 -->
        <a href="#" class="article-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px; box-shadow: 0 8px 32px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); min-height: 380px;">
          <div style="color: #2563EB; font-size: 14px; font-weight: 700; letter-spacing: 0.05em; text-transform: uppercase; margin-bottom: 24px;">Industry Insights</div>
          <h3 style="font-size: 28px; font-weight: 600; color: #111827; margin-bottom: 16px; line-height: 1.3; letter-spacing: -0.01em;">The Future Of Global Commerce</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.7; margin: 0 0 32px 0; flex-grow: 1;">How AI logistics routing is erasing borders and connecting emerging markets.</p>
          <div style="display: flex; align-items: center; justify-content: space-between; border-top: 1px solid rgba(0,0,0,0.05); padding-top: 24px;">
              <span style="color: #64748b; font-size: 15px; font-weight: 500; display: flex; align-items: center; gap: 8px;"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg> 8 min read</span>
              <div class="card-link" style="display: flex; align-items: center; color: #111827; font-weight: 600; font-size: 16px; transition: transform 0.3s ease;">Read Article <span style="margin-left: 8px;">→</span></div>
          </div>
        </a>
        <!-- Article 6 -->
        <a href="#" class="article-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px; box-shadow: 0 8px 32px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); min-height: 380px;">
          <div style="color: #2563EB; font-size: 14px; font-weight: 700; letter-spacing: 0.05em; text-transform: uppercase; margin-bottom: 24px;">AI Research</div>
          <h3 style="font-size: 28px; font-weight: 600; color: #111827; margin-bottom: 16px; line-height: 1.3; letter-spacing: -0.01em;">Building Trust With Autonomous AI</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.7; margin: 0 0 32px 0; flex-grow: 1;">Ensuring safety, reliability, and exact compliance when agents spend real money.</p>
          <div style="display: flex; align-items: center; justify-content: space-between; border-top: 1px solid rgba(0,0,0,0.05); padding-top: 24px;">
              <span style="color: #64748b; font-size: 15px; font-weight: 500; display: flex; align-items: center; gap: 8px;"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg> 5 min read</span>
              <div class="card-link" style="display: flex; align-items: center; color: #111827; font-weight: 600; font-size: 16px; transition: transform 0.3s ease;">Read Article <span style="margin-left: 8px;">→</span></div>
          </div>
        </a>
        <!-- Article 7 -->
        <a href="#" class="article-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px; box-shadow: 0 8px 32px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); min-height: 380px;">
          <div style="color: #2563EB; font-size: 14px; font-weight: 700; letter-spacing: 0.05em; text-transform: uppercase; margin-bottom: 24px;">Product Updates</div>
          <h3 style="font-size: 28px; font-weight: 600; color: #111827; margin-bottom: 16px; line-height: 1.3; letter-spacing: -0.01em;">Product Update: Business Suite</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.7; margin: 0 0 32px 0; flex-grow: 1;">New Advertiser Tracker features and extended competitive intelligence tools.</p>
          <div style="display: flex; align-items: center; justify-content: space-between; border-top: 1px solid rgba(0,0,0,0.05); padding-top: 24px;">
              <span style="color: #64748b; font-size: 15px; font-weight: 500; display: flex; align-items: center; gap: 8px;"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg> 3 min read</span>
              <div class="card-link" style="display: flex; align-items: center; color: #111827; font-weight: 600; font-size: 16px; transition: transform 0.3s ease;">Read Article <span style="margin-left: 8px;">→</span></div>
          </div>
        </a>
        <!-- Article 8 -->
        <a href="#" class="article-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px; box-shadow: 0 8px 32px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); min-height: 380px;">
          <div style="color: #2563EB; font-size: 14px; font-weight: 700; letter-spacing: 0.05em; text-transform: uppercase; margin-bottom: 24px;">Agentic Commerce</div>
          <h3 style="font-size: 28px; font-weight: 600; color: #111827; margin-bottom: 16px; line-height: 1.3; letter-spacing: -0.01em;">Marketplace Intelligence Explained</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.7; margin: 0 0 32px 0; flex-grow: 1;">How our global index maps supply, demand, and hidden supplier relationships.</p>
          <div style="display: flex; align-items: center; justify-content: space-between; border-top: 1px solid rgba(0,0,0,0.05); padding-top: 24px;">
              <span style="color: #64748b; font-size: 15px; font-weight: 500; display: flex; align-items: center; gap: 8px;"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg> 6 min read</span>
              <div class="card-link" style="display: flex; align-items: center; color: #111827; font-weight: 600; font-size: 16px; transition: transform 0.3s ease;">Read Article <span style="margin-left: 8px;">→</span></div>
          </div>
        </a>
        <!-- Article 9 -->
        <a href="#" class="article-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px; box-shadow: 0 8px 32px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); min-height: 380px;">
          <div style="color: #2563EB; font-size: 14px; font-weight: 700; letter-spacing: 0.05em; text-transform: uppercase; margin-bottom: 24px;">Industry Insights</div>
          <h3 style="font-size: 28px; font-weight: 600; color: #111827; margin-bottom: 16px; line-height: 1.3; letter-spacing: -0.01em;">Why Commerce Needs Better Search</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.7; margin: 0 0 32px 0; flex-grow: 1;">Keywords are dead. The necessity of intent-driven product discovery.</p>
          <div style="display: flex; align-items: center; justify-content: space-between; border-top: 1px solid rgba(0,0,0,0.05); padding-top: 24px;">
              <span style="color: #64748b; font-size: 15px; font-weight: 500; display: flex; align-items: center; gap: 8px;"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg> 5 min read</span>
              <div class="card-link" style="display: flex; align-items: center; color: #111827; font-weight: 600; font-size: 16px; transition: transform 0.3s ease;">Read Article <span style="margin-left: 8px;">→</span></div>
          </div>
        </a>
      </div>
    </div>
  </section>

  <!-- SECTION 4: EDITORIAL QUOTE (Light Gray Background) -->
  <section style="background-color: #f8fafc; padding: 180px 5%; width: 100%; box-sizing: border-box; border-top: 1px solid rgba(0,0,0,0.03);">
    <div style="max-width: 1000px; margin: 0 auto; text-align: center;">
      <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#2563EB" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" style="margin-bottom: 40px; opacity: 0.5;"><path d="M3 21c3 0 7-1 7-8V5c0-1.25-.756-2.017-2-2H4c-1.25 0-2 .75-2 1.972V11c0 1.25.75 2 2 2 1 0 1 0 1 1v1c0 1-1 2-2 2s-1 .008-1 1.031V20c0 1 0 1 1 1z"/><path d="M15 21c3 0 7-1 7-8V5c0-1.25-.757-2.017-2-2h-4c-1.25 0-2 .75-2 1.972V11c0 1.25.75 2 2 2h.75c0 2.25.25 4-2.75 4v3c0 1 0 1 1 1z"/></svg>
      <h2 style="font-size: 48px; font-weight: 500; color: #111827; line-height: 1.3; letter-spacing: -0.02em; font-style: italic; margin-bottom: 40px;">"The future of commerce won't be about searching faster.<br><br>It will be about never having to search at all."</h2>
      <div style="font-size: 20px; color: #64748b; font-weight: 600; letter-spacing: 0.05em; text-transform: uppercase;">— Nexmart</div>
    </div>
  </section>

  <!-- SECTION 5: NEWSLETTER (White Background) -->
  <section style="background-color: #ffffff; padding: 180px 5% 240px 5%; width: 100%; box-sizing: border-box; border-top: 1px solid rgba(0,0,0,0.03);">
    <div style="max-width: 800px; margin: 0 auto; text-align: center;">
      <h2 style="font-size: 48px; font-weight: 600; color: #111827; margin-bottom: 24px; letter-spacing: -0.03em;">Stay Ahead Of The Future</h2>
      <p style="font-size: 22px; color: #4B5563; line-height: 1.7; margin-bottom: 56px;">Receive product updates, AI insights, commerce trends, and exclusive Nexmart announcements directly in your inbox.</p>
      
      <form style="display: flex; gap: 16px; background: #f8fafc; padding: 12px; border-radius: 100px; border: 1px solid rgba(0,0,0,0.1); max-width: 600px; margin: 0 auto; box-shadow: 0 8px 32px rgba(0,0,0,0.03);">
        <input type="email" placeholder="Email Address" required style="flex-grow: 1; border: none; background: transparent; padding: 0 24px; font-size: 18px; color: #111827; outline: none; min-width: 0;" class="newsletter-input">
        <button type="button" class="newsletter-submit" style="background: #111827; color: #ffffff; padding: 16px 32px; border: none; border-radius: 100px; font-size: 16px; font-weight: 600; cursor: pointer; transition: all 0.3s ease; white-space: nowrap;">Subscribe</button>
      </form>
    </div>
  </section>

  <style>
    .featured-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 24px 64px rgba(0,0,0,0.06) !important;
        border-color: rgba(0,0,0,0.1) !important;
        background: #ffffff !important;
    }
    .featured-card:hover .card-link {
        transform: translateX(8px);
    }
    .category-card:hover {
        transform: translateY(-4px);
        background: #ffffff !important;
        border-color: rgba(37,99,235,0.2) !important;
        box-shadow: 0 12px 32px rgba(37,99,235,0.06) !important;
    }
    .article-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 24px 48px rgba(0,0,0,0.06) !important;
        border-color: rgba(0,0,0,0.1) !important;
    }
    .article-card:hover .card-link {
        transform: translateX(8px);
    }
    .newsletter-input::placeholder {
        color: #94A3B8;
    }
    .newsletter-submit:hover {
        background: #374151 !important;
        transform: translateY(-2px);
    }
    
    @media (max-width: 900px) {
        .semantic-blog-wrapper section {
            padding: 100px 5% !important;
        }
        .semantic-blog-wrapper h2 {
            font-size: 40px !important;
        }
        .semantic-blog-wrapper .featured-card {
            padding: 48px !important;
        }
    }
    @media (max-width: 600px) {
        .semantic-blog-wrapper section {
            padding: 80px 5% !important;
        }
        .semantic-blog-wrapper h2 {
            font-size: 32px !important;
        }
        .semantic-blog-wrapper form {
            flex-direction: column;
            border-radius: 24px !important;
            padding: 24px !important;
            background: #ffffff !important;
            box-shadow: 0 12px 48px rgba(0,0,0,0.05) !important;
        }
        .newsletter-input {
            padding: 16px !important;
            background: #f8fafc !important;
            border-radius: 12px !important;
        }
        .newsletter-submit {
            width: 100% !important;
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
        new_section = bs4.BeautifulSoup(blog_html, 'html.parser')
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

with open('blog.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Successfully built the Blog page.")
