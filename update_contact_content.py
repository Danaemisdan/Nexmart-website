import bs4
import re

with open('contact.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = bs4.BeautifulSoup(html, 'html.parser')

# Helper function to find a tag by exact string
def replace_text(tag_name, old_text, new_text):
    for tag in soup.find_all(tag_name):
        if tag.string and old_text in tag.string:
            tag.string = tag.string.replace(old_text, new_text)

# 1. Update Hero
h1 = soup.find('h1')
if h1 and 'Contact Nexmart' in h1.text:
    h1.string = "Let's Build The Future Together"

hero_p = soup.find('p', string=re.compile('Whether you need support'))
if hero_p:
    hero_p.string = "Whether you're a shopper, seller, enterprise partner, investor, or media organization, our team is ready to help you explore the future of Agentic Commerce."

# 2. Section 1 (Intelligent Contact Routing)
h2_routing = soup.find('h2', string='Intelligent Contact Routing')
if h2_routing:
    h2_routing.string = "How Can We Help?"
    # It doesn't have a paragraph. Let's add one, maintaining the style format from Section 3
    h2_routing['style'] = h2_routing.get('style', '').replace('margin-bottom: 64px', 'margin-bottom: 24px')
    
    new_p = soup.new_tag('p')
    new_p.string = "One conversation can save hours. Choose the team that best matches your enquiry and we'll connect you with the right specialists."
    new_p['style'] = "font-size: 20px; color: #4B5563; line-height: 1.7; margin: 0 auto 64px auto; text-align: center; max-width: 680px;"
    h2_routing.insert_after(new_p)

# Replace Card 1
h3_support = soup.find('h3', string='Support')
if h3_support:
    h3_support.string = "Customer Support"
p_support = soup.find('p', string='Questions about orders, accounts, payments or platform usage.')
if p_support:
    p_support.string = "Need help with orders, payments, deliveries or your Nexmart account? Our support specialists are ready to help."

# Replace Card 2
h3_sales = soup.find('h3', string='Sales')
if h3_sales:
    h3_sales.string = "Business Solutions"
p_sales = soup.find('p', string='Learn how Nexmart can help your business adopt Agentic Commerce.')
if p_sales:
    p_sales.string = "Discover how Nexmart can help your business grow with AI shopping agents, automation, and commerce intelligence."

# Replace Card 3
p_partnerships = soup.find('p', string='Discuss integrations, enterprise opportunities and collaborations.')
if p_partnerships:
    p_partnerships.string = "Collaborate with Nexmart on retail innovation, logistics, enterprise integrations, or strategic partnerships."

# Replace Card 4
p_press = soup.find('p', string='Media enquiries, interviews and announcements.')
if p_press:
    p_press.string = "Looking to feature Nexmart or speak with our leadership team? We'd love to hear from you."

# Replace Contact -> Links
card_links = soup.find_all('div', class_='card-link')
link_map = {
    0: "Talk to Support ",
    1: "Speak with Sales ",
    2: "Start a Partnership ",
    3: "Media Enquiries "
}
for i, link in enumerate(card_links):
    if i in link_map and 'Contact' in link.text:
        # Link structure is text + <span>→</span>
        span = link.find('span')
        link.clear()
        link.append(link_map[i])
        link.append(span)

# 3. Section 2 (Contact Form)
h2_form = soup.find('h2', string='Send a Message')
if h2_form:
    h2_form.string = "Start The Conversation"
    h2_form['style'] = h2_form.get('style', '').replace('margin-bottom: 64px', 'margin-bottom: 24px')
    
    new_p_form = soup.new_tag('p')
    new_p_form.string = "Tell us a little about your enquiry and the appropriate Nexmart team will get back to you."
    new_p_form['style'] = "font-size: 20px; color: #4B5563; line-height: 1.7; margin: 0 auto 64px auto; text-align: center; max-width: 680px;"
    h2_form.insert_after(new_p_form)

btn_submit = soup.find('button', class_='form-submit')
if btn_submit:
    # Button has text and an SVG inside
    svg = btn_submit.find('svg')
    btn_submit.clear()
    btn_submit.append("Send Enquiry ")
    btn_submit.append(svg)

# 4. Section 3 (Find Answers Faster)
h2_answers = soup.find('h2', string='Find Answers Faster')
if h2_answers:
    h2_answers.string = "Need Help Right Now?"
p_answers = soup.find('p', string='Many questions can be answered immediately through our knowledge resources.')
if p_answers:
    p_answers.string = "Many questions already have detailed answers and step-by-step guides. Save time by exploring our knowledge resources before submitting a request."

p_faq = soup.find('p', string='Browse answers to common questions.')
if p_faq:
    p_faq.string = "Instant answers to the questions we receive most often."
    
p_uni = soup.find('p', string='Explore tutorials and product guides.')
if p_uni:
    p_uni.string = "Master Agentic Commerce through tutorials, guides, and practical learning paths."

for link in card_links:
    if 'Open FAQ' in link.text:
        span = link.find('span')
        link.clear()
        link.append("Browse FAQs ")
        link.append(span)
    elif 'Explore University' in link.text:
        span = link.find('span')
        link.clear()
        link.append("Start Learning ")
        link.append(span)

# 5. Section 4 (Global Presence)
h2_global = soup.find('h2', string='Global Presence')
if h2_global:
    h2_global.string = "Building Commerce Without Borders"
    h2_global['style'] = h2_global.get('style', '').replace('margin-bottom: 80px', 'margin-bottom: 24px')
    
    new_p_global = soup.new_tag('p')
    new_p_global.string = "Nexmart operates with a global-first mindset, combining distributed AI infrastructure with regional commerce expertise."
    new_p_global['style'] = "font-size: 20px; color: #4B5563; line-height: 1.7; margin: 0 auto 80px auto; text-align: center; max-width: 680px;"
    h2_global.insert_after(new_p_global)

p_nig = soup.find('p', string='Primary Commerce Operations')
if p_nig: p_nig.string = 'Commerce Operations'

p_glob = soup.find('p', string='International Partnerships')
if p_glob: p_glob.string = 'Enterprise Partnerships'

p_rem = soup.find('p', string='Distributed AI Team')
if p_rem: p_rem.string = 'Distributed Product Team'

# 6. Section 5 (Community)
h2_comm = soup.find('h2', string='Stay Connected')
if h2_comm:
    h2_comm.string = "Join The Nexmart Ecosystem"

p_comm = soup.find('p', string='Follow Nexmart as we build the future of Agentic Commerce.')
if p_comm:
    p_comm.string = "Follow product updates, connect with our growing community, and help shape the future of Agentic Commerce."

# 7. FINAL CTA
# The final CTA is likely the last section in the body.
# Let's find it. It might be <section class="section is-cta"> or similar.
sections = soup.find_all('section')
if len(sections) > 1:
    cta_section = sections[-1] # From build_contact.py, the last section is the global CTA
    h2_cta = cta_section.find('h2')
    if h2_cta:
        h2_cta.string = "Ready To Experience Agentic Commerce?"
    p_cta = cta_section.find('p')
    if p_cta:
        p_cta.string = "Join thousands of shoppers and businesses discovering a faster, smarter way to buy, sell, and grow with AI."

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Contact page content updated successfully.")
