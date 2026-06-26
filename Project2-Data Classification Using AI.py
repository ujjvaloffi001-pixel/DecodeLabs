# ==========================================
# DecodeLabs Project 2
# Data Classification Using AI
# ==========================================

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# ------------------------------------------
# Load Dataset
# ------------------------------------------

file_name = "Dataset for Data Analytics.xlsx"

df = pd.read_excel(file_name)

print("=" * 60)
print("DATASET LOADED SUCCESSFULLY")
print("=" * 60)

print("\nFirst Five Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

# ------------------------------------------
# Remove unnecessary columns
# ------------------------------------------

df = df.drop(columns=[
    "OrderID",
    "CustomerID",
    "ShippingAddress",
    "TrackingNumber",
    "Date"
])

# ------------------------------------------
# Encode Categorical Columns
# ------------------------------------------

encoder = LabelEncoder()

for column in df.columns:
    if df[column].dtype == object:
        df[column] = encoder.fit_transform(df[column])

# ------------------------------------------
# Features and Target
# ------------------------------------------

X = df.drop("OrderStatus", axis=1)

y = df["OrderStatus"]

# ------------------------------------------
# Split Dataset
# ------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ------------------------------------------
# Train AI Model
# ------------------------------------------

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, y_train)

# ------------------------------------------
# Prediction
# ------------------------------------------

y_pred = model.predict(X_test)

# ------------------------------------------
# Evaluation
# ------------------------------------------

accuracy = accuracy_score(y_test, y_pred)

print("\n" + "=" * 60)
print("MODEL PERFORMANCE")
print("=" * 60)

print(f"\nAccuracy : {accuracy*100:.2f}%")

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

print("Confusion Matrix:\n")
print(confusion_matrix(y_test, y_pred))

print("\nModel Training Completed Successfully.")