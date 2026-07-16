import bs4
import shutil

# Reset from about.html
shutil.copy('about.html', 'faqs.html')

faqs = {
    "General": [
        ("What is Nexmart?", "Nexmart is an AI-powered commerce ecosystem that helps people discover, compare, and purchase products using intelligent shopping agents instead of traditional search."),
        ("What is Agentic Commerce?", "Agentic Commerce allows AI agents to understand your intent, research products, compare options, negotiate prices where possible, and recommend the best purchasing decisions."),
        ("How is Nexmart different from traditional marketplaces?", "Instead of manually browsing hundreds of listings, Nexmart's AI agents perform the research and present the best options based on your requirements."),
        ("Which countries does Nexmart support?", "Nexmart is designed for global commerce and continuously expands its supported regions and fulfillment network.")
    ],
    "AI Shopping Agents": [
        ("How do AI Shopping Agents work?", "They analyze your request, search multiple suppliers, compare products, pricing, delivery options, and recommend the best purchase."),
        ("Can the AI make purchases for me?", "Yes. Depending on your permissions, AI agents can complete purchases on your behalf."),
        ("Can I approve purchases before checkout?", "Yes. Users remain in full control and can review recommendations before confirming."),
        ("Can I give complex shopping instructions?", "Yes. You can provide budgets, preferred brands, delivery requirements, product specifications, and more.")
    ],
    "Membership & Cards": [
        ("Does Nexmart require a subscription?", "Many features are free, while premium tools and advanced AI capabilities are available through membership plans."),
        ("What is the Nexmart Card?", "The Nexmart Card enables secure payments and simplifies purchases throughout the Nexmart ecosystem."),
        ("Are there membership benefits?", "Premium members receive enhanced AI capabilities, exclusive tools, faster support, and additional ecosystem features.")
    ],
    "Orders & Shipping": [
        ("How can I track my orders?", "Every order includes real-time tracking directly within your Nexmart account."),
        ("Can AI choose faster shipping?", "Yes. AI considers delivery speed alongside price and reliability when making recommendations."),
        ("Does Nexmart support international shipping?", "Yes. International shipping is available depending on product availability and destination.")
    ],
    "Payments & Security": [
        ("Which payment methods are supported?", "Nexmart supports multiple secure payment methods, with additional options added as the platform expands."),
        ("Is my payment information secure?", "Yes. Nexmart uses industry-standard security practices to protect transactions and personal information."),
        ("What is Neural Ledger?", "Neural Ledger is Nexmart's intelligent transaction system that securely records and manages purchasing activity across the ecosystem.")
    ],
    "Returns & Refunds": [
        ("What is your return policy?", "Eligible products can be returned within the published return period, subject to seller policies."),
        ("How do refunds work?", "Refunds are processed after returned items are inspected and approved."),
        ("Can AI assist with returns?", "Yes. AI agents can guide users through the return process and prepare return requests.")
    ],
    "Sellers & Advertisers": [
        ("Can businesses sell on Nexmart?", "Yes. Businesses can integrate with Nexmart to reach AI-powered shoppers."),
        ("What is Advertiser Tracker?", "Advertiser Tracker provides competitive advertising intelligence to help businesses understand market activity."),
        ("Can sellers access analytics?", "Yes. Nexmart provides analytics and business intelligence tools for sellers.")
    ],
    "Account Management": [
        ("How do I create an account?", "Click Sign In and follow the registration process."),
        ("Can I manage multiple addresses?", "Yes. Users can save and manage multiple delivery addresses."),
        ("Can I delete my account?", "Yes. Account deletion can be requested through account settings or customer support.")
    ]
}

category_links = []
for cat in faqs.keys():
    cat_id = cat.lower().replace(' ', '-').replace('&', 'and')
    category_links.append(f'<a href="#{cat_id}" class="faq-cat-link" style="color: #111827; text-decoration: none; padding: 12px 24px; background: rgba(0,0,0,0.03); border-radius: 100px; font-weight: 500; font-size: 15px; white-space: nowrap; border: 1px solid rgba(0,0,0,0.05); transition: background 0.3s ease;">{cat}</a>')

categories_html = f"""
<div style="display: flex; flex-wrap: wrap; gap: 12px; justify-content: center; margin-bottom: 64px;">
    {''.join(category_links)}
</div>
"""

