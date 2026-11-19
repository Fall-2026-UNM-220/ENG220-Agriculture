# 1. Import libraries

import matplotlib.pyplot as plt
import numpy as np

# 2. Water usage values from research

growing_methods = [
    "Conventional Agriculture",
    "Aquaponics"
]

water_usage = [
    250,
    60
]

# 3. Create the horizontal bar graph

fig, ax = plt.subplots(figsize=(11, 5))

colors = [
    "#75A9D0",
    "#286D9E"
]

# Create bars

ax.barh(
    growing_methods,
    [280, 280],
    color="#EEEEEE",
    height=0.6
)

# Actual water usage bars

bars = ax.barh(
    growing_methods,
    water_usage,
    color=colors,
    height=0.6
)

# 4. Add values at the end of each bar

for bar in bars:
    width = bar.get_width()

    ax.text(
        width + 5,
        bar.get_y() + bar.get_height() / 2,
        f"{int(width)}",
        va="center",
        fontsize=12,
        fontweight="bold",
        color="black"
    )

#  5. Put graph title and axis label

ax.set_title(
    "Water Dependency by Growing Method",
    fontsize=16,
    fontweight="bold",
    loc="left",
    pad=18
)

ax.set_xlabel("Water Dependency (L/kg)", fontsize=11)

# 6. Format graph

ax.set_xlim(0, 300)

ax.invert_yaxis()

ax.set_yticks(
    [0, 1],
    labels=growing_methods,
    fontsize=12,
    fontweight="bold"
)

ax.set_xticks([])

ax.tick_params(axis="y", length=0, pad=10)

# Remove the borders

for spine in ax.spines.values():
    spine.set_visible(False)

ax.set_facecolor("white")
fig.patch.set_facecolor("white")

# 7. Add source

fig.text(
    0.05, 0.06,
    "Source: CU Denver (2017), abstract, page 25. "
    "Values converted from m³/kg to L/kg.",
    fontsize=9,
    color="black"
)

# 8. Adjust layout and save graph

plt.subplots_adjust(
    left=0.05,
    right=0.93,
    top=0.82,
    bottom=0.22
)

plt.savefig(
    "Graph4_Water_Usage_Analysis.png",
    dpi=300,
    bbox_inches="tight",
    facecolor="white"
)

plt.show()