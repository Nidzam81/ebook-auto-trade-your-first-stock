from playwright.sync_api import sync_playwright
import os
import base64
from PIL import Image
import io

md_dir = r"C:\Users\Nidzam\ebook-auto-trading"
flipbook_path = os.path.join(md_dir, "flipbook.html")
pdf_output = os.path.join(md_dir, "ebook-flipbook.pdf")

print("Generating flipbook PDF with individual page renders...")

with sync_playwright() as p:
    browser = p.chromium.launch(
        args=["--no-sandbox", "--disable-setuid-sandbox", "--disable-gpu"]
    )
    # Create a large viewport to fit one page at a time
    page = browser.new_page(viewport={"width": 900, "height": 1100})
    page.goto(f"file:///{flipbook_path}")
    page.wait_for_timeout(2000)
    
    # Get total number of pages
    total_pages = page.evaluate("() => document.querySelectorAll('.page').length")
    print(f"Total pages in flipbook: {total_pages}")
    
    # Capture each page as an image
    images = []
    
    for i in range(total_pages):
        # Flip to page i
        page.evaluate(f"() => {{ currentPage = {i}; updateUI(); }}")
        page.wait_for_timeout(500)
        
        # Take screenshot
        screenshot = page.screenshot()
        img = Image.open(io.BytesIO(screenshot))
        images.append(img)
        
        if (i + 1) % 10 == 0:
            print(f"  Captured {i+1}/{total_pages} pages...")
    
    browser.close()
    
    # Save as PDF
    print(f"Saving PDF with {len(images)} pages...")
    if images:
        first_image = images[0]
        rest_images = images[1:]
        
        first_image.save(
            pdf_output,
            "PDF",
            save_all=True,
            append_images=rest_images,
            resolution=150
        )
        
        file_size = os.path.getsize(pdf_output)
        print(f"\nFlipbook PDF created: {pdf_output}")
        print(f"File size: {file_size / 1024 / 1024:.1f} MB")
        print(f"Pages: {len(images)}")
    else:
        print("No images captured!")
