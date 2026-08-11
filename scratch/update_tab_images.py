from bs4 import BeautifulSoup
import os

def update_tab_images():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
        
    soup = BeautifulSoup(content, 'html.parser')
    
    updated_count = 0
    
    for pane in soup.find_all('div', class_='home-tab_pane'):
        h3 = pane.find('h3')
        if not h3: continue
        
        title = h3.text.strip()
        link = pane.find('a', class_='button-wrap')
        if not link: continue
        
        href = link.get('href')
        
        # Check if the href points to a local file
        if href and href.endswith('.html') and not href.startswith('http'):
            target_file = href
            if os.path.exists(target_file):
                with open(target_file, 'r', encoding='utf-8') as tf:
                    target_soup = BeautifulSoup(tf.read(), 'html.parser')
                    
                # The hero image is typically the first large image or one with specific classes
                # Let's find an image that looks like a dashboard or main graphic
                # On research-agent.html, what is the image class? Let's try finding the main hero image
                # Often it is in a "hero" div, or it's just the first major image in <main>
                # We can look for .ra-image, .da-image, etc. Or just get all images and find the best fit.
                
                # Let's print out the images in the target file to see what we have
                imgs = target_soup.find_all('img')
                # Exclude icons, avatars, small svg
                large_imgs = [i for i in imgs if i.get('src') and not i.get('src').endswith('.svg') and 'icon' not in (i.get('class') or []) and 'logo' not in (i.get('class') or [])]
                
                if large_imgs:
                    # Usually the first non-svg image is the hero
                    hero_img = large_imgs[0]
                    src = hero_img.get('src')
                    
                    # Update the tab image
                    tab_img = pane.find('img', class_='home-tab_image')
                    if tab_img and tab_img.get('src') != src:
                        tab_img['src'] = src
                        print(f"Updated '{title}' tab with image from {target_file}: {src}")
                        updated_count += 1
                else:
                    print(f"No suitable image found in {target_file} for '{title}'")
                    
    if updated_count > 0:
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"Successfully updated {updated_count} tab images.")
    else:
        print("No images were updated.")

if __name__ == "__main__":
    update_tab_images()
