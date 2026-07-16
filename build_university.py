import bs4

with open('nexmart-university.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = bs4.BeautifulSoup(html, 'html.parser')

# 1. Update Title
if soup.title:
    soup.title.string = "Nexmart - University"

# 2. Update Hero
hero = soup.find('section', class_=lambda c: c and 'is-hero' in c)
if hero:
    hero['style'] = hero.get('style', '') + '; background-color: #ffffff; color: #111827;'
    h1 = hero.find('h1')
    if h1:
        h1.string = "Learn Agentic Commerce"
        h1['style'] = h1.get('style', '') + '; color: #111827 !important;'
    p = hero.find('p')
    if p:
        p.string = "Master the future of AI-powered commerce through practical guides, tutorials, and learning paths designed for shoppers, sellers, and businesses."
        p['style'] = p.get('style', '') + '; color: #4B5563 !important;'

# 3. Build University Content HTML
university_html = """
<div class="semantic-university-wrapper" style="width: 100%; display: flex; flex-direction: column;">
  
  <!-- SECTION 1: LEARNING PATHS (White Background) -->
  <section style="background-color: #ffffff; padding: 120px 5% 180px 5%; width: 100%; box-sizing: border-box;">
    <div style="max-width: 1400px; margin: 0 auto;">
      <h2 style="font-size: 44px; font-weight: 600; color: #111827; margin-bottom: 64px; letter-spacing: -0.03em; text-align: center;">Choose Your Learning Path</h2>
      
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 32px;">
        <!-- Path 1 -->
        <a href="#" class="path-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px; box-shadow: 0 12px 32px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); min-height: 340px;">
          <div style="background: #f8fafc; width: 64px; height: 64px; border-radius: 20px; display: flex; align-items: center; justify-content: center; margin-bottom: 32px; color: #2563EB;">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1 0-5H20"/></svg>
          </div>
          <h3 style="font-size: 26px; font-weight: 600; color: #111827; margin-bottom: 16px; line-height: 1.3; letter-spacing: -0.01em;">Getting Started</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.7; margin: 0; flex-grow: 1;">Understand Agentic Commerce and complete your first AI-powered purchase.</p>
          <div class="card-link" style="display: flex; align-items: center; color: #2563EB; font-weight: 600; font-size: 18px; margin-top: 32px; transition: transform 0.3s ease;">Start Learning <span style="margin-left: 8px;">→</span></div>
        </a>
        <!-- Path 2 -->
        <a href="#" class="path-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px; box-shadow: 0 12px 32px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); min-height: 340px;">
          <div style="background: #f8fafc; width: 64px; height: 64px; border-radius: 20px; display: flex; align-items: center; justify-content: center; margin-bottom: 32px; color: #2563EB;">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z"/></svg>
          </div>
          <h3 style="font-size: 26px; font-weight: 600; color: #111827; margin-bottom: 16px; line-height: 1.3; letter-spacing: -0.01em;">Shopper Mastery</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.7; margin: 0; flex-grow: 1;">Advanced prompting, subscriptions, Magic AI Search, and personal AI shopping workflows.</p>
          <div class="card-link" style="display: flex; align-items: center; color: #2563EB; font-weight: 600; font-size: 18px; margin-top: 32px; transition: transform 0.3s ease;">Explore <span style="margin-left: 8px;">→</span></div>
        </a>
        <!-- Path 3 -->
        <a href="#" class="path-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px; box-shadow: 0 12px 32px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); min-height: 340px;">
          <div style="background: #f8fafc; width: 64px; height: 64px; border-radius: 20px; display: flex; align-items: center; justify-content: center; margin-bottom: 32px; color: #2563EB;">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
          </div>
          <h3 style="font-size: 26px; font-weight: 600; color: #111827; margin-bottom: 16px; line-height: 1.3; letter-spacing: -0.01em;">Seller Playbooks</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.7; margin: 0; flex-grow: 1;">Learn how to sell on Nexmart, optimize listings, use AI pricing and inventory intelligence.</p>
          <div class="card-link" style="display: flex; align-items: center; color: #2563EB; font-weight: 600; font-size: 18px; margin-top: 32px; transition: transform 0.3s ease;">View Guides <span style="margin-left: 8px;">→</span></div>
        </a>
        <!-- Path 4 -->
        <a href="#" class="path-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px; box-shadow: 0 12px 32px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); min-height: 340px;">
          <div style="background: #f8fafc; width: 64px; height: 64px; border-radius: 20px; display: flex; align-items: center; justify-content: center; margin-bottom: 32px; color: #2563EB;">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="4" rx="2" ry="2"/><line x1="16" x2="16" y1="2" y2="6"/><line x1="8" x2="8" y1="2" y2="6"/><line x1="3" x2="21" y1="10" y2="10"/><path d="M8 14h.01"/><path d="M12 14h.01"/><path d="M16 14h.01"/><path d="M8 18h.01"/><path d="M12 18h.01"/><path d="M16 18h.01"/></svg>
          </div>
          <h3 style="font-size: 26px; font-weight: 600; color: #111827; margin-bottom: 16px; line-height: 1.3; letter-spacing: -0.01em;">Business Suite</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.7; margin: 0; flex-grow: 1;">Master Advertiser Tracker, Competitor Research, Portfolio, Theme Detector and the complete AI toolkit.</p>
          <div class="card-link" style="display: flex; align-items: center; color: #2563EB; font-weight: 600; font-size: 18px; margin-top: 32px; transition: transform 0.3s ease;">Open Courses <span style="margin-left: 8px;">→</span></div>
        </a>
      </div>
    </div>
  </section>

  <!-- SECTION 2: FEATURED COURSES (Light Gray Background) -->
  <section style="background-color: #f8fafc; padding: 180px 5%; width: 100%; box-sizing: border-box; border-top: 1px solid rgba(0,0,0,0.03); border-bottom: 1px solid rgba(0,0,0,0.03);">
    <div style="max-width: 1400px; margin: 0 auto;">
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 64px; letter-spacing: -0.03em;">Popular Courses</h2>
      
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap: 32px;">
        <!-- Course 1 -->
        <a href="#" class="course-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 20px; padding: 40px; box-shadow: 0 8px 24px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);">
          <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 24px;">
            <span style="background: rgba(37,99,235,0.1); color: #2563EB; padding: 6px 12px; border-radius: 100px; font-size: 14px; font-weight: 600;">Beginner</span>
            <span style="color: #64748b; font-size: 15px; display: flex; align-items: center; gap: 6px;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg> 20 min</span>
          </div>
          <h3 style="font-size: 24px; font-weight: 600; color: #111827; margin-bottom: 8px; line-height: 1.3;">Introduction to Agentic Commerce</h3>
          <div class="card-link" style="display: flex; align-items: center; color: #2563EB; font-weight: 600; font-size: 16px; margin-top: auto; padding-top: 32px; transition: transform 0.3s ease;">Continue <span style="margin-left: 8px;">→</span></div>
        </a>
        <!-- Course 2 -->
        <a href="#" class="course-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 20px; padding: 40px; box-shadow: 0 8px 24px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);">
          <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 24px;">
            <span style="background: rgba(37,99,235,0.1); color: #2563EB; padding: 6px 12px; border-radius: 100px; font-size: 14px; font-weight: 600;">Beginner</span>
            <span style="color: #64748b; font-size: 15px; display: flex; align-items: center; gap: 6px;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg> 15 min</span>
          </div>
          <h3 style="font-size: 24px; font-weight: 600; color: #111827; margin-bottom: 8px; line-height: 1.3;">Your First AI Shopping Request</h3>
          <div class="card-link" style="display: flex; align-items: center; color: #2563EB; font-weight: 600; font-size: 16px; margin-top: auto; padding-top: 32px; transition: transform 0.3s ease;">Continue <span style="margin-left: 8px;">→</span></div>
        </a>
        <!-- Course 3 -->
        <a href="#" class="course-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 20px; padding: 40px; box-shadow: 0 8px 24px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);">
          <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 24px;">
            <span style="background: rgba(245,158,11,0.1); color: #d97706; padding: 6px 12px; border-radius: 100px; font-size: 14px; font-weight: 600;">Intermediate</span>
            <span style="color: #64748b; font-size: 15px; display: flex; align-items: center; gap: 6px;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg> 35 min</span>
          </div>
          <h3 style="font-size: 24px; font-weight: 600; color: #111827; margin-bottom: 8px; line-height: 1.3;">Magic AI Search Deep Dive</h3>
          <div class="card-link" style="display: flex; align-items: center; color: #2563EB; font-weight: 600; font-size: 16px; margin-top: auto; padding-top: 32px; transition: transform 0.3s ease;">Continue <span style="margin-left: 8px;">→</span></div>
        </a>
        <!-- Course 4 -->
        <a href="#" class="course-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 20px; padding: 40px; box-shadow: 0 8px 24px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);">
          <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 24px;">
            <span style="background: rgba(245,158,11,0.1); color: #d97706; padding: 6px 12px; border-radius: 100px; font-size: 14px; font-weight: 600;">Intermediate</span>
            <span style="color: #64748b; font-size: 15px; display: flex; align-items: center; gap: 6px;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg> 45 min</span>
          </div>
          <h3 style="font-size: 24px; font-weight: 600; color: #111827; margin-bottom: 8px; line-height: 1.3;">Building Your AI Store</h3>
          <div class="card-link" style="display: flex; align-items: center; color: #2563EB; font-weight: 600; font-size: 16px; margin-top: auto; padding-top: 32px; transition: transform 0.3s ease;">Continue <span style="margin-left: 8px;">→</span></div>
        </a>
        <!-- Course 5 -->
        <a href="#" class="course-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 20px; padding: 40px; box-shadow: 0 8px 24px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);">
          <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 24px;">
            <span style="background: rgba(16,185,129,0.1); color: #059669; padding: 6px 12px; border-radius: 100px; font-size: 14px; font-weight: 600;">Advanced</span>
            <span style="color: #64748b; font-size: 15px; display: flex; align-items: center; gap: 6px;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg> 40 min</span>
          </div>
          <h3 style="font-size: 24px; font-weight: 600; color: #111827; margin-bottom: 8px; line-height: 1.3;">Competitor Intelligence</h3>
          <div class="card-link" style="display: flex; align-items: center; color: #2563EB; font-weight: 600; font-size: 16px; margin-top: auto; padding-top: 32px; transition: transform 0.3s ease;">Continue <span style="margin-left: 8px;">→</span></div>
        </a>
        <!-- Course 6 -->
        <a href="#" class="course-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 20px; padding: 40px; box-shadow: 0 8px 24px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);">
          <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 24px;">
            <span style="background: rgba(16,185,129,0.1); color: #059669; padding: 6px 12px; border-radius: 100px; font-size: 14px; font-weight: 600;">Advanced</span>
            <span style="color: #64748b; font-size: 15px; display: flex; align-items: center; gap: 6px;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg> 60 min</span>
          </div>
          <h3 style="font-size: 24px; font-weight: 600; color: #111827; margin-bottom: 8px; line-height: 1.3;">Scaling with Business Suite</h3>
          <div class="card-link" style="display: flex; align-items: center; color: #2563EB; font-weight: 600; font-size: 16px; margin-top: auto; padding-top: 32px; transition: transform 0.3s ease;">Continue <span style="margin-left: 8px;">→</span></div>
        </a>
      </div>
    </div>
  </section>

  <!-- SECTION 3: LEARNING CATEGORIES (White Background) -->
  <section style="background-color: #ffffff; padding: 180px 5%; width: 100%; box-sizing: border-box;">
    <div style="max-width: 1400px; margin: 0 auto;">
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 64px; letter-spacing: -0.03em; text-align: center;">Explore Topics</h2>
      
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 24px;">
        <!-- Categories -->
        <a href="#" class="category-card" style="text-decoration: none; background: #f8fafc; border: 1px solid rgba(0,0,0,0.04); border-radius: 16px; padding: 32px; display: flex; align-items: center; gap: 16px; transition: all 0.3s ease;">
          <div style="color: #2563EB;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M16 12l-4-4-4 4"/></svg></div>
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin: 0;">AI Shopping</h3>
        </a>
        <a href="#" class="category-card" style="text-decoration: none; background: #f8fafc; border: 1px solid rgba(0,0,0,0.04); border-radius: 16px; padding: 32px; display: flex; align-items: center; gap: 16px; transition: all 0.3s ease;">
          <div style="color: #2563EB;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg></div>
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin: 0;">Seller Success</h3>
        </a>
        <a href="#" class="category-card" style="text-decoration: none; background: #f8fafc; border: 1px solid rgba(0,0,0,0.04); border-radius: 16px; padding: 32px; display: flex; align-items: center; gap: 16px; transition: all 0.3s ease;">
          <div style="color: #2563EB;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg></div>
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin: 0;">Business Analytics</h3>
        </a>
        <a href="#" class="category-card" style="text-decoration: none; background: #f8fafc; border: 1px solid rgba(0,0,0,0.04); border-radius: 16px; padding: 32px; display: flex; align-items: center; gap: 16px; transition: all 0.3s ease;">
          <div style="color: #2563EB;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg></div>
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin: 0;">Advertising</h3>
        </a>
        <a href="#" class="category-card" style="text-decoration: none; background: #f8fafc; border: 1px solid rgba(0,0,0,0.04); border-radius: 16px; padding: 32px; display: flex; align-items: center; gap: 16px; transition: all 0.3s ease;">
          <div style="color: #2563EB;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2a10 10 0 1 0 10 10 4 4 0 0 1-5-5 4 4 0 0 1-5-5"/></svg></div>
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin: 0;">Automation</h3>
        </a>
        <a href="#" class="category-card" style="text-decoration: none; background: #f8fafc; border: 1px solid rgba(0,0,0,0.04); border-radius: 16px; padding: 32px; display: flex; align-items: center; gap: 16px; transition: all 0.3s ease;">
          <div style="color: #2563EB;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 21V5a2 2 0 0 1 2-2h11l5 5v11a2 2 0 0 1-2 2z"/><polyline points="17 21 17 13 7 13 7 21"/><polyline points="7 3 7 8 15 8"/></svg></div>
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin: 0;">Supply Chain</h3>
        </a>
        <a href="#" class="category-card" style="text-decoration: none; background: #f8fafc; border: 1px solid rgba(0,0,0,0.04); border-radius: 16px; padding: 32px; display: flex; align-items: center; gap: 16px; transition: all 0.3s ease;">
          <div style="color: #2563EB;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="14" x="2" y="5" rx="2"/><line x1="2" x2="22" y1="10" y2="10"/></svg></div>
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin: 0;">Payments</h3>
        </a>
        <a href="#" class="category-card" style="text-decoration: none; background: #f8fafc; border: 1px solid rgba(0,0,0,0.04); border-radius: 16px; padding: 32px; display: flex; align-items: center; gap: 16px; transition: all 0.3s ease;">
          <div style="color: #2563EB;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><line x1="9" x2="9" y1="3" y2="21"/></svg></div>
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin: 0;">Logistics</h3>
        </a>
      </div>
    </div>
  </section>

  <!-- SECTION 4: WHY LEARN WITH NEXMART (Light Gray Background) -->
  <section style="background-color: #f8fafc; padding: 180px 5%; width: 100%; box-sizing: border-box; border-top: 1px solid rgba(0,0,0,0.03);">
    <div style="max-width: 1400px; margin: 0 auto;">
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 80px; letter-spacing: -0.03em; text-align: center;">Built For Real Commerce</h2>
      
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 32px;">
        <!-- Feature 1 -->
        <div class="feature-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.05); border-radius: 24px; padding: 48px; box-shadow: 0 8px 32px rgba(0,0,0,0.02); text-align: left; display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="margin-bottom: 24px; background: rgba(37,99,235,0.05); width: 64px; height: 64px; border-radius: 16px; display: flex; align-items: center; justify-content: center; color: #2563EB;">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="m18 16 4-4-4-4"/><path d="m6 8-4 4 4 4"/><path d="m14.5 4-5 16"/></svg>
          </div>
          <h3 style="font-size: 24px; font-weight: 600; color: #111827; margin-bottom: 12px; line-height: 1.3; letter-spacing: -0.01em;">Practical Lessons</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.7; margin: 0;">Real-world workflows instead of theory.</p>
        </div>
        <!-- Feature 2 -->
        <div class="feature-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.05); border-radius: 24px; padding: 48px; box-shadow: 0 8px 32px rgba(0,0,0,0.02); text-align: left; display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="margin-bottom: 24px; background: rgba(37,99,235,0.05); width: 64px; height: 64px; border-radius: 16px; display: flex; align-items: center; justify-content: center; color: #2563EB;">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12a10 10 0 1 0 20 0 10 10 0 1 0-20 0"/><path d="M12 6v6l4 2"/></svg>
          </div>
          <h3 style="font-size: 24px; font-weight: 600; color: #111827; margin-bottom: 12px; line-height: 1.3; letter-spacing: -0.01em;">Always Updated</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.7; margin: 0;">Content evolves alongside the platform.</p>
        </div>
        <!-- Feature 3 -->
        <div class="feature-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.05); border-radius: 24px; padding: 48px; box-shadow: 0 8px 32px rgba(0,0,0,0.02); text-align: left; display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="margin-bottom: 24px; background: rgba(37,99,235,0.05); width: 64px; height: 64px; border-radius: 16px; display: flex; align-items: center; justify-content: center; color: #2563EB;">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/></svg>
          </div>
          <h3 style="font-size: 24px; font-weight: 600; color: #111827; margin-bottom: 12px; line-height: 1.3; letter-spacing: -0.01em;">Expert Designed</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.7; margin: 0;">Built by the Nexmart product team.</p>
        </div>
        <!-- Feature 4 -->
        <div class="feature-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.05); border-radius: 24px; padding: 48px; box-shadow: 0 8px 32px rgba(0,0,0,0.02); text-align: left; display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="margin-bottom: 24px; background: rgba(37,99,235,0.05); width: 64px; height: 64px; border-radius: 16px; display: flex; align-items: center; justify-content: center; color: #2563EB;">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="3" rx="2"/><path d="M7 7h10"/><path d="M7 12h10"/><path d="M7 17h10"/></svg>
          </div>
          <h3 style="font-size: 24px; font-weight: 600; color: #111827; margin-bottom: 12px; line-height: 1.3; letter-spacing: -0.01em;">Learn At Your Pace</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.7; margin: 0;">Short modules that fit into your schedule.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 5: CERTIFICATION (White Background) -->
  <section style="background-color: #ffffff; padding: 180px 5% 240px 5%; width: 100%; box-sizing: border-box; border-top: 1px solid rgba(0,0,0,0.03);">
    <div style="max-width: 1000px; margin: 0 auto; text-align: center;">
      <h2 style="font-size: 48px; font-weight: 600; color: #111827; margin-bottom: 24px; letter-spacing: -0.03em;">Become Nexmart Certified</h2>
      <p style="font-size: 22px; color: #4B5563; line-height: 1.7; margin: 0 0 48px 0;">Complete learning paths and demonstrate your expertise in Agentic Commerce with official Nexmart certifications.</p>
      <div style="display: flex; gap: 16px; justify-content: center; flex-wrap: wrap;">
        <a href="#" class="btn-primary" style="text-decoration: none; background: #111827; color: #ffffff; padding: 18px 40px; border-radius: 100px; font-size: 18px; font-weight: 600; transition: all 0.3s ease;">Start Learning</a>
        <a href="#" class="btn-secondary" style="text-decoration: none; background: #f8fafc; border: 1px solid rgba(0,0,0,0.1); color: #111827; padding: 18px 40px; border-radius: 100px; font-size: 18px; font-weight: 600; transition: all 0.3s ease;">Browse Courses</a>
      </div>
    </div>
  </section>

  <style>
    .path-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 24px 48px rgba(0,0,0,0.06) !important;
        border-color: rgba(0,0,0,0.1) !important;
    }
    .path-card:hover .card-link {
        transform: translateX(8px);
    }
    .course-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 16px 32px rgba(0,0,0,0.06) !important;
        border-color: rgba(0,0,0,0.1) !important;
    }
    .course-card:hover .card-link {
        transform: translateX(8px);
    }
    .category-card:hover {
        transform: translateY(-4px);
        background: #ffffff !important;
        border-color: rgba(37,99,235,0.2) !important;
        box-shadow: 0 8px 24px rgba(37,99,235,0.06) !important;
    }
    .feature-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 24px 48px rgba(0,0,0,0.06) !important;
        border-color: rgba(0,0,0,0.1) !important;
    }
    .btn-primary:hover {
        background: #374151 !important;
        transform: translateY(-2px);
    }
    .btn-secondary:hover {
        background: #ffffff !important;
        border-color: rgba(0,0,0,0.2) !important;
        transform: translateY(-2px);
    }
    
    @media (max-width: 900px) {
        .semantic-university-wrapper section {
            padding: 100px 5% !important;
        }
        .semantic-university-wrapper h2 {
            font-size: 40px !important;
        }
        .semantic-university-wrapper .path-card, .course-card, .feature-card {
            padding: 40px !important;
        }
    }
    @media (max-width: 600px) {
        .semantic-university-wrapper section {
            padding: 80px 5% !important;
        }
        .semantic-university-wrapper h2 {
            font-size: 32px !important;
        }
        .semantic-university-wrapper .btn-primary, .semantic-university-wrapper .btn-secondary {
            width: 100%;
            text-align: center;
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
        new_section = bs4.BeautifulSoup(university_html, 'html.parser')
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

with open('nexmart-university.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Successfully built the Nexmart University page.")
