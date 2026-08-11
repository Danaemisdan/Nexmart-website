import os
from bs4 import BeautifulSoup

agents = ['discovery-agent.html', 'research-agent.html', 'price-agent.html', 'quality-agent.html', 'tracking-agent.html']

for agent in agents:
    with open(agent, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        
    imgs = soup.find_all('img')
    print(f"--- {agent} ---")
    for img in imgs:
        src = img.get('src')
        if src and not src.endswith('.svg') and 'logo' not in src.lower() and 'chatgpt' not in src.lower():
            print(src)
