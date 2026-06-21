
from PIL import Image, ImageDraw, ImageFont
import os

img_path = r"C:\Users\Nidzam\ebook-auto-trading\images\window-moomoo_OpenD.png"

if not os.path.exists(img_path):
    print("Screenshot not found, creating a mockup instead")
else:
    img = Image.open(img_path)
    print(f"Image size: {img.size}")
    
    # Create a draw object
    draw = ImageDraw.Draw(img)
    
    # Mask potential sensitive areas (top-right corner usually has account info)
    # Draw black rectangles over likely sensitive areas
    w, h = img.size
    
    # Mask top bar (window title bar area) - contains window title
    draw.rectangle([0, 0, w, 30], fill='#2c3e50')
    draw.text((10, 5), "moomoo OpenD", fill='white')
    
    # Mask any area that might show account ID (typically top portion)
    draw.rectangle([0, 30, w, 80], fill='#34495e')
    draw.text((10, 45), "API Connection Active", fill='#2ecc71')
    
    # Add a note
    draw.rectangle([0, h-40, w, h], fill='#2c3e50')
    draw.text((10, h-30), "Connected - Port 18888", fill='white')
    
    # Save masked version
    masked_path = r"C:\Users\Nidzam\ebook-auto-trading\images\04-moomoo-opend-masked.png"
    img.save(masked_path)
    print(f"Masked screenshot saved: {masked_path}")
