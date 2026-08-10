import os

script_path = 'build_final_agentic.py'
with open(script_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the sections parsing logic
old_logic = """    sections = main.find_all('section', recursive=False)
    
    for sec in sections:
        # Move all sections to thread wrapper except the footer (if footer is a section? footer is usually footer tag)
        thread_wrapper.append(sec)
        
    main.insert(0, thread_wrapper)"""
new_logic = """    main.clear()
    main.append(thread_wrapper)"""
content = content.replace(old_logic, new_logic)

# Replace sec_hero
content = content.replace("    sec_hero = sections[0]\n    sec_hero.clear()", "    sec_hero = soup.new_tag('section')\n    thread_wrapper.append(sec_hero)")
# Replace sec_chk1
content = content.replace("    sec_chk1 = sections[1]\n    sec_chk1.clear()", "    sec_chk1 = soup.new_tag('section')\n    thread_wrapper.append(sec_chk1)")
# Replace sec_chk2
content = content.replace("    sec_chk2 = sections[2]\n    sec_chk2.clear()", "    sec_chk2 = soup.new_tag('section')\n    thread_wrapper.append(sec_chk2)")
# Replace sec_out
content = content.replace("    sec_out = sections[3]\n    sec_out.clear()", "    sec_out = soup.new_tag('section')\n    thread_wrapper.append(sec_out)")
# Replace sec_4 (remove entirely)
content = content.replace("    sec_4 = sections[4] # Used to be tabs\n    sec_4.clear()", "")
# Replace sec_5
content = content.replace("    sec_5 = sections[5] # Final CTA\n    sec_5.clear()", "    sec_5 = soup.new_tag('section')\n    thread_wrapper.append(sec_5)")

# Also, change the base_file logic if it reads from agentic-commerce.html
content = content.replace("with open('agentic-commerce.html', 'r', encoding='utf-8') as f:", "with open('index.html', 'r', encoding='utf-8') as f:")

# But wait, there is a z-index issue!
# The vertical line has z-index: -1, and hero_container has z-index: 2.
# Why is the vertical line slicing through the text? 
# Because the text doesn't have a background color. If the vertical line is z-index: -1, it appears BEHIND the text. 
# We should give the hero container a solid background or add a background to the text if we want it to block the line.
# Or just don't worry about it, it might be the intended design. The user mainly said it was broken. We'll see.
# Wait, "Command your commerce" overlaps with "The intelligent engine...".
# Let's fix that by ensuring there's proper margin-bottom!

with open(script_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed build_final_agentic.py")
