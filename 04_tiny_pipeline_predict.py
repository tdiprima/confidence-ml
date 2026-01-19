import joblib
import pandas as pd

# Load saved pipeline
pipeline = joblib.load("models/health_pipeline.joblib")

# New data to predict
new_people = pd.DataFrame([
    {"age": 25, "minutes_exercised": 45, "sleep_hours": 8},
    {"age": 55, "minutes_exercised": 10, "sleep_hours": 5},
])

pred = pipeline.predict(new_people)
proba = pipeline.predict_proba(new_people)  # A 2D array of prediction probabilities

print("=== Tiny Pipeline Predictions ===")
print(new_people)

print("\nPredictions (0=not healthy, 1=healthy):")
print(pred)

print("\nProbabilities [P(0), P(1)]:")
print(proba)
