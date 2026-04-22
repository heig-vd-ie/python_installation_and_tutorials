import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Polygon

def create_figure(figsize=(11, 6), facecolor="#efefef"):
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_facecolor(facecolor)
    return fig, ax

def bus(ax, x, y, label, text_dx=0.12, text_dy=0.12, fontsize=15):
    ax.plot(x, y, 'ko', ms=8)
    ax.text(x + text_dx, y + text_dy, label, fontsize=fontsize)

def square(ax, x, y, s=0.10, facecolor="black", edgecolor="black"):
    ax.add_patch(Rectangle((x - s/2, y - s/2), s, s, fc=facecolor, ec=edgecolor))

def line(ax, p1, p2, label, dx=0, dy=0, color="gray", lw=1.5, fontsize=12):
    x1, y1 = p1
    x2, y2 = p2
    ax.plot([x1, x2], [y1, y2], color=color, lw=lw)
    ax.text((x1+x2)/2 + dx, (y1+y2)/2 + dy, label, fontsize=12)

def load_down(ax, x, y, label, color="gray", lw=1.2, fontsize=12):
    ax.plot([x, x], [y, y-0.45], color=color, lw=lw)
    tri = Polygon([[x-0.12, y-0.45], [x+0.12, y-0.45], [x, y-0.78]],
                  closed=True, fill=False, ec=color, lw=lw)
    ax.add_patch(tri)
    ax.text(x-0.35, y-1.0, label, fontsize=fontsize)

def gen_up(ax, x, y, label="gen", color="gray", lw=1.2, fontsize=12):
    ax.plot([x, x], [y, y+0.40], color=color, lw=lw)
    tri = Polygon([[x-0.10, y+0.58], [x+0.10, y+0.58], [x, y+0.82]],
                  closed=True, fill=False, ec=color, lw=lw)
    ax.add_patch(tri)
    ax.text(x-0.25, y+1.02, label, fontsize=fontsize)

def ext_grid(ax, x, y, label="external grid", color="gray", lw=1.2, fontsize=14):
    ax.plot([x, x], [y, y+0.40], color=color, lw=lw)
    square(ax, x, y+0.18, 0.10, facecolor='white', edgecolor=color)
    w, h = 0.40, 0.40
    ax.add_patch(Rectangle((x-w/2, y+0.40), w, h, fill=False, ec=color, lw=1.0))
    ax.plot([x-w/2, x+w/2], [y+0.40, y+0.40+h], color=color, lw=0.8)
    ax.plot([x-w/2, x+w/2], [y+0.40+h, y+0.40], color=color, lw=0.8)
    ax.text(x+0.45, y+0.50, label, fontsize=fontsize)

def trafo(ax, p1, p2, label="T1", color="gray", lw=1.2, fontsize=12):
    x1, y1 = p1
    x2, y2 = p2
    xm, ym = (x1+x2)/2, (y1+y2)/2
    ax.plot([x1, xm-0.18], [y1, ym], color=color, lw=lw)
    ax.plot([xm+0.18, x2], [ym, y2], color=color, lw=lw)
    ax.add_patch(Circle((xm-0.09, ym), 0.09, fill=False, ec=color, lw=lw))
    ax.add_patch(Circle((xm+0.09, ym), 0.09, fill=False, ec=color, lw=lw))
    ax.text(xm+0.25, ym+0.15, label, fontsize=fontsize)