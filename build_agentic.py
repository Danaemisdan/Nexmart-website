import bs4

with open('agentic-commerce-101.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = bs4.BeautifulSoup(html, 'html.parser')

# 1. Update Title
if soup.title:
    soup.title.string = "Nexmart - Agentic Commerce 101"

# 2. Build Agentic Commerce 101 Content HTML
agentic_html = """
<div class="semantic-agentic-wrapper" style="width: 100%; display: flex; flex-direction: column; font-family: 'Inter', system-ui, -apple-system, sans-serif;">
  
  <!-- HERO SECTION -->
  <section style="background-color: #ffffff; padding: 160px 5% 100px 5%; width: 100%; box-sizing: border-box; text-align: center;">
    <div style="max-width: 1000px; margin: 0 auto;">
      <h1 style="font-size: 64px; font-weight: 700; color: #111827; margin-bottom: 24px; letter-spacing: -0.04em; line-height: 1.1;">Agentic Commerce 101</h1>
      <p style="font-size: 22px; color: #4B5563; line-height: 1.6; margin: 0 auto; max-width: 800px;">Discover why the future of shopping isn't about searching for products—it's about intelligent AI agents understanding your intent and completing tasks on your behalf.</p>
    </div>
  </section>

  <!-- SECTION 1: THE EVOLUTION OF COMMERCE (Light Gray) -->
  <section style="background-color: #f8fafc; padding: 140px 5%; width: 100%; box-sizing: border-box; border-top: 1px solid rgba(0,0,0,0.03);">
    <div style="max-width: 1400px; margin: 0 auto; text-align: center;">
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 80px; letter-spacing: -0.03em;">The Evolution of Commerce</h2>
      
      <div class="evolution-timeline" style="display: flex; justify-content: space-between; position: relative; margin-bottom: 80px;">
        <div class="timeline-line-evo" style="position: absolute; top: 40px; left: 12.5%; right: 12.5%; height: 2px; background: rgba(37,99,235,0.1); z-index: 0;"></div>
        
        <div class="evo-step" style="position: relative; z-index: 1; flex: 1; padding: 0 16px;">
          <div style="background: #ffffff; border: 2px solid #2563EB; width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 24px auto; color: #2563EB;">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M3 2v7c0 1.1.9 2 2 2h4a2 2 0 0 0 2-2V2"/><path d="M7 2v20"/><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><path d="M16.5 15h2.5a2 2 0 0 0 2-2v-1"/><path d="M12 15h.01"/></svg>
          </div>
          <h4 style="font-size: 18px; font-weight: 600; color: #111827; margin-bottom: 8px;">Traditional Retail</h4>
          <p style="font-size: 14px; color: #4B5563; line-height: 1.5; margin: 0;">People visited physical stores.</p>
        </div>

        <div class="evo-step" style="position: relative; z-index: 1; flex: 1; padding: 0 16px;">
          <div style="background: #ffffff; border: 2px solid #2563EB; width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 24px auto; color: #2563EB;">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect width="20" height="14" x="2" y="3" rx="2"/><line x1="8" x2="16" y1="21" y2="21"/><line x1="12" x2="12" y1="17" y2="21"/></svg>
          </div>
          <h4 style="font-size: 18px; font-weight: 600; color: #111827; margin-bottom: 8px;">E-Commerce</h4>
          <p style="font-size: 14px; color: #4B5563; line-height: 1.5; margin: 0;">People searched websites manually.</p>
        </div>

        <div class="evo-step" style="position: relative; z-index: 1; flex: 1; padding: 0 16px;">
          <div style="background: #ffffff; border: 2px solid #2563EB; width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 24px auto; color: #2563EB;">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
          </div>
          <h4 style="font-size: 18px; font-weight: 600; color: #111827; margin-bottom: 8px;">Marketplace Era</h4>
          <p style="font-size: 14px; color: #4B5563; line-height: 1.5; margin: 0;">Millions of products but increasing complexity.</p>
        </div>

        <div class="evo-step" style="position: relative; z-index: 1; flex: 1; padding: 0 16px;">
          <div style="background: #2563EB; border: 2px solid #2563EB; width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 24px auto; color: #ffffff; box-shadow: 0 8px 24px rgba(37,99,235,0.2);">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2v20"/><path d="m17 5 5 5-5 5"/><path d="m7 19-5-5 5-5"/></svg>
          </div>
          <h4 style="font-size: 18px; font-weight: 600; color: #111827; margin-bottom: 8px;">Agentic Commerce</h4>
          <p style="font-size: 14px; color: #4B5563; line-height: 1.5; margin: 0;">AI understands intent, researches options, compares products, negotiates, and purchases autonomously.</p>
        </div>
      </div>
      
      <div style="font-size: 32px; font-weight: 500; color: #2563EB; line-height: 1.4; max-width: 800px; margin: 0 auto; font-style: italic;">
        "The next evolution isn't more marketplaces.<br/>It's intelligent agents."
      </div>
    </div>
  </section>

  <!-- SECTION 2: THE PROBLEM WITH MODERN SHOPPING (White) -->
  <section style="background-color: #ffffff; padding: 160px 5%; width: 100%; box-sizing: border-box;">
    <div style="max-width: 1400px; margin: 0 auto;">
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 64px; letter-spacing: -0.03em; text-align: center;">The Problem with Modern Shopping</h2>
      
      <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 24px;">
        <div class="problem-card" style="background: #f8fafc; border: 1px solid rgba(0,0,0,0.04); border-radius: 20px; padding: 40px; display: flex; align-items: flex-start; gap: 24px; transition: all 0.3s ease;">
          <div style="color: #ef4444; margin-top: 4px;"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" x2="12" y1="8" y2="12"/><line x1="12" x2="12.01" y1="16" y2="16"/></svg></div>
          <div>
            <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin: 0 0 12px 0;">Too Many Choices</h3>
            <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Thousands of nearly identical products create confusion.</p>
          </div>
        </div>
        <div class="problem-card" style="background: #f8fafc; border: 1px solid rgba(0,0,0,0.04); border-radius: 20px; padding: 40px; display: flex; align-items: flex-start; gap: 24px; transition: all 0.3s ease;">
          <div style="color: #ef4444; margin-top: 4px;"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20"/><path d="m17 5 5 5-5 5"/><path d="m7 19-5-5 5-5"/></svg></div>
          <div>
            <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin: 0 0 12px 0;">Decision Fatigue</h3>
            <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Research consumes time and energy.</p>
          </div>
        </div>
        <div class="problem-card" style="background: #f8fafc; border: 1px solid rgba(0,0,0,0.04); border-radius: 20px; padding: 40px; display: flex; align-items: flex-start; gap: 24px; transition: all 0.3s ease;">
          <div style="color: #ef4444; margin-top: 4px;"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"/><line x1="12" x2="12" y1="9" y2="13"/><line x1="12" x2="12.01" y1="17" y2="17"/></svg></div>
          <div>
            <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin: 0 0 12px 0;">Fake Reviews</h3>
            <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Finding trustworthy information becomes difficult.</p>
          </div>
        </div>
        <div class="problem-card" style="background: #f8fafc; border: 1px solid rgba(0,0,0,0.04); border-radius: 20px; padding: 40px; display: flex; align-items: flex-start; gap: 24px; transition: all 0.3s ease;">
          <div style="color: #ef4444; margin-top: 4px;"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg></div>
          <div>
            <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin: 0 0 12px 0;">Price Hunting</h3>
            <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Users manually compare countless websites.</p>
          </div>
        </div>
        <div class="problem-card" style="background: #f8fafc; border: 1px solid rgba(0,0,0,0.04); border-radius: 20px; padding: 40px; display: flex; align-items: flex-start; gap: 24px; transition: all 0.3s ease;">
          <div style="color: #ef4444; margin-top: 4px;"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 7V5a2 2 0 0 1 2-2h2"/><path d="M17 3h2a2 2 0 0 1 2 2v2"/><path d="M21 17v2a2 2 0 0 1-2 2h-2"/><path d="M7 21H5a2 2 0 0 1-2-2v-2"/></svg></div>
          <div>
            <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin: 0 0 12px 0;">Fragmented Experience</h3>
            <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Products, payments, delivery and subscriptions all exist separately.</p>
          </div>
        </div>
        <div class="problem-card" style="background: #f8fafc; border: 1px solid rgba(0,0,0,0.04); border-radius: 20px; padding: 40px; display: flex; align-items: flex-start; gap: 24px; transition: all 0.3s ease;">
          <div style="color: #ef4444; margin-top: 4px;"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg></div>
          <div>
            <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin: 0 0 12px 0;">Time Lost</h3>
            <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Hours disappear performing repetitive research.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 3: HOW AGENTIC COMMERCE CHANGES EVERYTHING (Blue Tint Background) -->
  <section style="background-color: #eff6ff; padding: 160px 5%; width: 100%; box-sizing: border-box;">
    <div style="max-width: 1400px; margin: 0 auto; text-align: center;">
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 80px; letter-spacing: -0.03em;">How Agentic Commerce Changes Everything</h2>
      
      <div style="display: flex; gap: 40px; justify-content: center; flex-wrap: wrap; text-align: left;">
        
        <!-- Traditional Shopping -->
        <div style="background: #ffffff; border-radius: 32px; padding: 56px; width: 100%; max-width: 500px; box-shadow: 0 12px 32px rgba(0,0,0,0.04); border: 1px solid rgba(0,0,0,0.05); display: flex; flex-direction: column; gap: 20px;">
          <h3 style="font-size: 24px; font-weight: 600; color: #4B5563; margin-bottom: 24px; text-transform: uppercase; letter-spacing: 0.05em; text-align: center;">Traditional Shopping</h3>
          
          <div class="compare-row"><div class="cross"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg></div>Search</div>
          <div class="compare-row"><div class="cross"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg></div>Open tabs</div>
          <div class="compare-row"><div class="cross"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg></div>Read reviews</div>
          <div class="compare-row"><div class="cross"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg></div>Compare prices</div>
          <div class="compare-row"><div class="cross"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg></div>Choose</div>
          <div class="compare-row"><div class="cross"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg></div>Buy</div>
        </div>

        <!-- Agentic Commerce -->
        <div style="background: #2563EB; border-radius: 32px; padding: 56px; width: 100%; max-width: 500px; box-shadow: 0 24px 64px rgba(37,99,235,0.2); display: flex; flex-direction: column; gap: 20px; color: #ffffff;">
          <h3 style="font-size: 24px; font-weight: 600; color: #ffffff; margin-bottom: 24px; text-transform: uppercase; letter-spacing: 0.05em; text-align: center;">Agentic Commerce</h3>
          
          <div class="compare-row-active"><div class="check"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg></div>Describe your intent</div>
          <div class="compare-row-active"><div class="check"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg></div>AI researches</div>
          <div class="compare-row-active"><div class="check"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg></div>AI compares</div>
          <div class="compare-row-active"><div class="check"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg></div>AI negotiates</div>
          <div class="compare-row-active"><div class="check"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg></div>AI recommends</div>
          <div class="compare-row-active"><div class="check"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg></div>You approve</div>
          <div class="compare-row-active"><div class="check"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg></div>Purchase completed</div>
        </div>

      </div>

      <p style="font-size: 20px; color: #1e3a8a; font-weight: 500; margin: 48px auto 0 auto; max-width: 800px; line-height: 1.6;">Instead of spending hours researching products, your AI agents complete the work in minutes.</p>
    </div>
  </section>

  <!-- SECTION 4: MEET YOUR AI SHOPPING AGENT (White) -->
  <section style="background-color: #ffffff; padding: 160px 5%; width: 100%; box-sizing: border-box;">
    <div style="max-width: 1400px; margin: 0 auto;">
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 64px; letter-spacing: -0.03em; text-align: center;">Meet Your AI Shopping Agent</h2>
      
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 32px;">
        <div class="agent-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px; box-shadow: 0 12px 32px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 64px; height: 64px; border-radius: 20px; display: flex; align-items: center; justify-content: center; margin-bottom: 32px;"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg></div>
          <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 12px;">Intent Understanding</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">The AI understands what you actually want.</p>
        </div>
        <div class="agent-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px; box-shadow: 0 12px 32px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 64px; height: 64px; border-radius: 20px; display: flex; align-items: center; justify-content: center; margin-bottom: 32px;"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg></div>
          <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 12px;">Autonomous Research</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Searches thousands of products simultaneously.</p>
        </div>
        <div class="agent-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px; box-shadow: 0 12px 32px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 64px; height: 64px; border-radius: 20px; display: flex; align-items: center; justify-content: center; margin-bottom: 32px;"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2v20"/><path d="m17 5 5 5-5 5"/><path d="m7 19-5-5 5-5"/></svg></div>
          <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 12px;">Intelligent Comparison</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Evaluates quality, reviews, pricing and availability.</p>
        </div>
        <div class="agent-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px; box-shadow: 0 12px 32px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 64px; height: 64px; border-radius: 20px; display: flex; align-items: center; justify-content: center; margin-bottom: 32px;"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2v20"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg></div>
          <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 12px;">Decision Support</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Presents the best recommendation with complete reasoning.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 5: REAL WORLD EXAMPLES (Light Gray) -->
  <section style="background-color: #f8fafc; padding: 160px 5%; width: 100%; box-sizing: border-box; border-top: 1px solid rgba(0,0,0,0.03);">
    <div style="max-width: 1400px; margin: 0 auto;">
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 64px; letter-spacing: -0.03em; text-align: center;">Real World Examples</h2>
      
      <div style="display: grid; grid-template-columns: 1fr; gap: 40px;">
        <!-- Example 1 -->
        <div class="example-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.05); border-radius: 32px; padding: 56px; box-shadow: 0 16px 40px rgba(0,0,0,0.02); display: flex; flex-direction: column; gap: 24px; transition: all 0.3s ease;">
          <div style="font-size: 14px; font-weight: 700; color: #4B5563; letter-spacing: 0.1em; text-transform: uppercase;">Example 1</div>
          <div style="font-size: 24px; font-weight: 500; color: #111827; line-height: 1.5; padding: 24px; background: #f8fafc; border-radius: 16px; border: 1px solid rgba(0,0,0,0.03);">"Find me a gaming laptop under $1,200 that can run Unreal Engine."</div>
          <div style="display: flex; gap: 16px; align-items: center; color: #2563EB;">
            <div style="background: rgba(37,99,235,0.1); width: 40px; height: 40px; border-radius: 12px; display: flex; align-items: center; justify-content: center;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m22 2-7 20-4-9-9-4Z"/><path d="M22 2 11 13"/></svg></div>
            <div style="font-size: 18px; font-weight: 500;">AI compares hundreds of devices before recommending the best match.</div>
          </div>
        </div>
        <!-- Example 2 -->
        <div class="example-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.05); border-radius: 32px; padding: 56px; box-shadow: 0 16px 40px rgba(0,0,0,0.02); display: flex; flex-direction: column; gap: 24px; transition: all 0.3s ease;">
          <div style="font-size: 14px; font-weight: 700; color: #4B5563; letter-spacing: 0.1em; text-transform: uppercase;">Example 2</div>
          <div style="font-size: 24px; font-weight: 500; color: #111827; line-height: 1.5; padding: 24px; background: #f8fafc; border-radius: 16px; border: 1px solid rgba(0,0,0,0.03);">"I need groceries for a family of four this week."</div>
          <div style="display: flex; gap: 16px; align-items: center; color: #2563EB;">
            <div style="background: rgba(37,99,235,0.1); width: 40px; height: 40px; border-radius: 12px; display: flex; align-items: center; justify-content: center;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m22 2-7 20-4-9-9-4Z"/><path d="M22 2 11 13"/></svg></div>
            <div style="font-size: 18px; font-weight: 500;">AI builds the basket automatically.</div>
          </div>
        </div>
        <!-- Example 3 -->
        <div class="example-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.05); border-radius: 32px; padding: 56px; box-shadow: 0 16px 40px rgba(0,0,0,0.02); display: flex; flex-direction: column; gap: 24px; transition: all 0.3s ease;">
          <div style="font-size: 14px; font-weight: 700; color: #4B5563; letter-spacing: 0.1em; text-transform: uppercase;">Example 3</div>
          <div style="font-size: 24px; font-weight: 500; color: #111827; line-height: 1.5; padding: 24px; background: #f8fafc; border-radius: 16px; border: 1px solid rgba(0,0,0,0.03);">"Buy the best travel backpack for Europe."</div>
          <div style="display: flex; gap: 16px; align-items: center; color: #2563EB;">
            <div style="background: rgba(37,99,235,0.1); width: 40px; height: 40px; border-radius: 12px; display: flex; align-items: center; justify-content: center;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m22 2-7 20-4-9-9-4Z"/><path d="M22 2 11 13"/></svg></div>
            <div style="font-size: 18px; font-weight: 500;">AI researches reviews, compares brands and places the order.</div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 6: WHY IT MATTERS (White) -->
  <section style="background-color: #ffffff; padding: 160px 5%; width: 100%; box-sizing: border-box;">
    <div style="max-width: 1400px; margin: 0 auto; text-align: center;">
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 80px; letter-spacing: -0.03em;">Why It Matters</h2>
      
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 32px;">
        <div class="matter-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.05); border-radius: 24px; padding: 48px 32px; box-shadow: 0 8px 32px rgba(0,0,0,0.02); transition: all 0.3s ease;">
          <h3 style="font-size: 24px; font-weight: 600; color: #111827; margin-bottom: 16px;">Hours Saved</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Less searching.<br/>More living.</p>
        </div>
        <div class="matter-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.05); border-radius: 24px; padding: 48px 32px; box-shadow: 0 8px 32px rgba(0,0,0,0.02); transition: all 0.3s ease;">
          <h3 style="font-size: 24px; font-weight: 600; color: #111827; margin-bottom: 16px;">Better Decisions</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">AI evaluates far more information than humans.</p>
        </div>
        <div class="matter-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.05); border-radius: 24px; padding: 48px 32px; box-shadow: 0 8px 32px rgba(0,0,0,0.02); transition: all 0.3s ease;">
          <h3 style="font-size: 24px; font-weight: 600; color: #111827; margin-bottom: 16px;">Reduced Cognitive Load</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Focus on outcomes instead of comparisons.</p>
        </div>
        <div class="matter-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.05); border-radius: 24px; padding: 48px 32px; box-shadow: 0 8px 32px rgba(0,0,0,0.02); transition: all 0.3s ease;">
          <h3 style="font-size: 24px; font-weight: 600; color: #111827; margin-bottom: 16px;">Future Ready</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Commerce becomes proactive instead of reactive.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 7: KEY PRINCIPLES (Light Gray) -->
  <section style="background-color: #f8fafc; padding: 160px 5%; width: 100%; box-sizing: border-box; border-top: 1px solid rgba(0,0,0,0.03);">
    <div style="max-width: 1000px; margin: 0 auto; text-align: center;">
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 64px; letter-spacing: -0.03em;">Key Principles</h2>
      
      <div style="background: #ffffff; border-radius: 32px; padding: 64px; border: 1px solid rgba(0,0,0,0.05); box-shadow: 0 16px 40px rgba(0,0,0,0.02); display: flex; flex-direction: column; gap: 32px;">
        <div style="font-size: 28px; font-weight: 600; color: #111827; display: flex; justify-content: center; align-items: center; gap: 16px;">
          <span style="color: #2563EB;">Intent</span> over Search
        </div>
        <div style="height: 1px; width: 60px; background: rgba(0,0,0,0.1); margin: 0 auto;"></div>
        <div style="font-size: 28px; font-weight: 600; color: #111827; display: flex; justify-content: center; align-items: center; gap: 16px;">
          <span style="color: #2563EB;">Automation</span> over Repetition
        </div>
        <div style="height: 1px; width: 60px; background: rgba(0,0,0,0.1); margin: 0 auto;"></div>
        <div style="font-size: 28px; font-weight: 600; color: #111827; display: flex; justify-content: center; align-items: center; gap: 16px;">
          <span style="color: #2563EB;">Confidence</span> over Guesswork
        </div>
        <div style="height: 1px; width: 60px; background: rgba(0,0,0,0.1); margin: 0 auto;"></div>
        <div style="font-size: 28px; font-weight: 600; color: #111827; display: flex; justify-content: center; align-items: center; gap: 16px;">
          <span style="color: #2563EB;">Recommendations</span> over Advertising
        </div>
        <div style="height: 1px; width: 60px; background: rgba(0,0,0,0.1); margin: 0 auto;"></div>
        <div style="font-size: 28px; font-weight: 600; color: #111827; display: flex; justify-content: center; align-items: center; gap: 16px;">
          <span style="color: #2563EB;">Human Approval</span> over Blind Automation
        </div>
      </div>
    </div>
  </section>

  <!-- FINAL CTA (White) -->
  <section style="background-color: #ffffff; padding: 180px 5% 240px 5%; width: 100%; box-sizing: border-box;">
    <div style="max-width: 1000px; margin: 0 auto; text-align: center;">
      <h2 style="font-size: 48px; font-weight: 600; color: #111827; margin-bottom: 24px; letter-spacing: -0.03em;">Experience the Future of Shopping</h2>
      <p style="font-size: 22px; color: #4B5563; line-height: 1.7; margin: 0 auto 48px auto; max-width: 700px;">See how intelligent AI agents transform shopping from a manual process into an autonomous experience.</p>
      
      <div style="display: flex; gap: 16px; justify-content: center; flex-wrap: wrap;">
        <a href="#" class="btn-primary" style="text-decoration: none; background: #2563EB; color: #ffffff; padding: 18px 40px; border-radius: 100px; font-size: 18px; font-weight: 600; transition: all 0.3s ease; display: inline-flex; align-items: center; gap: 12px;">
            Start Shopping With AI
        </a>
        <a href="mastering-ai-prompts.html" class="btn-secondary" style="text-decoration: none; background: #f8fafc; border: 1px solid rgba(0,0,0,0.1); color: #111827; padding: 18px 40px; border-radius: 100px; font-size: 18px; font-weight: 600; transition: all 0.3s ease;">
            Continue Learning
        </a>
      </div>
    </div>
  </section>

  <style>
    .compare-row {
      display: flex; align-items: center; gap: 16px; font-size: 18px; font-weight: 500; color: #4B5563; padding: 16px; border-radius: 12px; background: #f8fafc;
    }
    .compare-row-active {
      display: flex; align-items: center; gap: 16px; font-size: 18px; font-weight: 500; color: #ffffff; padding: 16px; border-radius: 12px; background: rgba(255,255,255,0.1);
    }
    .cross { color: #9CA3AF; display: flex; align-items: center; justify-content: center; }
    .check { color: #ffffff; display: flex; align-items: center; justify-content: center; }
    
    .problem-card:hover {
        transform: translateY(-4px);
        background: #ffffff !important;
        box-shadow: 0 12px 24px rgba(0,0,0,0.04) !important;
        border-color: rgba(0,0,0,0.1) !important;
    }
    .agent-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 24px 48px rgba(0,0,0,0.06) !important;
        border-color: rgba(37,99,235,0.2) !important;
    }
    .example-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 24px 48px rgba(0,0,0,0.04) !important;
        border-color: rgba(37,99,235,0.2) !important;
    }
    .matter-card:hover {
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
    
    @media (max-width: 991px) {
        .semantic-agentic-wrapper section {
            padding: 100px 5% !important;
        }
        .semantic-agentic-wrapper h1 {
            font-size: 48px !important;
        }
        .semantic-agentic-wrapper h2 {
            font-size: 32px !important;
        }
        .evolution-timeline {
            flex-direction: column !important;
            gap: 40px !important;
            margin-bottom: 40px !important;
        }
        .timeline-line-evo {
            display: none !important;
        }
        .problem-card {
            grid-column: span 2 !important;
        }
    }
    @media (max-width: 600px) {
        .semantic-agentic-wrapper section {
            padding: 80px 5% !important;
        }
        .semantic-agentic-wrapper h1 {
            font-size: 40px !important;
        }
        .semantic-agentic-wrapper .btn-primary, .semantic-agentic-wrapper .btn-secondary {
            width: 100%;
            justify-content: center;
        }
        .compare-row, .compare-row-active {
            font-size: 16px;
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
        new_section = bs4.BeautifulSoup(agentic_html, 'html.parser')
        wrapper.replace_with(new_section)
    else:
        # Fallback if no wrapper found
        section_to_replace = placeholder.find_parent('section')
        if section_to_replace:
            new_section = bs4.BeautifulSoup(agentic_html, 'html.parser')
            section_to_replace.replace_with(new_section)

with open('agentic-commerce-101.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Successfully built the Agentic Commerce 101 page.")
