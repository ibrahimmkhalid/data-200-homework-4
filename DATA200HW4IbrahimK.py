import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("./Real_estate.csv")
df_readable = df[["No",
                  "house_age",
                  "distance_to_the_nearest_MRT_station",
                  "number_of_convenience_stores",
                  "house_price_of_unit_area"]]

df_readable = df_readable.rename(columns={
    "No": "Transaction Number",
    "house_age": "Age (years)",
    "distance_to_the_nearest_MRT_station": "Distance to MRT station (meters)",
    "number_of_convenience_stores": "Number of convenience stores",
    "house_price_of_unit_area": "Price per unit area",
})

df_readable.head()

fig, ax = plt.subplots()
def conv_age_to_year(x): return int(2023 - x)

ax.scatter(list(map(conv_age_to_year, df.house_age)),
           df.distance_to_the_nearest_MRT_station)
ax.set_xlabel("Year house built in")
ax.set_ylabel("Distance from the nearest MRT station (Meters)")

st.write("Here is some interesting data about some real estate properties")
st.write(df_readable.head())
st.write("Below is a graph that showcases the trend between the distance of a house from the MRT station over time")
st.pyplot(fig)