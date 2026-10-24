# reports.py
# Makes the summary json files and the two markdown reports.
# Everything written in the reports comes from the real results, nothing is typed by hand.

import json
import pandas as pd


def make_summary(df):
    """Make a dictionary that describes the dataframe (rows, missing, dtypes, stats...)."""
    summary = {
        "rows": int(df.shape[0]),
        "columns": int(df.shape[1]),
        "column_names": list(df.columns),
        "missing_values": {c: int(v) for c, v in df.isna().sum().items()},
        "duplicate_rows": int(df.duplicated().sum()),
        "duplicate_student_ids": int(df["student_id"].duplicated().sum()),
        "data_types": {c: str(t) for c, t in df.dtypes.items()},
    }

    # stats only for columns that are really numeric
    numeric = df.select_dtypes(include="number")
    if not numeric.empty:
        summary["numeric_statistics"] = json.loads(numeric.describe().round(2).to_json())
    else:
        summary["numeric_statistics"] = "no numeric columns in this data (all are text)"

    # counts of the category columns
    summary["category_counts"] = {
        "domain": {str(k): int(v) for k, v in df["domain"].value_counts(dropna=False).items()},
        "submitted": {str(k): int(v) for k, v in df["submitted"].value_counts(dropna=False).items()},
    }
    return summary


def save_json(data, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, default=str)


def write_cleaning_report(path, before, after, log, results):
    lines = []
    lines.append("# Cleaning Report\n")

    lines.append("## 1. Dataset size\n")
    lines.append("| | Rows | Columns |")
    lines.append("|---|---|---|")
    lines.append(f"| Before cleaning | {before['rows']} | {before['columns']} |")
    lines.append(f"| After cleaning | {after['rows']} | {after['columns']} |\n")

    lines.append("## 2. Duplicates\n")
    lines.append(f"- Duplicate records removed: **{log['duplicates_removed']}**")
    lines.append(f"- Duplicate rows in raw data: {before['duplicate_rows']}")
    lines.append(f"- Duplicate rows left after cleaning: {after['duplicate_rows']}\n")

    lines.append("## 3. Missing and invalid values\n")
    lines.append("Missing values in the raw data (blank cells):\n")
    for col, n in before["missing_values"].items():
        if n > 0:
            lines.append(f"- `{col}`: {n}")
    lines.append("")
    lines.append("Invalid values (found after converting to numbers, set to missing first):\n")
    lines.append(f"- Attendance outside 0-100: {log['attendance_invalid_ids'] or 'none'}")
    lines.append(f"- Score outside 0-10: {log['score_invalid_ids'] or 'none'}")
    lines.append(f"- Negative study hours: {log['study_hours_invalid_ids'] or 'none'}\n")
    lines.append("Values filled in with the median of the column:\n")
    if log["imputed"]:
        for col, info in log["imputed"].items():
            lines.append(f"- `{col}`: student(s) {info['ids']} filled with {info['filled_with']}")
    else:
        lines.append("- nothing was filled")
    lines.append("")

    lines.append("## 4. Standardization decisions\n")
    lines.append("- Domain names changed to: ML, Web Dev, Electronics, Mechanical.")
    lines.append("- Submission status changed to: Submitted / Not Submitted.")
    lines.append("- Attendance: removed the `%` sign and made it a number.")
    lines.append("- Score and study hours: words like `nine` and `two` changed to numbers.")
    lines.append("- Height changed to cm (values in metres were multiplied by 100).")
    lines.append("- Weight changed to kg (the `kg` text was removed).\n")

    lines.append("## 5. Validation checks\n")
    lines.append("| Check | Result | Details |")
    lines.append("|---|---|---|")
    for r in results:
        status = "PASS" if r["passed"] else "FAIL"
        lines.append(f"| {r['check']} | {status} | {r['details']} |")
    failed = [r for r in results if not r["passed"]]
    lines.append("")
    lines.append(f"{len(results) - len(failed)} of {len(results)} checks passed.\n")

    lines.append("## 6. Short summary\n")
    lines.append(f"The raw data had {before['rows']} rows and the cleaned data has {after['rows']} rows. "
                 f"{log['duplicates_removed']} duplicate row(s) were removed. "
                 f"Text numbers and units were fixed, invalid values were turned into missing, "
                 f"and missing numbers were filled with the column median. "
                 f"No rows were deleted to make validation pass.")

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def write_plot_summary(path, df, plot_info, log):
    averages = plot_info["domain_averages"]
    counts = plot_info["submission_counts"]
    df_scatter = plot_info["df_scatter"]
    df_score = plot_info["df_score"]

    lines = []
    lines.append("# Plot Summary\n")

    # ---- plot 1
    lines.append("## 1. Domain Average Score\n")
    lines.append("**Purpose:** to compare how well each domain did on average.\n")
    lines.append(f"This plot uses {len(df_score)} students. Students whose score was missing "
                 f"(filled by median) are left out so fake numbers dont change the averages.\n")
    for domain, value in averages.items():
        n = int((df_score["domain"] == domain).sum())
        lines.append(f"- {domain}: {value:.2f} (from {n} student(s))")
    lines.append("")
    lines.append(f"- Highest average: **{averages.idxmax()}** ({averages.max():.2f})")
    lines.append(f"- Lowest average: **{averages.idxmin()}** ({averages.min():.2f})")
    lines.append("- Note: each domain has only a few students, so these averages are not very strong.\n")

    # ---- plot 2
    lines.append("## 2. Attendance vs Score\n")
    lines.append("**Purpose:** to see if students with more attendance also get more score.\n")
    lines.append(f"This plot uses {len(df_scatter)} students (students with filled-in attendance or "
                 f"score are left out).\n")
    if len(df_scatter) >= 3:
        corr = df_scatter["attendance_percent"].corr(df_scatter["score"])
        if corr >= 0.7:
            word = "a strong positive"
        elif corr >= 0.3:
            word = "a weak to medium positive"
        elif corr > -0.3:
            word = "almost no"
        else:
            word = "a negative"
        lines.append(f"- Correlation between attendance and score: **{corr:.2f}**, which means {word} relationship.")
        low = df_scatter.loc[df_scatter["attendance_percent"].idxmin()]
        high = df_scatter.loc[df_scatter["attendance_percent"].idxmax()]
        lines.append(f"- Lowest attendance: {low['student_id']} ({low['name']}) with {low['attendance_percent']:.0f}% and score {low['score']:.0f}")
        lines.append(f"- Highest attendance: {high['student_id']} ({high['name']}) with {high['attendance_percent']:.0f}% and score {high['score']:.0f}")
        lines.append("- With so few points this is only a rough pattern, not proof.\n")
    else:
        lines.append("- Not enough points to say anything.\n")

    # ---- plot 3
    lines.append("## 3. Submission Status Count\n")
    lines.append("**Purpose:** to see how many students submitted their work.\n")
    total = int(counts.sum())
    for status, n in counts.items():
        lines.append(f"- {status}: {n} ({n / total * 100:.0f}%)")
    lines.append("")

    # ---- conclusion
    lines.append("## Conclusion\n")
    submitted = int(counts.get("Submitted", 0))
    lines.append(f"Out of {total} students, {submitted} submitted. "
                 f"{averages.idxmax()} has the highest average score and {averages.idxmin()} has the lowest "
                 f"(among students with real scores). "
                 f"The data is small, so all of these points should be taken carefully.")

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
