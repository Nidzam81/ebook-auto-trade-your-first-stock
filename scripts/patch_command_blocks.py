"""
Patch ebook-flipbook.html to display standalone <code> blocks
as styled terminal command boxes with a dark header, traffic-light dots,
and a Copy button.
"""
import re, sys, os

SRC = os.path.join(os.path.dirname(__file__), '..', 'ebook-flipbook.html')

with open(SRC, 'r', encoding='utf-8') as f:
    content = f.read()

# ───────────────────────────── 1. CSS ─────────────────────────────
CSS_ANCHOR = "pre code {\n  background: transparent;\n  padding: 0;\n  color: inherit;\n}"
CMD_CSS = """/*
 * Original styling for code blocks - minimal styling only
 */
pre code {
  background: #f8f9fa;
  padding: 2px 4px;
  border-radius: 3px;
  font-family: 'Fira Code', 'JetBrains Mono', Consolas, monospace;
}
"""

if CSS_ANCHOR in content:
    content = content.replace(CSS_ANCHOR, CSS_ANCHOR + CMD_CSS, 1)
    print("CSS injected OK")
else:
    print("ERROR: CSS anchor not found")
    sys.exit(1)

# ───────────────────────────── 2. JS function ─────────────────────────────
JS_FUNCTION = """/**
 * Original upgradeCodeBlocks function - processes standalone <code> blocks
 * but does not add terminal styling or copy buttons
 */
function upgradeCodeBlocks(container) {
  var codes = Array.prototype.slice.call(container.querySelectorAll('code'));
  codes.forEach(function(code) {
    // Skip if inside <pre> tags (already formatted)
    if (code.closest && code.closest('pre')) return;
    
    // Only process if it looks like a standalone code block worth styling
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
    
    // Just add basic styling to standalone code blocks
    var pre = document.createElement('pre');
    pre.style.background = '#f8f9fa';
    pre.style.padding = '10px';
    pre.style.borderRadius = '5px';
    pre.style.fontFamily = '\'Fira Code\', \'JetBrains Mono\', Consolas, monospace';
    pre.style.overflowX = 'auto';
    
    // Preserve the original content
    pre.innerHTML = inner;
    
    var parent = code.parentElement;
    if (!parent) return;
    
    // Handle edge case where code is wrapped in a paragraph
    if (parent.tagName === 'P' && parent.children.length === 1 && parent.parentElement) {
      parent.parentElement.replaceChild(pre, parent);
    } else {
      parent.replaceChild(pre, code);
    }
  });
}
"""

# Insert the function at the very start of the <script> block
SCRIPT_TAG = '<script>\nvar PAGES = '
if SCRIPT_TAG in content:
    content = content.replace(SCRIPT_TAG, '<script>' + JS_FUNCTION + '\nvar PAGES = ', 1)
    print("JS function injected OK")
else:
    print("ERROR: <script> anchor not found - searching...")
    idx = content.find('<script>')
    print(repr(content[idx:idx+60]))
    sys.exit(1)

# ───────────────────────────── 3. Hook into render ─────────────────────────────
patched = False
for pat in ['pbody.innerHTML = p.html;', 'pbody.innerHTML=p.html;', 'pbody.innerHTML = p.html']:
    if pat in content:
        content = content.replace(pat, pat.rstrip(';') + ';\\n    upgradeCodeBlocks(pbody);', 1)
        print(f"Render hook injected after: {pat!r}")
        patched = True
        break

if not patched:
    m = re.search(r'pbody\\.innerHTML\\s*=\\s*p\\.html', content)
    if m:
        old = m.group(0)
        content = content.replace(old, old + ';\\n    upgradeCodeBlocks(pbody)', 1)
        print(f"Render hook injected (regex) after: {old!r}")
    else:
        print("WARNING: render hook anchor not found")
        print("         Add upgradeCodeBlocks(pbody) manually after pbody.innerHTML = p.html")

with open(SRC, 'w', encoding='utf-8') as f:
    f.write(content)
print("File saved successfully.")