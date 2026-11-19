# 1. Importing libraries

import pandas as pd
import matplotlib

matplotlib.use("TkAgg")

import matplotlib.pyplot as plt
import numpy as np

# 2. Loading the Census data

df = pd.read_csv("U.S. Census Bureau Economic Conditions_Raw.csv")

# 3. Finding the median income row

median_row = df[
    df["Label (Grouping)"].str.strip() == "Median income (dollars)"
].iloc[0]

# 4. Setting up the graph data

locations = ["Cuba CCD", "New Mexico", "United States"]

income = [31899, 64059, 80734]

margin_error = [4981, 808, 166]

# 5. Graphing colors

colors = ["#168C9B", "#4169A1", "#8AADD0"]

# 6. Creating the bar graph

plt.figure(figsize=(10, 6))

bars = plt.bar(
    locations,
    income,
    yerr=margin_error,
    capsize=7,
    color=colors,
    width=0.6
)

# 7. Adding income labels

for bar, value, error in zip(bars, income, margin_error):

    plt.text(
        bar.get_x() + bar.get_width() / 2,
        value + error + 2200,
        f"${value:,.0f}",
        ha="center",
        fontsize=12,
        fontweight="bold"
    )

# 8. Adding graph title and axis labels

plt.title(
    "Median Household Income Comparison",
    fontsize=17,
    fontweight="bold"
)

plt.xlabel("Geographic Area")

plt.ylabel("Median Household Income ($)")

# 9. Formating the y-axis

plt.ylim(0, 100000)

plt.yticks(
    np.arange(0, 100001, 20000),
    [f"${x:,.0f}" for x in np.arange(0, 100001, 20000)]
)

# 10. Adding gridlines

plt.grid(axis="y", linestyle="--", alpha=0.3)

plt.gca().set_axisbelow(True)

plt.gca().spines["top"].set_visible(False)

plt.gca().spines["right"].set_visible(False)

plt.gca().spines["left"].set_visible(False)

plt.tight_layout()

# 11. Save and display the graph

plt.savefig("Graph1_Median_Household_Income.png", dpi=300)

plt.show()