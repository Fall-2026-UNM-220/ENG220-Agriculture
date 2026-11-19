# 1. Import libraries

import matplotlib.pyplot as plt
import numpy as np

# 2. vegetable production values from research

vegetables = [
    "Cucumber\n(46 days)",
    "Tomato\n(80 days)",
    "Head Lettuce\n(145 days)"
]

production = [
    5.14,
    3.58,
    2.84
]

# 3. Create vertical bar graph

fig, ax = plt.subplots(figsize=(10, 6))

colors = [
    "#C6DDED",
    "#75A9D0",
    "#286D9E"
]

bars = ax.bar(
    vegetables,
    production,
    color=colors,
    width=0.6
)

# 4. Add values above each bar

for bar in bars:
    height = bar.get_height()

    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height + 0.1,
        f"{height:.2f}",
        ha="center",
        fontsize=12,
        fontweight="bold"
    )

# 5. Add graph title and axis labels

    ax.set_title(
        "Aquaponics Vegetable Production",
        fontsize=16,
        fontweight="bold",
        pad=18
    )

    ax.set_ylabel("Total Yield (kg/m²)", fontsize=11)
    ax.set_xlabel("Vegetable and Growing Period", fontsize=11)

# 6. Format graph

    ax.set_ylim(0, 6)

    ax.grid(axis="y", linestyle="--", alpha=0.4)

    ax.set_axisbelow(True)

# 7. Add source

    fig.text(
        0.5, 0.03,
        "Source: Goda et al. (2015), Table 2, page 531. "
        "IMTA-FRS aquaponic system.",
        ha="center",
        fontsize=9
    )

#  8. Adjust layout and save graph

    plt.tight_layout(rect=[0, 0.08, 1, 1])

    plt.savefig(
        "Graph5_Aquaponics_Vegetable_Production.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()