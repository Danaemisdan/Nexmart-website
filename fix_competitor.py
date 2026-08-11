import os

script_path = r'C:\Users\91844\.gemini\antigravity\brain\d2373c8e-c45c-4ee9-8d35-7df4e8dd5095\scratch\build_competitor_v3.py'
with open(script_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the overlap with the navbar by adjusting height and margin
old_canvas = """        .comp-canvas {
            position: relative;
            width: 100vw;
            height: 100vh;"""
new_canvas = """        .comp-canvas {
            position: relative;
            width: 100vw;
            height: calc(100vh - 80px);
            margin-top: 80px;"""
content = content.replace(old_canvas, new_canvas)

# Scale down the workspace so it fits in a single screen
old_workspace = """        .comp-workspace {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);"""
new_workspace = """        .comp-workspace {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%) scale(0.75);"""
content = content.replace(old_workspace, new_workspace)

with open(script_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed layout for competitor search.")
