import html.parser
import sys
import json

class LinkParser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.elements = []
        self.current_element = None
        self.path = []
        self.capture_text = False

    def handle_starttag(self, tag, attrs):
        self.path.append(tag)
        attrs_dict = dict(attrs)
        
        if tag in ['a', 'button', 'form']:
            class_name = attrs_dict.get('class', '')
            
            elem = {
                'tag': tag,
                'attrs': attrs_dict,
                'text': '',
                'classes': class_name,
                'parents': list(self.path)
            }
            self.current_element = elem
            self.capture_text = True
            
        elif self.capture_text and tag == 'img':
            if 'alt' in attrs_dict and attrs_dict['alt']:
                self.current_element['text'] += f'[Image: {attrs_dict["alt"]}] '
            else:
                self.current_element['text'] += '[Image] '
                
    def handle_endtag(self, tag):
        if tag in ['a', 'button', 'form']:
            if self.current_element and self.current_element['tag'] == tag:
                self.elements.append(self.current_element)
                self.current_element = None
                self.capture_text = False
        if self.path:
            self.path.pop()

    def handle_data(self, data):
        if self.capture_text and self.current_element:
            self.current_element['text'] += data.strip() + ' '

parser = LinkParser()
with open('index.html', 'r', encoding='utf-8') as f:
    parser.feed(f.read())

results = []
for el in parser.elements:
    href = el['attrs'].get('href', el['attrs'].get('action', 'N/A'))
    text = el['text'].strip() or 'No Text'
    
    # Try to determine location
    location = "Main Content"
    parents_str = " ".join(el['parents'])
    if 'nav' in parents_str or 'mega-nav' in el['classes']:
        location = "Navigation Bar"
    elif 'footer' in parents_str or 'footer' in el['classes']:
        location = "Footer"
    elif 'hero' in el['classes'] or 'hero' in parents_str:
        location = "Hero Section"
    elif 'pricing' in el['classes'] or 'pricing' in parents_str:
        location = "Pricing Section"
        
    results.append({
        'element': el['tag'].upper() + (f" ({el['classes']})" if el['classes'] else ""),
        'text': text,
        'location': location,
        'destination': href
    })

with open('audit_results.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2)
print("Audit data saved to audit_results.json")
