import bs4
import re

with open('index.html', 'r', encoding='utf-8') as f:
    idx_html = f.read()

with open('advertiser-tracker.html', 'r', encoding='utf-8') as f:
    tgt_html = f.read()

# We can find the exact indices. The nav starts with '<div data-animation="default"' and ends right before '<main class="main-wrapper"'
start_idx_index = idx_html.find('<div data-animation="default"')
end_idx_index = idx_html.find('<main class="main-wrapper"')

if start_idx_index == -1 or end_idx_index == -1:
    print("Could not find nav bounds in index.html")
else:
    correct_nav_str = idx_html[start_idx_index:end_idx_index]
    
    start_tgt_index = tgt_html.find('<div data-animation="default"')
    end_tgt_index = tgt_html.find('<main class="main-wrapper"')
    
    if start_tgt_index == -1 or end_tgt_index == -1:
        print("Could not find nav bounds in advertiser-tracker.html")
    else:
        new_tgt_html = tgt_html[:start_tgt_index] + correct_nav_str + tgt_html[end_tgt_index:]
        with open('advertiser-tracker.html', 'w', encoding='utf-8') as f:
            f.write(new_tgt_html)
        print("Successfully replaced nav block by exact string slicing.")
