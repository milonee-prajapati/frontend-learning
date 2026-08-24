import pandas as pd
import numpy as np

# Make the random data reproducible
np.random.seed(42)

# Number of students
number_of_students = 500

# Generate student information
attendance = np.random.uniform(50, 100, number_of_students)
study_hours = np.random.uniform(1, 8, number_of_students)
previous_score = np.random.uniform(40, 95, number_of_students)
assignment_score = np.random.uniform(40, 100, number_of_students)
assignments_completed = np.random.randint(3, 11, number_of_students)

# Generate final scores using the input features
noise = np.random.normal(0, 3, number_of_students)

final_score = (
    0.25 * attendance
    + 1.5 * study_hours
    + 0.35 * previous_score
    + 0.20 * assignment_score
    + 0.8 * assignments_completed
    + noise
)

# Keep scores between 0 and 100
final_score = np.clip(final_score, 0, 100)

# Create DataFrame
df = pd.DataFrame({
    "attendance": attendance.round(1),
    "study_hours": study_hours.round(1),
    "previous_score": previous_score.round(1),
    "assignment_score": assignment_score.round(1),
    "assignments_completed": assignments_completed,
    "final_score": final_score.round(1)
})

# Save dataset
df.to_csv("dataset.csv", index=False)

print("Dataset created successfully!")
print("Number of students:", len(df))
print("\nFirst 5 rows:")
print(df.head())