import bs4

def run():
    with open('agentic-commerce.html', 'r', encoding='utf-8') as f:
        soup = bs4.BeautifulSoup(f, 'html.parser')
    
    style_str = """
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap');

    :root {
        --pure-white: #ffffff;
        --slate-900: #0f172a;
        --slate-800: #1e293b;
        --slate-400: #94a3b8;
        --slate-200: #e2e8f0;
        --accent-blue: #0070f3;
        --success-green: #10b981;
        --app-bg: #09090b; /* Very deep premium charcoal/black */
    }

    body, html {
        margin: 0;
        padding: 0;
        width: 100%;
        font-family: 'Inter', -apple-system, sans-serif;
        background: var(--pure-white);
        color: var(--slate-900);
        overflow-x: hidden;
    }

    /* 
      SEAMLESS FLOW CONTAINER 
      This prevents any hard cuts. The page is one continuous scroll.
    */
    .seamless-page-wrapper {
        position: relative;
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        background: linear-gradient(180deg, var(--pure-white) 0%, var(--pure-white) 45vh, var(--app-bg) 75vh);
    }

    /* THE TYPOGRAPHY (DO NOT CHANGE) */
    .v1-typography {
        text-align: center;
        max-width: 1000px;
        padding: 16vh 24px 0 24px;
        z-index: 20;
    }

    .v1-title {
        font-size: 6.5rem;
        font-weight: 700;
        letter-spacing: -0.05em;
        line-height: 1.05;
        color: var(--slate-900);
        margin: 0 0 24px 0;
    }

    .v1-subtitle {
        font-size: 1.5rem;
        font-weight: 300;
        color: #64748b;
        max-width: 600px;
        margin: 0 auto 56px auto;
        letter-spacing: -0.01em;
        line-height: 1.4;
    }

    /* THE BRIDGE: Command Module & Agent Widgets */
    .v1-bridge-container {
        position: relative;
        width: 100%;
        max-width: 1100px;
        display: flex;
        flex-direction: column;
        align-items: center;
        z-index: 30; /* Floats above everything */
        margin-bottom: -150px; /* Pulls the application up underneath it to create overlap */
    }

    /* Floating Command Interface */
    .v1-command-module {
        width: 100%;
        max-width: 720px;
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(0, 0, 0, 0.05);
        border-radius: 100px;
        padding: 16px 24px;
        display: flex;
        align-items: center;
        gap: 20px;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.04), 0 1px 3px rgba(0,0,0,0.02);
        z-index: 35;
        margin-bottom: 40px;
    }

    .cmd-icon-box {
        width: 48px;
        height: 48px;
        border-radius: 50%;
        background: var(--slate-900);
        display: flex;
        align-items: center;
        justify-content: center;
        color: #fff;
        flex-shrink: 0;
        box-shadow: 0 10px 20px rgba(15, 23, 42, 0.2);
    }

    .cmd-input {
        font-size: 1.25rem;
        font-weight: 400;
        color: var(--slate-900);
        flex-grow: 1;
        display: flex;
        align-items: center;
    }

    .typewriter-text {
        display: inline-block;
        overflow: hidden;
        white-space: nowrap;
        width: 0;
        animation: typing 2.5s steps(40, end) forwards 1s;
    }
    
    .cursor {
        display: inline-block;
        width: 2px;
        height: 1.5rem;
        background: var(--accent-blue);
        margin-left: 4px;
        animation: blink 1s step-end infinite;
    }

    @keyframes typing { from { width: 0; } to { width: 100%; } }
    @keyframes blink { 50% { opacity: 0; } }

    /* The Agent Widgets (The "Substantial Body" bridging the gap) */
    .agent-widgets-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 24px;
        width: 100%;
        padding: 0 24px;
    }

    .agent-widget {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(0,0,0,0.04);
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 30px 60px rgba(0,0,0,0.05);
        opacity: 0;
        transform: translateY(20px);
        animation: float-up 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }
    
    .agent-widget:nth-child(1) { animation-delay: 3.5s; }
    .agent-widget:nth-child(2) { animation-delay: 3.7s; }
    .agent-widget:nth-child(3) { animation-delay: 3.9s; }

    @keyframes float-up { to { opacity: 1; transform: translateY(0); } }

    .widget-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; }
    .widget-title { font-size: 13px; font-weight: 600; color: var(--slate-900); }
    .widget-status { font-family: 'JetBrains Mono', monospace; font-size: 10px; font-weight: 700; color: var(--success-green); background: rgba(16,185,129,0.1); padding: 4px 8px; border-radius: 4px; }
    
    .widget-log { font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #64748b; line-height: 1.5; margin-bottom: 16px; }
    
    .widget-data { display: flex; align-items: center; gap: 8px; padding-top: 16px; border-top: 1px solid rgba(0,0,0,0.05); }
    .w-val { font-size: 14px; font-weight: 600; color: var(--slate-900); }
    .w-lbl { font-size: 12px; color: #64748b; }

    /* THE CONTINUOUS APPLICATION ENVIRONMENT */
    .v1-app-environment {
        width: 95vw;
        max-width: 1400px;
        background: var(--app-bg);
        border-radius: 24px 24px 0 0;
        border: 1px solid rgba(255,255,255,0.08);
        border-bottom: none;
        box-shadow: 0 -40px 100px rgba(0,0,0,0.15), 0 0 0 1px rgba(255,255,255,0.02) inset;
        z-index: 20;
        padding-top: 180px; /* Massive padding to accommodate the overlapping widgets */
        padding-bottom: 200px; /* Let it flow continuously downwards */
        position: relative;
    }

    .app-inner-glow {
        position: absolute;
        top: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 100%;
        height: 600px;
        background: radial-gradient(ellipse at top, rgba(0, 112, 243, 0.08) 0%, transparent 70%);
        pointer-events: none;
        border-radius: 24px 24px 0 0;
    }

    /* Live Commerce Table Inside the App */
    .commerce-matrix {
        width: 100%;
        max-width: 1100px;
        margin: 0 auto;
        display: flex;
        flex-direction: column;
        gap: 12px;
        position: relative;
        z-index: 25;
    }
    
    .matrix-header {
        display: flex;
        justify-content: space-between;
        padding: 0 24px 16px 24px;
        border-bottom: 1px solid rgba(255,255,255,0.1);
        margin-bottom: 8px;
    }
    
    .mh-title { font-size: 18px; font-weight: 600; color: #fff; }
    .mh-status { font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #a1a1aa; display: flex; align-items: center; gap: 8px; }
    .mh-dot { width: 6px; height: 6px; background: var(--accent-blue); border-radius: 50%; box-shadow: 0 0 10px var(--accent-blue); }

    .matrix-row {
        background: rgba(255,255,255,0.02);
        border: 1px solid rgba(255,255,255,0.05);
        border-radius: 12px;
        padding: 20px 24px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        transition: transform 0.3s, background 0.3s;
    }
    
    .matrix-row:hover {
        background: rgba(255,255,255,0.04);
        transform: translateY(-2px);
    }
    
    .mr-supplier { display: flex; flex-direction: column; gap: 4px; width: 25%; }
    .mr-name { font-size: 15px; font-weight: 600; color: #fff; }
    .mr-type { font-size: 12px; color: #71717a; }
    
    .mr-data { display: flex; flex-direction: column; gap: 4px; width: 20%; }
    .mrd-val { font-family: 'JetBrains Mono', monospace; font-size: 13px; color: #e4e4e7; }
    .mrd-lbl { font-size: 11px; color: #71717a; text-transform: uppercase; letter-spacing: 0.05em; }
    
    .mr-badge { padding: 6px 12px; border-radius: 100px; font-size: 11px; font-weight: 600; background: rgba(255,255,255,0.05); color: #fff; }
    .mr-badge.green { background: rgba(16,185,129,0.1); color: var(--success-green); border: 1px solid rgba(16,185,129,0.2); }
    .mr-badge.blue { background: rgba(59,130,246,0.1); color: #60a5fa; border: 1px solid rgba(59,130,246,0.2); }

    @media (max-width: 991px) {
        .v1-title { font-size: 4rem; }
        .v1-command-module { width: 90%; }
        .cmd-input { font-size: 1rem; }
        .agent-widgets-grid { grid-template-columns: 1fr; }
        .v1-bridge-container { margin-bottom: -50px; }
        .v1-app-environment { padding-top: 100px; width: 100vw; border-radius: 0; }
        .matrix-row { flex-direction: column; align-items: flex-start; gap: 16px; }
        .mr-supplier, .mr-data { width: 100%; }
    }
    """

    for s in soup.head.find_all('style'):
        if s.string and ('Hero Specific UI Variables' in s.string or 'Product UI Framework' in s.string or '--pure-white' in s.string):
            s.decompose()
            
    style = soup.new_tag('style')
    style.string = style_str
    soup.head.append(style)

    main = soup.find('main')
    footer = main.find(class_='footer_component')
    main.clear()

    hero_html = """
    <div class="seamless-page-wrapper">
        
        <!-- THE TYPOGRAPHY -->
        <div class="v1-typography">
            <h1 class="v1-title">Command the global economy.</h1>
            <p class="v1-subtitle">A single intent orchestrates thousands of autonomous procurement decisions across the world in real time.</p>
        </div>

        <!-- THE BRIDGE: Command & Agent Widgets -->
        <div class="v1-bridge-container">
            <!-- Premium Floating Interface -->
            <div class="v1-command-module">
                <div class="cmd-icon-box">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 16 16 12 12 8"></polyline><line x1="8" y1="12" x2="16" y2="12"></line></svg>
                </div>
                <div class="cmd-input">
                    <span class="typewriter-text">Procure 500 chairs for Lagos.</span><span class="cursor"></span>
                </div>
            </div>

            <!-- Agent Widgets providing BODY and connecting the white space to the dark app -->
            <div class="agent-widgets-grid">
                
                <div class="agent-widget">
                    <div class="widget-header">
                        <span class="widget-title">Discovery Agent</span>
                        <span class="widget-status">RUNNING</span>
                    </div>
                    <div class="widget-log">
                        > Querying global network...<br>
                        > 4,821 suppliers found.<br>
                        > Filtering by category...
                    </div>
                    <div class="widget-data">
                        <span class="w-val">2.4s</span><span class="w-lbl">Query Time</span>
                    </div>
                </div>

                <div class="agent-widget">
                    <div class="widget-header">
                        <span class="widget-title">Compliance Agent</span>
                        <span class="widget-status">RUNNING</span>
                    </div>
                    <div class="widget-log">
                        > Verifying SOC2 / ISO...<br>
                        > Rejecting 3,102 suppliers.<br>
                        > Cross-referencing ESG...
                    </div>
                    <div class="widget-data">
                        <span class="w-val">Strict</span><span class="w-lbl">Parameter</span>
                    </div>
                </div>

                <div class="agent-widget">
                    <div class="widget-header">
                        <span class="widget-title">Logistics Agent</span>
                        <span class="widget-status">RUNNING</span>
                    </div>
                    <div class="widget-log">
                        > Origin constraints open.<br>
                        > Destination: LOS (Lagos).<br>
                        > Modeling DDP freight...
                    </div>
                    <div class="widget-data">
                        <span class="w-val">Active</span><span class="w-lbl">Routing</span>
                    </div>
                </div>

            </div>
        </div>

        <!-- THE CONTINUOUS APPLICATION ENVIRONMENT -->
        <div class="v1-app-environment">
            <div class="app-inner-glow"></div>
            
            <div class="commerce-matrix">
                <div class="matrix-header">
                    <div class="mh-title">Live Sourcing Matrix</div>
                    <div class="mh-status"><div class="mh-dot"></div> Processing 1,719 viable suppliers</div>
                </div>
                
                <div class="matrix-row">
                    <div class="mr-supplier">
                        <span class="mr-name">Herman Miller B2B</span>
                        <span class="mr-type">Direct Manufacturer • Michigan, USA</span>
                    </div>
                    <div class="mr-data">
                        <span class="mrd-val">94,200</span>
                        <span class="mrd-lbl">YTD Volume</span>
                    </div>
                    <div class="mr-data">
                        <span class="mrd-val">SOC2, ISO 9001</span>
                        <span class="mrd-lbl">Compliance</span>
                    </div>
                    <div class="mr-badge green">Verified Match</div>
                </div>

                <div class="matrix-row">
                    <div class="mr-supplier">
                        <span class="mr-name">Steelcase Global</span>
                        <span class="mr-type">Global Distributor • Germany</span>
                    </div>
                    <div class="mr-data">
                        <span class="mrd-val">12,400</span>
                        <span class="mrd-lbl">YTD Volume</span>
                    </div>
                    <div class="mr-data">
                        <span class="mrd-val">ISO 9001</span>
                        <span class="mrd-lbl">Compliance</span>
                    </div>
                    <div class="mr-badge blue">Evaluating</div>
                </div>
                
                <div class="matrix-row">
                    <div class="mr-supplier">
                        <span class="mr-name">Knoll Corporate</span>
                        <span class="mr-type">Distributor • UK</span>
                    </div>
                    <div class="mr-data">
                        <span class="mrd-val">8,100</span>
                        <span class="mrd-lbl">YTD Volume</span>
                    </div>
                    <div class="mr-data">
                        <span class="mrd-val">Pending Audits</span>
                        <span class="mrd-lbl">Compliance</span>
                    </div>
                    <div class="mr-badge">Processing</div>
                </div>

                <div class="matrix-row" style="opacity:0.4;">
                    <div class="mr-supplier">
                        <span class="mr-name">Generic Wholesale Ltd</span>
                        <span class="mr-type">Broker • Unknown</span>
                    </div>
                    <div class="mr-data">
                        <span class="mrd-val">0</span>
                        <span class="mrd-lbl">YTD Volume</span>
                    </div>
                    <div class="mr-data">
                        <span class="mrd-val" style="color:#ef4444;">Failed SOC2</span>
                        <span class="mrd-lbl">Compliance</span>
                    </div>
                    <div class="mr-badge" style="color:#ef4444; border:1px solid rgba(239,68,68,0.2);">Rejected</div>
                </div>
                
            </div>
            
        </div>

    </div>
    """
    
    main.append(bs4.BeautifulSoup(hero_html, 'html.parser'))
    main.append(footer)

    with open('agentic-commerce.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    print("Seamless Hero implementation complete.")

if __name__ == '__main__':
    run()
