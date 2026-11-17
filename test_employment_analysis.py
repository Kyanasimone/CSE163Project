
import pandas as pd

from employment_analysis_clean import (
    clean_employment,
    calculate_hours_distribution
)


def test_clean_employment():
    data = pd.read_csv("tabn503.40.csv", header=None)
    cleaned = clean_employment(data)

    assert cleaned.shape == (3, 10)
    assert list(cleaned.index) == [2005, 2010, 2017]
    assert cleaned.loc[2005, "ft_employed"] == 49.8
    assert cleaned.loc[2010, "pt_employed"] == 74.5
    assert cleaned.loc[2017, "ft_employed"] == 43.1
    assert cleaned.isna().sum().sum() == 0


def test_calculate_hours_distribution():
    data = pd.DataFrame({
        "under20": [20, 10],
        "20to34": [30, 20],
        "35plus": [50, 70]
    })

    result = calculate_hours_distribution(data)

    assert result.loc[0, "under20"] == 20
    assert result.loc[0, "20to34"] == 30
    assert result.loc[1, "35plus"] == 70
    assert all(abs(result.sum(axis=1) - 100) < 0.0001)


def main():
    test_clean_employment()
    test_calculate_hours_distribution()
    print("All tests passed!")


if __name__ == "__main__":
    main()
