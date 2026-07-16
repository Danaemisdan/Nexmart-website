import bs4

def run():
    with open('product-template.html', 'r', encoding='utf-8') as f:
        soup = bs4.BeautifulSoup(f, 'html.parser')

    body = soup.find('body')
    if body:
        # Add body attributes
        classes = body.get('class', [])
        if 'theme-color-blue' not in classes:
            classes.append('theme-color-blue')
        body['class'] = classes
        body['data-barba'] = 'wrapper'

    page_wrapper = soup.find(class_='page-wrapper')
    if page_wrapper:
        # Check if main-wrapper already exists
        if not page_wrapper.find('main', class_='main-wrapper'):
            # Create the new main wrapper
            main_tag = soup.new_tag('main')
            main_tag['class'] = 'main-wrapper'
            main_tag['data-barba'] = 'container'

            # Move all contents except global_elements into main_tag
            children_to_move = []
            for child in page_wrapper.children:
                if isinstance(child, bs4.Tag):
                    if 'global_elements' in child.get('class', []):
                        continue
                children_to_move.append(child)

            for child in children_to_move:
                child.extract()
                main_tag.append(child)

            page_wrapper.append(main_tag)

    with open('product-template.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    print("product-template.html fixed successfully.")

if __name__ == '__main__':
    run()
