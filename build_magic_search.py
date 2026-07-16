import bs4
import re

def run():
    with open('magic-ai-search.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = bs4.BeautifulSoup(html, 'html.parser')
    
    # Remove existing custom styles we don't want anymore
    for style in soup.find_all('style'):
        if style.string and ('@import url' in style.string and 'Inter' in style.string):
            style.decompose()
            
    style_str = """
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap');

    :root {
        /* Deep Purple AI Palette */
        --warm-white: #FFFFFF;
        --lavender-mist: #F4F1FF;
        --soft-indigo: #8A72FF;
        --deep-purple: #5B3DF5;
        --indigo-core: #6F52FF;
        --electric-violet: #9A7BFF;
        --rich-violet: #3A1FAD;
        --abyss-purple: #160A40; 
        
        /* Typography & Assets */
        --text-dark: #090320;
        --text-muted: #5B5282;
        --glass-bg: rgba(255, 255, 255, 0.7);
        --glass-dark: rgba(22, 10, 64, 0.4);
        --glass-border: rgba(255, 255, 255, 0.5);
    }

    body, html {
        margin: 0;
        padding: 0;
        width: 100%;
        font-family: 'Inter', -apple-system, sans-serif;
        background-color: var(--abyss-purple);
        /* The Master Environment Gradient */
        background-image: linear-gradient(180deg, 
            var(--warm-white) 0vh, 
            var(--warm-white) 25vh,
            var(--lavender-mist) 45vh, 
            var(--soft-indigo) 70vh,
            var(--deep-purple) 95vh,
            var(--rich-violet) 130vh,
            var(--abyss-purple) 180vh,
            var(--abyss-purple) 100%);
        background-attachment: fixed; 
        color: var(--warm-white);
        overflow-x: hidden;
    }

    /* Infinite Glowing World Grid (Purple theme) */
    .bg-grid {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background-image: 
            linear-gradient(to right, rgba(138, 114, 255, 0.08) 1px, transparent 1px),
            linear-gradient(to bottom, rgba(138, 114, 255, 0.08) 1px, transparent 1px);
        background-size: 80px 80px;
        z-index: 0;
        pointer-events: none;
        -webkit-mask-image: linear-gradient(180deg, transparent 40%, black 60%, transparent 95%);
        mask-image: linear-gradient(180deg, transparent 40%, black 60%, transparent 95%);
    }

    .magic-wrapper {
        position: relative;
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        z-index: 1;
        padding-top: 18vh;
    }

    /* THE TYPOGRAPHY - Massively Premium */
    .magic-typography {
        text-align: center;
        max-width: 1100px;
        padding: 0 24px;
        z-index: 20;
    }

    .m-title {
        font-size: 6.5rem;
        font-weight: 700;
        letter-spacing: -0.05em;
        line-height: 1.05;
        color: var(--text-dark);
        margin: 0 0 24px 0;
        text-shadow: 0 4px 30px rgba(91, 61, 245, 0.08);
    }

    .m-subtitle {
        font-size: 1.5rem;
        font-weight: 400;
        color: var(--text-muted);
        max-width: 650px;
        margin: 0 auto 56px auto;
        letter-spacing: -0.01em;
        line-height: 1.5;
    }

    /* FLOATING AI SEARCH BAR */
    .magic-search-bar {
        width: 100%;
        max-width: 800px;
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(40px) saturate(150%);
        -webkit-backdrop-filter: blur(40px) saturate(150%);
        border: 1px solid rgba(255,255,255,1);
        border-radius: 100px;
        padding: 12px 12px 12px 28px;
        display: flex;
        align-items: center;
        gap: 20px;
        box-shadow: 
            0 30px 80px rgba(91, 61, 245, 0.15), 
            0 10px 20px rgba(91, 61, 245, 0.05),
            inset 0 1px 0 rgba(255,255,255,0.8),
            0 0 0 8px rgba(255,255,255,0.4);
        z-index: 35;
        margin: 0 auto 48px auto;
    }

    .msb-icon {
        width: 32px;
        height: 32px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: var(--deep-purple);
        flex-shrink: 0;
        font-size: 24px;
        filter: drop-shadow(0 0 10px rgba(91, 61, 245, 0.4));
    }

    .msb-input {
        font-size: 1.25rem;
        font-weight: 500;
        color: var(--text-dark);
        flex-grow: 1;
        display: flex;
        align-items: center;
    }

    .msb-button {
        background: linear-gradient(135deg, var(--deep-purple), var(--indigo-core));
        color: white;
        padding: 16px 28px;
        border-radius: 100px;
        font-weight: 600;
        font-size: 15px;
        display: flex;
        align-items: center;
        gap: 8px;
        box-shadow: 0 10px 20px rgba(91, 61, 245, 0.3);
        cursor: pointer;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .msb-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 15px 30px rgba(91, 61, 245, 0.4);
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
        background: var(--deep-purple); 
        margin-left: 4px;
        animation: blink 1s step-end infinite;
    }

    @keyframes typing { from { width: 0; } to { width: 100%; } }
    @keyframes blink { 50% { opacity: 0; } }

    /* FLOATING AI PROCESS CARDS */
    .magic-process-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
        width: 100%;
        max-width: 800px;
        margin: 0 auto 120px auto;
        z-index: 30;
    }

    .mp-card {
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(30px) saturate(180%);
        -webkit-backdrop-filter: blur(30px) saturate(180%);
        border: 1px solid rgba(255,255,255,0.7);
        border-radius: 16px;
        padding: 20px 24px;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        box-shadow: 
            0 20px 40px rgba(91, 61, 245, 0.08),
            0 5px 15px rgba(91, 61, 245, 0.03),
            inset 0 1px 0 rgba(255,255,255,1);
        opacity: 0;
        transform: translateY(15px);
        animation: float-up 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }
    
    .mp-card:nth-child(1) { animation-delay: 3.5s; }
    .mp-card:nth-child(2) { animation-delay: 3.7s; }
    .mp-card:nth-child(3) { animation-delay: 3.9s; }

    .mpc-title { font-size: 14px; font-weight: 600; color: var(--text-dark); margin-bottom: 4px;}
    .mpc-desc { font-size: 13px; color: var(--text-muted); margin-bottom: 12px;}
    .mpc-status {
        font-family: 'JetBrains Mono', monospace; 
        font-size: 10px; 
        font-weight: 700; 
        color: var(--deep-purple); 
        background: rgba(91, 61, 245, 0.1); 
        padding: 4px 10px; 
        border-radius: 100px; 
    }

    /* THE SEARCH ENGINE WORKSPACE */
    .magic-workspace-container {
        width: 100vw;
        max-width: 1600px;
        position: relative;
        z-index: 20;
        padding: 60px 40px 240px 40px;
        /* Master mask: completely soft feather to transparent at bottom */
        -webkit-mask-image: linear-gradient(180deg, black 0%, black 75%, transparent 100%);
        mask-image: linear-gradient(180deg, black 0%, black 75%, transparent 100%);
    }

    /* Ambient Workspace Lighting */
    .ambient-flare-purple {
        position: absolute;
        top: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 1200px;
        height: 800px;
        background: radial-gradient(ellipse, rgba(138, 114, 255, 0.35) 0%, transparent 65%);
        pointer-events: none;
        mix-blend-mode: screen;
        z-index: 0;
    }

    .mw-layout {
        display: grid;
        grid-template-columns: 280px 1fr 300px;
        gap: 32px;
        position: relative;
        z-index: 10;
        width: 100%;
        margin: 0 auto;
    }

    /* Side Panels */
    .mw-side-panel {
        background: rgba(22, 10, 64, 0.4);
        backdrop-filter: blur(40px) saturate(120%);
        -webkit-backdrop-filter: blur(40px) saturate(120%);
        border: 1px solid rgba(138, 114, 255, 0.2);
        border-top: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 24px;
        padding: 28px;
        box-shadow: 
            0 30px 60px rgba(9, 3, 32, 0.4),
            inset 0 0 40px rgba(138, 114, 255, 0.05);
        height: fit-content;
    }

    .sp-title { font-size: 16px; font-weight: 600; color: #FFFFFF; margin-bottom: 20px; display: flex; align-items: center; gap: 8px;}
    .sp-list { display: flex; flex-direction: column; gap: 14px; margin-bottom: 24px;}
    .spl-item { font-size: 13px; color: #E0DAFF; display: flex; align-items: center; gap: 8px;}
    .sp-footer { font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--electric-violet); border-top: 1px solid rgba(138, 114, 255, 0.15); padding-top: 16px; margin-top: 8px;}

    .sp-metric { font-size: 28px; font-weight: 700; color: #34D399; line-height: 1;}
    .sp-desc { font-size: 12px; color: #B3A4FF; margin-top: 8px; margin-bottom: 20px; line-height: 1.4;}
    .sp-chart { height: 50px; width: 100%; margin-bottom: 24px;}
    .sp-divider { height: 1px; width: 100%; background: rgba(138, 114, 255, 0.15); margin: 24px 0;}
    .sp-small-text { font-size: 12px; color: #B3A4FF;}
    .sp-large-price { font-size: 24px; font-weight: 700; color: #FFFFFF; margin: 4px 0; display: flex; align-items: center; gap: 12px;}
    .tag-green { background: rgba(16,185,129,0.15); color: #34D399; padding: 4px 8px; border-radius: 6px; font-size: 10px; font-weight: 600;}
    .tag-blue { background: rgba(56, 189, 248, 0.15); color: #38BDF8; padding: 4px 8px; border-radius: 6px; font-size: 10px; font-weight: 600;}
    .sp-button { background: var(--indigo-core); color: white; text-align: center; padding: 14px; border-radius: 12px; font-weight: 600; font-size: 14px; margin-top: 24px; cursor: pointer; transition: background 0.2s;}
    .sp-button:hover { background: var(--deep-purple); }

    /* Center Grid (Search Engine) */
    .mw-center {
        display: flex;
        flex-direction: column;
        gap: 24px;
    }

    .mwc-header {
        background: rgba(22, 10, 64, 0.6);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(138, 114, 255, 0.15);
        border-radius: 20px;
        padding: 16px 24px;
        display: flex;
        flex-direction: column;
        gap: 16px;
    }
    .mwc-input { font-size: 15px; color: #E0DAFF; display: flex; align-items: center; gap: 12px;}
    .mwc-tabs { display: flex; gap: 24px; border-top: 1px solid rgba(138, 114, 255, 0.1); padding-top: 16px;}
    .mwc-tabs span { font-size: 13px; font-weight: 500; color: #B3A4FF; cursor: pointer;}
    .mwc-tabs span.active { color: #FFFFFF; border-bottom: 2px solid var(--electric-violet); padding-bottom: 4px;}

    .mwc-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
    }

    .mwc-product {
        background: rgba(255, 255, 255, 1);
        border-radius: 20px;
        padding: 16px;
        position: relative;
        display: flex;
        flex-direction: column;
        gap: 8px;
        box-shadow: 0 10px 30px rgba(9, 3, 32, 0.2);
        transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.3s;
        cursor: pointer;
    }
    .mwc-product:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(9, 3, 32, 0.4), 0 0 0 2px var(--soft-indigo);
    }
    .prod-badge {
        position: absolute;
        top: 24px;
        left: 24px;
        background: var(--deep-purple);
        color: white;
        padding: 6px 12px;
        border-radius: 100px;
        font-size: 11px;
        font-weight: 700;
        z-index: 2;
        box-shadow: 0 4px 10px rgba(91, 61, 245, 0.3);
    }
    .prod-badge.blue { background: #38BDF8; box-shadow: 0 4px 10px rgba(56, 189, 248, 0.3); }
    .prod-badge.green { background: #10B981; box-shadow: 0 4px 10px rgba(16, 185, 129, 0.3); }
    
    .prod-img { width: 100%; height: 200px; object-fit: contain; border-radius: 12px; background: #F8F9FA; margin-bottom: 8px;}
    .prod-title { font-size: 15px; font-weight: 600; color: #090320; line-height: 1.3;}
    .prod-supplier { font-size: 12px; color: #5B5282; display: flex; align-items: center; gap: 4px;}
    .prod-rating { font-size: 12px; font-weight: 600; color: #EAB308;}
    .prod-price { font-size: 20px; font-weight: 700; color: #090320; margin: 4px 0;}
    .prod-price span { font-size: 12px; font-weight: 500; color: #9CA3AF;}
    .prod-tags { display: flex; gap: 8px; margin-top: auto;}

    /* BOTTOM STATISTICS */
    .magic-stats {
        display: flex;
        justify-content: center;
        gap: 80px;
        margin-top: 80px;
        padding-top: 60px;
        border-top: 1px solid rgba(138, 114, 255, 0.15);
        position: relative;
        z-index: 20;
    }
    .m-stat { display: flex; flex-direction: column; align-items: center; gap: 8px;}
    .ms-val { font-size: 48px; font-weight: 700; color: #FFFFFF; line-height: 1; letter-spacing: -0.03em;}
    .ms-lbl { font-size: 14px; font-weight: 500; color: #B3A4FF; text-transform: uppercase; letter-spacing: 0.1em;}

    @media (max-width: 1200px) {
        .mw-layout { grid-template-columns: 1fr; }
        .mw-side-panel { display: none; } /* Hide panels on smaller screens for simplicity */
        .mwc-grid { grid-template-columns: repeat(2, 1fr); }
    }
    @media (max-width: 768px) {
        .m-title { font-size: 4rem; }
        .magic-process-grid { grid-template-columns: 1fr; }
        .mwc-grid { grid-template-columns: 1fr; }
        .magic-stats { flex-direction: column; gap: 40px; }
    }

    /* Override footer text for dark abyss */
    .footer_component * { color: rgba(255,255,255,0.9) !important; }
    </style>
    """
    
    new_style = soup.new_tag('style')
    new_style.string = style_str
    soup.head.append(new_style)

    magic_html = """
    <main class="magic-wrapper">
        <div class="bg-grid"></div>
        
        <!-- HERO -->
        <div class="magic-typography">
            <div class="m-title">Find anything.<br/>Instantly. Intelligently.</div>
            <div class="m-subtitle">Search millions of products across suppliers, catalogs and marketplaces using natural language and AI reasoning.</div>
        </div>

        <div class="magic-search-bar">
            <div class="msb-icon">✨</div>
            <div class="msb-input">
                <span class="typewriter-text">Find ergonomic chairs under $200 that ship to Lagos within 5 days...</span><span class="cursor"></span>
            </div>
            <div class="msb-button">Search with AI</div>
        </div>

        <!-- AI PROCESS CARDS -->
        <div class="magic-process-grid">
            <div class="mp-card">
                <div class="mpc-title">Intent Understanding</div>
                <div class="mpc-desc">Natural language parsing</div>
                <div class="mpc-status">ACTIVE</div>
            </div>
            <div class="mp-card">
                <div class="mpc-title">Multi-source Search</div>
                <div class="mpc-desc">Searching 12,482 products</div>
                <div class="mpc-status">ACTIVE</div>
            </div>
            <div class="mp-card">
                <div class="mpc-title">Smart Ranking</div>
                <div class="mpc-desc">Evaluating suppliers</div>
                <div class="mpc-status">ACTIVE</div>
            </div>
        </div>

        <!-- WORKSPACE -->
        <div class="magic-workspace-container">
            <div class="ambient-flare-purple"></div>
            
            <div class="mw-layout">
                <!-- Left Panel -->
                <div class="mw-side-panel left-panel">
                    <div class="sp-title">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
                        AI Understanding
                    </div>
                    <div class="sp-list">
                        <div class="spl-item">
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#34D399" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
                            Intent detected
                        </div>
                        <div class="spl-item">
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#34D399" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
                            Budget understood
                        </div>
                        <div class="spl-item">
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#34D399" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
                            Category recognized
                        </div>
                        <div class="spl-item">
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#34D399" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
                            Destination mapped
                        </div>
                    </div>
                    <div class="sp-footer">✓ Results ready in 2.8s</div>
                </div>

                <!-- Center Grid -->
                <div class="mw-center">
                    <div class="mwc-header">
                        <div class="mwc-input">
                            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                            Ergonomic office chairs under $200...
                        </div>
                        <div class="mwc-tabs">
                            <span class="active">All Results</span>
                            <span>Verified Suppliers</span>
                            <span>Fastest Shipping</span>
                        </div>
                    </div>
                    
                    <div class="mwc-grid">
                        <div class="mwc-product">
                            <div class="prod-badge">Best Match</div>
                            <img src="https://images.unsplash.com/photo-1505843490538-5133c6c7d0e1?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80" alt="Chair" class="prod-img"/>
                            <div class="prod-title">ErgoPro Mesh Office Chair</div>
                            <div class="prod-supplier">Foshan Comfort Co. <svg width="14" height="14" viewBox="0 0 24 24" fill="#38BDF8" stroke="#38BDF8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg></div>
                            <div class="prod-rating">⭐ 4.9 (1,248)</div>
                            <div class="prod-price">$89.00 <span>/ unit</span></div>
                            <div class="prod-tags">
                                <span class="tag-green">✦ Fast Shipping</span>
                                <span class="tag-blue">✦ Low MOQ</span>
                            </div>
                        </div>

                        <div class="mwc-product">
                            <div class="prod-badge blue">Top Rated</div>
                            <img src="https://images.unsplash.com/photo-1592078615290-033ee584e267?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80" alt="Chair" class="prod-img"/>
                            <div class="prod-title">FlexiChair Pro Master</div>
                            <div class="prod-supplier">Zhejiang Furnishings <svg width="14" height="14" viewBox="0 0 24 24" fill="#38BDF8" stroke="#38BDF8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg></div>
                            <div class="prod-rating">⭐ 4.8 (2,156)</div>
                            <div class="prod-price">$92.50 <span>/ unit</span></div>
                            <div class="prod-tags">
                                <span class="tag-green">✦ Fast Shipping</span>
                            </div>
                        </div>

                        <div class="mwc-product">
                            <div class="prod-badge green">Best Value</div>
                            <img src="https://images.unsplash.com/photo-1580480055273-228ff5388ef8?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80" alt="Chair" class="prod-img"/>
                            <div class="prod-title">NexSeat Ergonomic</div>
                            <div class="prod-supplier">Guangdong Smart Living <svg width="14" height="14" viewBox="0 0 24 24" fill="#38BDF8" stroke="#38BDF8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg></div>
                            <div class="prod-rating">⭐ 4.8 (987)</div>
                            <div class="prod-price">$85.00 <span>/ unit</span></div>
                            <div class="prod-tags">
                                <span class="tag-blue">✦ Low MOQ</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Right Panel -->
                <div class="mw-side-panel right-panel">
                    <div class="sp-title">Market Insights</div>
                    <div class="sp-metric">-18%</div>
                    <div class="sp-desc">Avg. price dropped in the last 30 days</div>
                    <div class="sp-chart">
                        <svg viewBox="0 0 100 30" style="width:100%; height:100%; overflow:visible;">
                            <!-- Drop shadow for glow -->
                            <path d="M0 25 Q10 20 20 22 T40 15 T60 18 T80 5 T100 10" fill="none" stroke="rgba(52, 211, 153, 0.4)" stroke-width="6" stroke-linecap="round" filter="blur(4px)"/>
                            <path d="M0 25 Q10 20 20 22 T40 15 T60 18 T80 5 T100 10" fill="none" stroke="#34D399" stroke-width="2" stroke-linecap="round"/>
                        </svg>
                    </div>
                    
                    <div class="sp-divider"></div>
                    
                    <div class="sp-title">Procurement Summary</div>
                    <div class="sp-small-text">Est. Landed Cost</div>
                    <div class="sp-large-price">$7,650.00 <span class="tag-green">23% better value</span></div>
                    <div class="sp-small-text">for 100 units</div>
                    
                    <div class="sp-list mt-4" style="margin-top: 24px;">
                        <div class="spl-item">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
                            5 Verified Suppliers
                        </div>
                        <div class="spl-item">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="1" y="3" width="15" height="13"></rect><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"></polygon><circle cx="5.5" cy="18.5" r="2.5"></circle><circle cx="18.5" cy="18.5" r="2.5"></circle></svg>
                            3 Ship within 2 weeks
                        </div>
                        <div class="spl-item">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
                            All pass compliance
                        </div>
                    </div>
                    <div class="sp-button">Start Procurement →</div>
                </div>
            </div>

            <!-- Bottom Stats -->
            <div class="magic-stats">
                <div class="m-stat">
                    <div class="ms-val">12M+</div>
                    <div class="ms-lbl">Products</div>
                </div>
                <div class="m-stat">
                    <div class="ms-val">50K+</div>
                    <div class="ms-lbl">Stores</div>
                </div>
                <div class="m-stat">
                    <div class="ms-val">280ms</div>
                    <div class="ms-lbl">Search Time</div>
                </div>
                <div class="m-stat">
                    <div class="ms-val">98.8%</div>
                    <div class="ms-lbl">Accuracy</div>
                </div>
            </div>
            
            <div style="position: absolute; bottom: 80px; left: 50%; transform: translateX(-50%); z-index: 30; opacity: 0.8; display: flex; flex-direction: column; align-items: center; gap: 8px;">
                <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#8A72FF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="animation: bounce 2s infinite;"><polyline points="7 13 12 18 17 13"></polyline><polyline points="7 6 12 11 17 6"></polyline></svg>
            </div>
            <style>@keyframes bounce { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(10px); } }</style>
        </div>
    </main>
    """
    
    magic_soup = bs4.BeautifulSoup(magic_html, 'html.parser')
    
    # Locate nav and footer
    nav = soup.find('nav', class_='mega-nav')
    footer = soup.find('footer', class_='footer_component')
    
    if nav and footer:
        # Remove everything between nav and footer
        curr = nav.next_sibling
        while curr and curr != footer:
            next_node = curr.next_sibling
            curr.extract()
            curr = next_node
            
        # Insert our new magic wrapper
        nav.insert_after(magic_soup)
    else:
        print("Error: Could not find nav or footer")

    with open('magic-ai-search.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    print("Magic AI Search page successfully built.")

if __name__ == '__main__':
    run()
