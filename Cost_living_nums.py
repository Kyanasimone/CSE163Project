""" This file is to read the cost of living data we have."""
import pandas as pd

twentyten_csv = pd.read_csv("yrs2010-11.csv", header=[0,1])

""" For quantitative variables, this will be a seven-number summary (mean, standard deviation, minimum, first quartile, median, third quartile, maximum).
You are welcome to reuse your code from HW 1: Processing or use pandas’ DataFrame.describe method.
"""

def yr_cost(datafile: DataSeries.pd):
  # first want to be looking at the two yr stuff and it doesn't have like a MultiIndex, so just saying specific rows
  cost_dict = {}
  twoyr_live_flt = datafile.loc[25:27]
  twoyr_tuit_bk = datafile.loc[30:31]
  twoyr_campus = datafile.loc[34:35]
  twoyr_off_fam = datafile.loc[37]
  twoyr_off_nofam = datafile.loc[39:40]
  two_yr_data = datafile[twoyr_live_flt | twoyr_tuit_bk | twoyr_campus | twoyr_off_fam | twoyr_off_nofam]
  two_yr_describe = two_yr_data.describe
  two_yr_mean = two_yr_describe.loc["mean"]


  


# with later solved average for variable 2
other_cost_2010_twoyr = ave_cost_2010_twoyr - tuition_cost_2010_twoyr
other_cost_2010_fouryr = ave_cost_2010_fouryr - tuition_cost_2010_fouryr
