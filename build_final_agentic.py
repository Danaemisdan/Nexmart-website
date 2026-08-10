import bs4
import copy

def run():
    with open('index.html', 'r', encoding='utf-8') as f:
        soup = bs4.BeautifulSoup(f, 'html.parser')
    
    # ----------------------------------------------------
    # 1. Inject Product-Specific CSS & Orchestration Thread 
    # ----------------------------------------------------
    # We add a style block for the product UI specific patterns to keep them reusable.
    prod_style = soup.new_tag('style')
    prod_style.string = """
    /* Product UI Framework (Reusable for all product pages) */
    .product-console {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.03);
        padding: 40px;
        position: relative;
        overflow: hidden;
    }
    .product-ui-card {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 8px;
        padding: 24px;
        transition: border-color 0.2s ease;
    }
    .product-ui-card:hover {
        border-color: #1a365d;
    }
    .product-metric-lg {
        font-size: 3rem;
        font-weight: 700;
        color: #111827;
        line-height: 1.1;
    }
    .product-metric-highlight {
        color: #1a365d;
    }
    .product-label {
        font-size: 0.875rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #6b7280;
        font-weight: 600;
    }
    /* The Signature Component: Neural Ledger */
    .neural-ledger {
        position: fixed;
        bottom: 24px;
        left: 24px;
        z-index: 50;
        font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
        font-size: 11px;
        color: #6b7280;
        opacity: 0.4;
        pointer-events: none;
    }
    .neural-ledger span { color: #1a365d; font-weight: 600; }
    
    /* The Signature Component: Orchestration Thread */
    .orchestration-thread-wrapper {
        position: absolute;
        top: 0;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 2px;
        background: #e5e7eb;
        z-index: -1;
    }
    .orchestration-thread-active {
        position: absolute;
        top: 0;
        width: 100%;
        height: 60%; /* Represents progress */
        background: #1a365d;
    }
    
    @media (max-width: 767px) {
        .orchestration-thread-wrapper { left: 24px; transform: none; }
        .product-console { padding: 24px; }
    }
    
    /* Utility for stripping homepage marketing styles from grids */
    .ui-clean-grid { gap: 24px; }
    """
    soup.head.append(prod_style)
    
    main = soup.find('main')
    
    # Wrap sections in a relative wrapper for the continuous thread
    # We will create a wrapper div and move all sections (except footer) into it
    thread_wrapper = soup.new_tag('div')
    thread_wrapper['style'] = "position: relative; overflow: hidden; padding-top: 60px; padding-bottom: 60px;"
    
    thread_line = soup.new_tag('div', **{'class': 'orchestration-thread-wrapper'})
    active_line = soup.new_tag('div', **{'class': 'orchestration-thread-active'})
    thread_line.append(active_line)
    thread_wrapper.append(thread_line)
    
    main.clear()
    main.append(thread_wrapper)
    
    # Add Neural Ledger to body
    ledger = soup.new_tag('div', **{'class': 'neural-ledger'})
    ledger.append(bs4.BeautifulSoup('<div><span>[14:02:01.04]</span> System_Agent: Executing mission parameters...</div>', 'html.parser'))
    ledger.append(bs4.BeautifulSoup('<div><span>[14:02:02.12]</span> Auth_Agent: Handshake confirmed [OK].</div>', 'html.parser'))
    ledger.append(bs4.BeautifulSoup('<div><span>[14:02:05.88]</span> Discovery_Agent: Scanning global inventory...</div>', 'html.parser'))
    soup.body.append(ledger)
    
    # ----------------------------------------------------
    # 2. Mission Console (Hero)
    # ----------------------------------------------------
    sec_hero = soup.new_tag('section')
    thread_wrapper.append(sec_hero)
    
    hero_container = soup.new_tag('div', **{'class': 'container-large'})
    hero_container['style'] = "position: relative; z-index: 2; text-align: center; margin-bottom: 80px;"
    
    hero_title = soup.new_tag('h1', **{'class': 'margin-bottom'})
    hero_title.string = "Command your commerce."
    hero_title['style'] = "font-size: 4rem; font-weight: 800; color: #111827; letter-spacing: -0.02em; background: white; display: inline-block; padding: 0 24px; position: relative;"
    
    hero_sub = soup.new_tag('p', **{'class': 'text-size-large margin-bottom'})
    hero_sub.string = "The intelligent engine that executes your complex procurement tasks."
    hero_sub['style'] = "color: #6b7280; max-width: 600px; margin-left: auto; margin-right: auto; background: white; display: inline-block; padding: 12px 24px; position: relative;"
    
    console_div = soup.new_tag('div', **{'class': 'product-console'})
    console_div['style'] = "text-align: left; max-width: 800px; margin: 40px auto 0;"
    
    console_html = """
    <div style="border-bottom: 1px solid #e5e7eb; padding-bottom: 24px; margin-bottom: 24px;">
        <div class="product-label" style="margin-bottom: 8px;">Active Mission</div>
        <div style="font-size: 1.5rem; font-weight: 600; color: #111827;">"Procure 500 ergonomic office chairs under budget, delivered by Friday."</div>
    </div>
    <div class="w-layout-grid grid" style="grid-template-columns: 1fr 1fr; gap: 40px;">
        <div>
            <div class="product-label" style="margin-bottom: 16px;">Agent Status</div>
            <div style="display: flex; flex-direction: column; gap: 12px; font-family: monospace; font-size: 14px;">
                <div style="display: flex; align-items: center; gap: 8px;"><div style="width:8px;height:8px;border-radius:50%;background:#10b981;"></div> Discovery Agent [ACTIVE]</div>
                <div style="display: flex; align-items: center; gap: 8px;"><div style="width:8px;height:8px;border-radius:50%;background:#10b981;"></div> Pricing Agent [ACTIVE]</div>
                <div style="display: flex; align-items: center; gap: 8px;"><div style="width:8px;height:8px;border-radius:50%;background:#f59e0b;"></div> Negotiation Agent [RUNNING]</div>
                <div style="display: flex; align-items: center; gap: 8px;"><div style="width:8px;height:8px;border-radius:50%;border:1px solid #d1d5db;"></div> Checkout Agent [WAITING]</div>
            </div>
        </div>
        <div>
            <div class="product-label" style="margin-bottom: 16px;">Live Execution</div>
            <div style="display: flex; flex-direction: column; gap: 12px; font-size: 14px; color: #6b7280;">
                <div>> Supplier comparison completed (1.2s)</div>
                <div>> Identified top 3 wholesale partners</div>
                <div style="color:#1a365d; font-weight:600;">> Negotiating 14% volume discount...</div>
            </div>
        </div>
    </div>
    <div style="margin-top: 32px; text-align: right;">
        <a href="https://app.nexmartshop.ai" class="button-main w-button" style="background-color: #1a365d; color: #fff; padding: 12px 24px; border-radius: 8px;">Abort Mission</a>
    </div>
    """
    console_div.append(bs4.BeautifulSoup(console_html, 'html.parser'))
    
    hero_container.append(hero_title)
    hero_container.append(hero_sub)
    hero_container.append(console_div)
    sec_hero.append(hero_container)

    # ----------------------------------------------------
    # 3. Checkpoint 1 (Discovery)
    # ----------------------------------------------------
    sec_chk1 = soup.new_tag('section')
    thread_wrapper.append(sec_chk1)
    sec_chk1['style'] = "padding: 80px 0; position: relative; z-index: 2;"
    chk1_cont = soup.new_tag('div', **{'class': 'container-large'})
    
    chk1_html = """
    <div class="w-layout-grid grid" style="grid-template-columns: 1fr 1fr; gap: 60px; align-items: center;">
        <div style="background:#fff; padding:32px; border-radius:12px; border:1px solid #e5e7eb; box-shadow:0 10px 30px rgba(0,0,0,0.02);">
            <div class="product-label" style="margin-bottom:20px;">Data Table: Supplier Index</div>
            <table style="width: 100%; text-align: left; font-size: 14px; border-collapse: collapse;">
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <th style="padding: 12px 0; color:#6b7280; font-weight:500;">Supplier</th>
                    <th style="padding: 12px 0; color:#6b7280; font-weight:500;">Lead Time</th>
                    <th style="padding: 12px 0; color:#6b7280; font-weight:500;">Rating</th>
                </tr>
                <tr style="border-bottom: 1px solid #f3f4f6;">
                    <td style="padding: 12px 0; font-weight:600;">Herman Miller Direct</td>
                    <td style="padding: 12px 0;">3 days</td>
                    <td style="padding: 12px 0; color:#10b981;">99%</td>
                </tr>
                <tr style="border-bottom: 1px solid #f3f4f6;">
                    <td style="padding: 12px 0; font-weight:600;">OfficeDepot B2B</td>
                    <td style="padding: 12px 0;">5 days</td>
                    <td style="padding: 12px 0; color:#f59e0b;">94%</td>
                </tr>
                <tr>
                    <td style="padding: 12px 0; font-weight:600;">Steelcase Logistics</td>
                    <td style="padding: 12px 0;">2 days</td>
                    <td style="padding: 12px 0; color:#10b981;">98%</td>
                </tr>
            </table>
        </div>
        <div>
            <h2 style="font-size: 2.5rem; font-weight: 700; color: #111827; margin-bottom: 16px;">Instant Global Discovery</h2>
            <p style="font-size: 1.125rem; color: #6b7280; margin-bottom: 24px;">The Discovery Agent scans millions of global SKUs in milliseconds, indexing certified suppliers based on your exact logistical constraints.</p>
        </div>
    </div>
    """
    chk1_cont.append(bs4.BeautifulSoup(chk1_html, 'html.parser'))
    sec_chk1.append(chk1_cont)

    # ----------------------------------------------------
    # 4. Checkpoint 2 (Negotiation High Fidelity UI)
    # ----------------------------------------------------
    sec_chk2 = soup.new_tag('section')
    thread_wrapper.append(sec_chk2)
    sec_chk2['style'] = "padding: 80px 0; position: relative; z-index: 2;"
    chk2_cont = soup.new_tag('div', **{'class': 'container-large'})
    
    chk2_html = """
    <div class="w-layout-grid grid" style="grid-template-columns: 1fr 1fr; gap: 60px; align-items: center;">
        <div>
            <h2 style="font-size: 2.5rem; font-weight: 700; color: #111827; margin-bottom: 16px;">Automated Negotiation</h2>
            <p style="font-size: 1.125rem; color: #6b7280; margin-bottom: 24px;">Our Negotiation Agents engage directly with B2B suppliers, applying volume-based leverage and historic price data to secure exclusive margins without human intervention.</p>
        </div>
        <div class="product-ui-card" style="padding: 32px; box-shadow:0 10px 30px rgba(0,0,0,0.02);">
            <div class="product-label" style="margin-bottom:20px;">Optimization Checkpoint</div>
            <div style="background:#f9fafb; padding:16px; border-radius:8px; border:1px solid #e5e7eb; margin-bottom: 16px;">
                <div style="font-size:12px; color:#6b7280; margin-bottom:4px;">Initial Quote (500 Units)</div>
                <div style="font-size:20px; font-weight:700; color:#111827; text-decoration: line-through;">$125,000.00</div>
            </div>
            <div style="text-align:center; color:#6b7280; margin-bottom:16px;">↓ Agent Intervention ↓</div>
            <div style="background:#eff6ff; padding:16px; border-radius:8px; border:1px solid #bfdbfe; margin-bottom: 16px;">
                <div style="font-size:12px; color:#1e3a8a; margin-bottom:4px;">Negotiated Quote (500 Units)</div>
                <div style="font-size:24px; font-weight:700; color:#1e40af;">$107,500.00</div>
            </div>
            <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px dashed #e5e7eb; padding-top:16px;">
                <span style="font-size:14px; color:#6b7280;">Total Savings</span>
                <span style="font-size:16px; font-weight:700; color:#10b981;">+ $17,500 (14%)</span>
            </div>
        </div>
    </div>
    """
    chk2_cont.append(bs4.BeautifulSoup(chk2_html, 'html.parser'))
    sec_chk2.append(chk2_cont)

    # ----------------------------------------------------
    # 5. Business Outcomes
    # ----------------------------------------------------
    sec_out = soup.new_tag('section')
    thread_wrapper.append(sec_out)
    sec_out['style'] = "padding: 80px 0; position: relative; z-index: 2;"
    out_cont = soup.new_tag('div', **{'class': 'container-large'})
    
    out_html = """
    <div style="text-align: center; margin-bottom: 60px; max-width: 600px; margin-left: auto; margin-right: auto;">
        <h2 style="font-size: 2.5rem; font-weight: 700; color: #111827; margin-bottom: 16px;">Transform your operations.</h2>
        <p style="font-size: 1.125rem; color: #6b7280;">Agentic Commerce drastically reduces manual procurement hours while driving undeniable bottom-line value.</p>
    </div>
    <div class="w-layout-grid grid ui-clean-grid" style="grid-template-columns: 1fr 1fr; gap: 24px;">
        <div class="product-ui-card" style="display:flex; flex-direction:column; justify-content:center; align-items:center; padding: 40px; text-align:center;">
            <div class="product-metric-lg" style="margin-bottom: 12px;">98<span class="product-metric-highlight">%</span></div>
            <div class="product-label">Reduction in Sourcing Time</div>
        </div>
        <div class="product-ui-card" style="display:flex; flex-direction:column; justify-content:center; align-items:center; padding: 40px; text-align:center;">
            <div class="product-metric-lg" style="margin-bottom: 12px;">12-18<span class="product-metric-highlight">%</span></div>
            <div class="product-label">Average Margin Improvement</div>
        </div>
    </div>
    """
    out_cont.append(bs4.BeautifulSoup(out_html, 'html.parser'))
    sec_out.append(out_cont)
    
    # ----------------------------------------------------
    # 6. Clean up remaining sections to preserve structure without fluff
    # ----------------------------------------------------

    
    sec_5 = soup.new_tag('section')
    thread_wrapper.append(sec_5)
    sec_5['style'] = "padding: 120px 0; position: relative; z-index: 2; text-align:center;"
    cta_cont = soup.new_tag('div', **{'class': 'container-large'})
    cta_html = """
    <div style="background: #111827; border-radius: 16px; padding: 60px; text-align: center;">
        <h2 style="font-size: 2.5rem; font-weight: 700; color: #ffffff; margin-bottom: 16px;">Ready to deploy your agents?</h2>
        <p style="font-size: 1.125rem; color: #9ca3af; margin-bottom: 32px; max-width: 500px; margin-left:auto; margin-right:auto;">Experience the future of intelligent autonomous procurement.</p>
        <a href="https://app.nexmartshop.ai/sign-up" class="button-main w-button" style="background-color: #1a365d; color: #fff; padding: 16px 32px; border-radius: 8px;">Launch Mission Console</a>
    </div>
    """
    cta_cont.append(bs4.BeautifulSoup(cta_html, 'html.parser'))
    sec_5.append(cta_cont)
    
    # Save the file
    with open('agentic-commerce.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    print("Rebuild of agentic-commerce.html using product-centric architecture is complete.")

if __name__ == '__main__':
    run()
