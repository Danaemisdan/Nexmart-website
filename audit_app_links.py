import glob
import json
import html.parser
import re

class AppLinkParser(html.parser.HTMLParser):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.elements = []
        self.current_element = None
        self.capture_text = False

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        href = attrs_dict.get('href', '')
        
        if tag == 'a' and 'https://app.nexmartshop.ai' in href:
            self.current_element = {
                'file': self.filename,
                'href': href,
                'text': '',
                'classes': attrs_dict.get('class', '')
            }
            self.capture_text = True
            
        elif self.capture_text and tag == 'img':
            alt = attrs_dict.get('alt', '')
            if alt:
                self.current_element['text'] += f'[Image: {alt}] '
            else:
                self.current_element['text'] += '[Image] '

    def handle_endtag(self, tag):
        if tag == 'a' and self.current_element:
            self.elements.append(self.current_element)
            self.current_element = None
            self.capture_text = False

    def handle_data(self, data):
        if self.capture_text and self.current_element:
            self.current_element['text'] += data.strip() + ' '

results = []
for file in glob.glob('*.html'):
    parser = AppLinkParser(file)
    with open(file, 'r', encoding='utf-8') as f:
        parser.feed(f.read())
    results.extend(parser.elements)

# Grouping and generating report
report = [
    "# Nexmart App Redirects Audit",
    "This report catalogs every link pointing to `https://app.nexmartshop.ai` across the entire website.",
    ""
]

unique_links = {}
for item in results:
    text = item['text']
    text = re.sub(r'(@keyframes.*?\}|\.[\w-]+\s*\{.*?\})', '', text, flags=re.DOTALL)
    text = re.sub(r'\s+', ' ', text).strip()
    if not text:
        text = "(Empty/Icon)"
        
    href = item['href']
    file = item['file']
    
    key = f"{href}::{text}"
    if key not in unique_links:
        unique_links[key] = {
            'text': text,
            'href': href,
            'files': set(),
            'purpose': 'Unknown',
            'group': 'C'
        }
    unique_links[key]['files'].add(file)

# Business Logic Grouping
for key, data in unique_links.items():
    href = data['href']
    text = data['text'].lower()
    
    # Determine purpose
    if 'login' in href or 'sign-up' in href or 'start free trial' in text or 'sign in' in text or 'start shopping' in text:
        data['purpose'] = "Authentication / Onboarding"
        data['group'] = 'A' # Must be external app
        
    elif 'solutions' in href or 'videos' in href or 'product-library' in href:
        data['purpose'] = "Product Demo / Solution Showcase"
        data['group'] = 'A' # Likely deep links into the app features
        
    elif 'pricing' in href:
        data['purpose'] = "Pricing Page"
        data['group'] = 'B' # Should usually be a marketing page
        
    elif 'blog' in href or 'article' in text:
        data['purpose'] = "Blog / Content"
        data['group'] = 'B' # Blogs are typically hosted on the main marketing site
        
    elif 'about' in href:
        data['purpose'] = "About Us Page"
        data['group'] = 'B' # About us is standard marketing
        
    elif 'contact' in href:
        data['purpose'] = "Contact Page"
        data['group'] = 'B' # Contact is standard marketing
        
    elif 'faq' in href:
        data['purpose'] = "FAQ Page"
        data['group'] = 'B' # FAQs are standard marketing
        
    elif 'affiliate' in href:
        data['purpose'] = "Affiliate Program"
        data['group'] = 'B' # Standard marketing
        
    elif 'university' in href:
        data['purpose'] = "Course / University"
        data['group'] = 'C' # Could be LMS on main site, or inside app
        
    elif href == 'https://app.nexmartshop.ai/' or href == 'https://app.nexmartshop.ai':
        data['purpose'] = "App Dashboard / Homepage Redirect"
        data['group'] = 'B' # Homepage Logo / Language switchers usually shouldn't dump users into the app unauthenticated
    
    elif 'cookie-policy' in href or 'privacy' in href or 'terms' in href:
         data['purpose'] = "Legal Pages"
         data['group'] = 'B'
    else:
        data['purpose'] = "Other / Miscellaneous"
        data['group'] = 'C'

def generate_table(group_id, title, desc):
    md = [f"## {title}", desc, "", "| Link Text | Exact URL | Purpose | Files Present In |", "|---|---|---|---|"]
    for key, data in sorted(unique_links.items(), key=lambda x: x[1]['href']):
        if data['group'] == group_id:
            files_str = f"{len(data['files'])} files (e.g. {list(data['files'])[0]})"
            md.append(f"| {data['text'][:60]} | `{data['href']}` | {data['purpose']} | {files_str} |")
    return "\\n".join(md)

report.append(generate_table('A', "A. These should remain external", "Links related to user authentication, onboarding, and deep-app functionality. These are strictly application concerns."))
report.append("")
report.append(generate_table('B', "B. These should instead point to local pages", "Links related to top-of-funnel marketing, blogs, pricing, contact, and legal information. These traditionally live on the public-facing marketing website to improve SEO and user experience before signup."))
report.append("")
report.append(generate_table('C', "C. Unsure / needs business decision", "Links where context dictates whether it should be gated inside the app or open on the marketing site."))

with open('app_redirects_report.md', 'w', encoding='utf-8') as f:
    f.write("\\n".join(report))
print("Report generated.")
