import bs4

def redesign_dashboard():
    with open('advertiser-tracker.html', 'r', encoding='utf-8') as f:
        soup = bs4.BeautifulSoup(f.read(), 'html.parser')

    # Find the main wrapper for the component
    bridge_container = soup.find('div', class_='v1-bridge-container')
    app_env = soup.find('div', class_='v1-app-environment')

    if not bridge_container or not app_env:
        print("Could not find the target containers!")
        return

    # NEW HTML for bridge container (Search Bar + Agent Cards)
    new_bridge_html = """
    <div class="v1-bridge-container">
        <!-- New Search Bar -->
        <div class="ad-search-bar">
            <div class="ad-search-icon">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#10B981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path>
                    <polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline>
                    <line x1="12" y1="22.08" x2="12" y2="12"></line>
                </svg>
            </div>
            <div class="ad-search-input">
                <span class="ad-typewriter">Analyze top-performing competitor campaigns in Q3</span>
                <span class="ad-cursor"></span>
            </div>
        </div>

        <!-- New Agent Cards -->
        <div class="ad-agent-cards">
            <!-- Card 1 -->
            <div class="ad-agent-card">
                <div class="ad-card-header">
                    <div class="ad-card-title-group">
                        <div class="ad-icon-box"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#10B981" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><circle cx="12" cy="12" r="6"></circle><circle cx="12" cy="12" r="2"></circle></svg></div>
                        <span>Campaign Detection</span>
                    </div>
                    <div class="ad-status-pill"><span class="ad-pulse-dot"></span>RUNNING</div>
                </div>
                <div class="ad-card-log">
                    &gt; Scanning global ad networks...<br>
                    &gt; Found 12,402 active creatives.<br>
                    &gt; Filtering by campaign category...
                </div>
                <div class="ad-card-footer">
                    <span>2.4s <span class="ad-emerald">Real-time</span></span>
                </div>
            </div>

            <!-- Card 2 -->
            <div class="ad-agent-card">
                <div class="ad-card-header">
                    <div class="ad-card-title-group">
                        <div class="ad-icon-box"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#10B981" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg></div>
                        <span>Creative Analysis</span>
                    </div>
                    <div class="ad-status-pill"><span class="ad-pulse-dot"></span>RUNNING</div>
                </div>
                <div class="ad-card-log">
                    &gt; Extracting campaign messaging...<br>
                    &gt; Detecting winning creative formats...<br>
                    &gt; Identifying emotional triggers...
                </div>
                <div class="ad-card-footer">
                    <span>3.1s <span class="ad-emerald">Deep Analysis</span></span>
                </div>
            </div>

            <!-- Card 3 -->
            <div class="ad-agent-card">
                <div class="ad-card-header">
                    <div class="ad-card-title-group">
                        <div class="ad-icon-box"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#10B981" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg></div>
                        <span>Spend Intelligence</span>
                    </div>
                    <div class="ad-status-pill"><span class="ad-pulse-dot"></span>RUNNING</div>
                </div>
                <div class="ad-card-log">
                    &gt; Modeling competitor budgets...<br>
                    &gt; Predicting spend trajectory...<br>
                    &gt; Estimating ROI signals...
                </div>
                <div class="ad-card-footer">
                    <span>4.7s <span class="ad-emerald">Predictive</span></span>
                </div>
            </div>
        </div>
    </div>
    """

    new_app_env_html = """
    <div class="v1-app-environment">
        <div class="ambient-flare-left"></div>
        <div class="ambient-flare-right"></div>
        
        <div class="ad-campaign-feed">
            <div class="ad-feed-header">
                <div class="ad-fh-left">
                    <h2>Live Campaign Feed</h2>
                    <div class="ad-updated">
                        <span class="ad-pulse-dot"></span> UPDATED 3 MINUTES AGO
                    </div>
                </div>
                <a href="#" class="ad-fh-link">View All Campaigns &rarr;</a>
            </div>

            <div class="ad-table-header">
                <div class="ad-th-brand">BRAND</div>
                <div class="ad-th-campaign">CAMPAIGN</div>
                <div class="ad-th-platform">PLATFORM</div>
                <div class="ad-th-spend">EST. SPEND</div>
                <div class="ad-th-creative">CREATIVE TYPE</div>
                <div class="ad-th-status">STATUS</div>
                <div class="ad-th-insight">AI INSIGHT</div>
            </div>

            <div class="ad-table-rows">
                <!-- ROW 1 -->
                <div class="ad-row">
                    <div class="ad-td-brand">
                        <div class="ad-brand-logo"><svg viewBox="0 0 24 24" fill="white"><path d="M22.5 7.15c-1.35 1.55-3.32 2.76-6.14 2.87-4.22.18-8.12-1.92-12.87-5.5C2.65 3.82 2.1 4.8 2.8 5.6c4.07 4.67 9.55 7.75 14.88 8.05 1.95.1 3.52-.3 4.82-1.07V7.15z"/></svg></div>
                        <span>Nike</span>
                    </div>
                    <div class="ad-td-campaign">
                        <div class="ad-c-name">Air Max Launch</div>
                        <div class="ad-c-sub">Launched 28 days ago</div>
                    </div>
                    <div class="ad-td-platform">
                        <div class="ad-plat-icons">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg>
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33A2.78 2.78 0 0 0 3.4 19c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.25 29 29 0 0 0-.46-5.33z"></path><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"></polygon></svg>
                        </div>
                        <div class="ad-c-sub">Global Omni-channel</div>
                    </div>
                    <div class="ad-td-spend">
                        <div class="ad-c-name">$4.2M</div>
                        <div class="ad-c-sub ad-emerald">&uarr; 18% vs last 30d</div>
                    </div>
                    <div class="ad-td-creative">
                        <div class="ad-thumb video-thumb">
                            <div class="play-btn"></div>
                        </div>
                        <div class="ad-cr-text">
                            <div class="ad-c-name">Video & AR</div>
                            <div class="ad-c-sub">15 Variations</div>
                        </div>
                    </div>
                    <div class="ad-td-status">
                        <div class="ad-status-badge">ACTIVE</div>
                        <div class="ad-c-sub">High Velocity</div>
                    </div>
                    <div class="ad-td-insight">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#10B981" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path></svg>
                        <span>Scaling rapidly across EU & Southeast Asia</span>
                    </div>
                </div>
                
                <!-- ROW 2 -->
                <div class="ad-row">
                    <div class="ad-td-brand">
                        <div class="ad-brand-logo"><svg viewBox="0 0 24 24" fill="white"><path d="M17.05 20.28c-.98.68-2.05.8-3.08.35-1.09-.46-2.09-.48-3.24 0-1.44.62-2.2.44-3.06-.35C2.79 15.25 3.51 7.59 9.05 7.31c1.35.05 2.26.68 2.85.68.61 0 1.74-.75 3.3-.65 1.5.06 2.65.65 3.42 1.6-3 1.7-2.48 5.67.57 6.81-.66 1.72-1.44 3.44-2.14 4.53zM12.03 7.25c-.15-2.23 1.66-4.07 3.74-4.25.32 2.22-1.74 4.19-3.74 4.25z"/></svg></div>
                        <span>Apple</span>
                    </div>
                    <div class="ad-td-campaign">
                        <div class="ad-c-name">Privacy on iPhone</div>
                        <div class="ad-c-sub">Launched 42 days ago</div>
                    </div>
                    <div class="ad-td-platform">
                        <div class="ad-plat-icons">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg>
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                        </div>
                        <div class="ad-c-sub">Targeted Social</div>
                    </div>
                    <div class="ad-td-spend">
                        <div class="ad-c-name">$2.8M</div>
                        <div class="ad-c-sub ad-emerald">&uarr; 9% vs last 30d</div>
                    </div>
                    <div class="ad-td-creative">
                        <div class="ad-thumb carousel-thumb"></div>
                        <div class="ad-cr-text">
                            <div class="ad-c-name">Carousel Ads</div>
                            <div class="ad-c-sub">8 Variations</div>
                        </div>
                    </div>
                    <div class="ad-td-status">
                        <div class="ad-status-badge">ACTIVE</div>
                        <div class="ad-c-sub">Steady</div>
                    </div>
                    <div class="ad-td-insight">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#10B981" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path></svg>
                        <span>High engagement among 25-34 audience</span>
                    </div>
                </div>
                
                <!-- ROW 3 -->
                <div class="ad-row">
                    <div class="ad-td-brand">
                        <div class="ad-brand-logo blue-bg">S</div>
                        <span>Samsung</span>
                    </div>
                    <div class="ad-td-campaign">
                        <div class="ad-c-name">Galaxy AI</div>
                        <div class="ad-c-sub">Launched 19 days ago</div>
                    </div>
                    <div class="ad-td-platform">
                        <div class="ad-plat-icons">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="15" rx="2" ry="2"></rect><polyline points="17 2 12 7 7 2"></polyline></svg>
                        </div>
                        <div class="ad-c-sub">Connected TV</div>
                    </div>
                    <div class="ad-td-spend">
                        <div class="ad-c-name">$3.1M</div>
                        <div class="ad-c-sub ad-emerald">&uarr; 24% vs last 30d</div>
                    </div>
                    <div class="ad-td-creative">
                        <div class="ad-thumb tv-thumb">
                            <div class="play-btn"></div>
                        </div>
                        <div class="ad-cr-text">
                            <div class="ad-c-name">Interactive Video</div>
                            <div class="ad-c-sub">12 Variations</div>
                        </div>
                    </div>
                    <div class="ad-td-status">
                        <div class="ad-status-badge">ACTIVE</div>
                        <div class="ad-c-sub">Rising Fast</div>
                    </div>
                    <div class="ad-td-insight">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#10B981" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path></svg>
                        <span>Creative performance accelerating</span>
                    </div>
                </div>
                
                <!-- ROW 4 -->
                <div class="ad-row">
                    <div class="ad-td-brand">
                        <div class="ad-brand-logo black-bg">Sony</div>
                        <span>Sony</span>
                    </div>
                    <div class="ad-td-campaign">
                        <div class="ad-c-name">PlayStation 6</div>
                        <div class="ad-c-sub">Launched 7 days ago</div>
                    </div>
                    <div class="ad-td-platform">
                        <div class="ad-plat-icons">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect></svg>
                        </div>
                        <div class="ad-c-sub">Search & Display</div>
                    </div>
                    <div class="ad-td-spend">
                        <div class="ad-c-name">$1.5M</div>
                        <div class="ad-c-sub ad-emerald">&uarr; 12% vs last 30d</div>
                    </div>
                    <div class="ad-td-creative">
                        <div class="ad-thumb static-thumb"></div>
                        <div class="ad-cr-text">
                            <div class="ad-c-name">Static & GIF</div>
                            <div class="ad-c-sub">10 Variations</div>
                        </div>
                    </div>
                    <div class="ad-td-status">
                        <div class="ad-status-badge">ACTIVE</div>
                        <div class="ad-c-sub">Low Competition</div>
                    </div>
                    <div class="ad-td-insight">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#10B981" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path></svg>
                        <span>Opportunity to expand into YouTube</span>
                    </div>
                </div>

            </div>
            
            <div class="ad-carousel-nav">
                <button>&lsaquo;</button>
                <div class="ad-dots">
                    <span class="active"></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
                <button>&rsaquo;</button>
            </div>
            
        </div>
        
        <div class="ad-footer-badge">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#10B981" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
            Data powered by 50M+ daily ad signals across 15+ platforms
        </div>
    </div>
    """

    new_css = """
    /* Advertiser Tracker Redesign CSS */
    .ad-search-bar {
        display: flex;
        align-items: center;
        background: rgba(20, 20, 20, 0.7);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(16, 185, 129, 0.3);
        border-radius: 40px;
        padding: 16px 24px;
        max-width: 700px;
        margin: 0 auto 40px auto;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.4), 0 0 30px rgba(16, 185, 129, 0.1);
        gap: 16px;
    }
    .ad-search-icon { display: flex; align-items: center; justify-content: center; }
    .ad-search-input { display: flex; align-items: center; font-size: 1.1rem; color: #fff; font-family: 'Inter', sans-serif; font-weight: 400; }
    .ad-typewriter { opacity: 0.9; }
    .ad-cursor { width: 2px; height: 1.2rem; background-color: #10B981; margin-left: 4px; animation: blink 1s step-start infinite; }
    
    .ad-agent-cards { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; max-width: 1100px; margin: 0 auto; margin-bottom: 40px; }
    .ad-agent-card {
        background: rgba(18, 18, 18, 0.8);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        padding: 24px;
        transition: transform 0.3s ease, border-color 0.3s ease;
        display: flex; flex-direction: column; gap: 16px;
    }
    .ad-agent-card:hover { transform: translateY(-5px); border-color: rgba(16, 185, 129, 0.3); }
    .ad-card-header { display: flex; justify-content: space-between; align-items: center; }
    .ad-card-title-group { display: flex; align-items: center; gap: 12px; font-weight: 600; color: #fff; font-size: 1rem; }
    .ad-icon-box { background: rgba(16, 185, 129, 0.1); padding: 8px; border-radius: 8px; display: flex; align-items: center; justify-content: center; }
    .ad-status-pill { display: flex; align-items: center; gap: 6px; background: rgba(16, 185, 129, 0.15); color: #10B981; font-size: 0.75rem; padding: 4px 10px; border-radius: 20px; font-weight: 600; letter-spacing: 0.5px; }
    .ad-pulse-dot { width: 6px; height: 6px; background: #10B981; border-radius: 50%; animation: pulse 2s infinite; }
    .ad-card-log { font-family: 'JetBrains Mono', 'Fira Code', monospace; font-size: 0.85rem; color: #a1a1aa; line-height: 1.6; min-height: 70px;}
    .ad-card-footer { font-size: 0.85rem; color: #71717a; border-top: 1px solid rgba(255,255,255,0.05); padding-top: 12px; }
    .ad-emerald { color: #10B981; font-weight: 500; }

    .ad-campaign-feed {
        background: rgba(15, 15, 15, 0.8);
        backdrop-filter: blur(24px);
        border: 1px solid rgba(16, 185, 129, 0.2);
        border-radius: 24px;
        padding: 32px;
        max-width: 1200px;
        margin: 0 auto;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(255,255,255,0.05);
    }
    .ad-feed-header { display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 24px; }
    .ad-fh-left h2 { font-size: 1.5rem; color: #fff; font-weight: 600; margin-bottom: 8px; }
    .ad-updated { display: flex; align-items: center; gap: 8px; font-size: 0.75rem; color: #10B981; font-weight: 600; letter-spacing: 1px; }
    .ad-fh-link { color: #10B981; font-size: 0.9rem; text-decoration: none; font-weight: 500; }
    .ad-fh-link:hover { text-decoration: underline; }

    .ad-table-header { display: grid; grid-template-columns: 1.2fr 1.5fr 1.2fr 1fr 1.2fr 0.8fr 1.8fr; gap: 16px; padding-bottom: 16px; border-bottom: 1px solid rgba(255,255,255,0.1); font-size: 0.7rem; color: #71717a; font-weight: 600; letter-spacing: 0.5px; }
    .ad-table-rows { display: flex; flex-direction: column; }
    .ad-row { display: grid; grid-template-columns: 1.2fr 1.5fr 1.2fr 1fr 1.2fr 0.8fr 1.8fr; gap: 16px; align-items: center; padding: 20px 0; border-bottom: 1px solid rgba(255,255,255,0.05); transition: background 0.2s ease; }
    .ad-row:hover { background: rgba(255,255,255,0.02); }
    
    .ad-td-brand { display: flex; align-items: center; gap: 12px; color: #fff; font-weight: 600; font-size: 1.05rem; }
    .ad-brand-logo { width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; background: #000; border-radius: 6px; }
    .ad-brand-logo svg { width: 20px; height: 20px; }
    .blue-bg { background: #1428A0; color: white; font-size: 14px; font-weight: bold; }
    .black-bg { background: #000; color: white; font-size: 10px; font-weight: bold; font-family: serif;}

    .ad-c-name { color: #fff; font-weight: 500; font-size: 0.95rem; margin-bottom: 4px; }
    .ad-c-sub { color: #a1a1aa; font-size: 0.8rem; }
    .ad-plat-icons { display: flex; gap: 8px; color: #60a5fa; margin-bottom: 4px; }
    .ad-td-spend .ad-c-name { font-size: 1.05rem; }
    
    .ad-td-creative { display: flex; align-items: center; gap: 12px; }
    .ad-thumb { width: 48px; height: 32px; border-radius: 4px; background: #333; position: relative; overflow: hidden; }
    .video-thumb { background: linear-gradient(45deg, #1f2937, #4b5563); }
    .carousel-thumb { background: linear-gradient(to right, #374151 50%, #1f2937 50%); }
    .tv-thumb { background: linear-gradient(135deg, #0f172a, #1e293b); border: 1px solid #334155; }
    .static-thumb { background: linear-gradient(180deg, #111827, #374151); }
    .play-btn { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 0; height: 0; border-top: 4px solid transparent; border-bottom: 4px solid transparent; border-left: 6px solid #fff; }

    .ad-status-badge { display: inline-block; background: rgba(16, 185, 129, 0.2); color: #10B981; font-size: 0.7rem; font-weight: 700; padding: 4px 8px; border-radius: 4px; margin-bottom: 4px; border: 1px solid rgba(16, 185, 129, 0.4); }
    .ad-td-insight { display: flex; align-items: flex-start; gap: 8px; color: #fff; font-size: 0.9rem; line-height: 1.4; }
    
    .ad-carousel-nav { display: flex; justify-content: center; align-items: center; gap: 16px; margin-top: 24px; }
    .ad-carousel-nav button { background: rgba(255,255,255,0.05); border: none; color: #fff; width: 32px; height: 32px; border-radius: 50%; cursor: pointer; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; transition: background 0.2s; }
    .ad-carousel-nav button:hover { background: rgba(255,255,255,0.1); }
    .ad-dots { display: flex; gap: 8px; }
    .ad-dots span { width: 6px; height: 6px; border-radius: 50%; background: rgba(255,255,255,0.2); transition: background 0.2s; }
    .ad-dots span.active { background: #10B981; width: 8px; height: 8px; margin-top: -1px; }
    
    .ad-footer-badge { display: flex; justify-content: center; align-items: center; gap: 8px; color: #71717a; font-size: 0.85rem; margin-top: 32px; }

    @keyframes blink { 50% { opacity: 0; } }
    @keyframes pulse { 0% { transform: scale(1); opacity: 1; } 50% { transform: scale(1.5); opacity: 0.5; } 100% { transform: scale(1); opacity: 1; } }

    @media (max-width: 1024px) {
        .ad-agent-cards { grid-template-columns: 1fr; }
        .ad-table-header, .ad-row { grid-template-columns: 1fr 1fr 1fr 1fr; gap: 10px; }
        .ad-th-brand, .ad-td-brand, .ad-th-insight, .ad-td-insight, .ad-th-creative, .ad-td-creative { display: none; }
    }
    """

    # Inject the new HTML
    bridge_container.replace_with(bs4.BeautifulSoup(new_bridge_html, 'html.parser'))
    app_env.replace_with(bs4.BeautifulSoup(new_app_env_html, 'html.parser'))

    # Inject the new CSS into the style tag
    style_tag = soup.find('style')
    if style_tag:
        style_tag.append(new_css)
    else:
        # if no style tag exists, add it before closing </main>
        main_tag = soup.find('main')
        if main_tag:
            new_style_tag = soup.new_tag('style')
            new_style_tag.string = new_css
            main_tag.append(new_style_tag)

    with open('advertiser-tracker.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print("Dashboard Redesign completed successfully.")

if __name__ == "__main__":
    redesign_dashboard()
