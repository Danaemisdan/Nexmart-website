import bs4
import re

def rgb_to_str(r, g, b):
    return f"{r}, {g}, {b}"
def rgba_to_str(r, g, b, a):
    return f"rgba({r}, {g}, {b}, {a})"

def update_agentic_commerce():
    # Agentic Commerce currently uses global blue. We will inject a style block to override it to Emerald.
    with open('agentic-commerce.html', 'r', encoding='utf-8') as f:
        html = f.read()
    soup = bs4.BeautifulSoup(html, 'html.parser')
    
    custom_css = """
    /* Phase 1: Emerald Identity Overrides */
    :root {
        --brand-main: #22A06B;
        --brand-light: #1B8A5A;
        --brand-dark: #166B47;
        --brand-deep: #0E4F35;
    }
    .text-color-brand { color: var(--brand-main) !important; }
    .bg-color-brand, .button, .btn { background-color: var(--brand-main) !important; }
    .button:hover, .btn:hover { background-color: var(--brand-light) !important; }
    .hero-glow, .bg-glow { background: radial-gradient(circle, rgba(34, 160, 107, 0.15) 0%, transparent 70%) !important; }
    
    /* Custom Footer Transition */
    .footer_component {
        background: linear-gradient(180deg, #050505 0%, #0a0a0c 100%) !important;
        position: relative;
    }
    .footer_component::before {
        content: '';
        position: absolute; top: 0; left: 0; right: 0; height: 1px;
        background: linear-gradient(90deg, transparent, rgba(34, 160, 107, 0.3), transparent);
    }
    """
    style_tag = soup.find_all('style')[-1] if soup.find_all('style') else soup.new_tag('style')
    if style_tag.name == 'style':
        style_tag.append(custom_css)
        if not style_tag.parent:
            soup.head.append(style_tag)
    
    with open('agentic-commerce.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print("Agentic Commerce updated.")

def update_magic_ai_search():
    # Magic AI Search uses purple. We change to Blue.
    with open('magic-ai-search.html', 'r', encoding='utf-8') as f:
        html = f.read()
        
    # Replace Hex
    html = re.sub(r'(?i)#5B3DF5', '#4F7BFF', html)
    html = re.sub(r'(?i)#3A1FAD', '#3D68F5', html)
    html = re.sub(r'(?i)#8A72FF', '#6F93FF', html)
    html = re.sub(r'(?i)#A88BFF', '#A9BFFF', html)
    html = re.sub(r'(?i)#3B2475', '#243B75', html) # dark purple to dark blue
    
    # Replace RGB (91, 61, 245) to (79, 123, 255)
    html = re.sub(r'91,\s*61,\s*245', '79, 123, 255', html)
    # Replace RGB (168, 139, 255) to (111, 147, 255)
    html = re.sub(r'168,\s*139,\s*255', '111, 147, 255', html)
    
    # Inject footer transition
    soup = bs4.BeautifulSoup(html, 'html.parser')
    footer_css = """
    /* Magic AI Search Footer */
    .footer_component {
        background: linear-gradient(180deg, #050510 0%, #030305 100%) !important;
        position: relative;
    }
    .footer_component::before {
        content: ''; position: absolute; top: 0; left: 0; right: 0; height: 1px;
        background: linear-gradient(90deg, transparent, rgba(79, 123, 255, 0.4), transparent);
    }
    """
    style_tag = soup.find_all('style')[-1]
    if style_tag:
        style_tag.append(footer_css)
        
    with open('magic-ai-search.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print("Magic AI Search updated.")

def update_advertiser_tracker():
    # Advertiser Tracker uses Emerald. We change to Crimson Red.
    with open('advertiser-tracker.html', 'r', encoding='utf-8') as f:
        html = f.read()
        
    # Replace Hex
    html = re.sub(r'(?i)#10B981', '#E53935', html)
    html = re.sub(r'(?i)#059669', '#EF5350', html)
    html = re.sub(r'(?i)#047857', '#C62828', html)
    html = re.sub(r'(?i)#34D399', '#8E1F1C', html)
    html = re.sub(r'(?i)#065F46', '#721C1A', html)
    
    # Replace RGB (16, 185, 129) -> (229, 57, 53)
    html = re.sub(r'16,\s*185,\s*129', '229, 57, 53', html)
    # Replace RGB (52, 211, 153) -> (239, 83, 80)
    html = re.sub(r'52,\s*211,\s*153', '239, 83, 80', html)
    
    # Update Footer colors for Advertiser Tracker
    soup = bs4.BeautifulSoup(html, 'html.parser')
    footer_css = """
    /* Advertiser Tracker Footer Override */
    .footer_component {
        background: linear-gradient(180deg, #100505 0%, #050202 100%) !important;
        position: relative;
    }
    .footer_component::before {
        content: ''; position: absolute; top: 0; left: 0; right: 0; height: 1px;
        background: linear-gradient(90deg, transparent, rgba(229, 57, 53, 0.3), transparent) !important;
        box-shadow: 0 0 20px rgba(229, 57, 53, 0.1) !important;
    }
    """
    style_tag = soup.find_all('style')[-1]
    if style_tag:
        style_tag.append(footer_css)
        
    with open('advertiser-tracker.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print("Advertiser Tracker updated.")

if __name__ == "__main__":
    update_agentic_commerce()
    update_magic_ai_search()
    update_advertiser_tracker()
