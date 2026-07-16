from bs4 import BeautifulSoup

def process_template():
    with open('product-template.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        
    # Replace Meta/Title
    title = soup.find('title')
    if title: title.string = "Healthcare Commerce - Nexmart"
    meta_desc = soup.find('meta', attrs={'name': 'description'})
    if meta_desc: meta_desc['content'] = "Empower your healthcare business with Nexmart's agentic commerce. Expand reach, automate orders, and integrate into our nationwide marketplace."
    
    html_str = str(soup)
    
    replacements = {
        "[Product Name]": "Healthcare Commerce on Nexmart",
        "[Hero Description / Tagline]": "Empower your healthcare business with agentic commerce. Expand your reach, automate order management, and seamlessly integrate into our nationwide marketplace.",
        "[Primary CTA]": "Join the Marketplace",
        
        "[Product Overview Heading]": "Connect Your Healthcare Services to Millions",
        "[Detailed Product Overview Description explaining the core value proposition.]": "Nexmart provides healthcare merchants, pharmacies, and medical suppliers with a robust digital infrastructure. By joining our platform, your products and services become instantly discoverable through our AI-powered Agentic Commerce engine, driving growth and simplifying logistics.",
        "[Learn More CTA]": "Become a Merchant",
        
        "[Key Features]": "Platform Capabilities for Healthcare",
        "[Subtitle explaining why these features matter]": "We equip healthcare businesses with the tools needed to scale securely and efficiently in a digital-first economy.",
        
        "[Feature 1 Title]": "AI-Powered Discovery",
        "[Feature 1 detailed description emphasizing value.]": "Ensure your healthcare products are intelligently matched with customers actively searching for them using our agents.",
        "[Feature 2 Title]": "Secure Payments",
        "[Feature 2 detailed description emphasizing value.]": "Process transactions confidently with our integrated, compliant payment gateways designed for scale and reliability.",
        "[Feature 3 Title]": "Seamless Order Management",
        "[Feature 3 detailed description emphasizing value.]": "Automate fulfillment workflows and track your orders in real-time through our centralized merchant dashboard.",
        "[Feature 4 Title]": "Nationwide Logistics",
        "[Feature 4 detailed description emphasizing value.]": "Tap into Nexmart’s robust physical network for efficient, nationwide delivery and product distribution.",
        "[Feature 5 Title]": "Marketplace Reach",
        "[Feature 5 detailed description emphasizing value.]": "Expand beyond your local geography and present your vital services to millions of active Nexmart users.",
        "[Feature 6 Title]": "Data-Driven Insights",
        "[Feature 6 detailed description emphasizing value.]": "Monitor sales performance, track revenue trends, and optimize your inventory using our advanced analytics tools.",
        
        "[How It Works]": "How to Sell on Nexmart",
        "[Step-by-step product workflow explanation]": "Integrating your healthcare business into our agentic network is straightforward and designed for rapid growth.",
        
        "[Step 1 Name]": "Register Your Business",
        "[Step 1 explanation]": "Create your merchant profile, verify your credentials, and list your healthcare products on the Nexmart platform.",
        "[Step 2 Name]": "AI Driven Matching",
        "[Step 2 explanation]": "Our agentic commerce engine automatically surfaces your offerings to relevant, high-intent consumer searches.",
        "[Step 3 Name]": "Fulfill and Grow",
        "[Step 3 explanation]": "Manage incoming orders easily while Nexmart handles the underlying transaction security and logistics network.",
        
        "[Use Cases / Industries]": "Built for Healthcare Providers",
        "[Explore how different teams use this product]": "Our marketplace architecture is highly adaptable to various sectors within the healthcare industry.",
        
        "[Use Case 1]": "Pharmacies & Dispensaries",
        "[Use Case 1 Benefit]": "Digital Inventory Management",
        "[Explanation of how the product solves problems for Use Case 1]": "Digitize your physical inventory and reach patients faster through automated product discovery and integrated local fulfillment.",
        
        "[Use Case 2]": "Medical Suppliers",
        "[Use Case 2 Benefit]": "Streamlined Distribution",
        "[Explanation of how the product solves problems for Use Case 2]": "Simplify B2B and B2C equipment sales with our secure checkout flows and leverage our nationwide distribution network.",
        
        "[Use Case 3]": "Health Service Providers",
        "[Use Case 3 Benefit]": "Direct Patient Connection",
        "[Explanation of how the product solves problems for Use Case 3]": "Offer essential local services through our marketplace, connecting directly with users actively seeking care and wellness products.",
        
        "[View Use Case CTA]": "Explore Solutions",
        
        "[Ready to get started?]": "Accelerate your healthcare business",
        "[Final compelling reason to sign up right now]": "Join the future of agentic commerce and scale your operations effortlessly on the Nexmart platform.",
        "[Final CTA Button]": "Start Selling Today"
    }
    
    for old, new in replacements.items():
        html_str = html_str.replace(old, new)
        
    with open('healthcare-access.html', 'w', encoding='utf-8') as f:
        f.write(html_str)

process_template()
