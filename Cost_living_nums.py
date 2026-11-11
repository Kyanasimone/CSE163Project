""" This file is to read the cost of living data we have."""
import pandas as pd

twentyten_csv = pd.read_csv("yrs2010-11.csv", header=[0,1])
twentyseventeen_csv = pd.read_csv()

""" For quantitative variables, this will be a seven-number summary (mean, standard deviation, minimum, first quartile, median, third quartile, maximum).
You are welcome to reuse your code from HW 1: Processing or use pandas’ DataFrame.describe method.
"""

def yr_cost(datafile: DataSeries.pd):
  # first want to be looking at the two yr stuff and it doesn't have like a MultiIndex,
  # so just saying specific rows
  cost = {}
  twoyr_live_flt = datafile.loc[25:27]
  twoyr_tuit_bk = datafile.loc[30:31]
  twoyr_campus = datafile.loc[34:35]
  twoyr_off_fam = datafile.loc[37]
  twoyr_off_nofam = datafile.loc[39:40]
  two_yr_data = datafile[twoyr_live_flt | twoyr_tuit_bk | twoyr_campus | twoyr_off_fam | twoyr_off_nofam]
  two_yr_live_desc = twoyr_live_flt.describe()
  for col in two_yr_live_desc:
    cost[col] = two_yr_live_desc[col]
  twoyr_tuit = datafile.loc[30]
  cost["twoyr_tuit"] = twoyr_tuit
  # 4 yr time
  fouryr_live_flt = datafile.loc[6:8]
  fouryr_tuit_bk = datafile.loc[11:12]
  fouryr_campus = datafile.loc[15:16]
  fouryr_off_fam = datafile.loc[18]
  fouryr_off_nofam = datafile.loc[20:21]
  four_yr_data = datafile[fouryr_live_flt | fouryr_tuit_bk | fouryr_campus | fouryr_off_fam | fouryr_off_nofam]
  four_yr_describe = four_yr_data.describe()
  four_yr_live_desc = fouryr_live_flt.describe()
  for col in four_yr_live_desc:
    cost[col] = four_yr_live_desc[col]
  fouryr_tuit = datafile.loc[30]
  cost["fouryr_tuit"] = fouryr_tuit
  return cost



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
  # it will return a dictionary with the years compared costs
  yr_infla = {}
  if yr == 2010:
    # There was a price increase of 12.41% from 2010 to 2017
    cost2010_17 = cost * 1.1241
    yr_infla[2017] = int(cost2010_17)
    # The price increase was -10.44% also know as price decrease from 2010 to 2005
    cost2005 = cost * 0.8956
    yr_infla[2005] = int(cost_2005)
    yr_infla[2010] = cost
  if yr == 2017:
    # price change from 2017 to 2010 is decrease of 12.41% 
    cost2017_2010 = cost * 0.8759
    yr_infla[2010] = int(cost2017_10)
    # The price increase was -20.32% also know as price decrease from 2017 to 2005
    cost2005 = cost * 0.7968
    yr_infla[2005] = int(cost_2005)
    yr_infla[2017] = cost
  return yr_infla


# REMEMBER GOT TO TRANSFER EACH THING INTO OTHERS INFLATIONS COST 
# first do it so its yr_cost for both yrs
# then do it so its college inflation do it for average tuition, and average other for both yrs
# and now you will do the average tuition of each year and it says to do percent dif for three variables
# do it like 2005(in 2010 dollars) - 2010, then seperate group 2010-2017(in 2010 dollars), then do
# 2005(in 2017 dollars) - 2017 we can do it with different yrs dollars for 2005 because its percentages

ten_cost = yr_cost(twentyten_csv)
seventeen_cost = yr_cost(twentyseventeen_csv)
ten_tuit_two = ten_cost[twoyr_tuit]
seventeen_tuit_two = seventeen_cost[twoyr_tuit]
ten_tuit_four = ten_cost[fouryr_tuit]
seventeen_tuit_four = seventeen_cost[fouryr_tuit]
ten_tuit_dict_two = college_cost_infla(ten_tuit_two, 2010)
seventeen_tuit_dict_two = college_cost_infla(seventeen_tuit_two, 2017)
ten_tuit_dict_4 = college_cost_infla(ten_tuit_four, 2010)
seventeen_tuit_dict_4 = college_cost_infla(seventeen_tuit_four, 2017)
dif_05_10_tuit2 = 100 * ((ten_tuit_dict_two[2010] - ten_tuit_dict_two[2005])/ (ten_tuit_dict_two[2005]))
dif_10_17_tuit2 = 100 * ((ten_tuit_dict_two[2017] - ten_tuit_dict_two[2010])/ (ten_tuit_dict_two[2010]))
dif_05_17_tuit2 = 100 * ((seventeen_tuit_dict_two[2017] - seventeen_tuit_dict_two[2005])/ (seventeen_tuit_dict_two[2005]))

dif_05_10_tuit4 = 100 * ((ten_tuit_dict_4[2010] - ten_tuit_dict_4[2005])/ ((ten_tuit_dict_4[2005])))
dif_10_17_tuit4 = 100 * ((ten_tuit_dict_4[2017] - ten_tuit_dict_4[2010])/ ((ten_tuit_dict_4[2010])))
dif_05_17_tuit4 = 100 * ((seventeen_tuit_dict_4[2017] - seventeen_tuit_dict_4[2005])/ (seventeen_tuit_dict_4[2005]))

