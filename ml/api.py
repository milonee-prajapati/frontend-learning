from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import joblib


# ==========================================
# CREATE FASTAPI APP
# ==========================================

app = FastAPI(
    title="AI Student Performance Predictor",
    description="API for predicting student performance using Machine Learning",
    version="1.0"
)


# ==========================================
# ALLOW REACT TO CONNECT LATER
# ==========================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==========================================
# LOAD ML MODEL
# ==========================================

model = joblib.load("model.pkl")


# ==========================================
# INPUT DATA STRUCTURE
# ==========================================

class StudentData(BaseModel):

    attendance: float
    study_hours: float
    previous_score: float
    assignment_score: float
    assignments_completed: int


# ==========================================
# HOME ENDPOINT
# ==========================================

@app.get("/")
def home():

    return {
        "message": "AI Student Performance Predictor API is running!"
    }


# ==========================================
# HEALTH CHECK
# ==========================================

@app.get("/health")
def health():

    return {
        "status": "healthy",
        "model_loaded": True
    }


# ==========================================
# PREDICTION ENDPOINT
# ==========================================

@app.post("/predict")
def predict_student(data: StudentData):

    # Create DataFrame
    student = pd.DataFrame([
        {
            "attendance": data.attendance,
            "study_hours": data.study_hours,
            "previous_score": data.previous_score,
            "assignment_score": data.assignment_score,
            "assignments_completed": data.assignments_completed
        }
    ])


    # ======================================
    # ML PREDICTION
    # ======================================

    prediction = model.predict(student)

    score = float(prediction[0])

    # Keep score between 0 and 100
    score = max(0, min(100, score))


    # ======================================
    # PERFORMANCE LEVEL
    # ======================================

    if score >= 75:
        performance = "Good"

    elif score >= 50:
        performance = "Needs Improvement"

    else:
        performance = "At Risk"


    # ======================================
    # RISK ANALYSIS
    # ======================================

    risk_points = 0


    if data.attendance < 75:
        risk_points += 1

    if data.study_hours < 3:
        risk_points += 1

    if data.previous_score < 60:
        risk_points += 1

    if data.assignment_score < 70:
        risk_points += 1

    if data.assignments_completed < 6:
        risk_points += 1


    if score < 50:
        risk_points += 2

    elif score < 65:
        risk_points += 1


    # ======================================
    # RISK LEVEL
    # ======================================

    if risk_points <= 1:

        risk = "LOW RISK"

    elif risk_points <= 3:

        risk = "MEDIUM RISK"

    else:

        risk = "HIGH RISK"


    # ======================================
    # RECOMMENDATIONS
    # ======================================

    recommendations = []


    if data.attendance < 75:
        recommendations.append(
            "Improve attendance."
        )

    if data.study_hours < 3:
        recommendations.append(
            "Increase daily study time."
        )

    if data.previous_score < 60:
        recommendations.append(
            "Revise topics from previous exams."
        )

    if data.assignment_score < 70:
        recommendations.append(
            "Focus more on assignments."
        )

    if data.assignments_completed < 6:
        recommendations.append(
            "Complete assignments regularly."
        )


    if len(recommendations) == 0:

        recommendations.append(
            "Keep up your current study routine!"
        )


    # ======================================
    # RETURN JSON RESPONSE
    # ======================================

    return {

        "predicted_score": round(score, 2),

        "performance": performance,

        "risk": risk,

        "recommendations": recommendations

    }