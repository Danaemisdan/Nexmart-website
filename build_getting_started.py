import bs4

with open('getting-started.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = bs4.BeautifulSoup(html, 'html.parser')

# 1. Update Title
if soup.title:
    soup.title.string = "Nexmart - Getting Started"

# 2. Build Getting Started Content HTML
getting_started_html = """
<div class="semantic-getting-started-wrapper" style="width: 100%; display: flex; flex-direction: column; font-family: 'Inter', system-ui, -apple-system, sans-serif;">
  
  <!-- HERO SECTION -->
  <section style="background-color: #ffffff; padding: 160px 5% 100px 5%; width: 100%; box-sizing: border-box; text-align: center;">
    <div style="max-width: 1000px; margin: 0 auto;">
      <h1 style="font-size: 64px; font-weight: 700; color: #111827; margin-bottom: 24px; letter-spacing: -0.04em; line-height: 1.1;">Getting Started with Nexmart</h1>
      <p style="font-size: 22px; color: #4B5563; line-height: 1.6; margin: 0 auto; max-width: 700px;">Everything you need to begin using the world's first Agentic Commerce platform. Learn how AI shops, researches, compares, and purchases on your behalf.</p>
    </div>
  </section>

  <!-- SECTION 1: YOUR FIRST JOURNEY (Light Gray) -->
  <section style="background-color: #f8fafc; padding: 140px 5%; width: 100%; box-sizing: border-box; border-top: 1px solid rgba(0,0,0,0.03);">
    <div style="max-width: 1400px; margin: 0 auto;">
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 64px; letter-spacing: -0.03em; text-align: center;">Your First Journey</h2>
      
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 32px;">
        <!-- Card 1 -->
        <div class="journey-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 24px; padding: 48px 32px; box-shadow: 0 12px 32px rgba(0,0,0,0.02); display: flex; flex-direction: column; align-items: center; text-align: center; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="background: rgba(37,99,235,0.08); color: #2563EB; width: 64px; height: 64px; border-radius: 20px; display: flex; align-items: center; justify-content: center; margin-bottom: 32px; font-size: 24px; font-weight: 700;">1</div>
          <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 16px;">Create Your Account</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Set up your Nexmart profile and personalize your shopping preferences.</p>
        </div>
        <!-- Card 2 -->
        <div class="journey-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 24px; padding: 48px 32px; box-shadow: 0 12px 32px rgba(0,0,0,0.02); display: flex; flex-direction: column; align-items: center; text-align: center; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="background: rgba(37,99,235,0.08); color: #2563EB; width: 64px; height: 64px; border-radius: 20px; display: flex; align-items: center; justify-content: center; margin-bottom: 32px; font-size: 24px; font-weight: 700;">2</div>
          <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 16px;">Describe Your Intent</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Instead of searching products, simply tell Nexmart exactly what you need.</p>
        </div>
        <!-- Card 3 -->
        <div class="journey-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 24px; padding: 48px 32px; box-shadow: 0 12px 32px rgba(0,0,0,0.02); display: flex; flex-direction: column; align-items: center; text-align: center; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="background: rgba(37,99,235,0.08); color: #2563EB; width: 64px; height: 64px; border-radius: 20px; display: flex; align-items: center; justify-content: center; margin-bottom: 32px; font-size: 24px; font-weight: 700;">3</div>
          <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 16px;">Review AI Recommendations</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Your AI agents research the market, compare products, and present the best options.</p>
        </div>
        <!-- Card 4 -->
        <div class="journey-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 24px; padding: 48px 32px; box-shadow: 0 12px 32px rgba(0,0,0,0.02); display: flex; flex-direction: column; align-items: center; text-align: center; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="background: rgba(37,99,235,0.08); color: #2563EB; width: 64px; height: 64px; border-radius: 20px; display: flex; align-items: center; justify-content: center; margin-bottom: 32px; font-size: 24px; font-weight: 700;">4</div>
          <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 16px;">Approve & Purchase</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Approve the recommendation and let Nexmart complete the purchase for you.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 2: HOW AGENTIC COMMERCE WORKS (White) -->
  <section style="background-color: #ffffff; padding: 160px 5%; width: 100%; box-sizing: border-box;">
    <div style="max-width: 1400px; margin: 0 auto; text-align: center;">
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 80px; letter-spacing: -0.03em;">How Agentic Commerce Works</h2>
      
      <div class="timeline-container" style="display: flex; justify-content: space-between; position: relative;">
        <div class="timeline-line" style="position: absolute; top: 40px; left: 10%; right: 10%; height: 2px; background: rgba(37,99,235,0.1); z-index: 0;"></div>
        
        <div class="timeline-step" style="position: relative; z-index: 1; flex: 1; padding: 0 16px;">
          <div style="background: #ffffff; border: 2px solid #2563EB; width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 24px auto; color: #2563EB;">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
          </div>
          <h4 style="font-size: 18px; font-weight: 600; color: #111827; margin-bottom: 8px;">Intent</h4>
          <p style="font-size: 14px; color: #4B5563; line-height: 1.5; margin: 0;">You describe exactly what you are looking for.</p>
        </div>

        <div class="timeline-step" style="position: relative; z-index: 1; flex: 1; padding: 0 16px;">
          <div style="background: #ffffff; border: 2px solid #2563EB; width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 24px auto; color: #2563EB;">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>
          </div>
          <h4 style="font-size: 18px; font-weight: 600; color: #111827; margin-bottom: 8px;">Research</h4>
          <p style="font-size: 14px; color: #4B5563; line-height: 1.5; margin: 0;">AI agents scan the market for available options.</p>
        </div>

        <div class="timeline-step" style="position: relative; z-index: 1; flex: 1; padding: 0 16px;">
          <div style="background: #ffffff; border: 2px solid #2563EB; width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 24px auto; color: #2563EB;">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2v20"/><path d="m17 5 5 5-5 5"/><path d="m7 19-5-5 5-5"/></svg>
          </div>
          <h4 style="font-size: 18px; font-weight: 600; color: #111827; margin-bottom: 8px;">Comparison</h4>
          <p style="font-size: 14px; color: #4B5563; line-height: 1.5; margin: 0;">Options are evaluated based on your criteria.</p>
        </div>

        <div class="timeline-step" style="position: relative; z-index: 1; flex: 1; padding: 0 16px;">
          <div style="background: #ffffff; border: 2px solid #2563EB; width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 24px auto; color: #2563EB;">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><polyline points="9 11 12 14 22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>
          </div>
          <h4 style="font-size: 18px; font-weight: 600; color: #111827; margin-bottom: 8px;">Decision</h4>
          <p style="font-size: 14px; color: #4B5563; line-height: 1.5; margin: 0;">The best match is presented for your approval.</p>
        </div>

        <div class="timeline-step" style="position: relative; z-index: 1; flex: 1; padding: 0 16px;">
          <div style="background: #ffffff; border: 2px solid #2563EB; width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 24px auto; color: #2563EB;">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"/><path d="M3 6h18"/><path d="M16 10a4 4 0 0 1-8 0"/></svg>
          </div>
          <h4 style="font-size: 18px; font-weight: 600; color: #111827; margin-bottom: 8px;">Purchase</h4>
          <p style="font-size: 14px; color: #4B5563; line-height: 1.5; margin: 0;">Nexmart safely executes the transaction.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 3: YOUR FIRST AI PROMPT (Blue Tint) -->
  <section style="background-color: #eff6ff; padding: 140px 5%; width: 100%; box-sizing: border-box;">
    <div style="max-width: 1000px; margin: 0 auto; display: flex; flex-direction: column; align-items: center;">
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 48px; letter-spacing: -0.03em; text-align: center;">Your First AI Prompt</h2>
      
      <div style="background: #ffffff; border-radius: 32px; padding: 48px; width: 100%; box-shadow: 0 24px 64px rgba(37,99,235,0.1); margin-bottom: 48px; border: 1px solid rgba(37,99,235,0.1);">
        <div style="font-size: 14px; font-weight: 700; color: #2563EB; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 16px;">Example Prompt</div>
        <p style="font-size: 28px; color: #111827; line-height: 1.5; font-weight: 500; margin: 0;">"Find me a waterproof hiking backpack under $150 with at least 4.5-star reviews that can be delivered this week."</p>
      </div>

      <div style="width: 100%; max-width: 800px; background: rgba(255,255,255,0.6); backdrop-filter: blur(10px); border-radius: 24px; padding: 40px; border: 1px solid rgba(0,0,0,0.05);">
        <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin-bottom: 24px;">Why this works:</h3>
        <ul style="list-style: none; padding: 0; margin: 0; display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px;">
          <li style="display: flex; align-items: center; gap: 12px; color: #4B5563; font-size: 16px;">
            <div style="color: #2563EB;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg></div>
            Budget specified
          </li>
          <li style="display: flex; align-items: center; gap: 12px; color: #4B5563; font-size: 16px;">
            <div style="color: #2563EB;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg></div>
            Product clearly defined
          </li>
          <li style="display: flex; align-items: center; gap: 12px; color: #4B5563; font-size: 16px;">
            <div style="color: #2563EB;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg></div>
            Delivery expectation included
          </li>
          <li style="display: flex; align-items: center; gap: 12px; color: #4B5563; font-size: 16px;">
            <div style="color: #2563EB;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg></div>
            Quality requirement included
          </li>
        </ul>
      </div>
    </div>
  </section>

  <!-- SECTION 4: BEST PRACTICES (White) -->
  <section style="background-color: #ffffff; padding: 160px 5%; width: 100%; box-sizing: border-box;">
    <div style="max-width: 1400px; margin: 0 auto;">
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 64px; letter-spacing: -0.03em; text-align: center;">Best Practices</h2>
      
      <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 24px;">
        <div class="practice-card" style="background: #f8fafc; border: 1px solid rgba(0,0,0,0.04); border-radius: 20px; padding: 32px; display: flex; align-items: center; gap: 24px; transition: all 0.3s ease;">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 48px; height: 48px; border-radius: 12px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg></div>
          <h3 style="font-size: 18px; font-weight: 600; color: #111827; margin: 0;">Always specify your budget.</h3>
        </div>
        <div class="practice-card" style="background: #f8fafc; border: 1px solid rgba(0,0,0,0.04); border-radius: 20px; padding: 32px; display: flex; align-items: center; gap: 24px; transition: all 0.3s ease;">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 48px; height: 48px; border-radius: 12px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg></div>
          <h3 style="font-size: 18px; font-weight: 600; color: #111827; margin: 0;">Mention preferred brands if you have any.</h3>
        </div>
        <div class="practice-card" style="background: #f8fafc; border: 1px solid rgba(0,0,0,0.04); border-radius: 20px; padding: 32px; display: flex; align-items: center; gap: 24px; transition: all 0.3s ease;">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 48px; height: 48px; border-radius: 12px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg></div>
          <h3 style="font-size: 18px; font-weight: 600; color: #111827; margin: 0;">Include delivery expectations.</h3>
        </div>
        <div class="practice-card" style="background: #f8fafc; border: 1px solid rgba(0,0,0,0.04); border-radius: 20px; padding: 32px; display: flex; align-items: center; gap: 24px; transition: all 0.3s ease;">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 48px; height: 48px; border-radius: 12px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg></div>
          <h3 style="font-size: 18px; font-weight: 600; color: #111827; margin: 0;">Use natural language.</h3>
        </div>
        <div class="practice-card" style="background: #f8fafc; border: 1px solid rgba(0,0,0,0.04); border-radius: 20px; padding: 32px; display: flex; align-items: center; gap: 24px; transition: all 0.3s ease;">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 48px; height: 48px; border-radius: 12px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg></div>
          <h3 style="font-size: 18px; font-weight: 600; color: #111827; margin: 0;">Compare multiple options.</h3>
        </div>
        <div class="practice-card" style="background: #f8fafc; border: 1px solid rgba(0,0,0,0.04); border-radius: 20px; padding: 32px; display: flex; align-items: center; gap: 24px; transition: all 0.3s ease;">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 48px; height: 48px; border-radius: 12px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg></div>
          <h3 style="font-size: 18px; font-weight: 600; color: #111827; margin: 0;">Save successful prompts.</h3>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 5: WHAT HAPPENS NEXT? (Light Gray) -->
  <section style="background-color: #f8fafc; padding: 160px 5%; width: 100%; box-sizing: border-box; border-top: 1px solid rgba(0,0,0,0.03);">
    <div style="max-width: 1400px; margin: 0 auto;">
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 64px; letter-spacing: -0.03em; text-align: center;">What Happens Next?</h2>
      
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 32px;">
        <a href="nexmart-university.html" class="next-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px; box-shadow: 0 8px 24px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.3s ease;">
          <h3 style="font-size: 24px; font-weight: 600; color: #111827; margin: 0 0 16px 0;">Explore Nexmart University</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.6; margin: 0 0 32px 0; flex-grow: 1;">Continue learning advanced workflows.</p>
          <div style="color: #2563EB; font-weight: 600; display: flex; align-items: center; gap: 8px;">Explore <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg></div>
        </a>
        <a href="agentic-commerce-101.html" class="next-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px; box-shadow: 0 8px 24px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.3s ease;">
          <h3 style="font-size: 24px; font-weight: 600; color: #111827; margin: 0 0 16px 0;">Read Agentic Commerce 101</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.6; margin: 0 0 32px 0; flex-grow: 1;">Understand the philosophy behind AI shopping.</p>
          <div style="color: #2563EB; font-weight: 600; display: flex; align-items: center; gap: 8px;">Read More <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg></div>
        </a>
        <a href="mastering-ai-prompts.html" class="next-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px; box-shadow: 0 8px 24px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.3s ease;">
          <h3 style="font-size: 24px; font-weight: 600; color: #111827; margin: 0 0 16px 0;">Master AI Prompts</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.6; margin: 0 0 32px 0; flex-grow: 1;">Learn how to communicate effectively with your AI agents.</p>
          <div style="color: #2563EB; font-weight: 600; display: flex; align-items: center; gap: 8px;">Learn How <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg></div>
        </a>
      </div>
    </div>
  </section>

  <!-- FINAL CTA (White) -->
  <section style="background-color: #ffffff; padding: 180px 5% 240px 5%; width: 100%; box-sizing: border-box;">
    <div style="max-width: 1000px; margin: 0 auto; text-align: center;">
      <h2 style="font-size: 48px; font-weight: 600; color: #111827; margin-bottom: 24px; letter-spacing: -0.03em;">Ready to Start Shopping Smarter?</h2>
      <p style="font-size: 22px; color: #4B5563; line-height: 1.7; margin: 0 auto 48px auto;">Your AI shopping assistant is ready whenever you are.</p>
      
      <div style="display: flex; gap: 16px; justify-content: center; flex-wrap: wrap;">
        <a href="#" class="btn-primary" style="text-decoration: none; background: #2563EB; color: #ffffff; padding: 18px 40px; border-radius: 100px; font-size: 18px; font-weight: 600; transition: all 0.3s ease; display: inline-flex; align-items: center; gap: 12px;">
            Start Shopping With AI
        </a>
        <a href="nexmart-university.html" class="btn-secondary" style="text-decoration: none; background: #f8fafc; border: 1px solid rgba(0,0,0,0.1); color: #111827; padding: 18px 40px; border-radius: 100px; font-size: 18px; font-weight: 600; transition: all 0.3s ease;">
            Explore Nexmart University
        </a>
      </div>
    </div>
  </section>

  <style>
    .journey-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 24px 48px rgba(0,0,0,0.06) !important;
        border-color: rgba(37,99,235,0.2) !important;
    }
    .practice-card:hover {
        transform: translateY(-4px);
        background: #ffffff !important;
        box-shadow: 0 12px 24px rgba(0,0,0,0.04) !important;
        border-color: rgba(37,99,235,0.2) !important;
    }
    .next-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 24px 48px rgba(37,99,235,0.08) !important;
        border-color: rgba(37,99,235,0.3) !important;
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
    
    @media (max-width: 991px) {
        .semantic-getting-started-wrapper section {
            padding: 100px 5% !important;
        }
        .semantic-getting-started-wrapper h1 {
            font-size: 48px !important;
        }
        .semantic-getting-started-wrapper h2 {
            font-size: 32px !important;
        }
        .timeline-container {
            flex-direction: column !important;
            gap: 40px !important;
        }
        .timeline-line {
            display: none !important;
        }
        .practice-card {
            grid-column: span 2 !important;
        }
    }
    @media (max-width: 600px) {
        .semantic-getting-started-wrapper section {
            padding: 80px 5% !important;
        }
        .semantic-getting-started-wrapper h1 {
            font-size: 40px !important;
        }
        .semantic-getting-started-wrapper .btn-primary, .semantic-getting-started-wrapper .btn-secondary {
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
    # Depending on how the placeholder was generated, it might be inside semantic-placeholder-wrapper
    wrapper = placeholder.find_parent('div', class_='semantic-placeholder-wrapper')
    if wrapper:
        new_section = bs4.BeautifulSoup(getting_started_html, 'html.parser')
        wrapper.replace_with(new_section)

with open('getting-started.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Successfully built the Getting Started page.")
