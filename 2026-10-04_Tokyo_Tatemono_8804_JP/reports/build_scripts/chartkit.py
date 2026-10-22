"""Shared chart styling + chart builders for the Tokyo Tatemono report (static PNG, print-first)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np

# ---- palette (dataviz reference instance, light mode) ----
NAVY = "#15233F"
BLUE = "#2a78d6"      # categorical slot 1 / highlight
ORANGE = "#eb6834"    # slot 2
AQUA = "#1baf7a"      # slot 3
YELLOW = "#eda100"    # slot 4
MAGENTA = "#e87ba4"   # slot 5
GREEN = "#008300"     # slot 6
VIOLET = "#4a3aa7"    # slot 7
RED = "#e34948"       # slot 8
CAT = [BLUE, ORANGE, AQUA, YELLOW, MAGENTA, GREEN, VIOLET, RED]
PEER = "#B8BEC9"      # de-emphasis grey for peers
INK = "#0b0b0b"
INK2 = "#52514e"
MUTED = "#898781"
GRID = "#e1e0d9"
AXIS = "#c3c2b7"
SURFACE = "#ffffff"

# Japanese-capable fallback font
for f in ["/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf"]:
    try:
        font_manager.fontManager.addfont(f)
    except Exception:
        pass

plt.rcParams.update({
    "font.family": ["Liberation Sans", "IPAGothic", "DejaVu Sans"],
    "font.size": 9,
    "axes.edgecolor": AXIS,
    "axes.linewidth": 0.8,
    "axes.labelcolor": INK2,
    "axes.titlesize": 10.5,
    "axes.titleweight": "bold",
    "axes.titlecolor": NAVY,
    "axes.titlelocation": "left",
    "axes.grid": True,
    "axes.axisbelow": True,
    "grid.color": GRID,
    "grid.linewidth": 0.6,
    "grid.linestyle": "-",
    "xtick.color": MUTED,
    "ytick.color": MUTED,
    "xtick.labelcolor": INK2,
    "ytick.labelcolor": INK2,
    "legend.frameon": False,
    "legend.fontsize": 8.5,
    "figure.facecolor": SURFACE,
    "axes.facecolor": SURFACE,
    "savefig.facecolor": SURFACE,
    "savefig.dpi": 220,
})


def clean(ax, grid_axis="y"):
    for s in ["top", "right"]:
        ax.spines[s].set_visible(False)
    ax.grid(True, axis=grid_axis)
    ax.grid(False, axis="x" if grid_axis == "y" else "y")
    ax.tick_params(length=0)


def source(fig, text, y=0.01):
    fig.text(0.01, y, text, fontsize=7, color=MUTED, ha="left", va="bottom", style="italic")


def save(fig, out):
    fig.savefig(out, bbox_inches="tight", pad_inches=0.08)
    plt.close(fig)
    return out
