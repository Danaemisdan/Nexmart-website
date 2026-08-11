import os
import re

scratch_scripts = [
    r"C:\Users\91844\.gemini\antigravity\brain\d2373c8e-c45c-4ee9-8d35-7df4e8dd5095\scratch\build_healthcare.py",
    r"C:\Users\91844\.gemini\antigravity\brain\d2373c8e-c45c-4ee9-8d35-7df4e8dd5095\scratch\build_logistics_v2.py",
    r"C:\Users\91844\.gemini\antigravity\brain\d2373c8e-c45c-4ee9-8d35-7df4e8dd5095\scratch\build_advertiser.py",
    r"C:\Users\91844\.gemini\antigravity\brain\d2373c8e-c45c-4ee9-8d35-7df4e8dd5095\scratch\build_portfolio.py",
    r"C:\Users\91844\.gemini\antigravity\brain\d2373c8e-c45c-4ee9-8d35-7df4e8dd5095\scratch\build_creator.py",
    r"C:\Users\91844\.gemini\antigravity\brain\d2373c8e-c45c-4ee9-8d35-7df4e8dd5095\scratch\build_financial.py",
    r"C:\Users\91844\.gemini\antigravity\brain\d2373c8e-c45c-4ee9-8d35-7df4e8dd5095\scratch\build_competitor_v3.py",
]

for script in scratch_scripts:
    with open(script, 'r', encoding='utf-8') as f:
        content = f.read()

    # Use index.html as base file
    content = re.sub(r"base_file\s*=\s*os\.path\.join\([^,]+,\s*'[^']+'\)", "base_file = os.path.join(target_dir, 'index.html')", content)
    
    # We want to replace this block:
    #     page_wrapper = main_wrapper.find('div', class_='page-wrapper')
    #     if page_wrapper:
    #         page_wrapper.clear()
    # WITH:
    #     if True:
    #         main_wrapper.clear()
    #         page_wrapper = main_wrapper
    # This keeps all the indentation below it perfectly intact, since `if True:` keeps the block level the same!
    
    replace_block = """    page_wrapper = main_wrapper.find('div', class_='page-wrapper')
    if page_wrapper:
        page_wrapper.clear()"""
    
    new_block = """    if True:
        main_wrapper.clear()
        page_wrapper = main_wrapper"""
    
    content = content.replace(replace_block, new_block)
    
    with open(script, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Fixed {script}")
