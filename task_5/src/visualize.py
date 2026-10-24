# visualize.py
# Makes the 3 plots using matplotlib and saves them as png files.

import os
import matplotlib
matplotlib.use("Agg")   # so it works even without a screen
import matplotlib.pyplot as plt


def plot_domain_average_score(df, save_path):
    """Bar chart: average score for each domain."""
    averages = df.groupby("domain")["score"].mean().sort_values(ascending=False)

    plt.figure(figsize=(8, 5))
    bars = plt.bar(averages.index, averages.values, color="steelblue")
    for bar, value in zip(bars, averages.values):
        plt.text(bar.get_x() + bar.get_width() / 2, value + 0.1, f"{value:.1f}", ha="center")
    plt.title("Average Score by Domain")
    plt.xlabel("Domain")
    plt.ylabel("Average Score (out of 10)")
    plt.ylim(0, 11)
    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    plt.close()
    return averages


def plot_attendance_vs_score(df, save_path):
    """Scatter plot: attendance on x axis, score on y axis."""
    plt.figure(figsize=(8, 5))
    plt.scatter(df["attendance_percent"], df["score"], color="darkorange", s=60, edgecolor="black")
    for _, row in df.iterrows():
        plt.annotate(row["student_id"], (row["attendance_percent"], row["score"]),
                     textcoords="offset points", xytext=(5, 5), fontsize=8)
    plt.title("Attendance vs Score")
    plt.xlabel("Attendance (%)")
    plt.ylabel("Score (out of 10)")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    plt.close()


def plot_submission_count(df, save_path):
    """Bar chart: how many students submitted and how many did not."""
    counts = df["submitted"].value_counts()

    plt.figure(figsize=(6, 5))
    bars = plt.bar(counts.index, counts.values, color=["seagreen", "indianred"][:len(counts)])
    for bar, value in zip(bars, counts.values):
        plt.text(bar.get_x() + bar.get_width() / 2, value + 0.1, str(value), ha="center")
    plt.title("Submission Status Count")
    plt.xlabel("Submission Status")
    plt.ylabel("Number of Students")
    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    plt.close()
    return counts


def make_all_plots(df, log, output_folder):
    """
    Make all 3 plots.
    The students whose score or attendance was filled in by me (median) are left out
    of the plots that use that column, because those numbers are not real data.
    """
    imputed = log.get("imputed", {})
    skip_score = imputed.get("score", {}).get("ids", [])
    skip_attendance = imputed.get("attendance_percent", {}).get("ids", [])

    df_score = df[~df["student_id"].isin(skip_score)]
    df_scatter = df[~df["student_id"].isin(skip_score + skip_attendance)]

    paths = {
        "domain": os.path.join(output_folder, "domain_average_score.png"),
        "scatter": os.path.join(output_folder, "attendance_vs_score.png"),
        "submission": os.path.join(output_folder, "submission_status_count.png"),
    }

    averages = plot_domain_average_score(df_score, paths["domain"])
    plot_attendance_vs_score(df_scatter, paths["scatter"])
    counts = plot_submission_count(df, paths["submission"])

    return {
        "domain_averages": averages,
        "submission_counts": counts,
        "df_score": df_score,
        "df_scatter": df_scatter,
    }
