import bs4

with open('orders-and-returns.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = bs4.BeautifulSoup(html, 'html.parser')

# 1. Update Title
if soup.title:
    soup.title.string = "Nexmart - Orders & Returns"

# 2. Build Orders & Returns Content HTML
orders_html = """
<div class="semantic-orders-wrapper" style="width: 100%; display: flex; flex-direction: column; font-family: 'Inter', system-ui, -apple-system, sans-serif;">
  
  <!-- HERO SECTION -->
  <section style="background-color: #ffffff; padding: 160px 5% 100px 5%; width: 100%; box-sizing: border-box; text-align: center;">
    <div style="max-width: 1000px; margin: 0 auto;">
      <h1 style="font-size: 64px; font-weight: 700; color: #111827; margin-bottom: 24px; letter-spacing: -0.04em; line-height: 1.1;">Orders & Returns</h1>
      <p style="font-size: 22px; color: #4B5563; line-height: 1.6; margin: 0 auto; max-width: 800px;">Learn how Nexmart manages your purchases from order confirmation to doorstep delivery, including tracking, cancellations, returns, and refunds.</p>
    </div>
  </section>

  <!-- SECTION 1: THE ORDER JOURNEY (Light Gray) -->
  <section style="background-color: #f8fafc; padding: 160px 5%; width: 100%; box-sizing: border-box; border-top: 1px solid rgba(0,0,0,0.03);">
    <div style="max-width: 1400px; margin: 0 auto; text-align: center;">
      <div style="font-size: 14px; font-weight: 700; color: #2563EB; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 16px;">The Order Journey</div>
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 80px; letter-spacing: -0.03em;">From Checkout To Delivery</h2>
      
      <div class="journey-workflow" style="display: flex; justify-content: space-between; position: relative;">
        <div class="workflow-line" style="position: absolute; top: 40px; left: 8.33%; right: 8.33%; height: 2px; background: rgba(37,99,235,0.1); z-index: 0;"></div>
        
        <div class="workflow-step" style="position: relative; z-index: 1; flex: 1; padding: 0 16px;">
          <div style="background: #ffffff; border: 2px solid #2563EB; width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 24px auto; color: #2563EB; font-weight: 700; font-size: 24px; box-shadow: 0 8px 24px rgba(37,99,235,0.1);">1</div>
          <h4 style="font-size: 18px; font-weight: 600; color: #111827; margin-bottom: 8px;">Order Confirmed</h4>
          <p style="font-size: 14px; color: #4B5563; line-height: 1.5; margin: 0;">Your purchase is successfully received and logged.</p>
        </div>

        <div class="workflow-step" style="position: relative; z-index: 1; flex: 1; padding: 0 16px;">
          <div style="background: #ffffff; border: 2px solid #2563EB; width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 24px auto; color: #2563EB; font-weight: 700; font-size: 24px; box-shadow: 0 8px 24px rgba(37,99,235,0.1);">2</div>
          <h4 style="font-size: 18px; font-weight: 600; color: #111827; margin-bottom: 8px;">AI Verification</h4>
          <p style="font-size: 14px; color: #4B5563; line-height: 1.5; margin: 0;">Agents verify supplier stock, address, and logistics.</p>
        </div>

        <div class="workflow-step" style="position: relative; z-index: 1; flex: 1; padding: 0 16px;">
          <div style="background: #ffffff; border: 2px solid #2563EB; width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 24px auto; color: #2563EB; font-weight: 700; font-size: 24px; box-shadow: 0 8px 24px rgba(37,99,235,0.1);">3</div>
          <h4 style="font-size: 18px; font-weight: 600; color: #111827; margin-bottom: 8px;">Seller Processing</h4>
          <p style="font-size: 14px; color: #4B5563; line-height: 1.5; margin: 0;">The supplier prepares your items for dispatch.</p>
        </div>

        <div class="workflow-step" style="position: relative; z-index: 1; flex: 1; padding: 0 16px;">
          <div style="background: #ffffff; border: 2px solid #2563EB; width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 24px auto; color: #2563EB; font-weight: 700; font-size: 24px; box-shadow: 0 8px 24px rgba(37,99,235,0.1);">4</div>
          <h4 style="font-size: 18px; font-weight: 600; color: #111827; margin-bottom: 8px;">Shipment</h4>
          <p style="font-size: 14px; color: #4B5563; line-height: 1.5; margin: 0;">Your package leaves the fulfillment center.</p>
        </div>

        <div class="workflow-step" style="position: relative; z-index: 1; flex: 1; padding: 0 16px;">
          <div style="background: #ffffff; border: 2px solid #2563EB; width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 24px auto; color: #2563EB; font-weight: 700; font-size: 24px; box-shadow: 0 8px 24px rgba(37,99,235,0.1);">5</div>
          <h4 style="font-size: 18px; font-weight: 600; color: #111827; margin-bottom: 8px;">Delivery Tracking</h4>
          <p style="font-size: 14px; color: #4B5563; line-height: 1.5; margin: 0;">Real-time transit updates to your app.</p>
        </div>

        <div class="workflow-step" style="position: relative; z-index: 1; flex: 1; padding: 0 16px;">
          <div style="background: #2563EB; border: 2px solid #2563EB; width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 24px auto; color: #ffffff; font-weight: 700; font-size: 24px; box-shadow: 0 12px 32px rgba(37,99,235,0.2);">6</div>
          <h4 style="font-size: 18px; font-weight: 600; color: #111827; margin-bottom: 8px;">Delivered</h4>
          <p style="font-size: 14px; color: #4B5563; line-height: 1.5; margin: 0;">Your items safely arrive at their destination.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 2: TRACK EVERY ORDER (White) -->
  <section style="background-color: #ffffff; padding: 160px 5%; width: 100%; box-sizing: border-box;">
    <div style="max-width: 1400px; margin: 0 auto;">
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 64px; letter-spacing: -0.03em; text-align: center;">Real-Time Order Visibility</h2>
      
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 32px;">
        <div class="feature-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px; box-shadow: 0 12px 32px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 64px; height: 64px; border-radius: 20px; display: flex; align-items: center; justify-content: center; margin-bottom: 32px;"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="10"/><path d="M12 2v20"/><path d="m15 9-3-3-3 3"/></svg></div>
          <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 12px;">Live Tracking</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Monitor your shipment in real time.</p>
        </div>
        <div class="feature-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px; box-shadow: 0 12px 32px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 64px; height: 64px; border-radius: 20px; display: flex; align-items: center; justify-content: center; margin-bottom: 32px;"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="m22 2-7 20-4-9-9-4Z"/><path d="M22 2 11 13"/></svg></div>
          <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 12px;">Delivery Updates</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Receive automatic notifications throughout the journey.</p>
        </div>
        <div class="feature-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px; box-shadow: 0 12px 32px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 64px; height: 64px; border-radius: 20px; display: flex; align-items: center; justify-content: center; margin-bottom: 32px;"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg></div>
          <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 12px;">Estimated Arrival</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Know exactly when your package is expected.</p>
        </div>
        <div class="feature-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.06); border-radius: 24px; padding: 48px; box-shadow: 0 12px 32px rgba(0,0,0,0.02); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 64px; height: 64px; border-radius: 20px; display: flex; align-items: center; justify-content: center; margin-bottom: 32px;"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M14 2H6a2 2 0 0 0-2 2v16c0 1.1.9 2 2 2h12a2 2 0 0 0 2-2V8l-6-6z"/><path d="M14 3v5h5"/><path d="M16 13H8"/><path d="M16 17H8"/><path d="M10 9H8"/></svg></div>
          <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 12px;">Order History</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Access every purchase from your Nexmart account.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 3: MANAGING YOUR ORDERS (Blue Tint) -->
  <section style="background-color: #eff6ff; padding: 160px 5%; width: 100%; box-sizing: border-box;">
    <div style="max-width: 1400px; margin: 0 auto;">
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 64px; letter-spacing: -0.03em; text-align: center;">Everything In One Place</h2>
      
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 32px;">
        <div class="manage-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 24px; padding: 48px; box-shadow: 0 12px 32px rgba(37,99,235,0.04); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 56px; height: 56px; border-radius: 16px; display: flex; align-items: center; justify-content: center; margin-bottom: 24px;"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/></svg></div>
          <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 12px;">Modify Orders</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Update eligible orders before shipment.</p>
        </div>
        <div class="manage-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 24px; padding: 48px; box-shadow: 0 12px 32px rgba(37,99,235,0.04); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 56px; height: 56px; border-radius: 16px; display: flex; align-items: center; justify-content: center; margin-bottom: 24px;"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg></div>
          <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 12px;">Cancel Orders</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Cancel qualifying purchases with a single click.</p>
        </div>
        <div class="manage-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 24px; padding: 48px; box-shadow: 0 12px 32px rgba(37,99,235,0.04); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 56px; height: 56px; border-radius: 16px; display: flex; align-items: center; justify-content: center; margin-bottom: 24px;"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M14 2H6a2 2 0 0 0-2 2v16c0 1.1.9 2 2 2h12a2 2 0 0 0 2-2V8l-6-6z"/><path d="M14 3v5h5"/><path d="M12 18v-6"/><path d="M9 15l3 3 3-3"/></svg></div>
          <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 12px;">Invoices</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Download purchase invoices anytime.</p>
        </div>
        <div class="manage-card" style="background: #ffffff; border: 1px solid rgba(0,0,0,0.04); border-radius: 24px; padding: 48px; box-shadow: 0 12px 32px rgba(37,99,235,0.04); display: flex; flex-direction: column; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 56px; height: 56px; border-radius: 16px; display: flex; align-items: center; justify-content: center; margin-bottom: 24px;"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg></div>
          <h3 style="font-size: 22px; font-weight: 600; color: #111827; margin-bottom: 12px;">Support</h3>
          <p style="font-size: 16px; color: #4B5563; line-height: 1.6; margin: 0;">Contact Nexmart Support directly from your order.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 4: RETURNS MADE SIMPLE (White) -->
  <section style="background-color: #ffffff; padding: 160px 5%; width: 100%; box-sizing: border-box;">
    <div style="max-width: 1400px; margin: 0 auto; text-align: center;">
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 80px; letter-spacing: -0.03em;">A Hassle-Free Return Experience</h2>
      
      <div class="return-workflow" style="display: flex; justify-content: space-between; position: relative; margin-bottom: 64px;">
        <div class="workflow-line" style="position: absolute; top: 32px; left: 12.5%; right: 12.5%; height: 2px; background: rgba(37,99,235,0.1); z-index: 0;"></div>
        
        <div class="workflow-step" style="position: relative; z-index: 1; flex: 1; padding: 0 16px;">
          <div style="background: #ffffff; border: 2px solid #2563EB; width: 64px; height: 64px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 24px auto; color: #2563EB; font-weight: 700; font-size: 20px;">1</div>
          <h4 style="font-size: 18px; font-weight: 600; color: #111827; margin-bottom: 8px;">Request Return</h4>
        </div>

        <div class="workflow-step" style="position: relative; z-index: 1; flex: 1; padding: 0 16px;">
          <div style="background: #ffffff; border: 2px solid #2563EB; width: 64px; height: 64px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 24px auto; color: #2563EB; font-weight: 700; font-size: 20px;">2</div>
          <h4 style="font-size: 18px; font-weight: 600; color: #111827; margin-bottom: 8px;">Approval</h4>
        </div>

        <div class="workflow-step" style="position: relative; z-index: 1; flex: 1; padding: 0 16px;">
          <div style="background: #ffffff; border: 2px solid #2563EB; width: 64px; height: 64px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 24px auto; color: #2563EB; font-weight: 700; font-size: 20px;">3</div>
          <h4 style="font-size: 18px; font-weight: 600; color: #111827; margin-bottom: 8px;">Pickup / Shipping</h4>
        </div>

        <div class="workflow-step" style="position: relative; z-index: 1; flex: 1; padding: 0 16px;">
          <div style="background: #2563EB; border: 2px solid #2563EB; width: 64px; height: 64px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 24px auto; color: #ffffff; font-weight: 700; font-size: 20px; box-shadow: 0 12px 32px rgba(37,99,235,0.2);">4</div>
          <h4 style="font-size: 18px; font-weight: 600; color: #111827; margin-bottom: 8px;">Refund Processed</h4>
        </div>
      </div>

      <p style="font-size: 20px; color: #4B5563; line-height: 1.6; margin: 0 auto; max-width: 800px;">Our goal is to make returns transparent and stress-free. If a product doesn't meet your expectations, our automated system ensures you get your money back smoothly.</p>
    </div>
  </section>

  <!-- SECTION 5: FREQUENTLY ASKED QUESTIONS (Light Gray) -->
  <section style="background-color: #f8fafc; padding: 160px 5%; width: 100%; box-sizing: border-box; border-top: 1px solid rgba(0,0,0,0.03);">
    <div style="max-width: 800px; margin: 0 auto;">
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 64px; letter-spacing: -0.03em; text-align: center;">Frequently Asked Questions</h2>
      
      <div style="display: flex; flex-direction: column; gap: 16px;">
        
        <div class="faq-accordion" style="border: 1px solid rgba(0,0,0,0.08); border-radius: 16px; background: #ffffff; overflow: hidden; transition: all 0.3s ease;">
          <button class="faq-btn" style="width: 100%; text-align: left; background: none; border: none; padding: 24px 32px; font-size: 20px; font-weight: 600; color: #111827; cursor: pointer; display: flex; justify-content: space-between; align-items: center; font-family: inherit;">
            How do I track my order?
            <svg class="faq-icon" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="transition: transform 0.3s ease;"><path d="m6 9 6 6 6-6"/></svg>
          </button>
          <div class="faq-content" style="max-height: 0; overflow: hidden; transition: max-height 0.3s ease;">
            <p style="padding: 0 32px 24px 32px; margin: 0; font-size: 16px; color: #4B5563; line-height: 1.6;">You can track your order in real-time through the Nexmart app by navigating to your Order History and selecting the active order.</p>
          </div>
        </div>

        <div class="faq-accordion" style="border: 1px solid rgba(0,0,0,0.08); border-radius: 16px; background: #ffffff; overflow: hidden; transition: all 0.3s ease;">
          <button class="faq-btn" style="width: 100%; text-align: left; background: none; border: none; padding: 24px 32px; font-size: 20px; font-weight: 600; color: #111827; cursor: pointer; display: flex; justify-content: space-between; align-items: center; font-family: inherit;">
            Can I cancel an order after placing it?
            <svg class="faq-icon" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="transition: transform 0.3s ease;"><path d="m6 9 6 6 6-6"/></svg>
          </button>
          <div class="faq-content" style="max-height: 0; overflow: hidden; transition: max-height 0.3s ease;">
            <p style="padding: 0 32px 24px 32px; margin: 0; font-size: 16px; color: #4B5563; line-height: 1.6;">Yes, orders can be canceled before they enter the shipping process. The cancellation window depends on the specific supplier.</p>
          </div>
        </div>

        <div class="faq-accordion" style="border: 1px solid rgba(0,0,0,0.08); border-radius: 16px; background: #ffffff; overflow: hidden; transition: all 0.3s ease;">
          <button class="faq-btn" style="width: 100%; text-align: left; background: none; border: none; padding: 24px 32px; font-size: 20px; font-weight: 600; color: #111827; cursor: pointer; display: flex; justify-content: space-between; align-items: center; font-family: inherit;">
            How long do refunds take?
            <svg class="faq-icon" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="transition: transform 0.3s ease;"><path d="m6 9 6 6 6-6"/></svg>
          </button>
          <div class="faq-content" style="max-height: 0; overflow: hidden; transition: max-height 0.3s ease;">
            <p style="padding: 0 32px 24px 32px; margin: 0; font-size: 16px; color: #4B5563; line-height: 1.6;">Refunds are typically processed within 3-5 business days after the returned item is successfully received and inspected.</p>
          </div>
        </div>

        <div class="faq-accordion" style="border: 1px solid rgba(0,0,0,0.08); border-radius: 16px; background: #ffffff; overflow: hidden; transition: all 0.3s ease;">
          <button class="faq-btn" style="width: 100%; text-align: left; background: none; border: none; padding: 24px 32px; font-size: 20px; font-weight: 600; color: #111827; cursor: pointer; display: flex; justify-content: space-between; align-items: center; font-family: inherit;">
            Who pays return shipping?
            <svg class="faq-icon" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="transition: transform 0.3s ease;"><path d="m6 9 6 6 6-6"/></svg>
          </button>
          <div class="faq-content" style="max-height: 0; overflow: hidden; transition: max-height 0.3s ease;">
            <p style="padding: 0 32px 24px 32px; margin: 0; font-size: 16px; color: #4B5563; line-height: 1.6;">If the item is defective or incorrect, return shipping is covered by Nexmart. For standard returns due to change of mind, shipping policies depend on the original seller.</p>
          </div>
        </div>

        <div class="faq-accordion" style="border: 1px solid rgba(0,0,0,0.08); border-radius: 16px; background: #ffffff; overflow: hidden; transition: all 0.3s ease;">
          <button class="faq-btn" style="width: 100%; text-align: left; background: none; border: none; padding: 24px 32px; font-size: 20px; font-weight: 600; color: #111827; cursor: pointer; display: flex; justify-content: space-between; align-items: center; font-family: inherit;">
            What if my order arrives damaged?
            <svg class="faq-icon" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="transition: transform 0.3s ease;"><path d="m6 9 6 6 6-6"/></svg>
          </button>
          <div class="faq-content" style="max-height: 0; overflow: hidden; transition: max-height 0.3s ease;">
            <p style="padding: 0 32px 24px 32px; margin: 0; font-size: 16px; color: #4B5563; line-height: 1.6;">Report it instantly through the app. Our support agents will fast-track a replacement or refund.</p>
          </div>
        </div>

        <div class="faq-accordion" style="border: 1px solid rgba(0,0,0,0.08); border-radius: 16px; background: #ffffff; overflow: hidden; transition: all 0.3s ease;">
          <button class="faq-btn" style="width: 100%; text-align: left; background: none; border: none; padding: 24px 32px; font-size: 20px; font-weight: 600; color: #111827; cursor: pointer; display: flex; justify-content: space-between; align-items: center; font-family: inherit;">
            Where can I see my order history?
            <svg class="faq-icon" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="transition: transform 0.3s ease;"><path d="m6 9 6 6 6-6"/></svg>
          </button>
          <div class="faq-content" style="max-height: 0; overflow: hidden; transition: max-height 0.3s ease;">
            <p style="padding: 0 32px 24px 32px; margin: 0; font-size: 16px; color: #4B5563; line-height: 1.6;">Your complete history is available under the 'Orders' tab in your Nexmart account dashboard.</p>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- SECTION 6: BEST PRACTICES (White) -->
  <section style="background-color: #ffffff; padding: 160px 5%; width: 100%; box-sizing: border-box;">
    <div style="max-width: 1400px; margin: 0 auto;">
      <h2 style="font-size: 40px; font-weight: 600; color: #111827; margin-bottom: 64px; letter-spacing: -0.03em; text-align: center;">Best Practices</h2>
      
      <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 24px;">
        <div class="practice-card" style="background: #f8fafc; border: 1px solid rgba(0,0,0,0.04); border-radius: 20px; padding: 32px; display: flex; align-items: center; gap: 24px; transition: all 0.3s ease;">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 48px; height: 48px; border-radius: 12px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg></div>
          <h3 style="font-size: 18px; font-weight: 600; color: #111827; margin: 0;">Review Delivery Details</h3>
        </div>
        <div class="practice-card" style="background: #f8fafc; border: 1px solid rgba(0,0,0,0.04); border-radius: 20px; padding: 32px; display: flex; align-items: center; gap: 24px; transition: all 0.3s ease;">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 48px; height: 48px; border-radius: 12px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 0 1-3.46 0"/></svg></div>
          <h3 style="font-size: 18px; font-weight: 600; color: #111827; margin: 0;">Enable Notifications</h3>
        </div>
        <div class="practice-card" style="background: #f8fafc; border: 1px solid rgba(0,0,0,0.04); border-radius: 20px; padding: 32px; display: flex; align-items: center; gap: 24px; transition: all 0.3s ease;">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 48px; height: 48px; border-radius: 12px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16c0 1.1.9 2 2 2h12a2 2 0 0 0 2-2V8l-6-6z"/><path d="M14 3v5h5"/><path d="M16 13H8"/><path d="M16 17H8"/><path d="M10 9H8"/></svg></div>
          <h3 style="font-size: 18px; font-weight: 600; color: #111827; margin: 0;">Keep Your Invoice</h3>
        </div>
        <div class="practice-card" style="background: #f8fafc; border: 1px solid rgba(0,0,0,0.04); border-radius: 20px; padding: 32px; display: flex; align-items: center; gap: 24px; transition: all 0.3s ease;">
          <div style="background: rgba(37,99,235,0.05); color: #2563EB; width: 48px; height: 48px; border-radius: 12px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg></div>
          <h3 style="font-size: 18px; font-weight: 600; color: #111827; margin: 0;">Inspect Items Upon Arrival</h3>
        </div>
      </div>
    </div>
  </section>

  <!-- FINAL CTA (Light Gray) -->
  <section style="background-color: #f8fafc; padding: 180px 5% 240px 5%; width: 100%; box-sizing: border-box; border-top: 1px solid rgba(0,0,0,0.03);">
    <div style="max-width: 1000px; margin: 0 auto; text-align: center;">
      <h2 style="font-size: 48px; font-weight: 600; color: #111827; margin-bottom: 24px; letter-spacing: -0.03em;">Shop With Confidence</h2>
      <p style="font-size: 22px; color: #4B5563; line-height: 1.7; margin: 0 auto 48px auto; max-width: 800px;">Nexmart keeps every purchase transparent from checkout to delivery, giving you complete visibility and confidence throughout the entire shopping journey.</p>
      
      <div style="display: flex; gap: 16px; justify-content: center; flex-wrap: wrap;">
        <a href="#" class="btn-primary" style="text-decoration: none; background: #2563EB; color: #ffffff; padding: 18px 40px; border-radius: 100px; font-size: 18px; font-weight: 600; transition: all 0.3s ease; display: inline-flex; align-items: center; gap: 12px;">
            Start Shopping With AI
        </a>
        <a href="power-user-guide.html" class="btn-secondary" style="text-decoration: none; background: #ffffff; border: 1px solid rgba(0,0,0,0.1); color: #111827; padding: 18px 40px; border-radius: 100px; font-size: 18px; font-weight: 600; transition: all 0.3s ease; box-shadow: 0 4px 12px rgba(0,0,0,0.02);">
            Continue Learning
        </a>
      </div>
    </div>
  </section>

  <style>
    .feature-card:hover, .manage-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 24px 48px rgba(37,99,235,0.08) !important;
        border-color: rgba(37,99,235,0.2) !important;
    }
    .practice-card:hover {
        transform: translateY(-4px);
        background: #ffffff !important;
        box-shadow: 0 12px 24px rgba(0,0,0,0.04) !important;
        border-color: rgba(37,99,235,0.2) !important;
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
        .semantic-orders-wrapper section {
            padding: 100px 5% !important;
        }
        .semantic-orders-wrapper h1 {
            font-size: 48px !important;
        }
        .semantic-orders-wrapper h2 {
            font-size: 32px !important;
        }
        .journey-workflow, .return-workflow {
            flex-direction: column !important;
            gap: 40px !important;
        }
        .workflow-line {
            display: none !important;
        }
        .practice-card {
            grid-column: span 2 !important;
        }
    }
    @media (max-width: 600px) {
        .semantic-orders-wrapper section {
            padding: 80px 5% !important;
        }
        .semantic-orders-wrapper h1 {
            font-size: 40px !important;
        }
        .semantic-orders-wrapper .btn-primary, .semantic-orders-wrapper .btn-secondary {
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
                
                if (parent.classList.contains('is-open')) {
                    parent.classList.remove('is-open');
                    content.style.maxHeight = null;
                } else {
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
    wrapper = placeholder.find_parent('div', class_='semantic-placeholder-wrapper')
    if wrapper:
        new_section = bs4.BeautifulSoup(orders_html, 'html.parser')
        wrapper.replace_with(new_section)
    else:
        section_to_replace = placeholder.find_parent('section')
        if section_to_replace:
            new_section = bs4.BeautifulSoup(orders_html, 'html.parser')
            section_to_replace.replace_with(new_section)

with open('orders-and-returns.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Successfully built the Orders & Returns page.")
