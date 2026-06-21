
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np
import os

img_dir = r"C:\Users\Nidzam\ebook-auto-trading\images"

# ============================================================
# Fix: Cron timeline without emojis
# ============================================================
fig, ax = plt.subplots(1, 1, figsize=(12, 4))
ax.set_xlim(0, 12)
ax.set_ylim(0, 4)
ax.axis('off')
ax.set_facecolor('#f8f9fa')
fig.patch.set_facecolor('#f8f9fa')

ax.text(6, 3.6, 'Cron Job Schedule (Every 30 Minutes)', fontsize=16, fontweight='bold',
        ha='center', va='center', color='#2c3e50')

# Timeline
ax.plot([0.5, 11.5], [2, 2], color='#34495e', linewidth=2)

# Time markers
times = ['9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00']
x_positions = np.linspace(1, 11, len(times))

for i, (t, x) in enumerate(zip(times, x_positions)):
    ax.plot([x, x], [1.8, 2.2], color='#34495e', linewidth=2)
    ax.text(x, 2.5, t, fontsize=9, ha='center', va='center', color='#2c3e50')
    
    # Check/Wait indicators
    if i % 2 == 0:
        circle = plt.Circle((x, 1.3), 0.3, color='#27ae60', alpha=0.8)
        ax.add_patch(circle)
        ax.text(x, 1.3, '[CHECK]', fontsize=7, ha='center', va='center', 
                color='white', fontweight='bold')
    else:
        circle = plt.Circle((x, 1.3), 0.3, color='#f39c12', alpha=0.8)
        ax.add_patch(circle)
        ax.text(x, 1.3, '[WAIT]', fontsize=7, ha='center', va='center',
                color='white', fontweight='bold')
    ax.text(x, 0.7, 'Check market' if i % 2 == 0 else 'Wait 30 min', 
            fontsize=8, ha='center', va='center', color='#27ae60' if i % 2 == 0 else '#f39c12')

plt.tight_layout()
plt.savefig(os.path.join(img_dir, '09-cron-timeline.png'), dpi=150, bbox_inches='tight')
plt.close()
print("  Fixed: Cron timeline")

# ============================================================
# Image: Chapter 2 - Safety Scale
# ============================================================
fig, ax = plt.subplots(1, 1, figsize=(8, 5))
ax.set_xlim(0, 8)
ax.set_ylim(0, 5)
ax.axis('off')
ax.set_facecolor('#f8f9fa')
fig.patch.set_facecolor('#f8f9fa')

ax.text(4, 4.5, 'Safety First!', fontsize=18, fontweight='bold',
        ha='center', va='center', color='#27ae60')

# Balance scale
# Pivot
ax.plot([4, 4], [1.5, 3.5], color='#34495e', linewidth=3)
ax.plot([3.5, 4.5], [3.5, 3.5], color='#34495e', linewidth=3)

# Left side (RISK - lighter, higher)
ax.plot([4, 2.5], [3.5, 2.8], color='#34495e', linewidth=2)
box_risk = FancyBboxPatch((1.8, 2.2), 1.5, 0.6,
                           boxstyle="round,pad=0.1",
                           facecolor='#e74c3c', edgecolor='#c0392b', linewidth=2)
ax.add_patch(box_risk)
ax.text(2.55, 2.5, 'RISK', fontsize=12, fontweight='bold',
        ha='center', va='center', color='white')

# Right side (SAFETY - heavier, lower)
ax.plot([4, 5.5], [3.5, 2.0], color='#34495e', linewidth=2)
box_safe = FancyBboxPatch((4.8, 1.4), 1.5, 0.6,
                           boxstyle="round,pad=0.1",
                           facecolor='#27ae60', edgecolor='#1e8449', linewidth=2)
ax.add_patch(box_safe)
ax.text(5.55, 1.7, 'SAFETY', fontsize=12, fontweight='bold',
        ha='center', va='center', color='white')

# Arrow showing safety wins
ax.annotate('', xy=(5.55, 1.2), xytext=(5.55, 0.8),
            arrowprops=dict(arrowstyle='->', color='#27ae60', lw=3))
ax.text(5.55, 0.5, 'Always choose safety!', fontsize=11, fontweight='bold',
        ha='center', va='center', color='#27ae60')

plt.tight_layout()
plt.savefig(os.path.join(img_dir, '02-safety-scale.png'), dpi=150, bbox_inches='tight')
plt.close()
print("  Safety scale saved")

