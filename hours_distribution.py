"""
CSE 163: Final Project Part 2 (EDA) - RQ3 Analysis
Module for processing student employment distributions by enrollment status.
"""

import matplotlib.pyplot as plt
import pandas as pd


def load_and_clean_nces(filepath):
    """
    Extracts Full-time and Part-time overall employment and hours-worked
    percentages for 2005, 2010, and 2017 from hours_distribution.csv.
    """
    raw = pd.read_csv(filepath)
    year_rows = {2005: 7, 2010: 49, 2017: 91}
    records = []

    for year, row_idx in year_rows.items():
        row = raw.iloc[row_idx]
        # Full-time columns: 4 (total), 7 (<10),
        # 10 (10-19), 13 (20-34), 16 (35+)
        records.append({
                "year": year,
                "enrollment_status": "Full-time",
                "emp_rate": float(row.iloc[4]),
                "raw_under_20": float(row.iloc[7]) + float(row.iloc[10]),
                "raw_20_to_34": float(row.iloc[13]),
                "raw_35_plus": float(row.iloc[16])})
        # Part-time columns: 22 (total), 25 (<10),
        # 28 (10-19), 31 (20-34), 34 (35+)
        records.append({
                "year": year,
                "enrollment_status": "Part-time",
                "emp_rate": float(row.iloc[22]),
                "raw_under_20": float(row.iloc[25]) + float(row.iloc[28]),
                "raw_20_to_34": float(row.iloc[31]),
                "raw_35_plus": float(row.iloc[34])})

    return pd.DataFrame(records)


def compute_employment_rates(df):
    """
    Normalizes weekly hours worked as a percentage of employed students
    who were at work during the survey week.
    """
    res = df.copy()
    reported_total = (res["raw_under_20"] + res["raw_20_to_34"] +
                      res["raw_35_plus"])
    res["pct_under_20"] = (res["raw_under_20"] / reported_total) * 100
    res["pct_20_to_34"] = (res["raw_20_to_34"] / reported_total) * 100
    res["pct_35_plus"] = (res["raw_35_plus"] / reported_total) * 100
    return res


def plot_grouped_employment_rates(df):
    """
    Generates a grouped bar chart comparing Full-Time vs Part-Time employment
    rates across 2005, 2010, and 2017, saving it as a PNG file.
    """
    pivot_df = df.pivot(index="year", columns="enrollment_status",
                        values="emp_rate")

    fig, ax = plt.subplots(figsize=(8, 5))
    pivot_df.plot(kind="bar", ax=ax, width=0.7, edgecolor="black")

    ax.set_title("Undergraduate Employment Rate by Enrollment Status",
                 fontsize=13)
    ax.set_xlabel("Year", fontsize=11)
    ax.set_ylabel("Employment Rate (%)", fontsize=11)
    ax.set_ylim(0, 100)
    ax.legend(title="Status")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig("rq3_employment_rate.png")
    plt.close()


def plot_hours_distribution(df):
    """
    Generates a stacked bar chart showing the proportion of weekly hours
    worked, saving it as a PNG file.
    """
    plot_df = df.copy()
    plot_df["cohort"] = (plot_df["enrollment_status"] +
                         " (" + plot_df["year"].astype(str) + ")")

    cols = ["pct_under_20", "pct_20_to_34", "pct_35_plus"]
    chart_data = plot_df.set_index("cohort")[cols]

    fig, ax = plt.subplots(figsize=(10, 6))
    chart_data.plot(kind="bar", stacked=True, ax=ax, colormap="Blues",
                    edgecolor="black", width=0.6)

    ax.set_title("Distribution of Weekly Work Hours Among Employed Students",
                 fontsize=13)
    ax.set_xlabel("Cohort Group", fontsize=11)
    ax.set_ylabel("Proportion of Employed Students (%)", fontsize=11)
    ax.set_ylim(0, 100)
    ax.legend(["< 20 Hours", "20-34 Hours", "35+ Hours"],
              title="Weekly Commitment", loc="upper right")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("rq3_hours_distribution.png")
    plt.close()


def main():
    dataset_file = "hours_distribution.csv"
    cleaned = load_and_clean_nces(dataset_file)
    processed = compute_employment_rates(cleaned)

    print("=== Quantitative Summary (describe) ===")
    cols = ["emp_rate", "pct_under_20", "pct_20_to_34", "pct_35_plus"]
    print(processed[cols].describe())

    plot_grouped_employment_rates(processed)
    plot_hours_distribution(processed)


if __name__ == "__main__":
    main()
