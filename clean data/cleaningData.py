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
blackPercentage = tractData.iloc[:]["HC04_EST_VC19"]
americanIndianPercentage = tractData.iloc[:]["HC04_EST_VC20"]
asianPercentage = tractData.iloc[:]["HC04_EST_VC21"]
nativePercentage = tractData.iloc[:]["HC04_EST_VC22"]
otherPercentage = tractData.iloc[:]["HC04_EST_VC23"]
twoOrMorePercentage = tractData.iloc[:]["HC04_EST_VC24"]
hispanicPercentage = tractData.iloc[:]["HC04_EST_VC26"]
whitePercentage = tractData.iloc[:]["HC04_EST_VC27"]

leaving1 = tractData.iloc[:]["HC04_EST_VC97"]
leaving2 = tractData.iloc[:]["HC04_EST_VC98"]
leaving3 = tractData.iloc[:]["HC04_EST_VC99"]
leaving4 = tractData.iloc[:]["HC04_EST_VC100"]
leaving5 = tractData.iloc[:]["HC04_EST_VC101"]
leaving6 = tractData.iloc[:]["HC04_EST_VC102"]
leaving7 = tractData.iloc[:]["HC04_EST_VC103"]
leaving8 = tractData.iloc[:]["HC04_EST_VC104"]
leaving9 = tractData.iloc[:]["HC04_EST_VC105"]
leaving10 = tractData.iloc[:]["HC04_EST_VC106"]
# leavingHome = tractData.iloc[:, [569, 578, 587, 596, 605, 614, 623, 631, 640, 649]]
# print(leavingHome)
#print("max median income: ", medianIncome.max()) = 157500
#print('min median income; ', medianIncome.min()) = 4345
scatterPlot["niceName"] = scatterPlot.iloc[:, 2]
scatterPlot["totalPeople"] = total
scatterPlot["commuttersTakingTransit"] = numTransit
scatterPlot["meanTravelTimeTransit"] = meanTravelTimeTransit
scatterPlot["medianIncome"] = medianIncome
scatterPlot["blackPercentage"] = blackPercentage
scatterPlot["americanIndianPercentage"] = americanIndianPercentage
scatterPlot["asianPercentage"] = asianPercentage
scatterPlot["nativePercentage"] = nativePercentage
scatterPlot["otherPercentage"] = otherPercentage
scatterPlot["twoOrMorePercentage"] = twoOrMorePercentage
scatterPlot["hispanicPercentage"] = hispanicPercentage
scatterPlot["whitePercentage"] = whitePercentage

scatterPlot["leaving1"] = leaving1
scatterPlot["leaving2"] = leaving2
scatterPlot["leaving3"] = leaving3
scatterPlot["leaving4"] = leaving4
scatterPlot["leaving5"] = leaving5
scatterPlot["leaving6"] = leaving6
scatterPlot["leaving7"] = leaving7
scatterPlot["leaving8"] = leaving8
scatterPlot["leaving9"] = leaving9
scatterPlot["leaving10"] = leaving10
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
