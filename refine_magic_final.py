import bs4

def run():
    with open('magic-ai-search.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = bs4.BeautifulSoup(html, 'html.parser')
    
    # Remove existing custom styles we don't want anymore
    for style in soup.find_all('style'):
        if style.string and ('Deep Purple AI Palette' in style.string or 'magic-wrapper' in style.string or 'magic-white' in style.string):
            style.decompose()
            
    style_str = """
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    :root {
        --magic-white: #FFFFFF;
        --magic-bg-purple: #EBE5FF;
        --magic-deep-purple: #3B2475;
        --magic-royal-purple: #5B3DF5;
        --magic-violet: #8A72FF;
        --magic-indigo: #160A40;
        --magic-text-dark: #090320;
        --magic-text-gray: #475569;
        --magic-text-muted: #5B5282;
    }

    body, html {
        margin: 0;
        padding: 0;
        width: 100%;
        font-family: 'Inter', sans-serif;
        background-color: var(--magic-white);
        overflow-x: hidden;
    }

    .magic-wrapper {
        position: relative;
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        z-index: 1;
        overflow: hidden;
    }

    /* THE CONTINUOUS BACKGROUND SYSTEM */
    .magic-bg-top {
        background: var(--magic-white);
        width: 100%;
        position: relative;
        z-index: 10;
        padding-top: 140px;
        padding-bottom: 60px;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    /* Seamless gradient blending down to deep indigo */
    .magic-bg-bottom {
        background: linear-gradient(180deg, #A88BFF 0%, #5B3DF5 30%, #3A1FAD 60%, #160A40 100%);
        width: 100%;
        position: relative;
        z-index: 5;
        display: flex;
        flex-direction: column;
        align-items: center;
        padding-bottom: 120px;
    }

    /* The Volumetric Glow Wave */
    .magic-wave-divider {
        position: absolute;
        bottom: -150px;
        left: 0;
        width: 100%;
        height: 400px;
        overflow: hidden;
        z-index: 0;
        pointer-events: none;
    }
    
    .magic-wave-divider::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 250vw;
        height: 600px;
        background: radial-gradient(ellipse at bottom, rgba(255,255,255,1) 0%, rgba(255,255,255,1) 30%, transparent 75%);
        opacity: 1;
        z-index: 1;
    }
    
    .magic-flare {
        position: absolute;
        top: -100px;
        left: 50%;
        transform: translateX(-50%);
        width: 100vw;
        height: 800px;
        background: radial-gradient(ellipse, rgba(255, 255, 255, 0.3) 0%, transparent 70%);
        mix-blend-mode: overlay;
        pointer-events: none;
        z-index: 2;
    }

    .magic-flare-2 {
        position: absolute;
        bottom: 100px;
        left: 50%;
        transform: translateX(-50%);
        width: 180vw;
        height: 600px;
        background: radial-gradient(ellipse at center, rgba(168, 139, 255, 0.2) 0%, transparent 70%);
        mix-blend-mode: screen;
        pointer-events: none;
        z-index: 1;
    }

    /* TYPOGRAPHY */
    .m-title {
        font-size: 5.5rem;
        font-weight: 700;
        letter-spacing: -0.04em;
        line-height: 1.05;
        /* Headline in Deep Purple (#3B2475) */
        color: var(--magic-deep-purple);
        margin: 0 0 24px 0;
        text-align: center;
        max-width: 900px;
        position: relative;
        z-index: 20;
    }

    .m-subtitle {
        font-size: 1.25rem;
        font-weight: 400;
        /* Supporting text Dark Slate */
        color: var(--magic-text-gray);
        max-width: 650px;
        margin: 0 auto 56px auto;
        line-height: 1.6;
        text-align: center;
        position: relative;
        z-index: 20;
    }

    /* SEARCH BAR */
    .magic-search-bar {
        width: 100%;
        max-width: 700px;
        /* White glass */
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(255,255,255,1);
        border-radius: 100px;
        padding: 10px 10px 10px 24px;
        display: flex;
        align-items: center;
        gap: 16px;
        box-shadow: 0 20px 40px rgba(91, 61, 245, 0.08), 0 0 0 1px rgba(91, 61, 245, 0.1);
        margin-bottom: 60px;
        position: relative;
        z-index: 20;
    }

    .msb-icon {
        color: var(--magic-royal-purple);
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .msb-input {
        font-size: 1rem;
        color: var(--magic-text-dark);
        flex-grow: 1;
    }

    .msb-button {
        background: var(--magic-royal-purple);
        color: white;
        width: 44px;
        height: 44px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 8px 16px rgba(91, 61, 245, 0.3);
        cursor: pointer;
        flex-shrink: 0;
    }

    /* 3 AI PROCESS CARDS */
    .magic-process-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 24px;
        width: 100%;
        max-width: 900px;
        position: relative;
        z-index: 20;
    }

    .mp-card {
        /* White frosted glass */
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(255,255,255,1);
        border-radius: 20px;
        padding: 24px;
        display: flex;
        flex-direction: column;
        box-shadow: 0 20px 40px rgba(9, 3, 32, 0.04), 0 0 0 1px rgba(9, 3, 32, 0.02);
    }
    
    .mpc-header {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 12px;
    }
    
    .mpc-icon {
        width: 40px;
        height: 40px;
        background: #F4F0FF;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: var(--magic-royal-purple);
    }

    .mpc-num { font-size: 12px; font-weight: 700; color: var(--magic-royal-purple); }
    .mpc-title { font-size: 15px; font-weight: 600; color: var(--magic-text-dark); }
    .mpc-desc { font-size: 13px; color: var(--magic-text-gray); line-height: 1.5; flex-grow: 1;}

    /* WORKSPACE (THE HERO FEATURE) */
    .magic-workspace {
        width: 100%;
        max-width: 1200px;
        /* Completely transparent, no box */
        background: transparent;
        border: none;
        box-shadow: none;
        padding: 24px;
        display: grid;
        grid-template-columns: 240px 1fr 240px;
        gap: 32px;
        position: relative;
        z-index: 20;
        margin-top: 100px;
    }

    /* Workspace Left */
    .ws-left { padding: 0; display: flex; flex-direction: column;}
    .ws-title { font-size: 14px; font-weight: 600; color: #FFFFFF; margin-bottom: 24px;}
    .ws-list { display: flex; flex-direction: column; gap: 24px; flex-grow: 1;}
    .wsl-item { display: flex; flex-direction: column; gap: 4px;}
    .wsl-item-header { display: flex; align-items: center; gap: 8px; font-size: 13px; font-weight: 600; color: #FFFFFF;}
    .wsl-item-desc { font-size: 11px; color: rgba(255,255,255,0.7); padding-left: 24px;}
    .ws-check {
        width: 16px; height: 16px; background: #FFFFFF; border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
    }

    /* Workspace Center */
    .ws-center { display: flex; flex-direction: column; gap: 16px;}
    
    /* Applying soft glassmorphism to center elements so they float elegantly */
    .wsc-search-bar {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 12px;
        padding: 12px 16px;
        display: flex;
        align-items: center;
        gap: 12px;
        justify-content: space-between;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
    }
    .wsc-search-info { display: flex; align-items: center; gap: 12px; font-size: 12px; color: #FFFFFF;}
    .wsc-search-info span { color: rgba(255,255,255,0.7);}
    
    .wsc-filters { display: flex; gap: 12px;}
    .wsc-filter { background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.1); padding: 8px 12px; border-radius: 8px; font-size: 11px; color: #FFFFFF; display: flex; align-items: center; gap: 6px;}

    .wsc-products { display: flex; flex-direction: column; gap: 12px;}
    .wsc-product {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 16px;
        padding: 12px;
        display: flex;
        align-items: center;
        gap: 16px;
        transition: transform 0.2s, background 0.2s;
        cursor: pointer;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    .wsc-product:hover { background: rgba(255,255,255,0.08); transform: translateY(-2px);}
    .wscp-img { width: 80px; height: 80px; border-radius: 12px; background: #FFFFFF; object-fit: contain; padding: 4px;}
    .wscp-info { flex-grow: 1; display: flex; flex-direction: column; gap: 4px;}
    .wscp-badge { background: var(--magic-royal-purple); color: white; padding: 2px 8px; border-radius: 4px; font-size: 9px; font-weight: 700; width: fit-content; margin-bottom: 2px;}
    .wscp-badge.green { background: #10B981; }
    .wscp-badge.blue { background: #38BDF8; }
    .wscp-title { font-size: 14px; font-weight: 600; color: #FFFFFF; margin:0;}
    .wscp-store { font-size: 11px; color: rgba(255,255,255,0.7);}
    .wscp-rating { font-size: 11px; color: #FBBF24; display: flex; align-items: center; gap: 4px; margin-top: 2px;}
    .wscp-rating span { color: rgba(255,255,255,0.7);}
    
    .wscp-price-col { text-align: right; margin-right: 16px;}
    .wscp-price { font-size: 18px; font-weight: 700; color: #FFFFFF;}
    .wscp-price-old { font-size: 11px; color: rgba(255,255,255,0.7); text-decoration: line-through;}
    .wscp-discount { font-size: 9px; background: rgba(255,255,255,0.15); padding: 2px 4px; border-radius: 4px; color: #FFFFFF; margin-left: 4px;}
    
    .wscp-delivery-col { width: 100px;}
    .wscp-delivery-time { font-size: 12px; font-weight: 600; color: #FFFFFF;}
    .wscp-delivery-dest { font-size: 11px; color: rgba(255,255,255,0.7);}
    
    .wscp-action { width: 100px; display: flex; flex-direction: column; align-items: flex-end; gap: 12px;}
    .wscp-btn { background: var(--magic-royal-purple); color: white; padding: 8px 16px; border-radius: 8px; font-size: 11px; font-weight: 600; white-space: nowrap; border: 1px solid rgba(255,255,255,0.2);}

    /* Workspace Right */
    .ws-right { padding: 0; display: flex; flex-direction: column; gap: 32px;}
    .wsr-section { display: flex; flex-direction: column; gap: 12px;}
    .wsr-title { font-size: 12px; font-weight: 600; color: #FFFFFF;}
    .wsr-metric { font-size: 11px; color: rgba(255,255,255,0.7); display: flex; align-items: center; gap: 6px;}
    .wsr-trend { color: #10B981; background: rgba(16, 185, 129, 0.2); padding: 2px 6px; border-radius: 4px; font-weight: 600;}
    
    .wsr-demand { font-size: 12px; font-weight: 600; color: #FFFFFF;}
    .wsr-demand-desc { font-size: 11px; color: rgba(255,255,255,0.7); line-height: 1.4;}
    
    .wsr-gauge { width: 80px; height: 80px; border-radius: 50%; border: 4px solid rgba(255,255,255,0.1); border-top-color: var(--magic-royal-purple); border-right-color: var(--magic-royal-purple); display: flex; align-items: center; justify-content: center; font-size: 20px; font-weight: 700; color: #FFFFFF;}

    /* BUSINESS VALUE CARDS */
    .bv-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 20px;
        width: 100%;
        max-width: 1100px;
        position: relative;
        z-index: 20;
        margin-top: 80px;
    }
    
    .bv-card {
        background: rgba(255,255,255,0.05);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 20px;
        padding: 32px 24px;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
    }
    
    .bvc-val { font-size: 36px; font-weight: 700; color: #FFFFFF; line-height: 1; margin-bottom: 8px;}
    .bvc-desc { font-size: 13px; color: rgba(255,255,255,0.7); line-height: 1.4;}

    /* FINAL CTA */
    .magic-cta {
        margin-top: 100px;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        position: relative;
        z-index: 20;
    }

    .mcta-title { font-size: 2.5rem; font-weight: 700; color: #FFFFFF; margin-bottom: 16px; letter-spacing: -0.02em;}
    .mcta-subtitle { font-size: 1.1rem; color: rgba(255,255,255,0.8); max-width: 500px; line-height: 1.5; margin-bottom: 40px;}
    .mcta-btn {
        background: var(--magic-royal-purple);
        color: white;
        padding: 16px 32px;
        border-radius: 100px;
        font-weight: 600;
        font-size: 15px;
        display: flex;
        align-items: center;
        gap: 8px;
        box-shadow: 0 10px 20px rgba(91, 61, 245, 0.4);
        cursor: pointer;
        transition: transform 0.2s;
        border: 1px solid rgba(255,255,255,0.2);
    }
    .mcta-btn:hover { transform: translateY(-2px); }

    /* RESPONSIVE */
    @media (max-width: 1100px) {
        .magic-workspace { grid-template-columns: 1fr; }
        .ws-left, .ws-right { display: none; }
        .bv-grid { grid-template-columns: repeat(2, 1fr); }
    }
    @media (max-width: 768px) {
        .m-title { font-size: 3.5rem; }
        .magic-process-grid { grid-template-columns: 1fr; }
        .bv-grid { grid-template-columns: 1fr; }
        .wsc-products { overflow-x: auto; }
        .wsc-product { min-width: 600px; }
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
        
        <!-- SECTION 1: EDITORIAL HERO -->
        <div class="magic-bg-top">
            <div class="m-title">Find anything.<br/>Instantly. Intelligently.</div>
            <div class="m-subtitle">Magic AI Search understands natural language, scans millions of products, compares stores, and delivers the best purchasing decisions in seconds.</div>

            <div class="magic-search-bar">
                <div class="msb-icon">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg>
                </div>
                <div class="msb-input">
                    Find ergonomic chairs under $200 that ship to Lagos within 5 days.
                </div>
                <div class="msb-button">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                </div>
            </div>

            <!-- AI PROCESS CARDS -->
            <div class="magic-process-grid">
                <div class="mp-card">
                    <div class="mpc-header">
                        <div class="mpc-icon">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg>
                        </div>
                        <div>
                            <div class="mpc-num">01</div>
                            <div class="mpc-title">Intent Understanding</div>
                        </div>
                    </div>
                    <div class="mpc-desc">Reads natural language and identifies user intent.</div>
                </div>
                
                <div class="mp-card">
                    <div class="mpc-header">
                        <div class="mpc-icon">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                        </div>
                        <div>
                            <div class="mpc-num">02</div>
                            <div class="mpc-title">Multi-source Search</div>
                        </div>
                    </div>
                    <div class="mpc-desc">Searches millions of products across connected retailers.</div>
                </div>

                <div class="mp-card">
                    <div class="mpc-header">
                        <div class="mpc-icon">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                        </div>
                        <div>
                            <div class="mpc-num">03</div>
                            <div class="mpc-title">Smart Ranking</div>
                        </div>
                    </div>
                    <div class="mpc-desc">Ranks products using price, availability, delivery time and AI confidence.</div>
                </div>
            </div>
            
            <div class="magic-wave-divider"></div>
        </div>

        <!-- SECTION 2: PRODUCT EXPERIENCE -->
        <div class="magic-bg-bottom">
            <div class="magic-flare"></div>
            
            <!-- THE WORKSPACE -->
            <!-- Workspace has no background and dissolves into the environment -->
            <div class="magic-workspace">
                <!-- Left -->
                <div class="ws-left">
                    <div class="ws-title">AI Understanding</div>
                    <div class="ws-list">
                        <div class="wsl-item">
                            <div class="wsl-item-header">
                                <div class="ws-check"><svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="var(--magic-royal-purple)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg></div>
                                Intent detected
                            </div>
                            <div class="wsl-item-desc">Ergonomic office chairs</div>
                        </div>
                        <div class="wsl-item">
                            <div class="wsl-item-header">
                                <div class="ws-check"><svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="var(--magic-royal-purple)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg></div>
                                Budget identified
                            </div>
                            <div class="wsl-item-desc">Under $200</div>
                        </div>
                        <div class="wsl-item">
                            <div class="wsl-item-header">
                                <div class="ws-check"><svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="var(--magic-royal-purple)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg></div>
                                Category mapped
                            </div>
                            <div class="wsl-item-desc">Office Furniture</div>
                        </div>
                        <div class="wsl-item">
                            <div class="wsl-item-header">
                                <div class="ws-check"><svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="var(--magic-royal-purple)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg></div>
                                Delivery location
                            </div>
                            <div class="wsl-item-desc">Lagos, Nigeria</div>
                        </div>
                    </div>
                </div>

                <!-- Center -->
                <div class="ws-center">
                    
                    <div class="wsc-products">
                        <!-- Product 1 -->
                        <div class="wsc-product">
                            <img src="https://images.unsplash.com/photo-1505843490538-5133c6c7d0e1?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80" alt="Chair" class="wscp-img"/>
                            <div class="wscp-info">
                                <div class="wscp-badge">Best Match</div>
                                <div class="wscp-title">ErgoPro Mesh Chair</div>
                                <div class="wscp-store">OfficePro Direct</div>
                                <div class="wscp-rating"><svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg> 4.7 <span>(1,248)</span></div>
                            </div>
                            <div class="wscp-price-col">
                                <div class="wscp-price">$189</div>
                                <div><span class="wscp-discount">24% OFF</span></div>
                            </div>
                            <div class="wscp-delivery-col">
                                <div class="wscp-delivery-time">2-4 days</div>
                                <div class="wscp-delivery-dest">Delivery to Lagos</div>
                            </div>
                        </div>

                        <!-- Product 2 -->
                        <div class="wsc-product">
                            <img src="https://images.unsplash.com/photo-1592078615290-033ee584e267?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80" alt="Chair" class="wscp-img"/>
                            <div class="wscp-info">
                                <div class="wscp-badge green">Lowest Price</div>
                                <div class="wscp-title">ComfortMesh Task Chair</div>
                                <div class="wscp-store">WorkSmart Store</div>
                                <div class="wscp-rating"><svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg> 4.5 <span>(890)</span></div>
                            </div>
                            <div class="wscp-price-col">
                                <div class="wscp-price">$168</div>
                                <div><span class="wscp-discount">28% OFF</span></div>
                            </div>
                            <div class="wscp-delivery-col">
                                <div class="wscp-delivery-time">3-5 days</div>
                                <div class="wscp-delivery-dest">Delivery to Lagos</div>
                            </div>
                        </div>

                        <!-- Product 3 -->
                        <div class="wsc-product">
                            <img src="https://images.unsplash.com/photo-1580480055273-228ff5388ef8?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80" alt="Chair" class="wscp-img"/>
                            <div class="wscp-info">
                                <div class="wscp-badge blue">Fastest Delivery</div>
                                <div class="wscp-title">AeroLift Office Chair</div>
                                <div class="wscp-store">FurniHub Nigeria</div>
                                <div class="wscp-rating"><svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg> 4.5 <span>(634)</span></div>
                            </div>
                            <div class="wscp-price-col">
                                <div class="wscp-price">$199</div>
                                <div><span class="wscp-discount">23% OFF</span></div>
                            </div>
                            <div class="wscp-delivery-col">
                                <div class="wscp-delivery-time">1-3 days</div>
                                <div class="wscp-delivery-dest">Delivery to Lagos</div>
                            </div>
                        </div>

                    </div>
                </div>

                <!-- Right -->
                <div class="ws-right">
                    <div class="ws-title">Market Intelligence</div>
                    
                    <div class="wsr-section">
                        <div class="wsr-title">Price Trend</div>
                        <div class="wsr-metric"><span class="wsr-trend">↓ 12%</span></div>
                    </div>
                    
                    <div class="wsr-section" style="margin-top: 16px;">
                        <div class="wsr-title">Demand</div>
                        <div class="wsr-demand-desc">High</div>
                    </div>
                    
                    <div class="wsr-section" style="margin-top: 16px;">
                        <div class="wsr-title">Availability</div>
                        <div class="wsr-gauge">
                            82%
                        </div>
                    </div>
                </div>
            </div>

            <!-- SECTION 3: BUSINESS VALUE -->
            <div class="magic-flare-2"></div>

            <div class="bv-grid">
                <div class="bv-card">
                    <div class="bvc-val">12M+</div>
                    <div class="bvc-desc">Products indexed</div>
                </div>
                <div class="bv-card">
                    <div class="bvc-val">50K+</div>
                    <div class="bvc-desc">Connected stores</div>
                </div>
                <div class="bv-card">
                    <div class="bvc-val">280ms</div>
                    <div class="bvc-desc">Average search time</div>
                </div>
                <div class="bv-card">
                    <div class="bvc-val">98.8%</div>
                    <div class="bvc-desc">Search accuracy</div>
                </div>
            </div>

            <!-- SECTION 4: FINAL CTA -->
            <div class="magic-cta">
                <div class="mcta-title">Search smarter. Shop better.</div>
                <div class="mcta-subtitle">Join thousands of businesses already using Magic AI Search to discover the best products effortlessly.</div>
                
                <div class="mcta-btn">
                    Start Searching With AI
                </div>
            </div>
            
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
        
    print("Magic AI Search page successfully refined to 2-3 screens.")

if __name__ == '__main__':
    run()
