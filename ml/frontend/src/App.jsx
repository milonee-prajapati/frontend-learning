import { useState } from "react";
import "./App.css";

function App() {

  const [formData, setFormData] = useState({
    attendance: "",
    study_hours: "",
    previous_score: "",
    assignment_score: "",
    assignments_completed: ""
  });

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");


  // ==========================================
  // HANDLE INPUT CHANGES
  // ==========================================

  const handleChange = (event) => {

    const { name, value } = event.target;

    setFormData({
      ...formData,
      [name]: value
    });

  };


  // ==========================================
  // SEND DATA TO FASTAPI
  // ==========================================

  const predictPerformance = async (event) => {

    event.preventDefault();

    setLoading(true);
    setError("");
    setResult(null);


    try {

      const response = await fetch(
        "https://frontend-learning-gq78.onrender.com/predict",
        {
          method: "POST",

          headers: {
            "Content-Type": "application/json"
          },

          body: JSON.stringify({
            attendance: Number(formData.attendance),
            study_hours: Number(formData.study_hours),
            previous_score: Number(formData.previous_score),
            assignment_score: Number(formData.assignment_score),
            assignments_completed: Number(
              formData.assignments_completed
            )
          })
        }
      );


      if (!response.ok) {
        throw new Error("Prediction request failed.");
      }


      const data = await response.json();

      setResult(data);

    } catch (error) {

      setError(
        "Could not connect to the AI server. Make sure FastAPI is running."
      );

    } finally {

      setLoading(false);

    }

  };


  return (

    <div className="app">

      <div className="container">

        <header>

          <h1>
            🎓 AI Student Performance Predictor
          </h1>

          <p>
            Predict academic performance using Machine Learning
          </p>

        </header>


        {/* =====================================
            STUDENT FORM
        ====================================== */}

        <form
          className="student-form"
          onSubmit={predictPerformance}
        >

          <div className="form-group">

            <label>
              Attendance (%)
            </label>

            <input
              type="number"
              name="attendance"
              min="0"
              max="100"
              value={formData.attendance}
              onChange={handleChange}
              required
            />

          </div>


          <div className="form-group">

            <label>
              Study Hours Per Day
            </label>

            <input
              type="number"
              name="study_hours"
              min="0"
              max="24"
              step="0.1"
              value={formData.study_hours}
              onChange={handleChange}
              required
            />

          </div>


          <div className="form-group">

            <label>
              Previous Exam Score
            </label>

            <input
              type="number"
              name="previous_score"
              min="0"
              max="100"
              step="0.1"
              value={formData.previous_score}
              onChange={handleChange}
              required
            />

          </div>


          <div className="form-group">

            <label>
              Assignment Score
            </label>

            <input
              type="number"
              name="assignment_score"
              min="0"
              max="100"
              step="0.1"
              value={formData.assignment_score}
              onChange={handleChange}
              required
            />
          </div>
          <div className="form-group">
            <label>
              Assignments Completed
            </label>
            <input
              type="number"
              name="assignments_completed"
              min="0"
              max="10"
              value={formData.assignments_completed}
              onChange={handleChange}
              required
            />
          </div>
          <button
            type="submit"
            disabled={loading}
          >
            {loading
              ? "Analyzing..."
              : "Predict Performance"
            }
          </button>
        </form>

        {/* =====================================
            ERROR
        ====================================== */}

        {error && (
          <div className="error">
            {error}
          </div>
        )}

        {/* =====================================
            RESULTS
        ====================================== */}

        {result && (
          <div className="results">
            <h2>
              📊 Student Performance Report
            </h2>
            <div className="score">
              <span>
                Predicted Final Score
              </span>
              <strong>
                {result.predicted_score}
              </strong>
            </div>
            <div className="result-row">
              <div>
                <span>
                  Performance
                </span>
                <strong>
                  {result.performance}
                </strong>
              </div>
              <div>
                <span>
                  Risk Level
                </span>
                <strong>
                  {result.risk}
                </strong>
              </div>
            </div>
            <div className="recommendations">
              <h3>
                🤖 AI Recommendations
              </h3>
              <ul>
                {result.recommendations.map(
                  (recommendation, index) => (
                    <li key={index}>
                      {recommendation}
                    </li>
                  )
                )}
              </ul>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;