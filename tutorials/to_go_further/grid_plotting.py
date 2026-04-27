import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Polygon
import math

def create_figure(figsize=(11, 6), facecolor="#efefef"):
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_facecolor(facecolor)
    return fig, ax

def bus(ax, x, y, label, text_dx=0.12, text_dy=0.12, fontsize=15):
    ax.plot(x, y, 'ko', ms=8)
    ax.text(x + text_dx, y + text_dy, label, fontsize=fontsize)

def square(ax, x, y, s=0.10, facecolor="black", edgecolor="black"):
    ax.add_patch(Rectangle((x - s/2, y - s/2), s, s, fc=facecolor, ec=edgecolor))
    
def square_on_line(ax, p1, p2, t=0.5, offset=0.0, s=0.10,
                   facecolor="black", edgecolor="black"):
    x1, y1 = p1
    x2, y2 = p2

    dx = x2 - x1
    dy = y2 - y1
    L = math.hypot(dx, dy)

    if L == 0:
        x, y = x1, y1
    else:
        nx = -dy / L
        ny = dx / L
        x = x1 + t * dx + offset * nx
        y = y1 + t * dy + offset * ny

    square(ax, x, y, s=s, facecolor=facecolor, edgecolor=edgecolor)


def line(ax, p1, p2, label, t=0.5, normal_offset=0.15,
         text_dx=0.1, text_dy=0.2, color="gray", lw=1.5, fontsize=12):
    x1, y1 = p1
    x2, y2 = p2

    ax.plot([x1, x2], [y1, y2], color=color, lw=lw)

    
    dx = x2 - x1
    dy = y2 - y1
    L = math.hypot(dx, dy)

    if L == 0:
        xt = x1
        yt = y1
    else:
        nx = -dy / L
        ny = dx / L
        xt = x1 + t * dx + normal_offset * nx + text_dx
        yt = y1 + t * dy + normal_offset * ny + text_dy

    ax.text(xt, yt, label, fontsize=fontsize)

def load_down(ax, x, y, label, stem=0.45, arrow=0.33,
              text_dx=-0.35, text_dy=-1.0, color="gray", lw=1.2, fontsize=12):
    ax.plot([x, x], [y, y - stem], color=color, lw=lw)

    tri = Polygon(
        [[x - 0.12, y - stem], [x + 0.12, y - stem], [x, y - stem - arrow]],
        closed=True, fill=False, ec=color, lw=lw
    )
    ax.add_patch(tri)
    ax.text(x + text_dx, y + text_dy, label, fontsize=fontsize)


def gen_up(ax, x, y, label="gen", stem=0.40, arrow=0.24,
           text_dx=-0.25, text_dy=1.02, color="gray", lw=1.2, fontsize=12):
    ax.plot([x, x], [y, y + stem], color=color, lw=lw)

    tri = Polygon(
        [[x - 0.10, y + stem + 0.18],
         [x + 0.10, y + stem + 0.18],
         [x, y + stem + 0.18 + arrow]],
        closed=True, fill=False, ec=color, lw=lw
    )
    ax.add_patch(tri)
    ax.text(x + text_dx, y + text_dy, label, fontsize=fontsize)


def ext_grid(ax, x, y, label="external grid",
             box_dx=0.0, box_dy=0.40,
             text_dx=0.45, text_dy=0.50,
             color="gray", lw=1.2, fontsize=14):
    ax.plot([x, x], [y, y + 0.40], color=color, lw=lw)
    square(ax, x, y + 0.18, 0.10, facecolor='white', edgecolor=color)

    w, h = 0.40, 0.40
    x0 = x - w/2 + box_dx
    y0 = y + box_dy

    ax.add_patch(Rectangle((x0, y0), w, h, fill=False, ec=color, lw=1.0))
    ax.plot([x0, x0 + w], [y0, y0 + h], color=color, lw=0.8)
    ax.plot([x0, x0 + w], [y0 + h, y0], color=color, lw=0.8)

    ax.text(x + text_dx, y + text_dy, label, fontsize=fontsize)


def trafo(ax, p1, p2, label="T1", text_dx=0.25, text_dy=0.15,
          color="gray", lw=1.2, fontsize=12):
    x1, y1 = p1
    x2, y2 = p2
    xm, ym = (x1 + x2) / 2, (y1 + y2) / 2

    ax.plot([x1, xm - 0.18], [y1, ym], color=color, lw=lw)
    ax.plot([xm + 0.18, x2], [ym, y2], color=color, lw=lw)

    ax.add_patch(Circle((xm - 0.09, ym), 0.09, fill=False, ec=color, lw=lw))
    ax.add_patch(Circle((xm + 0.09, ym), 0.09, fill=False, ec=color, lw=lw))

    ax.text(xm + text_dx, ym + text_dy, label, fontsize=fontsize)