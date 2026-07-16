# Nexmart Website

## Project Overview
Nexmart is a modern, static marketing website for an Agentic Commerce platform. The site serves as the primary marketing vehicle to explain Nexmart's capabilities, showcase its suite of AI-driven tools, provide standard legal disclosures, and drive user acquisition.

## Tech Stack
*   **HTML5:** Semantic, statically generated HTML
*   **CSS3:** Monolithic utility-based CSS exported originally from Webflow.
*   **JavaScript:** Webflow's native JS bundle for interactions (hamburger menus, basic animations).
*   **Python (Build/Scripting):** Used strictly for mass-generation, SEO injection, and structural QA automation.

## Folder Structure
The project follows a flat, simple structure:
*   `/` (Root): All HTML files (`index.html`, `404.html`, legal pages, product pages).
*   `/robots.txt`: Search engine crawling rules.
*   `/sitemap.xml`: XML sitemap for SEO indexing.
*   *(Note: Images and CSS files are referenced locally per the Webflow export structure).*

## Local Development Instructions
To run the project locally and test navigation:
1. Open a terminal in the project root directory.
2. Run a local web server (e.g., using Python): `python -m http.server 8080`
3. Navigate to `http://localhost:8080` in your browser.

## Project Architecture & Website Structure
The website consists of 22 primary HTML files:
*   **Homepage:** `index.html` (The primary landing page).
*   **Product Template:** `product-template.html` (The master structural template for all tool/product pages).
*   **Product Pages (11):** `agentic-commerce.html`, `magic-ai-search.html`, `advertiser-tracker.html`, `advertiser-library.html`, `portfolio.html`, `creator-library.html`, `financial-inclusion.html`, `competitor-research.html`, `chrome-extension.html`, `pre-built-stores.html`, `theme-detector.html`.
*   **Legal Pages (6):** `privacy-policy.html`, `terms-and-conditions.html`, `refund-policy.html`, `return-policy.html`, `cancellation-policy.html`, `checkout-policy.html`.
*   **Utility Pages:** `404.html`.

## Asset Organization
All images use a mix of specific `.png`/`.jpg` files and SVG icons. Decorative elements must utilize `alt=""` while content-bearing images require descriptive text.

## Important Implementation Notes
*   **Do not modify the CSS:** The `nexmart-3-0.shared...min.css` file is considered immutable. All styling changes should be made by combining existing utility classes.
*   **Hardcoded Navigation:** Global navigation and footers are currently hardcoded into every HTML file. Changes to the header/footer must be replicated across all 21 active files.

## SEO Implementation
*   **Metadata:** Every page features unique Title tags, Meta descriptions, Open Graph (OG) tags, and Twitter Card tags.
*   **Canonical URLs:** Every page points to its authoritative `https://www.nexmartshop.ai/` counterpart.
*   **Crawling:** A `robots.txt` and `sitemap.xml` are present in the root directory for optimal search engine indexing.

## Browser Compatibility
The site utilizes standard Webflow flexbox and CSS grid layouts, supporting all modern browsers (Chrome, Safari, Firefox, Edge). Mobile responsiveness is natively handled by the CSS bundle's media queries.

## Known Limitations
*   **Orphan Pages:** The global navigation dropdowns on the homepage have not yet been updated to link to the newly generated product pages.
*   **Missing Destinations:** Several placeholder links (`#TODO`) require stakeholder input before launch (e.g., App Store links).
*   **Deferred Pages:** `logistics-node.html` and `healthcare-access.html` were deferred pending stakeholder capability review.
