import pandas as pd
import numpy as np

df = pd.read_csv(
    "data/IBM_Telco.csv"
)

# Cleaning
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

df["TotalCharges"] = df[
    "TotalCharges"
].fillna(
    df["TotalCharges"].median()
)

# Features

df["previous_month_bill"] = (
    df["MonthlyCharges"]
)

df["avg_bill_per_tenure"] = (
    df["TotalCharges"] /
    (df["tenure"] + 1)
)

addon_cols = [

    "OnlineSecurity",
    "OnlineBackup",
    "DeviceProtection",
    "TechSupport",
    "StreamingTV",
    "StreamingMovies"

]

df["addon_count"] = 0

for col in addon_cols:

    df["addon_count"] += (
        df[col] == "Yes"
    ).astype(int)

# Target creation

np.random.seed(42)

df["next_month_bill"] = (

    df["MonthlyCharges"]

    + np.random.normal(
        0,
        5,
        len(df)
    )

)

print(
    df[
        [
            "MonthlyCharges",
            "next_month_bill"
        ]
    ].head()
)

print(
    "\nShape:",
    df.shape
)