# ============================================================
# Image: Chapter 6 - Connection Diagram (Puzzle pieces)
# ============================================================
fig, ax = plt.subplots(1, 1, figsize=(10, 4))
ax.set_xlim(0, 10)
ax.set_ylim(0, 4)
ax.axis('off')
ax.set_facecolor('#f8f9fa')
fig.patch.set_facecolor('#f8f9fa')

ax.text(5, 3.5, 'Connecting Hermes to moomoo', fontsize=16, fontweight='bold',
        ha='center', va='center', color='#2c3e50')

# Hermes box
box_h = FancyBboxPatch((0.3, 1.0), 2.5, 2.0,
                        boxstyle="round,pad=0.2",
                        facecolor='#2ecc71', edgecolor='#27ae60', linewidth=2)
ax.add_patch(box_h)
ax.text(1.55, 2.3, 'Hermes', fontsize=14, fontweight='bold',
        ha='center', va='center', color='white')
ax.text(1.55, 1.6, 'AI Assistant', fontsize=10, ha='center', va='center', color='white')

# OpenD bridge
box_o = FancyBboxPatch((3.8, 1.5), 2.4, 1.0,
                        boxstyle="round,pad=0.1",
                        facecolor='#9b59b6', edgecolor='#8e44ad', linewidth=2)
ax.add_patch(box_o)
ax.text(5, 2.0, 'OpenD (Bridge)', fontsize=11, fontweight='bold',
        ha='center', va='center', color='white')

# moomoo box
box_m = FancyBboxPatch((7.2, 1.0), 2.5, 2.0,
                        boxstyle="round,pad=0.2",
                        facecolor='#e74c3c', edgecolor='#c0392b', linewidth=2)
ax.add_patch(box_m)
ax.text(8.45, 2.3, 'moomoo', fontsize=14, fontweight='bold',
        ha='center', va='center', color='white')
ax.text(8.45, 1.6, 'Trading App', fontsize=10, ha='center', va='center', color='white')

# Arrows
ax.annotate('', xy=(3.7, 2.0), xytext=(3.0, 2.0),
            arrowprops=dict(arrowstyle='->', color='#34495e', lw=2))
ax.annotate('', xy=(7.0, 2.0), xytext=(6.4, 2.0),
            arrowprops=dict(arrowstyle='->', color='#34495e', lw=2))

plt.tight_layout()
plt.savefig(os.path.join(img_dir, '06-connection-diagram.png'), dpi=150, bbox_inches='tight')
plt.close()
print("  Connection diagram saved")

# ============================================================
# Image: Chapter 7 - Waiter/Kitchen Analogy
# ============================================================
fig, ax = plt.subplots(1, 1, figsize=(12, 5))
ax.set_xlim(0, 12)
ax.set_ylim(0, 5)
ax.axis('off')
ax.set_facecolor('#f8f9fa')
fig.patch.set_facecolor('#f8f9fa')

ax.text(6, 4.5, 'The Restaurant Analogy', fontsize=16, fontweight='bold',
        ha='center', va='center', color='#2c3e50')

# Customer (You)
box_c = FancyBboxPatch((0.3, 1.0), 2.5, 2.5,
                        boxstyle="round,pad=0.2",
                        facecolor='#3498db', edgecolor='#2980b9', linewidth=2)
ax.add_patch(box_c)
ax.text(1.55, 2.8, 'YOU', fontsize=14, fontweight='bold',
        ha='center', va='center', color='white')
ax.text(1.55, 2.0, '"I want NVDA"', fontsize=10, ha='center', 
        va='center', color='white', style='italic')

# Waiter (Hermes)
box_w = FancyBboxPatch((4.7, 1.0), 2.5, 2.5,
                        boxstyle="round,pad=0.2",
                        facecolor='#2ecc71', edgecolor='#27ae60', linewidth=2)
ax.add_patch(box_w)
ax.text(6, 2.8, 'HERMES', fontsize=14, fontweight='bold',
        ha='center', va='center', color='white')
ax.text(6, 2.0, '(waiter)', fontsize=10, ha='center',
        va='center', color='white', style='italic')

# Chef (moomoo)
box_k = FancyBboxPatch((9.0, 1.0), 2.7, 2.5,
                        boxstyle="round,pad=0.2",
                        facecolor='#e74c3c', edgecolor='#c0392b', linewidth=2)
ax.add_patch(box_k)
ax.text(10.35, 2.8, 'MOOMOO', fontsize=14, fontweight='bold',
        ha='center', va='center', color='white')
ax.text(10.35, 2.0, '(chef)', fontsize=10, ha='center',
        va='center', color='white', style='italic')

