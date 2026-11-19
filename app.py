import streamlit as st

# Page configuration
st.set_page_config(
    page_title="ENG220 Agriculture Project",
    page_icon="🌱",
    layout="wide"
)

# Project title
st.title("ENG220 Team 21 Agriculture / Food Insecurity in Cuba")

st.write(
    "Team 21 is investigating food insecurity, food access, "
    "and agricultural production in Cuba, New Mexico."
)

st.divider()

# Project overview
st.header("Project Overview")

st.write(
    "This project examines food access in the Cuba Census County Division "
    "and explores how agricultural production methods, including aquaponics "
    "and greenhouse growing, may contribute to local food availability."
)

# Graph navigation
st.sidebar.title("Project Graphs")

graphs = {
    "Graph 1: Median Household Income":
        "Graph 1_Median Household Income/median_household_income.py",

    "Graph 2: Housing Units Without Vehicles":
        "Graph 2_Housing Without Vehicles/housing_without_vehicles.py",

    "Graph 3: Housing Units Receiving SNAP":
        "Graph 3_Housing Receiving SNAP/housing_receiving_snap.py",

    "Graph 4: Water Usage Comparison":
        "Graph 4_Water Usage Comparison/water_usage_comparison.py",

    "Graph 5: Aquaponics Vegetable Production":
        "Graph 5_Aquaponics Production/aquaponics_production.py",

    "Graph 6: Greenhouse Projections":
        "Graph 6_Greenhouse Projections/greenhouse_projection.py"
}

selected_graph = st.sidebar.selectbox(
    "Select a graph",
    list(graphs.keys())
)

# Display selected graph
st.header(selected_graph)

graph_path = (
    Path(__file__).resolve().parent
    / "Graphs"
    / graphs[selected_graph]
)

if graph_path.exists():
    runpy.run_path(str(graph_path))
else:
    st.error("The selected graph file could not be found.")
