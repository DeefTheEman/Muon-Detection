import matplotlib.pyplot as plt

pressureDict = {}
lineDict = {}
pressure = 0

avgPressureList = [] #list for plotting, all pressures from days will be put in here
eventAmountList = [] #list for plotting, number of events from each day will be put in here

for i in range(1,31):
        pressureDict[i] = []
        lineDict[i] = 0

# print(pressureDict)


numLine = 0 

with open('Data/OUTPUTevents-s3001-20211228.txt') as fa:
        for line_aa in fa.readlines(): 
                line_aa = line_aa.strip()

                col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col17,col18,col19,col20,col21,col22,col23,col24 = line_aa.split('\t',23)

                dayNumber = col1.split('-')[2]
                pressureDict[int(dayNumber)].append(col24)

                lineDict[int(dayNumber)] = int(lineDict[int(dayNumber)]) + 1

# print(lineDict)
# print(pressureDict)

dayCounter = 0
totalPressure = 0

for day in pressureDict:
        if dayCounter == 28:
                for pressure in pressureDict[dayCounter]:
                        totalPressure = float(totalPressure) + float(pressure)
                
                numLine = lineDict[dayCounter]
                eventAmountList.append(numLine)
                
                avgPressure = float(totalPressure)/int(numLine)
                avgPressureList.append(avgPressure)
                
                dayCounter += 1
                
        else:
                dayCounter += 1
                continue
        
        # for pressure in pressureDict[dayCounter]:
        #         totalPressure = float(totalPressure) + float(pressure)
        
        # numLine = lineDict[dayCounter]
        # eventAmountList.append(numLine)
        
        # avgPressure = float(totalPressure)/int(numLine)
        # avgPressureList.append(avgPressure)

        
        # dayCounter += 1

print(avgPressureList)
print(eventAmountList)



# print(avgPressure)

# print(pressureDict)
# print(lineDict)