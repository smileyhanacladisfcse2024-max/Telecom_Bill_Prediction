import streamlit as st
import pandas as pd

phase1 = pd.read_csv(
    "outputs/final_customer_scorecard.csv"
)

phase2 = pd.read_csv(
    "outputs/phase2_outreach.csv"
)

st.title(
    "📡 Telecom Enterprise Dashboard"
)

tab1, tab2 = st.tabs(
    [
        "Phase 1 - IBM Telco",
        "Phase 2 - Enterprise"
    ]
)

with tab1:

    st.header(
        "IBM Prototype"
    )

    st.metric(
        "Customers",
        len(phase1)
    )

    st.metric(
        "Bill Drop Customers",
        phase1["drop_flag"].sum()
    )

    st.dataframe(
        phase1.head(20)
    )

with tab2:

    st.header(
        "Enterprise Telecom"
    )

    st.metric(
        "Enterprise Customers",
        10000
    )

    st.metric(
        "Outreach Customers",
        len(phase2)
    )

    st.bar_chart(
        phase2["offer"].value_counts()
    )

    customer = st.selectbox(
        "Select Customer",
        phase2["customer_id"]
    )

    row = phase2[
        phase2["customer_id"]
        == customer
    ].iloc[0]

    st.write(
        "Predicted Bill:",
        row["predicted_bill"]
    )

    st.write(
        "Offer:",
        row["offer"]
    )

    st.text_area(
        "Generated Email",
        row["email"],
        height=200
    )