import os

def fix_urls(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content.replace('./cdn.prod.website-files.com/', 'https://cdn.prod.website-files.com/')
    new_content = new_content.replace('./d3e54v103j8qbb.cloudfront.net/', 'https://d3e54v103j8qbb.cloudfront.net/')
    new_content = new_content.replace('"cdn.prod.website-files.com/', '"https://cdn.prod.website-files.com/')
    new_content = new_content.replace('href=\"css/', 'href=\"https://cdn.prod.website-files.com/69c4a4d640fdca68c1cc9685/css/')
    
    if new_content != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print('Fixed URLs in', filename)
    else:
        print('No URLs needed fixing in', filename)

fix_urls('agentic-commerce.html')
fix_urls('magic-ai-search.html')
