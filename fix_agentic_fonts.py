import os

script_path = 'build_final_agentic.py'
with open(script_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add font import and styles to the CSS
css_injection = """
    /* =======================================================
       AGENTIC COMMERCE (PRODUCT CENTRIC ARCHITECTURE)
       ======================================================= */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    .agentic-page-wrapper {
        font-family: 'Inter', sans-serif !important;
    }
"""
content = content.replace("/* =======================================================\n       AGENTIC COMMERCE (PRODUCT CENTRIC ARCHITECTURE)\n       ======================================================= */", css_injection)

# 2. Add class and padding to thread_wrapper
wrapper_style = """thread_wrapper['style'] = "position: relative; overflow: hidden; padding-top: 160px; padding-bottom: 80px;"
    thread_wrapper['class'] = "agentic-page-wrapper"
"""
content = content.replace("thread_wrapper['style'] = \"position: relative; overflow: hidden; padding-top: 60px; padding-bottom: 60px;\"", wrapper_style)

with open(script_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied fonts and padding to build_final_agentic.py")
