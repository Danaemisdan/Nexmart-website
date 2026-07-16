import re
import glob

html = open('index.html', encoding='utf-8').read()
res = re.search(r'<div class="footer_link-wrap">[^<]*<div[^>]*><p>Resources</p></div>.*?</ul></div>', html)
if res:
    print(res.group(0))
else:
    print('Not found')
