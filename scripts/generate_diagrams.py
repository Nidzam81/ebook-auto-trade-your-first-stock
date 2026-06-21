
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
import os

img_dir = r"C:\Users\Nidzam\ebook-auto-trading\images"
os.makedirs(img_dir, exist_ok=True)

# Set style
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.family'] = 'Segoe UI, Arial, sans-serif'
plt.rcParams['font.size'] = 11

print("Generating ebook diagrams...")

# ============================================================
# Image 1: Chapter 1 - "You + Hermes + moomoo" diagram
# ============================================================
fig, ax = plt.subplots(1, 1, figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')
ax.set_facecolor('#f8f9fa')
fig.patch.set_facecolor('#f8f9fa')

# Title
ax.text(5, 5.5, 'How Automated Trading Works', fontsize=18, fontweight='bold',
        ha='center', va='center', color='#2c3e50')

# Three boxes
# You
box_you = FancyBboxPatch((0.5, 1.5), 2.5, 2.5, 
                          boxstyle="round,pad=0.2", 
                          facecolor='#3498db', edgecolor='#2980b9', linewidth=2)
ax.add_patch(box_you)
ax.text(1.75, 3.3, 'YOU', fontsize=14, fontweight='bold', 
        ha='center', va='center', color='white')
ax.text(1.75, 2.5, 'Type:\n"Buy NVDA"', fontsize=10, 
        ha='center', va='center', color='white', style='italic')

# Hermes
box_hermes = FancyBboxPatch((3.7, 1.5), 2.5, 2.5,
                             boxstyle="round,pad=0.2",
                             facecolor='#2ecc71', edgecolor='#27ae60', linewidth=2)
ax.add_patch(box_hermes)
ax.text(5, 3.3, 'HERMES', fontsize=14, fontweight='bold',
        ha='center', va='center', color='white')
ax.text(5, 2.5, 'Checks RSI\nPlaces order', fontsize=10,
        ha='center', va='center', color='white', style='italic')

# moomoo
box_moomoo = FancyBboxPatch((6.9, 1.5), 2.5, 2.5,
                             boxstyle="round,pad=0.2",
                             facecolor='#e74c3c', edgecolor='#c0392b', linewidth=2)
ax.add_patch(box_moomoo)
ax.text(8.15, 3.3, 'MOOMOO', fontsize=14, fontweight='bold',
        ha='center', va='center', color='white')
ax.text(8.15, 2.5, 'Executes trade\nRecords PnL', fontsize=10,
        ha='center', va='center', color='white', style='italic')

# Arrows
ax.annotate('', xy=(3.5, 2.75), xytext=(3.2, 2.75),
            arrowprops=dict(arrowstyle='->', color='#34495e', lw=2))
ax.annotate('', xy=(6.6, 2.75), xytext=(6.4, 2.75),
            arrowprops=dict(arrowstyle='->', color='#34495e', lw=2))

# OpenD bridge
ax.plot([5, 5], [1.2, 1.5], color='#9b59b6', linewidth=3, linestyle='--')
ax.text(5, 0.8, 'OpenD (Bridge)', fontsize=10, ha='center', va='center',
        color='#9b59b6', fontweight='bold')

plt.tight_layout()
plt.savefig(os.path.join(img_dir, '01-you-hermes-moomoo.png'), dpi=150, bbox_inches='tight')
plt.close()
print("  1. You + Hermes + moomoo diagram saved")

# ============================================================
# Image 2: Chapter 1 - Flowchart "Your Journey"
# ============================================================
fig, ax = plt.subplots(1, 1, figsize=(8, 10))
ax.set_xlim(0, 8)
ax.set_ylim(0, 10)
ax.axis('off')
ax.set_facecolor('#f8f9fa')
fig.patch.set_facecolor('#f8f9fa')

ax.text(4, 9.5, 'Your Journey', fontsize=18, fontweight='bold',
        ha='center', va='center', color='#2c3e50')

steps = [
    (4, 8.5, '1. You are here', '#3498db'),
    (4, 7.2, '2. Read this book', '#3498db'),
    (4, 5.9, '3. Set up your system', '#2ecc71'),
    (4, 4.6, '4. Practice with SIMULATE', '#f39c12'),
    (4, 3.3, '5. Trade with REAL money', '#e74c3c'),
]

for x, y, text, color in steps:
    box = FancyBboxPatch((x-1.5, y-0.4), 3, 0.8,
                          boxstyle="round,pad=0.1",
                          facecolor=color, edgecolor='white', linewidth=2, alpha=0.9)
    ax.add_patch(box)
    ax.text(x, y, text, fontsize=12, fontweight='bold',
            ha='center', va='center', color='white')

# Arrows between steps
for i in range(len(steps)-1):
    y1 = steps[i][1] - 0.4
    y2 = steps[i+1][1] + 0.4
    ax.annotate('', xy=(4, y2), xytext=(4, y1),
                arrowprops=dict(arrowstyle='->', color='#7f8c8d', lw=2))

plt.tight_layout()
plt.savefig(os.path.join(img_dir, '01-journey-flowchart.png'), dpi=150, bbox_inches='tight')
plt.close()
print("  2. Journey flowchart saved")

# ============================================================
# Image 3: Chapter 8 - RSI Gauge
# ============================================================
fig, ax = plt.subplots(1, 1, figsize=(8, 5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 5)
ax.axis('off')
ax.set_facecolor('#f8f9fa')
fig.patch.set_facecolor('#f8f9fa')

ax.text(5, 4.5, 'RSI Indicator', fontsize=18, fontweight='bold',
        ha='center', va='center', color='#2c3e50')

# Gauge background
gauge = mpatches.Wedge((5, 1.5), 2.5, 0, 180, facecolor='#ecf0f1', edgecolor='#bdc3c7', linewidth=2)
ax.add_patch(gauge)

# Colored zones
red_zone = mpatches.Wedge((5, 1.5), 2.5, 0, 45, facecolor='#e74c3c', alpha=0.7)
ax.add_patch(red_zone)
green_zone = mpatches.Wedge((5, 1.5), 2.5, 45, 135, facecolor='#f39c12', alpha=0.7)
ax.add_patch(green_zone)
blue_zone = mpatches.Wedge((5, 1.5), 2.5, 135, 180, facecolor='#2ecc71', alpha=0.7)
ax.add_patch(blue_zone)

# Labels
ax.text(2.0, 0.5, 'BELOW 30\nBUY (Cheap!)', fontsize=11, fontweight='bold',
        ha='center', va='center', color='#27ae60')
ax.text(5, 0.3, '30-70 = WAIT', fontsize=11, fontweight='bold',
        ha='center', va='center', color='#f39c12')
ax.text(8.0, 0.5, 'ABOVE 70\nSELL (Expensive!)', fontsize=11, fontweight='bold',
        ha='center', va='center', color='#c0392b')

# Needle (pointing to 28 - buy zone)
needle_angle = 180 - (28/100 * 180)  # RSI 28
needle_x = 5 + 2.0 * np.cos(np.radians(needle_angle))
needle_y = 1.5 + 2.0 * np.sin(np.radians(needle_angle))
ax.plot([5, needle_x], [1.5, needle_y], color='#2c3e50', linewidth=3)
ax.plot(5, 1.5, 'o', color='#2c3e50', markersize=8)

ax.text(5, 3.8, 'Current RSI: 28 → BUY SIGNAL!', fontsize=14, fontweight='bold',
        ha='center', va='center', color='#27ae60',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#d5f5e3', edgecolor='#27ae60'))

plt.tight_layout()
plt.savefig(os.path.join(img_dir, '08-rsi-gauge.png'), dpi=150, bbox_inches='tight')
plt.close()
print("  3. RSI gauge saved")

# ============================================================
# Image 4: Chapter 8 - EMA Crossover Chart
# ============================================================
fig, ax = plt.subplots(1, 1, figsize=(10, 5))
ax.set_facecolor('#f8f9fa')
fig.patch.set_facecolor('#f8f9fa')

# Generate sample data
np.random.seed(42)
days = np.arange(1, 51)
price = 100 + np.cumsum(np.random.randn(50) * 1.5)
ema_20 = np.convolve(price, np.ones(20)/20, mode='valid')
ema_days = days[19:]

ax.plot(days, price, color='#3498db', linewidth=1.5, alpha=0.8, label='Stock Price')
ax.plot(ema_days, ema_20, color='#e74c3c', linewidth=2, label='20-day EMA')

# Find crossover points
buy_signals = []
sell_signals = []
for i in range(1, len(ema_20)):
    if price[19+i-1] < ema_20[i-1] and price[19+i] > ema_20[i]:
        buy_signals.append((days[19+i], price[19+i]))
    elif price[19+i-1] > ema_20[i-1] and price[19+i] < ema_20[i]:
        sell_signals.append((days[19+i], price[19+i]))

# Plot signals
if buy_signals:
    bx, by = zip(*buy_signals)
    ax.scatter(bx, by, color='#27ae60', s=100, marker='^', zorder=5, label='BUY signal', edgecolors='black')
if sell_signals:
    sx, sy = zip(*sell_signals)
    ax.scatter(sx, sy, color='#e74c3c', s=100, marker='v', zorder=5, label='SELL signal', edgecolors='black')

ax.set_title('EMA Crossover Strategy', fontsize=16, fontweight='bold', color='#2c3e50')
ax.set_xlabel('Trading Days', fontsize=12)
ax.set_ylabel('Price ($)', fontsize=12)
ax.legend(loc='upper left', fontsize=10)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(img_dir, '08-ema-crossover.png'), dpi=150, bbox_inches='tight')
plt.close()
print("  4. EMA crossover chart saved")

# ============================================================
# Image 5: Chapter 8 - Bollinger Bands
# ============================================================
fig, ax = plt.subplots(1, 1, figsize=(10, 5))
ax.set_facecolor('#f8f9fa')
fig.patch.set_facecolor('#f8f9fa')

np.random.seed(123)
days = np.arange(1, 51)
price = 150 + np.cumsum(np.random.randn(50) * 2)
sma = np.convolve(price, np.ones(20)/20, mode='valid')
sma_days = days[19:]
std = np.array([np.std(price[i-20:i]) for i in range(20, 51)])
upper = sma + 2 * std
lower = sma - 2 * std

ax.fill_between(sma_days, lower, upper, alpha=0.2, color='#3498db', label='Bollinger Bands')
ax.plot(sma_days, upper, color='#e74c3c', linewidth=1, linestyle='--')
ax.plot(sma_days, sma, color='#f39c12', linewidth=2, label='20-day SMA (Middle)')
ax.plot(sma_days, lower, color='#27ae60', linewidth=1, linestyle='--')
ax.plot(days, price, color='#2c3e50', linewidth=1.5, alpha=0.8, label='Stock Price')

# Buy/sell annotations
ax.annotate('BUY\n(touches lower band)', xy=(sma_days[5], lower[5]),
            xytext=(sma_days[5]+3, lower[5]-5),
            fontsize=9, fontweight='bold', color='#27ae60',
            arrowprops=dict(arrowstyle='->', color='#27ae60'),
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#d5f5e3', edgecolor='#27ae60'))

ax.annotate('SELL\n(touches upper band)', xy=(sma_days[30], upper[30]),
            xytext=(sma_days[30]+3, upper[30]+5),
            fontsize=9, fontweight='bold', color='#c0392b',
            arrowprops=dict(arrowstyle='->', color='#c0392b'),
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#fadbd8', edgecolor='#c0392b'))

ax.set_title('Bollinger Bands Strategy', fontsize=16, fontweight='bold', color='#2c3e50')
ax.set_xlabel('Trading Days', fontsize=12)
ax.set_ylabel('Price ($)', fontsize=12)
ax.legend(loc='upper left', fontsize=9)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(img_dir, '08-bollinger-bands.png'), dpi=150, bbox_inches='tight')
plt.close()
print("  5. Bollinger Bands chart saved")

# ============================================================
# Image 6: Chapter 9 - Cron Job Timeline
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
    
    # Eye icon (open = checking)
    color = '#27ae60' if i % 2 == 0 else '#f39c12'
    ax.plot(x, 1.3, 'o', color=color, markersize=12)
    ax.text(x, 1.3, '👁' if i % 2 == 0 else '💤', fontsize=12, ha='center', va='center')
    ax.text(x, 0.7, 'Check' if i % 2 == 0 else 'Wait', fontsize=8, ha='center', 
            va='center', color=color, fontweight='bold')

# Legend
ax.text(6, 0.2, '🔍 Check market → 💤 Wait 30 min → 🔍 Check again...', 
        fontsize=11, ha='center', va='center', color='#7f8c8d', style='italic')

plt.tight_layout()
plt.savefig(os.path.join(img_dir, '09-cron-timeline.png'), dpi=150, bbox_inches='tight')
plt.close()
print("  6. Cron job timeline saved")

# ============================================================
# Image 7: Chapter 11 - Agent Creation Progress
# ============================================================
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.set_xlim(0, 8)
ax.set_ylim(0, 6)
ax.axis('off')
ax.set_facecolor('#f8f9fa')
fig.patch.set_facecolor('#f8f9fa')

ax.text(4, 5.5, 'Agent Creation Progress', fontsize=16, fontweight='bold',
        ha='center', va='center', color='#2c3e50')

steps_progress = [
    (4, 4.7, '1. Creating strategy...', True, '#27ae60'),
    (4, 4.0, '2. Setting up cron job...', True, '#27ae60'),
    (4, 3.3, '3. Connecting to moomoo...', True, '#27ae60'),
    (4, 2.6, '4. Creating trade log...', True, '#27ae60'),
    (4, 1.9, '5. Starting agent...', True, '#27ae60'),
    (4, 1.0, 'Agent is LIVE!', False, '#e74c3c'),
]

for x, y, text, done, color in steps_progress:
    if done:
        ax.plot(x-1.2, y, 's', color='#27ae60', markersize=12)
        ax.text(x-1.2, y, '✓', fontsize=12, ha='center', va='center', color='white', fontweight='bold')
    else:
        box = FancyBboxPatch((x-1.5, y-0.3), 3, 0.6,
                              boxstyle="round,pad=0.1",
                              facecolor=color, edgecolor='white', linewidth=2)
        ax.add_patch(box)
    ax.text(x+0.5, y, text, fontsize=12, ha='left', va='center', 
            color='#2c3e50', fontweight='bold')

plt.tight_layout()
plt.savefig(os.path.join(img_dir, '11-agent-progress.png'), dpi=150, bbox_inches='tight')
plt.close()
print("  7. Agent creation progress saved")

# ============================================================
# Image 8: Chapter 13 - Trade Log Example
# ============================================================
fig, ax = plt.subplots(1, 1, figsize=(12, 4))
ax.set_facecolor('#f8f9fa')
fig.patch.set_facecolor('#f8f9fa')
ax.axis('off')

ax.text(6, 3.5, 'Trade Log Example', fontsize=16, fontweight='bold',
        ha='center', va='center', color='#2c3e50')

# Table data
columns = ['#', 'Time', 'Agent', 'Side', 'Qty', 'Price', 'Entry', 'PnL']
data = [
    ['1', '10:00 AM', 'NVDA-RSI', 'BUY', '10', '$142.50', '$142.50', '--'],
    ['2', '2:30 PM', 'NVDA-RSI', 'SELL', '10', '$145.20', '$142.50', '+$27.00'],
    ['3', '11:00 AM', 'NVDA-RSI', 'BUY', '10', '$143.00', '$143.00', '--'],
    ['4', '3:15 PM', 'NVDA-RSI', 'SELL', '10', '$141.50', '$143.00', '-$15.00'],
]

table = ax.table(cellText=data, colLabels=columns, loc='center',
                 cellLoc='center', bbox=[0.02, 0.02, 0.96, 0.75])

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 1.5)

# Style header
for j in range(len(columns)):
    table[0, j].set_facecolor('#34495e')
    table[0, j].set_text_props(color='white', fontweight='bold')

# Color PnL cells
for i in range(1, len(data)+1):
    pnl_cell = table[i, 7]
    pnl_text = data[i-1][7]
    if '+' in str(pnl_text):
        pnl_cell.set_facecolor('#d5f5e3')
        pnl_cell.set_text_props(color='#27ae60', fontweight='bold')
    elif '-' in str(pnl_text) and pnl_text != '--':
        pnl_cell.set_facecolor('#fadbd8')
        pnl_cell.set_text_props(color='#c0392b', fontweight='bold')

plt.tight_layout()
plt.savefig(os.path.join(img_dir, '13-trade-log.png'), dpi=150, bbox_inches='tight')
plt.close()
print("  8. Trade log example saved")

# ============================================================
# Image 9: Chapter 15 - Dashboard Layout
# ============================================================
fig, ax = plt.subplots(1, 1, figsize=(12, 7))
ax.set_xlim(0, 12)
ax.set_ylim(0, 7)
ax.axis('off')
ax.set_facecolor('#f8f9fa')
fig.patch.set_facecolor('#f8f9fa')

ax.text(6, 6.5, 'Trading Dashboard Layout', fontsize=16, fontweight='bold',
        ha='center', va='center', color='#2c3e50')

# Account balance box
box1 = FancyBboxPatch((0.3, 5.0), 11.4, 1.0,
                       boxstyle="round,pad=0.1",
                       facecolor='#3498db', edgecolor='#2980b9', linewidth=2)
ax.add_patch(box1)
ax.text(6, 5.5, 'Account Balance: $1,000,000 (SIMULATE)', fontsize=14, fontweight='bold',
        ha='center', va='center', color='white')

# Agent cards
agents = ['NVDA-RSI', 'AAPL-BB', 'TSLA-EMA']
colors = ['#2ecc71', '#f39c12', '#e74c3c']
for i, (agent, color) in enumerate(zip(agents, colors)):
    x = 0.3 + i * 3.9
    box = FancyBboxPatch((x, 3.2), 3.5, 1.6,
                          boxstyle="round,pad=0.1",
                          facecolor=color, edgecolor='white', linewidth=2)
    ax.add_patch(box)
    ax.text(x + 1.75, 4.3, agent, fontsize=12, fontweight='bold',
            ha='center', va='center', color='white')
    ax.text(x + 1.75, 3.7, 'PnL: +$340.00', fontsize=10,
            ha='center', va='center', color='white')

# Trade log box
box_trade = FancyBboxPatch((0.3, 0.5), 7.2, 2.3,
                            boxstyle="round,pad=0.1",
                            facecolor='white', edgecolor='#bdc3c7', linewidth=1)
ax.add_patch(box_trade)
ax.text(3.9, 2.5, 'Trade Log', fontsize=12, fontweight='bold',
        ha='center', va='center', color='#2c3e50')

# Performance chart box
box_chart = FancyBboxPatch((7.8, 0.5), 3.9, 2.3,
                            boxstyle="round,pad=0.1",
                            facecolor='white', edgecolor='#bdc3c7', linewidth=1)
ax.add_patch(box_chart)
ax.text(9.75, 2.5, 'Performance Chart', fontsize=12, fontweight='bold',
        ha='center', va='center', color='#2c3e50')
# Mini chart
x_chart = np.linspace(8.2, 11.3, 20)
y_chart = np.linspace(1.0, 1.8, 20) + np.random.randn(20) * 0.1
ax.plot(x_chart, y_chart, color='#27ae60', linewidth=2)

plt.tight_layout()
plt.savefig(os.path.join(img_dir, '15-dashboard-layout.png'), dpi=150, bbox_inches='tight')
plt.close()
print("  9. Dashboard layout saved")

# ============================================================
# Image 10: Chapter 16 - SIMULATE vs LIVE
# ============================================================
fig, ax = plt.subplots(1, 1, figsize=(10, 5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 5)
ax.axis('off')
ax.set_facecolor('#f8f9fa')
fig.patch.set_facecolor('#f8f9fa')

ax.text(5, 4.5, 'Choose Your Environment', fontsize=18, fontweight='bold',
        ha='center', va='center', color='#2c3e50')

# SIMULATE door (green)
box_sim = FancyBboxPatch((0.5, 0.5), 4, 3.5,
                          boxstyle="round,pad=0.2",
                          facecolor='#27ae60', edgecolor='#1e8449', linewidth=3, alpha=0.9)
ax.add_patch(box_sim)
ax.text(2.5, 3.5, 'SIMULATE', fontsize=16, fontweight='bold',
        ha='center', va='center', color='white')
ax.text(2.5, 2.5, 'Practice Mode', fontsize=12, ha='center', va='center', color='white')
ax.text(2.5, 1.8, 'Fake money', fontsize=10, ha='center', va='center', color='#d5f5e3')
ax.text(2.5, 1.3, 'ZERO risk', fontsize=10, ha='center', va='center', color='#d5f5e3', fontweight='bold')

# LIVE door (red)
box_live = FancyBboxPatch((5.5, 0.5), 4, 3.5,
                           boxstyle="round,pad=0.2",
                           facecolor='#e74c3c', edgecolor='#c0392b', linewidth=3, alpha=0.9)
ax.add_patch(box_live)
ax.text(7.5, 3.5, 'LIVE', fontsize=16, fontweight='bold',
        ha='center', va='center', color='white')
ax.text(7.5, 2.5, 'Real Money', fontsize=12, ha='center', va='center', color='white')
ax.text(7.5, 1.8, 'Real trades', fontsize=10, ha='center', va='center', color='#fadbd8')
ax.text(7.5, 1.3, 'REAL risk!', fontsize=10, ha='center', va='center', color='#fadbd8', fontweight='bold')

# Arrow pointing to SIMULATE
ax.annotate('START HERE!', xy=(2.5, 4.0), xytext=(5, 4.3),
            fontsize=14, fontweight='bold', color='#27ae60',
            arrowprops=dict(arrowstyle='->', color='#27ae60', lw=3))

plt.tight_layout()
plt.savefig(os.path.join(img_dir, '16-simulate-vs-live.png'), dpi=150, bbox_inches='tight')
plt.close()
print("  10. SIMULATE vs LIVE saved")

print("\nAll diagrams generated!")
