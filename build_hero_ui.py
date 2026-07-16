import bs4
import copy

def run():
    with open('agentic-commerce.html', 'r', encoding='utf-8') as f:
        soup = bs4.BeautifulSoup(f, 'html.parser')
    
    # ----------------------------------------------------
    # Inject Custom CSS for the Hero Mockup
    # ----------------------------------------------------
    style = soup.new_tag('style')
    style.string = """
    /* Hero Specific UI Variables */
    :root {
        --saas-bg: #0f172a; /* Slate 900 */
        --saas-panel: #1e293b; /* Slate 800 */
        --saas-border: #334155; /* Slate 700 */
        --saas-text-main: #f8fafc; /* Slate 50 */
        --saas-text-muted: #94a3b8; /* Slate 400 */
        --saas-accent: #3b82f6; /* Blue 500 */
        --saas-accent-glow: rgba(59, 130, 246, 0.5);
        --saas-success: #10b981; /* Emerald 500 */
    }

    .hero-saas-container {
        position: relative;
        padding: 120px 0 0 0;
        overflow: hidden;
        background: #f8fafc; /* very light background for the page */
        text-align: center;
    }

    .hero-text-wrap {
        max-width: 800px;
        margin: 0 auto 60px auto;
        position: relative;
        z-index: 10;
        padding: 0 24px;
    }
    
    .hero-title {
        font-size: 4rem;
        font-weight: 800;
        color: #0f172a;
        letter-spacing: -0.03em;
        line-height: 1.1;
        margin-bottom: 24px;
    }
    
    .hero-subtitle {
        font-size: 1.25rem;
        color: #475569;
        margin-bottom: 32px;
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
    }

    .saas-app-wrapper {
        width: 100%;
        max-width: 1400px;
        margin: 0 auto;
        height: 70vh; /* Takes up 70% of viewport */
        min-height: 600px;
        background: var(--saas-bg);
        border-top-left-radius: 24px;
        border-top-right-radius: 24px;
        border: 1px solid var(--saas-border);
        border-bottom: none;
        box-shadow: 0 -20px 60px rgba(15, 23, 42, 0.15), 0 0 0 1px rgba(255,255,255,0.05) inset;
        display: flex;
        flex-direction: column;
        overflow: hidden;
        position: relative;
        z-index: 5;
    }
    
    /* App Header */
    .saas-header {
        height: 60px;
        border-bottom: 1px solid var(--saas-border);
        display: flex;
        align-items: center;
        padding: 0 24px;
        justify-content: space-between;
        background: rgba(15, 23, 42, 0.8);
        backdrop-filter: blur(12px);
        z-index: 10;
    }
    .saas-header-dots {
        display: flex;
        gap: 8px;
    }
    .saas-dot {
        width: 12px;
        height: 12px;
        border-radius: 50%;
    }
    .saas-dot.red { background: #ef4444; }
    .saas-dot.yellow { background: #f59e0b; }
    .saas-dot.green { background: #10b981; }

    /* App Body */
    .saas-body {
        display: flex;
        flex: 1;
        overflow: hidden;
    }

    /* Sidebar */
    .saas-sidebar {
        width: 260px;
        border-right: 1px solid var(--saas-border);
        background: var(--saas-bg);
        padding: 24px;
        display: flex;
        flex-direction: column;
        gap: 24px;
    }
    .saas-nav-item {
        display: flex;
        align-items: center;
        gap: 12px;
        color: var(--saas-text-muted);
        font-size: 0.875rem;
        font-weight: 500;
        padding: 8px 12px;
        border-radius: 6px;
        transition: all 0.2s;
    }
    .saas-nav-item.active {
        background: rgba(59, 130, 246, 0.1);
        color: var(--saas-accent);
    }
    .saas-nav-title {
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        color: var(--saas-text-muted);
        opacity: 0.6;
        margin-bottom: 8px;
        padding-left: 12px;
    }

    /* Main Content */
    .saas-main {
        flex: 1;
        padding: 40px;
        display: flex;
        flex-direction: column;
        gap: 32px;
        overflow-y: auto;
        background: radial-gradient(circle at top right, rgba(30, 41, 59, 0.5), transparent 50%), var(--saas-bg);
    }

    /* Mission Prompt */
    .saas-prompt-box {
        background: var(--saas-panel);
        border: 1px solid var(--saas-border);
        border-radius: 12px;
        padding: 24px;
        box-shadow: 0 4px 24px rgba(0,0,0,0.2);
    }
    .saas-prompt-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 16px;
    }
    .saas-badge {
        background: rgba(16, 185, 129, 0.1);
        color: var(--saas-success);
        border: 1px solid rgba(16, 185, 129, 0.2);
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
        letter-spacing: 0.05em;
        display: flex;
        align-items: center;
        gap: 6px;
    }
    .saas-badge::before {
        content: '';
        width: 6px;
        height: 6px;
        background: var(--saas-success);
        border-radius: 50%;
        box-shadow: 0 0 8px var(--saas-success);
    }
    .saas-prompt-text {
        font-size: 1.5rem;
        color: var(--saas-text-main);
        font-weight: 500;
        line-height: 1.4;
    }
    .saas-prompt-cursor {
        display: inline-block;
        width: 2px;
        height: 1.2em;
        background: var(--saas-accent);
        vertical-align: middle;
        margin-left: 4px;
        animation: blink 1s step-end infinite;
    }

    /* Agent Grid */
    .saas-agent-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 16px;
    }
    .saas-agent-card {
        background: var(--saas-panel);
        border: 1px solid var(--saas-border);
        border-radius: 10px;
        padding: 16px;
        display: flex;
        flex-direction: column;
        gap: 12px;
        transition: transform 0.2s, border-color 0.2s;
    }
    .saas-agent-card:hover {
        border-color: var(--saas-accent);
        transform: translateY(-2px);
    }
    .saas-agent-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .saas-agent-name {
        font-size: 0.875rem;
        color: var(--saas-text-main);
        font-weight: 600;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .saas-agent-icon {
        width: 24px;
        height: 24px;
        background: rgba(255,255,255,0.05);
        border-radius: 6px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: var(--saas-accent);
    }
    .saas-agent-status {
        font-size: 0.75rem;
        color: var(--saas-text-muted);
        font-family: monospace;
    }
    .saas-agent-log {
        font-size: 0.75rem;
        color: var(--saas-text-muted);
        font-family: monospace;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        background: rgba(0,0,0,0.2);
        padding: 8px;
        border-radius: 4px;
        border: 1px solid rgba(255,255,255,0.02);
    }

    /* Data Table */
    .saas-table-wrap {
        background: var(--saas-panel);
        border: 1px solid var(--saas-border);
        border-radius: 12px;
        overflow: hidden;
    }
    .saas-table {
        width: 100%;
        border-collapse: collapse;
        text-align: left;
    }
    .saas-table th {
        padding: 12px 24px;
        font-size: 0.75rem;
        text-transform: uppercase;
        color: var(--saas-text-muted);
        font-weight: 600;
        border-bottom: 1px solid var(--saas-border);
        background: rgba(0,0,0,0.2);
    }
    .saas-table td {
        padding: 16px 24px;
        font-size: 0.875rem;
        color: var(--saas-text-main);
        border-bottom: 1px solid var(--saas-border);
    }
    .saas-table tr:last-child td { border-bottom: none; }
    .saas-table tr.highlight {
        background: rgba(59, 130, 246, 0.05);
    }
    
    @keyframes blink {
        0%, 100% { opacity: 1; }
        50% { opacity: 0; }
    }
    
    @media (max-width: 991px) {
        .saas-sidebar { display: none; }
        .hero-title { font-size: 3rem; }
    }
    @media (max-width: 767px) {
        .saas-agent-grid { grid-template-columns: 1fr; }
        .saas-prompt-text { font-size: 1.125rem; }
        .saas-main { padding: 20px; }
    }
    """
    
    # Check if this style already exists in head to avoid duplicates
    if not soup.head.find('style', string=lambda s: s and 'Hero Specific UI Variables' in s):
        soup.head.append(style)
        
    main = soup.find('main')
    
    # We are completely replacing the first section with our new Hero
    sections = main.find_all('section', recursive=False)
    if not sections:
        # If there are no direct sections (e.g. wrapped in a relative div from previous step), find the first section
        sections = main.find_all('section')
        
    hero_section = sections[0]
    hero_section.clear()
    # Remove any existing padding/classes to ensure a clean slate
    hero_section['class'] = ['hero-saas-container']
    
    hero_html = """
    <div class="hero-text-wrap">
        <h1 class="hero-title">Operate at the speed of thought.</h1>
        <p class="hero-subtitle">The Agentic Commerce engine translates your intent into parallel execution. Deploy specialized AI agents to discover, negotiate, and optimize your supply chain instantly.</p>
        <div style="display:flex; justify-content:center; gap:16px;">
            <a href="https://app.nexmartshop.ai/sign-up" class="button-main w-button" style="background-color:#0f172a; color:#fff;">Deploy Your Agents</a>
            <a href="#demo" class="button-main w-button" style="background-color:transparent; color:#0f172a; border: 1px solid #cbd5e1; box-shadow:none;">Watch Demo</a>
        </div>
    </div>
    
    <div class="saas-app-wrapper">
        <div class="saas-header">
            <div class="saas-header-dots">
                <div class="saas-dot red"></div>
                <div class="saas-dot yellow"></div>
                <div class="saas-dot green"></div>
            </div>
            <div style="color:var(--saas-text-muted); font-family:monospace; font-size:12px; display:flex; align-items:center; gap:8px;">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
                Secure Connection Established
            </div>
        </div>
        
        <div class="saas-body">
            <div class="saas-sidebar">
                <div>
                    <div class="saas-nav-title">Workspaces</div>
                    <div class="saas-nav-item active">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
                        Global Procurement
                    </div>
                    <div class="saas-nav-item">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg>
                        Retail Restock
                    </div>
                </div>
                
                <div style="margin-top: 16px;">
                    <div class="saas-nav-title">Missions</div>
                    <div class="saas-nav-item">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
                        Active <span style="margin-left:auto; background:var(--saas-accent); color:#fff; padding:2px 6px; border-radius:12px; font-size:10px;">3</span>
                    </div>
                    <div class="saas-nav-item">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        Completed
                    </div>
                </div>
                
                <div style="margin-top: auto; padding: 16px; background: rgba(0,0,0,0.2); border-radius: 8px; border: 1px solid var(--saas-border);">
                    <div style="font-size:10px; color:var(--saas-text-muted); font-family:monospace; margin-bottom:8px;">SYSTEM TELEMETRY</div>
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
                        <span style="font-size:12px; color:var(--saas-text-main);">Agent CPU</span>
                        <span style="font-size:12px; color:var(--saas-success);">42%</span>
                    </div>
                    <div style="width:100%; height:4px; background:rgba(255,255,255,0.1); border-radius:2px;"><div style="width:42%; height:100%; background:var(--saas-success); border-radius:2px;"></div></div>
                </div>
            </div>
            
            <div class="saas-main">
                <div class="saas-prompt-box">
                    <div class="saas-prompt-header">
                        <div style="font-family:monospace; font-size:12px; color:var(--saas-text-muted);">MISSION ID: NX-9482-B</div>
                        <div class="saas-badge">EXECUTING</div>
                    </div>
                    <div class="saas-prompt-text">
                        Find the most reliable supplier for 500 ergonomic office chairs under budget, delivered by Friday.<span class="saas-prompt-cursor"></span>
                    </div>
                </div>
                
                <div class="saas-agent-grid">
                    <div class="saas-agent-card">
                        <div class="saas-agent-header">
                            <div class="saas-agent-name"><div class="saas-agent-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg></div> Discovery</div>
                            <div class="saas-agent-status" style="color:var(--saas-success);">RUNNING</div>
                        </div>
                        <div class="saas-agent-log">> Indexed 14,024 global SKUs</div>
                    </div>
                    <div class="saas-agent-card">
                        <div class="saas-agent-header">
                            <div class="saas-agent-name"><div class="saas-agent-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="1" x2="12" y2="23"></line><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg></div> Pricing</div>
                            <div class="saas-agent-status" style="color:var(--saas-success);">RUNNING</div>
                        </div>
                        <div class="saas-agent-log">> Analyzing historic vendor data</div>
                    </div>
                    <div class="saas-agent-card">
                        <div class="saas-agent-header">
                            <div class="saas-agent-name"><div class="saas-agent-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path></svg></div> Logistics</div>
                            <div class="saas-agent-status" style="color:var(--saas-text-muted);">WAITING</div>
                        </div>
                        <div class="saas-agent-log">> Awaiting optimization vector</div>
                    </div>
                </div>
                
                <div class="saas-table-wrap">
                    <table class="saas-table">
                        <tr>
                            <th>Supplier Vector</th>
                            <th>Lead Time</th>
                            <th>Unit Price</th>
                            <th>Reliability Score</th>
                        </tr>
                        <tr class="highlight">
                            <td><div style="display:flex; align-items:center; gap:8px;"><div style="width:8px;height:8px;border-radius:50%;background:var(--saas-accent);"></div> <strong>Herman Miller Direct (Recommended)</strong></div></td>
                            <td>3 Days (Air)</td>
                            <td style="color:var(--saas-success); font-family:monospace; font-weight:600;">$940.00 (-15%)</td>
                            <td>99.2%</td>
                        </tr>
                        <tr>
                            <td>OfficeDepot Wholesale</td>
                            <td>5 Days (Ground)</td>
                            <td style="font-family:monospace;">$1,100.00</td>
                            <td>94.5%</td>
                        </tr>
                        <tr>
                            <td>Steelcase Global Logistics</td>
                            <td>2 Days (Air)</td>
                            <td style="font-family:monospace;">$1,150.00</td>
                            <td>98.1%</td>
                        </tr>
                    </table>
                </div>
            </div>
        </div>
    </div>
    """
    
    hero_section.append(bs4.BeautifulSoup(hero_html, 'html.parser'))
    
    with open('agentic-commerce.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    print("Hero successfully rebuilt as a high-fidelity SaaS application interface.")

if __name__ == '__main__':
    run()
