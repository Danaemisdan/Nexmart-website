import bs4

faqs = {
    "GENERAL": [
        ("What is Nexmart?", "Nexmart is an AI-powered commerce platform that helps you discover, compare, and purchase products more intelligently. Instead of manually searching across multiple websites, you can simply describe what you need, and Nexmart's AI helps identify the best options based on your requirements."),
        ("What is Agentic Commerce?", "Agentic Commerce is a new way of shopping where AI assists with researching products, comparing options, and simplifying purchasing decisions based on your preferences."),
        ("How is Nexmart different from traditional marketplaces?", "Traditional marketplaces require you to manually browse products and compare listings yourself. Nexmart uses AI to help surface relevant products, compare choices, and simplify decision-making."),
        ("Which countries does Nexmart support?", "Nexmart is designed for global commerce. Availability of products, payment methods, and shipping options may vary depending on your region."),
        ("Do I need an account to use Nexmart?", "You can explore parts of the platform without an account, but creating an account unlocks personalized recommendations, saved searches, order history, and additional AI-powered features."),
        ("Is Nexmart free to use?", "Yes. Core shopping features are available to users. Some advanced business tools or future premium capabilities may require a subscription.")
    ],
    "AI SHOPPING": [
        ("How does AI Shopping work?", "Simply describe what you're looking for in natural language. Nexmart analyzes your request and helps identify products that best match your preferences."),
        ("Can I search using everyday language?", "Yes. You can search naturally, such as:<br/><br/>\"Find a lightweight gaming laptop under $1,200.\"<br/><br/>or<br/><br/>\"Suggest ergonomic office chairs for long working hours.\""),
        ("Can AI compare multiple products?", "Yes. Nexmart helps compare products across important factors such as pricing, specifications, ratings, and other relevant details."),
        ("Can AI recommend alternatives?", "Absolutely. If your preferred product is unavailable or another option better fits your requirements, Nexmart can recommend suitable alternatives."),
        ("Can I refine my search after receiving results?", "Yes. You can continue the conversation naturally by adding new preferences or adjusting your requirements."),
        ("Does AI remember my preferences?", "With your permission, Nexmart can personalize future recommendations based on your shopping preferences and previous interactions.")
    ],
    "ORDERS": [
        ("How do I place an order?", "After selecting a product, follow the checkout process by confirming your shipping details, payment method, and order information."),
        ("Can I cancel an order?", "Orders may be cancelled before they enter fulfillment. Availability depends on the seller and the current order status."),
        ("Can I modify my order after placing it?", "Order modifications may be possible before processing begins. Once an order has entered fulfillment, changes may no longer be available."),
        ("How can I track my order?", "You can track your order from your Nexmart account dashboard using the tracking information provided after shipment."),
        ("Will I receive order updates?", "Yes. You'll receive important notifications throughout the order lifecycle, including confirmation, shipment, and delivery updates.")
    ],
    "SHIPPING": [
        ("Which shipping options are available?", "Shipping options vary depending on the seller, product, and destination."),
        ("How long does delivery take?", "Estimated delivery times are displayed before checkout and may vary by location and shipping method."),
        ("Do you support international shipping?", "Many products support international shipping. Availability depends on the seller and destination country."),
        ("Can I track international shipments?", "Yes. Tracking information is provided whenever supported by the shipping carrier."),
        ("Will customs duties apply?", "International shipments may be subject to customs duties or import taxes according to local regulations.")
    ],
    "RETURNS & REFUNDS": [
        ("What is Nexmart's return policy?", "Eligible products can generally be returned within the applicable return window, subject to the seller's policy."),
        ("How do I request a return?", "Navigate to your order history, select the relevant order, and follow the return instructions."),
        ("When will I receive my refund?", "Refunds are processed after the returned product has been inspected and approved."),
        ("What if I receive a damaged product?", "Please contact support promptly with photos of the product and packaging so the issue can be investigated."),
        ("What if I receive the wrong item?", "If the delivered item doesn't match your order, contact support and we'll help resolve the issue.")
    ],
    "PAYMENTS": [
        ("Which payment methods are supported?", "Available payment methods depend on your region and may include cards, digital wallets, bank transfers, and other supported local options."),
        ("Is my payment information secure?", "Yes. Nexmart uses industry-standard security practices to help protect payment information."),
        ("Does Nexmart support Cash on Delivery?", "Cash on Delivery is available for eligible products and supported regions where sellers offer this option."),
        ("Can I save my payment methods?", "Yes. You can securely save supported payment methods for faster checkout."),
        ("Will I receive an invoice?", "Yes. An order confirmation and invoice are available after a successful purchase.")
    ],
    "ACCOUNT": [
        ("How do I create an account?", "Select Sign Up and follow the registration process using your email or other supported authentication methods."),
        ("How do I reset my password?", "Use the Forgot Password option on the login page and follow the instructions sent to your email."),
        ("Can I update my personal information?", "Yes. Your profile settings allow you to update personal details, addresses, and preferences."),
        ("Can I delete my account?", "You may request account deletion through your account settings or by contacting support."),
        ("How does Nexmart protect my privacy?", "We handle personal information according to our Privacy Policy and applicable data protection regulations.")
    ],
    "BUSINESS & PARTNERS": [
        ("Can businesses sell on Nexmart?", "Business onboarding information will be shared as our seller ecosystem continues to expand."),
        ("Can I partner with Nexmart?", "Yes. We welcome partnership opportunities with businesses, technology providers, and strategic collaborators."),
        ("Do you offer enterprise solutions?", "Enterprise capabilities are being expanded to support larger organizations with AI-powered commerce solutions."),
        ("How can I contact the sales team?", "Sales enquiries can be submitted through the Contact page."),
        ("How can I report an issue?", "You can contact our support team through the Contact page with details of the issue you're experiencing."),
        ("Where can I learn how to use Nexmart?", "Nexmart University will provide tutorials, guides, and educational resources as it launches."),
        ("How do I stay updated on new features?", "Follow the Nexmart Blog and community channels for announcements, feature releases, and platform updates."),
        ("Where can I get additional help?", "If you can't find the answer you're looking for, visit the Contact page and our team will be happy to assist.")
    ]
}

