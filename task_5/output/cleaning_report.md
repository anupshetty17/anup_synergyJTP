# Cleaning Report

## 1. Dataset size

| | Rows | Columns |
|---|---|---|
| Before cleaning | 11 | 9 |
| After cleaning | 10 | 9 |

## 2. Duplicates

- Duplicate records removed: **1**
- Duplicate rows in raw data: 1
- Duplicate rows left after cleaning: 0

## 3. Missing and invalid values

Missing values in the raw data (blank cells):

- `attendance_percent`: 1
- `score`: 1
- `weight`: 1

Invalid values (found after converting to numbers, set to missing first):

- Attendance outside 0-100: ['S007', 'S008']
- Score outside 0-10: none
- Negative study hours: none

Values filled in with the median of the column:

- `attendance_percent`: student(s) ['S003', 'S007', 'S008'] filled with 88.0
- `score`: student(s) ['S009'] filled with 7.0
- `weight_kg`: student(s) ['S003'] filled with 58.0

## 4. Standardization decisions

- Domain names changed to: ML, Web Dev, Electronics, Mechanical.
- Submission status changed to: Submitted / Not Submitted.
- Attendance: removed the `%` sign and made it a number.
- Score and study hours: words like `nine` and `two` changed to numbers.
- Height changed to cm (values in metres were multiplied by 100).
- Weight changed to kg (the `kg` text was removed).

## 5. Validation checks

| Check | Result | Details |
|---|---|---|
| Student IDs unique and not missing | PASS | 0 missing, 0 repeated |
| Attendance between 0 and 100 | PASS | 0 rows outside the range |
| Domain is in the allowed list | PASS | 0 rows have a domain not in ['ML', 'Web Dev', 'Electronics', 'Mechanical'] |
| Submission status is in the allowed list | PASS | 0 rows have a status not in ['Submitted', 'Not Submitted'] |
| No missing values in critical columns | PASS | 0 missing values |
| Numeric columns have valid numbers | PASS | all numeric columns are fine |
| Score between 0 and 10 (extra check) | PASS | 0 rows outside the range |

7 of 7 checks passed.

## 6. Short summary

The raw data had 11 rows and the cleaned data has 10 rows. 1 duplicate row(s) were removed. Text numbers and units were fixed, invalid values were turned into missing, and missing numbers were filled with the column median. No rows were deleted to make validation pass.
