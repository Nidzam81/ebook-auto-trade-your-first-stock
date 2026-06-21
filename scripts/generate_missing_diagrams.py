import os
import shutil
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle
import numpy as np

# Paths
dest_dir = r"C:\Users\Nidzam\ebook-auto-trading\images"
system_dir = r"C:\Users\Nidzam\.gemini\antigravity-cli\brain\dfb0a9ba-70f8-47ec-b5f9-a4591497e09c"

# Set styling for matplotlib
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.family'] = 'Segoe UI, Arial, sans-serif'
plt.rcParams['font.size'] = 11

print("Copying generated images...")

# Copier function
def copy_img(src_pattern, dest_name):
    # Find files starting with src_pattern in system_dir
    files = [f for f in os.listdir(system_dir) if f.startswith(src_pattern)]
    if files:
        # Sort to get the latest
        files.sort()
        src_path = os.path.join(system_dir, files[-1])
        dest_path = os.path.join(dest_dir, dest_name)
        shutil.copy2(src_path, dest_path)
        print(f"Copied {files[-1]} to {dest_name}")
    else:
        print(f"No file found for pattern: {src_pattern}")

# Copy the generated images
copy_img("cover_illustration", "00-cover.jpg")
copy_img("confused_chart", "13-confused-chart.jpg")
copy_img("weekly_planner", "13-weekly-planner.jpg")
copy_img("browser_dashboard", "15-browser-dashboard.jpg")
copy_img("staircase_indicators", "17-staircase-indicators.jpg")
copy_img("robot_mechanic", "18-robot-mechanic.jpg")

print("\nGenerating remaining diagrams via Matplotlib...")

# ============================================================
# Diagram 1: 18-flowchart-troubleshoot.png
# ============================================================
fig, ax = plt.subplots(1, 1, figsize=(12, 4))
ax.set_xlim(0, 12)
ax.set_ylim(0, 4)
ax.axis('off')
ax.set_facecolor('#f8f9fa')
fig.patch.set_facecolor('#f8f9fa')

ax.text(6, 3.5, '5-Step Troubleshooting Flowchart', fontsize=16, fontweight='bold',
        ha='center', va='center', color='#2c3e50')

steps = [
    '1. Check\nmoomoo open?',
    '2. Check\nOpenD?',
    '3. Check port/\npassword?',
    '4. Check\nfirewall?',
    '5. Restart\nHermes'
]
colors = ['#3498db', '#9b59b6', '#e67e22', '#e74c3c', '#2ecc71']
x_pos = np.linspace(1.2, 10.8, len(steps))

for i, (text, x, color) in enumerate(zip(steps, x_pos, colors)):
    # Draw box
    box = FancyBboxPatch((x-0.9, 1.2), 1.8, 1.3,
                          boxstyle="round,pad=0.1",
                          facecolor=color, edgecolor='none', alpha=0.9)
    ax.add_patch(box)
    ax.text(x, 1.85, text, fontsize=10, fontweight='bold',
            ha='center', va='center', color='white')
    
    # Draw arrow to next if not last
    if i < len(steps) - 1:
        next_x = x_pos[i+1]
        ax.annotate('', xy=(next_x - 1.0, 1.85), xytext=(x + 1.0, 1.85),
                    arrowprops=dict(arrowstyle='->', color='#7f8c8d', lw=2))

plt.tight_layout()
plt.savefig(os.path.join(dest_dir, '18-flowchart-troubleshoot.png'), dpi=150, bbox_inches='tight')
plt.close()
print("  Generated: 18-flowchart-troubleshoot.png")

# ============================================================
# Diagram 2: 19-stretching-calendar.png
# ============================================================
fig, ax = plt.subplots(1, 1, figsize=(8, 5))
ax.set_xlim(0, 8)
ax.set_ylim(0, 5)
ax.axis('off')
ax.set_facecolor('#f8f9fa')
fig.patch.set_facecolor('#f8f9fa')

ax.text(4, 4.4, 'Your Maintenance Routine', fontsize=16, fontweight='bold',
        ha='center', va='center', color='#2c3e50')

# Calendar box
cal_box = FancyBboxPatch((0.8, 0.8), 6.4, 3.0,
                          boxstyle="round,pad=0.1",
                          facecolor='white', edgecolor='#bdc3c7', linewidth=1)
ax.add_patch(cal_box)

# Header
ax.add_patch(Rectangle((0.8, 3.2), 6.4, 0.6, facecolor='#2ecc71', edgecolor='none'))
ax.text(4, 3.5, 'ROUTINE CHECKLIST', fontsize=12, fontweight='bold', ha='center', va='center', color='white')

# Checklist items
items = [
    ('[OK]  Daily Check:  Verify positions, balance, and logs', '#2c3e50'),
    ('[OK]  Weekly Review:  Backup configurations & evaluate PnL', '#2c3e50'),
    ('[OK]  Monthly Update:  Check for software & moomoo API updates', '#2c3e50'),
    ('[OK]  Physical Stretches:  Remember to stretch after desk work!', '#27ae60')
]

