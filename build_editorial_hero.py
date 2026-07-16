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

    /* 
      VIEWPORT 1: THE COMMAND 
      Pristine white, massive typography, floating premium command interface.
    */
    .v1-editorial-hero {
        position: relative;
        width: 100%;
        height: 100vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;
        padding-top: 18vh;
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
        margin: 0 auto 64px auto;
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
        z-index: 3;
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

    /* 
      THE EMERGENCE 
      The application peeking from below the fold.
    */
    .v1-app-peek {
        position: absolute;
        bottom: -30vh; /* Hidden below fold, peeking up */
        left: 50%;
        transform: translateX(-50%);
        width: 90vw;
        max-width: 1400px;
        height: 60vh;
        background: #0b1120;
        border-radius: 24px 24px 0 0;
        border: 1px solid rgba(255,255,255,0.05);
        border-bottom: none;
        box-shadow: 0 -40px 100px rgba(0,0,0,0.15), 0 0 0 1px rgba(255,255,255,0.02) inset;
        z-index: 1;
        display: flex;
        flex-direction: column;
    }

    .app-peek-header {
        height: 56px;
        border-bottom: 1px solid rgba(255,255,255,0.05);
        display: flex;
        align-items: center;
        padding: 0 24px;
        gap: 12px;
    }

    .peek-dot { width: 12px; height: 12px; border-radius: 50%; background: #334155; }
    .peek-title { margin: 0 auto; font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #64748b; letter-spacing: 0.2em; text-transform: uppercase; }

    /* Cinematic Lighting / Atmospheric depth */
    .ambient-glow {
        position: absolute;
        bottom: -20vh;
        left: 50%;
        transform: translateX(-50%);
        width: 60vw;
        height: 40vh;
        background: radial-gradient(ellipse at top, rgba(0, 112, 243, 0.08) 0%, transparent 70%);
        pointer-events: none;
        z-index: 0;
    }

    @media (max-width: 991px) {
        .v1-title { font-size: 4rem; }
        .v1-command-module { width: 90%; }
        .cmd-input { font-size: 1rem; }
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
            <div class="cmd-badge">Awaiting Intent</div>
        </div>

        <!-- Atmospheric Depth -->
        <div class="ambient-glow"></div>

        <!-- The Emergence: Dark software creeping up from the bottom -->
        <div class="v1-app-peek">
            <div class="app-peek-header">
                <div class="peek-dot"></div><div class="peek-dot"></div><div class="peek-dot"></div>
                <div class="peek-title">Nexmart Logistics & Procurement Engine</div>
                <div style="width:60px;"></div>
            </div>
            <!-- The rest of the app is hidden below the fold, creating anticipation -->
        </div>

    </section>
    """
    
    main.append(bs4.BeautifulSoup(hero_html, 'html.parser'))
    main.append(footer)

    with open('agentic-commerce.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    print("Editorial Hero viewport implementation complete.")

if __name__ == '__main__':
    run()
