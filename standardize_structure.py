import bs4
import re

def run():
    with open('magic-ai-search.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = bs4.BeautifulSoup(html, 'html.parser')
    
    # We will replace the entire <main class="magic-wrapper"> with our updated version
    magic_main = soup.find('main', class_='magic-wrapper')
    
    if magic_main:
        # We will update the internal structure to clearly define the 5 storytelling sections
        # while keeping the continuous gradient flow.
        
        updated_content = """
        <div class="bg-grid"></div>
        
        <!-- 1. EDITORIAL HERO -->
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

        <!-- 2. HOW IT WORKS -->
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

        <!-- 3. THE PRODUCT EXPERIENCE -->
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

            <!-- 4. BUSINESS VALUE -->
            <div class="magic-business-value">
                <div class="mbv-header">Precision at scale.</div>
                <div class="mbv-desc">Nexmart processes millions of data points instantly, giving you the fastest, most accurate procurement intelligence on earth.</div>
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
            </div>
            
            <!-- 5. CTA TRANSITION INDICATOR -->
            <div style="position: absolute; bottom: 80px; left: 50%; transform: translateX(-50%); z-index: 30; opacity: 0.8; display: flex; flex-direction: column; align-items: center; gap: 8px;">
                <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#8A72FF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="animation: bounce 2s infinite;"><polyline points="7 13 12 18 17 13"></polyline><polyline points="7 6 12 11 17 6"></polyline></svg>
            </div>
        </div>
        """
        
        # We need to inject the CSS for the new .magic-business-value section
        style_addition = """
        .magic-business-value {
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            margin-top: 180px;
            padding-top: 100px;
            position: relative;
            z-index: 20;
        }
        
        .magic-business-value::before {
            content: '';
            position: absolute;
            top: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 800px;
            height: 1px;
            background: linear-gradient(90deg, transparent, rgba(138, 114, 255, 0.4), transparent);
        }

        .mbv-header {
            font-size: 3rem;
            font-weight: 700;
            letter-spacing: -0.04em;
            color: #FFFFFF;
            margin-bottom: 24px;
        }

        .mbv-desc {
            font-size: 1.25rem;
            color: #B3A4FF;
            max-width: 600px;
            line-height: 1.6;
            margin-bottom: 80px;
        }

        /* Update magic-stats to remove old top border since we moved it */
        .magic-stats {
            margin-top: 0 !important;
            padding-top: 0 !important;
            border-top: none !important;
        }
        """
        
        # Append to the existing custom style tag
        style_tag = soup.find('style')
        if style_tag and 'Deep Purple AI Palette' in style_tag.string:
            style_tag.string += style_addition
        
        # Replace the inner HTML of magic_main
        new_content_soup = bs4.BeautifulSoup(updated_content, 'html.parser')
        magic_main.clear()
        for child in new_content_soup.contents:
            magic_main.append(child)
            
        with open('magic-ai-search.html', 'w', encoding='utf-8') as f:
            f.write(str(soup))
            
        print("Standardized 5-section structure implemented.")
    else:
        print("Error: Could not find magic-wrapper")

if __name__ == '__main__':
    run()
