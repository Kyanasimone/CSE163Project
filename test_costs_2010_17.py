""" This file is to assess the data has been properly
manually cleaned for the cost of education in 2010-11
and 2017-18 datasets and yrs_cost function"""

import pandas as pd

from Cost_living_nums.py import (
    yr_cost_seventeen,
    yr_cost_ten
)

def test_manual_2010():
    twentyten_csv = pd.read_csv("yrs2010-11.csv", header=[0,1])
    assert twentyten_csv.loc[7, 2] == 33494
    assert twentyten_csv.loc[10, 3] == 9044
    assert twentyten_csv.loc[14, 4] == 32452
    assert twentyten_csv.loc[16, 5] == 28651
    assert twentyten_csv.loc[2, 3] == "Public, in-state"


def test_manual_2017():
    twentyseventeen_csv = pd.read_csv("yrs_cost_2017-18", header=[0,1]) 
    assert twentyseventeen_csv.loc[7, 2] == 19940
    assert twentyseventeen_csv.loc[11, 3] == 7249
    assert twentyseventeen_csv.loc[15, 4] == 9464
    assert twentyseventeen_csv.loc[27, 5] == 28805
    assert twentyseventeen_csv.loc[2, 4] == "Non- profit"


def test_yr_cost_2017():
    csv_2017 = pd.read_csv("yrs_cost_2017-18", header=[0,1])

    yr_cost_seventeen(csv_2017)


def main():
    test_manual_2010()
    test_manual_2017()
    test_yr_cost_2017()
    print("All tests passed!")


if __name__ == "__main__":
    main()
