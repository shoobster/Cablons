# Cablons Cyber website

Static site for www.cablons.com. Plain HTML and CSS, no build step, intended for GitHub Pages.

## Files

- `index.html`, `vciso.html` (fractional CISO), `penetration-testing.html`, `grc-consultancy.html`, `msp-partners.html`, `insights.html`, `assessing-the-business-ending-event.html`, `about.html`, `contact.html`, `privacy.html`, `404.html`
- `styles.css` (all styling, one file)
- `assets/logo.svg` (gold logo, used in header and footer), plus `logo-white.svg` and `logo-black.svg` for other uses
- `assets/favicon.png`, `apple-touch-icon.png`, `android-chrome.png` from the logo pack
- `assets/news.json` (security headlines from The Hacker News, refreshed by `.github/workflows/news.yml` every three hours using `tools/fetch_news.py`; shown in the ticker on the home page)
- `sitemap.xml`, `robots.txt`, `CNAME`, `.nojekyll`

## Before you publish

1. Social preview image. Add `assets/og-image.png` (1200 x 630) or remove the `og:image` meta tag from each page.
2. Contact form. The form posts to Formspree. Create a free form at formspree.io, then replace `REPLACE_WITH_FORM_ID` in `contact.html` with the real ID. Formspree's free tier is enough for enquiry volumes. Alternatives that also work on static hosting: Basin, Web3Forms, or a Netlify Forms setup if you host there instead.
3. Check the commitments in the copy. The following statements are written as service promises and should be confirmed or edited before go-live:
   - free retest of remediated findings within 60 days (`index.html`, `penetration-testing.html`)
   - fixed quote within two working days (`index.html`, `penetration-testing.html`)
   - reply to enquiries within one working day (`contact.html`)
   - professional indemnity and cyber insurance in place (`index.html`, `about.html`)
   - Cyber Essentials Plus delivered through a certification body partner (`penetration-testing.html`)
   - office hours and out-of-hours incident support for retained clients (`contact.html`)
   - vCISO day allocations and 30-day rolling terms (`vciso.html`)
   - timelines quoted on `grc-consultancy.html`
4. Article. `assessing-the-business-ending-event.html` is a draft for review. The byline reads "Cablons Cyber. November 2026"; change the date or add an author name in `tools/build.py` before publishing. New articles are added as further entries in the `pages` dictionary and a row in the `insights.html` ledger.
5. MSP terms. `msp-partners.html` says referral and resale terms are agreed up front and that Cablons does not sell managed services. Confirm both are commitments you want in writing on the site.
6. Accreditations. The site deliberately claims only CISSP and ISO 27001 Lead Auditor. If the company holds CREST membership, Cyber Essentials, IASME or ISO 9001 certification, add the badges to the "Why Cablons" section on the home page and the aside on the about page. Do not add badges for accreditations the company does not hold; competitors are frequently checked against the CREST and NCSC registers.

## Deploying to GitHub Pages

1. Create a repository (for example `cablons-site`) and push these files to the `main` branch at the repository root.
2. In the repository, go to Settings, then Pages. Under Build and deployment choose "Deploy from a branch", branch `main`, folder `/ (root)`.
3. Custom domain. The `CNAME` file sets www.cablons.com as the custom domain on every deployment. GitHub serves the site there and redirects the github.io address to it. Tick "Enforce HTTPS" in Settings, Pages once the certificate is issued (usually within an hour of the DNS check passing).
4. DNS at your registrar:
   - `www` CNAME record pointing to `<your-github-username>.github.io`
   - Apex `cablons.com` A records pointing to 185.199.108.153, 185.199.109.153, 185.199.110.153 and 185.199.111.153, so the bare domain redirects to www.
   Check the current IPs in GitHub's Pages documentation before setting them.
5. Keep the Duda site live until DNS has propagated and the HTTPS certificate is active, then cancel it.

## Editing

Each page is self-contained. The header and footer are repeated in every file, so a navigation change needs applying to all eight pages (a find and replace across the folder does it). Colours, fonts and spacing are variables at the top of `styles.css`.

The pages are generated from `tools/build.py`, which holds the header, footer and all page content as Python strings, and `tools/circuit.py`, which draws the gold circuit art. To change the navigation, footer or any copy, edit `tools/build.py` and run `python3 tools/build.py` from the repository root; it rewrites every HTML file plus the sitemap. Editing the HTML files directly also works if you prefer, but the next build will overwrite them. The `tools` folder is harmless on GitHub Pages and can be left in the repository.
