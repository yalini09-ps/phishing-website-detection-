import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("dataset.csv")

# Features
features = ["length", "https", "has_at", "has_dash"]

X = data[features]
y = data["label"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create ML model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Test model
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", accuracy)


def predict_website(url):
    length = len(url)
    https = 1 if url.startswith("https://") else 0
    has_at = 1 if "@" in url else 0
    has_dash = 1 if "-" in url else 0

    features_data = [[length, https, has_at, has_dash]]

    prediction = model.predict(features_data)

    return prediction[0]


if __name__ == "__main__":

    url = input("Enter website URL: ")

    result = predict_website(url)

    print("Prediction:", result)