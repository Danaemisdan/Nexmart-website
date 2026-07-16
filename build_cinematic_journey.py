import bs4

def run():
    with open('agentic-commerce.html', 'r', encoding='utf-8') as f:
        soup = bs4.BeautifulSoup(f, 'html.parser')
    
    # ----------------------------------------------------
    # CSS for the 6-Scene Cinematic Journey
    # ----------------------------------------------------
    style_str = """
    :root {
        --saas-bg: #0f172a;
        --saas-panel: #1e293b;
        --saas-border: #334155;
        --saas-text-main: #f8fafc;
        --saas-text-muted: #94a3b8;
        --saas-accent: #2563eb;
        --saas-success: #10b981;
    }

    body { background: #0f172a; color: #fff; margin: 0; overflow-x: hidden; }

    /* Scene Transitions & Storytelling Framework */
    .scene { position: relative; width: 100%; overflow: hidden; }
    
    /* SCENE 1: THE IGNITION */
    .s1-hero {
        height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        padding-top: 80px; /* Account for navbar */
    }
    .s1-app-window {
        background: var(--saas-bg);
        border: 1px solid var(--saas-border);
        border-bottom: none;
        border-radius: 16px 16px 0 0;
        width: 96%;
        margin: 0 auto;
        height: 88vh;
        display: flex;
        flex-direction: column;
        overflow: hidden;
        box-shadow: 0 -20px 60px rgba(0,0,0,0.5);
    }
    .app-header {
        height: 44px;
        background: var(--saas-panel);
        border-bottom: 1px solid var(--saas-border);
        display: flex;
        align-items: center;
        padding: 0 16px;
        gap: 8px;
    }
    .app-dot { width: 10px; height: 10px; border-radius: 50%; }
    .app-dot.r { background: #ef4444; } .app-dot.y { background: #f59e0b; } .app-dot.g { background: #10b981; }
    
    .s1-layout { display: flex; flex: 1; }
    .s1-main { padding: 40px; display: flex; flex-direction: column; gap: 32px; width: 100%; max-width: 1200px; margin: 0 auto; }
    
    .mission-hud { background: var(--saas-panel); border: 1px solid var(--saas-border); border-radius: 8px; padding: 24px; }
    .m-title { font-size: 24px; font-weight: 500; margin: 12px 0; color: #fff; }
    .m-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; padding-top: 20px; border-top: 1px solid var(--saas-border); }
    .m-label { font-size: 10px; text-transform: uppercase; letter-spacing: 0.1em; color: var(--saas-text-muted); font-weight: 700; }
    .m-val { font-size: 14px; font-family: monospace; color: #fff; margin-top: 4px; }
    
    /* SCENE 2: THE NETWORK (Dark Canvas) */
    .s2-network {
        background: #0b1120;
        min-height: 80vh;
        padding: 120px 24px;
        position: relative;
        border-top: 1px solid var(--saas-border);
    }
    .s2-map {
        position: relative;
        max-width: 1200px;
        margin: 60px auto 0 auto;
        height: 400px;
        background-image: radial-gradient(circle at center, rgba(37,99,235,0.1) 0%, transparent 70%);
    }
    .node { position: absolute; width: 12px; height: 12px; background: var(--saas-accent); border-radius: 50%; box-shadow: 0 0 20px var(--saas-accent); }
    .node-label { position: absolute; font-family: monospace; font-size: 10px; color: var(--saas-text-muted); margin-top: 16px; margin-left: -20px; white-space: nowrap; }
    .node.origin { left: 50%; top: 50%; background: var(--saas-success); box-shadow: 0 0 20px var(--saas-success); }
    .node.f1 { left: 20%; top: 30%; } .node.f2 { left: 70%; top: 20%; } .node.f3 { left: 80%; top: 60%; }
    
    /* SCENE 3: EVALUATION (Floating Cards) */
    .s3-eval {
        background: var(--saas-bg);
        padding: 160px 24px;
        position: relative;
    }
    .s3-cards {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 24px;
        max-width: 1200px;
        margin: 80px auto 0 auto;
    }
    .eval-card {
        background: var(--saas-panel);
        border: 1px solid var(--saas-border);
        border-radius: 12px;
        padding: 32px;
        width: 300px;
        transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .eval-card.rejected {
        transform: scale(0.85) translateY(40px);
        opacity: 0.3;
        filter: grayscale(100%);
    }
    .eval-card.winner {
        transform: scale(1.1);
        border-color: var(--saas-accent);
        box-shadow: 0 24px 60px rgba(0,0,0,0.4), 0 0 0 1px var(--saas-accent) inset;
        z-index: 10;
        background: #1e293b;
    }
    .eval-metric { display: flex; justify-content: space-between; font-size: 12px; margin-top: 16px; padding-top: 16px; border-top: 1px solid var(--saas-border); }
    
    /* SCENE 4: THE ARENA (Split Layout) */
    .s4-arena {
        background: #0b1120;
        padding: 120px 24px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .s4-split {
        max-width: 1400px;
        width: 100%;
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 80px;
    }
    .s4-left { position: sticky; top: 200px; height: max-content; }
    .s4-right { display: flex; flex-direction: column; gap: 24px; }
    .chat-bubble { padding: 16px 20px; border-radius: 12px; max-width: 80%; font-size: 14px; line-height: 1.5; }
    .chat-supplier { background: var(--saas-panel); border: 1px solid var(--saas-border); align-self: flex-start; color: var(--saas-text-muted); }
    .chat-ai { background: var(--saas-accent); color: #fff; align-self: flex-end; box-shadow: 0 10px 30px rgba(37,99,235,0.2); }
    .chat-logic { font-family: monospace; font-size: 11px; color: var(--saas-text-muted); align-self: flex-end; margin-right: 20px; border-right: 2px solid var(--saas-accent); padding-right: 12px; text-align: right; }
    
    /* SCENE 5: THE ROUTE (Horizontal Logistics) */
    .s5-route {
        background: var(--saas-bg);
        padding: 160px 24px;
    }
    .s5-timeline {
        max-width: 1000px;
        margin: 80px auto 0 auto;
        display: flex;
        justify-content: space-between;
        align-items: center;
        position: relative;
    }
    .timeline-line { position: absolute; top: 50%; left: 0; right: 0; height: 2px; background: var(--saas-border); z-index: 1; }
    .timeline-node { position: relative; z-index: 2; background: var(--saas-panel); border: 2px solid var(--saas-border); padding: 24px; border-radius: 12px; width: 200px; text-align: center; }
    .t-icon { font-size: 24px; margin-bottom: 12px; color: #fff; }
    .t-title { font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: var(--saas-text-muted); }
    .t-desc { font-family: monospace; font-size: 11px; color: var(--saas-accent); margin-top: 8px; }
    
    /* SCENE 6: THE OUTCOME (Massive Minimal) */
    .s6-outcome {
        background: #ffffff;
        color: #0f172a;
        padding: 200px 24px;
        text-align: center;
    }
    .outcome-metric { font-size: 8rem; font-weight: 800; letter-spacing: -0.04em; color: #10b981; line-height: 1; margin: 24px 0; font-family: monospace; }
    .btn-massive { background: #0f172a; color: #fff; padding: 20px 40px; font-size: 16px; font-weight: 600; border-radius: 8px; border: none; cursor: pointer; transition: background 0.2s; margin-top: 40px; }
    .btn-massive:hover { background: var(--saas-accent); }
    
    /* Typographic Utilities */
    .scene-h2 { font-size: 2.5rem; font-weight: 700; letter-spacing: -0.02em; margin: 0; }
    .scene-p { font-size: 1.25rem; color: var(--saas-text-muted); margin-top: 16px; max-width: 600px; }
    
    /* Animations */
    @keyframes typing { from { width: 0; } to { width: 100%; } }
    @keyframes blink { 50% { border-color: transparent; } }
    .typewriter { overflow: hidden; white-space: nowrap; border-right: 2px solid var(--saas-accent); animation: typing 2s steps(40, end), blink .75s step-end infinite; }
    
    @media (max-width: 991px) {
        .s4-split { grid-template-columns: 1fr; }
        .s4-left { position: static; text-align: center; margin-bottom: 40px; }
        .s5-timeline { flex-direction: column; gap: 40px; }
        .timeline-line { width: 2px; height: 100%; top: 0; left: 50%; }
        .s3-cards { flex-direction: column; }
        .outcome-metric { font-size: 4rem; }
    }
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
    # SCENE 1: THE IGNITION
    # ----------------------------------------------------
    s1 = soup.new_tag('section', **{'class': 'scene s1-hero'})
    s1.append(bs4.BeautifulSoup("""
    <div class="s1-app-window">
        <div class="app-header">
            <div style="display:flex; gap:6px;"><div class="app-dot r"></div><div class="app-dot y"></div><div class="app-dot g"></div></div>
            <div style="margin-left:auto; font-family:monospace; font-size:10px; color:var(--saas-text-muted);">MISSION CONTROL</div>
        </div>
        <div class="s1-layout">
            <div class="s1-main">
                <div class="mission-hud">
                    <div style="font-family:monospace; font-size:11px; color:var(--saas-success); display:flex; justify-content:space-between;">
                        <span>SYSTEM BOOT COMPLETE</span>
                        <span>[EXECUTING]</span>
                    </div>
                    <h2 class="m-title typewriter">Procure 500 ergonomic office chairs.</h2>
                    <div class="m-grid">
                        <div><div class="m-label">Budget</div><div class="m-val">$600,000</div></div>
                        <div><div class="m-label">Destination</div><div class="m-val">Lagos (LOS)</div></div>
                        <div><div class="m-label">Deadline</div><div class="m-val">Friday, 14:00 GMT</div></div>
                        <div><div class="m-label">Compliance</div><div class="m-val">SOC2 Required</div></div>
                    </div>
                </div>
                
                <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:16px;">
                    <div style="background:#0b1120; border:1px solid var(--saas-border); padding:16px; border-radius:8px;">
                        <div style="font-size:12px; color:var(--saas-text-muted); font-weight:600; margin-bottom:8px;">Discovery Agent</div>
                        <div style="font-family:monospace; font-size:11px; color:var(--saas-success);">> Expanding global search</div>
                    </div>
                    <div style="background:#0b1120; border:1px solid var(--saas-border); padding:16px; border-radius:8px;">
                        <div style="font-size:12px; color:var(--saas-text-muted); font-weight:600; margin-bottom:8px;">Compliance Agent</div>
                        <div style="font-family:monospace; font-size:11px; color:var(--saas-accent);">> Auditing SOC2 records</div>
                    </div>
                    <div style="background:#0b1120; border:1px solid var(--saas-border); padding:16px; border-radius:8px;">
                        <div style="font-size:12px; color:var(--saas-text-muted); font-weight:600; margin-bottom:8px;">Negotiation Agent</div>
                        <div style="font-family:monospace; font-size:11px; color:#64748b;">> Awaiting shortlist</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """, 'html.parser'))
    main.append(s1)

    # ----------------------------------------------------
    # SCENE 2: THE NETWORK (Discovery)
    # ----------------------------------------------------
    s2 = soup.new_tag('section', **{'class': 'scene s2-network'})
    s2.append(bs4.BeautifulSoup("""
    <div style="text-align:center;">
        <h2 class="scene-h2">Global Discovery Network</h2>
        <p class="scene-p" style="margin:16px auto 0 auto;">Simultaneously querying 4,821 supplier databases worldwide to isolate SOC2-compliant manufacturers.</p>
    </div>
    <div class="s2-map">
        <!-- SVG Connections -->
        <svg style="position:absolute; top:0; left:0; width:100%; height:100%; z-index:0;" stroke="rgba(255,255,255,0.05)" stroke-width="1" fill="none">
            <path d="M50% 50% L20% 30%" />
            <path d="M50% 50% L70% 20%" />
            <path d="M50% 50% L80% 60%" />
        </svg>
        <!-- Nodes -->
        <div class="node origin" style="z-index:1;"><div class="node-label" style="color:var(--saas-success); margin-left:-30px;">Mission Origin</div></div>
        <div class="node f1" style="z-index:1;"><div class="node-label">Supplier DB: NA</div></div>
        <div class="node f2" style="z-index:1;"><div class="node-label">Supplier DB: EU</div></div>
        <div class="node f3" style="z-index:1;"><div class="node-label">Supplier DB: APAC</div></div>
    </div>
    """, 'html.parser'))
    main.append(s2)

    # ----------------------------------------------------
    # SCENE 3: EVALUATION (Supplier Cards)
    # ----------------------------------------------------
    s3 = soup.new_tag('section', **{'class': 'scene s3-eval'})
    s3.append(bs4.BeautifulSoup("""
    <div style="text-align:center;">
        <h2 class="scene-h2">Multi-Factor Reasoning</h2>
        <p class="scene-p" style="margin:16px auto 0 auto;">The AI evaluates historical reliability, margin impact, and exact compliance requirements instantly.</p>
    </div>
    <div class="s3-cards">
        <!-- Loser 1 -->
        <div class="eval-card rejected">
            <div style="font-weight:700; font-size:18px; margin-bottom:4px;">Generic Wholesale</div>
            <div style="font-size:12px; color:var(--saas-text-muted);">Broker</div>
            <div class="eval-metric"><span>Risk Score</span><span style="color:var(--saas-danger); font-weight:700;">84 (High)</span></div>
            <div class="eval-metric"><span>Compliance</span><span style="color:var(--saas-danger);">Failed SOC2</span></div>
            <div style="margin-top:24px; padding:8px; background:rgba(239, 68, 68, 0.1); color:var(--saas-danger); font-size:10px; font-weight:700; text-align:center; border-radius:4px;">REJECTED BY COMPLIANCE AGENT</div>
        </div>
        
        <!-- Winner -->
        <div class="eval-card winner">
            <div style="display:flex; justify-content:space-between;">
                <div>
                    <div style="font-weight:700; font-size:20px; color:#fff; margin-bottom:4px;">Herman Miller B2B</div>
                    <div style="font-size:12px; color:var(--saas-text-muted);">Direct Manufacturer</div>
                </div>
                <div style="background:var(--saas-accent); width:32px; height:32px; border-radius:8px; display:flex; align-items:center; justify-content:center;">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg>
                </div>
            </div>
            <div class="eval-metric" style="margin-top:24px;"><span>Risk Score</span><span style="color:var(--saas-success); font-weight:700;">12 (Low)</span></div>
            <div class="eval-metric"><span>Compliance</span><span style="color:var(--saas-success);">SOC2 Verified</span></div>
            <div class="eval-metric"><span>Est. Lead Time</span><span style="color:#fff;">14 Days to LOS</span></div>
            <div style="margin-top:24px; padding:8px; background:rgba(37, 99, 235, 0.1); color:var(--saas-accent); font-size:10px; font-weight:700; text-align:center; border-radius:4px;">PROMOTED TO NEGOTIATION</div>
        </div>
        
        <!-- Loser 2 -->
        <div class="eval-card rejected">
            <div style="font-weight:700; font-size:18px; margin-bottom:4px;">Steelcase Global</div>
            <div style="font-size:12px; color:var(--saas-text-muted);">Distributor</div>
            <div class="eval-metric"><span>Risk Score</span><span style="color:var(--saas-warning); font-weight:700;">42 (Med)</span></div>
            <div class="eval-metric"><span>Compliance</span><span style="color:var(--saas-success);">SOC2 Verified</span></div>
            <div style="margin-top:24px; padding:8px; background:rgba(245, 158, 11, 0.1); color:var(--saas-warning); font-size:10px; font-weight:700; text-align:center; border-radius:4px;">SUB-OPTIMAL MARGIN ($1,250)</div>
        </div>
    </div>
    """, 'html.parser'))
    main.append(s3)

    # ----------------------------------------------------
    # SCENE 4: THE ARENA (Negotiation Split Layout)
    # ----------------------------------------------------
    s4 = soup.new_tag('section', **{'class': 'scene s4-arena'})
    s4.append(bs4.BeautifulSoup("""
    <div class="s4-split">
        <div class="s4-left">
            <h2 class="scene-h2" style="margin-bottom:24px;">Live Negotiation</h2>
            <div style="font-size:12px; text-transform:uppercase; color:var(--saas-text-muted); font-weight:700; letter-spacing:0.1em; margin-bottom:8px;">Capital Preserved</div>
            <div style="font-size:5rem; font-weight:800; color:var(--saas-success); font-family:monospace; line-height:1; letter-spacing:-0.05em;">$75,000</div>
            <p class="scene-p">The AI leverages historical purchasing volume to autonomously negotiate down the base quote from $1,200 to $1,050 per unit.</p>
        </div>
        <div class="s4-right">
            <div class="chat-bubble chat-supplier">
                <div style="font-size:11px; font-weight:700; margin-bottom:6px; color:#fff;">Supplier: Herman Miller</div>
                We can fulfill 500 units DDP to Lagos at $1,200/unit. Total: $600,000.
            </div>
            
            <div class="chat-logic">
                > Cross-referencing Acme Retail YTD spend (2,400 units).<br>
                > Volume Tier 3 identified.<br>
                > Generating counter-offer...
            </div>
            
            <div class="chat-bubble chat-ai">
                <div style="font-size:11px; font-weight:700; margin-bottom:6px;">Agentic Negotiator</div>
                Based on our client's consolidated YTD volume, we propose a counter-offer of $1,050/unit to proceed.
            </div>
            
            <div class="chat-bubble chat-supplier" style="border-color:var(--saas-success);">
                <div style="font-size:11px; font-weight:700; margin-bottom:6px; color:var(--saas-success);">Supplier: Herman Miller</div>
                Accepted. We will lock the lot at $525,000 total. Forwarding contract.
            </div>
        </div>
    </div>
    """, 'html.parser'))
    main.append(s4)

    # ----------------------------------------------------
    # SCENE 5: THE ROUTE (Logistics Horizontal)
    # ----------------------------------------------------
    s5 = soup.new_tag('section', **{'class': 'scene s5-route'})
    s5.append(bs4.BeautifulSoup("""
    <div style="text-align:center;">
        <h2 class="scene-h2">Optimized Logistics Routing</h2>
        <p class="scene-p" style="margin:16px auto 0 auto;">Autonomous procurement doesn't end at the contract. The AI models the fastest, most carbon-efficient route to your final destination.</p>
    </div>
    <div class="s5-timeline">
        <div class="timeline-line"></div>
        
        <div class="timeline-node">
            <div class="t-icon">🏭</div>
            <div class="t-title">Factory Origin</div>
            <div class="t-desc">Michigan, USA</div>
        </div>
        
        <div class="timeline-node" style="border-color:var(--saas-accent); box-shadow: 0 0 30px rgba(37,99,235,0.1);">
            <div class="t-icon">🚢</div>
            <div class="t-title">Freight Optimized</div>
            <div class="t-desc" style="color:var(--saas-text-main);">Port of Newark -> LOS</div>
        </div>
        
        <div class="timeline-node">
            <div class="t-icon">🏢</div>
            <div class="t-title">Destination</div>
            <div class="t-desc">Lagos HQ Warehouse</div>
        </div>
    </div>
    """, 'html.parser'))
    main.append(s5)

    # ----------------------------------------------------
    # SCENE 6: THE OUTCOME (Minimal Metrics)
    # ----------------------------------------------------
    s6 = soup.new_tag('section', **{'class': 'scene s6-outcome'})
    s6.append(bs4.BeautifulSoup("""
    <div style="font-size:14px; font-weight:700; color:#64748b; text-transform:uppercase; letter-spacing:0.1em;">Mission Accomplished</div>
    <div class="outcome-metric">$75,000</div>
    <h2 style="font-size:2.5rem; font-weight:700; color:#0f172a; margin:0; letter-spacing:-0.02em;">Total Capital Preserved.</h2>
    <p style="font-size:1.25rem; color:#475569; max-width:600px; margin:24px auto 0 auto;">Mission NX-9482-B completed in 3 minutes. 500 units secured, routed, and contracted autonomously.</p>
    
    <a href="https://app.nexmartshop.ai/sign-up" class="btn-massive w-button">Launch Procurement Mission</a>
    """, 'html.parser'))
    main.append(s6)

    main.append(footer)

    with open('agentic-commerce.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    print("Cinematic Journey implementation complete.")

if __name__ == '__main__':
    run()
