import pandas as pd

df = pd.read_csv(
    "outputs/phase2_predictions.csv"
)

# bill drop
df["bill_drop"] = (
    df["previous_bill"]
    - df["predicted_bill"]
)

df["drop_flag"] = (
    df["bill_drop"] > -50
)

# offers
def offer_engine(row):

    if row["data_gb"] > 70:
        return "Unlimited Data Upgrade"

    elif row["plan_type_Postpaid"] == True:
        return "Postpaid Loyalty Pack"

    elif row["paid_status_Unpaid"] == True:
        return "Bill Reminder + Discount"

    else:
        return "Entertainment Add-on"

df["offer"] = df.apply(
    offer_engine,
    axis=1
)

# email generation
def mail(row):

    return f"""
Hello {row['customer_id']},

Your next bill is expected to reduce.

Recommended Offer:
{row['offer']}

Thank you,
Telecom Team
"""

df["email"] = df.apply(
    mail,
    axis=1
)

final = df[
    df["drop_flag"] == True
]

final.to_csv(
    "outputs/phase2_outreach.csv",
    index=False
)

print(
    final[
        [
            "customer_id",
            "predicted_bill",
            "bill_drop",
            "offer"
        ]
    ].head()
)

print(
    "\nBill drop customers:",
    len(final)
)