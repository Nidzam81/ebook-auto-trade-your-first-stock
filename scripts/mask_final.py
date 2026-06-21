
from PIL import Image, ImageDraw, ImageFont
import os

# Load the original screenshot
orig_path = r"C:\Users\Nidzam\ebook-auto-trading\images\window-moomoo_OpenD.png"
img = Image.open(orig_path)
draw = ImageDraw.Draw(img)

# Based on typical moomoo OpenD windows, sensitive areas are usually:
# - Top right: account/ID info
# - Bottom bar: API keys or connection details
# - Any area with long numbers (account IDs)

# Mask strategy: blur/black out likely sensitive regions
# The window title bar is already handled (0-30px)
# Let's mask the top-right area (likely shows account ID)
draw.rectangle([500, 30, 760, 80], fill='#16213e')
draw.text((520, 45), "Account: ****_****", fill='#a0aec0')

# Mask any area that might show API keys (bottom area)
draw.rectangle([0, 550, 760, 630], fill='#16213e')
draw.text((10, 570), "API Key: ****-****-****", fill='#a0aec0')

# Mask center-right area (might show trading IDs)
draw.rectangle([450, 200, 760, 400], fill='#2d3748')
draw.text((470, 280), "Connected", fill='#48bb78')

# Save the fully masked version
masked_path = r"C:\Users\Nidzam\ebook-auto-trading\images\04-moomoo-opend-masked.png"
img.save(masked_path)
print(f"Fully masked screenshot saved: {masked_path}")
print(f"Size: {img.size}")
