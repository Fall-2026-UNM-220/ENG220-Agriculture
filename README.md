# Agriculture & Food Insecurity in Cuba, New Mexico
## About Our Project

Food insecurity can be affected by several factors, including household income, transportation, and access to grocery stores. Our project inspects these challenges in the Cuba community and explores aquaponics and greenhouse production as potential ways to support local food availability.

### Live App: https://eng220-agriculture-h6wfpk4csqfho28liwfye5.streamlit.app/

## Project Goals

- Examine economic conditions and food access challenges.
- Explore the potential of aquaponics as a water-efficient growing method.
- Present research findings through an interactive Streamlit dashboard.

## Dashboard Overview

The dashboard includes six visualizations:

1. Median Household Income:
   - Compares median household income in Cuba CCD, New Mexico, and the United States.
   - Highlights the differences in household income.

3. Housing Units Without Vehicles
   - Examines housing units without vehicles across five census tracts intersecting Cuba CCD
   - Explores transportation as a potential barrier to grocery access.

3. Housing Units Receiving SNAP
   - Shows housing units receiving SNAP benefits across the same five census tracts.
   - Provides additional context about food assistance in the area.

4. Water Usage Comparison
   - Compares water usage between conventional agriculture and aquaponics.
   - Examines the potential water-efficiency benefits of aquaponics.

5. Aquaponics Vegetable Production
   - Compares cucumber, tomato, and head lettuce production rates.
   - Includes production per square meter and growing periods.

6. Greenhouse Production Projections
   - Estimates potential vegetable production in a 30 × 96-foot greenhouse.
   - Uses aquaponics production rates to project lettuce, tomato, and cucumber yields.
  
## Repository Orginazation

```
ENG220-Agriculture/
|
|-- Datasets/
|   |-- U.S. Census Bureau Economic Conditions_Raw.csv
|   |-- Cuba_CCD_Food_Access_Cleaned.csv
|   |-- Sources.md
|   |-- README.md
|
|-- Graphs/
|   |-- Graph 1_Median Household Income/
|   |-- Graph 2_Housing Without Vehicles/
|   |-- Graph 3_Housing Receiving SNAP/
|   |-- Graph 4_Water Usage Comparison/
|   |-- Graph 5_Aquaponics Production/
|   |-- Graph 6_Greenhouse Projections/
|
|-- app.py
|-- requirements.txt
|-- README.md
```
## Running the Dashboard
Requirements:
  - Python 3.9 or newer
  - Required packages listed in requirements.txt

## Data Sources

The project uses information from the following sources:

  - U.S. Census Bureau – American Community Survey (ACS): Median household income.

  - USDA Food Access Research Atlas: Housing units without vehicles and housing units receiving SNAP.

  -  U.S. Census Bureau – TIGER/Line Shapefiles: Census tract boundaries used to identify the five tracts intersecting Cuba CCD.

  - University of Colorado Denver (2017): Water usage comparison between conventional agriculture and aquaponics.

  - Goda et al. (2015): Aquaponics vegetable production rates for cucumbers, tomatoes, and head lettuce.

## Data Limitations

- Housing and SNAP values represent entire census tracts, not only the portions within Cuba CCD.

- The five census tracts were identified using Census Bureau TIGER/Line boundary files.

- Published aquaponics production rates vary under different growing conditions.

- Greenhouse production figures are based on assumption.

- Projected crop production represents the crops' respective growing cycles, not monthly harvests.

## Team 21 Roles

| Team Member | Responsibilities |
|---|---|
| Marissa Gomez (PM) | Project Management, Allocate Roles, Finalize Slides |
| Di’Jonai Ruffin | StreamLit, Data Cleaning, Visuals |
| Lauren Johnson | Satellite Data Sourcing, GitHub Management |
| Chloe Cortez | GitHub, Slides, Aquaponics Research |
| Mwachofi waNgure | Aquaponics Research And Proposal, Slides |

## Course Information
Course: ENG220 – Peace Engineering

Institution: University of New Mexico

Semester: Fall 2026

Project Title: Agriculture & Food Insecurity in Cuba, New Mexico
