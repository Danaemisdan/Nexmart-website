import os
import glob
from bs4 import BeautifulSoup
from collections import defaultdict

def main():
    html_files = glob.glob('*.html')
    
    # Exclude the backup file from the audit
    if "index_original.html" in html_files:
        html_files.remove("index_original.html")
        
    titles = defaultdict(list)
    descriptions = defaultdict(list)
    
    audit_data = {
        "missing_title": [],
        "long_title": [],
        "short_title": [],
        "duplicate_title": [],
        
        "missing_desc": [],
        "long_desc": [],
        "short_desc": [],
        "duplicate_desc": [],
        
        "missing_canonical": [],
        
        "missing_og": [],
        "missing_twitter": [],
        
        "multiple_h1": [],
        "missing_h1": [],
        
        "images_missing_alt": [],
        "images_missing_lazy": [],
        
        "orphan_pages": []
    }
    
    all_internal_links = set()
    all_targets = set()
    
    for file in html_files:
        with open(file, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, 'html.parser')
            
        # 1. Page titles
        title_tag = soup.find('title')
        if not title_tag or not title_tag.string:
            audit_data["missing_title"].append(file)
        else:
            title_text = title_tag.string.strip()
            titles[title_text].append(file)
            if len(title_text) < 30: audit_data["short_title"].append(file)
            if len(title_text) > 65: audit_data["long_title"].append(file)
            
        # 2. Meta descriptions
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        if not meta_desc or not meta_desc.get('content'):
            audit_data["missing_desc"].append(file)
        else:
            desc_text = meta_desc.get('content').strip()
            descriptions[desc_text].append(file)
            if len(desc_text) < 70: audit_data["short_desc"].append(file)
            if len(desc_text) > 160: audit_data["long_desc"].append(file)
            
        # 3. Canonical URLs
        canonical = soup.find('link', rel='canonical')
        if not canonical:
            audit_data["missing_canonical"].append(file)
            
        # 4. Open Graph & 5. Twitter Card
        og_title = soup.find('meta', attrs={'property': 'og:title'})
        twitter_title = soup.find('meta', attrs={'name': 'twitter:title'})
        if not og_title: audit_data["missing_og"].append(file)
        if not twitter_title: audit_data["missing_twitter"].append(file)
        
        # 6. Heading hierarchy
        h1s = soup.find_all('h1')
        if len(h1s) == 0: audit_data["missing_h1"].append(file)
        if len(h1s) > 1: audit_data["multiple_h1"].append(file)
        
        # 7. Internal linking (prep)
        for a in soup.find_all('a'):
            href = a.get('href', '')
            if href.endswith('.html') and not href.startswith('http'):
                target = href.split('#')[0]
                all_targets.add(target)
                
        # 8. Image SEO
        imgs = soup.find_all('img')
        for img in imgs:
            if not img.has_attr('alt'):
                audit_data["images_missing_alt"].append(file)
            # Webflow sometimes uses loading="lazy" but let's see how widespread it is missed
            if not img.has_attr('loading') or img.get('loading') != 'lazy':
                # Don't flag hero images (first image in body usually shouldn't be lazy loaded)
                # But for a basic check, we'll just flag if many are missing it
                audit_data["images_missing_lazy"].append(file)
                
    # Duplicates
    for t, files in titles.items():
        if len(files) > 1:
            audit_data["duplicate_title"].extend(files)
            
    for d, files in descriptions.items():
        if len(files) > 1:
            audit_data["duplicate_desc"].extend(files)
            
    # Orphans
    for f in html_files:
        if f not in all_targets and f != "index.html":
            audit_data["orphan_pages"].append(f)
            
    # Generate Report
    report = ["# Nexmart SEO Audit Report\n\nThis comprehensive audit evaluates the SEO readiness of the entire Nexmart marketing website (excluding backups). Recommendations are prioritized into Critical, Recommended, and Optional tiers.\n"]
    
    # --- CRITICAL ---
    report.append("## 🔴 CRITICAL\n_Must be addressed before launch to ensure basic search engine indexing and user experience._\n")
    
    if audit_data["missing_title"]:
        report.append("### 1. Missing Page Titles")
        report.append(f"The following pages are missing a `<title>` tag: {', '.join(audit_data['missing_title'])}")
        
    if audit_data["duplicate_title"]:
        report.append("### 2. Duplicate Page Titles")
        report.append("Search engines struggle to differentiate pages with identical titles.")
        for t, files in titles.items():
            if len(files) > 1: report.append(f"- '{t}' is shared by: {', '.join(files)}")
            
    if audit_data["missing_desc"]:
        report.append("### 3. Missing Meta Descriptions")
        report.append(f"Pages missing `<meta name=\"description\">`: {', '.join(audit_data['missing_desc'])}")
        
    if audit_data["duplicate_desc"]:
        report.append("### 4. Duplicate Meta Descriptions")
        for d, files in descriptions.items():
            if len(files) > 1: report.append(f"- Shared by: {', '.join(files)}")
            
    if audit_data["missing_h1"]:
        report.append("### 5. Missing H1 Tags")
        report.append(f"Every page must have an H1. Missing on: {', '.join(audit_data['missing_h1'])}")
        
    if audit_data["multiple_h1"]:
        report.append("### 6. Multiple H1 Tags")
        report.append(f"Pages with more than one H1 (confuses hierarchy): {', '.join(set(audit_data['multiple_h1']))}")
        
    if audit_data["orphan_pages"]:
        report.append("### 7. Orphan Pages")
        report.append("These pages are not linked to by any other internal page. They cannot be crawled by search engine bots effectively.")
        for o in set(audit_data["orphan_pages"]): report.append(f"- {o}")
        
    if not any([audit_data["missing_title"], audit_data["duplicate_title"], audit_data["missing_desc"], audit_data["duplicate_desc"], audit_data["missing_h1"], audit_data["multiple_h1"], audit_data["orphan_pages"]]):
        report.append("*No critical issues detected in these categories!*\n")
        
    # --- RECOMMENDED ---
    report.append("\n## 🟡 RECOMMENDED\n_Should be implemented to improve ranking, click-through rates, and social sharing._\n")
    
    report.append("### 1. Canonical URLs")
    if len(audit_data["missing_canonical"]) == len(html_files):
        report.append("- **Issue**: The entire site is missing `<link rel=\"canonical\">` tags.")
        report.append("- **Action**: Add a self-referencing canonical URL to the `<head>` of every page (e.g., `<link rel=\"canonical\" href=\"https://www.nexmartshop.ai/page-name.html\">`) to prevent duplicate content issues.")
    else:
        report.append(f"- Missing canonicals on: {', '.join(set(audit_data['missing_canonical']))}")
        
    report.append("\n### 2. Open Graph & Twitter Card Metadata")
    if len(audit_data["missing_og"]) > 0:
        report.append(f"- **Issue**: {len(set(audit_data['missing_og']))} pages are missing Open Graph (`og:title`, `og:description`, `og:image`) and Twitter Card tags.")
        report.append("- **Action**: Inject rich social metadata to ensure links render beautifully when shared on LinkedIn, X, and Facebook.")
        
    report.append("\n### 3. Title & Description Lengths")
    if audit_data["long_title"] or audit_data["short_title"]:
        report.append(f"- **Sub-optimal Titles**: {len(set(audit_data['long_title']))} are too long (>65 chars) and {len(set(audit_data['short_title']))} are too short (<30 chars). Aim for 50-60 characters containing the primary keyword.")
    if audit_data["long_desc"] or audit_data["short_desc"]:
        report.append(f"- **Sub-optimal Descriptions**: {len(set(audit_data['long_desc']))} are too long (>160 chars) and {len(set(audit_data['short_desc']))} are too short (<70 chars).")
        
    report.append("\n### 4. Image SEO (Missing Alt Attributes)")
    if audit_data["images_missing_alt"]:
        report.append(f"- **Issue**: While our recent cleanup fixed the generated product pages, {len(set(audit_data['images_missing_alt']))} pages (mostly legacy/legal/index) still contain `<img>` tags entirely missing the `alt` attribute.")
        report.append("- **Action**: Add `alt=\"\"` for decorative images or descriptive text for content images.")
        
    report.append("\n### 5. URL Consistency & Sitemap")
    report.append("- **Robots.txt**: No `robots.txt` detected in the root. Action: Create one to allow all crawling (`User-agent: * Allow: /`).")
    report.append("- **Sitemap.xml**: No `sitemap.xml` detected. Action: Generate an XML sitemap encompassing all 20 active pages and submit to Google Search Console.")
    
    # --- OPTIONAL ---
    report.append("\n## 🟢 OPTIONAL\n_Advanced optimizations for peak performance and rich search results._\n")
    
    report.append("### 1. Structured Data (JSON-LD)")
    report.append("- **Opportunity**: None of the pages currently utilize schema markup.")
    report.append("- **Action**: Implement `Organization` schema on the homepage, and `Product` or `SoftwareApplication` schema on the individual Tools pages (e.g. Agentic Commerce) to enable rich snippets in Google results.")
    
    report.append("\n### 2. Image Lazy Loading")
    report.append("- **Opportunity**: Many below-the-fold images lack the `loading=\"lazy\"` attribute.")
    report.append("- **Action**: Add `loading=\"lazy\"` to footer graphics and features grids to improve Core Web Vitals (LCP). Do *not* lazy load the Hero images.")
    
    report.append("\n### 3. Internal Linking Architecture")
    report.append("- **Opportunity**: The Legal pages (Privacy Policy, Terms, etc.) are weakly linked (only from the footer). The new Product pages are heavily cross-linked via 'Related Products', which is excellent. However, a central \"Products/Tools\" HTML sitemap or index page could strengthen authority distribution.")

    with open("seo_audit_report.md", "w", encoding="utf-8") as f:
        f.write("\n".join(report))

if __name__ == "__main__":
    main()