# Flow arrows
ax.annotate('', xy=(4.5, 2.25), xytext=(3.0, 2.25),
            arrowprops=dict(arrowstyle='->', color='#34495e', lw=2))
ax.text(3.75, 2.6, 'Order', fontsize=9, ha='center', va='center', color='#34495e')

ax.annotate('', xy=(8.8, 2.25), xytext=(7.4, 2.25),
            arrowprops=dict(arrowstyle='->', color='#34495e', lw=2))
ax.text(8.1, 2.6, 'Cook', fontsize=9, ha='center', va='center', color='#34495e')

# Return arrow
ax.annotate('', xy=(3.0, 1.5), xytext=(8.8, 1.5),
            arrowprops=dict(arrowstyle='->', color='#27ae60', lw=2, linestyle='--'))
ax.text(6, 1.2, 'Done! Trade executed.', fontsize=10, ha='center', va='center',
        color='#27ae60', fontweight='bold')

plt.tight_layout()
plt.savefig(os.path.join(img_dir, '07-restaurant-analogy.png'), dpi=150, bbox_inches='tight')
plt.close()
print("  Restaurant analogy saved")

# ============================================================
# Image: Chapter 10 - Planning Worksheet
# ============================================================
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.set_xlim(0, 8)
ax.set_ylim(0, 6)
ax.axis('off')
ax.set_facecolor('#f8f9fa')
fig.patch.set_facecolor('#f8f9fa')

ax.text(4, 5.5, 'My First Trading Agent Plan', fontsize=16, fontweight='bold',
        ha='center', va='center', color='#2c3e50')

plan_items = [
    ('Stock:', 'NVDA (NVIDIA)'),
    ('Strategy:', 'RSI (Buy < 30, Sell > 70)'),
    ('Virtual Capital:', '$100,000'),
    ('Environment:', 'SIMULATE'),
    ('Schedule:', 'Every 30 min (US market hours)'),
]

for i, (label, value) in enumerate(plan_items):
    y = 4.6 - i * 0.7
    ax.text(1.5, y, label, fontsize=12, ha='right', va='center',
            color='#34495e', fontweight='bold')
    
    box = FancyBboxPatch((1.8, y-0.25), 5, 0.5,
                          boxstyle="round,pad=0.05",
                          facecolor='white', edgecolor='#bdc3c7', linewidth=1)
    ax.add_patch(box)
    ax.text(2.0, y, value, fontsize=12, ha='left', va='center', color='#2c3e50')

plt.tight_layout()
plt.savefig(os.path.join(img_dir, '10-planning-worksheet.png'), dpi=150, bbox_inches='tight')
plt.close()
print("  Planning worksheet saved")

# ============================================================
# Image: Chapter 12 - Recipe Cards
# ============================================================
fig, ax = plt.subplots(1, 1, figsize=(12, 5))
ax.set_xlim(0, 12)
ax.set_ylim(0, 5)
ax.axis('off')
ax.set_facecolor('#f8f9fa')
fig.patch.set_facecolor('#f8f9fa')

ax.text(6, 4.5, 'Strategy Recipe Cards', fontsize=16, fontweight='bold',
        ha='center', va='center', color='#2c3e50')

recipes = [
    ('RSI Recipe', 'Buy when RSI < 30\nSell when RSI > 70', '#3498db'),
    ('Bollinger Recipe', 'Buy: touches lower band\nSell: touches upper band', '#e74c3c'),
    ('EMA Recipe', 'Buy: crosses above 20-EMA\nSell: crosses below 20-EMA', '#27ae60'),
]

for i, (title, content, color) in enumerate(recipes):
    x = 0.3 + i * 3.9
    box = FancyBboxPatch((x, 0.5), 3.5, 3.5,
                          boxstyle="round,pad=0.15",
                          facecolor='white', edgecolor=color, linewidth=2)
    ax.add_patch(box)
    
    # Title bar
    title_box = FancyBboxPatch((x, 3.0), 3.5, 1.0,
                                boxstyle="round,pad=0.05",
                                facecolor=color, edgecolor='none', alpha=0.9)
    ax.add_patch(title_box)
    ax.text(x + 1.75, 3.5, title, fontsize=12, fontweight='bold',
            ha='center', va='center', color='white')
    
    ax.text(x + 1.75, 2.0, content, fontsize=10, ha='center', va='center',
            color='#2c3e50', linespacing=1.5)

plt.tight_layout()
plt.savefig(os.path.join(img_dir, '12-recipe-cards.png'), dpi=150, bbox_inches='tight')
plt.close()
print("  Recipe cards saved")

