""" This file is to assess the data has been properly
manually cleaned for the cost of education in 2010-11
and 2017-18 datasets and yrs_cost function"""

import pandas as pd
import pytest

from Cost_living_nums.py import (
    yr_cost_seventeen,
    yr_cost_ten
)

def test_manual_2010():
    twentyten_csv = pd.read_csv("yrs2010-11.csv", header=[0,1])
    assert twentyten_csv.iloc[8, 1] == 14551
    assert twentyten_csv.iloc[3, 2] == 20114
    assert twentyten_csv.iloc[13, 3] == 2323
    assert twentyten_csv.iloc[17, 4] == 8543
    assert twentyten_csv.iloc[1, 0] == "4-year institutions"


def test_manual_2017():
    twentyseventeen_csv = pd.read_csv("yrs_cost_2017-18", header=[0,1]) 
    assert int(twentyseventeen_csv.iloc[7, 1]) == 18041
    assert int(twentyseventeen_csv.iloc[4, 2]) == 24320
    assert int(twentyseventeen_csv.iloc[12, 3]) == 23134
    assert int(twentyseventeen_csv.iloc[14, 4]) == 14169
    assert twentyseventeen_csv.iloc[3, 0] == "Average total cost, by living arrangement"

def test_yr_cost_2017():
    csv_2017 = pd.read_csv("yrs_cost_2017-18", header=[0,1])
    cost_dict = yr_cost_seventeen(csv_2017)
    assert cost_dict["twoyr_tuit"] == pytest.approx(9948.5)
    assert cost_dict["mean2"] == pytest.approx(20935.5833333333)
    assert cost_dict["fouryr_tuit"] == pytest.approx(19681.5)
    assert cost_dict["twoyr_other"] == pytest.approx(10987.0833333333)


def test_yr_cost_2010():
    csv_2010 = pd.read_csv("yrs2010-11.csv", header=[0,1])
    cost_dict = yr_cost_ten(csv_2010)
    assert cost_dict["twoyr_tuit"] == pytest.approx(9059)
    assert cost_dict["mean2"] == pytest.approx(18879.75)
    assert cost_dict["mean4"] == pytest.approx(26843.75)
    assert cost_dict["twoyr_other"] == pytest.approx(9820.75)


def main():
    test_manual_2010()
    test_manual_2017()
    test_yr_cost_2017()
    test_yr_cost_2010()
    print("All tests passed!")


if __name__ == "__main__":
    main()
