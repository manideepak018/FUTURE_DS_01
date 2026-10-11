
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

# --------------------------------------------------
# Page configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Sales Analytics Dashboard",
    page_icon="📊",
    layout="wide",
)

PROJECT_DIR = Path(__file__).resolve().parent
DATA_PATH = (
    PROJECT_DIR
    / "data"
    / "processed"
    / "cleaned_sales_data.csv"
)

st.title("📊 Sales Analytics Dashboard")
st.caption(
    "Interactive analysis of sales, revenue, profit, "
    "products, and regional performance."
)

# --------------------------------------------------
# Load data
# --------------------------------------------------
@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    numeric_columns = [
        "Quantity",
        "Unit_Price",
        "Revenue",
        "Cost",
        "Profit",
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    return df.dropna(subset=["Date", "Revenue", "Profit"])


if not DATA_PATH.exists():
    st.error(f"Dataset not found: {DATA_PATH}")
    st.info(
        "Check that data/processed/cleaned_sales_data.csv "
        "exists in your project repository."
    )
    st.stop()

df = load_data(DATA_PATH)

if df.empty:
    st.error("The dataset contains no usable sales records.")
    st.stop()

# --------------------------------------------------
# Sidebar filters
# --------------------------------------------------
st.sidebar.header("Dashboard Filters")

min_date = df["Date"].min().date()
max_date = df["Date"].max().date()

date_range = st.sidebar.date_input(
    "Select date range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date,
)

if isinstance(date_range, (tuple, list)) and len(date_range) == 2:
    start_date, end_date = date_range
    filtered = df[
        df["Date"].dt.date.between(start_date, end_date)
    ].copy()
else:
    filtered = df[
        df["Date"].dt.date == date_range
    ].copy()

categories = sorted(filtered["Category"].dropna().unique())
selected_categories = st.sidebar.multiselect(
    "Product categories",
    options=categories,
    default=categories,
)

regions = sorted(filtered["Region"].dropna().unique())
selected_regions = st.sidebar.multiselect(
    "Regions",
    options=regions,
    default=regions,
)

filtered = filtered[
    filtered["Category"].isin(selected_categories)
    & filtered["Region"].isin(selected_regions)
]

if filtered.empty:
    st.warning("No records match these filters.")
    st.stop()

# --------------------------------------------------
# KPI cards
# --------------------------------------------------
total_revenue = filtered["Revenue"].sum()
total_profit = filtered["Profit"].sum()
total_orders = filtered["Order_ID"].nunique()
total_units = filtered["Quantity"].sum()
profit_margin = (
    total_profit / total_revenue * 100
    if total_revenue else 0
)

k1, k2, k3, k4, k5 = st.columns(5)

k1.metric("Total Revenue", f"${total_revenue:,.2f}")
k2.metric("Total Profit", f"${total_profit:,.2f}")
k3.metric("Unique Orders", f"{total_orders:,}")
k4.metric("Units Sold", f"{total_units:,.0f}")
k5.metric("Profit Margin", f"{profit_margin:.1f}%")

st.divider()

# --------------------------------------------------
# Revenue and profit trends
# --------------------------------------------------
st.subheader("Revenue & Profit Trends")

daily = (
    filtered.groupby("Date", as_index=False)
    .agg(
        Revenue=("Revenue", "sum"),
        Profit=("Profit", "sum"),
    )
    .sort_values("Date")
)

trend = px.line(
    daily,
    x="Date",
    y=["Revenue", "Profit"],
    markers=True,
    title="Daily Revenue and Profit",
    labels={"value": "Amount ($)", "variable": "Metric"},
    template="plotly_white",
)
st.plotly_chart(trend, use_container_width=True)

# --------------------------------------------------
# Category and regional analysis
# --------------------------------------------------
left, right = st.columns(2)

with left:
    st.subheader("Performance by Category")

    category_data = (
        filtered.groupby("Category", as_index=False)
        .agg(
            Revenue=("Revenue", "sum"),
            Profit=("Profit", "sum"),
        )
        .sort_values("Revenue", ascending=False)
    )

    category_chart = px.bar(
        category_data,
        x="Category",
        y="Revenue",
        color="Profit",
        title="Revenue by Category",
        color_continuous_scale="Teal",
        template="plotly_white",
    )
    st.plotly_chart(category_chart, use_container_width=True)

with right:
    st.subheader("Performance by Region")

    region_data = (
        filtered.groupby("Region", as_index=False)
        .agg(
            Revenue=("Revenue", "sum"),
            Profit=("Profit", "sum"),
        )
        .sort_values("Revenue", ascending=False)
    )

    region_chart = px.bar(
        region_data,
        x="Region",
        y="Revenue",
        color="Profit",
        title="Revenue by Region",
        color_continuous_scale="Viridis",
        template="plotly_white",
    )
    st.plotly_chart(region_chart, use_container_width=True)

# --------------------------------------------------
# Top products
# --------------------------------------------------
st.subheader("Top Products by Revenue")

product_data = (
    filtered.groupby("Product", as_index=False)
    .agg(
        Revenue=("Revenue", "sum"),
        Profit=("Profit", "sum"),
        Units=("Quantity", "sum"),
    )
    .sort_values("Revenue", ascending=False)
)

st.dataframe(
    product_data.head(10).style.format({
        "Revenue": "${:,.2f}",
        "Profit": "${:,.2f}",
        "Units": "{:,.0f}",
    }),
    use_container_width=True,
    hide_index=True,
)

# --------------------------------------------------
# Raw records and CSV download
# --------------------------------------------------
with st.expander("Explore sales records"):
    st.dataframe(filtered, use_container_width=True, hide_index=True)

st.download_button(
    "Download filtered sales data",
    data=filtered.to_csv(index=False).encode("utf-8"),
    file_name="filtered_sales_data.csv",
    mime="text/csv",
)

st.caption(
    "Data source: project-generated sample sales dataset. "
    "Metrics reflect the selected filters."
)
