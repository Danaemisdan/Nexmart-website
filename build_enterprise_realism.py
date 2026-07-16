import bs4

def run():
    with open('agentic-commerce.html', 'r', encoding='utf-8') as f:
        soup = bs4.BeautifulSoup(f, 'html.parser')
    
    # ----------------------------------------------------
    # Update CSS for Solid Enterprise Realism & Boot Sequence
    # ----------------------------------------------------
    style_str = """
    :root {
        --saas-bg: #0f172a;
        --saas-panel: #1e293b;
        --saas-border: #334155;
        --saas-text-main: #f8fafc;
        --saas-text-muted: #94a3b8;
        --saas-accent: #2563eb; /* Royal Blue */
        --saas-success: #10b981;
        --saas-warning: #f59e0b;
        --saas-danger: #ef4444;
    }

    body { background: #f8fafc; }

    /* Solid Enterprise Application Frame */
    .app-window {
        background: var(--saas-bg);
        border: 1px solid var(--saas-border);
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        overflow: hidden;
        display: flex;
        flex-direction: column;
        position: relative;
    }
    
    .app-window-light {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
        overflow: hidden;
    }

    .app-header {
        height: 44px;
        background: var(--saas-bg);
        border-bottom: 1px solid var(--saas-border);
        display: flex;
        align-items: center;
        padding: 0 16px;
        gap: 8px;
    }
    .app-dot { width: 10px; height: 10px; border-radius: 50%; }
    .app-dot.r { background: #ef4444; } .app-dot.y { background: #f59e0b; } .app-dot.g { background: #10b981; }
    
    /* Hero Specifically */
    .hero-app { height: 75vh; min-height: 700px; margin-top: 40px; }
    .hero-layout { display: flex; flex: 1; overflow: hidden; }
    .hero-sidebar { width: 240px; background: #0b1120; border-right: 1px solid var(--saas-border); padding: 20px; display: flex; flex-direction: column; gap: 24px; overflow-y: auto; }
    .hero-main { flex: 1; padding: 32px; overflow-y: auto; display: flex; flex-direction: column; gap: 24px; background: var(--saas-bg); }
    
    .nav-group-title { font-size: 11px; text-transform: uppercase; letter-spacing: 0.05em; color: var(--saas-text-muted); margin-bottom: 8px; font-weight: 600; }
    .nav-item { display: flex; align-items: center; gap: 12px; padding: 6px 12px; color: var(--saas-text-muted); font-size: 13px; border-radius: 6px; font-weight: 500; cursor: pointer; transition: background 0.15s, color 0.15s; }
    .nav-item:hover { background: rgba(255,255,255,0.05); color: var(--saas-text-main); }
    .nav-item.active { background: rgba(37, 99, 235, 0.15); color: var(--saas-accent); }
    
    /* Boot Sequence Animations */
    @keyframes boot-fade { 0% { opacity: 0; transform: translateY(10px); } 100% { opacity: 1; transform: translateY(0); } }
    @keyframes boot-type { 0% { width: 0; } 100% { width: 100%; } }
    @keyframes load-bar { 0% { width: 0%; } 20% { width: 10%; } 50% { width: 40%; } 80% { width: 90%; } 100% { width: 100%; } }
    
    .boot-1 { opacity: 0; animation: boot-fade 0.4s ease forwards 0.2s; }
    .boot-2 { opacity: 0; animation: boot-fade 0.4s ease forwards 0.6s; }
    .boot-3 { opacity: 0; animation: boot-fade 0.4s ease forwards 1.0s; }
    
    .typing-text { display: inline-block; overflow: hidden; white-space: nowrap; animation: boot-type 1.5s steps(40, end) forwards 0.4s; width: 0; }
    .cursor-blink { display: inline-block; width: 2px; background: var(--saas-accent); margin-left: 2px; animation: blink 1s step-end infinite; }
    
    /* Mission Details */
    .mission-panel { background: var(--saas-panel); border: 1px solid var(--saas-border); border-radius: 8px; padding: 20px; }
    .mission-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-top: 20px; padding-top: 20px; border-top: 1px solid var(--saas-border); }
    .m-label { font-size: 11px; text-transform: uppercase; color: var(--saas-text-muted); margin-bottom: 4px; font-weight: 600; }
    .m-val { font-size: 13px; color: var(--saas-text-main); font-family: monospace; }
    
    /* Agent Status Grid */
    .agent-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; }
    .agent-card { background: var(--saas-bg); border: 1px solid var(--saas-border); border-radius: 6px; padding: 12px; }
    .ac-head { display: flex; justify-content: space-between; margin-bottom: 8px; align-items: center; }
    .ac-name { font-size: 13px; color: var(--saas-text-main); font-weight: 600; }
    .ac-stat { font-size: 10px; font-family: monospace; padding: 2px 6px; border-radius: 4px; font-weight: 600; }
    .ac-stat.run { background: rgba(16, 185, 129, 0.1); color: var(--saas-success); border: 1px solid rgba(16, 185, 129, 0.2); }
    .ac-stat.wait { background: rgba(148, 163, 184, 0.1); color: var(--saas-text-muted); border: 1px solid rgba(148, 163, 184, 0.2); }
    .ac-log { font-family: monospace; font-size: 11px; color: var(--saas-text-muted); white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }
    
    .prog-bg { width: 100%; height: 2px; background: rgba(255,255,255,0.05); margin-top: 8px; }
    .prog-fill { height: 100%; background: var(--saas-accent); animation: load-bar 4s cubic-bezier(0.4, 0, 0.2, 1) forwards 1.2s; width:0; }
    
    /* Connected Flow Layout */
    /* Instead of isolated blocks, the application windows overlap to feel like expanding nodes */
    .flow-connector {
        width: 2px;
        height: 60px;
        background: #cbd5e1;
        margin: 0 auto;
    }
    .flow-module {
        max-width: 1000px;
        margin: 0 auto;
        position: relative;
        z-index: 10;
    }
    
    /* Table / Data UI */
    .ui-table { width: 100%; border-collapse: collapse; font-size: 13px; text-align: left; }
    .ui-table th { padding: 12px 16px; border-bottom: 1px solid #e2e8f0; color: #64748b; font-weight: 600; text-transform: uppercase; font-size: 11px; background: #f8fafc; }
    .ui-table td { padding: 16px; border-bottom: 1px solid #e2e8f0; color: #0f172a; }
    .ui-table tr { transition: background 0.1s; }
    .ui-table tr.interactive:hover { background: #f1f5f9; cursor: pointer; }
    
    /* Action Button */
    .btn-solid { background: var(--saas-accent); color: #fff; border: none; padding: 8px 16px; border-radius: 6px; font-weight: 500; font-size: 13px; cursor: pointer; transition: background 0.15s; }
    .btn-solid:hover { background: #1d4ed8; }
    
    @keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }
    @media (max-width: 991px) { .hero-sidebar { display: none; } }
    @media (max-width: 767px) { .agent-grid { grid-template-columns: 1fr; } .mission-grid { grid-template-columns: 1fr 1fr; gap:12px; } }
    """

    for s in soup.head.find_all('style'):
        if s.string and ('Hero Specific UI Variables' in s.string or 'Product UI Framework' in s.string or '--saas-bg' in s.string):
            s.decompose()
            
    style = soup.new_tag('style')
    style.string = style_str
    soup.head.append(style)

    main = soup.find('main')
    footer = main.find(class_='footer_component')
    main.clear()

    # ----------------------------------------------------
    # SECTION 1: HERO (Application Boot Sequence)
    # ----------------------------------------------------
    sec_hero = soup.new_tag('section', **{'style': 'padding: 80px 24px 0 24px; position: relative;'})
    hero_html = """
    <div style="text-align:center; max-width:800px; margin:0 auto 32px auto;">
        <h1 style="font-size:3.5rem; font-weight:800; color:#0f172a; letter-spacing:-0.03em; margin-bottom:16px;">Execute autonomous procurement.</h1>
        <p style="font-size:1.125rem; color:#475569;">Don't search. Instruct. Deploy specialized AI agents to handle discovery, compliance, negotiation, and logistics in parallel.</p>
    </div>
    
    <div class="flow-module">
        <div class="app-window hero-app">
            <div class="app-header">
                <div style="display:flex; gap:6px;"><div class="app-dot r"></div><div class="app-dot y"></div><div class="app-dot g"></div></div>
                <div style="margin-left:auto; font-family:monospace; font-size:10px; color:var(--saas-text-muted);">WORKSPACE: ACME RETAIL NIGERIA</div>
            </div>
            <div class="hero-layout">
                <div class="hero-sidebar">
                    <div>
                        <div class="nav-group-title">Command Center</div>
                        <div class="nav-item active">Active Missions</div>
                        <div class="nav-item">Supplier Network</div>
                        <div class="nav-item">Live Negotiations</div>
                    </div>
                    <div>
                        <div class="nav-group-title">Operations</div>
                        <div class="nav-item">Purchase Orders</div>
                        <div class="nav-item">Logistics & Freight</div>
                        <div class="nav-item">Warehouses</div>
                    </div>
                    <div>
                        <div class="nav-group-title">Governance</div>
                        <div class="nav-item">Compliance Hub</div>
                        <div class="nav-item">Contracts</div>
                    </div>
                </div>
                
                <div class="hero-main">
                    <!-- Boot 1: Mission Load -->
                    <div class="mission-panel boot-1">
                        <div style="display:flex; justify-content:space-between; margin-bottom:12px;">
                            <div style="font-family:monospace; font-size:11px; color:var(--saas-accent);">MISSION ID: NX-9482-B</div>
                            <div style="font-family:monospace; font-size:10px; color:var(--saas-success); border:1px solid rgba(16,185,129,0.3); padding:2px 6px; border-radius:4px;">EXECUTING</div>
                        </div>
                        <div style="font-size:18px; color:var(--saas-text-main); line-height:1.4;">
                            <span class="typing-text">Procure 500 ergonomic office chairs from SOC2-compliant suppliers.</span><span class="cursor-blink">&nbsp;</span>
                        </div>
                        <div class="mission-grid">
                            <div><div class="m-label">Budget</div><div class="m-val">$600,000 USD</div></div>
                            <div><div class="m-label">Destination</div><div class="m-val">Lagos (LOS)</div></div>
                            <div><div class="m-label">Deadline</div><div class="m-val">Friday, 14:00 GMT</div></div>
                            <div><div class="m-label">Compliance</div><div class="m-val">SOC2, ISO 9001</div></div>
                        </div>
                    </div>
                    
                    <!-- Boot 2: Agents -->
                    <div class="boot-2">
                        <div style="font-family:monospace; font-size:11px; color:var(--saas-text-muted); margin-bottom:12px;">ACTIVE AGENT THREADS</div>
                        <div class="agent-grid">
                            <div class="agent-card">
                                <div class="ac-head"><div class="ac-name">Discovery</div><div class="ac-stat run">RUNNING</div></div>
                                <div class="ac-log">> Scraping 4,821 global SKUs</div>
                                <div class="prog-bg"><div class="prog-fill"></div></div>
                            </div>
                            <div class="agent-card">
                                <div class="ac-head"><div class="ac-name">Compliance</div><div class="ac-stat run">RUNNING</div></div>
                                <div class="ac-log">> Verifying SOC2 certificates</div>
                                <div class="prog-bg"><div class="prog-fill" style="animation-duration:2.5s;"></div></div>
                            </div>
                            <div class="agent-card">
                                <div class="ac-head"><div class="ac-name">Negotiation</div><div class="ac-stat wait">WAITING</div></div>
                                <div class="ac-log">> Awaiting shortlist</div>
                                <div class="prog-bg"></div>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Boot 3: Live Feed -->
                    <div class="boot-3" style="flex:1; display:flex; flex-direction:column;">
                        <div style="font-family:monospace; font-size:11px; color:var(--saas-text-muted); margin-bottom:12px;">SYSTEM EXECUTION LOG</div>
                        <div style="background:var(--saas-bg); border:1px solid var(--saas-border); border-radius:8px; padding:12px; flex:1; font-family:monospace; font-size:11px; color:var(--saas-text-muted); display:flex; flex-direction:column; gap:6px;">
                            <div><span style="color:var(--saas-success);">[SUCCESS]</span> Authentication verified via SAML.</div>
                            <div><span style="color:#fff;">[SYSTEM]</span> Mission NX-9482-B allocated 14 parallel threads.</div>
                            <div><span style="color:var(--saas-accent);">[DISCOVERY]</span> Filtering out non-SOC2 suppliers (Retained 84).</div>
                            <div><span style="color:var(--saas-accent);">[DISCOVERY]</span> Calculating estimated freight to LOS...</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """
    sec_hero.append(bs4.BeautifulSoup(hero_html, 'html.parser'))
    main.append(sec_hero)

    # ----------------------------------------------------
    # Flow Connectors instead of generic padding
    # ----------------------------------------------------
    main.append(bs4.BeautifulSoup('<div class="flow-connector"></div>', 'html.parser'))

    # ----------------------------------------------------
    # SECTION 2: Walkthrough 1 (Supplier Matrix)
    # ----------------------------------------------------
    sec_supp = soup.new_tag('section', **{'style': 'padding: 0 24px;'})
    supp_html = """
    <div class="flow-module app-window-light">
        <div style="padding:24px 32px; border-bottom:1px solid #e2e8f0; display:flex; justify-content:space-between; align-items:center; background:#f8fafc;">
            <div>
                <h3 style="font-size:16px; font-weight:700; color:#0f172a; margin:0;">Supplier Intelligence Matrix</h3>
                <p style="font-size:12px; color:#64748b; margin:4px 0 0 0;">Mission NX-9482-B | 500 Office Chairs | SOC2 Required</p>
            </div>
            <button class="btn-solid">Export Audit Trail</button>
        </div>
        <table class="ui-table">
            <tr>
                <th>Supplier Profile</th>
                <th>Risk Score</th>
                <th>Compliance Status</th>
                <th>CO2 Impact</th>
                <th>Base Quote</th>
            </tr>
            <tr class="interactive" style="background:rgba(16,185,129,0.03);">
                <td>
                    <div style="font-weight:600; font-size:13px;">Herman Miller B2B</div>
                    <div style="font-size:11px; color:#64748b;">Direct Manufacturer</div>
                </td>
                <td><span style="color:#10b981; font-weight:700; font-family:monospace;">12/100</span></td>
                <td><span style="border:1px solid #cbd5e1; font-size:10px; padding:2px 4px; border-radius:4px; color:#475569;">SOC2</span> <span style="border:1px solid #cbd5e1; font-size:10px; padding:2px 4px; border-radius:4px; color:#475569;">ISO9001</span></td>
                <td style="font-size:12px; font-weight:500;">14.2 kg/unit</td>
                <td style="font-family:monospace; font-weight:600;">$1,200.00</td>
            </tr>
            <tr class="interactive">
                <td>
                    <div style="font-weight:600; font-size:13px;">Steelcase Global Logistics</div>
                    <div style="font-size:11px; color:#64748b;">Wholesale Distributor</div>
                </td>
                <td><span style="color:#f59e0b; font-weight:700; font-family:monospace;">42/100</span></td>
                <td><span style="border:1px solid #cbd5e1; font-size:10px; padding:2px 4px; border-radius:4px; color:#475569;">SOC2</span></td>
                <td style="font-size:12px; font-weight:500;">22.4 kg/unit</td>
                <td style="font-family:monospace; font-weight:500; color:#475569;">$1,250.00</td>
            </tr>
        </table>
    </div>
    """
    sec_supp.append(bs4.BeautifulSoup(supp_html, 'html.parser'))
    main.append(sec_supp)
    
    main.append(bs4.BeautifulSoup('<div class="flow-connector"></div>', 'html.parser'))

    # ----------------------------------------------------
    # SECTION 3: Walkthrough 2 (Negotiation Chat)
    # ----------------------------------------------------
    sec_neg = soup.new_tag('section', **{'style': 'padding: 0 24px;'})
    neg_html = """
    <div class="flow-module app-window" style="background:var(--saas-panel);">
        <div class="app-header" style="justify-content:space-between; background:var(--saas-bg);">
            <div style="font-size:12px; font-weight:600; color:#fff; display:flex; align-items:center; gap:8px;">
                <div style="width:6px; height:6px; border-radius:50%; background:var(--saas-success);"></div> Live Negotiation Thread: Herman Miller
            </div>
            <div style="font-size:10px; font-family:monospace; color:var(--saas-accent);">SECURE B2B CHANNEL</div>
        </div>
        <div style="padding:32px; display:flex; flex-direction:column; gap:20px;">
            <!-- Internal Logic -->
            <div style="padding:12px; background:rgba(0,0,0,0.2); border-left:2px solid var(--saas-accent); font-family:monospace; font-size:11px; color:var(--saas-text-muted); border-radius:0 6px 6px 0;">
                <div style="color:var(--saas-accent); margin-bottom:4px;">[INTERNAL AGENT LOGIC]</div>
                <div>> Historic data: Acme Retail ordered 2,400 total units globally YTD.</div>
                <div>> Volume leverage threshold met (Tier 3).</div>
                <div>> Generating counter-offer at $1,050/unit to anchor negotiation.</div>
            </div>
            <!-- Agent Msg -->
            <div style="display:flex; gap:12px; flex-direction:row-reverse;">
                <div style="width:28px; height:28px; border-radius:6px; background:var(--saas-accent); display:flex; align-items:center; justify-content:center; flex-shrink:0;">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
                </div>
                <div style="background:var(--saas-bg); padding:12px 16px; border-radius:8px; border:1px solid var(--saas-border); color:var(--saas-text-main); font-size:13px; max-width:70%;">
                    Based on our client's consolidated YTD volume of 2,400 units, we formally propose a counter-offer of <strong>$1,050/unit</strong> for this 500-unit lot.
                </div>
            </div>
        </div>
    </div>
    """
    sec_neg.append(bs4.BeautifulSoup(neg_html, 'html.parser'))
    main.append(sec_neg)
    
    main.append(bs4.BeautifulSoup('<div class="flow-connector"></div>', 'html.parser'))

    # ----------------------------------------------------
    # SECTION 4: Walkthrough 3 (Financial Optimization)
    # ----------------------------------------------------
    sec_opt = soup.new_tag('section', **{'style': 'padding: 0 24px;'})
    opt_html = """
    <div class="flow-module app-window-light" style="padding:40px;">
        <div style="text-align:center; margin-bottom:32px;">
            <div style="font-size:11px; font-weight:700; color:#64748b; text-transform:uppercase; letter-spacing:0.1em; margin-bottom:8px;">Mission Financial Execution</div>
            <div style="font-size:3.5rem; font-weight:800; color:#10b981; line-height:1; font-family:monospace;">+$75,000</div>
            <div style="font-size:14px; color:#0f172a; font-weight:600; margin-top:8px;">Capital Preserved via Agentic Negotiation</div>
        </div>
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px;">
            <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:20px;">
                <div style="font-size:11px; color:#64748b; font-weight:600; margin-bottom:4px;">Original Quoted Spend</div>
                <div style="font-size:20px; font-weight:700; color:#94a3b8; text-decoration:line-through; font-family:monospace;">$600,000.00</div>
            </div>
            <div style="background:#eff6ff; border:1px solid #bfdbfe; border-radius:8px; padding:20px;">
                <div style="font-size:11px; color:#1e3a8a; font-weight:600; margin-bottom:4px;">Final Executed Spend (500 Units @ $1,050)</div>
                <div style="font-size:20px; font-weight:800; color:#1e40af; font-family:monospace;">$525,000.00</div>
            </div>
        </div>
    </div>
    """
    sec_opt.append(bs4.BeautifulSoup(opt_html, 'html.parser'))
    main.append(sec_opt)

    # ----------------------------------------------------
    # SECTION 5: FINAL CTA
    # ----------------------------------------------------
    s5 = soup.new_tag('section', **{'style': 'padding: 100px 24px; text-align:center;'})
    s5_html = """
    <div style="max-width:600px; margin:0 auto;">
        <h2 style="font-size: 2.5rem; font-weight: 800; color: #0f172a; margin-bottom: 16px; letter-spacing:-0.02em;">Ready to command?</h2>
        <p style="font-size: 1.125rem; color: #475569; margin-bottom: 32px;">Deploy your first AI agent today and experience the speed of autonomous procurement.</p>
        <a href="https://app.nexmartshop.ai/sign-up" class="btn-solid" style="padding:14px 28px; font-size:14px;">Launch Procurement Mission</a>
    </div>
    """
    s5.append(bs4.BeautifulSoup(s5_html, 'html.parser'))
    main.append(s5)

    main.append(footer)

    with open('agentic-commerce.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    print("Enterprise Realism implementation complete.")

if __name__ == '__main__':
    run()
