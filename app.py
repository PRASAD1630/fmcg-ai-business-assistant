import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------
# PAGE CONFIG
# -------------------------

st.set_page_config(
    page_title="FMCG AI Business Assistant",
    page_icon="🥤",
    layout="wide"
)

# -------------------------
# CUSTOM CSS
# -------------------------

st.markdown("""
<style>

.main {
    background-color: #f8fafc;
}

.metric-card {
    padding:15px;
    border-radius:10px;
}

h1,h2,h3 {
    color:#1e293b;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# HEADER
# -------------------------

st.markdown("""
<div style='padding:20px;
background:linear-gradient(90deg,#2563EB,#7C3AED);
border-radius:15px;'>

<h1 style='color:white;'>
🥤 FMCG AI Business Assistant
</h1>

<p style='color:white;'>
Sales • Inventory • Promotions • Analytics
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# -------------------------
# LOAD DATA
# -------------------------

sales = pd.read_csv("sales_promotions.csv")
inventory = pd.read_csv("inventory.csv")
products = pd.read_csv("product_master.csv")
stores = pd.read_csv("store_master.csv")

sales["week_start_date"] = pd.to_datetime(
    sales["week_start_date"]
)

sales_data = sales.merge(
    products,
    on="product_id"
)

# -------------------------
# SIDEBAR
# -------------------------

st.sidebar.title("📊 Dashboard")

menu = st.sidebar.radio(
    "Navigate",
    [
        "Executive Overview",
        "Sales Analytics",
        "Promotion Analytics",
        "Inventory Analytics",
        "Advanced Analytics"
    ]
)

# -------------------------
# OVERVIEW
# -------------------------

if menu == "Executive Overview":

    total_revenue = sales["revenue"].sum()
    total_units = sales["units_sold"].sum()
    total_products = products.shape[0]
    total_stores = stores.shape[0]

    c1,c2,c3,c4 = st.columns(4)

    c1.metric(
        "Revenue",
        f"₹{total_revenue:,.0f}"
    )

    c2.metric(
        "Units Sold",
        f"{total_units:,}"
    )

    c3.metric(
        "Products",
        total_products
    )

    c4.metric(
        "Stores",
        total_stores
    )

    st.markdown("---")

    trend = (
        sales.groupby(
            "week_start_date"
        )["revenue"]
        .sum()
        .reset_index()
    )

    fig = px.line(
        trend,
        x="week_start_date",
        y="revenue",
        markers=True,
        title="Revenue Trend"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    region = (
        sales.groupby("region")["revenue"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        region,
        x="region",
        y="revenue",
        title="Revenue by Region"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# -------------------------
# SALES ANALYTICS
# -------------------------

elif menu == "Sales Analytics":

    st.subheader(
        "Top Revenue Products"
    )

    top_products = (
        sales_data.groupby(
            "product_name"
        )["revenue"]
        .sum()
        .reset_index()
        .sort_values(
            "revenue",
            ascending=False
        )
        .head(10)
    )

    fig = px.bar(
        top_products,
        x="revenue",
        y="product_name",
        orientation="h",
        title="Top Products"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    category = (
        sales_data.groupby(
            "category"
        )["revenue"]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        category,
        names="category",
        values="revenue",
        hole=0.5,
        title="Category Revenue Share"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# -------------------------
# PROMOTION
# -------------------------

elif menu == "Promotion Analytics":

    promo = sales[
        sales["promotion_flag"] == 1
    ]

    promo_rev = (
        promo.groupby(
            "promotion_type"
        )["revenue"]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        promo_rev,
        names="promotion_type",
        values="revenue",
        hole=0.4,
        title="Promotion Revenue"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    fig = px.scatter(
        promo,
        x="discount_pct",
        y="revenue",
        color="region",
        title="Discount vs Revenue"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# -------------------------
# INVENTORY
# -------------------------

elif menu == "Inventory Analytics":

    stockouts = inventory[
        inventory["stockout_flag"] == True
    ]

    st.metric(
        "Stockout Records",
        len(stockouts)
    )

    st.dataframe(
        stockouts.head(100)
    )

    fig = px.histogram(
        inventory,
        x="closing_stock",
        title="Closing Stock Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# -------------------------
# ADVANCED
# -------------------------

elif menu == "Advanced Analytics":

    st.subheader(
        "Revenue Treemap"
    )

    fig = px.treemap(
        sales_data,
        path=[
            "category",
            "product_name"
        ],
        values="revenue"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader(
        "Sales Hierarchy"
    )

    fig = px.sunburst(
        sales_data,
        path=[
            "category",
            "product_name"
        ],
        values="units_sold"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    pivot = pd.pivot_table(
        sales_data,
        values="revenue",
        index="region",
        columns="category",
        aggfunc="sum"
    )

    fig = px.imshow(
        pivot,
        text_auto=True,
        title="Region vs Category Revenue"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# -------------------------
# FOOTER
# -------------------------

st.markdown("---")

st.caption(
    "Developed by Bhukya Prasad | FMCG AI Engineering Assessment"
)