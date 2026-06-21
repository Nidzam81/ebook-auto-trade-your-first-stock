
import ctypes
import ctypes.wintypes
import os
from PIL import Image

user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32

img_dir = r"C:\Users\Nidzam\ebook-auto-trading\images"
os.makedirs(img_dir, exist_ok=True)

# Get screen dimensions
width = user32.GetSystemMetrics(0)
height = user32.GetSystemMetrics(1)
print(f"Screen: {width}x{height}")

# Create device contexts
hwnd_desktop = user32.GetDesktopWindow()
hdc_desktop = user32.GetDC(hwnd_desktop)
hdc_mem = gdi32.CreateCompatibleDC(hdc_desktop)

# Create bitmap
hbitmap = gdi32.CreateCompatibleBitmap(hdc_desktop, width, height)
gdi32.SelectObject(hdc_mem, hbitmap)

# Copy screen to bitmap
gdi32.BitBlt(hdc_mem, 0, 0, width, height, hdc_desktop, 0, 0, 0x00CC0020)  # SRCCOPY

# Convert to PIL Image
import struct
bmp_info = ctypes.c_buffer(40)
gdi32.GetBitmapBits(hbitmap, 0, None)  # get size

# Use the GetDIBits approach
class BITMAPINFOHEADER(ctypes.Structure):
    _fields_ = [
        ('biSize', ctypes.c_uint32),
        ('biWidth', ctypes.c_int32),
        ('biHeight', ctypes.c_int32),
        ('biPlanes', ctypes.c_uint16),
        ('biBitCount', ctypes.c_uint16),
        ('biCompression', ctypes.c_uint32),
        ('biSizeImage', ctypes.c_uint32),
        ('biXPelsPerMeter', ctypes.c_int32),
        ('biYPelsPerMeter', ctypes.c_int32),
        ('biClrUsed', ctypes.c_uint32),
        ('biClrImportant', ctypes.c_uint32),
    ]

# Simpler approach: use the bitmap bits
buf_size = width * height * 4
buf = ctypes.create_string_buffer(buf_size)
gdi32.GetBitmapBits(hbitmap, buf_size, buf)

# Create image (BGRA format, need to convert to RGB)
img = Image.frombytes('RGB', (width, height), buf.raw, 'raw', 'BGRX')

filename = os.path.join(img_dir, "desktop-screenshot.png")
img.save(filename)
print(f"Saved: {filename}")

# Cleanup
gdi32.DeleteObject(hbitmap)
gdi32.DeleteDC(hdc_mem)
user32.ReleaseDC(hwnd_desktop, hdc_desktop)
