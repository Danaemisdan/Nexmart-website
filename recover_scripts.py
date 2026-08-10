import json
import os
import urllib.parse

log_path = r"C:\Users\91844\.gemini\antigravity\brain\d2373c8e-c45c-4ee9-8d35-7df4e8dd5095\.system_generated\logs\transcript_full.jsonl"
out_dir = r"C:\Users\91844\.gemini\antigravity\brain\d2373c8e-c45c-4ee9-8d35-7df4e8dd5095\scratch"

target_scripts = [
    "build_logistics_v2.py",
    "build_logistics.py",
    "build_advertiser.py",
    "build_portfolio.py",
    "build_creator.py",
    "build_financial.py",
    "build_competitor_v3.py",
    "build_competitor.py",
    "build_healthcare.py"
]

recovered = {}

with open(log_path, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            entry = json.loads(line)
        except:
            continue
            
        if "tool_calls" in entry:
            for tc in entry["tool_calls"]:
                if tc.get("name") in ("write_to_file", "default_api:write_to_file"):
                    args = tc.get("args", {})
                    target_file = args.get("TargetFile", "")
                    basename = os.path.basename(urllib.parse.unquote(target_file))
                    
                    if basename in target_scripts:
                        # Overwrite with the latest version found in the transcript
                        recovered[basename] = args.get("CodeContent", "")

for name, content in recovered.items():
    if not content:
        continue
    out_path = os.path.join(out_dir, name)
    with open(out_path, 'w', encoding='utf-8') as f:
        # Before writing, let's also fix the seamless-page-wrapper issue automatically
        content = content.replace("seamless-page-wrapper", "page-wrapper")
        f.write(content)
    print(f"Recovered {name} (size: {len(content)} bytes)")
