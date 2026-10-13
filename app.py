import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8")

st.title("Team 9 - Coffee Shop Staffing Dashboard")

st.caption(
    "For coffee shop store managers to decide which hours need more staff "
    "based on sales demand."
)

df = pd.read_csv("Coffee Shop Sales.csv")

df["transaction_date"] = pd.to_datetime(df["transaction_date"], format="%m/%d/%y")
df["transaction_time"] = pd.to_datetime(df["transaction_time"], format="%H:%M:%S").dt.time
df["hour"] = pd.to_datetime(df["transaction_time"].astype(str)).dt.hour
df["sales"] = df["transaction_qty"] * df["unit_price"]

min_date = df["transaction_date"].min().date()
max_date = df["transaction_date"].max().date()

st.sidebar.header("Filters")

store_filter = st.sidebar.multiselect(
    "Store Location",
    sorted(df["store_location"].unique()),
    sorted(df["store_location"].unique()),
)

category_filter = st.sidebar.multiselect(
    "Product Category",
    sorted(df["product_category"].unique()),
    sorted(df["product_category"].unique()),
)

date_filter = st.sidebar.date_input(
    "Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date,
)

filtered_df = df[
    (df["store_location"].isin(store_filter))
    & (df["product_category"].isin(category_filter))
]

if len(date_filter) == 2:
    start_date, end_date = date_filter
    filtered_df = filtered_df[
        (filtered_df["transaction_date"].dt.date >= start_date)
        & (filtered_df["transaction_date"].dt.date <= end_date)
    ]

st.write(
    "Data period: Jan 1, 2023 - Jun 30, 2023. Kaggle snapshot. "
    "In production, sales data should refresh nightly, and store managers "
    "should review the dashboard weekly before creating staff schedules."
)

total_sales = filtered_df["sales"].sum()
sales_records = len(filtered_df)

open_hours = filtered_df[["transaction_date", "store_location", "hour"]].drop_duplicates()
avg_records_per_open_hour = sales_records / len(open_hours) if len(open_hours) > 0 else 0

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"${total_sales:,.0f}")
col2.metric("Sales Records", f"{sales_records:,}")
col3.metric("Avg Records per Open Hour", f"{avg_records_per_open_hour:.1f}")

st.subheader("Hourly Demand")

hourly_demand = (
    filtered_df.groupby("hour")
    .size()
    .reindex(range(24), fill_value=0)
)

fig, ax = plt.subplots(figsize=(10, 4))
hourly_demand.plot(kind="bar", ax=ax)
ax.set_xlabel("Hour of Day")
ax.set_ylabel("Number of Sales Records")
ax.set_title("Sales Records by Hour")
st.pyplot(fig)

st.subheader("Sales by Product Category")

category_sales = (
    filtered_df.groupby("product_category")["sales"]
    .sum()
    .sort_values(ascending=False)
)

fig, ax = plt.subplots(figsize=(10, 4))
category_sales.plot(kind="bar", ax=ax)
ax.set_xlabel("Product Category")
ax.set_ylabel("Sales")
ax.set_title("Sales by Product Category")
ax.tick_params(axis="x", rotation=45)
st.pyplot(fig)

st.subheader("Filtered Data Preview")

st.dataframe(
    filtered_df[
        [
            "transaction_date",
            "transaction_time",
            "store_location",
            "product_category",
            "product_type",
            "transaction_qty",
            "unit_price",
            "sales",
        ]
    ].head(100)
)
