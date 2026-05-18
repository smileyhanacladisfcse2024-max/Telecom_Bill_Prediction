import pandas as pd

df = pd.read_csv(
    "data/IBM_Telco.csv"
)

emails = []

for _, row in df.head(10).iterrows():

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

    email = f"""

Hello Customer {row['customerID']},

Your upcoming bill pattern shows changes in usage.

Recommended Offer:
{offer}

Activate now and enjoy additional telecom benefits.

Regards,
Telecom Team

"""

    emails.append(
        email
    )

df = df.head(10)

df["email"] = emails

print(

    df[
        [
            "customerID",
            "email"
        ]
    ]

)