import re
import json
import base64
import os

html_path = r"C:\Users\Nidzam\ebook-auto-trading\ebook-flipbook.html"
images_dir = r"C:\Users\Nidzam\ebook-auto-trading\images"

print("Reading HTML file...")
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Helper to get base64 string of an image file
def get_base64_img(filename):
    path = os.path.join(images_dir, filename)
    if not os.path.exists(path):
        print(f"Warning: Image file not found: {path}")
        return None
    
    ext = os.path.splitext(filename)[1].lower().replace('.', '')
    if ext == 'jpg':
        ext = 'jpeg'
        
    with open(path, 'rb') as f:
        data = f.read()
    b64 = base64.b64encode(data).decode('utf-8')
    return f"data:image/{ext};base64,{b64}"

# Mapping from placeholder content to image filename
# Keywords are matched as substrings (case-insensitive) against placeholder descriptions
mappings = [
    ("cover", "00-cover.jpg"),
    ("robot arm", "01-journey-flowchart.png"),
    ("Three characters", "01-you-hermes-moomoo.png"),
    ("helmet", "02-safety-scale.png"),
    ("balance scale", "02-safety-scale.png"),
    ("desk with a computer", "03-windows-explorer.png"),
    ("Windows Explorer", "03-windows-explorer.png"),
    ("Download", "04-download-moomoo.png"),
    ("moomoo desktop", "04-download-moomoo.png"),
    ("OpenD toggle", "04-moomoo-opend-clean.png"),
    ("friendly robot", "05-hermes-interface.png"),
    ("Hermes Agent interface", "05-hermes-interface.png"),
    ("puzzle pieces", "06-config-form.png"),
    ("form-style", "06-config-form.png"),
    ("check moomoo balance", "06-connection-diagram.png"),
    ("restaurant analogy", "07-restaurant-analogy.png"),
    ("SIMULATE", "16-simulate-vs-live.png"),
    ("recipe book", "12-recipe-cards.png"),
    ("RSI Strategy", "08-rsi-gauge.png"),
    ("thermometer", "08-rsi-gauge.png"),
    ("moving average", "08-ema-crossover.png"),
    ("Bollinger", "08-bollinger-bands.png"),
    ("alarm clock", "09-cron-timeline.png"),
    ("30-minute", "09-cron-timeline.png"),
    ("whiteboard", "10-planning-worksheet.png"),
    ("worksheet", "10-planning-worksheet.png"),
    ("person sitting at a computer", "11-agent-progress.png"),
    ("progress bar", "11-agent-progress.png"),
    ("Three recipe cards", "12-recipe-cards.png"),
    ("sample trade log", "13-trade-log.png"),
    ("confused expression", "13-confused-chart.jpg"),
    ("Two hands exchanging", "13-money-exchange.png"),
    ("weekly planner", "13-weekly-planner.jpg"),
    ("Three robots standing", "14-multiple-agents.png"),
    ("large monitor screen", "15-dashboard-layout.png"),
    ("browser window showing the dashboard", "15-browser-dashboard.jpg"),
    ("diving board", "16-simulate-vs-live.png"),
    ("GO LIVE RULES", "16-go-live-rules.png"),
    ("staircase", "17-staircase-indicators.jpg"),
    ("traffic lights", "17-multi-indicator.png"),
    ("robot mechanic", "18-robot-mechanic.jpg"),
    ("5-step flowchart", "18-flowchart-troubleshoot.png"),
    ("doing stretches", "19-stretching-calendar.png"),
    ("monthly calendar", "19-maintenance-calendar.png"),
    ("vault door", "20-vault-security.png"),
    ("shield checklist", "20-security-checklist.png"),
    ("open dictionary page", "28-glossary-dictionary.png"),
]

# 1. Update Head to include Google Fonts
print("Injecting Google Fonts stylesheet link in head...")
google_fonts_link = '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Lora:ital,wght@0,400;0,500;0,600;1,400&family=Outfit:wght@400;500;600;700;800&display=swap" rel="stylesheet">\n'
# Insert right before </head>
if '</head>' in content:
    content = content.replace('</head>', f'{google_fonts_link}</head>')
else:
    print("Error: </head> not found in file.")

