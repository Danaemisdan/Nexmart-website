import bs4
import re

def refine_transition():
    with open('advertiser-tracker.html', 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = bs4.BeautifulSoup(html, 'html.parser')

    # The new refined CSS
    new_css = """
    /* Override Global Backgrounds for Advertiser Tracker CTA & Footer ONLY */
    .ad-cta-section {
        /* Reduce empty space between dashboard and CTA */
        margin-top: -80px !important; 
        padding-top: 120px !important;
        position: relative;
        /* Rich layered gradient transition */
        background: linear-gradient(180deg, 
            transparent 0%, 
            rgba(16, 185, 129, 0.05) 15%, 
            rgba(16, 185, 129, 0.08) 30%, 
            #0a0a0c 60%, 
            #050505 100%) !important;
        z-index: 1;
    }
    
    /* Faint AI grid / intelligence pattern behind the CTA */
    .ad-cta-section::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background-image: 
            linear-gradient(rgba(16, 185, 129, 0.03) 1px, transparent 1px),
            linear-gradient(90deg, rgba(16, 185, 129, 0.03) 1px, transparent 1px);
        background-size: 40px 40px;
        mask-image: radial-gradient(ellipse at top center, black 0%, transparent 70%);
        -webkit-mask-image: radial-gradient(ellipse at top center, black 0%, transparent 70%);
        z-index: -1;
        pointer-events: none;
    }

    .ad-cta-container {
        background: transparent !important;
        position: relative;
    }
    
    /* Spotlight glow behind the CTA heading */
    .ad-cta-container::before {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 60%;
        height: 150%;
        background: radial-gradient(circle, rgba(16, 185, 129, 0.1) 0%, transparent 60%);
        filter: blur(40px);
        z-index: -1;
        pointer-events: none;
    }
    
    /* Typography refinement for the CTA */
    .ad-cta-container h2 {
        text-shadow: 0 0 40px rgba(16, 185, 129, 0.3);
        letter-spacing: -0.02em;
    }

    /* Footer Transition Refinement */
    .footer_component {
        background: #050505 !important;
        position: relative;
    }
    
    /* Soft glowing separator */
    .footer_component::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(16, 185, 129, 0.2), transparent);
        box-shadow: 0 0 20px rgba(16, 185, 129, 0.1);
        z-index: 10;
    }
    
    /* Remove the blue background from CTA */
    .section_cta, [class*="cta-wrap"], .section-cta {
        background: transparent !important;
    }
    """

    # We need to replace the old block inside the style tag
    style_tag = soup.find_all('style')[-1]
    if style_tag and style_tag.string:
        old_css = style_tag.string
        # regex to replace everything from /* Override Global Backgrounds for Advertiser Tracker CTA & Footer ONLY */ to the end
        import re
        new_string = re.sub(r'/\* Override Global Backgrounds for Advertiser Tracker CTA & Footer ONLY \*/.*', new_css, old_css, flags=re.DOTALL)
        style_tag.string = new_string

    with open('advertiser-tracker.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print('Refined the CTA and Footer transition.')

if __name__ == "__main__":
    refine_transition()
