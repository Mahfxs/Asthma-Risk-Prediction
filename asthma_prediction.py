import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# -----------------------------
# Sample Air Pollution Dataset
# -----------------------------
data = {
    "PM2_5": [35, 70, 20],
    "NO2": [40, 55, 30],
    "Humidity": [60, 80, 50],
    "Asthma_Risk": [0, 1, 0]  # 1 = Asthma risk, 0 = No risk
}

# Convert to DataFrame
df = pd.DataFrame(data)

# -----------------------------
# Features (X) and Target (y)
# -----------------------------
X = df[["PM2_5", "NO2", "Humidity"]]
y = df["Asthma_Risk"]

# -----------------------------
# Train AI Model
# -----------------------------
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# -----------------------------
# Example Prediction
# -----------------------------
sample_input = [[50, 60, 70]]  # PM2.5, NO2, Humidity
prediction = model.predict(sample_input)

# Output result
if prediction[0] == 1:
    print("⚠️ High asthma risk detected")
else:
    print("✅ Low asthma risk")
