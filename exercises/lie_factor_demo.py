"""
Lie Factor Demonstration — Edward Tufte
========================================
For classroom use: illustrates how visual distortion misleads readers.

Tufte's Lie Factor = (Size of effect shown in graphic) / (Size of effect in data)
    - Lie Factor = 1.0  → honest representation
    - Lie Factor > 1.0  → exaggerates the data
    - Lie Factor < 1.0  → understates the data

This script generates two side-by-side charts:
  LEFT  — A deliberately misleading bar chart (Lie Factor ≈ 5.6)
  RIGHT — The honest version of the same data (Lie Factor = 1.0)

Technique used: truncated y-axis (non-zero baseline)
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ── Data ──────────────────────────────────────────────────────────────────────
# Fictional company quarterly revenue ($M) — a modest 5% growth story
quarters = ["Q1", "Q2", "Q3", "Q4"]
revenue  = [100, 102, 104, 105]          # only a 5% increase Q1→Q4

# ── Lie Factor Calculation ─────────────────────────────────────────────────────
# In the data:   effect = (105 - 100) / 100 = 5%
# In the graphic (truncated axis 98–106):
#   visual height of Q1 bar = 100 - 98 = 2 units
#   visual height of Q4 bar = 105 - 98 = 7 units
#   visual effect = (7 - 2) / 2 = 250%
# Lie Factor ≈ 250% / 5% ≈ 5.0  (clearly > 1)

data_effect   = (revenue[-1] - revenue[0]) / revenue[0]        # 0.05 → 5%
mislead_min   = 98                                              # truncated baseline

visual_q1     = revenue[0]  - mislead_min                      # 2
visual_q4     = revenue[-1] - mislead_min                      # 7
visual_effect = (visual_q4 - visual_q1) / visual_q1            # (7-2)/2 = 2.5 → 250%

lie_factor    = visual_effect / data_effect                     # 250% / 5% = 5.0

# ── Colour Palette ─────────────────────────────────────────────────────────────
RED    = "#E63946"
GREEN  = "#2A9D8F"
DARK   = "#1D1D2E"
LIGHT  = "#F4F1EC"
GREY   = "#9CA3AF"
YELLOW = "#E9C46A"

# ── Figure Setup ──────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(14, 7), facecolor=DARK)
fig.suptitle(
    "Tufte's Lie Factor  —  How a Truncated Axis Distorts Reality",
    fontsize=16, fontweight="bold", color=LIGHT, y=1.01
)

x = np.arange(len(quarters))
bar_width = 0.55

# ══════════════════════════════════════════════════════════════════════════════
# LEFT PANEL — Misleading chart (Lie Factor ≈ 5.0)
# ══════════════════════════════════════════════════════════════════════════════
ax1 = axes[0]
ax1.set_facecolor(DARK)

bars1 = ax1.bar(x, revenue, width=bar_width, color=RED, zorder=3,
                linewidth=0, edgecolor="none")

# Gradient-ish effect: darken the first bar to emphasise "small"
bars1[0].set_color("#9B2226")

# Axis — TRUNCATED (the lie)
ax1.set_ylim(mislead_min, 107)
ax1.set_xticks(x)
ax1.set_xticklabels(quarters, fontsize=13, color=LIGHT, fontweight="bold")
ax1.set_ylabel("Revenue ($M)", color=GREY, fontsize=11)
ax1.tick_params(colors=GREY)
ax1.spines[["top", "right"]].set_visible(False)
ax1.spines[["left", "bottom"]].set_color(GREY)
ax1.yaxis.set_tick_params(labelcolor=GREY)

# Value labels on bars
for bar, val in zip(bars1, revenue):
    ax1.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.15,
             f"${val}M", ha="center", va="bottom", color=LIGHT,
             fontsize=11, fontweight="bold")

# Annotation callouts
ax1.set_title("[X]  MISLEADING  (Lie Factor ~ {:.1f})".format(lie_factor),
              color=RED, fontsize=13, fontweight="bold", pad=12)
ax1.text(0.5, 0.08,
         "Y-axis starts at ${}M, not $0\n"
         "A 5% change LOOKS like 250%!".format(mislead_min),
         transform=ax1.transAxes, ha="center", va="bottom",
         fontsize=10, color=YELLOW,
         bbox=dict(boxstyle="round,pad=0.4", facecolor="#3A3A55",
                   edgecolor=YELLOW, linewidth=1.2))

# Arrow pointing at the baseline break
ax1.annotate("← Axis starts\n   here ($98M)",
             xy=(x[0], mislead_min + 0.3), xytext=(x[0] + 1.1, mislead_min + 1.2),
             arrowprops=dict(arrowstyle="->", color=YELLOW, lw=1.5),
             color=YELLOW, fontsize=9)

# ══════════════════════════════════════════════════════════════════════════════
# RIGHT PANEL — Honest chart (Lie Factor = 1.0)
# ══════════════════════════════════════════════════════════════════════════════
ax2 = axes[1]
ax2.set_facecolor(DARK)

bars2 = ax2.bar(x, revenue, width=bar_width, color=GREEN, zorder=3,
                linewidth=0, edgecolor="none")

# Axis starts at TRUE ZERO
ax2.set_ylim(0, 130)
ax2.set_xticks(x)
ax2.set_xticklabels(quarters, fontsize=13, color=LIGHT, fontweight="bold")
ax2.set_ylabel("Revenue ($M)", color=GREY, fontsize=11)
ax2.tick_params(colors=GREY)
ax2.spines[["top", "right"]].set_visible(False)
ax2.spines[["left", "bottom"]].set_color(GREY)
ax2.yaxis.set_tick_params(labelcolor=GREY)

for bar, val in zip(bars2, revenue):
    ax2.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1.2,
             f"${val}M", ha="center", va="bottom", color=LIGHT,
             fontsize=11, fontweight="bold")

ax2.set_title("[OK]  HONEST  (Lie Factor = 1.0)",
              color=GREEN, fontsize=13, fontweight="bold", pad=12)
ax2.text(0.5, 0.08,
         "Y-axis starts at $0\n"
         "5% growth looks like… 5% growth.",
         transform=ax2.transAxes, ha="center", va="bottom",
         fontsize=10, color=YELLOW,
         bbox=dict(boxstyle="round,pad=0.4", facecolor="#3A3A55",
                   edgecolor=GREEN, linewidth=1.2))

# ── Footer / formula box ───────────────────────────────────────────────────────
fig.text(
    0.5, -0.04,
    "Lie Factor  =  (visual effect shown in graphic)  ÷  (actual effect in data)\n"
    "Here:  visual Q1→Q4 change = {:.0f}%   |   actual Q1→Q4 change = {:.0f}%   "
    "→   Lie Factor ≈ {:.1f}".format(
        visual_effect * 100, data_effect * 100, lie_factor),
    ha="center", fontsize=11, color=YELLOW,
    bbox=dict(boxstyle="round,pad=0.6", facecolor="#2A2A3E",
              edgecolor=YELLOW, linewidth=1.5)
)

plt.tight_layout(pad=2.5)
output_path = "lie_factor_demo.png"
plt.savefig(output_path, dpi=150, bbox_inches="tight", facecolor=DARK)
print(f"Saved → {output_path}")
print(f"\nLie Factor Summary")
print(f"  Actual data effect (Q1→Q4): {data_effect*100:.1f}%")
print(f"  Visual effect shown:         {visual_effect*100:.1f}%")
print(f"  Lie Factor:                  {lie_factor:.1f}")
plt.show()
