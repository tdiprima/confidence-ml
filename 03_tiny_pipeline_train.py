from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# Paths
Path("models").mkdir(exist_ok=True)
Path("data").mkdir(exist_ok=True)

rng = np.random.default_rng(seed=42)

# 1) Generate dataset
n = 300
age = rng.integers(18, 70, size=n)
minutes_exercised = rng.normal(30, 15, size=n).clip(0, 120)
sleep_hours = rng.normal(7, 1.2, size=n).clip(3, 11)

# "Healthy" label rule: exercise + sleep good, age slightly harder
health_score = (minutes_exercised * 0.05) + (sleep_hours * 1.5) - (age * 0.03)
healthy = (health_score > 10).astype(int)

df = pd.DataFrame({
    "age": age,
    "minutes_exercised": minutes_exercised,
    "sleep_hours": sleep_hours,
    "healthy": healthy
})

# Save dataset so it's inspectable
df.to_csv("data/health.csv", index=False)

# 2) Split
X = df[["age", "minutes_exercised", "sleep_hours"]]
y = df["healthy"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# 3) Build pipeline: scale -> model
pipeline = Pipeline([("scaler", StandardScaler()), ("model", LogisticRegression())])

# 4) Train
pipeline.fit(X_train, y_train)

# 5) Evaluate
pred = pipeline.predict(X_test)
acc = accuracy_score(y_test, pred)

print("=== Tiny Pipeline Training ===")
print(f"Test accuracy: {acc:.3f}")

# 6) Save full pipeline (preprocessing + model)
joblib.dump(pipeline, "models/health_pipeline.joblib")
print("Saved model to models/health_pipeline.joblib")
