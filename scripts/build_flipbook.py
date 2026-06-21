"""
Full rebuild of ebook-flipbook.html from FULL-EBOOK.md.
Converts markdown to HTML, injects images, premium CSS, and cmd-block JS.
"""
import re, json, os, sys, base64

try:
    import markdown
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'markdown', '-q'])
    import markdown

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MD_PATH = os.path.join(BASE, 'FULL-EBOOK.md')
HTML_PATH = os.path.join(BASE, 'ebook-flipbook.html')
IMAGES_DIR = os.path.join(BASE, 'images')

with open(MD_PATH, 'r', encoding='utf-8') as f:
    md_text = f.read()

# Split into pages by <h1> headings only
lines = md_text.split('\n')
pages = []
current_title = None
current_lines = []

def flush_page():
    if current_title is None and not current_lines:
        return
    title = current_title or 'Untitled'
    body = '\n'.join(current_lines).strip()
    cls = 'chapter'
    if 'Auto-Trade' in title or 'Cover' in title:
        cls = 'cover'
    elif 'Table of Contents' in title or 'TABLE OF CONTENTS' in title:
        cls = 'toc'
    elif title.startswith('PART '):
        cls = 'part'
    elif title.startswith('APPENDICES'):
        cls = 'part'
    elif title.startswith('Appendix'):
        cls = 'appendix'
    elif title.startswith('Chapter'):
        cls = 'chapter'
    pages.append({'title': title, 'cls': cls, 'body': body})

for line in lines:
    h1_match = re.match(r'^#\s+(.+)', line)
    if h1_match:
        flush_page()
        current_title = h1_match.group(1).strip()
        current_lines = []
    else:
        current_lines.append(line)
flush_page()

print("Split into", len(pages), "pages")

# Image mapping: keyword -> filename
IMAGE_MAP = [
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

def get_base64_img(filename):
    path = os.path.join(IMAGES_DIR, filename)
    if not os.path.exists(path):
        return None
    ext = os.path.splitext(filename)[1].lower().replace('.', '')
    if ext == 'jpg':
        ext = 'jpeg'
    with open(path, 'rb') as f:
        data = f.read()
    b64 = base64.b64encode(data).decode('utf-8')
    return "data:image/" + ext + ";base64," + b64

def replace_image_placeholders(html):
    """Replace IMAGE PLACEHOLDER blockquotes with actual images."""
    def replacer(m):
        full = m.group(0)
        desc_m = re.search(r'IMAGE PLACEHOLDER:\s*(.+?)\]', full)
        if not desc_m:
            return full
        desc = desc_m.group(1).strip()
        
        # Find matching image
        matched_file = None
        for kw, fn in IMAGE_MAP:
            if kw.lower() in desc.lower():
                matched_file = fn
                break
        
        if matched_file:
            b64 = get_base64_img(matched_file)
            if b64:
                return '<div class="pi"><img src="' + b64 + '" alt="' + desc + '"></div>'
        
        # No match - keep as placeholder
        return '<div class="ph"><p>' + desc + '</p></div>'
    
    return re.sub(
        r'<blockquote>[\s\S]*?<strong>\[IMAGE PLACEHOLDER:[\s\S]*?</strong>[\s\S]*?</blockquote>',
        replacer, html
    )

# Convert markdown to HTML and replace images
md = markdown.Markdown(extensions=['tables', 'fenced_code'])
html_pages = []
for i, page in enumerate(pages):
    md.reset()
    body_html = md.convert(page['body'])
    
    # Replace cover page specially
    if i == 0 and page['cls'] == 'cover':
        b64 = get_base64_img('00-cover.jpg')
        if b64:
            body_html = '\n<h1>AUTO-TRADE YOUR FIRST STOCK</h1>\n<h2>A Beginner\'s Guide to Automated Trading with Hermes & moomoo</h2>\n<hr>\n<div class="pi"><img src="' + b64 + '" alt="Ebook Cover" style="max-height: 380px;"></div>\n'
    else:
        body_html = replace_image_placeholders(body_html)
    
    html_pages.append({
        'id': i,
        'cls': page['cls'],
        'title': page['title'],
        'html': body_html
    })

pages_json = json.dumps(html_pages, ensure_ascii=False)

# Build the complete HTML
html = '<!DOCTYPE html>\n<html><head>\n'
html += '<meta charset="UTF-8">\n'
html += '<meta name="viewport" content="width=device-width,initial-scale=1.0">\n'
html += '<title>Auto-Trade Your First Stock</title>\n'
html += '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Lora:ital,wght@0,400;0,500;0,600;1,400&family=Outfit:wght@400;500;600;700;800&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">\n'

# Read the premium CSS from inject_assets.py
inject_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'inject_assets.py')
with open(inject_path, 'r', encoding='utf-8') as f:
    inject_code = f.read()

