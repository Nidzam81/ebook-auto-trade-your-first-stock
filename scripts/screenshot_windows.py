
import win32gui
import time
from PIL import Image, ImageGrab
import os

img_dir = r"C:\Users\Nidzam\ebook-auto-trading\images"
os.makedirs(img_dir, exist_ok=True)

# First take a full screen screenshot
print("Taking full screen screenshot...")
try:
    img = ImageGrab.grab()
    filename = os.path.join(img_dir, "full-desktop-screenshot.png")
    img.save(filename)
    print(f"  Saved: {filename}")
except Exception as e:
    print(f"  Full screen error: {e}")

# Now try to capture specific windows using PrintWindow
def capture_window(hwnd, title):
    try:
        import win32ui
        import win32con
        
        # Get window dimensions
        rect = win32gui.GetWindowRect(hwnd)
        left, top, right, bottom = rect
        width = right - left
        height = bottom - top
        
        if width <= 0 or height <= 0:
            return
        
        # Create device context
        hwnd_dc = win32gui.GetWindowDC(hwnd)
        mfc_dc = win32ui.CreateDCFromHandle(hwnd_dc)
        save_dc = mfc_dc.CreateCompatibleDC()
        
        bitmap = win32ui.CreateBitmap()
        bitmap.CreateCompatibleBitmap(mfc_dc, width, height)
        save_dc.SelectObject(bitmap)
        
        # Print window to bitmap
        result = win32gui.PrintWindow(hwnd, save_dc.GetSafeHdc(), 0)
        
        if result:
            bmp_info = bitmap.GetInfo()
            bmp_str = bitmap.GetBitmapBits(True)
            im = Image.frombuffer(
                'RGB',
                (bmp_info['bmWidth'], bmp_info['bmHeight']),
                bmp_str, 'raw', 'BGRX', 0, 1
            )
            
            safe_title = title.replace(' ', '_').replace('/', '-').replace('\\', '-').replace(':', '').replace('*', '').replace('?', '').replace('"', '').replace('<', '').replace('>', '').replace('|', '')
            filename = os.path.join(img_dir, f"window-{safe_title}.png")
            im.save(filename)
            print(f"  Saved: {filename} ({width}x{height})")
        
        # Cleanup
        win32gui.DeleteObject(bitmap.GetHandle())
        save_dc.DeleteDC()
        mfc_dc.DeleteDC()
        win32gui.ReleaseDC(hwnd, hwnd_dc)
        
    except Exception as e:
        print(f"  Error capturing {title}: {e}")

def enum_callback(hwnd, results):
    if win32gui.IsWindowVisible(hwnd):
        title = win32gui.GetWindowText(hwnd)
        if title and ("moomoo" in title.lower() or "OpenD" in title.lower() or "hermes" in title.lower()):
            results.append((hwnd, title))
    return True

results = []
win32gui.EnumWindows(enum_callback, results)

if results:
    for hwnd, title in results:
        print(f"Capturing: {title}")
        capture_window(hwnd, title)
else:
    print("No matching windows found")
