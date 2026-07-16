import bs4
import re

def run():
    with open('agentic-commerce.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    # We will replace the entire <style> block we injected previously with a new Royal Blue styled block.
    # The block we injected starts with @import url('https://fonts.googleapis.com/css2?family=Inter
    
    style_str = """
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap');

    :root {
        /* Royal Blue Environment Palette */
        --warm-white: #FFFFFF;
        --soft-blue: #EBF4FC;
        --royal-light: #5E9DFF;
        --royal-glow: #2A64D8;
        --royal-mid: #1B4DBB;
        --royal-base: #143D8D;
        --royal-deep: #0E2A66;
        --royal-abyss: #071638; /* For the very bottom / footer */
        
        /* Atmosphere & Lighting */
        --ambient-cyan: rgba(56, 189, 248, 0.25);
        --glow-core: rgba(42, 100, 216, 0.4);
        --success-core: #10B981;
    }

    body, html {
        margin: 0;
        padding: 0;
        width: 100%;
        font-family: 'Inter', -apple-system, sans-serif;
        background-color: var(--royal-abyss);
        /* 
           The Master Environment Gradient 
           White -> Soft Atmospheric Blue -> Royal Blue -> Royal Abyss 
        */
        background-image: linear-gradient(180deg, 
            var(--warm-white) 0vh, 
            var(--warm-white) 25vh,
            var(--soft-blue) 45vh, 
            var(--royal-base) 80vh,
            var(--royal-abyss) 110vh,
            var(--royal-abyss) 100%);
        background-attachment: fixed; 
        color: var(--warm-white);
        overflow-x: hidden;
    }

    /* Infinite Glowing World Grid */
    .bg-grid {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background-image: 
            linear-gradient(to right, rgba(94, 157, 255, 0.05) 1px, transparent 1px),
            linear-gradient(to bottom, rgba(94, 157, 255, 0.05) 1px, transparent 1px);
        background-size: 80px 80px;
        z-index: 0;
        pointer-events: none;
        -webkit-mask-image: linear-gradient(180deg, transparent 40%, black 60%, transparent 95%);
        mask-image: linear-gradient(180deg, transparent 40%, black 60%, transparent 95%);
    }

    .seamless-page-wrapper {
        position: relative;
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        z-index: 1;
    }

    /* THE TYPOGRAPHY - Kept pristine */
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
        color: #050d1f; /* Dark navy for contrast against white top */
        margin: 0 0 24px 0;
        text-shadow: 0 4px 30px rgba(20, 61, 141, 0.05);
    }

    .v1-subtitle {
        font-size: 1.5rem;
        font-weight: 400;
        color: #4a5c80;
        max-width: 600px;
        margin: 0 auto 56px auto;
        letter-spacing: -0.01em;
        line-height: 1.4;
    }

    /* THE BRIDGE */
    .v1-bridge-container {
        position: relative;
        width: 100%;
        max-width: 1100px;
        display: flex;
        flex-direction: column;
        align-items: center;
        z-index: 30; 
        margin-bottom: -150px; 
    }

    .v1-command-module {
        width: 100%;
        max-width: 720px;
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(40px) saturate(150%);
        -webkit-backdrop-filter: blur(40px) saturate(150%);
        border: 1px solid rgba(255,255,255,1);
        border-radius: 100px;
        padding: 16px 24px;
        display: flex;
        align-items: center;
        gap: 20px;
        box-shadow: 
            0 30px 80px rgba(14, 42, 102, 0.15), 
            0 10px 20px rgba(14, 42, 102, 0.05),
            0 0 0 1px rgba(255,255,255,0.8);
        z-index: 35;
        margin-bottom: 64px;
    }

    .cmd-icon-box {
        width: 48px;
        height: 48px;
        border-radius: 50%;
        background: #050d1f;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #ffffff;
        flex-shrink: 0;
        box-shadow: 0 10px 20px rgba(14, 42, 102, 0.3);
    }

    .cmd-input {
        font-size: 1.25rem;
        font-weight: 500;
        color: #050d1f;
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
        background: var(--royal-glow); 
        margin-left: 4px;
        animation: blink 1s step-end infinite;
    }

    @keyframes typing { from { width: 0; } to { width: 100%; } }
    @keyframes blink { 50% { opacity: 0; } }

    /* AGENT WIDGETS - Enhanced Polish */
    .agent-widgets-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 24px;
        width: 100%;
        padding: 0 24px;
    }

    .agent-widget {
        background: rgba(255, 255, 255, 0.9); 
        backdrop-filter: blur(40px) saturate(180%);
        -webkit-backdrop-filter: blur(40px) saturate(180%);
        border: 1px solid rgba(255,255,255,0.6);
        border-radius: 20px;
        padding: 28px;
        box-shadow: 
            0 40px 100px rgba(14, 42, 102, 0.15),
            0 10px 30px rgba(14, 42, 102, 0.08),
            inset 0 1px 0 rgba(255,255,255,1),
            inset 0 0 40px rgba(157, 196, 255, 0.1);
        opacity: 0;
        transform: translateY(20px);
        animation: float-up 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }
    
    .agent-widget:nth-child(1) { animation-delay: 3.5s; }
    .agent-widget:nth-child(2) { animation-delay: 3.7s; }
    .agent-widget:nth-child(3) { animation-delay: 3.9s; }

    @keyframes float-up { to { opacity: 1; transform: translateY(0); } }

    .widget-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; }
    .widget-title { font-size: 13px; font-weight: 600; color: #050d1f; }
    
    .widget-status { 
        font-family: 'JetBrains Mono', monospace; 
        font-size: 10px; 
        font-weight: 700; 
        color: var(--royal-glow); 
        background: rgba(42, 100, 216, 0.08); 
        padding: 4px 8px; 
        border-radius: 6px; 
        border: 1px solid rgba(42, 100, 216, 0.15);
        box-shadow: 0 0 10px rgba(42, 100, 216, 0.1);
    }
    
    .widget-log { font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #4a5c80; line-height: 1.6; margin-bottom: 20px; }
    
    .widget-data { display: flex; align-items: center; gap: 8px; padding-top: 16px; border-top: 1px solid rgba(14, 42, 102, 0.06); }
    .w-val { font-size: 14px; font-weight: 600; color: #050d1f; }
    .w-lbl { font-size: 12px; color: var(--royal-glow); font-weight: 500; }

    /* 
      THE INFINITE ROYAL ENVIRONMENT 
      Glows majestically from behind the matrix, dissolving perfectly into the abyss below.
    */
    .v1-app-environment {
        width: 100vw; 
        max-width: 1800px;
        /* The glowing celestial halo */
        background: radial-gradient(ellipse at top center, rgba(42, 100, 216, 0.4) 0%, rgba(20, 61, 141, 0.1) 40%, transparent 80%);
        z-index: 20;
        padding-top: 240px; 
        padding-bottom: 300px; /* Leave space for the seamless crossfade */
        position: relative;
        /* Master mask: solid at top, completely soft feather to transparent at bottom */
        -webkit-mask-image: linear-gradient(180deg, black 0%, black 60%, transparent 100%);
        mask-image: linear-gradient(180deg, black 0%, black 60%, transparent 100%);
    }

    /* Cinematic Light Flares */
    .ambient-flare-left {
        position: absolute;
        top: 200px;
        left: -10%;
        width: 800px;
        height: 800px;
        background: radial-gradient(circle, var(--ambient-cyan) 0%, transparent 60%);
        pointer-events: none;
        mix-blend-mode: screen;
    }
    
    .ambient-flare-right {
        position: absolute;
        top: 100px;
        right: -10%;
        width: 1000px;
        height: 700px;
        background: radial-gradient(ellipse, var(--glow-core) 0%, transparent 65%);
        pointer-events: none;
        mix-blend-mode: screen;
    }

    /* Live Commerce Matrix - High End Glassmorphism */
    .commerce-matrix {
        width: 90%;
        max-width: 1200px;
        margin: 0 auto;
        display: flex;
        flex-direction: column;
        gap: 16px;
        position: relative;
        z-index: 25;
        /* We nest another mask here so the rows themselves literally evaporate at the bottom */
        -webkit-mask-image: linear-gradient(180deg, black 0%, black 40%, rgba(0,0,0,0.15) 80%, transparent 100%);
        mask-image: linear-gradient(180deg, black 0%, black 40%, rgba(0,0,0,0.15) 80%, transparent 100%);
    }
    
    .matrix-header {
        display: flex;
        justify-content: space-between;
        align-items: flex-end;
        padding: 0 0 16px 0;
        border-bottom: 1px solid rgba(255,255,255,0.15);
        margin-bottom: 16px;
    }
    
    .mh-title { font-size: 20px; font-weight: 600; color: #FFFFFF; text-shadow: 0 0 20px rgba(94, 157, 255, 0.4); }
    .mh-status { font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--royal-light); display: flex; align-items: center; gap: 8px; text-transform: uppercase; letter-spacing: 0.1em; }
    .mh-dot { width: 6px; height: 6px; background: #5E9DFF; border-radius: 50%; box-shadow: 0 0 12px #5E9DFF; }

    .matrix-row {
        background: rgba(14, 42, 102, 0.3);
        backdrop-filter: blur(20px) saturate(120%);
        border: 1px solid rgba(94, 157, 255, 0.15);
        border-top: 1px solid rgba(255, 255, 255, 0.2); /* Soft illuminated top edge */
        border-radius: 16px;
        padding: 24px 32px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), background 0.4s, border-color 0.4s;
        box-shadow: 
            0 10px 40px rgba(7, 22, 56, 0.5),
            inset 0 0 30px rgba(42, 100, 216, 0.1);
    }
    
    .matrix-row:hover {
        background: rgba(20, 61, 141, 0.5);
        border-color: rgba(94, 157, 255, 0.3);
        transform: translateY(-4px) scale(1.01);
        box-shadow: 
            0 20px 50px rgba(7, 22, 56, 0.6),
            inset 0 0 40px rgba(94, 157, 255, 0.15);
    }
    
    .mr-supplier { display: flex; flex-direction: column; gap: 6px; width: 30%; }
    .mr-name { font-size: 16px; font-weight: 600; color: #FFFFFF; }
    .mr-type { font-size: 13px; color: #9ABBF7; }
    
    .mr-data { display: flex; flex-direction: column; gap: 6px; width: 20%; }
    .mrd-val { font-family: 'JetBrains Mono', monospace; font-size: 14px; color: #FFFFFF; font-weight: 500; }
    .mrd-lbl { font-size: 11px; color: #7CA6F2; text-transform: uppercase; letter-spacing: 0.1em; }
    
    /* Elegant Glowing Badges */
    .mr-badge { 
        padding: 8px 16px; 
        border-radius: 100px; 
        font-size: 12px; 
        font-weight: 600; 
        background: rgba(42, 100, 216, 0.2); 
        color: #FFFFFF; 
        border: 1px solid rgba(94, 157, 255, 0.3); 
        box-shadow: 0 0 20px rgba(42, 100, 216, 0.15);
    }
    .mr-badge.green { 
        background: rgba(16,185,129,0.15); 
        color: #34D399; 
        border: 1px solid rgba(16,185,129,0.4); 
        box-shadow: 0 0 25px rgba(16,185,129,0.2);
    }

    /* Skeleton rows for the infinite fade effect */
    .skeleton-row {
        height: 80px;
        background: rgba(14, 42, 102, 0.1);
        border: 1px solid rgba(94, 157, 255, 0.05);
        border-radius: 16px;
        margin-top: 8px;
    }

    @media (max-width: 991px) {
        .v1-title { font-size: 4rem; }
        .v1-command-module { width: 90%; }
        .cmd-input { font-size: 1rem; }
        .agent-widgets-grid { grid-template-columns: 1fr; }
        .matrix-row { flex-direction: column; align-items: flex-start; gap: 16px; }
        .mr-supplier, .mr-data { width: 100%; }
    }
    
    /* Make sure footer text is visible on the deep abyss background */
    .footer_component * {
        color: rgba(255,255,255,0.9) !important;
    }
    """
    
    soup = bs4.BeautifulSoup(html, 'html.parser')
    
    # Remove the old style injection
    for style in soup.find_all('style'):
        if style.string and ('@import url' in style.string and '--mist-blue' in style.string):
            style.decompose()

    new_style = soup.new_tag('style')
    new_style.string = style_str
    soup.head.append(new_style)

    # Let's replace the v1-app-environment part to add the flares and skeleton rows.
    # We will locate the old v1-app-environment and replace it.
    
    env_div = soup.find('div', class_='v1-app-environment')
    if env_div:
        new_env_html = """
        <div class="v1-app-environment">
            <!-- Cinematic Light Flares -->
            <div class="ambient-flare-left"></div>
            <div class="ambient-flare-right"></div>
            
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
                
                <div class="matrix-row">
                    <div class="mr-supplier">
                        <span class="mr-name">Haworth Inc</span>
                        <span class="mr-type">Manufacturer • Netherlands</span>
                    </div>
                    <div class="mr-data">
                        <span class="mrd-val">3,200</span>
                        <span class="mrd-lbl">YTD Volume</span>
                    </div>
                    <div class="mr-data">
                        <span class="mrd-val">Awaiting Data</span>
                        <span class="mrd-lbl">Compliance</span>
                    </div>
                    <div class="mr-badge">Processing...</div>
                </div>
                
                <!-- Skeleton rows for infinite dissipation effect -->
                <div class="skeleton-row" style="opacity: 0.6"></div>
                <div class="skeleton-row" style="opacity: 0.3"></div>
                <div class="skeleton-row" style="opacity: 0.1"></div>
            </div>
            
            <!-- We add the bouncing chevron icon from the image at the bottom of the fade -->
            <div style="position: absolute; bottom: 80px; left: 50%; transform: translateX(-50%); z-index: 30; opacity: 0.8; display: flex; flex-direction: column; align-items: center; gap: 8px;">
                <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#5E9DFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="animation: bounce 2s infinite;"><polyline points="7 13 12 18 17 13"></polyline><polyline points="7 6 12 11 17 6"></polyline></svg>
            </div>
            <style>@keyframes bounce { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(10px); } }</style>
        </div>
        """
        new_env = bs4.BeautifulSoup(new_env_html, 'html.parser')
        env_div.replace_with(new_env)

    with open('agentic-commerce.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    print("Royal Blue polish update complete.")

if __name__ == '__main__':
    run()
