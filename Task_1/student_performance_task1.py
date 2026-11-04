"""
Project 1: Student Performance Predictor
Task 1: Load and Explore the Data

Create a small dataset of study hours and exam scores, then inspect
the first few rows, check for missing values, and review summary statistics.
"""

import pandas as pd


def main():
    data = {
        "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "Score": [35, 45, 48, 52, 60, 68, 75, 82, 88, 95],
    }
    df = pd.DataFrame(data)
    print(df)
    print("First 5 rows:")
    print(df.head())

    print("\nMissing values:")
    print(df.isnull().sum())

    print("\nData statistics:")
    print(df.describe())


if __name__ == "__main__":
    main()
