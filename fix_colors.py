import bs4
import re

def fix_agentic_commerce():
    with open('agentic-commerce.html', 'r', encoding='utf-8') as f:
        html = f.read()
        
    # Replace global blue hexes with emerald green hexes
    html = re.sub(r'(?i)#1B4DBB', '#22A06B', html) # main
    html = re.sub(r'(?i)#2A64D8', '#22A06B', html) # main alt
    html = re.sub(r'(?i)#5E9DFF', '#22A06B', html) # main light
    html = re.sub(r'(?i)#7CA6F2', '#1B8A5A', html) # light
    html = re.sub(r'(?i)#143D8D', '#166B47', html) # dark
    html = re.sub(r'(?i)#0E2A66', '#0E4F35', html) # deep
    html = re.sub(r'(?i)#EBF4FC', '#E8F5E9', html) # very light background
    
    # Replace RGBA blue with RGBA green
    # (34, 160, 107) is #22A06B
    html = re.sub(r'42,\s*100,\s*216', '34, 160, 107', html)
    html = re.sub(r'20,\s*61,\s*141', '22, 107, 71', html)
    html = re.sub(r'14,\s*42,\s*102', '14, 79, 53', html)
    
    # Fix the footer gradient
    html = re.sub(
        r'background:\s*linear-gradient\(180deg,\s*#[0-9a-fA-F]+\s*0%,\s*#[0-9a-fA-F]+\s*100%\)\s*!important;',
        'background: linear-gradient(180deg, #0E4F35 0%, #050505 100%) !important;',
        html
    )
    
    with open('agentic-commerce.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Agentic Commerce fixed.")

def fix_magic_ai_search():
    with open('magic-ai-search.html', 'r', encoding='utf-8') as f:
        html = f.read()
        
    # Fix the footer gradient
    html = re.sub(
        r'background:\s*linear-gradient\(180deg,\s*#[0-9a-fA-F]+\s*0%,\s*#[0-9a-fA-F]+\s*100%\)\s*!important;',
        'background: linear-gradient(180deg, #243B75 0%, #050505 100%) !important;',
        html
    )
    
    with open('magic-ai-search.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Magic AI fixed.")

def fix_advertiser_tracker():
    with open('advertiser-tracker.html', 'r', encoding='utf-8') as f:
        html = f.read()
        
    # Fix the footer gradient
    html = re.sub(
        r'background:\s*linear-gradient\(180deg,\s*#[0-9a-fA-F]+\s*0%,\s*#[0-9a-fA-F]+\s*100%\)\s*!important;',
        'background: linear-gradient(180deg, #721C1A 0%, #050505 100%) !important;',
        html
    )
    
    with open('advertiser-tracker.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Advertiser Tracker fixed.")

if __name__ == "__main__":
    fix_agentic_commerce()
    fix_magic_ai_search()
    fix_advertiser_tracker()
