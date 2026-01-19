import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# 1) Make the experiment reproducible
rng = np.random.default_rng(seed=42)

# 2) Create fake "hours studied"
n = 80
hours = rng.uniform(0, 10, size=n)

# 3) Create exam scores with noise
# True relationship: score = 50 + 5 * hours + random_noise
noise = rng.normal(0, 4, size=n)
score = 50 + 5 * hours + noise

# 4) Put into a dataframe (easier to inspect)
df = pd.DataFrame({"hours": hours, "score": score})

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

print("=== Steady Hand Regression ===")
print(f"Intercept (base score): {model.intercept_:.2f}")
print(f"Slope (points per hour): {model.coef_[0]:.2f}")
print(f"Mean Absolute Error: {mae:.2f}")

print("\nSample predictions:")
print(df.assign(pred_score=pred).head(10))