# 2. Replace CSS Block
print("Injecting premium stylesheet...")
new_style = """<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
html, body {
  height: 100%;
  overflow: hidden;
  background: radial-gradient(circle at center, #0f0f23 0%, #05050f 100%);
  font-family: 'Lora', Georgia, serif;
  color: #2c3e50;
  -webkit-font-smoothing: antialiased;
}
#book {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  perspective: 2200px;
}
.page {
  position: absolute;
  width: 94vw;
  max-width: 1050px;
  height: 90vh;
  border-radius: 4px 16px 16px 4px;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  transform-style: preserve-3d;
  backface-visibility: hidden;
  transition: transform .6s cubic-bezier(0.23, 1, 0.32, 1), opacity .6s ease;
  box-shadow: 0 25px 70px rgba(0,0,0,0.5), inset -2px 0 10px rgba(0,0,0,0.05);
}
.page.entering {
  transform: rotateY(75deg) translateZ(100px);
  opacity: 0;
}
.page.leaving {
  transform: rotateY(-75deg) translateZ(-100px);
  opacity: 0;
}
.page.current {
  transform: rotateY(0) translateZ(0);
  opacity: 1;
}
.page.cover {
  background: linear-gradient(135deg, #101428, #18224b 40%, #101530);
  border-left: 10px solid #080a18;
  border-radius: 4px 20px 20px 4px;
}
.page.toc {
  background: #fbfbf9;
}
.page.part {
  background: linear-gradient(135deg, #10344b, #194e70 50%, #0e2d42);
}
.page.chapter {
  background: #fcfcf9;
}
.page.appendix {
  background: #fafaf7;
}

/* Spine Crease / Highlight Effect */
.page::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  width: 45px;
  height: 100%;
  background: linear-gradient(to right, rgba(0, 0, 0, 0.12), rgba(0, 0, 0, 0.04) 20%, transparent 60%);
  pointer-events: none;
  z-index: 10;
}

.phdr {
  padding: 20px 65px;
  font-family: 'Outfit', sans-serif;
  font-size: 14px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 2px;
  border-bottom: 1px solid rgba(0,0,0,.06);
  flex-shrink: 0;
}
.phdr-cover {
  background: rgba(255,255,255,.03);
  color: rgba(255,255,255,.6);
  text-align: center;
  font-size: 12px;
}
.phdr-toc {
  background: #eef3f7;
  color: #194e70;
  border-bottom: 2px solid #3498db;
}
.phdr-part {
  background: rgba(0,0,0,.15);
  color: rgba(255,255,255,0.9);
  text-align: center;
  font-size: 15px;
  letter-spacing: 4px;
  border-bottom: none;
}
.phdr-chapter {
  background: #ffffff;
  color: #194e70;
  border-bottom: 2px solid #3498db;
}
.phdr-appendix {
  background: #fdf5ef;
  color: #d35400;
  border-bottom: 2px solid #e67e22;
}
.ch-num {
  display: inline-block;
  background: #3498db;
  color: white;
  padding: 3px 12px;
  border-radius: 20px;
  margin-right: 12px;
  font-size: 12px;
  font-weight: 700;
  vertical-align: middle;
}
.ch-title {
  vertical-align: middle;
  font-weight: 700;
}
.pbody {
  flex: 1;
  overflow-y: auto;
  padding: 50px 75px;
  font-size: 17px;
  line-height: 1.9;
  color: #34495e;
}
.pbody::-webkit-scrollbar {
  width: 6px;
}
.pbody::-webkit-scrollbar-track {
  background: rgba(0,0,0,0.02);
}
.pbody::-webkit-scrollbar-thumb {
  background: rgba(0,0,0,0.12);
  border-radius: 3px;
}
.pnum {
  text-align: center;
  padding: 15px 0;
  font-size: 12px;
  color: #95a5a6;
  font-family: 'Inter', sans-serif;
  border-top: 1px solid rgba(0,0,0,.04);
  margin: 0 65px;
}

/* Page Types */
.page.cover .pbody {
  color: #fff;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 40px;
}
.page.cover h1 {
  font-family: 'Outfit', sans-serif;
  font-size: 3.4em;
  font-weight: 800;
  line-height: 1.2;
  color: #ffffff;
  margin-bottom: 12px;
  letter-spacing: -1px;
  background: linear-gradient(135deg, #ffffff 30%, #3498db);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: 0 4px 20px rgba(0,0,0,0.15);
}
.page.cover h2 {
  font-family: 'Inter', sans-serif;
  font-size: 1.25em;
  font-weight: 400;
  color: #a0aed0;
  margin-bottom: 25px;
  max-width: 600px;
}
.page.cover hr {
  border: none;
  height: 2px;
  background: linear-gradient(to right, transparent, rgba(52, 152, 219, 0.4), transparent);
  margin: 20px 0;
  width: 60%;
}
.page.cover .pnum {
  color: rgba(255,255,255,.3);
  border-top: 1px solid rgba(255,255,255,.05);
}
.page.part .pbody {
  color: #fff;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
}
.page.part h1 {
  font-family: 'Outfit', sans-serif;
  font-size: 3em;
  color: #fff;
  letter-spacing: 4px;
  font-weight: 800;
  margin-bottom: 10px;
  background: linear-gradient(135deg, #ffffff 40%, #a2d2ff);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.page.part .pnum {
  color: rgba(255,255,255,.3);
  border-top: 1px solid rgba(255,255,255,.05);
}

/* Typography styles inside content */
h1 {
  font-family: 'Outfit', sans-serif;
  color: #194e70;
  font-size: 2.1em;
  font-weight: 700;
  margin-bottom: 24px;
  border-bottom: 2px solid #eef2f7;
  padding-bottom: 14px;
  letter-spacing: -0.5px;
}
h2 {
  font-family: 'Outfit', sans-serif;
  color: #2c3e50;
  margin: 32px 0 16px;
  font-size: 1.45em;
  font-weight: 600;
}
h3 {
  font-family: 'Outfit', sans-serif;
  color: #34495e;
  margin: 24px 0 12px;
  font-size: 1.2em;
  font-weight: 600;
}
p {
  margin-bottom: 18px;
  text-align: justify;
}
ul, ol {
  margin: 12px 0;
  padding-left: 30px;
}
li {
  margin: 6px 0;
}

/* Tables */
table {
  border-collapse: collapse;
  width: 100%;
  margin: 25px 0;
  font-family: 'Inter', sans-serif;
  font-size: 0.9em;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 4px 15px rgba(0,0,0,.03);
  border: 1px solid #eef2f5;
}
th, td {
  padding: 12px 16px;
  text-align: left;
}
th {
  background: #194e70;
  color: #ffffff;
  font-weight: 600;
  font-size: 0.95em;
}
td {
  color: #4f5f7f;
}
tr:nth-child(even) {
  background: #fcfdfe;
}
tr:hover {
  background: #f5f8fa;
}

/* Code & Pre */
pre {
  background: #101424;
  color: #e3e8f0;
  padding: 18px 24px;
  border-radius: 8px;
  overflow-x: auto;
  font-size: 0.88em;
  line-height: 1.6;
  margin: 22px 0;
  font-family: 'Fira Code', 'JetBrains Mono', Consolas, monospace;
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
  border-left: 4px solid #3498db;
}
code {
  background: #f1f4f8;
  padding: 3px 7px;
  border-radius: 4px;
  font-size: 0.88em;
  font-family: 'Fira Code', 'JetBrains Mono', Consolas, monospace;
  color: #c0392b;
  font-weight: 500;
}
pre code {
  background: transparent;
  padding: 0;
  color: inherit;
}

/* Blockquotes */
blockquote {
  background: linear-gradient(135deg, #f7f9fc, #f0f4f8);
  border-left: 4px solid #3498db;
  padding: 18px 24px;
  margin: 25px 0;
  border-radius: 0 8px 8px 0;
  color: #4a5b6a;
}
blockquote p {
  margin-bottom: 0;
  font-style: italic;
}

/* Custom Image Containers */
.pi {
  text-align: center;
  margin: 28px 0;
}
.pi img {
  max-width: 100%;
  max-height: 420px;
  border-radius: 8px;
  box-shadow: 0 8px 30px rgba(0,0,0,0.12);
  border: 1px solid rgba(0,0,0,0.05);
  transition: transform 0.3s ease;
}
.pi img:hover {
  transform: scale(1.01);
}

/* Placeholders (for backup) */
.ph {
  background: linear-gradient(135deg, #f5f7f8, #eef1f2);
  border: 2px dashed #cbd5e1;
  border-radius: 8px;
  padding: 40px 24px;
  text-align: center;
  margin: 25px 0;
  color: #64748b;
}
.phi {
  font-size: 2.8em;
  display: block;
  margin-bottom: 12px;
  opacity: .6;
}
.ph p {
  font-style: italic;
  text-align: center;
  font-size: 0.95em;
  margin: 0;
  font-family: 'Inter', sans-serif;
}

hr {
  border: none;
  border-top: 1px solid #eef2f7;
  margin: 28px 0;
}
strong {
  color: #194e70;
  font-weight: 600;
}

/* Nav Control Bar */
#nav {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  background: rgba(10, 10, 25, 0.88);
  backdrop-filter: blur(15px);
  -webkit-backdrop-filter: blur(15px);
  padding: 14px 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 16px;
  z-index: 100;
  border-top: 1px solid rgba(255,255,255,.06);
}
.nb {
  background: rgba(255,255,255,0.06);
  border: 1px solid rgba(255,255,255,0.12);
  color: rgba(255,255,255,0.9);
  padding: 9px 24px;
  border-radius: 30px;
  cursor: pointer;
  font-size: 13px;
  font-weight: 500;
  font-family: 'Inter', sans-serif;
  transition: all 0.2s ease;
}
.nb:hover {
  background: rgba(255,255,255,0.14);
  border-color: rgba(255,255,255,0.2);
  transform: translateY(-1px);
}
.nb:disabled {
  opacity: .15;
  cursor: default;
  transform: none;
}
#pi {
  color: rgba(255,255,255,.6);
  font-size: 13px;
  min-width: 130px;
  text-align: center;
  font-family: 'Inter', sans-serif;
}
#dots {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
  max-width: 250px;
  justify-content: center;
}
.dt {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: rgba(255,255,255,.15);
  cursor: pointer;
  transition: all .2s ease;
}
.dt.ac {
  background: #3498db;
  transform: scale(1.3);
}
.dt:hover {
  background: rgba(255,255,255,.4);
}

/* TOC Overlay styling */
#tov {
  display: none;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(8, 8, 18, 0.7);
  z-index: 200;
  justify-content: center;
  align-items: center;
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
}
#tov.on {
  display: flex;
}
#tp {
  background: #fafafa;
  padding: 40px 45px;
  border-radius: 16px;
  width: 90vw;
  max-width: 650px;
  max-height: 80vh;
  overflow-y: auto;
  box-shadow: 0 30px 90px rgba(0,0,0,0.6);
  border: 1px solid rgba(0,0,0,0.05);
}
#tp::-webkit-scrollbar {
  width: 5px;
}
#tp::-webkit-scrollbar-thumb {
  background: rgba(0,0,0,0.15);
  border-radius: 10px;
}
#tp h1 {
  text-align: center;
  margin-bottom: 24px;
  border-bottom: 2px solid #eef2f7;
  padding-bottom: 14px;
  color: #194e70;
  font-size: 1.6em;
}
.te {
  display: flex;
  align-items: center;
  padding: 11px 18px;
  margin: 4px 0;
  border-radius: 8px;
  color: #34495e;
  transition: all .2s ease;
  border-left: 4px solid transparent;
  font-size: 0.94em;
  text-decoration: none;
  font-family: 'Inter', sans-serif;
  font-weight: 500;
}
.te:hover {
  background: #eef3f8;
  border-left-color: #3498db;
  transform: translateX(4px);
}
.te.part {
  border-left-color: #1abc9c;
  font-weight: 700;
  background: #f0faf8;
  margin-top: 16px;
  font-size: 1.0em;
}
.te.appendix {
  border-left-color: #e67e22;
  background: #fff9f4;
}
.te.cover {
  border-left-color: #9b59b6;
}
.tn {
  color: #95a5a6;
  margin-right: 14px;
  font-size: .85em;
  font-weight: 600;
}
.tc {
  text-align: center;
  margin-top: 25px;
}

#cl, #cr {
  position: fixed;
  top: 0;
  height: 100vh;
  width: 15vw;
  cursor: pointer;
  z-index: 50;
}
#cl {
  left: 0;
}
#cr {
  right: 0;
}
#cl:hover {
  background: linear-gradient(to right, rgba(255,255,255,.02), transparent);
}
#cr:hover {
  background: linear-gradient(to left, rgba(255,255,255,.02), transparent);
}

@media(max-width:768px) {
  .page {
    width: 98vw;
    height: 88vh;
    border-radius: 8px;
  }
  .pbody {
    padding: 30px 24px;
    font-size: 15.5px;
  }
  h1 {
    font-size: 1.6em;
  }
  h2 {
    font-size: 1.25em;
  }
  .page.cover h1 {
    font-size: 2.2em;
  }
  .page.part h1 {
    font-size: 1.9em;
  }
  #dots {
    display: none;
  }
  .nb {
    padding: 8px 16px;
    font-size: 12px;
  }
}
</style>"""

