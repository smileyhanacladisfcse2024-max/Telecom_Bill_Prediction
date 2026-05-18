import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression

# Load dataset

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

    df["TotalCharges"]

    /

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

# Target
np.random.seed(42)

usage_factor = (

    df["addon_count"] * 1.5

)

tenure_factor = (

    df["tenure"] * 0.05

)

contract_factor = np.where(

    df["Contract"] ==

    "Month-to-month",

    -3,

    2

)

noise = np.random.normal(
    0,
    2,
    len(df)
)

df["next_month_bill"] = (

    df["MonthlyCharges"]

    +

    usage_factor

    +

    tenure_factor

    +

    contract_factor

    +

    noise

)

customer_ids = df[
    "customerID"
]

encoded = pd.get_dummies(
    df,
    drop_first=True
)

X = encoded.drop(
    "next_month_bill",
    axis=1
)

y = encoded[
    "next_month_bill"
]

model = LinearRegression()

model.fit(X,y)

pred = model.predict(X)

df["predicted_bill"] = pred

# Bill drop

df["bill_drop"] = (

    df["previous_month_bill"]

    -

    df["predicted_bill"]

)

df["drop_flag"] = (

    df["bill_drop"]

    > 3

)

# Offers

offers = []

for _,row in df.iterrows():

    if row["tenure"] > 24:

        offer = (
            "Loyalty Discount Offer"
        )

    elif row[
        "InternetService"
    ] == "Fiber optic":

        offer = (
            "Premium Speed Upgrade"
        )

    elif row[
        "MonthlyCharges"
    ] < 50:

        offer = (
            "Entertainment Bundle"
        )

    else:

        offer = (
            "Standard Add-on Pack"
        )

    offers.append(
        offer
    )

df["offer"] = offers

# Email

df["email"] = (

    "Hello "

    +

    customer_ids

    +

    ", Offer: "

    +

    df["offer"]

)

final = df[

    [

        "customerID",

        "predicted_bill",

        "bill_drop",

        "drop_flag",

        "offer",

        "email"

    ]

]

final.to_csv(

    "outputs/final_customer_scorecard.csv",

    index=False

)

print(

    final.head()

)

print(

    "\nSaved successfully"

)