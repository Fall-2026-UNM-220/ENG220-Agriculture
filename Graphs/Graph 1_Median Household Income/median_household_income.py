# 1. Importing libraries

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from pathlib import Path

# 2. Loading the Census data

REPO_ROOT = Path(__file__).resolve().parents[2]

df = pd.read_csv(
    REPO_ROOT / "Datasets" / "U.S. Census Bureau Economic Conditions_Raw.csv"
)

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

fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.bar(
    locations,
    income,
    yerr=margin_error,
    capsize=7,
    color=colors,
    width=0.6
)

# 7. Adding income labels

for bar, value, error in zip(bars, income, margin_error):

    ax.text(
        bar.get_x() + bar.get_width() / 2,
        value + error + 2200,
        f"${value:,.0f}",
        ha="center",
        fontsize=12,
        fontweight="bold"
    )

# 8. Adding graph title and axis labels

ax.set_title(
    "Median Household Income Comparison",
    fontsize=17,
    fontweight="bold"
)

ax.set_xlabel("Geographic Area")
ax.set_ylabel("Median Household Income ($)")

# 9. Formatting the y-axis

ax.set_ylim(0, 100000)

ax.set_yticks(
    np.arange(0, 100001, 20000)
)

ax.set_yticklabels(
    [f"${x:,.0f}" for x in np.arange(0, 100001, 20000)]
)

# 10. Adding gridlines

ax.grid(axis="y", linestyle="--", alpha=0.3)

ax.set_axisbelow(True)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)

fig.tight_layout()

# 11. Saving and displaying the graph

fig.savefig("Graph1_Median_Household_Income.png", dpi=300)

st.pyplot(fig)

plt.close(fig)
