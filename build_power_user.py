import bs4

with open('power-user-guide.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = bs4.BeautifulSoup(html, 'html.parser')

# 1. Update Title
if soup.title:
    soup.title.string = "Nexmart - Power User Guide"

# 2. Build Power User Guide Content HTML
power_html = """
<div class="semantic-power-wrapper" style="width: 100%; display: flex; flex-direction: column; font-family: 'Inter', system-ui, -apple-system, sans-serif;">
  
  <!-- HERO SECTION -->
  <section style="background-color: #ffffff; padding: 160px 5% 100px 5%; width: 100%; box-sizing: border-box; text-align: center;">
    <div style="max-width: 1000px; margin: 0 auto;">
      <h1 style="font-size: 64px; font-weight: 700; color: #111827; margin-bottom: 24px; letter-spacing: -0.04em; line-height: 1.1;">Power User Guide</h1>
      <p style="font-size: 22px; color: #4B5563; line-height: 1.6; margin: 0 auto; max-width: 800px;">Unlock the full potential of Nexmart with advanced AI workflows, automation techniques, and expert strategies used by experienced shoppers and businesses.</p>
    </div>
  </section>

  <!-- SECTION 1: THE POWER USER MINDSET (Light Gray) -->
  <section style="background-color: #f8fafc; padding: 160px 5%; width: 100%; box-sizing: border-box; border-top: 1px solid rgba(0,0,0,0.03);">
    <div style="max-width: 1400px; margin: 0 auto; text-align: center;">
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 24px; letter-spacing: -0.03em;">Think Beyond Search</h2>
      <div style="max-width: 800px; margin: 0 auto 64px auto; text-align: left;">
          <p style="font-size: 20px; color: #4B5563; line-height: 1.6; margin: 0 0 16px 0;">Power users don't search for products—they define outcomes.</p>
          <p style="font-size: 20px; color: #4B5563; line-height: 1.6; margin: 0;">Instead of comparing hundreds of products manually, they let AI handle research while they focus on making better decisions.</p>
      </div>
      
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 32px; text-align: left;">
        <div class="mindset-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 24px; padding: 48px 32px; box-shadow: 0 12px 32px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 56px; height: 56px; border-radius: 16px; display: flex; align-items: center; justify-content: center; margin-bottom: 24px;"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2v20"/><path d="m17 5 5 5-5 5"/><path d="m7 19-5-5 5-5"/></svg></div>
          <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 12px;">Automation First</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Let AI complete repetitive tasks.</p>
        </div>
        <div class="mindset-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 24px; padding: 48px 32px; box-shadow: 0 12px 32px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 56px; height: 56px; border-radius: 16px; display: flex; align-items: center; justify-content: center; margin-bottom: 24px;"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="4"/><line x1="21.17" x2="12" y1="8" y2="8"/><line x1="3.95" x2="8.54" y1="6.06" y2="14"/><line x1="10.88" x2="15.46" y1="21.94" y2="14"/></svg></div>
          <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 12px;">Outcome Driven</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Describe goals, not products.</p>
        </div>
        <div class="mindset-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 24px; padding: 48px 32px; box-shadow: 0 12px 32px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 56px; height: 56px; border-radius: 16px; display: flex; align-items: center; justify-content: center; margin-bottom: 24px;"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M3 3v18h18"/><path d="m19 9-5 5-4-4-3 3"/></svg></div>
          <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 12px;">Data Over Guesswork</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Trust insights backed by intelligence.</p>
        </div>
        <div class="mindset-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 24px; padding: 48px 32px; box-shadow: 0 12px 32px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 56px; height: 56px; border-radius: 16px; display: flex; align-items: center; justify-content: center; margin-bottom: 24px;"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M21.5 2v6h-6M2.13 15.57a9 9 0 1 0 3.8-11.45L2.5 7"/></svg></div>
          <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 12px;">Continuous Learning</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Refine prompts and workflows over time.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 2: ADVANCED AI WORKFLOWS (White) -->
  <section style="background-color: #ffffff; padding: 160px 5%; width: 100%; box-sizing: border-box;">
    <div style="max-width: 1400px; margin: 0 auto;">
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 64px; letter-spacing: -0.03em; text-align: center;">Work Smarter With AI</h2>
      
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 32px;">
        <div class="workflow-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.08); border-radius: 24px; padding: 40px; display: flex; flex-direction: column; transition: all 0.3s ease;">
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin-bottom: 16px;">Multi-step Shopping</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Research + Compare + Purchase.</p>
        </div>
        <div class="workflow-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.08); border-radius: 24px; padding: 40px; display: flex; flex-direction: column; transition: all 0.3s ease;">
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin-bottom: 16px;">Budget Optimization</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Maximize value within spending limits.</p>
        </div>
        <div class="workflow-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.08); border-radius: 24px; padding: 40px; display: flex; flex-direction: column; transition: all 0.3s ease;">
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin-bottom: 16px;">Subscription Management</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Automate recurring purchases.</p>
        </div>
        <div class="workflow-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.08); border-radius: 24px; padding: 40px; display: flex; flex-direction: column; transition: all 0.3s ease;">
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin-bottom: 16px;">Smart Comparison</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Evaluate multiple brands simultaneously.</p>
        </div>
        <div class="workflow-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.08); border-radius: 24px; padding: 40px; display: flex; flex-direction: column; transition: all 0.3s ease;">
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin-bottom: 16px;">Seasonal Planning</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Prepare purchases months in advance.</p>
        </div>
        <div class="workflow-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.08); border-radius: 24px; padding: 40px; display: flex; flex-direction: column; transition: all 0.3s ease;">
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin-bottom: 16px;">Bulk Purchasing</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Optimize larger orders for families and businesses.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 3: PROFESSIONAL PROMPT EXAMPLES (Light Gray) -->
  <section style="background-color: #f8fafc; padding: 160px 5%; width: 100%; box-sizing: border-box; border-top: 1px solid rgba(0,0,0,0.03);">
    <div style="max-width: 1400px; margin: 0 auto;">
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 64px; letter-spacing: -0.03em; text-align: center;">Advanced Prompt Library</h2>
      
      <div style="display: grid; grid-template-columns: 1fr; gap: 40px;">
        
        <!-- Example 1 -->
        <div class="showcase-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.05); border-radius: 32px; padding: 56px; box-shadow: 0 16px 40px rgba(0,0,0,0.02); display: flex; flex-direction: column; gap: 24px; transition: all 0.3s ease;">
          <div style="display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid rgba(0,0,0,0.05); padding-bottom: 24px;">
            <div style="font-size: 24px; font-weight: 600; color: #111827;">Business Procurement</div>
          </div>
          <div style="font-size: 24px; font-weight: 500; color: #111827; line-height: 1.5; padding: 32px; background: #f8fafc; border-radius: 16px; border: 1px solid rgba(0,0,0,0.03);">"Build a complete office setup for 25 employees while staying under a $20,000 budget."</div>
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 32px; margin-top: 16px;">
            <div>
              <div style="font-size: 14px; font-weight: 700; color: #2563EB; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 8px;">Why it works</div>
              <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Provides clear constraints (25 employees, $20k budget) while leaving product selection to the AI's optimization engine.</p>
            </div>
            <div>
              <div style="font-size: 14px; font-weight: 700; color: #10B981; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 8px;">Expected AI Outcome</div>
              <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">A fully itemized breakdown of desks, chairs, monitors, and peripherals optimized for bulk discounts and uniform delivery.</p>
            </div>
          </div>
        </div>

        <!-- Example 2 -->
        <div class="showcase-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.05); border-radius: 32px; padding: 56px; box-shadow: 0 16px 40px rgba(0,0,0,0.02); display: flex; flex-direction: column; gap: 24px; transition: all 0.3s ease;">
          <div style="display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid rgba(0,0,0,0.05); padding-bottom: 24px;">
            <div style="font-size: 24px; font-weight: 600; color: #111827;">Travel Planning</div>
          </div>
          <div style="font-size: 24px; font-weight: 500; color: #111827; line-height: 1.5; padding: 32px; background: #f8fafc; border-radius: 16px; border: 1px solid rgba(0,0,0,0.03);">"Prepare everything needed for a two-week European business trip."</div>
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 32px; margin-top: 16px;">
            <div>
              <div style="font-size: 14px; font-weight: 700; color: #2563EB; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 8px;">Why it works</div>
              <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Leverages AI's contextual understanding of European business travel requirements (adapters, luggage size, weather).</p>
            </div>
            <div>
              <div style="font-size: 14px; font-weight: 700; color: #10B981; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 8px;">Expected AI Outcome</div>
              <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">A curated checklist and shopping cart containing adapters, travel-sized toiletries, wrinkle-free attire, and appropriate luggage.</p>
            </div>
          </div>
        </div>

        <!-- Example 3 -->
        <div class="showcase-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.05); border-radius: 32px; padding: 56px; box-shadow: 0 16px 40px rgba(0,0,0,0.02); display: flex; flex-direction: column; gap: 24px; transition: all 0.3s ease;">
          <div style="display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid rgba(0,0,0,0.05); padding-bottom: 24px;">
            <div style="font-size: 24px; font-weight: 600; color: #111827;">Family Shopping</div>
          </div>
          <div style="font-size: 24px; font-weight: 500; color: #111827; line-height: 1.5; padding: 32px; background: #f8fafc; border-radius: 16px; border: 1px solid rgba(0,0,0,0.03);">"Plan healthy monthly groceries for a family of five with a budget of $600."</div>
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 32px; margin-top: 16px;">
            <div>
              <div style="font-size: 14px; font-weight: 700; color: #2563EB; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 8px;">Why it works</div>
              <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Combines scale (monthly), dietary preference (healthy), demographics (family of 5), and a strict financial constraint.</p>
            </div>
            <div>
              <div style="font-size: 14px; font-weight: 700; color: #10B981; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 8px;">Expected AI Outcome</div>
              <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">A comprehensive, balanced grocery list utilizing bulk discounts and staple items to meet the budget while ensuring nutritional variety.</p>
            </div>
          </div>
        </div>

        <!-- Example 4 -->
        <div class="showcase-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.05); border-radius: 32px; padding: 56px; box-shadow: 0 16px 40px rgba(0,0,0,0.02); display: flex; flex-direction: column; gap: 24px; transition: all 0.3s ease;">
          <div style="display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid rgba(0,0,0,0.05); padding-bottom: 24px;">
            <div style="font-size: 24px; font-weight: 600; color: #111827;">Technology Upgrade</div>
          </div>
          <div style="font-size: 24px; font-weight: 500; color: #111827; line-height: 1.5; padding: 32px; background: #f8fafc; border-radius: 16px; border: 1px solid rgba(0,0,0,0.03);">"Recommend a complete workstation for video editing under $3,000."</div>
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 32px; margin-top: 16px;">
            <div>
              <div style="font-size: 14px; font-weight: 700; color: #2563EB; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 8px;">Why it works</div>
              <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Identifies the highly specific use case (video editing) which informs the AI to prioritize GPU and RAM allocation within the budget.</p>
            </div>
            <div>
              <div style="font-size: 14px; font-weight: 700; color: #10B981; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 8px;">Expected AI Outcome</div>
              <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">A customized build or pre-built system recommendation paired with an appropriate color-accurate monitor and peripherals.</p>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- SECTION 4: PRODUCTIVITY TIPS (White) -->
  <section style="background-color: #ffffff; padding: 160px 5%; width: 100%; box-sizing: border-box;">
    <div style="max-width: 1400px; margin: 0 auto;">
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 64px; letter-spacing: -0.03em; text-align: center;">Save More Time</h2>
      
      <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 24px;">
        <div class="tip-card" style="background: #f8fafc; border: 1px solid rgba(0,0,0,0.04); border-radius: 20px; padding: 40px; display: flex; align-items: flex-start; gap: 24px; transition: all 0.3s ease;">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 48px; height: 48px; border-radius: 12px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11l5 5v11a2 2 0 0 1-2 2z"/><polyline points="17 21 17 13 7 13 7 21"/><polyline points="7 3 7 8 15 8"/></svg></div>
          <div>
            <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin: 0;">Save Successful Prompts</h3>
          </div>
        </div>
        <div class="tip-card" style="background: #f8fafc; border: 1px solid rgba(0,0,0,0.04); border-radius: 20px; padding: 40px; display: flex; align-items: flex-start; gap: 24px; transition: all 0.3s ease;">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 48px; height: 48px; border-radius: 12px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg></div>
          <div>
            <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin: 0;">Reuse Winning Workflows</h3>
          </div>
        </div>
        <div class="tip-card" style="background: #f8fafc; border: 1px solid rgba(0,0,0,0.04); border-radius: 20px; padding: 40px; display: flex; align-items: flex-start; gap: 24px; transition: all 0.3s ease;">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 48px; height: 48px; border-radius: 12px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3v18"/><path d="m3 12 9-9 9 9"/></svg></div>
          <div>
            <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin: 0;">Combine Multiple Requests</h3>
          </div>
        </div>
        <div class="tip-card" style="background: #f8fafc; border: 1px solid rgba(0,0,0,0.04); border-radius: 20px; padding: 40px; display: flex; align-items: flex-start; gap: 24px; transition: all 0.3s ease;">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 48px; height: 48px; border-radius: 12px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg></div>
          <div>
            <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin: 0;">Review AI Reasoning</h3>
          </div>
        </div>
        <div class="tip-card" style="background: #f8fafc; border: 1px solid rgba(0,0,0,0.04); border-radius: 20px; padding: 40px; display: flex; align-items: flex-start; gap: 24px; transition: all 0.3s ease;">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 48px; height: 48px; border-radius: 12px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 20h9"/><path d="M16.5 3.5a2.12 2.12 0 0 1 3 3L7 19l-4 1 1-4Z"/></svg></div>
          <div>
            <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin: 0;">Update Preferences</h3>
          </div>
        </div>
        <div class="tip-card" style="background: #f8fafc; border: 1px solid rgba(0,0,0,0.04); border-radius: 20px; padding: 40px; display: flex; align-items: flex-start; gap: 24px; transition: all 0.3s ease;">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 48px; height: 48px; border-radius: 12px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6H5a2 2 0 0 0-2 2v3a2 2 0 0 0 2 2h13l4-3.5L18 6Z"/><path d="M12 13v9"/><path d="M12 2v4"/></svg></div>
          <div>
            <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin: 0;">Experiment Frequently</h3>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 5: BUSINESS SUITE (Blue Tint) -->
  <section style="background-color: #eff6ff; padding: 160px 5%; width: 100%; box-sizing: border-box;">
    <div style="max-width: 1400px; margin: 0 auto;">
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 24px; letter-spacing: -0.03em; text-align: center;">Beyond Shopping</h2>
      <p style="font-size: 20px; color: #4B5563; line-height: 1.6; margin: 0 auto 64px auto; max-width: 800px; text-align: center;">Introduce advanced Nexmart products.</p>
      
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 32px;">
        <div class="biz-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 24px; padding: 48px; box-shadow: 0 12px 32px rgba(37,99,235,0.04); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 56px; height: 56px; border-radius: 16px; display: flex; align-items: center; justify-content: center; margin-bottom: 24px;"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M21 12V7H5a2 2 0 0 1 0-4h14v4"/><path d="M3 5v14a2 2 0 0 0 2 2h16v-5"/><path d="M18 12a2 2 0 0 0 0 4h4v-4Z"/></svg></div>
          <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 12px;">Advertiser Tracker</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Monitor competitor advertising.</p>
        </div>
        <div class="biz-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 24px; padding: 48px; box-shadow: 0 12px 32px rgba(37,99,235,0.04); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 56px; height: 56px; border-radius: 16px; display: flex; align-items: center; justify-content: center; margin-bottom: 24px;"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg></div>
          <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 12px;">Creator Library</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Discover high-performing creators.</p>
        </div>
        <div class="biz-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 24px; padding: 48px; box-shadow: 0 12px 32px rgba(37,99,235,0.04); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 56px; height: 56px; border-radius: 16px; display: flex; align-items: center; justify-content: center; margin-bottom: 24px;"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M3 3v18h18"/><path d="m19 9-5 5-4-4-3 3"/></svg></div>
          <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 12px;">Sales Tracker</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Track products and revenue.</p>
        </div>
        <div class="biz-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 24px; padding: 48px; box-shadow: 0 12px 32px rgba(37,99,235,0.04); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 56px; height: 56px; border-radius: 16px; display: flex; align-items: center; justify-content: center; margin-bottom: 24px;"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect width="18" height="18" x="3" y="3" rx="2"/><path d="M3 9h18"/><path d="M9 21V9"/></svg></div>
          <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 12px;">Product Library</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Explore winning products globally.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 6: EXPERT PRINCIPLES (White) -->
  <section style="background-color: #ffffff; padding: 160px 5%; width: 100%; box-sizing: border-box;">
    <div style="max-width: 1000px; margin: 0 auto; text-align: center;">
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 64px; letter-spacing: -0.03em;">The Five Principles Of Every Power User</h2>
      
      <div style="background: #f8fafc; border-radius: 32px; padding: 64px; box-shadow: 0 24px 64px rgba(0,0,0,0.03); border: 1px solid rgba(0,0,0,0.05); text-align: left;">
        <div style="display: flex; flex-direction: column; gap: 32px;">
            <div style="font-size: 24px; font-weight: 600; color: #111827; display: flex; gap: 24px; align-items: center; border-bottom: 1px solid rgba(0,0,0,0.05); padding-bottom: 32px;">
                <div style="color: #2563EB; font-weight: 700; font-size: 28px;">01</div>
                <div>Intent Before Search</div>
            </div>
            <div style="font-size: 24px; font-weight: 600; color: #111827; display: flex; gap: 24px; align-items: center; border-bottom: 1px solid rgba(0,0,0,0.05); padding-bottom: 32px;">
                <div style="color: #2563EB; font-weight: 700; font-size: 28px;">02</div>
                <div>Context Creates Better Results</div>
            </div>
            <div style="font-size: 24px; font-weight: 600; color: #111827; display: flex; gap: 24px; align-items: center; border-bottom: 1px solid rgba(0,0,0,0.05); padding-bottom: 32px;">
                <div style="color: #2563EB; font-weight: 700; font-size: 28px;">03</div>
                <div>Trust Data</div>
            </div>
            <div style="font-size: 24px; font-weight: 600; color: #111827; display: flex; gap: 24px; align-items: center; border-bottom: 1px solid rgba(0,0,0,0.05); padding-bottom: 32px;">
                <div style="color: #2563EB; font-weight: 700; font-size: 28px;">04</div>
                <div>Automate Repetition</div>
            </div>
            <div style="font-size: 24px; font-weight: 600; color: #111827; display: flex; gap: 24px; align-items: center;">
                <div style="color: #2563EB; font-weight: 700; font-size: 28px;">05</div>
                <div>Stay Curious</div>
            </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 7: WHAT'S NEXT (Light Gray) -->
  <section style="background-color: #f8fafc; padding: 160px 5%; width: 100%; box-sizing: border-box; border-top: 1px solid rgba(0,0,0,0.03);">
    <div style="max-width: 1400px; margin: 0 auto;">
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 64px; letter-spacing: -0.03em; text-align: center;">Continue Your Journey</h2>
      
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 32px;">
        <a href="#" class="journey-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.08); border-radius: 32px; padding: 56px; display: flex; flex-direction: column; transition: all 0.3s ease;">
          <h3 style="font-size: 24px; font-weight: 600; color: #111827; margin-bottom: 16px;">Explore Business Suite</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.6; margin: 0 0 32px 0; flex-grow: 1;">Discover advanced commerce tools.</p>
          <div style="color: #2563EB; font-weight: 600; display: inline-flex; align-items: center; gap: 8px;">Explore <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg></div>
        </a>
        <a href="blog.html" class="journey-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.08); border-radius: 32px; padding: 56px; display: flex; flex-direction: column; transition: all 0.3s ease;">
          <h3 style="font-size: 24px; font-weight: 600; color: #111827; margin-bottom: 16px;">Read The Nexmart Journal</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.6; margin: 0 0 32px 0; flex-grow: 1;">Stay informed about the future of AI commerce.</p>
          <div style="color: #2563EB; font-weight: 600; display: inline-flex; align-items: center; gap: 8px;">Read Journal <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg></div>
        </a>
        <a href="discord-community.html" class="journey-card" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.08); border-radius: 32px; padding: 56px; display: flex; flex-direction: column; transition: all 0.3s ease;">
          <h3 style="font-size: 24px; font-weight: 600; color: #111827; margin-bottom: 16px;">Join The Discord Community</h3>
          <p style="font-size: 18px; color: #4B5563; line-height: 1.6; margin: 0 0 32px 0; flex-grow: 1;">Connect with builders, creators, and early adopters.</p>
          <div style="color: #2563EB; font-weight: 600; display: inline-flex; align-items: center; gap: 8px;">Join Community <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg></div>
        </a>
      </div>
    </div>
  </section>

  <!-- FINAL CTA (White) -->
  <section style="background-color: #ffffff; padding: 180px 5% 240px 5%; width: 100%; box-sizing: border-box;">
    <div style="max-width: 1000px; margin: 0 auto; text-align: center;">
      <h2 style="font-size: 48px; font-weight: 600; color: #111827; margin-bottom: 24px; letter-spacing: -0.03em;">You're Ready To Master Agentic Commerce</h2>
      <p style="font-size: 22px; color: #4B5563; line-height: 1.7; margin: 0 auto 16px auto; max-width: 800px;">You've completed the Nexmart learning journey.</p>
      <p style="font-size: 22px; color: #4B5563; line-height: 1.7; margin: 0 auto 48px auto; max-width: 800px;">Now it's time to put everything into practice.</p>
      
      <div style="display: flex; gap: 16px; justify-content: center; flex-wrap: wrap;">
        <a href="#" class="btn-primary" style="text-decoration: none; background: #2563EB; color: #ffffff; padding: 18px 40px; border-radius: 100px; font-size: 18px; font-weight: 600; transition: all 0.3s ease; display: inline-flex; align-items: center; gap: 12px;">
            Start Shopping With AI
        </a>
        <a href="nexmart-university.html" class="btn-secondary" style="text-decoration: none; background: #f8fafc; border: 1px solid rgba(0,0,0,0.1); color: #111827; padding: 18px 40px; border-radius: 100px; font-size: 18px; font-weight: 600; transition: all 0.3s ease;">
            Return to Nexmart University
        </a>
      </div>
    </div>
  </section>

  <style>
    .mindset-card:hover, .biz-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 24px 48px rgba(37,99,235,0.08) !important;
        border-color: rgba(37,99,235,0.2) !important;
    }
    .workflow-card:hover, .journey-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 16px 32px rgba(0,0,0,0.04) !important;
        border-color: rgba(37,99,235,0.3) !important;
    }
    .showcase-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 24px 48px rgba(0,0,0,0.04) !important;
        border-color: rgba(37,99,235,0.2) !important;
    }
    .tip-card:hover {
        transform: translateY(-4px);
        background: #ffffff !important;
        box-shadow: 0 16px 32px rgba(0,0,0,0.04) !important;
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
    
    @media (max-width: 991px) {
        .semantic-power-wrapper section {
            padding: 100px 5% !important;
        }
        .semantic-power-wrapper h1 {
            font-size: 48px !important;
        }
        .semantic-power-wrapper h2 {
            font-size: 32px !important;
        }
        .tip-card {
            grid-column: span 2 !important;
        }
    }
    @media (max-width: 600px) {
        .semantic-power-wrapper section {
            padding: 80px 5% !important;
        }
        .semantic-power-wrapper h1 {
            font-size: 40px !important;
        }
        .semantic-power-wrapper .btn-primary, .semantic-power-wrapper .btn-secondary {
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
    wrapper = placeholder.find_parent('div', class_='semantic-placeholder-wrapper')
    if wrapper:
        new_section = bs4.BeautifulSoup(power_html, 'html.parser')
        wrapper.replace_with(new_section)
    else:
        section_to_replace = placeholder.find_parent('section')
        if section_to_replace:
            new_section = bs4.BeautifulSoup(power_html, 'html.parser')
            section_to_replace.replace_with(new_section)

with open('power-user-guide.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Successfully built the Power User Guide page.")
