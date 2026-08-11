import glob

def run():
    with open('index.html', 'r', encoding='utf-8') as f:
        idx_content = f.read()

    # Extract footer
    start = idx_content.find('<footer')
    end = idx_content.find('</footer>', start) + len('</footer>')
    if start == -1 or end == -1:
        print("Could not find footer in index.html")
        return
    
    footer_html = idx_content[start:end]
    
    files_to_check = [
        'competitor-research.html',
        'discovery-agent.html',
        'financial-inclusion.html',
        'healthcare-access.html',
        'logistics-node.html',
        'negotiation-agent.html',
        'portfolio.html',
        'price-agent.html',
        'quality-agent.html',
        'research-agent.html',
        'tracking-agent.html',
        'creator-library.html',
        'advertiser-library.html'
    ]
    
    for file in files_to_check:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if '<footer' not in content:
                # Insert right before </main>
                target = '</main>'
                pos = content.rfind(target)
                if pos != -1:
                    new_content = content[:pos] + footer_html + content[pos:]
                    with open(file, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Restored footer to {file}")
                else:
                    print(f"Could not find </main> in {file}")
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"Error processing {file}: {e}")

if __name__ == "__main__":
    run()
