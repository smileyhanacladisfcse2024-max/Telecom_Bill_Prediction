import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Telecom Bill Prediction",
    layout="wide"
)

df = pd.read_csv(
    "outputs/final_customer_scorecard.csv"
)

drop_df = df[
    df["drop_flag"] == True
]

st.title(
    "📡 Telecom Bill Prediction Dashboard"
)

c1,c2,c3 = st.columns(3)

c1.metric(
    "Customers",
    len(df)
)

c2.metric(
    "Bill Drop Customers",
    len(drop_df)
)

c3.metric(
    "Offers Generated",
    df["offer"].nunique()
)

st.subheader(
    "Customer Scorecard"
)

st.dataframe(
    df.head(20),
    use_container_width=True
)

st.subheader(
    "Bill Drop Customers"
)

st.dataframe(
    drop_df.head(20),
    use_container_width=True
)

st.bar_chart(
    df["offer"].value_counts()
)

st.subheader(
    "Generated Email"
)

customer = st.selectbox(
    "Customer",
    df["customerID"]
)

selected = df[
    df["customerID"]
    == customer
]

st.text_area(
    "Email",
    selected[
        "email"
    ].values[0],
    height=120
)

csv = df.to_csv(
    index=False
)

st.download_button(
    "Download Scorecard CSV",
    csv,
    "customer_scorecard.csv",
    "text/csv"
)