# ============================================================
# Image: Chapter 14 - Multiple Agents
# ============================================================
fig, ax = plt.subplots(1, 1, figsize=(12, 5))
ax.set_xlim(0, 12)
ax.set_ylim(0, 5)
ax.axis('off')
ax.set_facecolor('#f8f9fa')
fig.patch.set_facecolor('#f8f9fa')

ax.text(6, 4.5, 'Multiple Trading Agents', fontsize=16, fontweight='bold',
        ha='center', va='center', color='#2c3e50')

agents = [
    ('NVDA-RSI', '+340', '#27ae60'),
    ('AAPL-BB', '+85', '#3498db'),
    ('TSLA-EMA', '-45', '#e74c3c'),
]

for i, (name, pnl, color) in enumerate(agents):
    x = 0.5 + i * 3.9
    box = FancyBboxPatch((x, 0.8), 3.5, 3.0,
                          boxstyle="round,pad=0.2",
                          facecolor=color, edgecolor='white', linewidth=2, alpha=0.9)
    ax.add_patch(box)
    ax.text(x + 1.75, 3.3, name, fontsize=13, fontweight='bold',
            ha='center', va='center', color='white')
    ax.text(x + 1.75, 2.3, 'PnL:', fontsize=11, ha='center', va='center', color='white')
    ax.text(x + 1.75, 1.6, f'${pnl}', fontsize=18, fontweight='bold',
            ha='center', va='center', color='white')

plt.tight_layout()
plt.savefig(os.path.join(img_dir, '14-multiple-agents.png'), dpi=150, bbox_inches='tight')
plt.close()
print("  Multiple agents saved")

# ============================================================
# Image: Chapter 17 - Multi-Indicator
# ============================================================
fig, ax = plt.subplots(1, 1, figsize=(8, 5))
ax.set_xlim(0, 8)
ax.set_ylim(0, 5)
ax.axis('off')
ax.set_facecolor('#f8f9fa')
fig.patch.set_facecolor('#f8f9fa')

ax.text(4, 4.5, 'Multi-Indicator = Strong Signal', fontsize=14, fontweight='bold',
        ha='center', va='center', color='#2c3e50')

indicators = [
    ('RSI < 30', '#27ae60'),
    ('Volume > 1.5x', '#3498db'),
    ('Price > 20-EMA', '#f39c12'),
]

# Three traffic lights
for i, (label, color) in enumerate(indicators):
    x = 1.5 + i * 2.2
    circle = plt.Circle((x, 2.8), 0.6, color=color, alpha=0.9)
    ax.add_patch(circle)
    ax.text(x, 2.8, 'ON', fontsize=12, fontweight='bold',
            ha='center', va='center', color='white')
    ax.text(x, 1.8, label, fontsize=10, ha='center', va='center',
            color='#2c3e50', fontweight='bold')

# = STRONG SIGNAL
ax.text(4, 0.8, '= STRONG SIGNAL to BUY!', fontsize=14, fontweight='bold',
        ha='center', va='center', color='#27ae60',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#d5f5e3', edgecolor='#27ae60'))

plt.tight_layout()
plt.savefig(os.path.join(img_dir, '17-multi-indicator.png'), dpi=150, bbox_inches='tight')
plt.close()
print("  Multi-indicator saved")

# ============================================================
# Image: Chapter 20 - Security Shield
# ============================================================
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.set_xlim(0, 8)
ax.set_ylim(0, 6)
ax.axis('off')
ax.set_facecolor('#f8f9fa')
fig.patch.set_facecolor('#f8f9fa')

ax.text(4, 5.5, 'Security Checklist', fontsize=16, fontweight='bold',
        ha='center', va='center', color='#2c3e50')

checklist = [
    'Protect credentials',
    'Hide API keys',
    'Know the kill switch',
    'Backup configs',
    'Secure computer',
]

for i, item in enumerate(checklist):
    y = 4.6 - i * 0.7
    # Checkbox
    box = FancyBboxPatch((1.0, y-0.2), 0.5, 0.5,
                          boxstyle="round,pad=0.05",
                          facecolor='#27ae60', edgecolor='#1e8449', linewidth=2)
    ax.add_patch(box)
    ax.text(1.25, y+0.05, 'v', fontsize=14, fontweight='bold',
            ha='center', va='center', color='white')
    ax.text(2.0, y+0.05, item, fontsize=12, ha='left', va='center',
            color='#2c3e50', fontweight='bold')

plt.tight_layout()
plt.savefig(os.path.join(img_dir, '20-security-checklist.png'), dpi=150, bbox_inches='tight')
plt.close()
print("  Security checklist saved")

print("\nAll additional diagrams generated!")
