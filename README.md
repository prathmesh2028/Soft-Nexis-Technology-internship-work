# SoftNexis Technology Internship Tasks

This repository contains my work for the SoftNexis Technology internship. The tasks build a small **Student Performance Predictor** project, starting with exploring study-hours and exam-score data, then training and evaluating a linear regression model.

## Project overview

The sample dataset contains 10 study-hour and exam-score pairs. The scripts use `Hours` as the input feature and `Score` as the target.

| Folder | Task | What it does |
|---|---|---|
| `Task_1/` | Load and explore the data | Creates the sample dataset, displays its rows, checks for missing values, and prints descriptive statistics. |
| `Task_2/` | Train a linear regression model | Splits data into training and test sets, trains a model, reports the slope and intercept, and makes predictions. |
| `Task_3/` | Evaluate and make predictions | Calculates Mean Absolute Error (MAE), compares actual and predicted test scores, and predicts a score for 4.5 study hours. |

## Repository structure

```text
.
├── Task_1/
│   └── student_performance_task1.py
├── Task_2/
│   └── linear_regression.py
├── Task_3/
│   └── evaluate_predictions.py
└── README.md
```

## Requirements

- Python
- pandas
- scikit-learn

Install the required packages:

```bash
python -m pip install pandas scikit-learn
```

## Run the tasks

Run each script from the repository root:

```bash
python Task_1/student_performance_task1.py
python Task_2/linear_regression.py
python Task_3/evaluate_predictions.py
```

## Sample results

With the included dataset and fixed train/test split, Task 2 reports a slope of approximately `6.78` and an intercept of approximately `27.06`. Task 3 reports an MAE of approximately `2.25` points and predicts a score of approximately `57.59` for 4.5 study hours.

## Notes

This is a small educational example intended to demonstrate basic data exploration, train/test splitting, linear regression, and model evaluation. Its predictions are based only on the sample data and should not be treated as real-world student performance assessments.
