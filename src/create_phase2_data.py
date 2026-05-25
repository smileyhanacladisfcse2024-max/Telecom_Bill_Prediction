import pandas as pd
import numpy as np

n = 10000

customers = pd.DataFrame({
    "customer_id":[f"CUST{i}" for i in range(n)],
    "operator":np.random.choice(
        ["Airtel","Jio","Vi","BSNL"],
        n
    ),
    "plan_type":np.random.choice(
        ["Prepaid","Postpaid"],
        n
    ),
    "tenure":np.random.randint(1,72,n)
})

billing = pd.DataFrame({
    "customer_id":customers["customer_id"],
    "previous_bill":np.random.randint(200,2000,n),
    "paid_status":np.random.choice(
        ["Paid","Unpaid"],
        n
    )
})

usage = pd.DataFrame({
    "customer_id":customers["customer_id"],
    "data_gb":np.random.randint(1,100,n),
    "call_minutes":np.random.randint(10,5000,n)
})

customers.to_csv(
    "data/telecom_iot_crm/crm/customer_profiles.csv",
    index=False
)

billing.to_csv(
    "data/telecom_iot_crm/revenue/billing_history.csv",
    index=False
)

usage.to_csv(
    "data/telecom_iot_crm/device/usage_metrics.csv",
    index=False
)

print("Phase 2 telecom dataset created")