# validate_data.py
# This file checks if the cleaned data follows the rules.
# Important: it only CHECKS. It does not delete any rows to make the checks pass.

import pandas as pd

ALLOWED_DOMAINS = ["ML", "Web Dev", "Electronics", "Mechanical"]
ALLOWED_SUBMITTED = ["Submitted", "Not Submitted"]
CRITICAL_COLUMNS = ["student_id", "name", "domain", "attendance_percent",
                    "score", "study_hours", "submitted"]
NUMERIC_COLUMNS = ["attendance_percent", "score", "study_hours", "height_cm", "weight_kg"]


def make_result(name, passed, details):
    return {"check": name, "passed": bool(passed), "details": details}


def check_student_ids(df):
    missing = df["student_id"].isna().sum() + (df["student_id"].astype(str).str.strip() == "").sum()
    repeated = df["student_id"].duplicated().sum()
    passed = (missing == 0) and (repeated == 0)
    return make_result("Student IDs unique and not missing", passed,
                       f"{missing} missing, {repeated} repeated")


def check_attendance(df):
    bad = df[(df["attendance_percent"] < 0) | (df["attendance_percent"] > 100)]
    return make_result("Attendance between 0 and 100", len(bad) == 0,
                       f"{len(bad)} rows outside the range")


def check_domains(df):
    bad = df[~df["domain"].isin(ALLOWED_DOMAINS)]
    return make_result("Domain is in the allowed list", len(bad) == 0,
                       f"{len(bad)} rows have a domain not in {ALLOWED_DOMAINS}")


def check_submitted(df):
    bad = df[~df["submitted"].isin(ALLOWED_SUBMITTED)]
    return make_result("Submission status is in the allowed list", len(bad) == 0,
                       f"{len(bad)} rows have a status not in {ALLOWED_SUBMITTED}")


def check_critical_missing(df):
    counts = df[CRITICAL_COLUMNS].isna().sum()
    total = int(counts.sum())
    bad_cols = counts[counts > 0].to_dict()
    return make_result("No missing values in critical columns", total == 0,
                       f"{total} missing values {bad_cols if bad_cols else ''}".strip())


def check_numeric_columns(df):
    problems = []
    for col in NUMERIC_COLUMNS:
        if not pd.api.types.is_numeric_dtype(df[col]):
            problems.append(f"{col} is not numeric")
        elif df[col].isna().any():
            problems.append(f"{col} has NaN values")
    return make_result("Numeric columns have valid numbers", len(problems) == 0,
                       "; ".join(problems) if problems else "all numeric columns are fine")


def check_score_range(df):
    # extra check from me: score should be 0 to 10
    bad = df[(df["score"] < 0) | (df["score"] > 10)]
    return make_result("Score between 0 and 10 (extra check)", len(bad) == 0,
                       f"{len(bad)} rows outside the range")


def validate_students(df):
    """Run every check and give back the list of results."""
    return [
        check_student_ids(df),
        check_attendance(df),
        check_domains(df),
        check_submitted(df),
        check_critical_missing(df),
        check_numeric_columns(df),
        check_score_range(df),
    ]


def print_validation(results):
    for r in results:
        status = "PASS" if r["passed"] else "FAIL"
        print(f"  [{status}] {r['check']} -> {r['details']}")
