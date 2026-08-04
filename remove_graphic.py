import bs4
import glob

def remove_footer_graphic():
    # The smiling cube graphic is an image at the top of the footer
    files = ['magic-ai-search.html', 'agentic-commerce.html', 'advertiser-tracker.html']
    
    for filename in files:
        with open(filename, 'r', encoding='utf-8') as f:
            html = f.read()
            
        soup = bs4.BeautifulSoup(html, 'html.parser')
        
        # Remove the smiling cube graphic
        wrappers = soup.find_all(class_='footer_graphic-wrap')
        for wrap in wrappers:
            wrap.decompose()
            
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"Removed smiling cube graphic from {filename}")

if __name__ == "__main__":
    remove_footer_graphic()
