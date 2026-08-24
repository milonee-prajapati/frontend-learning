import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score


# ==========================================
# 1. LOAD DATASET
# ==========================================

df = pd.read_csv("dataset.csv")

print("Dataset loaded successfully!")
print("Number of students:", len(df))


# ==========================================
# 2. SELECT INPUT FEATURES
# ==========================================

X = df[
    [
        "attendance",
        "study_hours",
        "previous_score",
        "assignment_score",
        "assignments_completed"
    ]
]


# ==========================================
# 3. SELECT TARGET
# ==========================================

y = df["final_score"]


# ==========================================
# 4. SPLIT DATA
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


print("\nTraining students:", len(X_train))
print("Testing students:", len(X_test))


# ==========================================
# 5. LINEAR REGRESSION
# ==========================================

linear_model = LinearRegression()

linear_model.fit(X_train, y_train)

linear_predictions = linear_model.predict(X_test)

linear_mae = mean_absolute_error(
    y_test,
    linear_predictions
)

linear_r2 = r2_score(
    y_test,
    linear_predictions
)


# ==========================================
# 6. RANDOM FOREST
# ==========================================

random_forest_model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

random_forest_model.fit(
    X_train,
    y_train
)

random_forest_predictions = random_forest_model.predict(X_test)

random_forest_mae = mean_absolute_error(
    y_test,
    random_forest_predictions
)

random_forest_r2 = r2_score(
    y_test,
    random_forest_predictions
)


# ==========================================
# 7. DISPLAY RESULTS
# ==========================================

print("\n==============================")
print("MODEL COMPARISON")
print("==============================")

print("\nLinear Regression")
print("MAE:", round(linear_mae, 2))
print("R2 Score:", round(linear_r2, 2))

print("\nRandom Forest")
print("MAE:", round(random_forest_mae, 2))
print("R2 Score:", round(random_forest_r2, 2))


# ==========================================
# 8. SELECT BEST MODEL
# ==========================================

if random_forest_mae < linear_mae:
    best_model = random_forest_model
    best_model_name = "Random Forest"
else:
    best_model = linear_model
    best_model_name = "Linear Regression"


print("\n==============================")
print("BEST MODEL:", best_model_name)
print("==============================")


# ==========================================
# 9. SAVE BEST MODEL
# ==========================================

joblib.dump(best_model, "model.pkl")

print("\nBest model saved as model.pkl")