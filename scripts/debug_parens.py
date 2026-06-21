with open(r'C:/Users/Nidzam/ebook-auto-trading/scripts/generate_mockups.py', 'rb') as f:
    content = f.read()

# Find the line and check what's before it
lines = content.split(b'\n')
# Check lines 75-90
for i in range(74, 92):
    if i < len(lines):
        line = lines[i]
        # Count open/close parens
        opens = line.count(b'(')
        closes = line.count(b')')
        print(f"Line {i+1}: opens={opens} closes={closes} diff={opens-closes}")
        if opens != closes:
            print(f"  >>> MISMATCH: {line}")
