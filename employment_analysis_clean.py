
import pandas as pd
import matplotlib.pyplot as plt


def clean_employment(data):
    """Clean undergraduate employment data for selected years."""
    rows = [8, 50, 92]
    years = [2005, 2010, 2017]
    columns = [4, 7, 10, 13, 16, 22, 25, 28, 31, 34]

    cleaned = data.loc[rows, columns].copy()

    cleaned.columns = [
        "ft_employed", "ft_under10", "ft_10to19",
        "ft_20to34", "ft_35plus",
        "pt_employed", "pt_under10", "pt_10to19",
        "pt_20to34", "pt_35plus"
    ]

    cleaned["year"] = years
    cleaned = cleaned.astype(float)
    cleaned = cleaned.set_index("year")

    return cleaned


def calculate_hours_distribution(data):
    """Calculate the percentage in each working-hours category."""
    totals = data.sum(axis=1)
    return data.div(totals, axis=0) * 100


def plot_employment_rates(data):
    """Create a line graph of undergraduate employment rates."""
    fig, ax = plt.subplots(figsize=(8, 5))

    ax.plot(data.index, data["ft_employed"],
            marker="o", label="Full-time")

    ax.plot(data.index, data["pt_employed"],
            marker="o", label="Part-time")

    ax.set_title("Undergraduate Employment Rates (2005-2017)")
    ax.set_xlabel("Year")
    ax.set_ylabel("Employment Rate (%)")
    ax.set_xticks([2005, 2010, 2017])
    ax.set_ylim(0, 100)
    ax.legend()

    plt.savefig("employment_rates.png")
    plt.show()


def plot_working_hours(data):
    """Create stacked bar charts of weekly working hours."""
    data = data.copy()

    # Combine categories representing fewer than 20 hours
    data["ft_under20"] = data["ft_under10"] + data["ft_10to19"]
    data["pt_under20"] = data["pt_under10"] + data["pt_10to19"]

    # Select working-hours categories
    ft_hours = data[
        ["ft_under20", "ft_20to34", "ft_35plus"]
    ].copy()

    pt_hours = data[
        ["pt_under20", "pt_20to34", "pt_35plus"]
    ].copy()

    # Normalize categories to percentages totaling 100
    ft_hours = calculate_hours_distribution(ft_hours)
    pt_hours = calculate_hours_distribution(pt_hours)

    # Display years as whole numbers
    ft_hours.index = ft_hours.index.astype(int)
    pt_hours.index = pt_hours.index.astype(int)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Full-time students
    ft_hours.plot(kind="bar", stacked=True, ax=ax1)

    ax1.set_title("Full-Time Students")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Percentage (%)")
    ax1.set_ylim(0, 100)
    ax1.legend(["Under 20", "20-34", "35+"],
               title="Hours Worked")

    # Part-time students
    pt_hours.plot(kind="bar", stacked=True, ax=ax2)

    ax2.set_title("Part-Time Students")
    ax2.set_xlabel("Year")
    ax2.set_ylabel("Percentage (%)")
    ax2.set_ylim(0, 100)
    ax2.legend(["Under 20", "20-34", "35+"],
               title="Hours Worked")

    plt.suptitle("Weekly Working Hours (2005-2017)")
    plt.tight_layout()
    plt.savefig("working_hours.png")
    plt.show()


def main():
    """Load, clean, summarize, and visualize employment data."""
    employment = pd.read_csv("tabn503.40.csv", header=None)
    cleaned = clean_employment(employment)

    print("Dataset overview:")
    print(cleaned.shape)

    print("Missing values:")
    print(cleaned.isna().sum())

    print("Descriptive statistics:")
    print(cleaned.describe())

    print("Years included:")
    print(cleaned.index.value_counts())

    plot_employment_rates(cleaned)
    plot_working_hours(cleaned)


if __name__ == "__main__":
    main()
