
import streamlit as st
import runpy
from pathlib import Path

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Agriculture & Food Insecurity",
    page_icon="🌱",
    layout="wide"
)

REPO_ROOT = Path(__file__).resolve().parent

# --------------------------------------------------
# CUSTOM DESIGN
# --------------------------------------------------

st.markdown("""
<style>
    .stApp {
        background-color: #FFFFFF;
        color: #222222;
    }

    h1, h2, h3 {
        color: #344638;
    }

    .main-title {
        color: #344638;
        font-size: 42px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 5px;
    }

    .subtitle {
        color: #555555;
        font-size: 17px;
        text-align: center;
        margin-bottom: 20px;
    }

    .section-title {
        background-color: #EAF0E8;
        color: #344638;
        padding: 12px 14px;
        border-radius: 7px;
        font-size: 19px;
        font-weight: 650;
        margin-bottom: 12px;
    }

    .description {
        background-color: #F7F8F6;
        border-left: 4px solid #A5B59F;
        padding: 12px;
        border-radius: 5px;
        color: #333333;
        font-size: 14px;
        line-height: 1.5;
    }

    .source {
        color: #71866F;
        font-size: 13px;
        font-weight: 600;
        margin-top: 10px;
        line-height: 1.5;
    }

    .overview {
        background-color: #F8FAF7;
        padding: 18px 22px;
        border-radius: 8px;
        margin-bottom: 20px;
        font-size: 15px;
        line-height: 1.6;
    }

    hr {
        border-color: #DDE4DA;
    }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# PROJECT HEADER
# --------------------------------------------------

st.markdown(
    '<div class="main-title">Agriculture & Food Insecurity</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'A Data-Driven View of Food Access, Transportation, '
    'and Local Agriculture in Cuba, New Mexico'
    '</div>',
    unsafe_allow_html=True
)

st.divider()

# --------------------------------------------------
# PROJECT OVERVIEW
# --------------------------------------------------

st.markdown("## Project Overview")

st.markdown("""
<div class="overview">
This project examines access to affordable, nutritious food in Cuba,
New Mexico, and explores how local agriculture may relate to food
availability. Using data from the U.S. Census Bureau, USDA Food Access
Research Atlas, and agricultural research, we examine household income,
transportation access, SNAP participation, water use, aquaponics
production, and potential greenhouse production.
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# GRAPH INFORMATION, DESCRIPTIONS, AND SOURCES
# --------------------------------------------------

graphs = [
    {
        "title": "1. Median Household Income Comparison",
        "folder": "Graph 1_Median Household Income",
        "script": "median_household_income.py",
        "description": (
            "Compares median household income in Cuba CCD, New Mexico, "
            "and the United States. This provides economic context for "
            "understanding potential financial barriers to accessing "
            "affordable, nutritious food."
        ),
        "source": (
            "U.S. Census Bureau – American Community Survey (ACS)."
        )
    },
    {
        "title": "2. Housing Units Without Vehicles",
        "folder": "Graph 2_Housing Without Vehicles",
        "script": "housing_without_vehicles.py",
        "description": (
            "Shows housing units without vehicles across five census "
            "tracts that intersect Cuba CCD. We identified these tracts "
            "by comparing the Cuba CCD boundary with census tract "
            "boundaries. Counts represent the full tracts, not just "
            "the portions within Cuba CCD."
        ),
        "source": (
            "USDA Food Access Research Atlas; U.S. Census Bureau – "
            "TIGER/Line Shapefiles for census tract identification."
        )
    },
    {
        "title": "3. Housing Units Receiving SNAP Benefits",
        "folder": "Graph 3_Housing Receiving SNAP",
        "script": "housing_receiving_snap.py",
        "description": (
            "Shows housing units receiving SNAP benefits across the "
            "same five census tracts. The tracts were selected based "
            "on their geographic intersection with Cuba CCD. Counts "
            "represent the full tracts, not just the portions within "
            "Cuba CCD."
        ),
        "source": (
            "USDA Food Access Research Atlas; U.S. Census Bureau – "
            "TIGER/Line Shapefiles for census tract identification."
        )
    },
    {
        "title": "4. Water Usage Comparison",
        "folder": "Graph 4_Water Usage Comparison",
        "script": "water_usage_comparison.py",
        "description": (
            "Compares the water required to produce one kilogram of "
            "food using conventional agriculture and aquaponics. "
            "The comparison highlights the potential water-saving "
            "benefits of aquaponics where water resources are limited."
        ),
        "source": (
            "University of Colorado Denver (2017), research abstract, "
            "page 25."
        )
    },
    {
        "title": "5. Aquaponics Vegetable Production",
        "folder": "Graph 5_Aquaponics Production",
        "script": "aquaponics_production.py",
        "description": (
            "Compares reported production rates for cucumbers, "
            "tomatoes, and head lettuce in an aquaponics system, "
            "measured in kilograms per square meter alongside "
            "each crop's growing period."
        ),
        "source": (
            "Goda et al. (2015), Table 2, page 531."
        )
    },
    {
        "title": "6. Projected Greenhouse Vegetable Production",
        "folder": "Graph 6_Greenhouse Projections",
        "script": "greenhouse_projection.py",
        "description": (
            "Estimates potential production of lettuce, tomatoes, "
            "and cucumbers in a proposed greenhouse using its "
            "dimensions, estimated growing area, and research-based "
            "crop production rates."
        ),
        "source": (
            "Our team greenhouse projection assumptions and calculations, "
            "based on aquaponics production rates."
        )
    }
]

# --------------------------------------------------
# DISPLAY ALL SIX GRAPHS IN TWO COLUMNS
# --------------------------------------------------

st.divider()

for i in range(0, len(graphs), 2):

    left_column, right_column = st.columns(2, gap="large")

    for column, graph in zip(
        [left_column, right_column],
        graphs[i:i + 2]
    ):

        with column:

            with st.container(border=True):

                st.markdown(
                    f'<div class="section-title">'
                    f'{graph["title"]}'
                    f'</div>',
                    unsafe_allow_html=True
                )

                graph_path = (
                    REPO_ROOT
                    / "Graphs"
                    / graph["folder"]
                    / graph["script"]
                )

                if graph_path.exists():
                    runpy.run_path(str(graph_path))
                else:
                    st.error(
                        f"Could not find graph file: {graph_path}"
                    )

                st.markdown(
                    f'<div class="description">'
                    f'<strong>Description:</strong> '
                    f'{graph["description"]}'
                    f'</div>',
                    unsafe_allow_html=True
                )

                st.markdown(
                    f'<div class="source">'
                    f'Source: {graph["source"]}'
                    f'</div>',
                    unsafe_allow_html=True
                )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------


st.divider()

st.markdown("## Project Information")

st.markdown("""
**ENG220 – Team 21**

**Team Members:**
- Di’Jonai Ruffin
- Marissa Gomez
- Lauren Johnson
- Chloe Cortez
- Mwachofi waNgure

University of New Mexico

Agriculture & Food Insecurity in Cuba, New Mexico
""")
