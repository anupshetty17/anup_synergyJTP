# clean_data.py
# This file has all the functions that clean the messy student data.
# I made one small function for each problem so its easy to follow.

import re
import pandas as pd

# words to numbers, because the score and study hours have some words in them
WORD_TO_NUMBER = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
}

# different spellings of the same domain -> one proper name
DOMAIN_MAP = {
    "ml": "ML",
    "machine learning": "ML",
    "web": "Web Dev",
    "web dev": "Web Dev",
    "web development": "Web Dev",
    "electronics": "Electronics",
    "mechanical": "Mechanical",
}

# different spellings of submitted -> one proper name
SUBMITTED_MAP = {
    "yes": "Submitted",
    "y": "Submitted",
    "no": "Not Submitted",
    "n": "Not Submitted",
}


def load_data(path):
    """Read the csv file. If the file is not there then stop with a clear message."""
    try:
        df = pd.read_csv(path)
    except FileNotFoundError:
        raise FileNotFoundError(f"Cannot find the input file: {path}")
    return df


def remove_duplicates(df, log):
    """Remove the rows that are exactly the same, and also repeated student ids."""
    rows_before = len(df)
    df = df.drop_duplicates()                                  # exact same rows
    df = df.drop_duplicates(subset="student_id", keep="first")  # same id again
    removed = rows_before - len(df)
    log["duplicates_removed"] = removed
    return df


def clean_domain(df):
    """Make domain names the same. Example: 'web' and 'Web Development' -> 'Web Dev'."""
    def fix(value):
        if pd.isna(value):
            return None
        key = str(value).strip().lower()
        return DOMAIN_MAP.get(key, None)   # if we dont know the domain it becomes None
    df["domain"] = df["domain"].apply(fix)
    return df


def clean_submitted(df):
    """yes / Yes / Y -> Submitted, and no / N -> Not Submitted."""
    def fix(value):
        if pd.isna(value):
            return None
        return SUBMITTED_MAP.get(str(value).strip().lower(), None)
    df["submitted"] = df["submitted"].apply(fix)
    return df


def to_number(value):
    """Turn something like '92%' or 'nine' or '5' into a number. If we cant then NaN."""
    if pd.isna(value):
        return float("nan")
    text = str(value).strip().lower()
    if text in WORD_TO_NUMBER:
        return float(WORD_TO_NUMBER[text])
    text = text.replace("%", "").strip()
    try:
        return float(text)
    except ValueError:
        return float("nan")


def clean_attendance(df, log):
    """Attendance -> number. Remove the % sign. Values outside 0 to 100 are wrong so make them NaN."""
    df["attendance_percent"] = df["attendance_percent"].apply(to_number)
    bad = (df["attendance_percent"] < 0) | (df["attendance_percent"] > 100)
    log["attendance_invalid_ids"] = df.loc[bad, "student_id"].tolist()
    df.loc[bad, "attendance_percent"] = float("nan")
    return df


def clean_score(df, log):
    """Score -> number (nine -> 9). Score should be between 0 and 10, anything else is invalid."""
    df["score"] = df["score"].apply(to_number)
    bad = (df["score"] < 0) | (df["score"] > 10)
    log["score_invalid_ids"] = df.loc[bad, "student_id"].tolist()
    df.loc[bad, "score"] = float("nan")
    return df


def clean_study_hours(df, log):
    """Study hours -> number (two -> 2). Negative hours are not possible so make them NaN."""
    df["study_hours"] = df["study_hours"].apply(to_number)
    bad = df["study_hours"] < 0
    log["study_hours_invalid_ids"] = df.loc[bad, "student_id"].tolist()
    df.loc[bad, "study_hours"] = float("nan")
    return df


def height_to_cm(value):
    """'170 cm' -> 170, '168cm' -> 168, '1.62 m' -> 162."""
    if pd.isna(value):
        return float("nan")
    text = str(value).strip().lower()
    match = re.search(r"[\d.]+", text)
    if match is None:
        return float("nan")
    number = float(match.group())
    if "cm" in text:
        return number
    if "m" in text:
        return round(number * 100, 1)   # metre to cm
    # no unit written, so guess: a small number must be in metres
    if number < 3:
        return round(number * 100, 1)
    return number


def weight_to_kg(value):
    """'65 kg' -> 65, '55kg' -> 55. All weights in this file are already in kg."""
    if pd.isna(value):
        return float("nan")
    text = str(value).strip().lower()
    match = re.search(r"[\d.]+", text)
    if match is None:
        return float("nan")
    number = float(match.group())
    if "lb" in text:
        return round(number * 0.453592, 1)   # pounds to kg (not needed here but just in case)
    return number


def clean_height_weight(df):
    df["height"] = df["height"].apply(height_to_cm)
    df["weight"] = df["weight"].apply(weight_to_kg)
    df = df.rename(columns={"height": "height_cm", "weight": "weight_kg"})
    return df


def fill_missing_numbers(df, log):
    """
    Fill the missing numbers with the median of that column.
    I used median and not mean because the mean can change a lot if there is one weird value.
    I also save which student ids were filled, so I can mention it in the report.
    """
    log["imputed"] = {}
    for col in ["attendance_percent", "score", "study_hours", "height_cm", "weight_kg"]:
        missing = df[col].isna()
        if missing.sum() > 0:
            median_value = df[col].median()
            log["imputed"][col] = {
                "ids": df.loc[missing, "student_id"].tolist(),
                "filled_with": float(median_value),
            }
            df.loc[missing, col] = median_value
    return df


def clean_students(df):
    """Run all the cleaning steps one by one. Returns the clean data and a log of what happened."""
    log = {}
    df = df.copy()

    # strip spaces from the text columns first
    for col in ["student_id", "name"]:
        df[col] = df[col].astype(str).str.strip()

    df = remove_duplicates(df, log)
    df = clean_domain(df)
    df = clean_submitted(df)
    df = clean_attendance(df, log)
    df = clean_score(df, log)
    df = clean_study_hours(df, log)
    df = clean_height_weight(df)
    df = fill_missing_numbers(df, log)

    df = df.reset_index(drop=True)
    return df, log
