import bs4

def update_footer_transition():
    with open('advertiser-tracker.html', 'r', encoding='utf-8') as f:
        soup = bs4.BeautifulSoup(f.read(), 'html.parser')

    # We inject a highly specific CSS rule that targets .footer_component but ONLY within this page.
    # We also target .section_cta if it exists, or the CTA's parent container.
    custom_css = """
    /* Override Global Backgrounds for Advertiser Tracker CTA & Footer ONLY */
    .footer_component {
        background: radial-gradient(circle at top center, rgba(16, 185, 129, 0.08) 0%, rgba(10, 10, 12, 1) 40%, #050505 100%) !important;
        position: relative;
    }
    .footer_component::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(16, 185, 129, 0.3), transparent);
        z-index: 10;
    }
    
    /* Remove the blue background from CTA */
    .section_cta, [class*="cta-wrap"], .section-cta {
        background: transparent !important;
    }
    """

    # We need to find the parent section of the CTA to apply a transparent background to it
    # Because the blue background is likely applied to the CTA wrapper.
    cta_text = soup.find(string=lambda t: t and 'The Future of Commerce Starts Here' in t)
    if cta_text:
        cta_container = cta_text.find_parent('div', class_='heading-wrap')
        if cta_container:
            # Add a unique class to scope our CSS
            cta_container['class'] = cta_container.get('class', []) + ['ad-cta-container']
            custom_css += """
            .ad-cta-container {
                background: transparent !important;
            }
            """
        
        # We also want to target the actual section that might have the blue background
        # Usually it's `.padding-global`'s parent. Let's just target the `main-wrapper`'s children if needed, 
        # or append `ad-cta-section` to the parent of `container-large` that holds the CTA.
        container_large = cta_text.find_parent('div', class_='container-large')
        if container_large and container_large.parent:
            container_large.parent['class'] = container_large.parent.get('class', []) + ['ad-cta-section']
            custom_css += """
            .ad-cta-section {
                background: linear-gradient(180deg, #050505 0%, rgba(10, 10, 12, 1) 100%) !important;
            }
            """

    style_tag = soup.find_all('style')[-1]
    if style_tag:
        style_tag.append(custom_css)

    with open('advertiser-tracker.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print('Added custom scoped CSS for the footer background transition.')

if __name__ == "__main__":
    update_footer_transition()
