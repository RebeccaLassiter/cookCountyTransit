import numpy as np 
import pandas as pd

tractData = pd.read_csv("commutingByCensusTract.csv", skiprows=(1,2))
print(tractData.head())
print(tractData.iloc[0][0])

#get the total number of people and number of people taking transit
#get the mean travel time for transit
#get the median income
scatterPlot = pd.DataFrame(tractData.iloc[:,0:3]) #keep the geographic info
print(scatterPlot.iloc[:, 1:3])
total = tractData.iloc[:]["HC01_EST_VC01"]
numTransit = tractData.iloc[:]["HC04_EST_VC01"]
meanTravelTimeTransit = tractData.iloc[:]["HC04_EST_VC118"]
medianIncome = tractData.iloc[:]["HC01_EST_VC51"]
# leavingHome = tractData.iloc[:, [569, 578, 587, 596, 605, 614, 623, 631, 640, 649]]
# print(leavingHome)
#print("max median income: ", medianIncome.max()) = 157500
#print('min median income; ', medianIncome.min()) = 4345
scatterPlot["niceName"] = scatterPlot.iloc[:, 2]
scatterPlot["totalPeople"] = total
scatterPlot["commuttersTakingTransit"] = numTransit
scatterPlot["meanTravelTimeTransit"] = meanTravelTimeTransit
scatterPlot["medianIncome"] = medianIncome
#scatterPlot = pd.concat([scatterPlot, leavingHome], axis=1)
#12am-5am = index 569
#5am-5:30 = index 578 (+ 9)
#5:30-6 = 587
#6-6:30 = 596
#6:30-7 = 605
#7-7:30 = 614
#7:30-8 = 623
#8-8:30 = 631
#8:30-9 = 640
#9am-12pm = 649
##tract data. want the time they leave in the morning, race, and industry they work in for transit riders


scatterPlot.to_csv("scatterPlotData.csv")
print(scatterPlot)
