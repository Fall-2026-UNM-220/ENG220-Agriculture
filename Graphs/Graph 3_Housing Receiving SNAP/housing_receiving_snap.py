# 1. Import the libraries

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from pathlib import Path

# 2. Locate and load the original raw Food Access Research Atlas data

REPO_ROOT = Path(__file__).resolve().parents[2]

df = pd.read_csv(
    REPO_ROOT / "Cuba_CCD_Food_Access_Raw.csv"
)

# 3. Filter the data for Sandoval County, New Mexico

sandoval_data = df[
    (df["State"] == "New Mexico") &
    (df["County"] == "Sandoval County")
].copy()

# 4. Identify the five census tracts that intersect Cuba CCD

cuba_tracts = [
    35043010722,
    35043010723,
    35043010900,
    35043011200,
    35043940900
]

# 5. Organize the census tracts in the correct order

sandoval_data["CensusTract"] = pd.to_numeric(
    sandoval_data["CensusTract"]
)

food_access_analysis = (
    sandoval_data[
        sandoval_data["CensusTract"].isin(cuba_tracts)
    ]
    .set_index("CensusTract")
    .loc[cuba_tracts]
    .reset_index()
)

# 6. Identify the housing units receiving SNAP benefits

snap_units = pd.to_numeric(
    food_access_analysis["TractSNAP"]
).tolist()

# 7. Create census tract labels

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

# 8. Create the horizontal bar graph

fig, ax = plt.subplots(figsize=(11, 7))

colors = [
    "#C6DDED",
    "#9FC5DF",
    "#75A9D0",
    "#4F8DBB",
    "#286D9E"
]

bars = ax.barh(
    tract_labels,
    snap_units,
    color=colors,
    height=0.6
)

# 9. Add values at the end of each bar

for bar in bars:
    width = bar.get_width()

    ax.text(
        width + 15,
        bar.get_y() + bar.get_height() / 2,
        f"{int(width):,}",
        va="center",
        fontsize=11
    )

# 10. Add the title and axis labels

ax.set_title(
    "Housing Units Receiving SNAP Benefits by Census Tract",
    fontsize=15,
    pad=15
)

ax.set_xlabel(
    "Number of Housing Units Receiving SNAP",
    fontsize=11
)

ax.set_ylabel("Census Tract", fontsize=11)

# 11. Format the graph

ax.set_xlim(0, max(snap_units) + 100)

ax.grid(axis="x", linestyle="--", alpha=0.4)

ax.invert_yaxis()

# 12. Add geographic note and GEOID key

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

# 13. Adjust layout and save graph

plt.tight_layout(rect=[0, 0.22, 1, 1])

fig.savefig(
    Path(__file__).with_name(
        "Graph3_Housing_Units_Receiving_SNAP.png"
    ),
    dpi=300,
    bbox_inches="tight"
)

# 14. Display graph in Streamlit

st.pyplot(fig)

plt.close(fig)