# Extract the new_style block from inject_assets.py
style_match = re.search(r'new_style = """(.*?)"""', inject_code, re.DOTALL)
if style_match:
    premium_css = style_match.group(1)
    # Strip the <style> and </style> tags that inject_assets.py includes
    premium_css = re.sub(r'^<style>\s*', '', premium_css)
    premium_css = re.sub(r'\s*</style>\s*$', '', premium_css)
else:
    premium_css = ""

# Add cmd-block CSS
cmd_css = """
/* -- Terminal / Command Block -- */
.cmd-block { background:#0d1117; border-radius:10px; margin:24px 0; overflow:hidden; box-shadow:0 10px 30px rgba(0,0,0,0.25),0 0 0 1px rgba(255,255,255,0.06); font-family:'Fira Code','JetBrains Mono',Consolas,monospace; }
.cmd-block-header { background:#1c1f26; padding:9px 14px; display:flex; align-items:center; gap:7px; border-bottom:1px solid rgba(255,255,255,0.06); }
.cmd-block-dot { width:12px; height:12px; border-radius:50%; display:inline-block; flex-shrink:0; }
.cmd-block-dot.red { background:#ff5f57; }
.cmd-block-dot.yellow { background:#febc2e; }
.cmd-block-dot.green { background:#28c840; }
.cmd-block-label { flex:1; font-size:11px; color:rgba(255,255,255,0.35); letter-spacing:0.5px; font-family:'Inter',sans-serif; font-weight:500; text-align:center; }
.cmd-block-copy { background:rgba(255,255,255,0.07); border:1px solid rgba(255,255,255,0.12); color:rgba(255,255,255,0.55); font-size:11px; padding:3px 10px; border-radius:5px; cursor:pointer; font-family:'Inter',sans-serif; transition:all 0.2s ease; white-space:nowrap; }
.cmd-block-copy:hover { background:rgba(52,152,219,0.25); border-color:rgba(52,152,219,0.5); color:#fff; }
.cmd-block-body { padding:16px 20px; overflow-x:auto; color:#c9d1d9; font-size:0.87em; line-height:1.7; white-space:pre-wrap; word-break:break-word; }
.cmd-block-body p { margin:0 0 6px 0; text-align:left; }
.cmd-block-body p:last-child { margin-bottom:0; }
.cmd-block-body ul, .cmd-block-body ol { margin:6px 0; padding-left:22px; }
.cmd-block-body li { margin:3px 0; }
"""

html += '<style>\n' + premium_css + cmd_css + '\n</style>\n'
html += '</head>\n<body>\n'
html += '<div id="book"></div>\n'
html += '<div id="cl" onclick="prev()"></div>\n'
html += '<div id="cr" onclick="next()"></div>\n'
html += '<div id="nav">\n'
html += '  <button class="nb" id="bp" onclick="prev()">&#9664; Prev</button>\n'
html += '  <span id="pi">Page 1 of ' + str(len(html_pages)) + '</span>\n'
html += '  <button class="nb" id="bn" onclick="next()">Next &#9654;</button>\n'
html += '</div>\n'
html += '<script>\n'
html += 'var PAGES = ' + pages_json + ';\n'
html += 'var T=' + str(len(html_pages)) + ', cur=0, lock=false, pageEl=null;\n'

