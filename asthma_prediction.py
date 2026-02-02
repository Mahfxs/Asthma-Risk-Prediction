import pandas as pd
from sklearn.ensemble import RandomForestClassifier
data = {
    'PM2.5': [35, 70, 20],
    'NO2': [40, 55, 30],
    'Humidity': [60, 80, 50],
    'Asthma': [0, 1, 0]  # Target variable
}

df = pd.DataFrame(data)
# Features and target
X = df[['PM2.5', 'NO2', 'Humidity']]
y = df['Asthma']

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Example prediction
sample_input = [[50, 60, 70]]  # Replace with your own values
prediction = model.predict(sample_input)
print("Predicted asthma risk:", prediction[0])
