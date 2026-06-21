
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np
import os

img_dir = r"C:\Users\Nidzam\ebook-auto-trading\images"

fig, ax = plt.subplots(1, 1, figsize=(8, 11))
ax.set_xlim(0, 8)
ax.set_ylim(0, 11)
ax.axis('off')
ax.set_facecolor('#1a1a2e')
fig.patch.set_facecolor('#1a1a2e')

# Border
border = FancyBboxPatch((0.2, 0.2), 7.6, 10.6,
                         boxstyle="round,pad=0.2",
                         facecolor='none', edgecolor='#3498db', linewidth=3)
ax.add_patch(border)

# Title
ax.text(4, 9.5, 'AUTO-TRADE', fontsize=32, fontweight='bold',
        ha='center', va='center', color='#3498db')
ax.text(4, 8.8, 'YOUR FIRST STOCK', fontsize=20, fontweight='bold',
        ha='center', va='center', color='white')

# Subtitle
ax.text(4, 7.8, 'A Beginner\'s Guide to Automated Trading', fontsize=13,
        ha='center', va='center', color='#a0a0a0')
ax.text(4, 7.3, 'with Hermes & moomoo', fontsize=13,
        ha='center', va='center', color='#a0a0a0')

# Robot character (simple geometric representation)
# Head
head = plt.Circle((4, 5.5), 0.8, facecolor='#2ecc71', edgecolor='#27ae60', linewidth=3)
ax.add_patch(head)
# Eyes
ax.plot(3.7, 5.6, 'o', color='white', markersize=8)
ax.plot(4.3, 5.6, 'o', color='white', markersize=8)
ax.plot(3.7, 5.6, 'o', color='#2c3e50', markersize=4)
ax.plot(4.3, 5.6, 'o', color='#2c3e50', markersize=4)
# Smile
ax.plot([3.6, 4.0, 4.4], [5.2, 5.0, 5.2], color='white', linewidth=2)

# Arms holding chart and phone
# Left arm -> chart
ax.plot([3.2, 2.0], [5.0, 4.0], color='#2ecc71', linewidth=4)
# Right arm -> phone
ax.plot([4.8, 6.0], [5.0, 4.0], color='#2ecc71', linewidth=4)

# Stock chart (left)
chart_box = FancyBboxPatch((0.8, 3.0), 2.0, 1.5,
                            boxstyle="round,pad=0.1",
                            facecolor='#2c3e50', edgecolor='#3498db', linewidth=2)
ax.add_patch(chart_box)
# Chart line
x_chart = np.linspace(1.0, 2.6, 15)
y_chart = np.linspace(3.3, 4.2, 15) + np.random.randn(15) * 0.1
ax.plot(x_chart, y_chart, color='#27ae60', linewidth=2)
ax.text(1.8, 3.15, 'STOCK', fontsize=8, fontweight='bold',
        ha='center', va='center', color='#27ae60')

# Phone (right)
phone_box = FancyBboxPatch((5.2, 3.0), 2.0, 1.5,
                            boxstyle="round,pad=0.1",
                            facecolor='#2c3e50', edgecolor='#e74c3c', linewidth=2)
ax.add_patch(phone_box)
ax.text(6.2, 3.8, 'moomoo', fontsize=10, fontweight='bold',
        ha='center', va='center', color='#e74c3c')
ax.text(6.2, 3.3, 'API', fontsize=9, ha='center', va='center', color='#a0a0a0')

# Arrow between (the connection)
ax.annotate('', xy=(5.2, 3.75), xytext=(2.9, 3.75),
            arrowprops=dict(arrowstyle='->', color='#9b59b6', lw=3, linestyle='--'))
ax.text(4.05, 3.95, 'OpenD', fontsize=9, ha='center', va='center',
        color='#9b59b6', fontweight='bold')

# Key features
features = [
    'Step-by-step setup',
    'No coding required',
    'Practice with SIMULATE',
    'Go LIVE when ready',
]
for i, feat in enumerate(features):
    y = 2.2 - i * 0.4
    ax.text(1.0, y, '[OK]', fontsize=10, ha='left', va='center', color='#27ae60')
    ax.text(1.5, y, feat, fontsize=10, ha='left', va='center', color='#a0a0a0')

# Author
ax.text(4, 0.7, 'Version 1.0 | June 2026', fontsize=9,
        ha='center', va='center', color='#7f8c8d')

plt.tight_layout()
plt.savefig(os.path.join(img_dir, '00-cover.png'), dpi=150, bbox_inches='tight')
plt.close()
print("Cover image saved")
