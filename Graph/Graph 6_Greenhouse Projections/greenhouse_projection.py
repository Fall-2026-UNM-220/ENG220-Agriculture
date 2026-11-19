
# 1. Import libraries

import matplotlib.pyplot as plt

# 2. Geenhouse dimensions and growing-space estimate

greenhouse_length = 96
greenhouse_width = 30

total_area = greenhouse_length * greenhouse_width

growing_space_percentage = 0.64

growing_area = total_area * growing_space_percentage

print("Total greenhouse area:", total_area, "sq. ft.")
print("Estimated growing area:", growing_area, "sq. ft.")

# 3. Divide growing area among vegetables

vegetables = [
    "Head Lettuce\n(145 days)",
    "Tomato\n(80 days)",
    "Cucumber\n(46 days)"
]

growing_area_per_crop = growing_area / 3

# Convert square feet to square meters

growing_area_m2 = growing_area_per_crop * 0.092903

print("Growing area per vegetable:", growing_area_per_crop, "sq. ft.")
print("Growing area per vegetable:", growing_area_m2, "m²")

# 4. Enter production rates from research

production_rates = [
    2.84,
    3.58,
    5.14
]

# Production rates are measured in kg per square meter

# 5. Calculate projected vegetable production

production = []

for rate in production_rates:
    total_production = rate * growing_area_m2
    production.append(total_production)

print("Projected vegetable production:")

for vegetable, amount in zip(vegetables, production):
    print(vegetable, ":", round(amount, 2), "kg")

# 6. Calculate total projected production

total_production = sum(production)

print("Total projected production:", round(total_production, 2), "kg")

# 7. Create vertical bar graph

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

# 8. Add production values above each bar

for bar in bars:
    height = bar.get_height()

    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height + 5,
        f"{height:.1f} kg",
        ha="center",
        fontsize=12,
        fontweight="bold"
    )

# 9. Add graph title and axis labels

ax.set_title(
    "Projected Greenhouse Vegetable Production",
    fontsize=16,
    fontweight="bold",
    pad=18
)

ax.set_ylabel("Projected Production (kg)", fontsize=11)
ax.set_xlabel("Vegetable and Growing Period", fontsize=11)

# 10. Format graph

ax.set_ylim(0, max(production) + 60)

ax.grid(axis="y", linestyle="--", alpha=0.4)

ax.set_axisbelow(True)

# 11. Add greenhouse assumptions and research source

fig.text(
    0.5, 0.035,
    "Assumptions: 30 × 96 ft greenhouse; 64% estimated growing area; "
    "equal space per vegetable.",
    ha="center",
    fontsize=9
)

fig.text(
    0.5, 0.01,
    "Source: Goda et al. (2015), Table 2, page 531. "
    "Production rates applied to estimated growing area.",
    ha="center",
    fontsize=9
)

# 12. Adjust layout and save graph

plt.tight_layout(rect=[0, 0.12, 1, 1])

plt.savefig(
    "Graph6_Greenhouse_Projections.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()