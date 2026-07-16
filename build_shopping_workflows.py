import bs4

with open('shopping-workflows.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = bs4.BeautifulSoup(html, 'html.parser')

# 1. Update Title
if soup.title:
    soup.title.string = "Nexmart - Shopping Workflows"

# 2. Build Shopping Workflows Content HTML
shopping_html = """
<div class="semantic-shopping-wrapper" style="width: 100%; display: flex; flex-direction: column; font-family: 'Inter', system-ui, -apple-system, sans-serif;">
  
  <!-- HERO SECTION -->
  <section style="background-color: #ffffff; padding: 160px 5% 100px 5%; width: 100%; box-sizing: border-box; text-align: center;">
    <div style="max-width: 1000px; margin: 0 auto;">
      <h1 style="font-size: 64px; font-weight: 700; color: #111827; margin-bottom: 24px; letter-spacing: -0.04em; line-height: 1.1;">Shopping Workflows</h1>
      <p style="font-size: 22px; color: #4B5563; line-height: 1.6; margin: 0 auto; max-width: 800px;">Discover how Nexmart transforms a simple request into a complete shopping experience through intelligent AI workflows.</p>
    </div>
  </section>

  <!-- SECTION 1: THE COMPLETE SHOPPING JOURNEY (Light Gray) -->
  <section style="background-color: #f8fafc; padding: 160px 5%; width: 100%; box-sizing: border-box; border-top: 1px solid rgba(0,0,0,0.03);">
    <div style="max-width: 1400px; margin: 0 auto; text-align: center;">
      <div style="font-size: 14px; font-weight: 700; color: #2563EB; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 16px;">The Complete Shopping Journey</div>
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 80px; letter-spacing: -0.03em;">From Intent To Delivery</h2>
      
      <div class="journey-workflow" style="display: flex; justify-content: space-between; position: relative;">
        <div class="workflow-line" style="position: absolute; top: 40px; left: 8.33%; right: 8.33%; height: 2px; background: rgba(37,99,235,0.1); z-index: 0;"></div>
        
        <div class="workflow-step" style="position: relative; z-index: 1; flex: 1; padding: 0 16px;">
          <div style="background: #ffffff; border: 2px solid #2563EB; width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 24px auto; color: #2563EB; font-weight: 700; font-size: 24px; box-shadow: 0 8px 24px rgba(37,99,235,0.1);">1</div>
          <h4 style="font-size: 18px; font-weight: 600; color: #111827; margin-bottom: 8px;">Describe Your Need</h4>
          <p style="font-size: 14px; color: #4B5563; line-height: 1.5; margin: 0;">Tell Nexmart what you're looking for.</p>
        </div>

        <div class="workflow-step" style="position: relative; z-index: 1; flex: 1; padding: 0 16px;">
          <div style="background: #ffffff; border: 2px solid #2563EB; width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 24px auto; color: #2563EB; font-weight: 700; font-size: 24px; box-shadow: 0 8px 24px rgba(37,99,235,0.1);">2</div>
          <h4 style="font-size: 18px; font-weight: 600; color: #111827; margin-bottom: 8px;">AI Research</h4>
          <p style="font-size: 14px; color: #4B5563; line-height: 1.5; margin: 0;">Your AI agents search thousands of products across trusted suppliers.</p>
        </div>

        <div class="workflow-step" style="position: relative; z-index: 1; flex: 1; padding: 0 16px;">
          <div style="background: #ffffff; border: 2px solid #2563EB; width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 24px auto; color: #2563EB; font-weight: 700; font-size: 24px; box-shadow: 0 8px 24px rgba(37,99,235,0.1);">3</div>
          <h4 style="font-size: 18px; font-weight: 600; color: #111827; margin-bottom: 8px;">Intelligent Comparison</h4>
          <p style="font-size: 14px; color: #4B5563; line-height: 1.5; margin: 0;">Products are evaluated based on price, quality, reviews, delivery, and overall value.</p>
        </div>

        <div class="workflow-step" style="position: relative; z-index: 1; flex: 1; padding: 0 16px;">
          <div style="background: #ffffff; border: 2px solid #2563EB; width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 24px auto; color: #2563EB; font-weight: 700; font-size: 24px; box-shadow: 0 8px 24px rgba(37,99,235,0.1);">4</div>
          <h4 style="font-size: 18px; font-weight: 600; color: #111827; margin-bottom: 8px;">Recommendation</h4>
          <p style="font-size: 14px; color: #4B5563; line-height: 1.5; margin: 0;">The AI presents the best options with transparent reasoning.</p>
        </div>

        <div class="workflow-step" style="position: relative; z-index: 1; flex: 1; padding: 0 16px;">
          <div style="background: #ffffff; border: 2px solid #2563EB; width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 24px auto; color: #2563EB; font-weight: 700; font-size: 24px; box-shadow: 0 8px 24px rgba(37,99,235,0.1);">5</div>
          <h4 style="font-size: 18px; font-weight: 600; color: #111827; margin-bottom: 8px;">Approval</h4>
          <p style="font-size: 14px; color: #4B5563; line-height: 1.5; margin: 0;">Review the recommendation and approve the purchase.</p>
        </div>

        <div class="workflow-step" style="position: relative; z-index: 1; flex: 1; padding: 0 16px;">
          <div style="background: #2563EB; border: 2px solid #2563EB; width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 24px auto; color: #ffffff; font-weight: 700; font-size: 24px; box-shadow: 0 12px 32px rgba(37,99,235,0.2);">6</div>
          <h4 style="font-size: 18px; font-weight: 600; color: #111827; margin-bottom: 8px;">Delivery</h4>
          <p style="font-size: 14px; color: #4B5563; line-height: 1.5; margin: 0;">Track your order until it reaches your doorstep.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 2: BEHIND EVERY RECOMMENDATION (White) -->
  <section style="background-color: #ffffff; padding: 160px 5%; width: 100%; box-sizing: border-box;">
    <div style="max-width: 1400px; margin: 0 auto;">
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 64px; letter-spacing: -0.03em; text-align: center;">Behind Every Recommendation</h2>
      
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 32px;">
        <div class="feature-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px; box-shadow: 0 12px 32px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 64px; height: 64px; border-radius: 20px; display: flex; align-items: center; justify-content: center; margin-bottom: 32px;"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg></div>
          <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 12px;">Market Research</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">AI searches multiple suppliers simultaneously.</p>
        </div>
        <div class="feature-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px; box-shadow: 0 12px 32px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 64px; height: 64px; border-radius: 20px; display: flex; align-items: center; justify-content: center; margin-bottom: 32px;"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2v20"/><path d="m17 5 5 5-5 5"/><path d="m7 19-5-5 5-5"/></svg></div>
          <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 12px;">Quality Analysis</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Reviews, ratings, and product history are evaluated.</p>
        </div>
        <div class="feature-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px; box-shadow: 0 12px 32px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 64px; height: 64px; border-radius: 20px; display: flex; align-items: center; justify-content: center; margin-bottom: 32px;"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><line x1="12" x2="12" y1="2" y2="22"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg></div>
          <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 12px;">Price Intelligence</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">The AI identifies the best value rather than simply the lowest price.</p>
        </div>
        <div class="feature-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px; box-shadow: 0 12px 32px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 64px; height: 64px; border-radius: 20px; display: flex; align-items: center; justify-content: center; margin-bottom: 32px;"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect width="16" height="16" x="4" y="4" rx="2"/><path d="M4 12h16"/><path d="M12 4v16"/></svg></div>
          <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 12px;">Delivery Optimization</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Shipping speed, reliability, and availability are factored into every recommendation.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 3: REAL SHOPPING WORKFLOWS (Light Gray) -->
  <section style="background-color: #f8fafc; padding: 160px 5%; width: 100%; box-sizing: border-box; border-top: 1px solid rgba(0,0,0,0.03);">
    <div style="max-width: 1400px; margin: 0 auto;">
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 64px; letter-spacing: -0.03em; text-align: center;">Real Shopping Workflows</h2>
      
      <div style="display: grid; grid-template-columns: 1fr; gap: 40px;">
        <!-- Workflow 1 -->
        <div class="showcase-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.05); border-radius: 32px; padding: 56px; box-shadow: 0 16px 40px rgba(0,0,0,0.02); display: flex; flex-direction: column; gap: 24px; transition: all 0.3s ease;">
          <div style="display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid rgba(0,0,0,0.05); padding-bottom: 24px;">
            <div style="font-size: 24px; font-weight: 600; color: #111827;">Home Office Setup</div>
            <div style="font-size: 14px; font-weight: 700; color: #4B5563; letter-spacing: 0.1em; text-transform: uppercase;">Workflow 1</div>
          </div>
          
          <div style="display: flex; flex-direction: column; gap: 8px;">
             <div style="font-size: 14px; font-weight: 700; color: #4B5563; text-transform: uppercase; letter-spacing: 0.05em;">Prompt:</div>
             <div style="font-size: 24px; font-weight: 500; color: #111827; line-height: 1.5; padding: 24px; background: #f8fafc; border-radius: 16px; border: 1px solid rgba(0,0,0,0.03);">"I need everything for a productive home office with a $1,000 budget."</div>
          </div>

          <div style="display: flex; flex-direction: column; gap: 8px; margin-top: 8px;">
             <div style="font-size: 14px; font-weight: 700; color: #2563EB; text-transform: uppercase; letter-spacing: 0.05em;">Result:</div>
             <div style="display: flex; gap: 16px; align-items: center; color: #111827;">
               <div style="background: #eff6ff; color: #2563EB; width: 48px; height: 48px; border-radius: 12px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12A10 10 0 1 1 12 2a10 10 0 0 1 10 10z"/><circle cx="12" cy="12" r="3"/></svg></div>
               <div style="font-size: 18px; font-weight: 500;">AI creates a complete shopping list, compares products, and optimizes the budget.</div>
             </div>
          </div>
        </div>

        <!-- Workflow 2 -->
        <div class="showcase-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.05); border-radius: 32px; padding: 56px; box-shadow: 0 16px 40px rgba(0,0,0,0.02); display: flex; flex-direction: column; gap: 24px; transition: all 0.3s ease;">
          <div style="display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid rgba(0,0,0,0.05); padding-bottom: 24px;">
            <div style="font-size: 24px; font-weight: 600; color: #111827;">Weekly Grocery Shopping</div>
            <div style="font-size: 14px; font-weight: 700; color: #4B5563; letter-spacing: 0.1em; text-transform: uppercase;">Workflow 2</div>
          </div>
          
          <div style="display: flex; flex-direction: column; gap: 8px;">
             <div style="font-size: 14px; font-weight: 700; color: #4B5563; text-transform: uppercase; letter-spacing: 0.05em;">Prompt:</div>
             <div style="font-size: 24px; font-weight: 500; color: #111827; line-height: 1.5; padding: 24px; background: #f8fafc; border-radius: 16px; border: 1px solid rgba(0,0,0,0.03);">"Plan healthy groceries for a vegetarian family of four."</div>
          </div>

          <div style="display: flex; flex-direction: column; gap: 8px; margin-top: 8px;">
             <div style="font-size: 14px; font-weight: 700; color: #2563EB; text-transform: uppercase; letter-spacing: 0.05em;">Result:</div>
             <div style="display: flex; gap: 16px; align-items: center; color: #111827;">
               <div style="background: #eff6ff; color: #2563EB; width: 48px; height: 48px; border-radius: 12px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12A10 10 0 1 1 12 2a10 10 0 0 1 10 10z"/><circle cx="12" cy="12" r="3"/></svg></div>
               <div style="font-size: 18px; font-weight: 500;">AI builds a balanced grocery basket and recommends the best stores.</div>
             </div>
          </div>
        </div>

        <!-- Workflow 3 -->
        <div class="showcase-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.05); border-radius: 32px; padding: 56px; box-shadow: 0 16px 40px rgba(0,0,0,0.02); display: flex; flex-direction: column; gap: 24px; transition: all 0.3s ease;">
          <div style="display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid rgba(0,0,0,0.05); padding-bottom: 24px;">
            <div style="font-size: 24px; font-weight: 600; color: #111827;">Travel Planning</div>
            <div style="font-size: 14px; font-weight: 700; color: #4B5563; letter-spacing: 0.1em; text-transform: uppercase;">Workflow 3</div>
          </div>
          
          <div style="display: flex; flex-direction: column; gap: 8px;">
             <div style="font-size: 14px; font-weight: 700; color: #4B5563; text-transform: uppercase; letter-spacing: 0.05em;">Prompt:</div>
             <div style="font-size: 24px; font-weight: 500; color: #111827; line-height: 1.5; padding: 24px; background: #f8fafc; border-radius: 16px; border: 1px solid rgba(0,0,0,0.03);">"Help me prepare for a two-week hiking trip."</div>
          </div>

          <div style="display: flex; flex-direction: column; gap: 8px; margin-top: 8px;">
             <div style="font-size: 14px; font-weight: 700; color: #2563EB; text-transform: uppercase; letter-spacing: 0.05em;">Result:</div>
             <div style="display: flex; gap: 16px; align-items: center; color: #111827;">
               <div style="background: #eff6ff; color: #2563EB; width: 48px; height: 48px; border-radius: 12px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12A10 10 0 1 1 12 2a10 10 0 0 1 10 10z"/><circle cx="12" cy="12" r="3"/></svg></div>
               <div style="font-size: 18px; font-weight: 500;">AI recommends equipment, compares brands, and builds a complete shopping checklist.</div>
             </div>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- SECTION 4: BENEFITS (White) -->
  <section style="background-color: #ffffff; padding: 160px 5%; width: 100%; box-sizing: border-box;">
    <div style="max-width: 1400px; margin: 0 auto;">
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 64px; letter-spacing: -0.03em; text-align: center;">Benefits</h2>
      
      <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 24px;">
        <div class="benefit-card" style="background: #f8fafc; border: 1px solid rgba(0,0,0,0.04); border-radius: 20px; padding: 40px; display: flex; align-items: flex-start; gap: 24px; transition: all 0.3s ease;">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 56px; height: 56px; border-radius: 16px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg></div>
          <div>
            <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin: 0 0 12px 0;">Save Time</h3>
            <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Reduce hours of research to minutes.</p>
          </div>
        </div>
        <div class="benefit-card" style="background: #f8fafc; border: 1px solid rgba(0,0,0,0.04); border-radius: 20px; padding: 40px; display: flex; align-items: flex-start; gap: 24px; transition: all 0.3s ease;">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 56px; height: 56px; border-radius: 16px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20"/><path d="m17 5 5 5-5 5"/><path d="m7 19-5-5 5-5"/></svg></div>
          <div>
            <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin: 0 0 12px 0;">Better Decisions</h3>
            <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Recommendations backed by data.</p>
          </div>
        </div>
        <div class="benefit-card" style="background: #f8fafc; border: 1px solid rgba(0,0,0,0.04); border-radius: 20px; padding: 40px; display: flex; align-items: flex-start; gap: 24px; transition: all 0.3s ease;">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 56px; height: 56px; border-radius: 16px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" x2="12" y1="2" y2="22"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg></div>
          <div>
            <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin: 0 0 12px 0;">Lower Costs</h3>
            <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Find the best overall value.</p>
          </div>
        </div>
        <div class="benefit-card" style="background: #f8fafc; border: 1px solid rgba(0,0,0,0.04); border-radius: 20px; padding: 40px; display: flex; align-items: flex-start; gap: 24px; transition: all 0.3s ease;">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 56px; height: 56px; border-radius: 16px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg></div>
          <div>
            <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin: 0 0 12px 0;">Less Stress</h3>
            <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Let AI handle repetitive comparison work.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 5: WORKFLOW BEST PRACTICES (Blue Tint) -->
  <section style="background-color: #eff6ff; padding: 160px 5%; width: 100%; box-sizing: border-box;">
    <div style="max-width: 1400px; margin: 0 auto; text-align: center;">
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 64px; letter-spacing: -0.03em;">Workflow Best Practices</h2>
      
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 32px;">
        <div class="practice-item" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 24px; padding: 40px; box-shadow: 0 12px 32px rgba(37,99,235,0.04); display: flex; align-items: center; gap: 24px; transition: all 0.3s ease; text-align: left;">
          <div style="color: #2563EB;"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg></div>
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin: 0;">Be Specific</h3>
        </div>
        <div class="practice-item" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 24px; padding: 40px; box-shadow: 0 12px 32px rgba(37,99,235,0.04); display: flex; align-items: center; gap: 24px; transition: all 0.3s ease; text-align: left;">
          <div style="color: #2563EB;"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg></div>
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin: 0;">Provide Context</h3>
        </div>
        <div class="practice-item" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 24px; padding: 40px; box-shadow: 0 12px 32px rgba(37,99,235,0.04); display: flex; align-items: center; gap: 24px; transition: all 0.3s ease; text-align: left;">
          <div style="color: #2563EB;"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg></div>
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin: 0;">Set Priorities</h3>
        </div>
        <div class="practice-item" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 24px; padding: 40px; box-shadow: 0 12px 32px rgba(37,99,235,0.04); display: flex; align-items: center; gap: 24px; transition: all 0.3s ease; text-align: left;">
          <div style="color: #2563EB;"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg></div>
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin: 0;">Review Recommendations</h3>
        </div>
        <div class="practice-item" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 24px; padding: 40px; box-shadow: 0 12px 32px rgba(37,99,235,0.04); display: flex; align-items: center; gap: 24px; transition: all 0.3s ease; text-align: left;">
          <div style="color: #2563EB;"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg></div>
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin: 0;">Save Successful Workflows</h3>
        </div>
        <div class="practice-item" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 24px; padding: 40px; box-shadow: 0 12px 32px rgba(37,99,235,0.04); display: flex; align-items: center; gap: 24px; transition: all 0.3s ease; text-align: left;">
          <div style="color: #2563EB;"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg></div>
          <h3 style="font-size: 20px; font-weight: 600; color: #111827; margin: 0;">Continue Learning</h3>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 6: FREQUENTLY ASKED QUESTIONS (White) -->
  <section style="background-color: #ffffff; padding: 160px 5%; width: 100%; box-sizing: border-box;">
    <div style="max-width: 800px; margin: 0 auto;">
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 64px; letter-spacing: -0.03em; text-align: center;">Frequently Asked Questions</h2>
      
      <div style="display: flex; flex-direction: column; gap: 16px;">
        
        <div class="faq-accordion" style="border: 1px solid rgba(0,0,0,0.08); border-radius: 16px; background: #ffffff; overflow: hidden; transition: all 0.3s ease;">
          <button class="faq-btn" style="width: 100%; text-align: left; background: none; border: none; padding: 24px 32px; font-size: 20px; font-weight: 600; color: #111827; cursor: pointer; display: flex; justify-content: space-between; align-items: center; font-family: inherit;">
            How long does a workflow take?
            <svg class="faq-icon" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="transition: transform 0.3s ease;"><path d="m6 9 6 6 6-6"/></svg>
          </button>
          <div class="faq-content" style="max-height: 0; overflow: hidden; transition: max-height 0.3s ease;">
            <p style="padding: 0 32px 24px 32px; margin: 0; font-size: 16px; color: #4B5563; line-height: 1.6;">Most shopping workflows take less than two minutes from your initial prompt to a fully researched recommendation. More complex requests involving dozens of variables may take slightly longer.</p>
          </div>
        </div>

        <div class="faq-accordion" style="border: 1px solid rgba(0,0,0,0.08); border-radius: 16px; background: #ffffff; overflow: hidden; transition: all 0.3s ease;">
          <button class="faq-btn" style="width: 100%; text-align: left; background: none; border: none; padding: 24px 32px; font-size: 20px; font-weight: 600; color: #111827; cursor: pointer; display: flex; justify-content: space-between; align-items: center; font-family: inherit;">
            Can I modify recommendations?
            <svg class="faq-icon" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="transition: transform 0.3s ease;"><path d="m6 9 6 6 6-6"/></svg>
          </button>
          <div class="faq-content" style="max-height: 0; overflow: hidden; transition: max-height 0.3s ease;">
            <p style="padding: 0 32px 24px 32px; margin: 0; font-size: 16px; color: #4B5563; line-height: 1.6;">Yes. You have complete control. If you don't like a recommendation, simply tell the AI what needs to change (e.g., "Find something cheaper" or "Show me red options instead").</p>
          </div>
        </div>

        <div class="faq-accordion" style="border: 1px solid rgba(0,0,0,0.08); border-radius: 16px; background: #ffffff; overflow: hidden; transition: all 0.3s ease;">
          <button class="faq-btn" style="width: 100%; text-align: left; background: none; border: none; padding: 24px 32px; font-size: 20px; font-weight: 600; color: #111827; cursor: pointer; display: flex; justify-content: space-between; align-items: center; font-family: inherit;">
            Does AI explain its decisions?
            <svg class="faq-icon" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="transition: transform 0.3s ease;"><path d="m6 9 6 6 6-6"/></svg>
          </button>
          <div class="faq-content" style="max-height: 0; overflow: hidden; transition: max-height 0.3s ease;">
            <p style="padding: 0 32px 24px 32px; margin: 0; font-size: 16px; color: #4B5563; line-height: 1.6;">Absolutely. Transparency is a core principle. Every recommendation includes a breakdown of exactly why the AI selected that specific product over the alternatives.</p>
          </div>
        </div>

        <div class="faq-accordion" style="border: 1px solid rgba(0,0,0,0.08); border-radius: 16px; background: #ffffff; overflow: hidden; transition: all 0.3s ease;">
          <button class="faq-btn" style="width: 100%; text-align: left; background: none; border: none; padding: 24px 32px; font-size: 20px; font-weight: 600; color: #111827; cursor: pointer; display: flex; justify-content: space-between; align-items: center; font-family: inherit;">
            Can I save workflows?
            <svg class="faq-icon" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="transition: transform 0.3s ease;"><path d="m6 9 6 6 6-6"/></svg>
          </button>
          <div class="faq-content" style="max-height: 0; overflow: hidden; transition: max-height 0.3s ease;">
            <p style="padding: 0 32px 24px 32px; margin: 0; font-size: 16px; color: #4B5563; line-height: 1.6;">Yes. If you frequently purchase similar baskets (like weekly groceries or monthly office supplies), you can save the workflow and re-run it with a single click in the future.</p>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- FINAL CTA (Light Gray) -->
  <section style="background-color: #f8fafc; padding: 180px 5% 240px 5%; width: 100%; box-sizing: border-box; border-top: 1px solid rgba(0,0,0,0.03);">
    <div style="max-width: 1000px; margin: 0 auto; text-align: center;">
      <h2 style="font-size: 48px; font-weight: 600; color: #111827; margin-bottom: 24px; letter-spacing: -0.03em;">Ready To Experience Intelligent Shopping?</h2>
      <p style="font-size: 22px; color: #4B5563; line-height: 1.7; margin: 0 auto 48px auto; max-width: 700px;">Your AI shopping workflow begins with a single conversation.</p>
      
      <div style="display: flex; gap: 16px; justify-content: center; flex-wrap: wrap;">
        <a href="#" class="btn-primary" style="text-decoration: none; background: #2563EB; color: #ffffff; padding: 18px 40px; border-radius: 100px; font-size: 18px; font-weight: 600; transition: all 0.3s ease; display: inline-flex; align-items: center; gap: 12px;">
            Start Shopping With AI
        </a>
        <a href="orders-and-returns.html" class="btn-secondary" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.1); color: #111827; padding: 18px 40px; border-radius: 100px; font-size: 18px; font-weight: 600; transition: all 0.3s ease; box-shadow: 0 4px 12px rgba(0,0,0,0.02);">
            Continue Learning
        </a>
      </div>
    </div>
  </section>

  <style>
    .feature-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 24px 48px rgba(37,99,235,0.08) !important;
        border-color: rgba(37,99,235,0.2) !important;
    }
    .showcase-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 24px 48px rgba(0,0,0,0.04) !important;
        border-color: rgba(37,99,235,0.2) !important;
    }
    .benefit-card:hover {
        transform: translateY(-4px);
        background: #ffffff !important;
        box-shadow: 0 16px 32px rgba(0,0,0,0.04) !important;
        border-color: rgba(37,99,235,0.2) !important;
    }
    .practice-item:hover {
        transform: translateY(-4px);
        border-color: rgba(37,99,235,0.3) !important;
        box-shadow: 0 16px 40px rgba(37,99,235,0.08) !important;
    }
    .btn-primary:hover {
        background: #1d4ed8 !important;
        transform: translateY(-2px);
    }
    .btn-secondary:hover {
        background: #f8fafc !important;
        border-color: rgba(0,0,0,0.2) !important;
        transform: translateY(-2px);
    }
    
    .faq-accordion.is-open {
        border-color: #2563EB !important;
        box-shadow: 0 12px 24px rgba(37,99,235,0.08) !important;
    }
    .faq-accordion.is-open .faq-icon {
        transform: rotate(180deg);
        color: #2563EB;
    }
    
    @media (max-width: 991px) {
        .semantic-shopping-wrapper section {
            padding: 100px 5% !important;
        }
        .semantic-shopping-wrapper h1 {
            font-size: 48px !important;
        }
        .semantic-shopping-wrapper h2 {
            font-size: 32px !important;
        }
        .journey-workflow {
            flex-direction: column !important;
            gap: 40px !important;
        }
        .workflow-line {
            display: none !important;
        }
        .benefit-card {
            grid-column: span 2 !important;
        }
    }
    @media (max-width: 600px) {
        .semantic-shopping-wrapper section {
            padding: 80px 5% !important;
        }
        .semantic-shopping-wrapper h1 {
            font-size: 40px !important;
        }
        .semantic-shopping-wrapper .btn-primary, .semantic-shopping-wrapper .btn-secondary {
            width: 100%;
            justify-content: center;
        }
        .faq-btn {
            font-size: 18px !important;
            padding: 20px 24px !important;
        }
        .faq-content p {
            padding: 0 24px 24px 24px !important;
        }
    }
  </style>

  <script>
    document.addEventListener('DOMContentLoaded', function() {
        const faqs = document.querySelectorAll('.faq-btn');
        faqs.forEach(btn => {
            btn.addEventListener('click', function() {
                const parent = this.parentElement;
                const content = this.nextElementSibling;
                
                // Toggle current
                if (parent.classList.contains('is-open')) {
                    parent.classList.remove('is-open');
                    content.style.maxHeight = null;
                } else {
                    // Close others (optional, but good UX)
                    document.querySelectorAll('.faq-accordion').forEach(acc => {
                        acc.classList.remove('is-open');
                        acc.querySelector('.faq-content').style.maxHeight = null;
                    });
                    
                    parent.classList.add('is-open');
                    content.style.maxHeight = content.scrollHeight + "px";
                }
            });
        });
    });
  </script>
</div>
"""

# Replace placeholder section
placeholder = soup.find(string=lambda text: text and 'Content Coming Soon' in text)
if placeholder:
    # Depending on how the placeholder was generated, it might be inside semantic-placeholder-wrapper
    wrapper = placeholder.find_parent('div', class_='semantic-placeholder-wrapper')
    if wrapper:
        new_section = bs4.BeautifulSoup(shopping_html, 'html.parser')
        wrapper.replace_with(new_section)
    else:
        # Fallback if no wrapper found
        section_to_replace = placeholder.find_parent('section')
        if section_to_replace:
            new_section = bs4.BeautifulSoup(shopping_html, 'html.parser')
            section_to_replace.replace_with(new_section)

with open('shopping-workflows.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Successfully built the Shopping Workflows page.")
