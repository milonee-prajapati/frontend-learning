import pandas as pd
import matplotlib.pyplot as plt
import joblib

from sklearn.model_selection import train_test_split


# ==========================================
# LOAD DATA
# ==========================================

df = pd.read_csv("dataset.csv")


# ==========================================
# GRAPH 1
# Study Hours vs Final Score
# ==========================================

plt.figure(figsize=(8, 5))

plt.scatter(
    df["study_hours"],
    df["final_score"]
)

plt.xlabel("Study Hours Per Day")
plt.ylabel("Final Score")
plt.title("Study Hours vs Final Score")

plt.grid(True)

plt.savefig("study_hours_vs_score.png")

plt.show()


# ==========================================
# GRAPH 2
# Attendance vs Final Score
# ==========================================

plt.figure(figsize=(8, 5))

plt.scatter(
    df["attendance"],
    df["final_score"]
)

plt.xlabel("Attendance (%)")
plt.ylabel("Final Score")
plt.title("Attendance vs Final Score")

plt.grid(True)

plt.savefig("attendance_vs_score.png")

plt.show()


# ==========================================
# GRAPH 3
# Assignment Score vs Final Score
# ==========================================

plt.figure(figsize=(8, 5))

plt.scatter(
    df["assignment_score"],
    df["final_score"]
)

plt.xlabel("Assignment Score")
plt.ylabel("Final Score")
plt.title("Assignment Score vs Final Score")

plt.grid(True)

plt.savefig("assignment_vs_score.png")

plt.show()


# ==========================================
# GRAPH 4
# Actual vs Predicted Score
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

y = df["final_score"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


model = joblib.load("model.pkl")

predictions = model.predict(X_test)


plt.figure(figsize=(8, 5))

plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    linestyle="--"
)

plt.xlabel("Actual Score")
plt.ylabel("Predicted Score")
plt.title("Actual vs Predicted Scores")

plt.grid(True)

plt.savefig("actual_vs_predicted.png")

plt.show()


print("All visualizations created successfully!")