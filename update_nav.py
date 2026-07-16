import os
import glob
import shutil
import json
from bs4 import BeautifulSoup

def main():
    backup_dir = "navigation_backup"
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    html_files = glob.glob("*.html")
    if "index_original.html" in html_files:
        html_files.remove("index_original.html")

    # 1. Create backups (only if not already created to prevent overwriting with broken ones, though they aren't broken)
    for f in html_files:
        backup_path = os.path.join(backup_dir, f)
        if not os.path.exists(backup_path):
            shutil.copy(f, backup_path)
        
    mapping = {
        "Healthcare Access": "healthcare-access.html",
        "Agentic Commerce": "agentic-commerce.html",
        "Logistics Node": "logistics-node.html",
        "Magic AI Search": "magic-ai-search.html",
        "Advertiser Tracker": "advertiser-tracker.html",
        "Advertiser Library": "advertiser-library.html",
        "Portfolio": "portfolio.html",
        "Creator Library": "creator-library.html",
        "Financial Inclusion": "financial-inclusion.html",
        "Competitor Research": "competitor-research.html",
        "Chrome Extension": "chrome-extension.html",
        "Pre-built Stores": "pre-built-stores.html",
        "Theme Detector": "theme-detector.html"
    }

    report = {
        "files_modified": [],
        "links_changed": set(),
        "unchanged": set(),
        "broken_eliminated": set()
    }

    for file in html_files:
        with open(file, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")

        modified = False

        # Find all anchor tags
        links = soup.find_all("a")
        
        for link in links:
            # Look for the specific span that contains the tool name
            span = link.find("span", class_="mega-nav__panel-link-text")
            if span and span.string:
                link_text = span.string.strip()
                if link_text in mapping:
                    target_file = mapping[link_text]
                    # Check if target file exists
                    if os.path.exists(target_file):
                        old_href = link.get("href")
                        if old_href != target_file:
                            link["href"] = target_file
                            modified = True
                            report["links_changed"].add(f"{link_text}: {old_href} -> {target_file}")
                            if old_href and old_href != "#" and not old_href.startswith("http"):
                                report["broken_eliminated"].add(old_href)
                            elif old_href and "app.nexmartshop.ai" in old_href:
                                report["broken_eliminated"].add(old_href)
                    else:
                        report["unchanged"].add(f"{link_text} (Target {target_file} does not exist)")

        if modified:
            with open(file, "w", encoding="utf-8") as f:
                f.write(str(soup))
            report["files_modified"].append(file)

    # Output report data to parse later
    with open("nav_report_data.json", "w", encoding="utf-8") as f:
        # convert sets to lists
        report["links_changed"] = sorted(list(report["links_changed"]))
        report["unchanged"] = sorted(list(report["unchanged"]))
        report["broken_eliminated"] = sorted(list(report["broken_eliminated"]))
        json.dump(report, f, indent=4)

if __name__ == "__main__":
    main()
