import bs4

def run():
    with open('agentic-commerce.html', 'r', encoding='utf-8') as f:
        soup = bs4.BeautifulSoup(f, 'html.parser')
    
    style_str = """
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap');

    :root {
        --pure-white: #ffffff;
        --off-white: #fafafa;
        --slate-900: #0f172a;
        --slate-800: #1e293b;
        --slate-400: #94a3b8;
        --slate-200: #e2e8f0;
        --accent-blue: #0070f3;
        --success-green: #10b981;
    }

    body, html {
        margin: 0;
        padding: 0;
        width: 100%;
        height: 100%;
        font-family: 'Inter', -apple-system, sans-serif;
        background: var(--pure-white);
        color: var(--slate-900);
        overflow-x: hidden;
    }

    /* VIEWPORT 1: THE COMMAND */
    .v1-editorial-hero {
        position: relative;
        width: 100%;
        height: 100vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;
        padding-top: 14vh;
        overflow: hidden;
        background: var(--pure-white);
        z-index: 10;
    }

    .v1-typography {
        text-align: center;
        max-width: 1000px;
        padding: 0 24px;
        z-index: 2;
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

    /* Floating Command Interface */
    .v1-command-module {
        position: relative;
        width: 100%;
        max-width: 720px;
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(0, 0, 0, 0.05);
        border-radius: 100px;
        padding: 16px 24px;
        display: flex;
        align-items: center;
        gap: 20px;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.04), 0 1px 3px rgba(0,0,0,0.02);
        z-index: 10;
        transform: translateY(20px);
        opacity: 0;
        animation: float-up 1s cubic-bezier(0.16, 1, 0.3, 1) forwards 0.5s;
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

    @keyframes typing { from { width: 0; } to { width: 100%; } }
    @keyframes blink { 50% { opacity: 0; } }
    @keyframes float-up { to { transform: translateY(0); opacity: 1; } }

    .typewriter-text {
        display: inline-block;
        overflow: hidden;
        white-space: nowrap;
        width: 0;
        animation: typing 2.5s steps(40, end) forwards 1.5s;
    }
    
    .cursor {
        display: inline-block;
        width: 2px;
        height: 1.5rem;
        background: var(--accent-blue);
        margin-left: 4px;
        animation: blink 1s step-end infinite;
    }

    .cmd-badge {
        font-family: 'JetBrains Mono', monospace;
        font-size: 10px;
        font-weight: 600;
        letter-spacing: 0.1em;
        padding: 6px 12px;
        border-radius: 100px;
        background: var(--slate-100);
        color: var(--slate-400);
        text-transform: uppercase;
        border: 1px solid var(--slate-200);
    }

    /* THE EMERGENCE: The application peeking from below the fold */
    .v1-app-peek-container {
        position: absolute;
        bottom: 0; /* Align perfectly to the bottom of the viewport */
        left: 50%;
        transform: translateX(-50%);
        width: 95vw;
        max-width: 1400px;
        height: 35vh; /* Only the top 35% is visible */
        z-index: 1;
    }

    /* The Main App Window */
    .v1-main-app {
        position: absolute;
        top: 60px; /* Leave room for floating panels to escape */
        left: 0;
        width: 100%;
        height: 100vh; /* It extends way down off screen */
        background: #09090b; /* Deep premium black */
        border-radius: 24px 24px 0 0;
        border: 1px solid rgba(255,255,255,0.1);
        border-bottom: none;
        box-shadow: 0 -40px 100px rgba(0,0,0,0.3), 0 0 0 1px rgba(255,255,255,0.02) inset;
        display: flex;
        flex-direction: column;
        overflow: hidden;
    }

    .app-header-lux {
        height: 48px;
        background: rgba(255,255,255,0.02);
        border-bottom: 1px solid rgba(255,255,255,0.08);
        display: flex;
        align-items: center;
        padding: 0 24px;
        backdrop-filter: blur(10px);
    }

    .lux-dot { width: 10px; height: 10px; border-radius: 50%; background: #334155; margin-right: 8px; }
    
    /* The active commerce data inside the main window */
    .app-body-lux {
        padding: 24px 40px;
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        gap: 24px;
        background: radial-gradient(circle at top, rgba(0, 112, 243, 0.05) 0%, transparent 60%);
    }

    .data-row {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 16px 0;
        border-bottom: 1px solid rgba(255,255,255,0.05);
    }
    .data-label { color: #a1a1aa; font-size: 13px; font-weight: 500; }
    .data-value { color: #fff; font-family: 'JetBrains Mono', monospace; font-size: 13px; }
    .data-value.green { color: #10b981; }
    .data-value.blue { color: #3b82f6; }

    /* Floating Panels Escaping the Bounds */
    .floating-panel {
        position: absolute;
        background: rgba(24, 24, 27, 0.85); /* Semi-transparent zinc */
        backdrop-filter: blur(24px);
        -webkit-backdrop-filter: blur(24px);
        border: 1px solid rgba(255,255,255,0.15);
        border-radius: 16px;
        box-shadow: 0 30px 60px rgba(0,0,0,0.5), 0 0 0 1px rgba(255,255,255,0.05) inset;
        color: #fff;
        z-index: 20;
    }

    /* Panel 1: Live Logistics Route (Escaping Top Left) */
    .panel-logistics {
        top: 10px;
        left: 40px;
        width: 280px;
        padding: 20px;
        animation: float-hover 6s ease-in-out infinite;
    }
    .panel-header { font-size: 10px; text-transform: uppercase; letter-spacing: 0.1em; color: #71717a; margin-bottom: 12px; font-weight: 700; }
    .route-visual { display: flex; align-items: center; gap: 8px; margin-top: 12px; }
    .route-node { width: 8px; height: 8px; border-radius: 50%; background: #3b82f6; box-shadow: 0 0 10px #3b82f6; }
    .route-line { height: 2px; flex-grow: 1; background: linear-gradient(90deg, #3b82f6, #10b981); position: relative; overflow: hidden; }
    .route-node.end { background: #10b981; box-shadow: 0 0 10px #10b981; }
    
    @keyframes route-scan { 0% { left: -100%; } 100% { left: 100%; } }
    .route-line::after { content: ''; position: absolute; top:0; left:0; width: 50%; height: 100%; background: #fff; opacity: 0.5; filter: blur(2px); animation: route-scan 2s linear infinite; }

    /* Panel 2: Live Purchase Order updating (Escaping Top Right) */
    .panel-po {
        top: -10px;
        right: 80px;
        width: 320px;
        padding: 24px;
        background: rgba(9, 9, 11, 0.95);
        border: 1px solid rgba(16, 185, 129, 0.3);
        box-shadow: 0 40px 80px rgba(0,0,0,0.6), 0 0 40px rgba(16, 185, 129, 0.1);
        animation: float-hover-offset 7s ease-in-out infinite;
    }
    
    @keyframes float-hover { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-8px); } }
    @keyframes float-hover-offset { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(6px); } }

    @keyframes live-update { 0%, 100% { color: #fff; text-shadow: none; } 50% { color: #10b981; text-shadow: 0 0 15px #10b981; } }
    .live-value { font-family: 'JetBrains Mono', monospace; font-size: 24px; font-weight: 700; margin-top: 8px; animation: live-update 3s infinite; }

    /* Atmospheric Lighting behind the app */
    .ambient-glow-back {
        position: absolute;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 80vw;
        height: 40vh;
        background: radial-gradient(ellipse at bottom, rgba(59, 130, 246, 0.15) 0%, transparent 60%);
        pointer-events: none;
        z-index: 0;
    }

    @media (max-width: 991px) {
        .v1-title { font-size: 3.5rem; }
        .v1-command-module { width: 90%; }
        .cmd-input { font-size: 1rem; }
        .floating-panel { display: none; /* Hide complex floating UI on mobile to keep it clean */ }
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
    <section class="v1-editorial-hero">
        
        <div class="v1-typography">
            <h1 class="v1-title">Command the global economy.</h1>
            <p class="v1-subtitle">A single intent orchestrates thousands of autonomous procurement decisions across the world in real time.</p>
        </div>

        <!-- Premium Floating Interface -->
        <div class="v1-command-module">
            <div class="cmd-icon-box">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 16 16 12 12 8"></polyline><line x1="8" y1="12" x2="16" y2="12"></line></svg>
            </div>
            <div class="cmd-input">
                <span class="typewriter-text">Procure 500 chairs for Lagos.</span><span class="cursor"></span>
            </div>
            <div class="cmd-badge">Executing Intent</div>
        </div>

        <!-- Atmospheric Depth behind the app -->
        <div class="ambient-glow-back"></div>

        <!-- The Emergence: Layered, floating, active UI -->
        <div class="v1-app-peek-container">
            
            <!-- Main Application Window -->
            <div class="v1-main-app">
                <div class="app-header-lux">
                    <div class="lux-dot" style="background:#ef4444;"></div>
                    <div class="lux-dot" style="background:#f59e0b;"></div>
                    <div class="lux-dot" style="background:#10b981;"></div>
                    <div style="margin-left:16px; color:#52525b; font-size:12px; font-weight:500;">Nexmart Global Sourcing Matrix</div>
                </div>
                
                <div class="app-body-lux">
                    <!-- Beautiful active commerce data -->
                    <div>
                        <div class="panel-header">Supplier Volume</div>
                        <div class="data-row"><span class="data-label">Herman Miller B2B</span><span class="data-value blue">94,200 units</span></div>
                        <div class="data-row"><span class="data-label">Steelcase Global</span><span class="data-value">12,400 units</span></div>
                        <div class="data-row"><span class="data-label">Knoll Distribution</span><span class="data-value">8,100 units</span></div>
                    </div>
                    <div>
                        <div class="panel-header">Live Compliance Check</div>
                        <div class="data-row"><span class="data-label">SOC2 Certification</span><span class="data-value green">Verified</span></div>
                        <div class="data-row"><span class="data-label">ISO 9001</span><span class="data-value green">Verified</span></div>
                        <div class="data-row"><span class="data-label">Carbon Footprint</span><span class="data-value blue">-12% YTD</span></div>
                    </div>
                    <div>
                        <div class="panel-header">Market Equilibrium</div>
                        <div class="data-row"><span class="data-label">Average Unit Cost</span><span class="data-value">$1,240.00</span></div>
                        <div class="data-row"><span class="data-label">Negotiated Target</span><span class="data-value green">$1,050.00</span></div>
                        <div class="data-row"><span class="data-label">Fulfillment Risk</span><span class="data-value">Low (0.04)</span></div>
                    </div>
                </div>
            </div>

            <!-- Floating Panel 1: Route Optimization (Escaping Bounds) -->
            <div class="floating-panel panel-logistics">
                <div class="panel-header">Autonomous Reroute: Active</div>
                <div style="font-size:14px; font-weight:500;">Port of Newark -> Lagos</div>
                <div style="font-size:11px; color:#a1a1aa; margin-top:4px;">Avoiding Atlantic weather system</div>
                <div class="route-visual">
                    <div class="route-node"></div>
                    <div class="route-line"></div>
                    <div class="route-node end"></div>
                </div>
                <div style="display:flex; justify-content:space-between; margin-top:12px; font-size:11px; font-family:monospace; color:#3b82f6;">
                    <span>ETA -14 hrs</span>
                    <span>Optimized</span>
                </div>
            </div>

            <!-- Floating Panel 2: Live Purchase Order (Escaping Bounds) -->
            <div class="floating-panel panel-po">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <div class="panel-header" style="margin:0; color:#10b981;">Contract Approved</div>
                    <div style="width:24px; height:24px; border-radius:50%; background:rgba(16, 185, 129, 0.2); display:flex; align-items:center; justify-content:center;">
                        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg>
                    </div>
                </div>
                <div style="font-size:13px; color:#a1a1aa; margin-top:16px;">PO #NX-8842-A</div>
                <div style="font-size:15px; font-weight:600; margin-top:4px;">500x Ergonomic Chairs</div>
                
                <div style="height:1px; background:rgba(255,255,255,0.1); margin:16px 0;"></div>
                
                <div style="font-size:11px; text-transform:uppercase; letter-spacing:0.1em; color:#71717a;">Final Negotiated Capital</div>
                <div class="live-value">$525,000.00</div>
                <div style="font-size:12px; color:#10b981; margin-top:8px; font-family:monospace;">+ $75,000 Preserved vs Market</div>
            </div>

        </div>

    </section>
    """
    
    main.append(bs4.BeautifulSoup(hero_html, 'html.parser'))
    main.append(footer)

    with open('agentic-commerce.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    print("Redesigned Editorial Hero viewport implementation complete.")

if __name__ == '__main__':
    run()
