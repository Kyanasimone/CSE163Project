""" This file is to read the cost of living data we have."""
import pandas as pd

twentyten_csv = pd.read_csv("yrs2010-11.csv", header=[0,1])

""" For quantitative variables, this will be a seven-number summary (mean, standard deviation, minimum, first quartile, median, third quartile, maximum).
You are welcome to reuse your code from HW 1: Processing or use pandas’ DataFrame.describe method.
"""

def yr_cost(datafile: DataSeries.pd):
  # first want to be looking at the two yr stuff and it doesn't have like a MultiIndex,
  # so just saying specific rows
  twoyr_live_flt = datafile.loc[25:27]
  twoyr_tuit_bk = datafile.loc[30:31]
  twoyr_campus = datafile.loc[34:35]
  twoyr_off_fam = datafile.loc[37]
  twoyr_off_nofam = datafile.loc[39:40]
  two_yr_data = datafile[twoyr_live_flt | twoyr_tuit_bk | twoyr_campus | twoyr_off_fam | twoyr_off_nofam]
  two_yr_describe = two_yr_data.describe()
  # 4 yr time
  fouryr_live_flt = datafile.loc[6:8]
  fouryr_tuit_bk = datafile.loc[11:12]
  fouryr_campus = datafile.loc[15:16]
  fouryr_off_fam = datafile.loc[18]
  fouryr_off_nofam = datafile.loc[20:21]
  four_yr_data = datafile[fouryr_live_flt | fouryr_tuit_bk | fouryr_campus | fouryr_off_fam | fouryr_off_nofam]
  four_yr_describe = four_yr_data.describe()
  # next need to put into a dictionary so we can also have the value for the tuition costs



# with later solved average for variable 2
other_cost_2010_twoyr = ave_cost_2010_twoyr - tuition_cost_2010_twoyr
other_cost_2010_fouryr = ave_cost_2010_fouryr - tuition_cost_2010_fouryr

# visualisations
"""One will compare the college costs against inflation. The other will show the percentage
difference in the cost of college versus the difference in the cost of other expenses for each year."""
"""-The cost per year for a two- and four-year institution. You find it within that year's
dollars. Index “average total cost, by living arrangement”; we will average “On Campus”,
“Off Campus, living with family”, and “Off Campus, not living with family” per year while keeping
the “Two-year institute” and “Four-year institute”. We want to see the change in cost per year in those
years, so then we can find the change in costs due to inflation.
-The cost of tuition, which is in each of the two- and four-year institution categories. We can use
the average cost minus the tuition cost to get the other fees to be able to compare the changes in
prices per year. We are doing this to see which elements of students' costs are changing the most.
"""

def college_cost_infla(cost: int, yr: int):
  # We can use this for both graphs
  yrs_cost = {}
  if yr == 2010:
    # There was a price increase of 12.41% from 2010 to 2017
    cost2017 = cost * 1.1241
    cost_2017_round = rounded(cost2017, 2)
    yrs_cost[2017] = cost_2017_round
    # The price increase was -10.44% also know as price decrease from 2010 to 2005
    cost2005 = cost * 0.8956
    cost_2005_round = rounded(cost2005, 2)
    yrs_cost[2005] = cost_2005_round