faq_html_blocks = []
for section_name, questions in faqs.items():
    cat_id = section_name.lower().replace(' ', '-').replace('&', 'and')
    section_html = f"""
    <div id="{cat_id}" style="margin-bottom: 80px; scroll-margin-top: 100px;">
        <h2 style="font-size: 28px; font-weight: 600; color: #111827; margin-bottom: 32px; border-bottom: 1px solid rgba(0,0,0,0.1); padding-bottom: 16px; letter-spacing: -0.01em;">{section_name}</h2>
        <div style="display: flex; flex-direction: column; gap: 16px;">
    """
    
    for q, a in questions:
        # Rounded glass cards on white background
        item_html = f"""
            <details style="background: rgba(255,255,255,0.7); backdrop-filter: blur(12px); border: 1px solid rgba(0,0,0,0.08); border-radius: 16px; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.02); margin: 0; padding: 0;">
                <summary style="padding: 28px 32px; font-size: 20px; font-weight: 500; color: #111827; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center; outline: none; margin: 0; line-height: 1.4; letter-spacing: -0.01em;">
                    <span style="display: block;">{q}</span>
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="opacity: 0.4; flex-shrink: 0; margin-left: 16px;"><polyline points="6 9 12 15 18 9"></polyline></svg>
                </summary>
                <div style="padding: 0 32px 32px 32px; font-size: 18px; color: #4B5563; line-height: 1.6; margin: 0;">
                    {a}
                </div>
            </details>
        """
        section_html += item_html
        
    section_html += """
        </div>
    </div>
    """
    faq_html_blocks.append(section_html)

all_faqs = "\n".join(faq_html_blocks)

# The user wants a white background for the page.
# I will override the background of the main wrapper and make the text dark.
# I'll keep the hero background transparent (if it's above the grid) or make it white too.
# Actually, setting background: #fff on the faq container is safest.
faq_section_wrapper = f"""
<!-- Clean Semantic FAQ Wrapper -->
<div class="semantic-faq-wrapper" style="background-color: #ffffff; padding-top: 80px; padding-bottom: 120px; width: 100%;">
  <div style="max-width: 900px; margin: 0 auto; padding: 0 5%; width: 100%; box-sizing: border-box;">
      {categories_html}
      {all_faqs}
  </div>
  <style>
      .semantic-faq-wrapper details:hover {{
          background: rgba(255,255,255,0.95) !important;
          box-shadow: 0 8px 24px rgba(0,0,0,0.04) !important;
      }}
      .semantic-faq-wrapper details[open] svg {{
          transform: rotate(180deg);
      }}
      .semantic-faq-wrapper details summary::-webkit-details-marker {{
          display: none;
      }}
      .faq-cat-link:hover {{
          background: rgba(0,0,0,0.06) !important;
      }}
  </style>
</div>
"""

with open('faqs.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = bs4.BeautifulSoup(html, 'html.parser')

# Update Hero safely
hero = soup.find('section', class_=lambda c: c and 'is-hero' in c)
if hero:
    # Make hero have a white background and dark text to match the requested design
    hero['style'] = hero.get('style', '') + '; background-color: #ffffff; color: #111827;'
    h1 = hero.find('h1')
    if h1:
        h1.string = "Frequently Asked Questions"
        h1['style'] = h1.get('style', '') + '; color: #111827 !important;'
    p = hero.find('p')
    if p:
        p.string = "Everything you need to know about Nexmart, Agentic Commerce, shopping, orders, payments, shipping, and using our AI-powered commerce platform."
        p['style'] = p.get('style', '') + '; color: #4B5563 !important;'

# Replace placeholder
placeholder = soup.find(string=lambda text: text and 'Content Coming Soon' in text)
if placeholder:
    section_to_replace = placeholder.find_parent('section')
    if section_to_replace:
        new_section = bs4.BeautifulSoup(faq_section_wrapper, 'html.parser')
        section_to_replace.replace_with(new_section)

# Make sure CTA section also has a matching white background so it flows seamlessly
sections = soup.find_all('section')
if len(sections) > 1:
    cta = sections[-1]
    cta['style'] = cta.get('style', '') + '; background-color: #ffffff;'
    # Darken CTA text if it was white
    for h in cta.find_all(['h2', 'h3']):
        h['style'] = h.get('style', '') + '; color: #111827 !important;'
    for p in cta.find_all('p'):
        p['style'] = p.get('style', '') + '; color: #4B5563 !important;'

with open('faqs.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

