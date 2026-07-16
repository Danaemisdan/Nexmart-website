import bs4
import copy

def run():
    with open('financial-inclusion.html', 'r', encoding='utf-8') as f:
        soup = bs4.BeautifulSoup(f, 'html.parser')

    body = soup.find('body')
    if body:
        # 1. Add body attributes
        body['class'] = body.get('class', []) + ['theme-color-blue']
        body['data-barba'] = 'wrapper'

    page_wrapper = soup.find(class_='page-wrapper')
    if page_wrapper:
        # 2. Create the new main wrapper
        main_tag = soup.new_tag('main')
        main_tag['class'] = 'main-wrapper'
        main_tag['data-barba'] = 'container'

        # 3. Move all contents except global_elements into main_tag
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

    with open('financial-inclusion-test-2.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    print("financial-inclusion-test-2.html created successfully.")

if __name__ == '__main__':
    run()
