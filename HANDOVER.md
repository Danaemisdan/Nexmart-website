# Technical Handover Document

## Overall Architecture
The Nexmart marketing website is a static, multi-page HTML site. It was originally exported from Webflow but is now maintained independently as a traditional static codebase. There is no dynamic backend, CMS, or build tool (like Webpack or Vite) natively required to serve the site.

## Static HTML / Webflow Architecture
The project relies on a single, monolithic CSS file (`nexmart-3-0.shared...min.css`) and a global JS bundle. 
**Crucial Rule:** The CSS file is immutable. You must style new components strictly by reusing existing Webflow utility classes found throughout the HTML. Do not append custom `<style>` blocks or create new CSS files.

## Reusable Templates
Rather than building pages from scratch, the architecture relies on cloning master structures:
1.  **Product Template (`product-template.html`):** Contains the approved, compliant structure for all product marketing pages. It includes the Global Nav, Hero Section, Feature Grid, and final CTA Banner. All 11 live product pages were programmatically generated from this exact structure.
2.  **Legal Page Template:** All 6 legal/policy pages share an identical structural wrapper (a simple rich-text container) to ensure visual consistency.

## Navigation & Header/Footer Strategy
*   **Duplication Strategy:** Because there is no templating engine (like PHP, Next.js, or Hugo), the header (`navbar-component`) and footer (`is-footer`) are explicitly duplicated across all 22 HTML files.
*   **Maintenance:** If a link is added to the footer, you must run a script or mass-find/replace to update all 22 files simultaneously. 
*   **Mobile Nav:** The hamburger menu relies on the `w-nav-button` and `w-nav-menu` classes intersecting with the Webflow JavaScript runtime.

## SEO & Accessibility Implementation
*   **Accessibility:** Duplicate Webflow-generated IDs (e.g., `w-node-_01f39a58...`) were systematically replaced with unique numerical suffixes to pass strict HTML validation. Image `alt` tags have been applied globally.
*   **SEO:** Canonical tags, Open Graph (social sharing), and Twitter metadata were injected into the `<head>` of every file. Meta descriptions for legal pages were uniquely generated to prevent duplication penalties.

## Product Page Generation Workflow
If new products are added to the Nexmart ecosystem, follow this workflow:
1.  Draft a "Product Brief" confirming capabilities and claims.
2.  Duplicate `product-template.html`.
3.  Inject the brief's copy into the template's designated text nodes.
4.  Update the `<title>`, meta description, and canonical tags.
5.  *Never invent CSS.*

## Pending Stakeholder Decisions (Important)
Before launch, the following items require manual intervention:
1.  **Hero Images:** The product pages currently use placeholder hero graphics. There is an HTML comment (`<!-- TODO: Replace with product-specific hero image -->`) preceding the `<img>` tag on every product page.
2.  **External Links:** There are 5 missing URLs marked with `#TODO` in the `href` attributes (App Store, Chrome Store, Portfolio Showcase, NexPay Portal, Themes Gallery).
3.  **Global Navigation Sync:** The links inside the header dropdown menus must be updated to point to the newly generated `[product-name].html` files.
