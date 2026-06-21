
from PIL import Image, ImageDraw, ImageFont
import os

img_dir = r"C:\Users\Nidzam\ebook-auto-trading\images"

# Create a clean mockup of the moomoo OpenD window
img = Image.new('RGB', (760, 630), color='#1e1e2e')
draw = ImageDraw.Draw(img)

# Title bar
draw.rectangle([0, 0, 760, 40], fill='#16213e')
draw.text((10, 10), "moomoo OpenD - API Console", fill='#ffffff')

# Status area
draw.rectangle([20, 60, 740, 120], fill='#2d3748')
draw.text((40, 75), "Connection Status:", fill='#a0aec0')
draw.text((40, 95), "CONNECTED - Port 18888", fill='#48bb78')

# API log area
draw.rectangle([20, 140, 740, 500], fill='#2d3748')
draw.text((40, 155), "API Log:", fill='#a0aec0')

# Sample log entries (with masked IDs)
logs = [
    "10:00:01 | GET /api/v1/account | Status: 200",
    "10:00:02 | Account: ****_****_****_1234",
    "10:00:05 | GET /api/v1/quote/NVDA | Status: 200",
    "10:00:06 | RSI: 28 (signal: BUY)",
    "10:00:10 | POST /api/v1/order | SIMULATE",
    "10:00:11 | Order: BUY 10 NVDA @ $142.50",
    "10:00:12 | Order ID: ****-****-****-5678",
    "10:00:13 | Status: FILLED (SIMULATE)",
    "10:30:01 | GET /api/v1/account | Status: 200",
    "10:30:05 | GET /api/v1/quote/NVDA | Status: 200",
    "10:30:06 | RSI: 32 (signal: WAIT)",
    "11:00:01 | GET /api/v1/account | Status: 200",
]

y = 175
for log in logs:
    color = '#a0aec0'
    if 'BUY' in log and 'Order' in log:
        color = '#48bb78'
    elif 'SELL' in log:
        color = '#f56565'
    elif 'WAIT' in log:
        color = '#ecc94b'
    elif 'Account' in log or 'Order ID' in log:
        color = '#a0aec0'
    draw.text((40, y), log, fill=color)
    y += 18

# Bottom status bar
draw.rectangle([0, 580, 760, 630], fill='#16213e')
draw.text((10, 595), "Status: Running | API v1.0 | SIMULATE Mode", fill='#48bb78')

# Save
output_path = os.path.join(img_dir, '04-moomoo-opend-clean.png')
img.save(output_path)
print(f"Clean moomoo OpenD mockup saved: {output_path}")
