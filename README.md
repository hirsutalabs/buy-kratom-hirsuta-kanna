# HirsutaLab – Multilingual SEO Website

A multilingual, SEO-optimized static website for [hirsutalab.com](https://hirsutalab.com/) — linking to the shop products across 8 languages.

## Languages
🇬🇧 English · 🇩🇪 Deutsch · 🇫🇷 Français · 🇨🇿 Čeština · 🇸🇮 Slovenščina · 🇸🇰 Slovenčina · 🇵🇱 Polski · 🇷🇺 Русский

## Products Covered
- Mitragyna Hirsuta (Kra Thum Khok) Leaf Powder
- Green Borneo Kratom Powder
- Red Maeng Da Kratom Nano Powder
- Kanna Extract Powder (Strong)
- Kanna Premium Extract – Ultra Strong
- Kanna Crystal Ultimate Extract
- Kanna Full Spectrum Extract
- Kanna Happy Calming Extract

## Deploy to GitHub Pages

### Step 1 – Create a repository
1. Go to [github.com](https://github.com) and create a new **public** repository named e.g. `hirsutalab`

### Step 2 – Upload files
```bash
git init
git add .
git commit -m "Initial commit – HirsutaLab multilingual site"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/hirsutalab.git
git push -u origin main
```

### Step 3 – Enable GitHub Pages
1. Open your repository → **Settings** → **Pages**
2. Under *Source* select **Deploy from a branch**
3. Select branch **main**, folder **/ (root)**
4. Click **Save**

Your site will be live at:  
`https://YOUR_USERNAME.github.io/hirsutalab/`

### Step 4 – Update sitemap & robots.txt
Replace `YOUR_GITHUB_USERNAME` in `sitemap.xml` and `robots.txt` with your actual username.

## File Structure
```
/
├── index.html          ← English
├── style.css           ← Global styles
├── main.js             ← JS interactions
├── sitemap.xml         ← SEO sitemap
├── robots.txt
├── _config.yml         ← GitHub Pages config
├── de/index.html       ← German
├── fr/index.html       ← French
├── cs/index.html       ← Czech
├── sl/index.html       ← Slovenian
├── sk/index.html       ← Slovak
├── pl/index.html       ← Polish
└── ru/index.html       ← Russian
```

## SEO Features
- Unique `<title>`, `<meta description>`, `<meta keywords>` per language
- `hreflang` alternate tags linking all language versions
- Schema.org structured data (Store + Product markup)
- sitemap.xml with hreflang annotations
- robots.txt with sitemap reference
- Semantic HTML5 with `itemscope`/`itemprop`
- Lazy-loaded product images with descriptive `alt` text
- Canonical URLs pointing to hirsutalab.com