faq_html_blocks = []

for section_name, questions in faqs.items():
    section_html = f"""
    <div class="faq-category" style="margin-bottom: 60px;">
        <h2 style="font-size: 24px; font-weight: 600; color: #fff; margin-bottom: 24px; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 12px; line-height: 1.3;">{section_name}</h2>
        <div class="faq-list" style="display: flex; flex-direction: column; gap: 16px;">
    """
    
    for q, a in questions:
        item_html = f"""
            <details class="faq-item" style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 12px; overflow: hidden; transition: background 0.3s ease; margin: 0; padding: 0;">
                <summary style="padding: 24px; font-size: 18px; font-weight: 500; color: #fff; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center; outline: none; margin: 0;">
                    <span style="display: block; line-height: 1.4;">{q}</span>
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="faq-icon" style="transition: transform 0.3s ease; opacity: 0.6; flex-shrink: 0; margin-left: 16px;"><polyline points="6 9 12 15 18 9"></polyline></svg>
                </summary>
                <div style="padding: 0 24px 24px 24px; font-size: 16px; color: #94A3B8; line-height: 1.6; margin: 0;">
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

all_faqs = "\\n".join(faq_html_blocks)

faq_section_wrapper = f"""
<!-- using a standard div to avoid global section Webflow interaction styles -->
<div class="semantic-faq-wrapper" style="padding-top: 60px; padding-bottom: 120px; width: 100%; display: block;">
  <div style="max-width: 800px; margin: 0 auto; padding: 0 5%; width: 100%; box-sizing: border-box;">
      {all_faqs}
  </div>
  <style>
      .semantic-faq-wrapper .faq-item:hover {{
          background: rgba(255,255,255,0.04) !important;
      }}
      .semantic-faq-wrapper details.faq-item[open] .faq-icon {{
          transform: rotate(180deg);
      }}
      .semantic-faq-wrapper details.faq-item summary::-webkit-details-marker {{
          display: none;
      }}
  </style>
</div>
"""

with open('faqs.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = bs4.BeautifulSoup(html, 'html.parser')

# Find hero and ONLY update the text content, preserve all structure/classes completely
hero = soup.find('section', class_=lambda c: c and 'is-hero' in c)
if hero:
    h1 = hero.find('h1')
    if h1:
        h1.string = "Frequently Asked Questions"
    p = hero.find('p')
    if p:
        p.string = "Everything you need to know about Nexmart, Agentic Commerce, shopping, orders, payments, shipping, and using our AI-powered commerce platform."

# Find placeholder and replace its parent section with our semantic wrapper
placeholder = soup.find(string=lambda text: text and 'Content Coming Soon' in text)
if placeholder:
    section_to_replace = placeholder.find_parent('section')
    if section_to_replace:
        new_section = bs4.BeautifulSoup(faq_section_wrapper, 'html.parser')
        section_to_replace.replace_with(new_section)

# Update page title
if soup.title:
    soup.title.string = "Nexmart - Frequently Asked Questions"

with open('faqs.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Successfully injected FAQ content cleanly.")
