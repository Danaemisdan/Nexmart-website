import bs4
import shutil

# Make a backup
shutil.copy('contact.html', 'contact_backup.html')

with open('contact.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = bs4.BeautifulSoup(html, 'html.parser')

# 1. Update Title
if soup.title:
    soup.title.string = "Nexmart - Contact Us"

# 2. Update Hero
hero = soup.find('section', class_=lambda c: c and 'is-hero' in c)
if hero:
    hero['style'] = hero.get('style', '') + '; background-color: #ffffff; color: #111827;'
    h1 = hero.find('h1')
    if h1:
        h1.string = "Contact Nexmart"
        h1['style'] = h1.get('style', '') + '; color: #111827 !important;'
    p = hero.find('p')
    if p:
        p.string = "Whether you need support, want to partner with us, have a sales enquiry, or simply want to learn more about Agentic Commerce, we're here to help."
        p['style'] = p.get('style', '') + '; color: #4B5563 !important;'

# 3. Build Contact Content HTML
contact_html = """
<div class="semantic-contact-wrapper" style="width: 100%; display: flex; flex-direction: column;">
  
  <!-- SECTION 1: INTELLIGENT CONTACT ROUTING (White Background) -->
  <section style="background-color: #ffffff; padding: 120px 5% 180px 5%; width: 100%; box-sizing: border-box;">
    <div style="max-width: 1400px; margin: 0 auto;">
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 64px; letter-spacing: -0.03em; text-align: center;">Intelligent Contact Routing</h2>
      
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 32px;">
        <!-- Card 1 -->
        <a href="#form-section" class="contact-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px; box-shadow: 0 12px 32px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); min-height: 280px;">
          <div style="background: #f8fafc; width: 64px; height: 64px; border-radius: 20px; display: flex; align-items: center; justify-content: center; margin-bottom: 24px; color: #111827;">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>
          </div>
          <h3 style="font-size: 24px; font-weight: 600; color: #111827; margin-bottom: 16px; line-height: 1.3; letter-spacing: -0.01em;">Support</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.7; margin: 0; flex-grow: 1;">Questions about orders, accounts, payments or platform usage.</p>
          <div class="card-link" style="display: flex; align-items: center; color: #111827; font-weight: 600; font-size: 18px; margin-top: 32px; transition: transform 0.3s ease;">Contact <span style="margin-left: 8px;">→</span></div>
        </a>
        <!-- Card 2 -->
        <a href="#form-section" class="contact-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px; box-shadow: 0 12px 32px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); min-height: 280px;">
          <div style="background: #f8fafc; width: 64px; height: 64px; border-radius: 20px; display: flex; align-items: center; justify-content: center; margin-bottom: 24px; color: #111827;">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="4" rx="2" ry="2"/><line x1="16" x2="16" y1="2" y2="6"/><line x1="8" x2="8" y1="2" y2="6"/><line x1="3" x2="21" y1="10" y2="10"/><path d="M8 14h.01"/><path d="M12 14h.01"/><path d="M16 14h.01"/><path d="M8 18h.01"/><path d="M12 18h.01"/><path d="M16 18h.01"/></svg>
          </div>
          <h3 style="font-size: 24px; font-weight: 600; color: #111827; margin-bottom: 16px; line-height: 1.3; letter-spacing: -0.01em;">Sales</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.7; margin: 0; flex-grow: 1;">Learn how Nexmart can help your business adopt Agentic Commerce.</p>
          <div class="card-link" style="display: flex; align-items: center; color: #111827; font-weight: 600; font-size: 18px; margin-top: 32px; transition: transform 0.3s ease;">Contact <span style="margin-left: 8px;">→</span></div>
        </a>
        <!-- Card 3 -->
        <a href="#form-section" class="contact-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px; box-shadow: 0 12px 32px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); min-height: 280px;">
          <div style="background: #f8fafc; width: 64px; height: 64px; border-radius: 20px; display: flex; align-items: center; justify-content: center; margin-bottom: 24px; color: #111827;">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m11 17 2 2a1 1 0 1 0 3-3"/><path d="m14 14 2.5 2.5a1 1 0 1 0 3-3l-3.88-3.88a3 3 0 0 0-4.24 0l-7.38 7.38a6 6 0 1 0 8.5 8.5l2.5-2.5"/></svg>
          </div>
          <h3 style="font-size: 24px; font-weight: 600; color: #111827; margin-bottom: 16px; line-height: 1.3; letter-spacing: -0.01em;">Partnerships</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.7; margin: 0; flex-grow: 1;">Discuss integrations, enterprise opportunities and collaborations.</p>
          <div class="card-link" style="display: flex; align-items: center; color: #111827; font-weight: 600; font-size: 18px; margin-top: 32px; transition: transform 0.3s ease;">Contact <span style="margin-left: 8px;">→</span></div>
        </a>
        <!-- Card 4 -->
        <a href="#form-section" class="contact-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px; box-shadow: 0 12px 32px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); min-height: 280px;">
          <div style="background: #f8fafc; width: 64px; height: 64px; border-radius: 20px; display: flex; align-items: center; justify-content: center; margin-bottom: 24px; color: #111827;">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12a5 5 0 0 0 5 5 8 8 0 0 1 5 2 8 8 0 0 1 5-2 5 5 0 0 0 5-5V7h-5a8 8 0 0 0-5 2 8 8 0 0 0-5-2H2Z"/><path d="M6 11c1.5 0 3 .5 3 2-2 0-3 0-3-2Z"/><path d="M18 11c-1.5 0-3 .5-3 2 2 0 3 0 3-2Z"/></svg>
          </div>
          <h3 style="font-size: 24px; font-weight: 600; color: #111827; margin-bottom: 16px; line-height: 1.3; letter-spacing: -0.01em;">Press & Media</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.7; margin: 0; flex-grow: 1;">Media enquiries, interviews and announcements.</p>
          <div class="card-link" style="display: flex; align-items: center; color: #111827; font-weight: 600; font-size: 18px; margin-top: 32px; transition: transform 0.3s ease;">Contact <span style="margin-left: 8px;">→</span></div>
        </a>
      </div>
    </div>
  </section>

  <!-- SECTION 2: CONTACT FORM (Light Gray Background) -->
  <section id="form-section" style="background-color: #f8fafc; padding: 180px 5%; width: 100%; box-sizing: border-box; border-top: 1px solid rgba(0,0,0,0.03); border-bottom: 1px solid rgba(0,0,0,0.03);">
    <div style="max-width: 800px; margin: 0 auto;">
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 64px; letter-spacing: -0.03em; text-align: center;">Send a Message</h2>
      
      <form style="background: #ffffff; border: 1px solid rgba(0,0,0,0.05); border-radius: 32px; padding: 64px; box-shadow: 0 12px 48px rgba(0,0,0,0.03); display: flex; flex-direction: column; gap: 32px;">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 32px;">
          <!-- Name -->
          <div style="display: flex; flex-direction: column; gap: 8px;">
            <label style="font-size: 15px; font-weight: 600; color: #4B5563;">Name</label>
            <input type="text" placeholder="Your full name" style="width: 100%; padding: 18px 24px; border: 1px solid rgba(0,0,0,0.1); border-radius: 12px; font-size: 16px; color: #111827; background: #f8fafc; box-sizing: border-box; outline: none; transition: border-color 0.3s ease;" class="form-input">
          </div>
          <!-- Email -->
          <div style="display: flex; flex-direction: column; gap: 8px;">
            <label style="font-size: 15px; font-weight: 600; color: #4B5563;">Email</label>
            <input type="email" placeholder="you@company.com" style="width: 100%; padding: 18px 24px; border: 1px solid rgba(0,0,0,0.1); border-radius: 12px; font-size: 16px; color: #111827; background: #f8fafc; box-sizing: border-box; outline: none; transition: border-color 0.3s ease;" class="form-input">
          </div>
        </div>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 32px;">
          <!-- Company -->
          <div style="display: flex; flex-direction: column; gap: 8px;">
            <label style="font-size: 15px; font-weight: 600; color: #4B5563;">Company (optional)</label>
            <input type="text" placeholder="Your organization" style="width: 100%; padding: 18px 24px; border: 1px solid rgba(0,0,0,0.1); border-radius: 12px; font-size: 16px; color: #111827; background: #f8fafc; box-sizing: border-box; outline: none; transition: border-color 0.3s ease;" class="form-input">
          </div>
          <!-- Category -->
          <div style="display: flex; flex-direction: column; gap: 8px;">
            <label style="font-size: 15px; font-weight: 600; color: #4B5563;">Category</label>
            <div style="position: relative;">
                <select style="width: 100%; padding: 18px 24px; border: 1px solid rgba(0,0,0,0.1); border-radius: 12px; font-size: 16px; color: #111827; background: #f8fafc; box-sizing: border-box; outline: none; appearance: none; -webkit-appearance: none; transition: border-color 0.3s ease;" class="form-input">
                  <option value="support">Support</option>
                  <option value="sales">Sales</option>
                  <option value="partnership">Partnership</option>
                  <option value="press">Press</option>
                  <option value="other">Other</option>
                </select>
                <div style="position: absolute; right: 24px; top: 50%; transform: translateY(-50%); pointer-events: none; color: #94A3B8;">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>
                </div>
            </div>
          </div>
        </div>

        <!-- Subject -->
        <div style="display: flex; flex-direction: column; gap: 8px;">
          <label style="font-size: 15px; font-weight: 600; color: #4B5563;">Subject</label>
          <input type="text" placeholder="How can we help?" style="width: 100%; padding: 18px 24px; border: 1px solid rgba(0,0,0,0.1); border-radius: 12px; font-size: 16px; color: #111827; background: #f8fafc; box-sizing: border-box; outline: none; transition: border-color 0.3s ease;" class="form-input">
        </div>

        <!-- Message -->
        <div style="display: flex; flex-direction: column; gap: 8px;">
          <label style="font-size: 15px; font-weight: 600; color: #4B5563;">Message</label>
          <textarea placeholder="Tell us more about your enquiry..." rows="6" style="width: 100%; padding: 24px; border: 1px solid rgba(0,0,0,0.1); border-radius: 16px; font-size: 16px; color: #111827; background: #f8fafc; box-sizing: border-box; outline: none; resize: vertical; font-family: inherit; transition: border-color 0.3s ease;" class="form-input"></textarea>
        </div>

        <!-- Submit Button -->
        <button type="button" class="form-submit" style="background: #111827; color: #ffffff; padding: 20px 32px; border: none; border-radius: 100px; font-size: 18px; font-weight: 600; cursor: pointer; transition: all 0.3s ease; width: 100%; margin-top: 16px; display: flex; align-items: center; justify-content: center; gap: 12px;">
          Send Message
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m22 2-7 20-4-9-9-4Z"/><path d="M22 2 11 13"/></svg>
        </button>
      </form>
    </div>
  </section>

  <!-- SECTION 3: SELF-SERVE SUPPORT (White Background) -->
  <section style="background-color: #ffffff; padding: 180px 5%; width: 100%; box-sizing: border-box;">
    <div style="max-width: 1400px; margin: 0 auto;">
      <div style="text-align: center; margin-bottom: 80px; max-width: 680px; margin-left: auto; margin-right: auto;">
        <h2 style="font-size: 48px; font-weight: 600; color: #111827; margin-bottom: 24px; letter-spacing: -0.03em;">Find Answers Faster</h2>
        <p style="font-size: 20px; color: #4B5563; line-height: 1.7; margin: 0;">Many questions can be answered immediately through our knowledge resources.</p>
      </div>
      
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap: 40px; max-width: 1200px; margin: 0 auto;">
        <!-- FAQ Card -->
        <a href="/faqs" class="support-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 32px; padding: 64px; box-shadow: 0 12px 48px rgba(0,0,0,0.03); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="background: #f0f9ff; width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-bottom: 32px; color: #2563EB;">
            <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/></svg>
          </div>
          <h3 style="font-size: 32px; font-weight: 600; color: #111827; margin-bottom: 20px; line-height: 1.2; letter-spacing: -0.02em;">Frequently Asked Questions</h3>
          <p style="font-size: 20px; color: #4B5563; line-height: 1.7; margin: 0; flex-grow: 1;">Browse answers to common questions.</p>
          <div class="card-link" style="display: flex; align-items: center; color: #2563EB; font-weight: 600; font-size: 18px; margin-top: 40px; transition: transform 0.3s ease;">Open FAQ <span style="margin-left: 8px;">→</span></div>
        </a>
        <!-- University Card -->
        <a href="/nexmart-university" class="support-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 32px; padding: 64px; box-shadow: 0 12px 48px rgba(0,0,0,0.03); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="background: #f0f9ff; width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-bottom: 32px; color: #2563EB;">
            <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg>
          </div>
          <h3 style="font-size: 32px; font-weight: 600; color: #111827; margin-bottom: 20px; line-height: 1.2; letter-spacing: -0.02em;">Nexmart University</h3>
          <p style="font-size: 20px; color: #4B5563; line-height: 1.7; margin: 0; flex-grow: 1;">Explore tutorials and product guides.</p>
          <div class="card-link" style="display: flex; align-items: center; color: #2563EB; font-weight: 600; font-size: 18px; margin-top: 40px; transition: transform 0.3s ease;">Explore University <span style="margin-left: 8px;">→</span></div>
        </a>
      </div>
    </div>
  </section>

  <!-- SECTION 4: GLOBAL PRESENCE (Light Gray Background) -->
  <section style="background-color: #f8fafc; padding: 180px 5%; width: 100%; box-sizing: border-box; border-top: 1px solid rgba(0,0,0,0.03);">
    <div style="max-width: 1400px; margin: 0 auto;">
      <h2 style="font-size: 48px; font-weight: 600; color: #111827; margin-bottom: 80px; letter-spacing: -0.03em; text-align: center;">Global Presence</h2>
      
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 40px; max-width: 1200px; margin: 0 auto;">
        <!-- Location 1 -->
        <div class="location-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.05); border-radius: 24px; padding: 48px; box-shadow: 0 8px 32px rgba(0,0,0,0.03); display: flex; flex-direction: column; align-items: center; text-align: center; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="margin-bottom: 24px; color: #94A3B8;">
            <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>
          </div>
          <h3 style="font-size: 28px; font-weight: 600; color: #111827; margin-bottom: 12px; letter-spacing: -0.01em;">Nigeria</h3>
          <p style="font-size: 18px; color: #64748b; margin: 0;">Primary Commerce Operations</p>
        </div>
        <!-- Location 2 -->
        <div class="location-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.05); border-radius: 24px; padding: 48px; box-shadow: 0 8px 32px rgba(0,0,0,0.03); display: flex; flex-direction: column; align-items: center; text-align: center; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="margin-bottom: 24px; color: #94A3B8;">
            <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/></svg>
          </div>
          <h3 style="font-size: 28px; font-weight: 600; color: #111827; margin-bottom: 12px; letter-spacing: -0.01em;">Global</h3>
          <p style="font-size: 18px; color: #64748b; margin: 0;">International Partnerships</p>
        </div>
        <!-- Location 3 -->
        <div class="location-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.05); border-radius: 24px; padding: 48px; box-shadow: 0 8px 32px rgba(0,0,0,0.03); display: flex; flex-direction: column; align-items: center; text-align: center; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="margin-bottom: 24px; color: #94A3B8;">
            <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="14" x="2" y="3" rx="2"/><line x1="8" x2="16" y1="21" y2="21"/><line x1="12" x2="12" y1="17" y2="21"/></svg>
          </div>
          <h3 style="font-size: 28px; font-weight: 600; color: #111827; margin-bottom: 12px; letter-spacing: -0.01em;">Remote First</h3>
          <p style="font-size: 18px; color: #64748b; margin: 0;">Distributed AI Team</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 5: COMMUNITY (White Background) -->
  <section style="background-color: #ffffff; padding: 180px 5% 240px 5%; width: 100%; box-sizing: border-box;">
    <div style="max-width: 1400px; margin: 0 auto;">
      <div style="text-align: center; margin-bottom: 80px; max-width: 680px; margin-left: auto; margin-right: auto;">
        <h2 style="font-size: 48px; font-weight: 600; color: #111827; margin-bottom: 24px; letter-spacing: -0.03em;">Stay Connected</h2>
        <p style="font-size: 20px; color: #4B5563; line-height: 1.7; margin: 0;">Follow Nexmart as we build the future of Agentic Commerce.</p>
      </div>
      
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 24px; max-width: 1000px; margin: 0 auto;">
        <!-- Discord -->
        <a href="/discord-community" class="social-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 20px; padding: 40px; box-shadow: 0 8px 24px rgba(0,0,0,0.02); display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);">
          <div style="color: #111827; margin-bottom: 20px;">
            <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M18 10a1 1 0 0 1-1 1h-2a1 1 0 0 1-1-1v-2a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1Z"/><path d="M10 10a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1v-2a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1Z"/><path d="M21 16c-1.2-1-2.9-1.5-4.8-1.5-1.9 0-3.6.5-4.8 1.5M3 16c1.2-1 2.9-1.5 4.8-1.5 1.9 0 3.6.5 4.8 1.5"/><path d="M12 21a9 9 0 1 1 0-18 9 9 0 0 1 0 18Z"/></svg>
          </div>
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin: 0;">Discord Community</h3>
        </a>
        <!-- LinkedIn -->
        <a href="#" class="social-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 20px; padding: 40px; box-shadow: 0 8px 24px rgba(0,0,0,0.02); display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);">
          <div style="color: #111827; margin-bottom: 20px;">
            <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect width="4" height="12" x="2" y="9"/><circle cx="4" cy="4" r="2"/></svg>
          </div>
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin: 0;">LinkedIn</h3>
        </a>
        <!-- Twitter (X) -->
        <a href="#" class="social-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 20px; padding: 40px; box-shadow: 0 8px 24px rgba(0,0,0,0.02); display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);">
          <div style="color: #111827; margin-bottom: 20px;">
            <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="m3 21 1.9-5.7a8.5 8.5 0 1 1 3.8 3.8z"/></svg>
          </div>
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin: 0;">X (Twitter)</h3>
        </a>
        <!-- Blog -->
        <a href="/blog" class="social-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 20px; padding: 40px; box-shadow: 0 8px 24px rgba(0,0,0,0.02); display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);">
          <div style="color: #111827; margin-bottom: 20px;">
            <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>
          </div>
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin: 0;">Blog</h3>
        </a>
      </div>
    </div>
  </section>

  <style>
    .contact-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 24px 48px rgba(0,0,0,0.06) !important;
        border-color: rgba(0,0,0,0.1) !important;
    }
    .contact-card:hover .card-link {
        transform: translateX(8px);
    }
    .support-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 24px 48px rgba(37,99,235,0.08) !important;
        border-color: rgba(37,99,235,0.2) !important;
    }
    .support-card:hover .card-link {
        transform: translateX(8px);
    }
    .location-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 24px 48px rgba(0,0,0,0.06) !important;
        border-color: rgba(0,0,0,0.1) !important;
    }
    .social-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 16px 32px rgba(0,0,0,0.04) !important;
        border-color: rgba(0,0,0,0.1) !important;
        background: #f8fafc !important;
    }
    .form-input:focus {
        border-color: #111827 !important;
        background: #ffffff !important;
    }
    .form-submit:hover {
        background: #374151 !important;
        transform: translateY(-2px);
    }
    
    @media (max-width: 900px) {
        .semantic-contact-wrapper section {
            padding: 100px 5% !important;
        }
        .semantic-contact-wrapper h2 {
            font-size: 40px !important;
        }
        .semantic-contact-wrapper .contact-card, .support-card, .location-card {
            padding: 40px !important;
        }
    }
    @media (max-width: 600px) {
        .semantic-contact-wrapper section {
            padding: 80px 5% !important;
        }
        .semantic-contact-wrapper h2 {
            font-size: 32px !important;
        }
        .semantic-contact-wrapper form {
            padding: 32px !important;
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
        new_section = bs4.BeautifulSoup(contact_html, 'html.parser')
        section_to_replace.replace_with(new_section)

# Make sure CTA section has white background to match the final section (Community is white)
sections = soup.find_all('section')
if len(sections) > 1:
    cta = sections[-1]
    cta['style'] = cta.get('style', '') + '; background-color: #ffffff;'
    # Darken CTA text if it was white
    for h in cta.find_all(['h2', 'h3']):
        h['style'] = h.get('style', '') + '; color: #111827 !important;'
    for p in cta.find_all('p'):
        p['style'] = p.get('style', '') + '; color: #4B5563 !important;'

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Successfully built the Contact page.")
