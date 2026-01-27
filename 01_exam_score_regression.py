"""
We generate fake data where:
more hours studied → higher exam score

Then we fit linear regression and print results.
"""
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# 1) Make the experiment reproducible
rng = np.random.default_rng(seed=42)

# 2) Create fake "hours studied"
n = 80  # 80 fake students
hours = rng.uniform(0, 10, size=n)  # For each of the 80 students, generate a random number between 0 and 10.

# Mini histogram (text-based)
counts, edges = np.histogram(hours, bins=10, range=(0, 10))

print("\nHours studied distribution (mini histogram):")
for i in range(len(counts)):
    left = edges[i]
    right = edges[i + 1]
    bar = "█" * counts[i]
    print(f"{left:>4.1f}-{right:>4.1f}: {bar} ({counts[i]})")

# 3) Create exam scores with noise
# For each student, add a random wiggle to their score.
noise = rng.normal(0, 4, size=n)  # Random score variation per student (mean 0, std 4)
score = 50 + 5 * hours + noise  # Score = baseline + hours effect + randomness

# 4) Put into a dataframe (easier to inspect)
df = pd.DataFrame({"hours": hours, "score": score})
print(df.head())

# 5) Choose features (X) and target (y)
X = df[["hours"]]  # 2D because sklearn expects rows x columns
y = df["score"]  # 1D target

# 6) Train model
model = LinearRegression()
model.fit(X, y)

# 7) Predict using same data (simple on purpose)
pred = model.predict(X)

# 8) Evaluate
mae = mean_absolute_error(y, pred)

print("=== Exam Score Regression ===")
print(f"Intercept (base score): {model.intercept_:.2f}")
print(f"Slope (points per hour): {model.coef_[0]:.2f}")
print(f"Mean Absolute Error: {mae:.2f}")

print("\nSample predictions:")
print(df.assign(pred_score=pred).head(10))
