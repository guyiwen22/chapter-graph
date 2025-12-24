import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["Times New Roman"]

def arrow_axes(ax):
    # Hide normal spines
    for spine in ["top", "right", "left", "bottom"]:
        ax.spines[spine].set_visible(False)

    # Remove ticks
    ax.set_xticks([])
    ax.set_yticks([])

    # Get limits
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()

    # Draw arrow axes
    ax.annotate(
        "", xy=(xmax, ymin), xytext=(xmin, ymin),
        arrowprops=dict(arrowstyle="->", linewidth=1.2, color="black")
    )
    ax.annotate(
        "", xy=(xmin, ymax), xytext=(xmin, ymin),
        arrowprops=dict(arrowstyle="->", linewidth=1.2, color="black")
    )

# X range (conceptual time)
x = np.linspace(0, 10, 400)

# Common limits
xlim = (0, 10)
ylim = (8.5, 10.5)

# =========================
# Graph 1: Gentle downward trend
# =========================
y1 = 10 - 0.04 * x

fig, ax = plt.subplots(figsize=(5, 4))
ax.plot(x, y1, linewidth=1.5, color="black")
ax.set_xlabel("Time",fontsize=12, fontname="Times New Roman")
ax.set_ylabel("Relationship Satisfaction",fontsize=12, fontname="Times New Roman")
ax.set_title("Figure 1a",fontsize=12, fontname="Times New Roman")
ax.set_xlim(xlim)
ax.set_ylim(ylim)
arrow_axes(ax)
plt.tight_layout()
plt.show()

# =========================
# Graph 2: Sharp V-shaped mid disruption
# =========================
baseline = 10 - 0.04 * x
center = 5.0
width = 1.5
depth = 0.5

v_drop = np.maximum(0, 1 - np.abs(x - center) / width)
y2 = baseline - depth * v_drop

fig, ax = plt.subplots(figsize=(5, 4))
ax.plot(x, y2, linewidth=1.5, color="black")
ax.set_xlabel("Time",fontsize=12, fontname="Times New Roman")
ax.set_ylabel("Relationship Satisfaction",fontsize=12, fontname="Times New Roman")
ax.set_title("Figure 1b",fontsize=12, fontname="Times New Roman")
ax.set_xlim(xlim)
ax.set_ylim(ylim)
arrow_axes(ax)
plt.tight_layout()
plt.show()

# =========================
# Graph 3: Fluctuations around the trend
# =========================
y3 = baseline + 0.15 * np.sin(3.0 * x)

fig, ax = plt.subplots(figsize=(5, 4))
ax.plot(x, y3, linewidth=1.5, color="black")
ax.set_xlabel("Time",fontsize=12, fontname="Times New Roman")
ax.set_ylabel("Relationship Satisfaction",fontsize=12, fontname="Times New Roman")
ax.set_title("Figure 1c",fontsize=12, fontname="Times New Roman")
ax.set_xlim(xlim)
ax.set_ylim(ylim)
arrow_axes(ax)
plt.tight_layout()
plt.show()
