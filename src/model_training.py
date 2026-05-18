import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import mean_absolute_error

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

# Target

np.random.seed(42)

df["next_month_bill"] = (

    df["MonthlyCharges"]

    + np.random.normal(
        0,
        5,
        len(df)
    )

)

# Encoding

df = pd.get_dummies(
    df,
    drop_first=True
)

# Split

X = df.drop(
    "next_month_bill",
    axis=1
)

y = df[
    "next_month_bill"
]

X_train,X_test,y_train,y_test = (
    train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )
)

# Models

models = {

    "Linear Regression":
    LinearRegression(),

    "Random Forest":
    RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

}

# Training

for name,model in models.items():

    model.fit(
        X_train,
        y_train
    )

    pred = model.predict(
        X_test
    )

    mae = mean_absolute_error(
        y_test,
        pred
    )

    print(
        f"{name} MAE: {mae}"
    )