# for other
ten_other_two = ten_cost[twoyr_other]
seventeen_other_two = seventeen_cost[twoyr_other]
ten_other_four = ten_cost[fouryr_other]
seventeen_other_four = seventeen_cost[fouryr_other]
ten_other_dict_two = college_cost_infla(ten_other_two, 2010)
seventeen_other_dict_two = college_cost_infla(seventeen_other_two, 2017)
ten_other_dict_4 = college_cost_infla(ten_other_four, 2010)
seventeen_other_dict_4 = college_cost_infla(seventeen_other_four, 2017)
dif_05_10_other2 = 100 * ((ten_other_dict_two[2010] - ten_other_dict_two[2005])/ ((ten_other_dict_two[2005])))
dif_10_17_other2 = 100 * ((ten_other_dict_two[2017] - ten_other_dict_two[2010])/ ((ten_other_dict_two[2010]))
dif_05_17_other2 = 100 * ((seventeen_other_dict_two[2017] - seventeen_other_dict_two[2005])/ ((seventeen_other_dict_two[2005])))

dif_05_10_other4 = 100 * ((ten_other_dict_4[2010] - ten_other_dict_4[2005])/ ((ten_other_dict_4[2005]))
dif_10_17_other4 = 100 * ((ten_other_dict_4[2017] - ten_other_dict_4[2010])/ ((ten_other_dict_4[2010]))
dif_05_17_other4 = 100 * ((seventeen_other_dict_4[2017] - seventeen_other_dict_4[2005])/ (seventeen_other_dict_4[2005]))

# we will also be having a third bar for each two year chunk for the inflation amounts 
dif_influ_05_10 = 10.44
dif_influ_10_17 = 12.41
dif_influ_05_17 = 20.32

# then going to make a big dictionary for two year results
two_yr_results = {"2005-2010":{
  "Tuit": dif_05_10_tuit2,
  "Other": dif_05_10_other2,
  "Infla": dif_influ_05_10},
                  "2005-2017": {
  "Tuit": dif_05_17_tuit2,
  "Other": dif_05_17_other2,
  "Infla": dif_influ_05_17}},
                  "2010-2017": {
  "Tuit": dif_10_17_tuit2,
  "Other": dif_10_17_other2,
  "Infla": dif_influ_10_17}}}



# this is for the graph with the costs on average
ten_cost = yr_cost(twentyten_csv)
seventeen_cost = yr_cost(twentyseventeen_csv)
# getting the averages into variables
ave_cost_ten_two = ten_cost["mean"]
ave_cost_seventeen_two = seventeen_cost["mean"]
ave_cost_ten_four = ten_cost["mean"]
ave_cost_seventeen_four = seventeen_cost["mean"]
# putting it with inflation
infla_ten_two = college_cost_infla(ave_cost_ten_two, 2010)
infla_seventeen_two = college_cost_infla(ave_cost_seventeen_two, 2017)
infla_ten_four = college_cost_infla(ave_cost_ten_four, 2010)
infla_seventeen_four = college_cost_infla(ave_cost_seventeen_four, 2017)
# now can get each point for line graph x= year and y = cost

# have to make it a connected dictionary
dic_ave_ten_two = {2005 : infla_ten_two[2005], 2010: infla_ten_two[2010], 2017: infla_ten_two[2017]}
dic_ave_seventeen_two = {2005 : infla_seventeen_two[2005], 2010: infla_seventeen_two[2010], 2017: infla_seventeen_two[2017]}
dic_ave_ten_four = {2005 : infla_ten_four[2005], 2010: infla_ten_four[2010], 2017: infla_ten_four[2017]}
dic_ave_seventeen_four = {2005 : infla_seventeen_four[2005], 2010: infla_seventeen_four[2010], 2017: infla_seventeen_four[2017]}

import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, figsize=(20,10))
# then this is for all the axes
ave_ten_two_x = list(dic_ave_ten_two.keys())
ave_ten_two_y = list(dic_ave_ten_two.values())
ave_seventeen_two_x = list(dic_ave_seventeen_two.keys())
ave_seventeen_two_y = list(dic_ave_seventeen_two.values())
ave_ten_four_x = list(dic_ave_ten_four.keys())
ave_ten_four_y = list(dic_ave_ten_four.values())
ave_seventeen_four_x = list(dic_ave_seventeen_four.keys())
ave_seventeen_four_y = list(dic_ave_seventeen_four.values())

dic_ave_ten_two.plot(x=ave_ten_two_x, y=ave_ten_two_y, ax=ax)
dic_ave_seventeen_two.plot(x=ave_seventeen_two_x, y=ave_seventeen_two_y, ax=ax)
dic_ave_ten_four.plot(x=ave_ten_four_x, y=ave_ten_four_y, ax=ax)
dic_ave_seventeen_four.plot(x=ave_seventeen_four_x, y=ave_seventeen_four_y, ax=ax)

plt.xlabel("Year")
plt.ylabel("Cost")
plt.title("Inflation of Each Years Cost")
plt.legend()
plt.savefig('InflationPerYear.png')





