# Task 5 - Student Data Cleaning, Validation and Visualization

In this task I took a messy student csv file and cleaned it using Python and Pandas.
After cleaning I checked the data with some rules, made 3 plots with Matplotlib
and made the reports automatically from the results.

## Folder structure

```
task_5/
├── README.md
├── notes.md
├── data/
│   └── messy_students.csv
├── output/
│   ├── cleaned_students.csv
│   ├── summary_before.json
│   ├── summary_after.json
│   ├── cleaning_report.md
│   ├── plot_summary.md
│   ├── domain_average_score.png
│   ├── attendance_vs_score.png
│   └── submission_status_count.png
└── src/
    ├── clean_data.py
    ├── validate_data.py
    ├── visualize.py
    ├── reports.py
    └── main.py
```

## Setup

You need Python 3 and two libraries:

```
pip install pandas matplotlib
```

## How to run

Run this from the main `task_5` folder:

```
python src/main.py data/messy_students.csv output
```

It will do everything in one go: load the data, make summary before, clean,
validate, save the clean csv and summary after, make the 3 plots and write both reports.
If the output folder is not there it makes it.

## What each file does

- `src/clean_data.py` - all the cleaning functions (duplicates, domain names, % sign, words to numbers, cm and kg, missing values)
- `src/validate_data.py` - checks the clean data (unique ids, attendance 0-100, allowed domains, allowed submission values, no missing, numeric columns)
- `src/visualize.py` - makes the 3 plots
- `src/reports.py` - makes the json summaries and the markdown reports (I added this extra file to keep main.py short)
- `src/main.py` - runs everything in order

## Output files

- `cleaned_students.csv` - the clean data
- `summary_before.json` and `summary_after.json` - rows, columns, missing values, duplicates, data types, stats
- `cleaning_report.md` - what was cleaned and the validation results
- `plot_summary.md` - what the plots show
- `domain_average_score.png`, `attendance_vs_score.png`, `submission_status_count.png` - the plots

## Note

The reports are made by the code from the real data, so if the csv changes the reports change too.
More about my decisions is in `notes.md`.
