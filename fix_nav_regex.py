import bs4
import re

with open('index.html', 'r', encoding='utf-8') as f:
    idx_html = f.read()

with open('advertiser-tracker.html', 'r', encoding='utf-8') as f:
    tgt_html = f.read()

# We need the nav string from index.html.
# The global navigation wrapper has data-animation="default"
match_idx = re.search(r'<div data-animation="default"[\s\S]*?</nav>\s*</div>\s*</div>\s*</div>', idx_html)
if match_idx:
    correct_nav_str = match_idx.group(0)
    print("Found correct nav string.")
    
    match_tgt = re.search(r'<div data-animation="default"[\s\S]*?</nav>\s*</div>\s*</div>\s*</div>', tgt_html)
    if match_tgt:
        corrupt_nav_str = match_tgt.group(0)
        new_tgt_html = tgt_html.replace(corrupt_nav_str, correct_nav_str)
        with open('advertiser-tracker.html', 'w', encoding='utf-8') as f:
            f.write(new_tgt_html)
        print("Successfully replaced nav block in advertiser-tracker.html.")
    else:
        print("Could not find corrupt nav block.")
else:
    print("Could not find correct nav block.")