# Replace old style block with the new one
content = re.sub(r'<style>.*?</style>', new_style, content, flags=re.DOTALL)

# 3. Parse var PAGES = [...]
print("Parsing PAGES array from HTML...")
match = re.search(r'var PAGES\s*=\s*(\[.*?\]);', content, re.DOTALL)
if not match:
    print("Error: Could not find var PAGES in HTML.")
    exit(1)

pages_str = match.group(1)
pages = json.loads(pages_str)
print(f"Loaded {len(pages)} pages.")

# Keep track of injections
injections_count = 0

for p in pages:
    pid = p.get('id')
    cls = p.get('cls')
    html = p.get('html', '')
    
    # Check Cover Image replacement
    if pid == 0 and cls == "cover":
        print("Injecting premium cover image into Cover page...")
        b64_cover = get_base64_img("00-cover.jpg")
        if b64_cover:
            # We want to replace any existing img tag in the cover HTML
            # Current HTML on page 0: <h2>A Beginner's Guide...</h2><hr><blockquote><strong><div class="pi"><img src="..."></div></strong></blockquote>
            new_cover_html = f'\n<h1>AUTO-TRADE YOUR FIRST STOCK</h1>\n<h2>A Beginner\'s Guide to Automated Trading with Hermes & moomoo</h2>\n<hr>\n<div class="pi"><img src="{b64_cover}" alt="Ebook Cover illustration of a friendly trading robot holding a tablet showing charts" style="max-height: 380px;"></div>\n'
            p['html'] = new_cover_html
            injections_count += 1
            print("  Cover image injected.")
            
    # Check other page placeholders
    # We find `<div class="ph">...<p>(description)</p></div>` blocks
    # Let's search using regex
    phs = list(re.finditer(r'<div class="ph">.*?<p>(.*?)</p>\s*</div>', html, re.DOTALL))
    
    if phs:
        # Reconstruct the HTML
        new_html = html
        offset = 0
        for ph in phs:
            ph_text = ph.group(0)
            desc = ph.group(1).strip()
            
            # Match placeholder description with image mapping
            matched_file = None
            for kw, fn in mappings:
                if kw.lower() in desc.lower():
                    matched_file = fn
                    break
            
            if matched_file:
                print(f"Found placeholder on Page {pid}: '{desc[:30]}...' -> Mapping to '{matched_file}'")
                b64_data = get_base64_img(matched_file)
                if b64_data:
                    # Replacement HTML block
                    replacement_html = f'<div class="pi"><img src="{b64_data}" alt="{desc}"></div>'
                    # Perform replacement
                    new_html = new_html.replace(ph_text, replacement_html)
                    injections_count += 1
                else:
                    print(f"  Warning: Base64 data not loaded for {matched_file}")
            else:
                print(f"  Warning: No matching image file found for placeholder: '{desc[:60]}...'")
        
        # Save updated HTML to the page dictionary
        p['html'] = new_html

# Write the updated PAGES back to the content
print(f"Writing updated PAGES array back (total {injections_count} changes made)...")
new_pages_str = json.dumps(pages, ensure_ascii=False)
# Safely replace in content. The old match was match.group(0).
# Let's replace the whole `var PAGES = ...;` line
content = content[:match.start()] + "var PAGES = " + new_pages_str + ";" + content[match.end():]

print("Saving modified HTML file back to disk...")
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Modification complete!")
