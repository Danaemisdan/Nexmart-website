import bs4

def run():
    with open('agentic-commerce.html', 'r', encoding='utf-8') as f:
        soup = bs4.BeautifulSoup(f, 'html.parser')
    
    style_str = """
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap');

    :root {
        /* The New Premium Cohesive Navy/Slate Color System */
        --warm-white: #FBFCFD;       /* Clean but slightly warm */
        --soft-silver: #F1F4F9;      /* Subtle silver-blue */
        --blue-slate: #94A3B8;       /* Desaturated slate blue */
        --dark-steel: #334155;       /* Bridging tone */
        --graphite-blue: #1E293B;    /* Lighter navy */
        --midnight-navy: #0F172A;    /* Deep premium navy (replaces harsh black) */
        --mist-blue: #E2E8F0;        /* Desaturated atmospheric light blue */
        
        /* Subtle Studio Lighting */
        --ambient-blue: rgba(14, 165, 233, 0.15); /* Soft azure light */
        --ambient-glow: rgba(56, 189, 248, 0.1); 
        --success-core: #10B981;
    }

    body, html {
        margin: 0;
        padding: 0;
        width: 100%;
        font-family: 'Inter', -apple-system, sans-serif;
        background: var(--warm-white);
        color: var(--midnight-navy);
        overflow-x: hidden;
    }

    /* Infinite Architectural Grid Background */
    .bg-grid {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background-image: 
            linear-gradient(to right, rgba(15, 23, 42, 0.03) 1px, transparent 1px),
            linear-gradient(to bottom, rgba(15, 23, 42, 0.03) 1px, transparent 1px);
        background-size: 100px 100px;
        z-index: 0;
        pointer-events: none;
    }

    /* SEAMLESS FLOW CONTAINER */
    .seamless-page-wrapper {
        position: relative;
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        /* Cohesive transition: Warm White -> Soft Silver -> Mist Blue -> Midnight Navy */
        background: linear-gradient(180deg, 
            var(--warm-white) 0%, 
            var(--soft-silver) 40vh, 
            var(--mist-blue) 75vh,
            var(--midnight-navy) 100%);
        z-index: 1;
    }

    /* THE TYPOGRAPHY */
    .v1-typography {
        text-align: center;
        max-width: 1000px;
        padding: 18vh 24px 0 24px;
        z-index: 20;
    }

    .v1-title {
        font-size: 6.5rem;
        font-weight: 700;
        letter-spacing: -0.05em;
        line-height: 1.05;
        color: var(--midnight-navy);
        margin: 0 0 24px 0;
        text-shadow: 0 4px 20px rgba(15, 23, 42, 0.05);
    }

    .v1-subtitle {
        font-size: 1.5rem;
        font-weight: 400;
        color: var(--dark-steel);
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
        z-index: 30; 
        margin-bottom: -180px; 
    }

    /* Floating Command Interface - Refined Glass */
    .v1-command-module {
        width: 100%;
        max-width: 720px;
        background: rgba(251, 252, 253, 0.7);
        backdrop-filter: blur(40px) saturate(150%);
        -webkit-backdrop-filter: blur(40px) saturate(150%);
        border: 1px solid rgba(255,255,255,1);
        border-radius: 100px;
        padding: 16px 24px;
        display: flex;
        align-items: center;
        gap: 20px;
        box-shadow: 
            0 30px 60px rgba(15, 23, 42, 0.06), 
            0 10px 20px rgba(15, 23, 42, 0.02),
            0 0 0 1px rgba(255,255,255,0.8);
        z-index: 35;
        margin-bottom: 56px;
    }

    .cmd-icon-box {
        width: 48px;
        height: 48px;
        border-radius: 50%;
        background: var(--midnight-navy);
        display: flex;
        align-items: center;
        justify-content: center;
        color: var(--warm-white);
        flex-shrink: 0;
        box-shadow: 0 10px 20px rgba(15, 23, 42, 0.2);
    }

    .cmd-input {
        font-size: 1.25rem;
        font-weight: 500;
        color: var(--midnight-navy);
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
        background: #0EA5E9; /* Azure cursor */
        margin-left: 4px;
        animation: blink 1s step-end infinite;
    }

    @keyframes typing { from { width: 0; } to { width: 100%; } }
    @keyframes blink { 50% { opacity: 0; } }

    /* The Agent Widgets (Luxury Mist Glass) */
    .agent-widgets-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 24px;
        width: 100%;
        padding: 0 24px;
    }

    .agent-widget {
        background: rgba(241, 244, 249, 0.85); /* Silver mist glass */
        backdrop-filter: blur(40px);
        -webkit-backdrop-filter: blur(40px);
        border: 1px solid rgba(255,255,255,0.8);
        border-radius: 20px;
        padding: 28px;
        box-shadow: 
            0 40px 80px rgba(15, 23, 42, 0.08),
            0 10px 30px rgba(15, 23, 42, 0.04),
            inset 0 1px 0 rgba(255,255,255,1);
        opacity: 0;
        transform: translateY(20px);
        animation: float-up 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }
    
    .agent-widget:nth-child(1) { animation-delay: 3.5s; }
    .agent-widget:nth-child(2) { animation-delay: 3.7s; }
    .agent-widget:nth-child(3) { animation-delay: 3.9s; }

    @keyframes float-up { to { opacity: 1; transform: translateY(0); } }

    .widget-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; }
    .widget-title { font-size: 13px; font-weight: 600; color: var(--midnight-navy); }
    
    /* Elegant Status Badge */
    .widget-status { 
        font-family: 'JetBrains Mono', monospace; 
        font-size: 10px; 
        font-weight: 700; 
        color: var(--success-core); 
        background: rgba(16,185,129,0.08); 
        padding: 4px 8px; 
        border-radius: 6px; 
        border: 1px solid rgba(16,185,129,0.15);
        box-shadow: 0 0 10px rgba(16,185,129,0.1);
    }
    
    .widget-log { font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--dark-steel); line-height: 1.6; margin-bottom: 20px; }
    
    .widget-data { display: flex; align-items: center; gap: 8px; padding-top: 16px; border-top: 1px solid rgba(15, 23, 42, 0.06); }
    .w-val { font-size: 14px; font-weight: 600; color: var(--midnight-navy); }
    .w-lbl { font-size: 12px; color: var(--blue-slate); }

    /* THE CONTINUOUS NAVY ENVIRONMENT */
    .v1-app-environment {
        width: 100vw; 
        max-width: 1600px;
        /* Studio Lighting Gradient: Deep Navy illuminated softly by Azure */
        background: radial-gradient(ellipse at top center, var(--graphite-blue) 0%, var(--midnight-navy) 80%);
        border-radius: 32px 32px 0 0;
        border: 1px solid rgba(255,255,255,0.06);
        border-bottom: none;
        box-shadow: 
            0 -40px 100px rgba(15, 23, 42, 0.3), 
            0 0 0 1px rgba(255,255,255,0.04) inset;
        z-index: 20;
        padding-top: 240px; 
        padding-bottom: 300px; 
        position: relative;
        /* Very subtle fade to seamlessly dissolve into the next section */
        -webkit-mask-image: linear-gradient(to bottom, black 0%, black 85%, transparent 100%);
        mask-image: linear-gradient(to bottom, black 0%, black 85%, transparent 100%);
    }

    /* Ambient Blue Studio Light Reflections */
    .ambient-reflection-left {
        position: absolute;
        top: 0;
        left: 0;
        width: 400px;
        height: 600px;
        background: radial-gradient(ellipse at top left, var(--ambient-blue) 0%, transparent 70%);
        pointer-events: none;
    }
    
    .ambient-reflection-center {
        position: absolute;
        top: -100px;
        left: 50%;
        transform: translateX(-50%);
        width: 800px;
        height: 400px;
        background: radial-gradient(ellipse at top center, var(--ambient-glow) 0%, transparent 60%);
        pointer-events: none;
    }

    /* Infinite App Grid inside Workspace (subtle steel) */
    .app-grid {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            linear-gradient(to right, rgba(255,255,255,0.02) 1px, transparent 1px),
            linear-gradient(to bottom, rgba(255,255,255,0.02) 1px, transparent 1px);
        background-size: 80px 80px;
        pointer-events: none;
    }

    /* Live Commerce Table - Premium Slate Panels */
    .commerce-matrix {
        width: 90%;
        max-width: 1200px;
        margin: 0 auto;
        display: flex;
        flex-direction: column;
        gap: 16px;
        position: relative;
        z-index: 25;
    }
    
    .matrix-header {
        display: flex;
        justify-content: space-between;
        align-items: flex-end;
        padding: 0 0 16px 0;
        border-bottom: 1px solid rgba(255,255,255,0.06);
        margin-bottom: 16px;
    }
    
    .mh-title { font-size: 20px; font-weight: 600; color: var(--warm-white); }
    .mh-status { font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--blue-slate); display: flex; align-items: center; gap: 8px; text-transform: uppercase; letter-spacing: 0.1em; }
    .mh-dot { width: 6px; height: 6px; background: #0EA5E9; border-radius: 50%; box-shadow: 0 0 12px #0EA5E9; }

    .matrix-row {
        background: rgba(255,255,255,0.02);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.04);
        border-radius: 16px;
        padding: 24px 32px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), background 0.4s, border-color 0.4s;
        box-shadow: 0 10px 30px rgba(15,23,42,0.2);
    }
    
    .matrix-row:hover {
        background: rgba(255,255,255,0.04);
        border-color: rgba(255,255,255,0.08);
        transform: translateY(-4px) scale(1.01);
    }
    
    .mr-supplier { display: flex; flex-direction: column; gap: 6px; width: 30%; }
    .mr-name { font-size: 16px; font-weight: 600; color: var(--warm-white); }
    .mr-type { font-size: 13px; color: var(--blue-slate); }
    
    .mr-data { display: flex; flex-direction: column; gap: 6px; width: 20%; }
    .mrd-val { font-family: 'JetBrains Mono', monospace; font-size: 14px; color: var(--mist-blue); font-weight: 500; }
    .mrd-lbl { font-size: 11px; color: var(--blue-slate); text-transform: uppercase; letter-spacing: 0.1em; }
    
    .mr-badge { padding: 8px 16px; border-radius: 100px; font-size: 12px; font-weight: 600; background: rgba(255,255,255,0.03); color: var(--warm-white); border: 1px solid rgba(255,255,255,0.08); }
    .mr-badge.green { 
        background: rgba(16,185,129,0.1); 
        color: var(--success-core); 
        border: 1px solid rgba(16,185,129,0.25); 
        box-shadow: 0 0 20px rgba(16,185,129,0.08);
    }

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
        if s.string and ('Hero Specific UI Variables' in s.string or 'Product UI Framework' in s.string or '--pure-white' in s.string or '--warm-white' in s.string):
            s.decompose()
            
    style = soup.new_tag('style')
    style.string = style_str
    soup.head.append(style)

    main = soup.find('main')
    footer = main.find(class_='footer_component')
    main.clear()

    hero_html = """
    <!-- Infinite Architectural Grid Background -->
    <div class="bg-grid"></div>

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

            <!-- Agent Widgets (Premium Mist Glass) -->
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

        <!-- THE CONTINUOUS NAVY ENVIRONMENT -->
        <div class="v1-app-environment">
            <!-- Studio Lighting Reflections -->
            <div class="ambient-reflection-left"></div>
            <div class="ambient-reflection-center"></div>
            
            <!-- Structural Grid -->
            <div class="app-grid"></div>
            
            <!-- Live Commerce Matrix -->
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
                    <div class="mr-badge">Evaluating...</div>
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
                    <div class="mr-badge">Processing...</div>
                </div>
                
                <!-- The mask-image in CSS makes the rows smoothly fade away into the Midnight Navy background -->
            </div>
            
        </div>

    </div>
    """
    
    main.append(bs4.BeautifulSoup(hero_html, 'html.parser'))
    main.append(footer)

    with open('agentic-commerce.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    print("Navy/Slate premium color polish complete.")

if __name__ == '__main__':
    run()
