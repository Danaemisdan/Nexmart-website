import bs4
import re

def add_funnel_transition():
    with open('advertiser-tracker.html', 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = bs4.BeautifulSoup(html, 'html.parser')

    # Find the CTA section
    cta_text = soup.find(string=lambda t: t and 'The Future of Commerce Starts Here' in t)
    if not cta_text:
        print('CTA not found.')
        return
        
    container_large = cta_text.find_parent('div', class_='container-large')
    cta_section = container_large.parent
    
    # We will insert a new div right before the CTA section
    funnel_html = """
    <div class="ad-funnel-transition">
        <!-- Floating particles -->
        <div class="ad-particle p1"></div>
        <div class="ad-particle p2"></div>
        <div class="ad-particle p3"></div>
        <div class="ad-particle p4"></div>
        <div class="ad-particle p5"></div>
        
        <svg class="ad-funnel-svg" viewBox="0 0 1000 400" preserveAspectRatio="none">
            <defs>
                <linearGradient id="funnel-glow" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="0%" stop-color="rgba(16, 185, 129, 0.15)" />
                    <stop offset="50%" stop-color="rgba(16, 185, 129, 0.4)" />
                    <stop offset="100%" stop-color="rgba(16, 185, 129, 0.8)" />
                </linearGradient>
                <filter id="blur-glow" x="-20%" y="-20%" width="140%" height="140%">
                    <feGaussianBlur stdDeviation="15" />
                </filter>
            </defs>
            <!-- Core glowing funnel -->
            <path d="M 0,0 
                     L 1000,0 
                     C 800,50 650,200 530,300
                     C 515,315 505,330 505,350
                     L 495,350
                     C 495,330 485,315 470,300
                     C 350,200 200,50 0,0 Z" 
                  fill="url(#funnel-glow)" 
                  filter="url(#blur-glow)" />
                  
            <!-- Inner brighter core -->
            <path d="M 200,0 
                     L 800,0 
                     C 650,50 580,200 520,300
                     C 510,315 502,330 502,350
                     L 498,350
                     C 498,330 490,315 480,300
                     C 420,200 350,50 200,0 Z" 
                  fill="rgba(255, 255, 255, 0.15)" 
                  filter="url(#blur-glow)" />
        </svg>
        
        <!-- Intelligence Node Icon at the convergence point -->
        <div class="ad-convergence-node">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#10B981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="12" cy="12" r="10"></circle>
                <line x1="12" y1="16" x2="12" y2="12"></line>
                <line x1="12" y1="8" x2="12.01" y2="8"></line>
            </svg>
        </div>
    </div>
    """
    
    # Check if we already inserted it
    if soup.find('div', class_='ad-funnel-transition'):
        soup.find('div', class_='ad-funnel-transition').decompose()
        
    funnel_soup = bs4.BeautifulSoup(funnel_html, 'html.parser')
    cta_section.insert_before(funnel_soup)

    # Now add the CSS for this funnel
    funnel_css = """
    /* Advertiser Tracker Funnel Transition */
    .ad-funnel-transition {
        position: relative;
        width: 100%;
        height: 300px;
        background: linear-gradient(180deg, #050505 0%, rgba(10, 10, 12, 1) 100%);
        overflow: hidden;
        display: flex;
        justify-content: center;
        align-items: flex-end;
        margin-top: -100px; /* pull up over the previous section's padding */
        z-index: 2;
    }
    .ad-funnel-svg {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 1;
        opacity: 0.8;
    }
    .ad-convergence-node {
        position: relative;
        z-index: 3;
        margin-bottom: 25px;
        width: 48px;
        height: 48px;
        background: rgba(16, 185, 129, 0.1);
        border: 1px solid rgba(16, 185, 129, 0.4);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 0 30px rgba(16, 185, 129, 0.8), inset 0 0 15px rgba(16, 185, 129, 0.4);
        animation: nodePulse 3s infinite alternate;
    }
    .ad-particle {
        position: absolute;
        width: 3px;
        height: 3px;
        background: #10B981;
        border-radius: 50%;
        box-shadow: 0 0 8px 2px #10B981;
        z-index: 2;
        animation: particleFlow 4s infinite linear;
        opacity: 0;
    }
    .p1 { left: 40%; top: 20%; animation-delay: 0s; }
    .p2 { left: 60%; top: 30%; animation-delay: 1s; }
    .p3 { left: 45%; top: 10%; animation-delay: 2.5s; }
    .p4 { left: 55%; top: 15%; animation-delay: 1.5s; }
    .p5 { left: 50%; top: 0%; animation-delay: 3s; }

    @keyframes nodePulse {
        0% { box-shadow: 0 0 20px rgba(16, 185, 129, 0.5), inset 0 0 10px rgba(16, 185, 129, 0.2); }
        100% { box-shadow: 0 0 40px rgba(16, 185, 129, 1), inset 0 0 20px rgba(16, 185, 129, 0.6); }
    }
    @keyframes particleFlow {
        0% { transform: translateY(0) scale(1); opacity: 0; }
        20% { opacity: 1; }
        80% { opacity: 1; }
        100% { transform: translateY(200px) scale(0.5) translateX(calc((50vw - 100%) * 0.2)); opacity: 0; }
    }
    
    /* Fix CTA section spacing since we added the funnel */
    .ad-cta-section {
        margin-top: 0 !important;
        padding-top: 60px !important;
        background: rgba(10, 10, 12, 1) !important;
    }
    """

    style_tag = soup.find_all('style')[-1]
    if style_tag:
        style_tag.append(funnel_css)

    with open('advertiser-tracker.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print('Added Funnel Transition.')

if __name__ == "__main__":
    add_funnel_transition()
