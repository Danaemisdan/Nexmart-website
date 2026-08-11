import re

with open('scratch/nav.txt', 'r', encoding='utf-8') as f:
    content = f.read()

print('Original length:', len(content))

# Remove is-video
content = re.sub(r'<div class="mega-nav__panel-col is-video".*?</ul></div>', '', content, flags=re.DOTALL)

# Remove all is-bottom
content = re.sub(r'<div class="mega-nav__panel-col is-bottom".*?</ul></div>', '', content, flags=re.DOTALL)

print('New length:', len(content))

with open('scratch/nav_fixed.txt', 'w', encoding='utf-8') as f:
    f.write(content)
