from sklearn.ensemble import RandomForestClassifier

# Simple example for demonstration
X = [
    [75, 3, 1, 5, 0, 5, 200],
    [150, 6, 0, 12, 1, 15, 0],
]

y = [0, 1]  # 0 = Safe, 1 = Phishing

model = RandomForestClassifier()
model.fit(X, y)

def predict(features):
    prediction = model.predict([features])[0]
    probability = model.predict_proba([features])[0][1]
    return prediction, round(probability * 100, 2)
