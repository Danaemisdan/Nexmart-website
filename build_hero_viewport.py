import bs4

def run():
    with open('agentic-commerce.html', 'r', encoding='utf-8') as f:
        soup = bs4.BeautifulSoup(f, 'html.parser')
    
    # ----------------------------------------------------
    # CSS for the Dribbble-Quality Hero Viewport
    # ----------------------------------------------------
    style_str = """
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;700&display=swap');

    :root {
        --nx-bg: #000000;
        --nx-panel: #0a0a0a;
        --nx-panel-light: #171717;
        --nx-border: rgba(255,255,255,0.08);
        --nx-text: #ffffff;
        --nx-text-dim: #a3a3a3;
        --nx-accent: #2563eb;
        --nx-accent-glow: rgba(37, 99, 235, 0.4);
        --nx-success: #10b981;
    }

    body { background: var(--nx-bg); color: var(--nx-text); font-family: 'Inter', sans-serif; margin: 0; padding: 0; overflow-x: hidden; }

    /* Scene 1: The Hero Viewport */
    .hero-viewport {
        min-height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 120px 24px 80px 24px;
        background: radial-gradient(circle at top center, #111827 0%, #000000 60%);
        position: relative;
    }

    .hero-title {
        font-size: 5rem;
        font-weight: 800;
        letter-spacing: -0.04em;
        line-height: 1;
        text-align: center;
        margin-bottom: 24px;
        background: linear-gradient(180deg, #FFFFFF 0%, #a3a3a3 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        z-index: 10;
    }

    .hero-subtitle {
        font-size: 1.25rem;
        color: var(--nx-text-dim);
        text-align: center;
        max-width: 600px;
        margin-bottom: 64px;
        font-weight: 400;
        z-index: 10;
    }

    /* The Application UI */
    .app-window {
        width: 100%;
        max-width: 1200px;
        background: var(--nx-panel);
        border: 1px solid var(--nx-border);
        border-radius: 16px;
        box-shadow: 0 40px 100px rgba(0,0,0,0.8), 0 0 0 1px rgba(255,255,255,0.02) inset;
        overflow: hidden;
        display: flex;
        flex-direction: column;
        z-index: 10;
    }

    .app-header {
        height: 48px;
        background: var(--nx-panel-light);
        border-bottom: 1px solid var(--nx-border);
        display: flex;
        align-items: center;
        padding: 0 20px;
        gap: 8px;
    }
    
    .dot { width: 12px; height: 12px; border-radius: 50%; }
    .dot.r { background: #ff5f56; } .dot.y { background: #ffbd2e; } .dot.g { background: #27c93f; }
    
    .app-title { margin-left: auto; margin-right: auto; font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--nx-text-dim); letter-spacing: 0.1em; }

    .app-body {
        padding: 40px;
        display: flex;
        flex-direction: column;
        gap: 24px;
    }

    /* Command Input */
    .command-bar {
        background: var(--nx-panel-light);
        border: 1px solid var(--nx-border);
        border-radius: 12px;
        padding: 20px 24px;
        display: flex;
        align-items: center;
        gap: 16px;
        box-shadow: 0 8px 30px rgba(0,0,0,0.5);
    }

    .cmd-icon {
        width: 24px;
        height: 24px;
        color: var(--nx-accent);
    }

    .cmd-text {
        font-size: 1.5rem;
        font-weight: 500;
        color: var(--nx-text);
        position: relative;
    }

    /* Animations */
    @keyframes typing { from { width: 0; } to { width: 100%; } }
    @keyframes blink { 50% { opacity: 0; } }
    @keyframes slide-down { from { opacity: 0; transform: translateY(-10px); } to { opacity: 1; transform: translateY(0); } }
    @keyframes pulse-glow { 0%, 100% { box-shadow: 0 0 15px rgba(16, 185, 129, 0); } 50% { box-shadow: 0 0 15px rgba(16, 185, 129, 0.4); } }

    .typewriter-text {
        display: inline-block;
        overflow: hidden;
        white-space: nowrap;
        width: 0;
        animation: typing 2.5s steps(50, end) forwards 0.5s;
    }
    
    .cursor {
        display: inline-block;
        width: 2px;
        height: 1.5rem;
        background: var(--nx-accent);
        vertical-align: text-bottom;
        margin-left: 4px;
        animation: blink 1s step-end infinite;
    }

    /* Agent Threads */
    .threads-container {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 16px;
        opacity: 0;
        animation: slide-down 0.5s ease forwards 3.5s;
    }

    .thread-card {
        background: var(--nx-panel-light);
        border: 1px solid var(--nx-border);
        border-radius: 12px;
        padding: 20px;
        display: flex;
        flex-direction: column;
        gap: 12px;
    }

    .thread-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .thread-name { font-size: 14px; font-weight: 600; }
    
    .thread-status {
        font-family: 'JetBrains Mono', monospace;
        font-size: 10px;
        font-weight: 700;
        padding: 4px 8px;
        border-radius: 4px;
        letter-spacing: 0.05em;
    }
    
    .status-running {
        background: rgba(16, 185, 129, 0.1);
        color: var(--nx-success);
        border: 1px solid rgba(16, 185, 129, 0.2);
        animation: pulse-glow 2s infinite;
    }
    
    .thread-log {
        font-family: 'JetBrains Mono', monospace;
        font-size: 11px;
        color: var(--nx-text-dim);
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }

    .progress-track {
        height: 4px;
        background: rgba(255,255,255,0.05);
        border-radius: 2px;
        overflow: hidden;
    }
    
    .progress-fill {
        height: 100%;
        background: var(--nx-success);
        width: 0%;
        border-radius: 2px;
        transition: width 0.1s linear;
    }
    
    @keyframes load-1 { from { width: 0%; } to { width: 85%; } }
    @keyframes load-2 { from { width: 0%; } to { width: 40%; } }
    @keyframes load-3 { from { width: 0%; } to { width: 10%; } }
    
    .fill-1 { animation: load-1 4s ease-out forwards 3.8s; }
    .fill-2 { animation: load-2 3s ease-out forwards 4.0s; }
    .fill-3 { animation: load-3 5s ease-out forwards 4.2s; }

    @media (max-width: 991px) {
        .hero-title { font-size: 3.5rem; }
        .threads-container { grid-template-columns: 1fr; }
        .cmd-text { font-size: 1.1rem; }
    }
    """

    for s in soup.head.find_all('style'):
        if s.string and ('Hero Specific UI Variables' in s.string or 'Product UI Framework' in s.string or '--nx-bg' in s.string or '--saas-bg' in s.string):
            s.decompose()
            
    style = soup.new_tag('style')
    style.string = style_str
    soup.head.append(style)

    main = soup.find('main')
    footer = main.find(class_='footer_component')
    main.clear()

    # ----------------------------------------------------
    # SCENE 1: THE COMMAND (Hero Viewport)
    # ----------------------------------------------------
    hero_html = """
    <section class="hero-viewport">
        <!-- Minimal, powerful typography -->
        <h1 class="hero-title">Command the economy.</h1>
        <p class="hero-subtitle">Deploy intelligent agents to discover, negotiate, and route global procurement autonomously in real time.</p>
        
        <!-- The UI Hero -->
        <div class="app-window">
            <div class="app-header">
                <div class="dot r"></div><div class="dot y"></div><div class="dot g"></div>
                <div class="app-title">NEXMART ORCHESTRATOR</div>
                <div style="width:42px;"></div><!-- Balance -->
            </div>
            
            <div class="app-body">
                <!-- Command Input -->
                <div class="command-bar">
                    <svg class="cmd-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
                    <div class="cmd-text">
                        <span class="typewriter-text">Procure 500 ergonomic office chairs for Lagos.</span><span class="cursor"></span>
                    </div>
                </div>
                
                <!-- Autonomous Execution Threads -->
                <div class="threads-container">
                    
                    <div class="thread-card">
                        <div class="thread-header">
                            <span class="thread-name">Global Discovery</span>
                            <span class="thread-status status-running">RUNNING</span>
                        </div>
                        <div class="progress-track"><div class="progress-fill fill-1"></div></div>
                        <div class="thread-log">> Scanning 4,821 supplier profiles...</div>
                    </div>
                    
                    <div class="thread-card">
                        <div class="thread-header">
                            <span class="thread-name">Compliance Audit</span>
                            <span class="thread-status status-running">RUNNING</span>
                        </div>
                        <div class="progress-track"><div class="progress-fill fill-2"></div></div>
                        <div class="thread-log">> Verifying SOC2 certificates...</div>
                    </div>
                    
                    <div class="thread-card">
                        <div class="thread-header">
                            <span class="thread-name">Logistics Routing</span>
                            <span class="thread-status status-running">RUNNING</span>
                        </div>
                        <div class="progress-track"><div class="progress-fill fill-3"></div></div>
                        <div class="thread-log">> Mapping origin to LOS via sea freight...</div>
                    </div>
                    
                </div>
            </div>
        </div>
    </section>
    """
    main.append(bs4.BeautifulSoup(hero_html, 'html.parser'))
    main.append(footer)

    with open('agentic-commerce.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    print("Hero viewport implementation complete.")

if __name__ == '__main__':
    run()
