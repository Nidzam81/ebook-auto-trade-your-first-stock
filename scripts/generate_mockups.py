
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle
import numpy as np
import os

img_dir = r"C:\Users\Nidzam\ebook-auto-trading\images"

# ============================================================
# Image: Chapter 5 - Hermes Interface Mockup
# ============================================================
fig, ax = plt.subplots(1, 1, figsize=(12, 7))
ax.set_xlim(0, 12)
ax.set_ylim(0, 7)
ax.axis('off')
ax.set_facecolor('#1a1a2e')
fig.patch.set_facecolor('#1a1a2e')

# Title bar
ax.add_patch(Rectangle((0, 6.5), 12, 0.5, facecolor='#16213e', edgecolor='none'))
ax.text(0.3, 6.75, 'Hermes Agent', fontsize=14, fontweight='bold', 
        ha='left', va='center', color='white')

# Left sidebar
ax.add_patch(Rectangle((0, 0), 3, 6.5, facecolor='#0f3460', edgecolor='none'))
ax.text(0.3, 6.0, 'Conversations', fontsize=10, fontweight='bold',
        ha='left', va='center', color='#a0a0a0')
ax.text(0.5, 5.4, '> NVDA-RSI Agent', fontsize=10, ha='left', va='center', color='white')
ax.text(0.5, 4.9, '  AAPL-BB Agent', fontsize=10, ha='left', va='center', color='#a0a0a0')
ax.text(0.5, 4.4, '  Dashboard', fontsize=10, ha='left', va='center', color='#a0a0a0')

# Chat area
ax.add_patch(Rectangle((3, 0.8), 9, 5.7, facecolor='#1a1a2e', edgecolor='#0f3460', linewidth=1))

# User message (right aligned, blue bubble)
msg_box = FancyBboxPatch((7, 4.8), 4.5, 0.8,
                          boxstyle="round,pad=0.1",
                          facecolor='#3498db', edgecolor='none')
ax.add_patch(msg_box)
ax.text(9.25, 5.2, 'Check NVDA RSI', fontsize=11, ha='center', va='center', color='white')

# Hermes reply (left aligned, gray bubble)
reply_box = FancyBboxPatch((3.2, 3.5), 6, 1.0,
                            boxstyle="round,pad=0.1",
                            facecolor='#2c3e50', edgecolor='none')
ax.add_patch(reply_box)
ax.text(3.5, 3.9, 'NVDA RSI is 28 (below 30). Placing BUY order...', 
        fontsize=10, ha='left', va='center', color='white')

# Another user message
msg2_box = FancyBboxPatch((7, 2.3), 4.5, 0.8,
                           boxstyle="round,pad=0.1",
                           facecolor='#3498db', edgecolor='none')
ax.add_patch(msg2_box)
ax.text(9.25, 2.7, 'Show my balance', fontsize=11, ha='center', va='center', color='white')

# Hermes reply
reply2_box = FancyBboxPatch((3.2, 1.2), 6, 0.9,
                             boxstyle="round,pad=0.1",
                             facecolor='#2c3e50', edgecolor='none')
ax.add_patch(reply2_box)
ax.text(3.5, 1.6, 'Your SIMULATE balance: $1,000,000', 
        fontsize=10, ha='left', va='center', color='#2ecc71')

# Input box
ax.add_patch(Rectangle((3, 0), 9, 0.8, facecolor='#0f3460', edgecolor='none'))
ax.text(3.3, 0.4, 'Type a message...', fontsize=10, ha='left', va='center', color='#a0a0a0')

plt.tight_layout()
plt.savefig(os.path.join(img_dir, '05-hermes-interface.png'), dpi=150, bbox_inches='tight')
plt.close()
print("  Hermes interface mockup saved")

