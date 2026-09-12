import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

from feature_extraction import extract_features


# Load dataset
data = pd.read_csv("backend/dataset.csv")

print("Dataset loaded successfully!")
print("Total URLs:", len(data))


# Extract features
X = []

for url in data["url"]:
    features = extract_features(url)
    X.append(list(features.values()))


# Target labels
y = data["label"]


# Convert features into DataFrame
X = pd.DataFrame(X)


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# Create Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# Train model
print("\nTraining Random Forest model...")

model.fit(X_train, y_train)

print("Training completed!")


# Test model
predictions = model.predict(X_test)


# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("\nModel Accuracy:", round(accuracy * 100, 2), "%")


# Detailed report
print("\nClassification Report:")
print(classification_report(
    y_test,
    predictions,
    target_names=["Legitimate", "Phishing"]
))


# Save model
joblib.dump(model, "backend/phishing_model.pkl")

print("\nModel saved successfully!")
print("File: backend/phishing_model.pkl")