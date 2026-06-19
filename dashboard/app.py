import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(
    page_title="EV BATTERY ANALYTICS PLATFORM",
    layout="wide"
)

st.title("EV Battery Analytics Platform")

st.write(
    "This dashboard analyzes EV specifications and NASA battery degradation data."
)


st.sidebar.title("Navigation")
page = st.sidebar.selectbox(
    "Select Page",
    ["Battery Analytics", "EV Market Analytics"]
)

ev = pd.read_excel("C:/Users/nandi/OneDrive/Documents/academics/ev_battery_analytics/data/kaggle_dataset/electric_vehicles_specs_2025.csv.xlsx")

if page == "Battery Analytics":
    st.header("Battery Health Analytics")
    ## Load NASA battery data
    ml = pd.read_csv("data/nasa_dataset/ml_dataset.csv")

    # Clean invalid capacity values
    ml_clean = ml[ml["Capacity"] > 0]

    # Battery summary calculation
    battery_summary = []

    for battery in ml_clean["battery_id"].unique():
        temp = ml_clean[ml_clean["battery_id"] == battery].sort_values("test_id")

        initial_capacity = temp["Capacity"].max()
        final_capacity = temp["Capacity"].iloc[-1]
        final_soh = (final_capacity / initial_capacity) * 100

        battery_summary.append([
            battery,
            initial_capacity,
            final_capacity,
            final_soh
        ])

    summary_df = pd.DataFrame(
        battery_summary,
        columns=[
            "battery_id",
            "initial_capacity",
            "final_capacity",
            "final_soh"
        ]
    )
    display_summary = summary_df.copy()
    display_summary["initial_capacity"] = (
    display_summary["initial_capacity"].round(2))
    display_summary["final_capacity"] = (
    display_summary["final_capacity"].round(2))
    display_summary["final_soh"] = (
    display_summary["final_soh"].round(2))

    # KPI section
    st.subheader("Battery Health Overview")

    st.subheader("Top 5 Healthiest Batteries")
    st.dataframe(
        summary_df.sort_values("final_soh", ascending=False).head(5)
    )

    st.subheader("Top 5 Most Degraded Batteries")
    st.dataframe(
        summary_df.sort_values("final_soh").head(5)
    )
    st.divider()

    st.subheader("Average Battery SOH by Ambient Temperature")

    fig = px.histogram(
        summary_df,
        x="final_soh",
        nbins=15,
        title="Distribution of Final SOH"
    )
    st.plotly_chart(fig, use_container_width=True)
    st.divider()

    st.subheader("Top 10 Batteries by Final SOH")
    fig = px.bar(
        summary_df.sort_values("final_soh", ascending=False).head(10),
        x="battery_id",
        y="final_soh",
        title="Top 10 Battery Health Scores"
    )
    st.plotly_chart(fig, use_container_width=True)
    st.divider()

    st.subheader("Top 10 Most Degraded Batteries")
    fig = px.bar(
        summary_df.sort_values("final_soh").head(10),
        x="battery_id",
        y="final_soh",
        title="Most Degraded Batteries"
    )
    st.plotly_chart(fig, use_container_width=True)
    st.divider()

    battery = st.selectbox(
        "Select Battery",
        sorted(ml_clean["battery_id"].unique())
    )

    data = ml_clean[
        ml_clean["battery_id"] == battery
    ].sort_values("test_id")

    initial_capacity = data["Capacity"].max()
    final_capacity = data["Capacity"].iloc[-1]
    soh = (final_capacity / initial_capacity) * 100

    if soh >= 80:
        status = "🟢 Healthy"
    elif soh >= 60:
        status = "🟡 Moderate"
    else:
        status = "🔴 Replace Soon"

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Initial Capacity",
        f"{initial_capacity:.2f} Ah"
    )
    col2.metric(
        "Final Capacity",
        f"{final_capacity:.2f} Ah"
    )
    col3.metric(
        "Current SOH",
        f"{soh:.2f}%"
    )
    col4.metric(
        "Battery Status",
        status
    )

    fig = px.line(
        data,
        x="test_id",
        y="Capacity",
        title=f"Capacity Degradation - {battery}"
    )
    st.plotly_chart(fig, use_container_width=True)
    

    col1, col2, col3 = st.columns(3)
    col1.metric(
        "Initial Capacity",
        f"{initial_capacity:.2f} Ah"
    )
    col2.metric(
        "Final Capacity",
        f"{final_capacity:.2f} Ah"
    )
    col3.metric(
        "Current SOH",
        f"{soh:.2f}%"
    )

    data["SOH"] = (
        data["Capacity"] /
        data["Capacity"].max()
    ) * 100

    fig = px.line(
        data,
        x="test_id",
        y="SOH",
        title=f"SOH Trend - {battery}"
    )
    st.plotly_chart(fig, use_container_width=True)

    battery_temp = []
    for battery in ml_clean["battery_id"].unique():
        temp_data = ml_clean[ml_clean["battery_id"] == battery].sort_values("test_id")
        temperature = temp_data["ambient_temperature"].iloc[0]
        initial_capacity = temp_data["Capacity"].max()
        final_capacity = temp_data["Capacity"].iloc[-1]
        soh = (final_capacity / initial_capacity) * 100
        battery_temp.append([
            battery,
            temperature,
            soh
        ])

    temp_df = pd.DataFrame(
        battery_temp,
        columns=["battery_id", "temperature", "soh"]
    )
    temp_summary = temp_df.groupby("temperature")["soh"].mean().reset_index()
    temp_summary["temperature"] = temp_summary["temperature"].astype(str) + "°C"

    fig = px.bar(
        temp_summary,
        x="temperature",
        y="soh",
        title="Average SOH by Temperature"
    )
    st.plotly_chart(fig, use_container_width=True)

