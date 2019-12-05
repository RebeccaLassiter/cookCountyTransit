import numpy as np 
import pandas as pd

tractData = pd.read_csv("commutingByCensusTract.csv", skiprows=(1,2))
print(tractData.head())
print(tractData.iloc[0][0])

#get the total number of people and number of people taking transit
#get the mean travel time for transit
#get the median income
scatterPlot = pd.DataFrame(tractData.iloc[:,0:3]) #keep the geographic info
total = tractData.iloc[:]["HC01_EST_VC01"]
numTransit = tractData.iloc[:]["HC04_EST_VC01"]
meanTravelTimeTransit = tractData.iloc[:]["HC04_EST_VC118"]
medianIncome = tractData.iloc[:]["HC01_EST_VC51"]
#print("max median income: ", medianIncome.max()) = 157500
#print('min median income; ', medianIncome.min()) = 4345
scatterPlot["totalPeople"] = total
scatterPlot["commuttersTakingTransit"] = numTransit
scatterPlot["meanTravelTimeTransit"] = meanTravelTimeTransit
scatterPlot["medianIncome"] = medianIncome


scatterPlot.to_csv("scatterPlotData.csv")
print(scatterPlot)
