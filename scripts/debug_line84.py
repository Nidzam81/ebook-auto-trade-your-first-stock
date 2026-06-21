with open(r'C:/Users/Nidzam/ebook-auto-trading/scripts/generate_mockups.py', 'rb') as f:
    lines = f.readlines()
    line84 = lines[83]
    print(repr(line84))
    print('Length:', len(line84))
    for i, b in enumerate(line84):
        c = chr(b) if 32 <= b < 127 else '?'
        print(f'  byte {i}: {hex(b)} ({c})')