elif page == "EV Market Analytics":
    st.header("EV Market Analytics")
    st.subheader("EV Market Overview")
    st.write("This page analyzes EV specifications such as range, battery capacity, efficiency and vehicle segment.")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total EV Models", len(ev))
    col2.metric("Total Brands", ev["brand"].nunique())
    col3.metric("Average Range", f"{ev['range_km'].mean():.2f} km")
    col4.metric("Average Battery Capacity", f"{ev['battery_capacity_kWh'].mean():.2f} kWh")

    st.subheader("Top 10 Brands by Average Range")

    brand_range = (
        ev.groupby("brand")["range_km"]
        .mean()
        .reset_index()
        .sort_values("range_km", ascending=False)
        .head(10)
    )

    fig = px.bar(
        brand_range,
        x="brand",
        y="range_km",
        title="Top 10 Brands by Average Range"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Battery Capacity vs Driving Range")

    fig = px.scatter(
        ev,
        x="battery_capacity_kWh",
        y="range_km",
        color="brand",
        hover_data=["model"],
        title="Range vs Battery Capacity"
    )

    st.plotly_chart(fig, use_container_width=True)
    st.subheader("Top 10 Most Efficient Brands")
    efficiency = (ev.groupby("brand")["efficiency_wh_per_km"].mean().reset_index().sort_values("efficiency_wh_per_km").head(10))
    fig = px.bar(efficiency,x="brand",y="efficiency_wh_per_km",title="Top 10 Most Efficient Brands")
    st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("EV Count by Segment")
    segment_count = (ev["segment"].value_counts().reset_index())
    segment_count.columns = ["segment", "count"]
    fig = px.bar(
    segment_count,
    x="segment",
    y="count",
    title="EV Count by Segment")
    st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("Top Brands by Average Battery Capacity")
    battery_brand = (
    ev.groupby("brand")["battery_capacity_kWh"]
    .mean()
    .reset_index()
    .sort_values(
        "battery_capacity_kWh",
        ascending=False
    )
    .head(10))
    fig = px.bar(
    battery_brand,
    x="brand",
    y="battery_capacity_kWh",
    title="Top Brands by Average Battery Capacity")
    st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("Drivetrain Distribution")
    drive = (
    ev["drivetrain"]
    .value_counts()
    .reset_index())
    drive.columns = ["drivetrain", "count"]
    fig = px.pie(
    drive,
    names="drivetrain",
    values="count",
    title="EV Drivetrain Distribution")
    st.plotly_chart(fig, use_container_width=True)