# Deployment Guide

Follow this guide to safely push the Nexmart static website to production.

## 1. Pre-deployment Checklist
Before deploying, ensure the following steps are completed:
- [ ] **Delete Backups:** Ensure `index_original.html` and any testing Python scripts (`create_404.py`, `seo_implement.py`, etc.) are removed from the deployment directory.
- [ ] **Replace Hero Images:** Locate the `<!-- TODO: Replace with product-specific hero image -->` comments in the product pages and swap the `src` with actual product screenshots.
- [ ] **Update Global Navigation:** Update the dropdown links in the header across all 21 files to point away from `#` and toward the actual `[product].html` files.

## 2. Required Stakeholder Confirmations
- [ ] Obtain the 5 missing external URLs replacing the current `#TODO` hrefs:
  - App Store / Play Store link
  - NexPay Portal URL
  - Chrome Web Store link
  - Themes Gallery URL
  - Portfolio Showcase URL
- [ ] Finalize the content and capability claims for `healthcare-access.html` and `logistics-node.html` (currently deferred).

## 3. Deployment Steps
Because this is a static site, it can be deployed to any standard CDN/Hosting provider (AWS S3 + Cloudfront, Vercel, Netlify, Cloudflare Pages).
1. Define the build folder as the root directory (`/`).
2. There is no build command (e.g., no `npm run build` is required).
3. Ensure the hosting provider is configured to serve `404.html` as the default error document.

## 4. Post-deployment Verification
Once the site is live at `https://www.nexmartshop.ai`:

### SEO & Technical Verification
- [ ] **robots.txt:** Navigate to `https://www.nexmartshop.ai/robots.txt` and ensure it allows crawling.
- [ ] **sitemap.xml:** Navigate to `https://www.nexmartshop.ai/sitemap.xml` and ensure all URLs load correctly without 404s.
- [ ] **Canonical Tags:** Inspect the `<head>` of a few live pages to ensure canonical tags point to `https://www.nexmartshop.ai/...`.

### Cache Invalidation
If deploying over a previous version, force a cache invalidation on your CDN (e.g., Cloudfront Invalidation for `/*`) to ensure the updated CSS, HTML, and images propagate immediately to users.

### Browser Testing Checklist
- [ ] Verify the hamburger menu opens and closes correctly on mobile devices (iOS Safari, Android Chrome).
- [ ] Test the 404 page by visiting a random, non-existent URL (e.g., `/does-not-exist`).
- [ ] Verify that clicking the header/footer logos safely routes back to `/`.
