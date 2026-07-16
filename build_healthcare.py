from bs4 import BeautifulSoup

def process_template():
    with open('product-template.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        
    # Replace Meta/Title
    title = soup.find('title')
    if title: title.string = "Healthcare Access - Nexmart"
    meta_desc = soup.find('meta', attrs={'name': 'description'})
    if meta_desc: meta_desc['content'] = "Nexmart Healthcare Access connects communities to vital health services, telemedicine, and pharmacy support through our nationwide smart hubs."
    
    html_str = str(soup)
    
    replacements = {
        "[Product Name]": "Healthcare Access",
        "[Hero Description / Tagline]": "Connecting communities to vital health services through our nationwide minimart network and AI-powered platforms.",
        "[Primary CTA]": "Get Healthcare Support",
        
        "[Product Overview Heading]": "Comprehensive Care, Accessible Anywhere",
        "[Detailed Product Overview Description explaining the core value proposition.]": "Nexmart bridges the gap between digital healthcare and physical access. By combining our nationwide network of smart hubs with agentic AI, we provide seamless access to telemedicine, pharmacy services, and essential health resources directly from your local minimart.",
        "[Learn More CTA]": "Find a Hub Near You",
        
        "[Key Features]": "Why Choose Nexmart Healthcare",
        "[Subtitle explaining why these features matter]": "We integrate physical convenience with advanced AI to deliver uncompromising care.",
        
        "[Feature 1 Title]": "Telemedicine Kiosks",
        "[Feature 1 detailed description emphasizing value.]": "Connect with certified medical professionals instantly from any Nexmart location.",
        "[Feature 2 Title]": "Pharmacy Integration",
        "[Feature 2 detailed description emphasizing value.]": "Order, track, and pick up essential prescriptions securely at your local hub.",
        "[Feature 3 Title]": "AI Health Assistant",
        "[Feature 3 detailed description emphasizing value.]": "Use our intelligent agents to find the right specialists and book appointments.",
        "[Feature 4 Title]": "Insurance Enrollment",
        "[Feature 4 detailed description emphasizing value.]": "Easily compare and enroll in accessible health insurance plans on-site.",
        "[Feature 5 Title]": "Walk-in Screenings",
        "[Feature 5 detailed description emphasizing value.]": "Access basic diagnostics and wellness checks without a prior appointment.",
        "[Feature 6 Title]": "Secure Health Records",
        "[Feature 6 detailed description emphasizing value.]": "Manage and access your medical history safely across the entire Nexmart network.",
        
        "[How It Works]": "How Healthcare Access Works",
        "[Step-by-step product workflow explanation]": "Getting the care you need is as simple as visiting your local minimart.",
        
        "[Step 1 Name]": "Visit a Hub or Go Online",
        "[Step 1 explanation]": "Access our healthcare services through the Nexmart app or at any physical minimart location.",
        "[Step 2 Name]": "Consult with AI or Doctors",
        "[Step 2 explanation]": "Use our AI to triage symptoms or connect directly with a telemedicine professional.",
        "[Step 3 Name]": "Receive Care and Prescriptions",
        "[Step 3 explanation]": "Get immediate guidance, referrals, and pick up prescribed medications on the spot.",
        
        "[Use Cases / Industries]": "Who Benefits from Nexmart Healthcare?",
        "[Explore how different teams use this product]": "Our distributed network is designed to serve diverse health needs.",
        
        "[Use Case 1]": "Individuals & Families",
        "[Use Case 1 Benefit]": "Accessible Everyday Care",
        "[Explanation of how the product solves problems for Use Case 1]": "Affordable care for everyday health needs, pediatrics, and urgent consultations without the wait times of traditional clinics.",
        
        "[Use Case 2]": "Rural Communities",
        "[Use Case 2 Benefit]": "Bridging the Distance",
        "[Explanation of how the product solves problems for Use Case 2]": "Bringing essential medical services and expert consultations to underserved and remote areas through our physical hubs.",
        
        "[Use Case 3]": "Corporate Wellness",
        "[Use Case 3 Benefit]": "Employee Health Support",
        "[Explanation of how the product solves problems for Use Case 3]": "Providing businesses with a distributed network for employee health screenings, vaccinations, and preventative care.",
        
        "[View Use Case CTA]": "Learn More",
        
        "[Ready to get started?]": "Prioritize your health with Nexmart",
        "[Final compelling reason to sign up right now]": "Join thousands of individuals who trust our agentic network for seamless, accessible healthcare.",
        "[Final CTA Button]": "Find a Healthcare Hub"
    }
    
    for old, new in replacements.items():
        html_str = html_str.replace(old, new)
        
    with open('healthcare-access.html', 'w', encoding='utf-8') as f:
        f.write(html_str)

process_template()
