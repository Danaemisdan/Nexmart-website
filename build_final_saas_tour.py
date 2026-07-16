import bs4
import copy

def run():
    with open('agentic-commerce.html', 'r', encoding='utf-8') as f:
        soup = bs4.BeautifulSoup(f, 'html.parser')
    
    # ----------------------------------------------------
    # CSS specifically for the SaaS tour
    # ----------------------------------------------------
    style = soup.new_tag('style')
    style.string = """
    :root {
        --saas-bg: #0f172a;
        --saas-panel: #1e293b;
        --saas-border: #334155;
        --saas-text-main: #f8fafc;
        --saas-text-muted: #94a3b8;
        --saas-accent: #3b82f6;
        --saas-success: #10b981;
        --saas-warning: #f59e0b;
        --saas-danger: #ef4444;
    }

    body { background: #f8fafc; } /* Website base background */

    /* Animations */
    @keyframes pulse-dot { 0% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.4); } 70% { box-shadow: 0 0 0 6px rgba(16, 185, 129, 0); } 100% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); } }
    @keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }
    @keyframes load-bar { 0% { width: 0%; } 50% { width: 80%; } 100% { width: 100%; } }
    @keyframes scroll-up { 0% { transform: translateY(20px); opacity: 0; } 100% { transform: translateY(0); opacity: 1; } }

    .pulse-green { animation: pulse-dot 2s infinite; }
    .blink { animation: blink 1s step-end infinite; }
    
    /* Shared Application Window Frame */
    .app-window {
        background: var(--saas-bg);
        border: 1px solid var(--saas-border);
        border-radius: 16px;
        box-shadow: 0 24px 80px rgba(15, 23, 42, 0.2), 0 0 0 1px rgba(255,255,255,0.05) inset;
        overflow: hidden;
        display: flex;
        flex-direction: column;
    }
    .app-header {
        height: 50px;
        background: rgba(15, 23, 42, 0.95);
        border-bottom: 1px solid var(--saas-border);
        display: flex;
        align-items: center;
        padding: 0 20px;
        gap: 8px;
    }
    .app-dot { width: 10px; height: 10px; border-radius: 50%; }
    .app-dot.r { background: #ef4444; } .app-dot.y { background: #f59e0b; } .app-dot.g { background: #10b981; }
    
    /* Hero Specifically */
    .hero-app { height: 75vh; min-height: 700px; margin-top: 40px; }
    .hero-layout { display: flex; flex: 1; overflow: hidden; }
    .hero-sidebar { width: 260px; background: #0b1120; border-right: 1px solid var(--saas-border); padding: 24px; display: flex; flex-direction: column; gap: 32px; overflow-y: auto; }
    .hero-main { flex: 1; padding: 40px; overflow-y: auto; display: flex; flex-direction: column; gap: 32px; background: radial-gradient(circle at top right, rgba(30, 41, 59, 0.4), transparent 50%), var(--saas-bg); }
    
    .nav-group-title { font-size: 10px; text-transform: uppercase; letter-spacing: 0.1em; color: var(--saas-text-muted); margin-bottom: 12px; font-weight: 600; }
    .nav-item { display: flex; align-items: center; gap: 12px; padding: 8px 12px; color: var(--saas-text-muted); font-size: 13px; border-radius: 6px; font-weight: 500; cursor: default; }
    .nav-item.active { background: rgba(59, 130, 246, 0.15); color: var(--saas-accent); }
    
    /* Mission Details */
    .mission-panel { background: var(--saas-panel); border: 1px solid var(--saas-border); border-radius: 12px; padding: 24px; }
    .mission-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; margin-top: 24px; padding-top: 24px; border-top: 1px dashed var(--saas-border); }
    .m-label { font-size: 11px; text-transform: uppercase; color: var(--saas-text-muted); margin-bottom: 6px; font-family: monospace; }
    .m-val { font-size: 14px; color: var(--saas-text-main); font-weight: 600; }
    
    /* Agent Status Grid */
    .agent-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; }
    .agent-card { background: rgba(0,0,0,0.2); border: 1px solid var(--saas-border); border-radius: 8px; padding: 16px; }
    .ac-head { display: flex; justify-content: space-between; margin-bottom: 12px; align-items: center; }
    .ac-name { font-size: 13px; color: #fff; font-weight: 600; }
    .ac-stat { font-size: 11px; font-family: monospace; padding: 2px 6px; border-radius: 4px; }
    .ac-stat.run { background: rgba(16, 185, 129, 0.1); color: var(--saas-success); border: 1px solid rgba(16, 185, 129, 0.2); }
    .ac-log { font-family: monospace; font-size: 11px; color: var(--saas-text-muted); background: #000; padding: 8px; border-radius: 4px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap; }
    
    /* Progress Bar */
    .prog-bg { width: 100%; height: 4px; background: rgba(255,255,255,0.05); border-radius: 2px; margin-top: 12px; overflow: hidden; }
    .prog-fill { height: 100%; background: var(--saas-accent); border-radius: 2px; animation: load-bar 3s cubic-bezier(0.4, 0, 0.2, 1) forwards; }
    
    /* Zoomed Modules */
    .zoom-module { margin: 120px auto; max-width: 1120px; }
    .zoom-header { text-align: center; margin-bottom: 60px; max-width: 700px; margin-left: auto; margin-right: auto; }
    .zoom-title { font-size: 2.5rem; font-weight: 800; color: #0f172a; margin-bottom: 16px; letter-spacing: -0.02em; }
    .zoom-desc { font-size: 1.25rem; color: #475569; }
    
    /* Light UI for Analytics (Contrast) */
    .app-window-light {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        box-shadow: 0 24px 80px rgba(15, 23, 42, 0.08);
        overflow: hidden;
    }
    
    @media (max-width: 991px) {
        .hero-sidebar { display: none; }
        .mission-grid { grid-template-columns: repeat(2, 1fr); }
    }
    @media (max-width: 767px) {
        .agent-grid { grid-template-columns: 1fr; }
        .hero-app { height: auto; }
    }
    """
    
    # Clean previous styles and add new one
    for s in soup.head.find_all('style'):
        if s.string and ('Hero Specific UI Variables' in s.string or 'Product UI Framework' in s.string):
            s.decompose()
    soup.head.append(style)

    main = soup.find('main')
    
    # Retain only the footer
    footer = main.find(class_='footer_component')
    main.clear()
    
    # ----------------------------------------------------
    # SECTION 1: HERO (Massive SaaS App)
    # ----------------------------------------------------
    hero_section = soup.new_tag('section')
    hero_section['style'] = "padding: 120px 24px 0 24px; position: relative;"
    
    hero_html = """
    <div style="text-align:center; max-width:800px; margin:0 auto 40px auto; position:relative; z-index:10;">
        <div style="display:inline-block; padding:6px 12px; background:rgba(59,130,246,0.1); color:#2563eb; font-size:12px; font-weight:700; letter-spacing:0.05em; border-radius:20px; margin-bottom:24px;">AGENTIC COMMERCE INTERFACE</div>
        <h1 style="font-size:4.5rem; font-weight:800; color:#0f172a; line-height:1.1; letter-spacing:-0.03em; margin-bottom:24px;">Execution is the new search.</h1>
        <p style="font-size:1.25rem; color:#475569;">Don't search for suppliers. Command a fleet of AI agents to discover, negotiate, and secure your procurement objectives autonomously.</p>
    </div>
    
    <div style="max-width: 1400px; margin: 0 auto; position:relative; z-index:10;">
        <div class="app-window hero-app">
            <div class="app-header">
                <div class="app-dot r"></div><div class="app-dot y"></div><div class="app-dot g"></div>
                <div style="margin-left:auto; font-family:monospace; font-size:11px; color:var(--saas-text-muted);">ENCRYPTED CONNECTION : NX-SECURE</div>
            </div>
            <div class="hero-layout">
                <div class="hero-sidebar">
                    <div>
                        <div class="nav-group-title">Organization</div>
                        <div class="nav-item">Acme Retail Nigeria</div>
                        <div class="nav-item">Team Directory</div>
                    </div>
                    <div>
                        <div class="nav-group-title">Procurement</div>
                        <div class="nav-item active">Active Missions <div class="pulse-green" style="width:6px;height:6px;border-radius:50%;background:var(--saas-success);margin-left:auto;"></div></div>
                        <div class="nav-item">Supplier Network</div>
                        <div class="nav-item">Live Negotiations</div>
                        <div class="nav-item">Purchase Orders</div>
                        <div class="nav-item">Contracts</div>
                    </div>
                    <div>
                        <div class="nav-group-title">Logistics</div>
                        <div class="nav-item">Warehouses</div>
                        <div class="nav-item">Global Freight</div>
                    </div>
                    <div>
                        <div class="nav-group-title">Risk & Analytics</div>
                        <div class="nav-item">Compliance Hub</div>
                        <div class="nav-item">Savings Analytics</div>
                        <div class="nav-item">CO2 Monitoring</div>
                    </div>
                </div>
                
                <div class="hero-main">
                    <!-- Mission Header -->
                    <div class="mission-panel">
                        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:16px;">
                            <div style="font-family:monospace; font-size:12px; color:var(--saas-accent);">MISSION ID: NX-9482-B</div>
                            <div style="font-family:monospace; font-size:11px; padding:4px 8px; background:rgba(59,130,246,0.1); color:var(--saas-accent); border:1px solid rgba(59,130,246,0.2); border-radius:4px;">STATUS: ORCHESTRATING</div>
                        </div>
                        <div style="font-size:24px; color:#fff; font-weight:500; line-height:1.4;">
                            Procure 500 ergonomic office chairs from SOC2-compliant suppliers.<span class="blink" style="border-right:2px solid var(--saas-accent); margin-left:4px;"></span>
                        </div>
                        
                        <div class="mission-grid">
                            <div><div class="m-label">Max Budget</div><div class="m-val">$600,000.00</div></div>
                            <div><div class="m-label">Destination</div><div class="m-val">Lagos, Nigeria (LOS)</div></div>
                            <div><div class="m-label">Required By</div><div class="m-val">Friday, 14:00 GMT</div></div>
                            <div><div class="m-label">Compliance</div><div class="m-val">SOC2, ISO 9001</div></div>
                        </div>
                    </div>
                    
                    <!-- Agent Statuses -->
                    <div>
                        <div style="font-family:monospace; font-size:11px; color:var(--saas-text-muted); margin-bottom:12px;">AGENT TELEMETRY</div>
                        <div class="agent-grid">
                            <div class="agent-card" style="border-color:var(--saas-accent);">
                                <div class="ac-head">
                                    <div class="ac-name">Discovery Agent</div>
                                    <div class="ac-stat run">RUNNING</div>
                                </div>
                                <div class="ac-log">> Scraping 4,821 global catalogs...</div>
                                <div class="prog-bg"><div class="prog-fill" style="animation-duration: 4s;"></div></div>
                            </div>
                            <div class="agent-card">
                                <div class="ac-head">
                                    <div class="ac-name">Compliance Agent</div>
                                    <div class="ac-stat run">RUNNING</div>
                                </div>
                                <div class="ac-log">> Cross-referencing SOC2 databases...</div>
                                <div class="prog-bg"><div class="prog-fill" style="animation-duration: 2.5s;"></div></div>
                            </div>
                            <div class="agent-card">
                                <div class="ac-head">
                                    <div class="ac-name">Negotiation Agent</div>
                                    <div class="ac-stat" style="background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1);">IDLE</div>
                                </div>
                                <div class="ac-log">> Awaiting supplier shortlist</div>
                                <div class="prog-bg"></div>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Real-time Live Feed -->
                    <div style="flex:1; display:flex; flex-direction:column;">
                        <div style="font-family:monospace; font-size:11px; color:var(--saas-text-muted); margin-bottom:12px; display:flex; justify-content:space-between;">
                            <span>LIVE COMMERCE FEED</span>
                            <span>LATENCY: 14ms</span>
                        </div>
                        <div style="background:#0b1120; border:1px solid var(--saas-border); border-radius:12px; padding:16px; flex:1; font-family:monospace; font-size:12px; color:var(--saas-text-muted); display:flex; flex-direction:column; gap:8px;">
                            <div><span style="color:var(--saas-success);">[SUCCESS]</span> Authentication verified via SAML.</div>
                            <div><span style="color:#fff;">[SYSTEM]</span> Mission NX-9482-B allocated 14 parallel threads.</div>
                            <div><span style="color:var(--saas-accent);">[DISCOVERY]</span> Filtering out non-SOC2 suppliers (Removed 14,020 / Retained 84).</div>
                            <div><span style="color:var(--saas-accent);">[DISCOVERY]</span> Calculating estimated freight to LOS...</div>
                            <div style="display:flex; align-items:center; gap:8px; color:#fff;">
                                <div style="width:12px; height:12px; border:2px solid var(--saas-text-muted); border-top-color:var(--saas-accent); border-radius:50%; animation: spin 1s linear infinite;"></div>
                                Compiling supplier matrix...
                            </div>
                        </div>
                    </div>
                    
                </div>
            </div>
        </div>
    </div>
    """
    hero_section.append(bs4.BeautifulSoup(hero_html, 'html.parser'))
    main.append(hero_section)

    # ----------------------------------------------------
    # SECTION 2: ZOOM 1 (Negotiation Timeline)
    # ----------------------------------------------------
    s2 = soup.new_tag('section', **{'class': 'zoom-module', 'style': 'padding: 0 24px;'})
    s2_html = """
    <div class="zoom-header">
        <h2 class="zoom-title">Negotiation is now a spectator sport.</h2>
        <p class="zoom-desc">Watch as AI agents autonomously engage with suppliers in real-time, leveraging your purchasing history and volume data to aggressively counter-offer and secure the best margins.</p>
    </div>
    
    <div class="app-window" style="background:var(--saas-panel); max-width:900px; margin:0 auto; box-shadow:0 30px 100px rgba(0,0,0,0.15);">
        <div class="app-header" style="justify-content:space-between; background:var(--saas-bg);">
            <div style="display:flex; gap:8px;"><div class="app-dot r"></div><div class="app-dot y"></div><div class="app-dot g"></div></div>
            <div style="font-size:12px; font-weight:600; color:#fff;">Thread: Herman Miller Direct B2B</div>
            <div style="font-size:11px; font-family:monospace; color:var(--saas-success);">SECURE CHANNEL</div>
        </div>
        <div style="padding:40px; display:flex; flex-direction:column; gap:24px;">
            
            <!-- Supplier Msg -->
            <div style="display:flex; gap:16px;">
                <div style="width:36px; height:36px; border-radius:8px; background:#fff; display:flex; align-items:center; justify-content:center; flex-shrink:0;">
                    <span style="color:#000; font-weight:800; font-size:14px;">HM</span>
                </div>
                <div style="background:rgba(255,255,255,0.05); padding:16px 20px; border-radius:12px; border:1px solid var(--saas-border); color:var(--saas-text-main); font-size:14px; max-width:80%;">
                    Thank you for the inquiry. For 500 units of the Aeron, our standard B2B rate applies. We can offer this lot at $1,200/unit. Total: $600,000. DDP to Lagos within 14 days.
                    <div style="margin-top:12px; padding-top:12px; border-top:1px solid var(--saas-border); font-size:12px; color:var(--saas-text-muted); display:flex; justify-content:space-between;">
                        <span>Quote ID: #Q-9942</span>
                        <span>14:08 GMT</span>
                    </div>
                </div>
            </div>
            
            <!-- Agent Logic Overlay (Internal) -->
            <div style="margin-left:52px; padding:12px; background:rgba(0,0,0,0.3); border-left:2px solid var(--saas-accent); font-family:monospace; font-size:11px; color:var(--saas-text-muted); border-radius:0 8px 8px 0;">
                <div style="color:var(--saas-accent); margin-bottom:4px;">[INTERNAL LOGIC TRACE]</div>
                <div>> Historical data check: Last 3 orders averaged $1,080/unit.</div>
                <div>> Volume leverage detected (Tier 3 Quantity).</div>
                <div>> Generating counter-offer at $1,050/unit to anchor negotiation.</div>
            </div>
            
            <!-- Agent Msg -->
            <div style="display:flex; gap:16px; flex-direction:row-reverse;">
                <div style="width:36px; height:36px; border-radius:8px; background:var(--saas-accent); display:flex; align-items:center; justify-content:center; flex-shrink:0; box-shadow:0 0 20px rgba(59,130,246,0.4);">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
                </div>
                <div style="background:var(--saas-bg); padding:16px 20px; border-radius:12px; border:1px solid var(--saas-accent); color:var(--saas-text-main); font-size:14px; max-width:80%;">
                    Based on Acme Retail's purchasing history of 2,400 total units this year, and adjusting for current Q3 excess inventory markers, we propose a volume counter-offer of <strong>$1,050/unit</strong>.
                    <div style="margin-top:12px; padding-top:12px; border-top:1px solid var(--saas-border); font-size:12px; color:var(--saas-accent); display:flex; justify-content:space-between; align-items:center;">
                        <span>System Generated Counter-Offer</span>
                        <div style="display:flex; gap:8px;">
                            <button style="background:rgba(59,130,246,0.2); border:none; color:#fff; padding:4px 12px; border-radius:4px; cursor:pointer;">View Analytics</button>
                        </div>
                    </div>
                </div>
            </div>
            
        </div>
    </div>
    """
    s2.append(bs4.BeautifulSoup(s2_html, 'html.parser'))
    main.append(s2)

    # ----------------------------------------------------
    # SECTION 3: ZOOM 2 (Supplier Intelligence - Light UI)
    # ----------------------------------------------------
    s3 = soup.new_tag('section', **{'class': 'zoom-module', 'style': 'padding: 0 24px;'})
    s3_html = """
    <div class="zoom-header">
        <h2 class="zoom-title">Deep supplier intelligence.</h2>
        <p class="zoom-desc">Never guess on compliance or reliability. The platform synthesizes global risk metrics, CO2 impact, and historic performance before ever presenting an option.</p>
    </div>
    
    <div class="app-window-light" style="max-width:1000px; margin:0 auto;">
        <div style="padding:32px; border-bottom:1px solid #e2e8f0; display:flex; justify-content:space-between; align-items:center;">
            <div>
                <h3 style="font-size:20px; font-weight:700; color:#0f172a; margin-bottom:4px;">Qualified Suppliers Matrix</h3>
                <p style="font-size:14px; color:#64748b; margin:0;">Filtered for: 500 Units | SOC2 | Delivery to LOS</p>
            </div>
            <button style="background:#f1f5f9; border:1px solid #cbd5e1; color:#0f172a; padding:8px 16px; border-radius:6px; font-weight:600; font-size:13px;">Export CSV</button>
        </div>
        
        <table style="width:100%; border-collapse:collapse; text-align:left;">
            <tr style="background:#f8fafc; border-bottom:1px solid #e2e8f0; font-size:12px; text-transform:uppercase; color:#64748b; font-weight:700; letter-spacing:0.05em;">
                <th style="padding:16px 32px;">Vendor Profile</th>
                <th style="padding:16px 32px;">Risk Score</th>
                <th style="padding:16px 32px;">Compliance</th>
                <th style="padding:16px 32px;">CO2 Impact</th>
                <th style="padding:16px 32px;">Unit Price (Neg.)</th>
            </tr>
            <!-- Row 1 (Winner) -->
            <tr style="border-bottom:1px solid #e2e8f0; background:rgba(16,185,129,0.03);">
                <td style="padding:24px 32px;">
                    <div style="display:flex; align-items:center; gap:12px;">
                        <div style="width:40px; height:40px; background:#0f172a; border-radius:8px; display:flex; align-items:center; justify-content:center; color:#fff; font-weight:700;">HM</div>
                        <div>
                            <div style="font-weight:700; color:#0f172a; font-size:15px; display:flex; align-items:center; gap:8px;">Herman Miller B2B <span style="background:#10b981; color:#fff; font-size:10px; padding:2px 6px; border-radius:12px; font-weight:700; letter-spacing:0.05em;">RECOMMENDED</span></div>
                            <div style="color:#64748b; font-size:13px;">Direct Manufacturer</div>
                        </div>
                    </div>
                </td>
                <td style="padding:24px 32px;"><span style="color:#10b981; font-weight:700; font-family:monospace; font-size:15px;">12 / 100</span> <span style="font-size:12px; color:#64748b;">(Low)</span></td>
                <td style="padding:24px 32px;"><div style="display:flex; gap:4px;"><span style="border:1px solid #cbd5e1; font-size:11px; padding:2px 6px; border-radius:4px; color:#475569;">SOC2</span><span style="border:1px solid #cbd5e1; font-size:11px; padding:2px 6px; border-radius:4px; color:#475569;">ISO9001</span></div></td>
                <td style="padding:24px 32px; color:#0f172a; font-weight:600; font-size:14px;">14.2 kg/unit</td>
                <td style="padding:24px 32px; font-family:monospace; font-size:16px; font-weight:700; color:#0f172a;">$1,050.00</td>
            </tr>
            <!-- Row 2 -->
            <tr style="border-bottom:1px solid #e2e8f0;">
                <td style="padding:24px 32px;">
                    <div style="display:flex; align-items:center; gap:12px;">
                        <div style="width:40px; height:40px; background:#f1f5f9; border-radius:8px; display:flex; align-items:center; justify-content:center; color:#475569; font-weight:700; border:1px solid #e2e8f0;">SG</div>
                        <div>
                            <div style="font-weight:600; color:#0f172a; font-size:15px;">Steelcase Global</div>
                            <div style="color:#64748b; font-size:13px;">Wholesale Distributor</div>
                        </div>
                    </div>
                </td>
                <td style="padding:24px 32px;"><span style="color:#f59e0b; font-weight:700; font-family:monospace; font-size:15px;">42 / 100</span> <span style="font-size:12px; color:#64748b;">(Med)</span></td>
                <td style="padding:24px 32px;"><div style="display:flex; gap:4px;"><span style="border:1px solid #cbd5e1; font-size:11px; padding:2px 6px; border-radius:4px; color:#475569;">SOC2</span></div></td>
                <td style="padding:24px 32px; color:#0f172a; font-weight:500; font-size:14px;">22.4 kg/unit</td>
                <td style="padding:24px 32px; font-family:monospace; font-size:15px; font-weight:500; color:#475569;">$1,120.00</td>
            </tr>
        </table>
        
        <div style="padding:20px 32px; background:#f8fafc; text-align:center;">
            <button style="background:transparent; border:none; color:#2563eb; font-weight:600; font-size:14px; cursor:pointer;">View 82 more filtered suppliers →</button>
        </div>
    </div>
    """
    s3.append(bs4.BeautifulSoup(s3_html, 'html.parser'))
    main.append(s3)

    # ----------------------------------------------------
    # SECTION 4: ZOOM 3 (Optimization & Savings - Light UI)
    # ----------------------------------------------------
    s4 = soup.new_tag('section', **{'class': 'zoom-module', 'style': 'padding: 0 24px;'})
    s4_html = """
    <div class="zoom-header">
        <h2 class="zoom-title">Undeniable bottom-line impact.</h2>
        <p class="zoom-desc">See exactly how much margin the agents reclaimed. The platform provides granular breakdowns of logistics savings, volume discounts, and operational efficiency.</p>
    </div>
    
    <div class="app-window-light" style="max-width:800px; margin:0 auto; padding:40px;">
        <div style="text-align:center; margin-bottom:40px;">
            <div style="font-size:12px; font-weight:700; color:#64748b; text-transform:uppercase; letter-spacing:0.1em; margin-bottom:8px;">Mission Financial Summary</div>
            <div style="font-size:4rem; font-weight:800; color:#10b981; line-height:1; font-family:monospace;">$75,000</div>
            <div style="font-size:16px; color:#0f172a; font-weight:600; margin-top:12px;">Total Capital Preserved</div>
        </div>
        
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:24px;">
            <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:12px; padding:24px;">
                <div style="font-size:12px; color:#64748b; margin-bottom:4px; font-weight:600;">Original Budget</div>
                <div style="font-size:24px; font-weight:700; color:#94a3b8; text-decoration:line-through; font-family:monospace;">$600,000.00</div>
                <div style="margin-top:16px; font-size:13px; color:#475569; display:flex; justify-content:space-between; border-top:1px solid #e2e8f0; padding-top:12px;">
                    <span>Procurement Time</span>
                    <span style="font-weight:600;">Est. 48 hours</span>
                </div>
            </div>
            <div style="background:#eff6ff; border:1px solid #bfdbfe; border-radius:12px; padding:24px;">
                <div style="font-size:12px; color:#1e3a8a; margin-bottom:4px; font-weight:600;">Agentic Executed Cost</div>
                <div style="font-size:24px; font-weight:800; color:#1e40af; font-family:monospace;">$525,000.00</div>
                <div style="margin-top:16px; font-size:13px; color:#1e3a8a; display:flex; justify-content:space-between; border-top:1px solid #bfdbfe; padding-top:12px;">
                    <span>Procurement Time</span>
                    <span style="font-weight:800;">3 minutes</span>
                </div>
            </div>
        </div>
    </div>
    """
    s4.append(bs4.BeautifulSoup(s4_html, 'html.parser'))
    main.append(s4)

    # ----------------------------------------------------
    # SECTION 5: FINAL CTA
    # ----------------------------------------------------
    s5 = soup.new_tag('section', **{'style': 'padding: 120px 24px; background:#0f172a; text-align:center;'})
    s5_html = """
    <div style="max-width:600px; margin:0 auto;">
        <h2 style="font-size: 3rem; font-weight: 800; color: #fff; margin-bottom: 24px; letter-spacing:-0.02em;">Ready to command?</h2>
        <p style="font-size: 1.25rem; color: #94a3b8; margin-bottom: 40px;">Deploy your first AI agent today and experience the speed of autonomous procurement.</p>
        <a href="https://app.nexmartshop.ai/sign-up" class="button-main w-button" style="background-color: #3b82f6; color: #fff; padding: 18px 36px; border-radius: 8px; font-size:16px; font-weight:600;">Launch Procurement Mission</a>
    </div>
    """
    s5.append(bs4.BeautifulSoup(s5_html, 'html.parser'))
    main.append(s5)

    # Add footer back
    main.append(footer)
    
    # Add CSS for spin animation
    style.string += "\n@keyframes spin { 100% { transform: rotate(360deg); } }\n"

    with open('agentic-commerce.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    print("SaaS Tour implementation complete.")

if __name__ == '__main__':
    run()
