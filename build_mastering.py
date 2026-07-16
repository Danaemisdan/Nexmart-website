import bs4

with open('mastering-ai-prompts.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = bs4.BeautifulSoup(html, 'html.parser')

# 1. Update Title
if soup.title:
    soup.title.string = "Nexmart - Mastering AI Prompts"

# 2. Build Mastering AI Prompts Content HTML
mastering_html = """
<div class="semantic-mastering-wrapper" style="width: 100%; display: flex; flex-direction: column; font-family: 'Inter', system-ui, -apple-system, sans-serif;">
  
  <!-- HERO SECTION -->
  <section style="background-color: #ffffff; padding: 160px 5% 100px 5%; width: 100%; box-sizing: border-box; text-align: center;">
    <div style="max-width: 1000px; margin: 0 auto;">
      <h1 style="font-size: 64px; font-weight: 700; color: #111827; margin-bottom: 24px; letter-spacing: -0.04em; line-height: 1.1;">Mastering AI Prompts</h1>
      <p style="font-size: 22px; color: #4B5563; line-height: 1.6; margin: 0 auto; max-width: 800px;">The better you communicate your intent, the better your AI shopping agent performs. Learn how to write prompts that produce faster, smarter, and more accurate results.</p>
    </div>
  </section>

  <!-- SECTION 1: WHY PROMPTS MATTER (Light Gray) -->
  <section style="background-color: #f8fafc; padding: 140px 5%; width: 100%; box-sizing: border-box; border-top: 1px solid rgba(0,0,0,0.03);">
    <div style="max-width: 1400px; margin: 0 auto; text-align: center;">
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 24px; letter-spacing: -0.03em;">Intent Is Everything</h2>
      <p style="font-size: 20px; color: #4B5563; line-height: 1.6; margin: 0 auto 64px auto; max-width: 800px;">Unlike traditional search engines, Nexmart understands natural language. The more context you provide, the more precisely your AI agent can research, compare, and recommend products.</p>
      
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 32px; text-align: left;">
        <div class="matter-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 24px; padding: 48px 32px; box-shadow: 0 12px 32px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 56px; height: 56px; border-radius: 16px; display: flex; align-items: center; justify-content: center; margin-bottom: 24px;"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M22 12A10 10 0 1 1 12 2a10 10 0 0 1 10 10z"/><circle cx="12" cy="12" r="3"/></svg></div>
          <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 12px;">Clear Intent</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Tell the AI exactly what you're trying to achieve.</p>
        </div>
        <div class="matter-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 24px; padding: 48px 32px; box-shadow: 0 12px 32px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 56px; height: 56px; border-radius: 16px; display: flex; align-items: center; justify-content: center; margin-bottom: 24px;"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M14 2H6a2 2 0 0 0-2 2v16c0 1.1.9 2 2 2h12a2 2 0 0 0 2-2V8l-6-6z"/><path d="M14 3v5h5"/><path d="M16 13H8"/><path d="M16 17H8"/><path d="M10 9H8"/></svg></div>
          <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 12px;">Context</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Include details like budget, usage, preferences, and timing.</p>
        </div>
        <div class="matter-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 24px; padding: 48px 32px; box-shadow: 0 12px 32px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 56px; height: 56px; border-radius: 16px; display: flex; align-items: center; justify-content: center; margin-bottom: 24px;"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect width="18" height="18" x="3" y="3" rx="2"/><path d="M9 3v18"/><path d="M15 3v18"/></svg></div>
          <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 12px;">Constraints</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Mention brands, delivery dates, colors, sizes, or anything important.</p>
        </div>
        <div class="matter-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 24px; padding: 48px 32px; box-shadow: 0 12px 32px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 56px; height: 56px; border-radius: 16px; display: flex; align-items: center; justify-content: center; margin-bottom: 24px;"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="m22 2-7 20-4-9-9-4Z"/><path d="M22 2 11 13"/></svg></div>
          <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 12px;">Outcome</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Well-written prompts produce dramatically better recommendations.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 2: PROMPT FORMULA (White) -->
  <section style="background-color: #ffffff; padding: 160px 5%; width: 100%; box-sizing: border-box;">
    <div style="max-width: 1400px; margin: 0 auto; text-align: center;">
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 80px; letter-spacing: -0.03em;">The Perfect Prompt Formula</h2>
      
      <div class="formula-timeline" style="display: flex; justify-content: space-between; position: relative;">
        <div class="timeline-line" style="position: absolute; top: 32px; left: 10%; right: 10%; height: 2px; background: rgba(37,99,235,0.1); z-index: 0;"></div>
        
        <div class="formula-step" style="position: relative; z-index: 1; flex: 1; padding: 0 16px;">
          <div style="background: #ffffff; border: 2px solid #2563EB; width: 64px; height: 64px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 24px auto; color: #2563EB; font-weight: 700; font-size: 20px;">1</div>
          <h4 style="font-size: 18px; font-weight: 600; color: #111827; margin-bottom: 8px;">Need</h4>
          <p style="font-size: 14px; color: #4B5563; line-height: 1.5; margin: 0;">What you are looking for.</p>
        </div>

        <div class="formula-step" style="position: relative; z-index: 1; flex: 1; padding: 0 16px;">
          <div style="background: #ffffff; border: 2px solid #2563EB; width: 64px; height: 64px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 24px auto; color: #2563EB; font-weight: 700; font-size: 20px;">2</div>
          <h4 style="font-size: 18px; font-weight: 600; color: #111827; margin-bottom: 8px;">Budget</h4>
          <p style="font-size: 14px; color: #4B5563; line-height: 1.5; margin: 0;">How much you want to spend.</p>
        </div>

        <div class="formula-step" style="position: relative; z-index: 1; flex: 1; padding: 0 16px;">
          <div style="background: #ffffff; border: 2px solid #2563EB; width: 64px; height: 64px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 24px auto; color: #2563EB; font-weight: 700; font-size: 20px;">3</div>
          <h4 style="font-size: 18px; font-weight: 600; color: #111827; margin-bottom: 8px;">Preferences</h4>
          <p style="font-size: 14px; color: #4B5563; line-height: 1.5; margin: 0;">Style, brand, or quality goals.</p>
        </div>

        <div class="formula-step" style="position: relative; z-index: 1; flex: 1; padding: 0 16px;">
          <div style="background: #ffffff; border: 2px solid #2563EB; width: 64px; height: 64px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 24px auto; color: #2563EB; font-weight: 700; font-size: 20px;">4</div>
          <h4 style="font-size: 18px; font-weight: 600; color: #111827; margin-bottom: 8px;">Timeline</h4>
          <p style="font-size: 14px; color: #4B5563; line-height: 1.5; margin: 0;">When you need it delivered.</p>
        </div>

        <div class="formula-step" style="position: relative; z-index: 1; flex: 1; padding: 0 16px;">
          <div style="background: #ffffff; border: 2px solid #2563EB; width: 64px; height: 64px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 24px auto; color: #2563EB; font-weight: 700; font-size: 20px;">5</div>
          <h4 style="font-size: 18px; font-weight: 600; color: #111827; margin-bottom: 8px;">Special Requirements</h4>
          <p style="font-size: 14px; color: #4B5563; line-height: 1.5; margin: 0;">Must-have features.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 3: EXAMPLES (Light Gray) -->
  <section style="background-color: #f8fafc; padding: 160px 5%; width: 100%; box-sizing: border-box; border-top: 1px solid rgba(0,0,0,0.03);">
    <div style="max-width: 1400px; margin: 0 auto;">
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 64px; letter-spacing: -0.03em; text-align: center;">Good Prompts vs Better Prompts</h2>
      
      <div style="display: grid; grid-template-columns: 1fr; gap: 40px;">
        
        <!-- Example 1 -->
        <div class="compare-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.05); border-radius: 32px; padding: 48px; box-shadow: 0 16px 40px rgba(0,0,0,0.02); display: grid; grid-template-columns: 1fr 1fr; gap: 40px; transition: all 0.3s ease;">
          <div style="background: #fef2f2; border: 1px solid rgba(239,68,68,0.2); border-radius: 20px; padding: 32px;">
            <div style="font-size: 14px; font-weight: 700; color: #ef4444; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 16px; display: flex; align-items: center; gap: 8px;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg> Poor Prompt</div>
            <div style="font-size: 20px; color: #111827; line-height: 1.5;">"Need a laptop."</div>
          </div>
          <div style="background: #eff6ff; border: 1px solid rgba(37,99,235,0.2); border-radius: 20px; padding: 32px;">
            <div style="font-size: 14px; font-weight: 700; color: #2563EB; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 16px; display: flex; align-items: center; gap: 8px;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> Better Prompt</div>
            <div style="font-size: 20px; color: #111827; line-height: 1.5; font-weight: 500;">"Find me a lightweight Windows laptop under $900 for programming and travel."</div>
          </div>
        </div>

        <!-- Example 2 -->
        <div class="compare-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.05); border-radius: 32px; padding: 48px; box-shadow: 0 16px 40px rgba(0,0,0,0.02); display: grid; grid-template-columns: 1fr 1fr; gap: 40px; transition: all 0.3s ease;">
          <div style="background: #fef2f2; border: 1px solid rgba(239,68,68,0.2); border-radius: 20px; padding: 32px;">
            <div style="font-size: 14px; font-weight: 700; color: #ef4444; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 16px; display: flex; align-items: center; gap: 8px;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg> Poor Prompt</div>
            <div style="font-size: 20px; color: #111827; line-height: 1.5;">"I need shoes."</div>
          </div>
          <div style="background: #eff6ff; border: 1px solid rgba(37,99,235,0.2); border-radius: 20px; padding: 32px;">
            <div style="font-size: 14px; font-weight: 700; color: #2563EB; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 16px; display: flex; align-items: center; gap: 8px;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> Better Prompt</div>
            <div style="font-size: 20px; color: #111827; line-height: 1.5; font-weight: 500;">"Find waterproof hiking boots under $180 with excellent ankle support."</div>
          </div>
        </div>

        <!-- Example 3 -->
        <div class="compare-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.05); border-radius: 32px; padding: 48px; box-shadow: 0 16px 40px rgba(0,0,0,0.02); display: grid; grid-template-columns: 1fr 1fr; gap: 40px; transition: all 0.3s ease;">
          <div style="background: #fef2f2; border: 1px solid rgba(239,68,68,0.2); border-radius: 20px; padding: 32px;">
            <div style="font-size: 14px; font-weight: 700; color: #ef4444; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 16px; display: flex; align-items: center; gap: 8px;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg> Poor Prompt</div>
            <div style="font-size: 20px; color: #111827; line-height: 1.5;">"Buy groceries."</div>
          </div>
          <div style="background: #eff6ff; border: 1px solid rgba(37,99,235,0.2); border-radius: 20px; padding: 32px;">
            <div style="font-size: 14px; font-weight: 700; color: #2563EB; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 16px; display: flex; align-items: center; gap: 8px;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> Better Prompt</div>
            <div style="font-size: 20px; color: #111827; line-height: 1.5; font-weight: 500;">"Build a healthy grocery basket for a vegetarian family of four with a budget of $120."</div>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- SECTION 4: PROMPT LIBRARY (White) -->
  <section style="background-color: #ffffff; padding: 160px 5%; width: 100%; box-sizing: border-box;">
    <div style="max-width: 1400px; margin: 0 auto;">
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 64px; letter-spacing: -0.03em; text-align: center;">Ready-to-Use Prompt Templates</h2>
      
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 32px;">
        <!-- Card 1 -->
        <div class="library-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.08); border-radius: 24px; padding: 40px; display: flex; flex-direction: column; transition: all 0.3s ease;">
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin-bottom: 16px;">Shopping</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.6; margin: 0 0 24px 0; font-style: italic; flex-grow: 1;">"Find me the best rated noise-cancelling headphones under $200 that ship by Friday."</p>
          <div style="color: #2563EB; font-weight: 600; display: inline-flex; align-items: center; gap: 8px; cursor: pointer;">Copy Prompt <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg></div>
        </div>
        <!-- Card 2 -->
        <div class="library-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.08); border-radius: 24px; padding: 40px; display: flex; flex-direction: column; transition: all 0.3s ease;">
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin-bottom: 16px;">Travel</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.6; margin: 0 0 24px 0; font-style: italic; flex-grow: 1;">"Plan a week-long beach vacation to Mexico for two adults under $3,000 total."</p>
          <div style="color: #2563EB; font-weight: 600; display: inline-flex; align-items: center; gap: 8px; cursor: pointer;">Copy Prompt <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg></div>
        </div>
        <!-- Card 3 -->
        <div class="library-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.08); border-radius: 24px; padding: 40px; display: flex; flex-direction: column; transition: all 0.3s ease;">
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin-bottom: 16px;">Home</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.6; margin: 0 0 24px 0; font-style: italic; flex-grow: 1;">"Compare modern minimalist coffee tables made of real wood under $400."</p>
          <div style="color: #2563EB; font-weight: 600; display: inline-flex; align-items: center; gap: 8px; cursor: pointer;">Copy Prompt <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg></div>
        </div>
        <!-- Card 4 -->
        <div class="library-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.08); border-radius: 24px; padding: 40px; display: flex; flex-direction: column; transition: all 0.3s ease;">
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin-bottom: 16px;">Business</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.6; margin: 0 0 24px 0; font-style: italic; flex-grow: 1;">"Research ergonomic office chairs for tall people with lower back support."</p>
          <div style="color: #2563EB; font-weight: 600; display: inline-flex; align-items: center; gap: 8px; cursor: pointer;">Copy Prompt <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg></div>
        </div>
        <!-- Card 5 -->
        <div class="library-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.08); border-radius: 24px; padding: 40px; display: flex; flex-direction: column; transition: all 0.3s ease;">
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin-bottom: 16px;">Technology</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.6; margin: 0 0 24px 0; font-style: italic; flex-grow: 1;">"Recommend a beginner-friendly mirrorless camera for vlogging under $800."</p>
          <div style="color: #2563EB; font-weight: 600; display: inline-flex; align-items: center; gap: 8px; cursor: pointer;">Copy Prompt <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg></div>
        </div>
        <!-- Card 6 -->
        <div class="library-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.08); border-radius: 24px; padding: 40px; display: flex; flex-direction: column; transition: all 0.3s ease;">
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin-bottom: 16px;">Health</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.6; margin: 0 0 24px 0; font-style: italic; flex-grow: 1;">"Help me choose the best organic vegan protein powder without artificial sweeteners."</p>
          <div style="color: #2563EB; font-weight: 600; display: inline-flex; align-items: center; gap: 8px; cursor: pointer;">Copy Prompt <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg></div>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 5: COMMON MISTAKES (Light Gray) -->
  <section style="background-color: #f8fafc; padding: 160px 5%; width: 100%; box-sizing: border-box; border-top: 1px solid rgba(0,0,0,0.03);">
    <div style="max-width: 1400px; margin: 0 auto;">
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 64px; letter-spacing: -0.03em; text-align: center;">Avoid These Mistakes</h2>
      
      <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 24px;">
        <div class="mistake-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 20px; padding: 40px; display: flex; align-items: flex-start; gap: 24px; transition: all 0.3s ease;">
          <div style="color: #ef4444; margin-top: 4px;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="15" x2="9" y1="9" y2="15"/><line x1="9" x2="15" y1="9" y2="15"/></svg></div>
          <div>
            <h3 style="font-size: 18px; font-weight: 600; color: #111827; margin: 0 0 8px 0;">Being Too Vague</h3>
            <p style="font-size: 15px; color: #4B5563; line-height: 1.6; margin: 0;">Without specifics, the AI must guess your preferences.</p>
          </div>
        </div>
        <div class="mistake-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 20px; padding: 40px; display: flex; align-items: flex-start; gap: 24px; transition: all 0.3s ease;">
          <div style="color: #ef4444; margin-top: 4px;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="15" x2="9" y1="9" y2="15"/><line x1="9" x2="15" y1="9" y2="15"/></svg></div>
          <div>
            <h3 style="font-size: 18px; font-weight: 600; color: #111827; margin: 0 0 8px 0;">Missing Budget</h3>
            <p style="font-size: 15px; color: #4B5563; line-height: 1.6; margin: 0;">The AI cannot filter effectively without knowing your price range.</p>
          </div>
        </div>
        <div class="mistake-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 20px; padding: 40px; display: flex; align-items: flex-start; gap: 24px; transition: all 0.3s ease;">
          <div style="color: #ef4444; margin-top: 4px;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="15" x2="9" y1="9" y2="15"/><line x1="9" x2="15" y1="9" y2="15"/></svg></div>
          <div>
            <h3 style="font-size: 18px; font-weight: 600; color: #111827; margin: 0 0 8px 0;">Ignoring Delivery Time</h3>
            <p style="font-size: 15px; color: #4B5563; line-height: 1.6; margin: 0;">You might be recommended a perfect product that arrives too late.</p>
          </div>
        </div>
        <div class="mistake-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 20px; padding: 40px; display: flex; align-items: flex-start; gap: 24px; transition: all 0.3s ease;">
          <div style="color: #ef4444; margin-top: 4px;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="15" x2="9" y1="9" y2="15"/><line x1="9" x2="15" y1="9" y2="15"/></svg></div>
          <div>
            <h3 style="font-size: 18px; font-weight: 600; color: #111827; margin: 0 0 8px 0;">No Usage Context</h3>
            <p style="font-size: 15px; color: #4B5563; line-height: 1.6; margin: 0;">Failing to mention how or where you will use the item.</p>
          </div>
        </div>
        <div class="mistake-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 20px; padding: 40px; display: flex; align-items: flex-start; gap: 24px; transition: all 0.3s ease;">
          <div style="color: #ef4444; margin-top: 4px;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="15" x2="9" y1="9" y2="15"/><line x1="9" x2="15" y1="9" y2="15"/></svg></div>
          <div>
            <h3 style="font-size: 18px; font-weight: 600; color: #111827; margin: 0 0 8px 0;">Too Many Requests</h3>
            <p style="font-size: 15px; color: #4B5563; line-height: 1.6; margin: 0;">Packing multiple different items into a single prompt confuses search.</p>
          </div>
        </div>
        <div class="mistake-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 20px; padding: 40px; display: flex; align-items: flex-start; gap: 24px; transition: all 0.3s ease;">
          <div style="color: #ef4444; margin-top: 4px;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="15" x2="9" y1="9" y2="15"/><line x1="9" x2="15" y1="9" y2="15"/></svg></div>
          <div>
            <h3 style="font-size: 18px; font-weight: 600; color: #111827; margin: 0 0 8px 0;">Missing Priorities</h3>
            <p style="font-size: 15px; color: #4B5563; line-height: 1.6; margin: 0;">Not clarifying which requirement (e.g., price vs speed) is most important.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 6: PRO TIPS (White) -->
  <section style="background-color: #ffffff; padding: 160px 5%; width: 100%; box-sizing: border-box;">
    <div style="max-width: 1400px; margin: 0 auto; text-align: center;">
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 24px; letter-spacing: -0.03em;">Write Like You're Talking To A Person</h2>
      <p style="font-size: 20px; color: #4B5563; line-height: 1.6; margin: 0 auto 64px auto; max-width: 800px;">Don't use keyword stuffing. Speak naturally to your agent.</p>
      
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 32px; text-align: left;">
        <div class="tip-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px 32px; box-shadow: 0 12px 32px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 56px; height: 56px; border-radius: 16px; display: flex; align-items: center; justify-content: center; margin-bottom: 24px;"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg></div>
          <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 12px;">Use Natural Language</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Write full sentences instead of fragmented keywords.</p>
        </div>
        <div class="tip-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px 32px; box-shadow: 0 12px 32px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 56px; height: 56px; border-radius: 16px; display: flex; align-items: center; justify-content: center; margin-bottom: 24px;"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M14 2H6a2 2 0 0 0-2 2v16c0 1.1.9 2 2 2h12a2 2 0 0 0 2-2V8l-6-6z"/><path d="M14 3v5h5"/><path d="M16 13H8"/><path d="M16 17H8"/><path d="M10 9H8"/></svg></div>
          <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 12px;">Give Context</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Explain *why* you are buying the item.</p>
        </div>
        <div class="tip-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px 32px; box-shadow: 0 12px 32px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 56px; height: 56px; border-radius: 16px; display: flex; align-items: center; justify-content: center; margin-bottom: 24px;"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg></div>
          <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 12px;">Prioritize Your Requirements</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Tell the agent which factor (price, quality, speed) is non-negotiable.</p>
        </div>
        <div class="tip-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px 32px; box-shadow: 0 12px 32px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 56px; height: 56px; border-radius: 16px; display: flex; align-items: center; justify-content: center; margin-bottom: 24px;"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M21.5 2v6h-6M2.13 15.57a9 9 0 1 0 3.8-11.45L2.5 7"/></svg></div>
          <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 12px;">Iterate When Needed</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">You can always refine your prompt based on the initial results.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 7: PRACTICE EXERCISE (Blue Tint) -->
  <section style="background-color: #eff6ff; padding: 160px 5%; width: 100%; box-sizing: border-box;">
    <div style="max-width: 1000px; margin: 0 auto; display: flex; flex-direction: column; align-items: center;">
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 48px; letter-spacing: -0.03em; text-align: center;">Try It Yourself</h2>
      
      <div style="background: #ffffff; border-radius: 32px; padding: 48px; width: 100%; box-shadow: 0 24px 64px rgba(37,99,235,0.1); margin-bottom: 24px; border: 1px solid rgba(37,99,235,0.1);">
        <div style="font-size: 14px; font-weight: 700; color: #2563EB; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 16px;">Scenario</div>
        <p style="font-size: 24px; color: #111827; line-height: 1.5; font-weight: 500; margin: 0 0 32px 0;">You're looking for a noise-cancelling headset for remote work with a budget of $250.</p>
        
        <div style="font-size: 14px; font-weight: 700; color: #4B5563; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 16px;">Challenge</div>
        <p style="font-size: 20px; color: #4B5563; margin: 0;">Write your own prompt.</p>
      </div>

      <div style="width: 100%; max-width: 800px; background: rgba(255,255,255,0.6); backdrop-filter: blur(10px); border-radius: 24px; padding: 40px; border: 1px solid rgba(0,0,0,0.05); text-align: center;">
        <h3 style="font-size: 16px; font-weight: 700; color: #2563EB; margin-bottom: 16px; text-transform: uppercase; letter-spacing: 0.1em;">Example Solution</h3>
        <p style="font-size: 20px; color: #111827; line-height: 1.5; margin: 0; font-style: italic;">"Find a highly-rated noise-cancelling wireless headset with a great microphone for Zoom calls. My budget is $250, and I need it delivered by Monday."</p>
      </div>
    </div>
  </section>

  <!-- FINAL CTA (White) -->
  <section style="background-color: #ffffff; padding: 180px 5% 240px 5%; width: 100%; box-sizing: border-box;">
    <div style="max-width: 1000px; margin: 0 auto; text-align: center;">
      <h2 style="font-size: 48px; font-weight: 600; color: #111827; margin-bottom: 24px; letter-spacing: -0.03em;">You're Ready To Talk To AI</h2>
      <p style="font-size: 22px; color: #4B5563; line-height: 1.7; margin: 0 auto 48px auto; max-width: 700px;">Start using better prompts today and unlock the full power of Agentic Commerce.</p>
      
      <div style="display: flex; gap: 16px; justify-content: center; flex-wrap: wrap;">
        <a href="#" class="btn-primary" style="text-decoration: none; background: #2563EB; color: #ffffff; padding: 18px 40px; border-radius: 100px; font-size: 18px; font-weight: 600; transition: all 0.3s ease; display: inline-flex; align-items: center; gap: 12px;">
            Start Shopping With AI
        </a>
        <a href="shopping-workflows.html" class="btn-secondary" style="text-decoration: none; background: #f8fafc; border: 1px solid rgba(0,0,0,0.1); color: #111827; padding: 18px 40px; border-radius: 100px; font-size: 18px; font-weight: 600; transition: all 0.3s ease;">
            Continue Learning
        </a>
      </div>
    </div>
  </section>

  <style>
    .matter-card:hover, .tip-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 24px 48px rgba(37,99,235,0.08) !important;
        border-color: rgba(37,99,235,0.2) !important;
    }
    .compare-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 24px 48px rgba(0,0,0,0.04) !important;
        border-color: rgba(37,99,235,0.2) !important;
    }
    .library-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 16px 32px rgba(0,0,0,0.04) !important;
        border-color: rgba(37,99,235,0.3) !important;
    }
    .mistake-card:hover {
        transform: translateY(-4px);
        background: #ffffff !important;
        box-shadow: 0 12px 24px rgba(239,68,68,0.06) !important;
        border-color: rgba(239,68,68,0.2) !important;
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
        .semantic-mastering-wrapper section {
            padding: 100px 5% !important;
        }
        .semantic-mastering-wrapper h1 {
            font-size: 48px !important;
        }
        .semantic-mastering-wrapper h2 {
            font-size: 32px !important;
        }
        .formula-timeline {
            flex-direction: column !important;
            gap: 40px !important;
        }
        .timeline-line {
            display: none !important;
        }
        .compare-card {
            grid-template-columns: 1fr !important;
        }
        .mistake-card {
            grid-column: span 2 !important;
        }
    }
    @media (max-width: 600px) {
        .semantic-mastering-wrapper section {
            padding: 80px 5% !important;
        }
        .semantic-mastering-wrapper h1 {
            font-size: 40px !important;
        }
        .semantic-mastering-wrapper .btn-primary, .semantic-mastering-wrapper .btn-secondary {
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
        new_section = bs4.BeautifulSoup(mastering_html, 'html.parser')
        wrapper.replace_with(new_section)
    else:
        # Fallback if no wrapper found
        section_to_replace = placeholder.find_parent('section')
        if section_to_replace:
            new_section = bs4.BeautifulSoup(mastering_html, 'html.parser')
            section_to_replace.replace_with(new_section)

with open('mastering-ai-prompts.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Successfully built the Mastering AI Prompts page.")
