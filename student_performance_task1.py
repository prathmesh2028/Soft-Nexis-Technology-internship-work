from pathlib import Path

code = '''"""
Project 1: Student Performance Predictor
Task 1: Load and Explore the Data

Goal:
Create a small dataset containing study hours and exam scores,
then inspect its structure and basic statistics.

Requirements:
    pip install pandas
"""

import pandas as pd


def main():
    # 1. Create a sample dataset
    data = {
        "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "Score": [35, 45, 48, 52, 60, 68, 75, 82, 88, 95],
    }

    # 2. Convert the dataset into a pandas DataFrame
    df = pd.DataFrame(data)

    # 3. Display the first five rows
    print("First 5 rows:")
    print(df.head())

    # 4. Display basic statistical information
    print("\\nData statistics:")
    print(df.describe())

    # 5. Check for missing values
    print("\\nMissing values:")
    print(df.isnull().sum())

    # 6. Display the mean, minimum, and maximum values
    print("\\nBasic data summary:")
    print(f"Average study hours: {df['Hours'].mean():.1f}")
    print(f"Average exam score: {df['Score'].mean():.1f}")
    print(f"Minimum study hours: {df['Hours'].min()}")
    print(f"Maximum study hours: {df['Hours'].max()}")
    print(f"Minimum exam score: {df['Score'].min()}")
    print(f"Maximum exam score: {df['Score'].max()}")


if __name__ == "__main__":
    main()
'''

path = Path("/mnt/data/student_performance_task1.py")
path.write_text(code, encoding="utf-8")
print(f"Created: {path}")
