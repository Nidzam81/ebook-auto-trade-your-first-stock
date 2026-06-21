from playwright.sync_api import sync_playwright
import os

md_dir = r"C:\Users\Nidzam\ebook-auto-trading"
html_path = os.path.join(md_dir, "ebook-final.html")
pdf_path = os.path.join(md_dir, "ebook-flipbook.pdf")

print("=" * 50)
print("FLIPBOOK PDF GENERATOR v2")
print("=" * 50)
print(f"Input:  {html_path}")
print(f"Output: {pdf_path}")
print()

with sync_playwright() as p:
    browser = p.chromium.launch(
        args=[
            "--no-sandbox",
            "--disable-setuid-sandbox",
            "--disable-gpu",
            "--disable-dev-shm-usage",
            "--disable-software-rasterizer"
        ],
        headless=True
    )
    
    context = browser.new_context(
        viewport={"width": 900, "height": 1200},
        device_scale_factor=2
    )
    
    page = context.new_page()
    
    # Load HTML
    print("Loading HTML...")
    page.goto(f"file:///{html_path}", wait_until="domcontentloaded", timeout=30000)
    page.wait_for_timeout(2000)
    
    # Get dimensions
    total_height = page.evaluate("() => document.body.scrollHeight")
    print(f"Total content height: {total_height}px")
    
    # Generate PDF
    print("Generating PDF...")
    page.pdf(
        path=pdf_path,
        width="820px",
        height="1100px",
        print_background=True,
        prefer_css_page_size=False,
        margin={"top": "0px", "right": "0px", "bottom": "0px", "left": "0px"}
    )
    
    browser.close()

file_size = os.path.getsize(pdf_path)
print()
print("=" * 50)
print("SUCCESS!")
print(f"PDF: {pdf_path}")
print(f"Size: {file_size / 1024 / 1024:.1f} MB")
print("=" * 50)