for i, (item, color) in enumerate(items):
    y = 2.8 - i * 0.6
    ax.text(1.2, y, item, fontsize=11, ha='left', va='center', color=color)

plt.tight_layout()
plt.savefig(os.path.join(dest_dir, '19-stretching-calendar.png'), dpi=150, bbox_inches='tight')
plt.close()
print("  Generated: 19-stretching-calendar.png")

# ============================================================
# Diagram 3: 20-vault-security.png
# ============================================================
fig, ax = plt.subplots(1, 1, figsize=(8, 5))
ax.set_xlim(0, 8)
ax.set_ylim(0, 5)
ax.axis('off')
ax.set_facecolor('#f8f9fa')
fig.patch.set_facecolor('#f8f9fa')

ax.text(4, 4.4, 'Securing Your System', fontsize=16, fontweight='bold',
        ha='center', va='center', color='#2c3e50')

# Draw Vault Dial
circle_outer = plt.Circle((4, 2.2), 1.6, facecolor='#34495e', edgecolor='#2c3e50', linewidth=3)
ax.add_patch(circle_outer)
circle_inner = plt.Circle((4, 2.2), 1.2, facecolor='#7f8c8d', edgecolor='#34495e', linewidth=2)
ax.add_patch(circle_inner)
circle_dial = plt.Circle((4, 2.2), 0.5, facecolor='#bdc3c7', edgecolor='#7f8c8d', linewidth=2)
ax.add_patch(circle_dial)

# Dial ticks
for angle in range(0, 360, 30):
    rad = np.deg2rad(angle)
    x1, y1 = 4 + 1.2 * np.cos(rad), 2.2 + 1.2 * np.sin(rad)
    x2, y2 = 4 + 1.5 * np.cos(rad), 2.2 + 1.5 * np.sin(rad)
    ax.plot([x1, x2], [y1, y2], color='#ecf0f1', linewidth=2)

ax.text(4, 2.2, 'SAFE', fontsize=10, fontweight='bold', ha='center', va='center', color='#2c3e50')

# Safe text
ax.text(4, 0.3, 'Never share API keys or configuration files!', fontsize=11, fontweight='bold',
        ha='center', va='center', color='#c0392b')

plt.tight_layout()
plt.savefig(os.path.join(dest_dir, '20-vault-security.png'), dpi=150, bbox_inches='tight')
plt.close()
print("  Generated: 20-vault-security.png")

# ============================================================
# Diagram 4: 28-glossary-dictionary.png
# ============================================================
fig, ax = plt.subplots(1, 1, figsize=(9, 5))
ax.set_xlim(0, 9)
ax.set_ylim(0, 5)
ax.axis('off')
ax.set_facecolor('#f8f9fa')
fig.patch.set_facecolor('#f8f9fa')

ax.text(4.5, 4.4, 'Trading Glossary Quick Reference', fontsize=16, fontweight='bold',
        ha='center', va='center', color='#2c3e50')

# Book background
book_box = FancyBboxPatch((0.5, 0.8), 8.0, 3.1,
                           boxstyle="round,pad=0.1",
                           facecolor='white', edgecolor='#3498db', linewidth=2)
ax.add_patch(book_box)

# Center divider line
ax.plot([4.5, 4.5], [0.8, 3.8], color='#3498db', linewidth=1.5, linestyle='--')

# Left page terms
left_terms = [
    ('API', 'Application Programming Interface -\ntalks to other systems'),
    ('RSI', 'Relative Strength Index -\nindicates overbought/oversold status'),
    ('PnL', 'Profit and Loss -\nyour net trading returns')
]

for i, (term, defn) in enumerate(left_terms):
    y = 3.3 - i * 1.0
    ax.text(0.8, y, term, fontsize=12, fontweight='bold', ha='left', va='center', color='#2980b9')
    ax.text(0.8, y - 0.3, defn, fontsize=9.5, ha='left', va='center', color='#34495e')

# Right page terms
right_terms = [
    ('SIMULATE', 'Paper trading mode using real-time\nmarket data but fake money'),
    ('LIVE', 'Real trading using real money\nfrom your moomoo account'),
    ('CRON JOB', 'Automated timer that runs your\ntrading agent on a schedule')
]

for i, (term, defn) in enumerate(right_terms):
    y = 3.3 - i * 1.0
    ax.text(4.8, y, term, fontsize=12, fontweight='bold', ha='left', va='center', color='#2980b9')
    ax.text(4.8, y - 0.3, defn, fontsize=9.5, ha='left', va='center', color='#34495e')

plt.tight_layout()
plt.savefig(os.path.join(dest_dir, '28-glossary-dictionary.png'), dpi=150, bbox_inches='tight')
plt.close()
print("  Generated: 28-glossary-dictionary.png")

print("All image setups done successfully!")
