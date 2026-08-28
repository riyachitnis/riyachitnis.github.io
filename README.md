# Clearer Days - ADHD Coaching with Riya Chitnis

Three-page, light-only website and digital brand system for Clearer Days.

## Site map

- `index.html` - concise homepage and 60-second breathing reset
- `coaching.html` - coaching approach, support options and FAQ
- `about.html` - Riya's background, values and coaching scope

## Brand kit

- `assets/brand/logos/` - editable SVG and transparent PNG logo variants
- `assets/brand/social/` - LinkedIn and Instagram templates in SVG and PNG
- `assets/brand/generated/` - supporting open-horizon artwork
- `output/pdf/clearer-days-brand-guide.pdf` - complete usage guide

Run `tools/build_brand_assets.py` to rebuild brand exports. The script uses CairoSVG when available and always rebuilds the editable SVG sources.


## 🚀 Deployment & Local Preview

This project is built with vanilla **HTML5, CSS3, and modern JavaScript**, with zero dependencies or build steps required.

### Local Preview:
Open `index.html` directly in any web browser, or serve it locally:

```bash
# Using Python
python3 -m http.server 8000
```
Then visit `http://localhost:8000`.

### GitHub Pages:
Since this repository is configured for GitHub Pages (`riyachitnis.github.io`), simply commit and push changes to the `main` branch. GitHub Pages will host the site live automatically.
