"""
We generate fake data where:
higher income + lower debt → "approved" loan

Then train logistic regression and evaluate.
"""
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Random Number Generator
rng = np.random.default_rng(seed=42)

n = 200

# Features
income = rng.normal(60000, 15000, size=n)  # dollars
debt = rng.normal(15000, 7000, size=n)  # dollars

# Rule (simple + interpretable):
# approved if income - 2*debt is high enough
score = income - 2 * debt

# Convert to probability-ish via threshold
approved = (score > 20000).astype(int)

df = pd.DataFrame({"income": income, "debt": debt, "approved": approved})

X = df[["income", "debt"]]
y = df["approved"]

model = LogisticRegression()
model.fit(X, y)

pred = model.predict(X)

print("=== Yes/No Classification ===")
print(f"Accuracy: {accuracy_score(y, pred):.3f}")
print("\nClassification report:")
print(classification_report(y, pred))

print("\nFirst 10 predictions:")
print(df.assign(pred_approved=pred).head(10))
