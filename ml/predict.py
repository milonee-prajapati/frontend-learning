import joblib
import pandas as pd


# ==========================================
# 1. LOAD TRAINED MODEL
# ==========================================

model = joblib.load("model.pkl")


# ==========================================
# 2. ENTER STUDENT INFORMATION
# ==========================================

attendance = float(input("Enter attendance percentage: "))
study_hours = float(input("Enter study hours per day: "))
previous_score = float(input("Enter previous exam score: "))
assignment_score = float(input("Enter assignment score: "))
assignments_completed = int(input("Enter assignments completed: "))


# ==========================================
# 3. CREATE STUDENT DATA
# ==========================================

student = pd.DataFrame([
    {
        "attendance": attendance,
        "study_hours": study_hours,
        "previous_score": previous_score,
        "assignment_score": assignment_score,
        "assignments_completed": assignments_completed
    }
])


# ==========================================
# 4. PREDICT FINAL SCORE
# ==========================================

prediction = model.predict(student)

score = float(prediction[0])

# Keep score between 0 and 100
score = max(0, min(100, score))


# ==========================================
# 5. PERFORMANCE LEVEL
# ==========================================

if score >= 75:
    performance = "Good"
elif score >= 50:
    performance = "Needs Improvement"
else:
    performance = "At Risk"


# ==========================================
# 6. RISK ANALYSIS
# ==========================================

risk_points = 0


if attendance < 75:
    risk_points += 1

if study_hours < 3:
    risk_points += 1

if previous_score < 60:
    risk_points += 1

if assignment_score < 70:
    risk_points += 1

if assignments_completed < 6:
    risk_points += 1


# Include predicted score
if score < 50:
    risk_points += 2
elif score < 65:
    risk_points += 1


# Determine risk level
if risk_points <= 1:
    risk = "LOW RISK"
    emoji = "🟢"

elif risk_points <= 3:
    risk = "MEDIUM RISK"
    emoji = "🟡"

else:
    risk = "HIGH RISK"
    emoji = "🔴"


# ==========================================
# 7. DISPLAY RESULT
# ==========================================

print("\n===================================")
print("       STUDENT PERFORMANCE REPORT")
print("===================================")

print(f"\nPredicted Final Score: {score:.2f}")

print(f"Performance: {performance}")

print(f"Risk Level: {emoji} {risk}")


# ==========================================
# 8. RECOMMENDATIONS
# ==========================================

print("\nAI Recommendations:")

recommendation_found = False


if attendance < 75:
    print("• Improve attendance.")
    recommendation_found = True

if study_hours < 3:
    print("• Increase daily study time.")
    recommendation_found = True

if previous_score < 60:
    print("• Revise topics from previous exams.")
    recommendation_found = True

if assignment_score < 70:
    print("• Focus more on assignments.")
    recommendation_found = True

if assignments_completed < 6:
    print("• Complete assignments regularly.")
    recommendation_found = True

if not recommendation_found:
    print("• Keep up your current study routine! 👍")