import pandas as pd

df = pd.read_csv(
    "data/IBM_Telco.csv"
)

offers = []

for _, row in df.iterrows():

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

df["recommended_offer"] = (
    offers
)

print(

    df[
        [
            "customerID",
            "MonthlyCharges",
            "tenure",
            "recommended_offer"
        ]
    ].head(10)

)