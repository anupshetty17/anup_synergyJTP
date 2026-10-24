# main.py
# Run this from the project folder like this:
#   python src/main.py data/messy_students.csv output

import os
import sys

# so imports work no matter where we run it from
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from clean_data import load_data, clean_students
from validate_data import validate_students, print_validation
from visualize import make_all_plots
from reports import make_summary, save_json, write_cleaning_report, write_plot_summary


def main():
    if len(sys.argv) != 3:
        print("How to run: python src/main.py <input_csv> <output_folder>")
        print("Example:    python src/main.py data/messy_students.csv output")
        sys.exit(1)

    input_path = sys.argv[1]
    output_folder = sys.argv[2]

    # make the output folder if its not there
    os.makedirs(output_folder, exist_ok=True)

    # 1. load the raw data
    print("Loading data...")
    try:
        raw = load_data(input_path)
    except FileNotFoundError as error:
        print(error)
        sys.exit(1)

    # 2. summary before cleaning
    summary_before = make_summary(raw)
    save_json(summary_before, os.path.join(output_folder, "summary_before.json"))
    print(f"  raw data: {summary_before['rows']} rows, {summary_before['columns']} columns")

    # 3. clean
    print("Cleaning data...")
    clean, log = clean_students(raw)

    # 4. validate
    print("Validating data...")
    results = validate_students(clean)
    print_validation(results)

    # 5. save clean csv and summary after
    clean.to_csv(os.path.join(output_folder, "cleaned_students.csv"), index=False)
    summary_after = make_summary(clean)
    save_json(summary_after, os.path.join(output_folder, "summary_after.json"))
    print(f"  clean data: {summary_after['rows']} rows, {summary_after['columns']} columns")

    # 6. plots
    print("Making plots...")
    plot_info = make_all_plots(clean, log, output_folder)

    # 7. reports
    print("Writing reports...")
    write_cleaning_report(os.path.join(output_folder, "cleaning_report.md"),
                          summary_before, summary_after, log, results)
    write_plot_summary(os.path.join(output_folder, "plot_summary.md"), clean, plot_info, log)

    print("Done! Check the", output_folder, "folder.")


if __name__ == "__main__":
    main()
