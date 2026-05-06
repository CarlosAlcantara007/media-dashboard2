import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Media Dashboard")

uploaded_file = st.file_uploader("Upload CSV")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.write("Preview", df.head())

    numeric_cols = df.select_dtypes(include='number').columns
    cat_cols = df.select_dtypes(include='object').columns

    metric = st.selectbox("Metric", numeric_cols)
    dimension = st.selectbox("Dimension", cat_cols)

    grouped = df.groupby(dimension)[metric].sum().reset_index()

    fig = px.bar(grouped, x=dimension, y=metric)
    st.plotly_chart(fig, use_container_width=True)

    st.write("### Insights")

    top = grouped.sort_values(metric, ascending=False).iloc[0][dimension]
    st.write(f"Top performer: {top}")

    total = df[metric].sum()
    st.write(f"Total: {total:,.0f}")
``