# ============================================================
# Image: Chapter 3 - Windows Explorer (C:\Trading folder)
# ============================================================
fig, ax = plt.subplots(1, 1, figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')
ax.set_facecolor('#f5f5f5')
fig.patch.set_facecolor('#f5f5f5')

# Title bar
ax.add_patch(Rectangle((0, 5.5), 10, 0.5, facecolor='#0078d4', edgecolor='none'))
ax.text(0.3, 5.75, 'C:\\Trading', fontsize=12, fontweight='bold',
        ha='left', va='center', color='white')

# Toolbar
ax.add_patch(Rectangle((0, 5.0), 10, 0.5, facecolor='#f0f0f0', edgecolor='#d0d0d0', linewidth=0.5))
ax.text(0.3, 5.25, 'File  Home  Share  View', fontsize=9, ha='left', va='center', color='#333')

# Address bar
ax.add_patch(Rectangle((0, 4.6), 10, 0.4, facecolor='white', edgecolor='#d0d0d0', linewidth=0.5))
ax.text(0.3, 4.8, 'C:\\Trading', fontsize=10, ha='left', va='center', color='#333')

# File list area
ax.add_patch(Rectangle((0, 0), 10, 4.6, facecolor='white', edgecolor='none'))

# Folder items
folders = [
    ('📁', 'agents', 'Agent configurations'),
    ('📁', 'logs', 'Trade logs'),
    ('📁', 'backups', 'Backup files'),
    ('📄', 'README.txt', 'Getting started'),
]

for i, (icon, name, desc) in enumerate(folders):
    y = 4.0 - i * 0.8
    ax.text(0.5, y, f'{icon} {name}', fontsize=11, ha='left', va='center',
            color='#333', fontweight='bold')
    ax.text(3.5, y, desc, fontsize=9, ha='left', va='center', color='#666')

# Highlight the Trading folder
highlight = FancyBboxPatch((0.2, 3.7), 9.5, 0.6,
                            boxstyle="round,pad=0.05",
                            facecolor='#fff3cd', edgecolor='#ffc107', linewidth=2)
ax.add_patch(highlight)
ax.text(0.5, 4.0, f'📁  Trading', fontsize=11, ha='left', va='center',
        color='#333', fontweight='bold')

plt.tight_layout()
plt.savefig(os.path.join(img_dir, '03-windows-explorer.png'), dpi=150, bbox_inches='tight')
plt.close()
print("  Windows Explorer mockup saved")

# ============================================================
# Image: Chapter 4 - Download moomoo mockup
# ============================================================
fig, ax = plt.subplots(1, 1, figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')
ax.set_facecolor='white'
fig.patch.set_facecolor='white'

# Browser frame
ax.add_patch(Rectangle((0, 5.5), 10, 0.5, facecolor='#4285f4', edgecolor='none'))
ax.text(0.3, 5.75, 'moomoo.com/download', fontsize=11, ha='left', va='center', color='white')

# Page content
ax.text(5, 4.5, 'Download moomoo Desktop', fontsize=18, fontweight='bold',
        ha='center', va='center', color='#2c3e50')

# Download button
btn = FancyBboxPatch((3.5, 2.8), 3, 0.8,
                      boxstyle="round,pad=0.1",
                      facecolor='#4285f4', edgecolor='#3367d6', linewidth=2)
ax.add_patch(btn)
ax.text(5, 3.2, 'Download for Windows', fontsize=13, fontweight='bold',
        ha='center', va='center', color='white')

# Arrow pointing to button
ax.annotate('Click here!', xy=(5, 3.6), xytext=(7.5, 4.2),
            fontsize=12, fontweight='bold', color='#e74c3c',
            arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=2))

plt.tight_layout()
plt.savefig(os.path.join(img_dir, '04-download-moomoo.png'), dpi=150, bbox_inches='tight')
plt.close()
print("  Download moomoo mockup saved")

# ============================================================
# Image: Chapter 6 - Configuration Form
# ============================================================
fig, ax = plt.subplots(1, 1, figsize=(8, 5))
ax.set_xlim(0, 8)
ax.set_ylim(0, 5)
ax.axis('off')
ax.set_facecolor('#f8f9fa')
fig.patch.set_facecolor='#f8f9fa'

ax.text(4, 4.5, 'moomoo API Configuration', fontsize=16, fontweight='bold',
        ha='center', va='center', color='#2c3e50')

fields = [
    ('Host:', 'localhost'),
    ('Port:', '18888'),
    ('Password:', '********'),
    ('Environment:', 'SIMULATE'),
]

for i, (label, value) in enumerate(fields):
    y = 3.6 - i * 0.7
    ax.text(1.5, y, label, fontsize=12, ha='right', va='center',
            color='#34495e', fontweight='bold')
    
    box = FancyBboxPatch((1.8, y-0.25), 5, 0.5,
                          boxstyle="round,pad=0.05",
                          facecolor='white', edgecolor='#bdc3c7', linewidth=1)
    ax.add_patch(box)
    ax.text(2.0, y, value, fontsize=12, ha='left', va='center', color='#2c3e50')

# Connect button
btn = FancyBboxPatch((3, 0.5), 2, 0.6,
                      boxstyle="round,pad=0.1",
                      facecolor='#27ae60', edgecolor='#1e8449', linewidth=2)
ax.add_patch(btn)
ax.text(4, 0.8, 'Connect', fontsize=13, fontweight='bold',
        ha='center', va='center', color='white')

plt.tight_layout()
plt.savefig(os.path.join(img_dir, '06-config-form.png'), dpi=150, bbox_inches='tight')
plt.close()
print("  Configuration form saved")

# ============================================================
# Image: Chapter 11 - Agent Progress (without emojis)
# ============================================================
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.set_xlim(0, 8)
ax.set_ylim(0, 6)
ax.axis('off')
ax.set_facecolor('#f8f9fa')
fig.patch.set_facecolor='#f8f9fa'

ax.text(4, 5.5, 'Agent Creation Progress', fontsize=16, fontweight='bold',
        ha='center', va='center', color='#2c3e50')

steps = [
    (4, 4.7, '1. Creating strategy...'),
    (4, 4.0, '2. Setting up cron job...'),
    (4, 3.3, '3. Connecting to moomoo...'),
    (4, 2.6, '4. Creating trade log...'),
    (4, 1.9, '5. Starting agent...'),
    (4, 1.0, 'Agent is LIVE!'),
]

for x, y, text in steps:
    if 'LIVE' in text:
        box = FancyBboxPatch((x-1.5, y-0.3), 3, 0.6,
                              boxstyle="round,pad=0.1",
                              facecolor='#e74c3c', edgecolor='white', linewidth=2)
        ax.add_patch(box)
        ax.text(x, y, text, fontsize=12, ha='center', va='center', color='white', fontweight='bold')
    else:
        # Checkmark box
        check_box = FancyBboxPatch((x-1.2, y-0.2), 0.5, 0.5,
                                    boxstyle="round,pad=0.05",
                                    facecolor='#27ae60', edgecolor='#1e8449', linewidth=2)
        ax.add_patch(check_box)
        ax.text(x-0.95, y+0.05, 'OK', fontsize=10, ha='center', va='center', 
                color='white', fontweight='bold')
        ax.text(x+0.5, y, text, fontsize=12, ha='left', va='center', 
                color='#2c3e50', fontweight='bold')

plt.tight_layout()
plt.savefig(os.path.join(img_dir, '11-agent-progress.png'), dpi=150, bbox_inches='tight')
plt.close()
print("  Agent progress (fixed) saved")

# ============================================================
# Image: Chapter 13 - Money Exchange
# ============================================================
fig, ax = plt.subplots(1, 1, figsize=(8, 4))
ax.set_xlim(0, 8)
ax.set_ylim(0, 4)
ax.axis('off')
ax.set_facecolor('#f8f9fa')
fig.patch.set_facecolor('#f8f9fa')

ax.text(4, 3.5, 'Trade Result', fontsize=16, fontweight='bold',
        ha='center', va='center', color='#2c3e50')

# Left: BUY
box_buy = FancyBboxPatch((0.3, 0.8), 2.5, 2.0,
                          boxstyle="round,pad=0.2",
                          facecolor='#e74c3c', edgecolor='#c0392b', linewidth=2)
ax.add_patch(box_buy)
ax.text(1.55, 2.3, 'BUY', fontsize=14, fontweight='bold',
        ha='center', va='center', color='white')
ax.text(1.55, 1.5, '10 x $142.50', fontsize=10, ha='center', va='center', color='white')
ax.text(1.55, 1.0, '-$1,425.00', fontsize=11, fontweight='bold',
        ha='center', va='center', color='#fadbd8')

# Arrow
ax.annotate('', xy=(4.0, 1.8), xytext=(3.0, 1.8),
            arrowprops=dict(arrowstyle='->', color='#34495e', lw=3))

# Right: SELL
box_sell = FancyBboxPatch((5.2, 0.8), 2.5, 2.0,
                           boxstyle="round,pad=0.2",
                           facecolor='#27ae60', edgecolor='#1e8449', linewidth=2)
ax.add_patch(box_sell)
ax.text(6.45, 2.3, 'SELL', fontsize=14, fontweight='bold',
        ha='center', va='center', color='white')
ax.text(6.45, 1.5, '10 x $145.20', fontsize=10, ha='center', va='center', color='white')
ax.text(6.45, 1.0, '+$1,452.00', fontsize=11, fontweight='bold',
        ha='center', va='center', color='#d5f5e3')

# Profit box
box_pnl = FancyBboxPatch((2.5, 0.1), 3, 0.5,
                          boxstyle="round,pad=0.1",
                          facecolor='#27ae60', edgecolor='#1e8449', linewidth=2)
ax.add_patch(box_pnl)
ax.text(4, 0.35, 'PROFIT: +$27.00', fontsize=13, fontweight='bold',
        ha='center', va='center', color='white')

plt.tight_layout()
plt.savefig(os.path.join(img_dir, '13-money-exchange.png'), dpi=150, bbox_inches='tight')
plt.close()
print("  Money exchange saved")

# ============================================================
# Image: Chapter 16 - Go Live Rules Shield
# ============================================================
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.set_xlim(0, 8)
ax.set_ylim(0, 6)
ax.axis('off')
ax.set_facecolor('#f8f9fa')
fig.patch.set_facecolor='#f8f9fa'

ax.text(4, 5.5, 'GO LIVE RULES', fontsize=16, fontweight='bold',
        ha='center', va='center', color='#c0392b')

rules = [
    '1. Start Small',
    '2. One Agent Only',
    '3. Set Stop-Loss',
    '4. Monitor Closely',
    '5. Do Not Panic',
]

for i, rule in enumerate(rules):
    y = 4.6 - i * 0.7
    box = FancyBboxPatch((1.0, y-0.2), 6, 0.45,
                          boxstyle="round,pad=0.05",
                          facecolor='#fff3cd', edgecolor='#f39c12', linewidth=1)
    ax.add_patch(box)
    ax.text(4, y+0.02, rule, fontsize=11, ha='center', va='center',
            color='#2c3e50', fontweight='bold')

plt.tight_layout()
plt.savefig(os.path.join(img_dir, '16-go-live-rules.png'), dpi=150, bbox_inches='tight')
plt.close()
print("  Go Live rules saved")

# ============================================================
# Image: Chapter 19 - Maintenance Calendar
# ============================================================
fig, ax = plt.subplots(1, 1, figsize=(12, 5))
ax.set_xlim(0, 12)
ax.set_ylim(0, 5)
ax.axis('off')
ax.set_facecolor('#f8f9fa')
fig.patch.set_facecolor('#f8f9fa')

ax.text(6, 4.5, 'Maintenance Schedule', fontsize=16, fontweight='bold',
        ha='center', va='center', color='#2c3e50')

# Daily
box_daily = FancyBboxPatch((0.3, 0.5), 3.5, 3.5,
                            boxstyle="round,pad=0.15",
                            facecolor='#3498db', edgecolor='#2980b9', linewidth=2)
ax.add_patch(box_daily)
ax.text(2, 3.5, 'DAILY', fontsize=12, fontweight='bold',
        ha='center', va='center', color='white')
ax.text(2, 2.5, '2 minutes', fontsize=10, ha='center', va='center', color='white')
ax.text(2, 1.8, '- Check agents', fontsize=9, ha='center', va='center', color='white')
ax.text(2, 1.3, '- Check PnL', fontsize=9, ha='center', va='center', color='white')

# Weekly
box_weekly = FancyBboxPatch((4.3, 0.5), 3.5, 3.5,
                             boxstyle="round,pad=0.15",
                             facecolor='#27ae60', edgecolor='#1e8449', linewidth=2)
ax.add_patch(box_weekly)
ax.text(6, 3.5, 'WEEKLY', fontsize=12, fontweight='bold',
        ha='center', va='center', color='white')
ax.text(6, 2.5, '10 minutes', fontsize=10, ha='center', va='center', color='white')
ax.text(6, 1.8, '- Review trades', fontsize=9, ha='center', va='center', color='white')
ax.text(6, 1.3, '- Win rate', fontsize=9, ha='center', va='center', color='white')

# Monthly
box_monthly = FancyBboxPatch((8.3, 0.5), 3.5, 3.5,
                              boxstyle="round,pad=0.15",
                              facecolor='#f39c12', edgecolor='#e67e22', linewidth=2)
ax.add_patch(box_monthly)
ax.text(10, 3.5, 'MONTHLY', fontsize=12, fontweight='bold',
        ha='center', va='center', color='white')
ax.text(10, 2.5, '30 minutes', fontsize=10, ha='center', va='center', color='white')
ax.text(10, 1.8, '- Update software', fontsize=9, ha='center', va='center', color='white')
ax.text(10, 1.3, '- Backup configs', fontsize=9, ha='center', va='center', color='white')

plt.tight_layout()
plt.savefig(os.path.join(img_dir, '19-maintenance-calendar.png'), dpi=150, bbox_inches='tight')
plt.close()
print("  Maintenance calendar saved")

print("\nAll mockups generated!")