# upgradeCodeBlocks JS
html += """
// -- Upgrade <code> blocks to terminal command boxes --
// Handles both standalone <code> and <pre><code> patterns
function upgradeCodeBlocks(container) {
  var codes = container.querySelectorAll('code');
  codes.forEach(function(code) {
    var inner = code.innerHTML;
    var text  = code.textContent || '';
    var isBlock = (
      inner.indexOf('<p>') !== -1 ||
      inner.indexOf('<ul>') !== -1 ||
      inner.indexOf('<ol>') !== -1 ||
      inner.indexOf('<h') !== -1 ||
      text.trim().length > 60
    );
    if (!isBlock) return;
    var block = document.createElement('div');
    block.className = 'cmd-block';
    var hdr = document.createElement('div');
    hdr.className = 'cmd-block-header';
    hdr.innerHTML =
      '<span class="cmd-block-dot red"></span>' +
      '<span class="cmd-block-dot yellow"></span>' +
      '<span class="cmd-block-dot green"></span>' +
      '<span class="cmd-block-label">command</span>';
    var copyBtn = document.createElement('button');
    copyBtn.className = 'cmd-block-copy';
    copyBtn.textContent = 'Copy';
    var capturedText = text;
    copyBtn.addEventListener('click', function() {
      if (navigator.clipboard) navigator.clipboard.writeText(capturedText);
      copyBtn.textContent = 'Copied!';
      setTimeout(function() { copyBtn.textContent = 'Copy'; }, 1500);
    });
    hdr.appendChild(copyBtn);
    var body = document.createElement('div');
    body.className = 'cmd-block-body';
    body.innerHTML = inner;
    block.appendChild(hdr);
    block.appendChild(body);
    var parent = code.parentElement;
    if (!parent) return;
    if (parent.tagName === 'PRE') {
      if (parent.parentElement) parent.parentElement.replaceChild(block, parent);
      return;
    }
    if (parent.tagName === 'P' && parent.children.length === 1) {
      parent.parentElement && parent.parentElement.replaceChild(block, parent);
    } else {
      parent.replaceChild(block, code);
    }
  });
}
"""

# Navigation JS
html += 'function makePage(n){var p=PAGES[n];var el=document.createElement("div");el.className="page "+p.cls;var hdr="";if(p.cls==="cover")hdr="<div class=\\"phdr phdr-cover\\">&#128218; Auto-Trade Your First Stock</div>";else if(p.cls==="toc")hdr="<div class=\\"phdr phdr-toc\\">&#128203; Table of Contents</div>";else if(p.cls==="part")hdr="<div class=\\"phdr phdr-part\\">"+p.title+"</div>";else if(p.cls==="chapter"){var m=p.title.match(/Chapter (\\d+)/);var num=m?m[1]:"";var ttl=p.title.replace(/Chapter \\d+:\\s*/,"");hdr="<div class=\\"phdr phdr-chapter\\"><span class=\\"ch-num\\">Ch "+num+"</span><span class=\\"ch-title\\">"+ttl+"</span></div>"}else if(p.cls==="appendix")hdr="<div class=\\"phdr phdr-appendix\\">"+p.title+"</div>";el.innerHTML=hdr+"<div class=\\"pbody\\">"+p.html+"</div><div class=\\"pnum\\">Page "+(n+1)+" of "+T+"</div>";return el}\n'
html += 'function render(n){var el=makePage(n);upgradeCodeBlocks(el);el.classList.add("current");document.getElementById("book").appendChild(el);pageEl=el;cur=n}\n'
html += 'function next(){if(lock||cur>=T-1)return;lock=true;pageEl.classList.add("leaving");setTimeout(function(){pageEl.remove();render(cur+1);lock=false},500)}\n'
html += 'function prev(){if(lock||cur<=0)return;lock=true;pageEl.classList.add("leaving");setTimeout(function(){pageEl.remove();render(cur-1);lock=false},500)}\n'
html += 'function go(n){if(lock||n<0||n>=T)return;lock=true;pageEl.classList.add("leaving");setTimeout(function(){pageEl.remove();render(n);lock=false},500)}\n'
html += 'document.addEventListener("keydown",function(e){if(e.key==="ArrowRight"||e.key===" "||e.key==="PageDown"){e.preventDefault();next()}else if(e.key==="ArrowLeft"||e.key==="PageUp"){e.preventDefault();prev()}else if(e.key==="Home"){e.preventDefault();go(0)}else if(e.key==="End"){e.preventDefault();go(T-1)}});\n'
html += 'document.getElementById("bp").disabled=true;\n'
html += 'render(0);\n'
html += '</script>\n</body></html>'

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(html)

# Verify
with open(HTML_PATH, 'r', encoding='utf-8') as f:
    verify = f.read()

import re as re2
data_imgs = len(re2.findall(r'data:image/', verify))
phs = len(re2.findall(r'<div class="ph">', verify))
pi_imgs = len(re2.findall(r'<div class="pi"><img', verify))

print("\n=== Build Complete ===")
print("File size:", len(verify) // 1024, "KB")
print("Pages:", len(html_pages))
print("Base64 images:", data_imgs)
print("Pi image divs:", pi_imgs)
print("Remaining placeholders:", phs)
print("Has upgradeCodeBlocks:", "upgradeCodeBlocks" in verify)
print("Has cmd-block CSS:", "cmd-block {" in verify)
print("Has Google Fonts:", "fonts.googleapis.com" in verify)
print("upgradeCodeBlocks count:", verify.count("upgradeCodeBlocks"))
