# 1. Importing libraries

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 2. Loading the raw Food Access Research Atlas data

df = pd.read_csv("Cuba_CCD_Food_Access_Raw.csv")

# 3. Filtering data for Sandoval County, New Mexico

sandoval_data = df[
    (df["State"] == "New Mexico") &
    (df["County"] == "Sandoval County")
].copy()

# 4. Displaying Sandoval County census tract numbers

print(sandoval_data["CensusTract"].tolist())

# 5. Checking the raw dataset columns

print(df.columns.tolist())

# The five census tracts were indentified through a geographic
# intersection analysis between Sandoval County census tracts
# and the Cuba Census County Division (CCD) boundary.

# 6. These five census tracts that intersect Cuba CCD

cuba_tracts = [
    35043010722,
    35043010723,
    35043010900,
    35043011200,
    35043940900
]

food_access_analysis = sandoval_data[
    sandoval_data["CensusTract"].isin(cuba_tracts)
].copy()

# 7. Processing housing units without vehicles

no_vehicle = food_access_analysis["TractHUNV"].tolist()

# 8. Creating census tract labels

tract_labels = [
    "Tract 1",
    "Tract 2",
    "Tract 3",
    "Tract 4",
    "Tract 5"
]

geoids = [
    "35043010722",
    "35043010723",
    "35043010900",
    "35043011200",
    "35043940900"
]

# 9. Creating horizontal bar graph

fig, ax = plt.subplots(figsize=(11, 7))

colors = [
    "#C6DDED",
    "#9FC5DF",
    "#75A9D0",
    "#4F8DBB",
    "#286D9E"
]

bars = ax.barh(tract_labels, no_vehicle, color=colors, height=0.6)

# 10. Putting values at the end of each bar

for bar in bars:
    width = bar.get_width()

    ax.text(
        width + 2,
        bar.get_y() + bar.get_height() / 2,
        f"{int(width):,}",
        va="center",
        fontsize=11
    )

# 11. Adding title and axis labels

    ax.set_title(
        "Housing Units Without Vehicles by Census Tract",
        fontsize=15,
        pad=15
    )

    ax.set_xlabel("Number of Housing Units Without Vehicles", fontsize=11)
    ax.set_ylabel("Census Tract", fontsize=11)

# 12. Formatting graph

    ax.set_xlim(0, max(no_vehicle) + 20)

    ax.grid(axis="x", linestyle="--", alpha=0.4)

    ax.invert_yaxis()

# 13. Adding geographic notes and GEOID key

    fig.text(
        0.5, 0.12,
        "Note: Counts represent the full census tracts that intersect Cuba CCD, "
        "not just the portions within Cuba CCD.",
        ha="center",
        fontsize=9
    )

    geoid_text = "\n".join(
        [f"{label}: {geoid}" for label, geoid in zip(tract_labels, geoids)]
    )

    fig.text(
        0.5, 0.02,
        geoid_text,
        ha="center",
        fontsize=8
    )

# 14. Adjusting layout and saving the graph

    plt.tight_layout(rect=[0, 0.22, 1, 1])

    plt.savefig(
        "Graph2_Housing_Units_Without_Vehicles.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show ()