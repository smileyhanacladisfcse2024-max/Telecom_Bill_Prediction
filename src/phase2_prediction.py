import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

df = pd.read_csv(
    "outputs/phase2_merged.csv"
)

# create synthetic next bill target
df["next_bill"] = (
    df["previous_bill"]
    + df["data_gb"]*5
    + df["call_minutes"]*0.05
    + np.random.randint(
        -150,
        150,
        len(df)
    )
)

# encode categorical columns
df = pd.get_dummies(
    df,
    columns=[
        "operator",
        "plan_type",
        "paid_status"
    ]
)

X = df.drop(
    [
        "customer_id",
        "next_bill"
    ],
    axis=1
)

y = df["next_bill"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(
    X_train,
    y_train
)

pred = model.predict(
    X_test
)

print(
    "MAE:",
    mean_absolute_error(
        y_test,
        pred
    )
)

df["predicted_bill"] = model.predict(X)

df.to_csv(
    "outputs/phase2_predictions.csv",
    index=False
)

print(
    df[
        [
            "previous_bill",
            "predicted_bill"
        ]
    ].head()
)