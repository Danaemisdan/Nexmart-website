import bs4

with open('advertiser-tracker.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = bs4.BeautifulSoup(html, 'html.parser')

# Update Title
if soup.title:
    soup.title.string = "Nexmart - Advertiser Tracker"

# Build Advertiser Tracker Content
content_html = """
<div class="semantic-advertiser-tracker-wrapper" style="width: 100%; display: flex; flex-direction: column; font-family: 'Inter', system-ui, -apple-system, sans-serif; background-color: #030303; color: #fff; overflow-x: hidden;">
    
    <!-- HERO SECTION: THE INTERCEPT -->
    <section style="position: relative; min-height: 100vh; display: flex; align-items: center; padding: 180px 5% 120px 5%; overflow: hidden;">
        <!-- Selective Emerald Glow -->
        <div style="position: absolute; top: 20%; right: 0; width: 600px; height: 600px; background: radial-gradient(circle, rgba(16, 185, 129, 0.08) 0%, transparent 60%); z-index: 0; filter: blur(40px);"></div>
        <div style="position: absolute; bottom: 0; left: 10%; width: 500px; height: 500px; background: radial-gradient(circle, rgba(255, 255, 255, 0.03) 0%, transparent 60%); z-index: 0; filter: blur(40px);"></div>

        <div style="position: relative; z-index: 1; max-width: 1400px; margin: 0 auto; width: 100%; display: grid; grid-template-columns: 1fr 1fr; gap: 64px; align-items: center;">
            
            <!-- Hero Left: Typography & Philosophy -->
            <div style="animation: fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;">
                <div style="font-family: 'JetBrains Mono', monospace; font-size: 11px; text-transform: uppercase; letter-spacing: 0.15em; color: #10B981; margin-bottom: 32px; display: flex; align-items: center; gap: 12px;">
                    <span style="width: 6px; height: 6px; background: #10B981; border-radius: 50%; animation: pulse-glow 2s infinite;"></span>
                    [ LIVE INTERCEPT // NETWORK SECURE ]
                </div>
                
                <h1 style="font-size: clamp(3.5rem, 5vw, 5.5rem); font-weight: 800; letter-spacing: -0.04em; line-height: 1.05; margin-bottom: 32px; background: linear-gradient(180deg, #FFFFFF 0%, rgba(255,255,255,0.6) 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                    Intelligence<br>Over Guesswork.
                </h1>
                
                <p style="font-size: clamp(1.125rem, 1.5vw, 1.25rem); color: rgba(255,255,255,0.7); max-width: 540px; line-height: 1.6; margin-bottom: 40px;">
                    Stop funding blind experiments. Intercept competitor spend, decode their winning creatives, and scale with verified financial truth.
                </p>

                <!-- Editorial Statement -->
                <div style="padding-left: 24px; border-left: 2px solid rgba(255,255,255,0.15);">
                    <p style="font-size: 1rem; color: #fff; font-weight: 500; font-style: italic; margin: 0; letter-spacing: -0.01em;">
                        "The market rewards those who know. Stop guessing. Start intercepting."
                    </p>
                </div>
            </div>

            <!-- Hero Right: The AI Scan Sequence -->
            <div style="position: relative; height: 500px; display: flex; justify-content: center; align-items: center; perspective: 1000px; animation: fadeInUp 1s cubic-bezier(0.16, 1, 0.3, 1) 0.2s forwards; opacity: 0;">
                
                <!-- Floating Intercept Assets -->
                <div style="position: absolute; width: 100%; height: 100%; background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 24px; overflow: hidden; box-shadow: 0 40px 100px rgba(0,0,0,0.5);">
                    <!-- Mosaic of blurred ads -->
                    <div style="position: absolute; inset: 0; display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; padding: 24px; opacity: 0.5;">
                        <div style="background: rgba(255,255,255,0.1); border-radius: 12px; filter: blur(4px);"></div>
                        <div style="background: rgba(255,255,255,0.05); border-radius: 12px; filter: blur(8px);"></div>
                        <div style="background: rgba(255,255,255,0.08); border-radius: 12px; filter: blur(6px);"></div>
                        <div style="background: rgba(255,255,255,0.04); border-radius: 12px; filter: blur(10px);"></div>
                        <div style="background: rgba(255,255,255,0.12); border-radius: 12px; filter: blur(2px);"></div>
                        <div style="background: rgba(255,255,255,0.06); border-radius: 12px; filter: blur(8px);"></div>
                    </div>
                    
                    <!-- The Scan Line -->
                    <div class="hero-scan-line" style="position: absolute; top: 0; left: 0; right: 0; height: 100%; pointer-events: none;">
                        <div style="width: 100%; height: 2px; background: #10B981; box-shadow: 0 0 20px 4px rgba(16, 185, 129, 0.5); position: absolute; top: 0;"></div>
                        <div style="width: 100%; height: 100px; background: linear-gradient(180deg, rgba(16, 185, 129, 0.1) 0%, transparent 100%);"></div>
                    </div>

                    <!-- Decoded Intel Overlay (Appears as scan passes) -->
                    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 80%; background: rgba(10,10,10,0.9); backdrop-filter: blur(20px); border: 1px solid rgba(255,255,255,0.1); border-radius: 16px; padding: 32px; box-shadow: 0 20px 60px rgba(0,0,0,0.8);">
                        <div style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #10B981; margin-bottom: 12px; letter-spacing: 0.1em;">SIGNAL DECODED</div>
                        <div style="display: flex; justify-content: space-between; align-items: flex-end;">
                            <div>
                                <div style="font-size: 14px; color: rgba(255,255,255,0.5); margin-bottom: 4px;">Est. 24h Spend</div>
                                <div style="font-size: 32px; font-weight: 700; color: #fff;">$4,250</div>
                            </div>
                            <div style="text-align: right;">
                                <div style="font-size: 14px; color: rgba(255,255,255,0.5); margin-bottom: 4px;">Trajectory</div>
                                <div style="font-size: 14px; color: #10B981; font-weight: 600;">+12% Scaling</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- SECTION 2: THE WORKSPACE (Intelligence Dossier) -->
    <section style="padding: 120px 5%; background: #030303; border-top: 1px solid rgba(255,255,255,0.03);">
        <div style="max-width: 1400px; margin: 0 auto;">
            
            <div style="margin-bottom: 64px; text-align: center;">
                <h2 style="font-size: clamp(2rem, 3vw, 3rem); font-weight: 700; letter-spacing: -0.03em; margin-bottom: 24px;">The Competitor Matrix</h2>
                <p style="font-size: 1.125rem; color: rgba(255,255,255,0.6); max-width: 600px; margin: 0 auto;">A sprawling intelligence dossier, not a generic dashboard. See everything they are doing in one place.</p>
            </div>

            <!-- Full-width Dark Glass Canvas -->
            <div style="background: rgba(255,255,255,0.01); border: 1px solid rgba(255,255,255,0.05); border-radius: 24px; overflow: hidden; display: flex; flex-direction: column;">
                
                <!-- Terminal Header -->
                <div style="background: #0A0A0A; border-bottom: 1px solid rgba(255,255,255,0.05); padding: 20px 32px; display: flex; justify-content: space-between; align-items: center;">
                    <div style="display: flex; align-items: center; gap: 16px;">
                        <div style="width: 32px; height: 32px; border-radius: 8px; background: rgba(255,255,255,0.05); display: flex; align-items: center; justify-content: center;">
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>
                        </div>
                        <div style="font-family: 'JetBrains Mono', monospace; font-size: 12px; color: rgba(255,255,255,0.7); letter-spacing: 0.05em;">TARGET: APEX ATHLETICS</div>
                    </div>
                    <div style="font-family: 'JetBrains Mono', monospace; font-size: 12px; color: #10B981; background: rgba(16, 185, 129, 0.1); padding: 4px 12px; border-radius: 100px;">
                        CONNECTION SECURE
                    </div>
                </div>

                <div style="display: grid; grid-template-columns: 1fr 340px; gap: 0;">
                    
                    <!-- Main Area: Spend River & Ad Deconstruction -->
                    <div style="padding: 40px; border-right: 1px solid rgba(255,255,255,0.03);">
                        
                        <!-- The Spend River Timeline -->
                        <div style="margin-bottom: 48px;">
                            <h3 style="font-size: 1rem; font-weight: 600; color: #fff; margin-bottom: 24px;">30-Day Spend Intensity</h3>
                            <div style="height: 120px; width: 100%; border-bottom: 1px solid rgba(255,255,255,0.1); position: relative; display: flex; align-items: flex-end; padding-bottom: 8px; gap: 4px;">
                                <!-- Mock Bars -->
                                <div style="flex: 1; height: 20%; background: rgba(255,255,255,0.05); border-radius: 4px 4px 0 0;"></div>
                                <div style="flex: 1; height: 25%; background: rgba(255,255,255,0.05); border-radius: 4px 4px 0 0;"></div>
                                <div style="flex: 1; height: 22%; background: rgba(255,255,255,0.05); border-radius: 4px 4px 0 0;"></div>
                                <div style="flex: 1; height: 40%; background: rgba(255,255,255,0.1); border-radius: 4px 4px 0 0;"></div>
                                <div style="flex: 1; height: 65%; background: rgba(255,255,255,0.2); border-radius: 4px 4px 0 0;"></div>
                                <div style="flex: 1; height: 85%; background: rgba(16, 185, 129, 0.4); border-radius: 4px 4px 0 0; position: relative;">
                                    <div style="position: absolute; top: -8px; left: 50%; transform: translateX(-50%); width: 8px; height: 8px; background: #10B981; border-radius: 50%; box-shadow: 0 0 12px #10B981;"></div>
                                </div>
                                <div style="flex: 1; height: 90%; background: rgba(16, 185, 129, 0.6); border-radius: 4px 4px 0 0;"></div>
                                <div style="flex: 1; height: 100%; background: #10B981; border-radius: 4px 4px 0 0; position: relative; box-shadow: 0 0 24px rgba(16,185,129,0.3);">
                                    <div style="position: absolute; top: -32px; left: 50%; transform: translateX(-50%); font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #10B981; white-space: nowrap;">NEW AD</div>
                                </div>
                                <div style="flex: 1; height: 95%; background: rgba(16, 185, 129, 0.8); border-radius: 4px 4px 0 0;"></div>
                            </div>
                        </div>

                        <!-- Creative Deconstruction -->
                        <div>
                            <h3 style="font-size: 1rem; font-weight: 600; color: #fff; margin-bottom: 24px;">Creative Deconstruction</h3>
                            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px;">
                                <div style="background: rgba(0,0,0,0.5); border: 1px solid rgba(255,255,255,0.05); border-radius: 16px; padding: 24px;">
                                    <div style="aspect-ratio: 16/9; background: rgba(255,255,255,0.05); border-radius: 8px; margin-bottom: 16px; position: relative; display: flex; align-items: center; justify-content: center;">
                                        <div style="font-family: 'JetBrains Mono', monospace; color: rgba(255,255,255,0.3); font-size: 12px;">CREATIVE_ASSET_1</div>
                                    </div>
                                    <div style="display: flex; flex-direction: column; gap: 8px;">
                                        <div style="display: flex; justify-content: space-between; font-size: 13px;">
                                            <span style="color: rgba(255,255,255,0.5);">HOOK TYPE</span>
                                            <span style="color: #fff; font-weight: 500;">Scarcity / Urgency</span>
                                        </div>
                                        <div style="display: flex; justify-content: space-between; font-size: 13px;">
                                            <span style="color: rgba(255,255,255,0.5);">LIFESPAN</span>
                                            <span style="color: #fff; font-weight: 500;">45 Days</span>
                                        </div>
                                    </div>
                                </div>
                                <div style="background: rgba(0,0,0,0.5); border: 1px solid rgba(255,255,255,0.05); border-radius: 16px; padding: 24px;">
                                    <div style="aspect-ratio: 16/9; background: rgba(255,255,255,0.05); border-radius: 8px; margin-bottom: 16px; position: relative; display: flex; align-items: center; justify-content: center;">
                                        <div style="font-family: 'JetBrains Mono', monospace; color: rgba(255,255,255,0.3); font-size: 12px;">CREATIVE_ASSET_2</div>
                                    </div>
                                    <div style="display: flex; flex-direction: column; gap: 8px;">
                                        <div style="display: flex; justify-content: space-between; font-size: 13px;">
                                            <span style="color: rgba(255,255,255,0.5);">HOOK TYPE</span>
                                            <span style="color: #fff; font-weight: 500;">Social Proof</span>
                                        </div>
                                        <div style="display: flex; justify-content: space-between; font-size: 13px;">
                                            <span style="color: rgba(255,255,255,0.5);">LIFESPAN</span>
                                            <span style="color: #fff; font-weight: 500;">12 Days</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                    </div>

                    <!-- Right Sidebar: AI Recommendations -->
                    <div style="background: rgba(0,0,0,0.3); padding: 40px 32px;">
                        <h3 style="font-size: 1rem; font-weight: 600; color: #fff; margin-bottom: 32px; display: flex; align-items: center; gap: 12px;">
                            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#10B981" stroke-width="2"><path d="M12 2v20"/><path d="m17 5 5 5-5 5"/><path d="m7 19-5-5 5-5"/></svg>
                            AI Recommendations
                        </h3>
                        
                        <div style="display: flex; flex-direction: column; gap: 24px;">
                            <!-- Alert 1 -->
                            <div style="background: rgba(16, 185, 129, 0.05); border: 1px solid rgba(16, 185, 129, 0.2); border-radius: 12px; padding: 20px;">
                                <div style="font-family: 'JetBrains Mono', monospace; font-size: 10px; color: #10B981; margin-bottom: 8px; font-weight: 600;">ACTION RECOMMENDED</div>
                                <p style="font-size: 13px; color: rgba(255,255,255,0.8); line-height: 1.5; margin: 0;">
                                    Competitor has doubled spend on "Performance Jogger" in the last 48 hours. Consider scaling similar inventory immediately to capture trailing demand.
                                </p>
                            </div>
                            
                            <!-- Alert 2 -->
                            <div style="background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.05); border-radius: 12px; padding: 20px;">
                                <div style="font-family: 'JetBrains Mono', monospace; font-size: 10px; color: rgba(255,255,255,0.5); margin-bottom: 8px;">OBSERVATION</div>
                                <p style="font-size: 13px; color: rgba(255,255,255,0.6); line-height: 1.5; margin: 0;">
                                    "Core Hoodie" campaigns have reduced spend by 30% over 7 days. High probability of creative fatigue or inventory depletion.
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- SECTION 3: STORY BLOCKS (The AI Edge) -->
    <section style="padding: 120px 5%; background: #000;">
        <div style="max-width: 1400px; margin: 0 auto; display: flex; flex-direction: column; gap: 160px;">
            
            <!-- Block A: The Speed Advantage -->
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 80px; align-items: center;">
                <div>
                    <div style="font-family: 'JetBrains Mono', monospace; font-size: 12px; color: rgba(255,255,255,0.5); margin-bottom: 16px;">01 // DETECTION</div>
                    <h2 style="font-size: clamp(2rem, 3vw, 2.75rem); font-weight: 700; letter-spacing: -0.03em; margin-bottom: 24px; color: #fff;">Spot the winner before it scales.</h2>
                    <p style="font-size: 1.125rem; color: rgba(255,255,255,0.6); line-height: 1.6; margin-bottom: 0;">
                        By the time a product trends publicly, the market is saturated. Our AI detects aggressive spend patterns in real-time, giving you a 2-4 week advantage to source and launch before the masses catch on.
                    </p>
                </div>
                <div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 24px; padding: 64px; display: flex; align-items: center; justify-content: center; position: relative;">
                    <!-- Velocity Dial Concept -->
                    <div style="width: 200px; height: 200px; border-radius: 50%; border: 2px dashed rgba(255,255,255,0.1); position: relative; display: flex; align-items: center; justify-content: center;">
                        <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; border-radius: 50%; border: 4px solid transparent; border-top-color: #10B981; border-right-color: #10B981; transform: rotate(45deg); opacity: 0.8;"></div>
                        <div style="text-align: center;">
                            <div style="font-size: 32px; font-weight: 700; color: #fff; font-family: 'JetBrains Mono', monospace;">92%</div>
                            <div style="font-size: 11px; color: #10B981; text-transform: uppercase; font-family: 'JetBrains Mono', monospace; margin-top: 4px;">Velocity</div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Block B: Financial Exposure -->
            <div style="background: rgba(255,255,255,0.01); border: 1px solid rgba(255,255,255,0.03); border-radius: 32px; padding: 120px 5%; text-align: center; position: relative; overflow: hidden;">
                <!-- Blurred ad mosaic background -->
                <div style="position: absolute; inset: 0; display: grid; grid-template-columns: repeat(5, 1fr); gap: 8px; opacity: 0.1; filter: blur(12px);">
                    <div style="background: #fff; height: 100%;"></div><div style="background: #ccc; height: 100%;"></div><div style="background: #fff; height: 100%;"></div><div style="background: #999; height: 100%;"></div><div style="background: #fff; height: 100%;"></div>
                </div>
                
                <div style="position: relative; z-index: 1;">
                    <div style="font-family: 'JetBrains Mono', monospace; font-size: 12px; color: rgba(255,255,255,0.5); margin-bottom: 24px;">02 // FINANCIAL EXPOSURE</div>
                    <h2 style="font-size: clamp(2rem, 3vw, 2.75rem); font-weight: 700; letter-spacing: -0.03em; margin-bottom: 48px; color: #fff;">We calculate the risk they are taking.</h2>
                    
                    <div style="font-size: clamp(4rem, 8vw, 8rem); font-weight: 800; color: #fff; line-height: 1; letter-spacing: -0.05em; margin-bottom: 24px; text-shadow: 0 20px 60px rgba(0,0,0,0.5);">
                        $1,204,500
                    </div>
                    <p style="font-size: 1.125rem; color: rgba(255,255,255,0.6); line-height: 1.6; max-width: 600px; margin: 0 auto;">
                        AI models estimate actual dollar spend based on engagement velocity and reach signals. You see exactly how heavily they invest.
                    </p>
                </div>
            </div>

            <!-- Block C: Opportunity Engine -->
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 80px; align-items: center; direction: rtl;">
                <div style="direction: ltr;">
                    <div style="font-family: 'JetBrains Mono', monospace; font-size: 12px; color: rgba(255,255,255,0.5); margin-bottom: 16px;">03 // OPPORTUNITY ENGINE</div>
                    <h2 style="font-size: clamp(2rem, 3vw, 2.75rem); font-weight: 700; letter-spacing: -0.03em; margin-bottom: 24px; color: #fff;">Exploit the gaps they leave behind.</h2>
                    <p style="font-size: 1.125rem; color: rgba(255,255,255,0.6); line-height: 1.6; margin-bottom: 0;">
                        Tracking competitors isn't just about copying them—it's about finding what they missed. The AI identifies high-demand niches with low competitor ad spend, serving you untapped opportunities on a silver platter.
                    </p>
                </div>
                <div style="direction: ltr; background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 24px; padding: 64px; display: flex; flex-direction: column; gap: 16px;">
                    <!-- Opportunity Bars -->
                    <div style="display: flex; align-items: center; justify-content: space-between; padding: 16px; background: rgba(0,0,0,0.5); border-radius: 8px; border-left: 4px solid #10B981;">
                        <span style="font-size: 14px; font-weight: 500; color: #fff;">Smart Home Security</span>
                        <span style="font-family: 'JetBrains Mono', monospace; font-size: 12px; color: #10B981;">HIGH GAP</span>
                    </div>
                    <div style="display: flex; align-items: center; justify-content: space-between; padding: 16px; background: rgba(0,0,0,0.5); border-radius: 8px; border-left: 4px solid rgba(255,255,255,0.2);">
                        <span style="font-size: 14px; font-weight: 500; color: #fff;">Pet Tech Devices</span>
                        <span style="font-family: 'JetBrains Mono', monospace; font-size: 12px; color: rgba(255,255,255,0.5);">SATURATED</span>
                    </div>
                    <div style="display: flex; align-items: center; justify-content: space-between; padding: 16px; background: rgba(0,0,0,0.5); border-radius: 8px; border-left: 4px solid rgba(255,255,255,0.2);">
                        <span style="font-size: 14px; font-weight: 500; color: #fff;">Ergonomic Furniture</span>
                        <span style="font-family: 'JetBrains Mono', monospace; font-size: 12px; color: rgba(255,255,255,0.5);">SATURATED</span>
                    </div>
                </div>
            </div>

        </div>
    </section>

    <!-- SECTION 4: CLARITY SHOCK (Metrics) -->
    <section style="padding: 160px 5%; background: #ffffff; color: #000;">
        <div style="max-width: 1400px; margin: 0 auto; text-align: center;">
            <h2 style="font-size: clamp(2.5rem, 4vw, 3.5rem); font-weight: 800; letter-spacing: -0.04em; margin-bottom: 80px;">Absolute Truth. <br>Absolute Clarity.</h2>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 40px; text-align: left;">
                <div style="border-top: 2px solid #000; padding-top: 32px;">
                    <div style="font-size: clamp(4rem, 6vw, 5rem); font-weight: 800; color: #000; letter-spacing: -0.05em; line-height: 1; margin-bottom: 24px;">10x</div>
                    <div style="font-size: 1.25rem; font-weight: 700; color: #000; margin-bottom: 12px;">Research Time Eliminated</div>
                    <p style="color: #4B5563; font-size: 1.125rem; line-height: 1.6; margin: 0;">Automated intelligence gathering replaces hours of manual ad library browsing every single day.</p>
                </div>
                <div style="border-top: 2px solid #000; padding-top: 32px;">
                    <div style="font-size: clamp(4rem, 6vw, 5rem); font-weight: 800; color: #000; letter-spacing: -0.05em; line-height: 1; margin-bottom: 24px;">$0</div>
                    <div style="font-size: 1.25rem; font-weight: 700; color: #000; margin-bottom: 12px;">Wasted Budget</div>
                    <p style="color: #4B5563; font-size: 1.125rem; line-height: 1.6; margin: 0;">Never fund a dead trend again. Validate products through verified competitor spend before launching.</p>
                </div>
                <div style="border-top: 2px solid #000; padding-top: 32px;">
                    <div style="font-size: clamp(4rem, 6vw, 5rem); font-weight: 800; color: #000; letter-spacing: -0.05em; line-height: 1; margin-bottom: 24px;">30-D</div>
                    <div style="font-size: 1.25rem; font-weight: 700; color: #000; margin-bottom: 12px;">Predictive Edge</div>
                    <p style="color: #4B5563; font-size: 1.125rem; line-height: 1.6; margin: 0;">Secure a massive head start by identifying scaling products weeks before they appear on social feeds.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- SECTION 5: FINAL CTA (Marketing Driven) -->
    <section style="padding: 180px 5% 160px 5%; background: #000; text-align: center; position: relative; overflow: hidden;">
         <!-- Very subtle emerald accent -->
         <div style="position: absolute; bottom: -20%; left: 50%; transform: translateX(-50%); width: 800px; height: 400px; background: radial-gradient(circle, rgba(16, 185, 129, 0.1) 0%, transparent 70%); z-index: 0; filter: blur(50px);"></div>
         
         <div style="position: relative; z-index: 1; max-width: 800px; margin: 0 auto;">
             <h2 style="font-size: clamp(3.5rem, 6vw, 5rem); font-weight: 800; color: #fff; letter-spacing: -0.04em; margin-bottom: 24px; line-height: 1.05;">The Unfair Advantage.</h2>
             <p style="font-size: 1.5rem; color: rgba(255,255,255,0.7); margin-bottom: 56px; max-width: 600px; margin-left: auto; margin-right: auto; line-height: 1.5;">
                 Don't let your competitors scale without you. Access the intelligence layer today.
             </p>
             <div style="display: flex; justify-content: center; gap: 16px; flex-wrap: wrap;">
                 <a href="#" class="primary-btn" style="background: #fff; color: #000; font-size: 1.125rem; font-weight: 600; padding: 20px 48px; border-radius: 99px; text-decoration: none; transition: transform 0.3s ease;">Initiate Tracking</a>
             </div>
         </div>
    </section>

    <style>
        .primary-btn:hover {
            transform: scale(1.03);
            background: #f8fafc !important;
            box-shadow: 0 10px 30px rgba(255,255,255,0.1);
        }
        @keyframes fadeInUp {
            0% { opacity: 0; transform: translateY(30px); }
            100% { opacity: 1; transform: translateY(0); }
        }
        @keyframes pulse-glow {
            0% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.5); }
            70% { box-shadow: 0 0 0 8px rgba(16, 185, 129, 0); }
            100% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
        }
        @keyframes scan-motion {
            0% { transform: translateY(0); }
            50% { transform: translateY(400px); }
            100% { transform: translateY(0); }
        }
        .hero-scan-line {
            animation: scan-motion 4s cubic-bezier(0.4, 0, 0.2, 1) infinite;
        }
    </style>
</div>
"""

# Replace placeholder
placeholder = soup.find(string=lambda text: text and 'Content Coming Soon' in text)
if placeholder:
    wrapper = placeholder.find_parent('div', class_='semantic-placeholder-wrapper')
    if wrapper:
        new_section = bs4.BeautifulSoup(content_html, 'html.parser')
        wrapper.replace_with(new_section)
    else:
        section_to_replace = placeholder.find_parent('section')
        if section_to_replace:
            new_section = bs4.BeautifulSoup(content_html, 'html.parser')
            section_to_replace.replace_with(new_section)
else:
    # Look for existing wrapper
    old_wrapper = soup.find('div', class_='semantic-advertiser-tracker-wrapper')
    if old_wrapper:
        new_section = bs4.BeautifulSoup(content_html, 'html.parser')
        old_wrapper.replace_with(new_section)

with open('advertiser-tracker.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Successfully rebuilt the Advertiser Tracker product page with the refined AI Intelligence design.")
