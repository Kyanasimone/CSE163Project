"""
CSE 163: Unit tests for RQ3 data processing and cleaning functions.
"""

import pandas as pd
from hours_distribution import compute_employment_rates, load_and_clean_nces


def make_test_data():
    """
    Creates a small synthetic DataFrame matching the cleaned NCES structure
    to test normalization math with easy-to-verify numbers.
    """
    return pd.DataFrame({
            "year": [2005, 2005],
            "enrollment_status": ["Full-time", "Part-time"],
            "emp_rate": [50.0, 80.0],
            "raw_under_20": [20.0, 10.0],
            "raw_20_to_34": [20.0, 20.0],
            "raw_35_plus": [10.0, 50.0]})


def test_compute_employment_rates():
    """
    Tests that compute_employment_rates accurately normalizes hour brackets
    to sum to 100% of active working students.
    """
    df = make_test_data()
    res = compute_employment_rates(df)

    # Full-time row: 20 + 20 + 10 = 50 total -> 40%, 40%, 20%
    ft_row = res.iloc[0]
    assert abs(ft_row["pct_under_20"] - 40.0) < 0.001
    assert abs(ft_row["pct_20_to_34"] - 40.0) < 0.001
    assert abs(ft_row["pct_35_plus"] - 20.0) < 0.001

    # Part-time row: 10 + 20 + 50 = 80 total -> 12.5%, 25.0%, 62.5%
    pt_row = res.iloc[1]
    assert abs(pt_row["pct_under_20"] - 12.5) < 0.001
    assert abs(pt_row["pct_20_to_34"] - 25.0) < 0.001
    assert abs(pt_row["pct_35_plus"] - 62.5) < 0.001


def test_load_and_clean_nces():
    """
    Tests that load_and_clean_nces extracts the exact 6 rows and column
    values from hours_distribution.csv without shifting rows or columns.
    """
    cleaned = load_and_clean_nces("hours_distribution.csv")

    # Should produce 6 rows (3 years x 2 enrollment statuses)
    assert len(cleaned) == 6
    assert list(cleaned["year"]) == [2005, 2005, 2010, 2010, 2017, 2017]
    assert list(cleaned["enrollment_status"]) == ["Full-time", "Part-time",
                                                  "Full-time", "Part-time",
                                                  "Full-time", "Part-time"]

    # Verify 2005 Full-time values (Row 7: emp=49.8,
    # <10=7.2, 10-19=9.3 -> 16.5)
    assert abs(cleaned.loc[0, "emp_rate"] - 49.8) < 0.001
    assert abs(cleaned.loc[0, "raw_under_20"] - 16.5) < 0.001

    # Verify 2017 Part-time values (Row 91: emp=80.6, 35+=45.7)
    assert abs(cleaned.loc[5, "emp_rate"] - 80.6) < 0.001
    assert abs(cleaned.loc[5, "raw_35_plus"] - 45.7) < 0.001


def test_full_pipeline_sums():
    """
    Verifies that every processed row from hours_distribution.csv has
    normalized hour percentages summing to 100%.
    """
    cleaned = load_and_clean_nces("hours_distribution.csv")
    processed = compute_employment_rates(cleaned)

    for idx in range(len(processed)):
        row = processed.iloc[idx]
        total_pct = (row["pct_under_20"] + row["pct_20_to_34"] +
                     row["pct_35_plus"])
        assert abs(total_pct - 100.0) < 0.001


def main():
    test_compute_employment_rates()
    test_load_and_clean_nces()
    test_full_pipeline_sums()
    print("All tests passed.")


if __name__ == "__main__":
    main()
