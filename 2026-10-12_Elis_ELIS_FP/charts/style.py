"""Shared chart style (dataviz reference palette, print/light mode). Liberation Sans = Arial-metric."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm

INK, INK2, MUTED = '#0b0b0b', '#52514e', '#898781'
GRID, AXIS, SURFACE = '#e1e0d9', '#c3c2b7', '#ffffff'
NAVY = '#13213f'
# categorical slots, fixed order (validated reference palette, light mode)
CAT = ['#2a78d6', '#eb6834', '#1baf7a', '#eda100', '#e87ba4', '#008300', '#6250d6', '#e34948']
BLUE, ORANGE, AQUA, YELLOW, MAGENTA, GREEN, VIOLET, RED = CAT
GOOD, WARN, SERIOUS, CRITICAL = '#0ca30c', '#fab219', '#ec835a', '#d03b3b'
SEQ = ['#cde2fb', '#9ec5f4', '#6da7ec', '#3987e5', '#2a78d6', '#1c5cab', '#104281', '#0d366b']
PEER_GRAY = '#9a9890'

def setup():
    plt.rcParams.update({
        'font.family': 'Liberation Sans', 'font.size': 9, 'axes.titlesize': 10, 'axes.titleweight': 'bold',
        'axes.titlelocation': 'left', 'axes.labelsize': 8.5, 'axes.labelcolor': INK2, 'axes.edgecolor': AXIS,
        'axes.linewidth': 0.8, 'axes.spines.top': False, 'axes.spines.right': False, 'axes.grid': True,
        'axes.grid.axis': 'y', 'grid.color': GRID, 'grid.linewidth': 0.8, 'grid.linestyle': '-',
        'xtick.color': MUTED, 'ytick.color': MUTED, 'xtick.labelsize': 8, 'ytick.labelsize': 8,
        'xtick.major.size': 0, 'ytick.major.size': 0, 'legend.frameon': False, 'legend.fontsize': 8,
        'figure.facecolor': SURFACE, 'axes.facecolor': SURFACE, 'savefig.facecolor': SURFACE,
        'lines.linewidth': 2.0, 'lines.solid_capstyle': 'round', 'lines.solid_joinstyle': 'round',
        'text.color': INK, 'figure.dpi': 110, 'savefig.dpi': 220, 'savefig.bbox': 'tight', 'savefig.pad_inches': 0.08,
    })

def source_note(fig, text, y=-0.02):
    fig.text(0.0, y, text, fontsize=6.8, color=MUTED, ha='left', va='top', transform=fig.transFigure)

def rounded_bars(ax, x, h, width=0.6, color=BLUE, bottom=None, **kw):
    """Bars with a 4px-ish rounded data end (approximated with FancyBboxPatch)."""
    from matplotlib.patches import FancyBboxPatch
    import numpy as np
    bottom = np.zeros(len(h)) if bottom is None else bottom
    patches = []
    for xi, hi, bi in zip(x, h, bottom):
        if hi == 0 or hi is None:
            continue
        y0, hh = (bi, hi) if hi > 0 else (bi + hi, -hi)
        p = FancyBboxPatch((xi - width / 2, y0), width, hh, boxstyle='round,pad=0,rounding_size=0.0', linewidth=0, facecolor=color, **kw)
        ax.add_patch(p); patches.append(p)
    return patches
