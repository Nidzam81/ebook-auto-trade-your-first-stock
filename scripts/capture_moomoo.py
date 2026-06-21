
import ctypes
import ctypes.wintypes
import os
from PIL import Image
import win32gui

user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32

img_dir = r"C:\Users\Nidzam\ebook-auto-trading\images"
os.makedirs(img_dir, exist_ok=True)

def capture_window_by_hwnd(hwnd, title):
    """Capture a specific window by handle"""
    try:
        # Get window dimensions
        rect = win32gui.GetWindowRect(hwnd)
        left, top, right, bottom = rect
        w = right - left
        h = bottom - top
        
        if w <= 0 or h <= 0:
            print(f"  Invalid dimensions for {title}: {w}x{h}")
            return
        
        print(f"  Window '{title}' at ({left},{top}) size {w}x{h}")
        
        # Create device contexts
        hdc_window = user32.GetDC(hwnd)
        hdc_mem = gdi32.CreateCompatibleDC(hdc_window)
        
        # Create bitmap
        hbitmap = gdi32.CreateCompatibleBitmap(hdc_window, w, h)
        gdi32.SelectObject(hdc_mem, hbitmap)
        
        # Copy window content
        gdi32.BitBlt(hdc_mem, 0, 0, w, h, hdc_window, 0, 0, 0x00CC0020)
        
        # Convert to PIL
        buf_size = w * h * 4
        buf = ctypes.create_string_buffer(buf_size)
        gdi32.GetBitmapBits(hbitmap, buf_size, buf)
        
        img = Image.frombytes('RGB', (w, h), buf.raw, 'raw', 'BGRX')
        
        safe_title = title.replace(' ', '_').replace('/', '-').replace('\\', '-').replace(':', '').replace('*', '').replace('?', '').replace('"', '').replace('<', '').replace('>', '').replace('|', '')
        filename = os.path.join(img_dir, f"window-{safe_title}.png")
        img.save(filename)
        print(f"  Saved: {filename}")
        
        # Cleanup
        gdi32.DeleteObject(hbitmap)
        gdi32.DeleteDC(hdc_mem)
        user32.ReleaseDC(hwnd, hdc_window)
        
    except Exception as e:
        print(f"  Error: {e}")

# Capture moomoo_OpenD window (hwnd=460948)
print("Capturing moomoo_OpenD...")
capture_window_by_hwnd(460948, "moomoo_OpenD")

# Also try to find and capture any visible moomoo trading window
def enum_callback(hwnd, results):
    if win32gui.IsWindowVisible(hwnd):
        title = win32gui.GetWindowText(hwnd)
        if title and len(title) > 0:
            results.append((hwnd, title))
    return True

all_windows = []
win32gui.EnumWindows(enum_callback, all_windows)

print(f"\nAll visible windows ({len(all_windows)}):")
for hwnd, title in all_windows:
    if title.strip():
        print(f"  [{hwnd}] {title}")
