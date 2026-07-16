import bs4

def update_advertiser_tracker():
    with open('advertiser-tracker.html', 'r', encoding='utf-8') as f:
        soup = bs4.BeautifulSoup(f.read(), 'html.parser')

    # 1. Hero Subtitle & Query
    # Subtitle: "A single intent orchestrates thousands of autonomous procurement decisions across the world in real time."
    subtitle_elem = soup.find(string=lambda t: t and 'A single intent orchestrates' in t)
    if subtitle_elem:
        subtitle_elem.replace_with('AI-powered competitor intelligence platform for tracking advertising strategies, spend, creatives, and campaign performance.')

    # Main Visual Component: Search query
    query_elem = soup.find(string=lambda t: t and 'Procure 500 chairs for Lagos.' in t)
    if query_elem:
        query_elem.replace_with('Analyze top-performing competitor campaigns in Q3')

    # 2. Main Visual Component: Agents
    agent_replacements = {
        'Discovery Agent': 'Campaign Detection',
        '> Querying global network...': '> Scanning global ad networks...',
        '> 4,821 suppliers found.': '> Found 12,402 active creatives.',
        'Compliance Agent': 'Creative Analysis',
        '> Verifying SOC2 / ISO...': '> Extracting messaging...',
        '> Rejecting 3,102 suppliers.': '> Identifying winning formats.',
        '> Cross-referencing ESG...': '> Breaking down emotional tone...',
        'Logistics Agent': 'Spend Intelligence',
        '> Origin constraints open.': '> Modeling competitor budgets...',
        '> Destination: LOS (Lagos).': '> Predicting spend trajectory.',
        '> Modeling DDP freight...': '> Analyzing ROI signals...'
    }
    for old, new in agent_replacements.items():
        elem = soup.find(string=lambda t: t and old in t)
        if elem:
            elem.replace_with(elem.replace(old, new))

    # Metrics on Agents
    metric_replacements = {
        'Query Time': 'Scan Time',
        'Parameter': 'Analysis',
        'Routing': 'Prediction'
    }
    for old, new in metric_replacements.items():
        elem = soup.find(string=lambda t: t and old in t)
        if elem:
            elem.replace_with(elem.replace(old, new))

    # 3. Main Visual Component: Live Campaign Feed
    table_header = soup.find(string=lambda t: t and 'Live Sourcing Matrix' in t)
    if table_header:
        table_header.replace_with('Live Campaign Feed')
        
    table_sub = soup.find(string=lambda t: t and 'Processing 1,719 viable suppliers' in t)
    if table_sub:
        table_sub.replace_with('Monitoring 1,719 active campaigns')

    # Row 1
    row1 = [
        ('Herman Miller B2B', 'Nike'),
        ('Direct Manufacturer • Michigan, USA', 'Air Max Launch • Global Omni-channel'),
        ('94,200', '$4.2M'),
        ('YTD Volume', 'Estimated Spend'),
        ('SOC2, ISO 9001', 'Video + AR'),
        ('Compliance', 'Format'),
        ('Verified Match', 'Scaling')
    ]
    # Row 2
    row2 = [
        ('Steelcase Global', 'Apple'),
        ('Global Distributor • Germany', 'Privacy on iPhone • Targeted Social'),
        ('12,400', '$2.8M'),
        ('ISO 9001', 'Carousel'),
        ('Evaluating...', 'Analyzing...')
    ]
    # Row 3
    row3 = [
        ('Knoll Corporate', 'Samsung'),
        ('Distributor • UK', 'Galaxy AI • Connected TV'),
        ('8,100', '$3.1M'),
        ('Pending Audits', 'Interactive Video'),
        ('Processing...', 'Detecting...')
    ]
    # Row 4
    row4 = [
        ('Haworth Inc', 'Sony'),
        ('Manufacturer • Netherlands', 'PlayStation 6 • Search & Display'),
        ('3,200', '$1.5M'),
        ('Awaiting Data', 'Static + GIF')
    ]

    for row_replacements in [row1, row2, row3, row4]:
        for old, new in row_replacements:
            # Handle possible partial matches safely
            elems = soup.find_all(string=lambda t: t and old in t)
            for elem in elems:
                elem.replace_with(elem.replace(old, new))

    # 4. Feature Cards
    feature_replacements = [
        # Original Title, New Title, Original Desc, New Desc
        (
            'Autonomous Discovery', 'Campaign Detection',
            'Instantly identify compliant suppliers globally without manual keyword searches.', 'Monitor every major advertising network and detect new campaigns instantly.'
        ),
        (
            'Real-Time Compliance', 'Creative Analysis',
            'Automatically verify SOC2, ISO, and ESG certifications before adding to your matrix.', 'Automatically break down messaging, visuals, hooks, emotional tone, and creative strategy.'
        ),
        (
            'Dynamic Sourcing', 'Spend Intelligence',
            'Predictive modeling ensures you always receive the best market rates.', 'Estimate competitor budgets across channels using AI prediction models.'
        ),
        (
            'Market Intelligence', 'Market Signals',
            'Identify emerging supply chain risks and alternative sourcing opportunities before they impact your business.', 'Identify emerging opportunities before competitors dominate them.'
        ),
        (
            'Global Logistics', 'Audience Insights',
            'Simulate complex DDP freight routing to calculate landed costs accurately.', 'Understand which audiences competitors are targeting and how campaigns perform.'
        ),
        (
            'AI Recommendations', 'AI Recommendations',
            'Receive actionable procurement recommendations based on global market dynamics.', 'Receive actionable recommendations based on competitor activity.'
        )
    ]

    for old_title, new_title, old_desc, new_desc in feature_replacements:
        # Some titles might have been globally replaced if they contained 'Agentic Commerce' etc, but these are generic.
        t_elem = soup.find(string=lambda t: t and old_title in t)
        if t_elem:
            t_elem.replace_with(new_title)
        
        # Descriptions can be exact or partial. We'll use exact replacement.
        d_elems = soup.find_all(string=lambda t: t and old_desc in t)
        for d in d_elems:
            d.replace_with(new_desc)

    with open('advertiser-tracker.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print("Content successfully replaced.")

if __name__ == "__main__":
    update_advertiser_tracker()
