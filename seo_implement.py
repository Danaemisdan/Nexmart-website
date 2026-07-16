import os
import glob
from bs4 import BeautifulSoup
from datetime import datetime

BASE_URL = "https://www.nexmartshop.ai"

# Legal page descriptions
legal_descriptions = {
    "privacy-policy.html": "Review the Nexmart Privacy Policy to understand how we collect, use, protect, and handle your personal data when using our agentic commerce platform.",
    "terms-and-conditions.html": "Read the Nexmart Terms and Conditions governing your use of our e-commerce platform, AI agents, and marketplace services.",
    "refund-policy.html": "Learn about the Nexmart Refund Policy, including eligibility criteria, timelines, and the process for requesting refunds for purchases.",
    "return-policy.html": "Review the Nexmart Return Policy to understand our guidelines for returning physical products purchased through our merchant network.",
    "cancellation-policy.html": "Understand the Nexmart Cancellation Policy, including how to cancel orders, subscriptions, and services before fulfillment.",
    "checkout-policy.html": "Read our Checkout Policy detailing secure payment processing, authorized payment methods, and transaction security on Nexmart."
}

# SEO Optimized Titles
optimized_titles = {
    "agentic-commerce.html": "Agentic Commerce: Autonomous AI Shopping Agents | Nexmart",
    "magic-ai-search.html": "Magic AI Search: Multimodal E-commerce Product Discovery | Nexmart",
    "advertiser-tracker.html": "Advertiser Tracker: Monitor Facebook Competitor Campaigns | Nexmart",
    "advertiser-library.html": "Advertiser Library: Analyze Competitor Ad Spend & Revenue | Nexmart",
    "portfolio.html": "Portfolio: Weekly High-Converting Dropshipping Products | Nexmart",
    "creator-library.html": "Creator Library: Discover Revenue-Generating TikTok Creators | Nexmart",
    "financial-inclusion.html": "Sales Tracker & Financial Inclusion Dashboard | Nexmart",
    "competitor-research.html": "Competitor Research: E-commerce Market Intelligence | Nexmart",
    "chrome-extension.html": "Nexmart Chrome Extension: Real-Time E-commerce Insights",
    "pre-built-stores.html": "Pre-built Shopify Stores: AI-Generated Dropshipping Launchpad | Nexmart",
    "theme-detector.html": "Shopify Theme Detector: Instant E-commerce Store Analysis | Nexmart",
    "healthcare-access.html": "Healthcare Access: Digital Marketplace for Medical Suppliers | Nexmart"
}

def implement_seo():
    html_files = glob.glob('*.html')
    if "index_original.html" in html_files:
        html_files.remove("index_original.html")
    # exclude template
    if "product-template.html" in html_files:
        html_files.remove("product-template.html")
        
    for file in html_files:
        with open(file, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, 'html.parser')
            
        head = soup.find('head')
        if not head: continue
        
        # 1. Update Title if under-optimized
        title_tag = soup.find('title')
        page_title = title_tag.string.strip() if title_tag and title_tag.string else "Nexmart: Agentic Commerce"
        
        if file in optimized_titles:
            new_title = optimized_titles[file]
            if title_tag:
                title_tag.string = new_title
            else:
                new_tag = soup.new_tag('title')
                new_tag.string = new_title
                head.append(new_tag)
            page_title = new_title
            
        # 2. Update Meta Description for Legal Pages
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        desc_text = "Discover Nexmart, the future of Agentic Commerce. Deploy autonomous AI agents to handle product discovery, negotiation, and checkout."
        
        if file in legal_descriptions:
            desc_text = legal_descriptions[file]
            if meta_desc:
                meta_desc['content'] = desc_text
            else:
                new_desc = soup.new_tag('meta', attrs={'name': 'description', 'content': desc_text})
                head.append(new_desc)
        elif meta_desc and meta_desc.get('content'):
            desc_text = meta_desc.get('content').strip()
            
        # 3. Add Canonical URL
        page_url = f"{BASE_URL}/{file}"
        if file == "index.html":
            page_url = f"{BASE_URL}/"
            
        existing_canonical = soup.find('link', rel='canonical')
        if existing_canonical:
            existing_canonical['href'] = page_url
        else:
            canonical_tag = soup.new_tag('link', rel='canonical', href=page_url)
            head.append(canonical_tag)
            
        # 4 & 5. Open Graph and Twitter Cards
        # Remove existing if any to avoid duplicates
        for tag in soup.find_all('meta', attrs={'property': lambda x: x and x.startswith('og:')}): tag.decompose()
        for tag in soup.find_all('meta', attrs={'name': lambda x: x and x.startswith('twitter:')}): tag.decompose()
        
        social_image = "nexmart_dashboard.png" # Assuming this exists as the best default social share image
        
        og_tags = [
            {'property': 'og:title', 'content': page_title},
            {'property': 'og:description', 'content': desc_text},
            {'property': 'og:type', 'content': 'website'},
            {'property': 'og:url', 'content': page_url},
            {'property': 'og:image', 'content': f"{BASE_URL}/{social_image}"}
        ]
        
        twitter_tags = [
            {'name': 'twitter:card', 'content': 'summary_large_image'},
            {'name': 'twitter:title', 'content': page_title},
            {'name': 'twitter:description', 'content': desc_text},
            {'name': 'twitter:image', 'content': f"{BASE_URL}/{social_image}"}
        ]
        
        for tag_data in og_tags + twitter_tags:
            meta = soup.new_tag('meta', attrs=tag_data)
            head.append(meta)
            
        with open(file, "w", encoding="utf-8") as f:
            f.write(str(soup))
            
    # 6. Generate robots.txt
    robots_content = f"User-agent: *\nAllow: /\n\nSitemap: {BASE_URL}/sitemap.xml\n"
    with open("robots.txt", "w", encoding="utf-8") as f:
        f.write(robots_content)
        
    # 7. Generate sitemap.xml
    sitemap_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]
    
    today = datetime.now().strftime('%Y-%m-%d')
    for file in html_files:
        url = f"{BASE_URL}/{file}"
        if file == "index.html": url = f"{BASE_URL}/"
        
        priority = "0.8"
        if file == "index.html": priority = "1.0"
        elif "policy" in file or "terms" in file: priority = "0.3"
        
        sitemap_lines.append(f"  <url>\n    <loc>{url}</loc>\n    <lastmod>{today}</lastmod>\n    <priority>{priority}</priority>\n  </url>")
        
    sitemap_lines.append('</urlset>')
    
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write("\n".join(sitemap_lines))

if __name__ == "__main__":
    implement_seo()
