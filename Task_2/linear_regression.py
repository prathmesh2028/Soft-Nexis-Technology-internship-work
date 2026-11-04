# Project 1: Student Performance Predictor
# Task 2: Train a Linear Regression Model

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Create the dataset used by this model
data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Score": [35, 45, 48, 52, 60, 68, 75, 82, 88, 95]
}
df = pd.DataFrame(data)

# Separate input (X) and output (y)
X = df[["Hours"]]
y = df["Score"]

# Split the data: 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Display the learned slope and intercept
print("Slope (coefficient):", round(model.coef_[0], 2))
print("Intercept:", round(model.intercept_, 2))

# Predict scores for the testing data
y_pred = model.predict(X_test)

print("\nTesting data predictions:")
results = pd.DataFrame({
    "Hours Studied": X_test["Hours"].values,
    "Actual Score": y_test.values,
    "Predicted Score": y_pred.round(2)
})
print(results.sort_values("Hours Studied").to_string(index=False))

# Predict the score for a student who studies 7 hours
new_student = pd.DataFrame({"Hours": [7]})
predicted_score = model.predict(new_student)[0]
print("\nPredicted score for 7 study hours:", round(predicted_score, 2))