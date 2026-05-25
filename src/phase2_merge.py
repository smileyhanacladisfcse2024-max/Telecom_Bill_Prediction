import pandas as pd

crm = pd.read_csv(
    "data/telecom_iot_crm/crm/customer_profiles.csv"
)

billing = pd.read_csv(
    "data/telecom_iot_crm/revenue/billing_history.csv"
)

usage = pd.read_csv(
    "data/telecom_iot_crm/device/usage_metrics.csv"
)

merged = crm.merge(
    billing,
    on="customer_id"
)

merged = merged.merge(
    usage,
    on="customer_id"
)

merged["avg_usage_score"] = (
    merged["data_gb"]*0.6
    +
    merged["call_minutes"]*0.4/100
)

merged.to_csv(
    "outputs/phase2_merged.csv",
    index=False
)

print(
    merged.head()
)

print(
    "\nShape:",
    merged.shape
)