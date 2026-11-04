"""Task 3: Evaluate the student performance model and make predictions."""

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split


def main():
    data = {
        "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "Score": [35, 45, 48, 52, 60, 68, 75, 82, 88, 95],
    }
    df = pd.DataFrame(data)

    X = df[["Hours"]]
    y = df["Score"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    print(f"Mean Absolute Error: {mae:.2f} points")

    results = pd.DataFrame(
        {
            "Actual": y_test.to_numpy(),
            "Predicted": y_pred.round(2),
        },
        index=X_test.index,
    ).sort_index()
    print("\nActual vs. predicted test scores:")
    print(results)

    new_student = pd.DataFrame({"Hours": [4.5]})
    predicted_score = model.predict(new_student)[0]
    print(f"\nPredicted score for 4.5 study hours: {predicted_score:.2f}")


if __name__ == "__main__":
    main()
