import bs4
import copy

def run():
    # Load index.html to act as our component library
    with open('index.html', 'r', encoding='utf-8') as f:
        idx_soup = bs4.BeautifulSoup(f, 'html.parser')
    
    idx_main = idx_soup.find('main')
    idx_sections = idx_main.find_all('section', recursive=False)
    
    # Extract components
    hero_comp = copy.copy(idx_sections[0])
    tabs_comp = copy.copy(idx_sections[1])
    cards_comp = copy.copy(idx_sections[3]) # Grid of cards (Why Nexmart?)
    workflow_comp = copy.copy(idx_sections[4]) # Workflow
    cta_comp = copy.copy(idx_sections[5]) # Final CTA
    
    # ----------------------------------------------------
    # 1. Product Hero Redesign
    # ----------------------------------------------------
    # Remove marquee
    marquee = hero_comp.find(class_='hero_marquee-wrap')
    if marquee: marquee.decompose()
    
    # Update Hero Content
    h1 = hero_comp.find('h1')
    if h1: h1.string = "Agentic Commerce"
    
    p = hero_comp.find('p', class_='text-size-medium')
    if p: p.string = "Deploy autonomous AI agents to handle the entire shopping and procurement lifecycle—from product discovery to tracking."
    
    a_btn = hero_comp.find('a', class_='button-main')
    if a_btn: 
        a_btn['href'] = "https://app.nexmartshop.ai/sign-up"
        btn_txt = a_btn.find('div', string=lambda t: t and 'Nexmart' in t)
        if not btn_txt: btn_txt = a_btn.find('div')
        if btn_txt: btn_txt.string = "Start Shopping With AI"
        
    # Replace Hero graphic
    # Find the hero icon/graphic
    hero_graphic = hero_comp.find('img', class_='hero_icon-svg')
    if hero_graphic:
        # We will use an existing asset that represents orchestration/AI.
        hero_graphic['src'] = "https://cdn.prod.website-files.com/69c4a4d640fdca68c1cc9685/69d1e06831e27963bd87b2c7_Product%20Library%20-%20Small.svg" # A proxy for AI agents
    
    # Inject Custom CSS for Deep Royal Blue Gradient on Hero
    # We will append a style block to the hero section
    style = idx_soup.new_tag('style')
    style.string = """
    .is-hero { background: linear-gradient(135deg, #f8f9fc 0%, #e6edf7 100%); position: relative; }
    .is-hero::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 100%; background: radial-gradient(circle at 50% -20%, rgba(26, 54, 93, 0.08) 0%, transparent 60%); pointer-events: none; }
    """
    hero_comp.append(style)

    # ----------------------------------------------------
    # 2. Meet Your AI Agents (Cards)
    # ----------------------------------------------------
    agents_comp = copy.copy(cards_comp)
    agents_h2 = agents_comp.find('h2')
    if agents_h2: agents_h2.string = "Meet Your AI Agents"
    agents_p = agents_comp.find('p', class_='text-size-medium')
    if agents_p: agents_p.string = "Our platform deploys specialized agents for every step of the commerce lifecycle."
    
    # We need 5-6 cards. The component has some cards. Let's find the grid.
    agents_grid = agents_comp.find('div', class_='grid')
    if agents_grid:
        card_template = agents_grid.find('div', class_='benefit-card')
        if card_template:
            agents_grid.clear()
            agents_data = [
                {"t": "Discovery Agent", "d": "Finds products matching your exact needs, preferences, and budgets across millions of listings."},
                {"t": "Price & Coupon Agent", "d": "Tracks prices across sellers and automatically applies discounts, promotions, and cashback."},
                {"t": "Negotiation Agent", "d": "Communicates directly with sellers to secure better offers and bulk pricing."},
                {"t": "Quality Agent", "d": "Verifies authenticity, seller reputation, and warranty information before purchase."},
                {"t": "Checkout Agent", "d": "Builds your cart and handles secure payment and order processing seamlessly."},
                {"t": "Tracking & Support", "d": "Monitors deliveries in real-time and manages returns, refunds, and exchanges."}
            ]
            for ad in agents_data:
                new_c = copy.copy(card_template)
                h3 = new_c.find(['h3', 'div'], class_=lambda x: x and 'text-size-large' in x)
                if h3: h3.string = ad['t']
                cp = new_c.find('p')
                if cp: cp.string = ad['d']
                agents_grid.append(new_c)

    # ----------------------------------------------------
    # 3. How It Works (Workflow)
    # ----------------------------------------------------
    works_comp = copy.copy(workflow_comp)
    w_h2 = works_comp.find('h2')
    if w_h2: w_h2.string = "How Agentic Commerce Works"
    w_p = works_comp.find('p', class_='text-size-medium')
    if w_p: w_p.string = "Experience handsfree shopping today."
    
    w_grid = works_comp.find('div', class_='grid')
    if w_grid:
        w_card = w_grid.find('div', class_=lambda x: x and 'card' in x.lower())
        if w_card:
            w_grid.clear()
            w_data = [
                {"t": "User Intent", "d": "Simply input what you want. No endless searching or comparison fatigue."},
                {"t": "AI Planning", "d": "Agents analyze your intent and formulate a comprehensive procurement strategy."},
                {"t": "Parallel Collaboration", "d": "Our 9 AI agents discover, research, and negotiate in parallel."},
                {"t": "Best Recommendation", "d": "Agents compile and present the absolute best options available."},
                {"t": "Purchase", "d": "Approve the final cart, and the system securely handles checkout."}
            ]
            for wd in w_data:
                nc = copy.copy(w_card)
                nc_title = nc.find(['h3', 'div'], class_=lambda x: x and 'text-weight-bold' in x)
                if nc_title: nc_title.string = wd['t']
                nc_p = nc.find('p')
                if nc_p: nc_p.string = wd['d']
                w_grid.append(nc)

    # ----------------------------------------------------
    # 4. Benefits (2x2 Grid)
    # ----------------------------------------------------
    ben_comp = copy.copy(cards_comp)
    b_h2 = ben_comp.find('h2')
    if b_h2: b_h2.string = "Why Agentic Commerce?"
    b_p = ben_comp.find('p', class_='text-size-medium')
    if b_p: b_p.string = "Unleash the power of AI to transform your shopping experience."
    b_grid = ben_comp.find('div', class_='grid')
    if b_grid:
        b_card = b_grid.find('div', class_='benefit-card')
        if b_card:
            b_grid.clear()
            # Set grid to 2 columns on desktop
            b_grid['data-grid-column-desktop'] = "2"
            b_data = [
                {"t": "Less Searching", "d": "Never spend hours scrolling through pages again. Agents find exactly what you need."},
                {"t": "Better Prices", "d": "Agents actively negotiate and apply the best coupons automatically."},
                {"t": "Smarter Decisions", "d": "Data-driven insights ensure you buy the highest quality product."},
                {"t": "Faster Shopping", "d": "Achieve your procurement goals in minutes instead of days."}
            ]
            for bd in b_data:
                nc = copy.copy(b_card)
                nc_title = nc.find(['h3', 'div'], class_=lambda x: x and 'text-size-large' in x)
                if nc_title: nc_title.string = bd['t']
                nc_p = nc.find('p')
                if nc_p: nc_p.string = bd['d']
                b_grid.append(nc)

    # ----------------------------------------------------
    # 5. Real-world Use Cases (Tabs)
    # ----------------------------------------------------
    tabs_comp = copy.copy(tabs_comp)
    t_h2 = tabs_comp.find('h2')
    if t_h2: t_h2.string = "Who Uses Agentic Commerce?"
    t_p = tabs_comp.find('p', class_='text-size-medium')
    if t_p: t_p.string = "Built to scale for diverse procurement needs."
    
    t_menu = tabs_comp.find('div', class_='home-tab_menu')
    t_content = tabs_comp.find('div', class_='home-tab_content')
    if t_menu and t_content:
        tab_links = t_menu.find_all('button', class_='home-tab-item__link')
        tab_panes = t_content.find_all('div', class_='home-tab_pane')
        
        u_data = [
            {"name": "Shopping", "title": "Everyday Consumers", "desc": "Stop browsing. Let AI find better prices and execute purchases while you sleep."},
            {"name": "Business Procurement", "title": "E-commerce Merchants", "desc": "Use agents to identify trending products, monitor competitors, and streamline sourcing."},
            {"name": "Bulk Purchasing", "title": "Enterprise Brands", "desc": "Deploy intelligent shopping agents to automate bulk procurement and optimize supplier relationships."},
            {"name": "Everyday Commerce", "title": "Time-saving", "desc": "Reclaim your time by offloading all purchasing decisions and order tracking to autonomous AI."}
        ]
        
        # We only need 4 tabs
        for idx in range(len(tab_links)):
            if idx < len(u_data):
                txt = tab_links[idx].find('div')
                if txt: txt.string = u_data[idx]['name']
                
                pane = tab_panes[idx]
                p_title = pane.find('h3')
                if p_title: p_title.string = u_data[idx]['title']
                p_desc = pane.find('p')
                if p_desc: p_desc.string = u_data[idx]['desc']
            else:
                # hide or remove extra tabs
                tab_links[idx].decompose()
                tab_panes[idx].decompose()

    # ----------------------------------------------------
    # 6. Final CTA
    # ----------------------------------------------------
    cta_h2 = cta_comp.find('h2')
    if cta_h2: cta_h2.string = "Experience true Agentic Commerce today"
    cta_p = cta_comp.find('p', class_='text-size-medium')
    if cta_p: cta_p.string = "Save time, save money, and shop smarter. Your AI agents never sleep."
    c_btn = cta_comp.find('a', class_='button-main')
    if c_btn:
        c_btn['href'] = "https://app.nexmartshop.ai/sign-up"
        btn_txt = c_btn.find('div', string=lambda t: t and 'Nexmart' in t)
        if not btn_txt: btn_txt = c_btn.find('div')
        if btn_txt: btn_txt.string = "Start Shopping With AI"

    # Assemble the new main wrapper
    with open('agentic-commerce.html', 'r', encoding='utf-8') as f:
        ag_soup = bs4.BeautifulSoup(f, 'html.parser')
    
    ag_main = ag_soup.find('main')
    if ag_main:
        ag_main.clear()
        ag_main.append(hero_comp)
        ag_main.append(agents_comp)
        ag_main.append(works_comp)
        ag_main.append(ben_comp)
        ag_main.append(tabs_comp)
        ag_main.append(cta_comp)
        
        # Don't forget to append the footer which is part of agentic-commerce.html main originally
        footer = idx_main.find('footer')
        if footer:
            ag_main.append(copy.copy(footer))
            
    with open('agentic-commerce.html', 'w', encoding='utf-8') as f:
        f.write(str(ag_soup))
        
    print("Agentic Commerce Redesign Complete.")

if __name__ == '__main__':
    run()
