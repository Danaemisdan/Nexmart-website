import json
import re

with open('audit_results.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

md = [
    "# Nexmart Homepage Clickable Elements Audit",
    "",
    "## 1. Overview",
    "This report catalogs every clickable button, navigation item, card, image, and text link on the homepage (`index.html`).",
    "",
    "## 2. Forms",
    "**Status:** No `<form>` elements were found on the homepage. Any interactive inputs (if present) are likely handled dynamically via JavaScript without semantic form tags.",
    "",
    "## 3. Comprehensive Element Audit",
    "| Element | Location | Current Destination | Status | Recommendation |",
    "|---------|----------|---------------------|--------|----------------|"
]

for item in data:
    # Cleanup Element name
    el_raw = item['element']
    el_type = el_raw.split()[0] if ' ' in el_raw else el_raw
    
    # Cleanup Text
    text = item['text']
    text = re.sub(r'(@keyframes.*?\}|\.[\w-]+\s*\{.*?\})', '', text, flags=re.DOTALL)
    text = re.sub(r'\s+', ' ', text).strip()
    if len(text) > 50:
        text = text[:47] + "..."
        
    dest = item['destination']
    
    # Determine Status & Recommendation
    if dest == "N/A":
        status = "JavaScript Action"
        rec = "Keep"
    elif dest.startswith("http") and "app.nexmartshop.ai" in dest:
        status = "External Website (App)"
        rec = "Keep"
    elif dest.startswith("http"):
        status = "External Website"
        rec = "Keep"
    elif dest.endswith(".html"):
        status = "Local Page"
        rec = "Keep"
    elif dest.startswith("#") or dest == "":
        status = "Empty/Placeholder"
        rec = "Update destination"
    else:
        status = "Unknown"
        rec = "Review"
        
    if "No Text" in text and "Image" not in text:
        text = "(Empty/Icon)"
        
    row = f"| {el_type} - {text} | {item['location']} | {dest} | {status} | {rec} |"
    md.append(row)

with open('audit_report.md', 'w', encoding='utf-8') as f:
    f.write("\n".join(md))

print("Report generated.")
