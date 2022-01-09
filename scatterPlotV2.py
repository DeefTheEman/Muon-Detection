import matplotlib.pyplot as plt
import statistics
import numpy as np

dataFolder = 'Data'
dataFileExtension = '.txt'

eventFile = 'events-s8004-20211201_20211231'
weatherFile = 'weather-s8004-20211201_20211231'

stationName = '8004: Universiteit Eindhoven 2'

imageFolder = 'Images'

monthName = 'December'
daysInMonth = 31

#Check if the event and weather file have the same station and the same date(s)
if eventFile.split('-')[1] == weatherFile.split('-')[1] and eventFile.split('-')[2] == weatherFile.split('-')[2]:
    pass
else:
    raise Exception('The event and weather file are not compatible')

eventList = []
pressureDict = {}
avgPressureList = []

#Create empty lists and dictionaries with lists inside them, so that if there is a lack of data for one day
#it is immediately obvious. This prevents days from the eventlist to be paired up with the wrong days from the pressurelist
for i in range(1, daysInMonth):
    eventList.append(0)
    avgPressureList.append(0)
    pressureDict[i] = []

# print(eventList)
# print(pressureDict)
# print('\n')

#reading the event file and creating a list, with each item being the number of events that day
with open(dataFolder + '/' + eventFile + dataFileExtension) as events:
    for eventLine in events.readlines():
        if eventLine[0] == '#':
            continue
        else:
            pass
        col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col17,col18,col19,col20,col21,col22,col23 = eventLine.split('\t',23)
        # if int(col5) >= 200 and int(col6) >= 200:
        #     dayNumber = int(col1.split('-')[2])
        #     eventList[dayNumber - 1] = eventList[dayNumber - 1] + 1
        # else:
        #     continue
        dayNumber = int(col1.split('-')[2])
        eventList[dayNumber - 1] = eventList[dayNumber - 1] + 1

#reading the weather file and making a dictionary with the day as a key and all the registered pressures from that day in a list
with open(dataFolder + '/' + weatherFile + dataFileExtension) as weather:
    for weatherLine in weather.readlines():
        if weatherLine[0] == '#':
            continue
        else:
            pass
        col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col17 = weatherLine.split('\t',17)

        dayNumber = int(col1.split('-')[2])
        pressureDict[dayNumber].append(float(col8))

# print(eventList)
# print(pressureDict)

#creating a list using the average pressures, each item will be one day
for day in range(1, daysInMonth):
    try:
        avgPressureList[day - 1] = round(statistics.mean(pressureDict[day]), 2)
    except KeyError:
        print(f'ERROR: MISSING DAY {day}')


# print('\n')
# print(eventList)
# print(len(eventList))
# print(avgPressureList)
# print(len(avgPressureList))

fig, ax = plt.subplots()
ax.scatter(eventList, avgPressureList)
ax.set_ylabel('Gemiddelde luchtdruk per dag (hPa)')
ax.set_xlabel('Metingen per dag')
ax.set_title(f'Aantal metingen en luchtdruk meetstation {stationName}\n{monthName} 2021 ')

z = np.polyfit(eventList, avgPressureList, 1)
p = np.poly1d(z)
plt.plot(eventList, p(eventList), '-')
correlation_matrix = np.corrcoef(eventList, avgPressureList)
correlation_xy = correlation_matrix[0,1]
r_squared = correlation_xy**2

plt.figtext(.7, .8, f'R = {round(correlation_xy, 4)}')
plt.figtext(.7, .75, f'R^2 = {round(r_squared, 4)}')

plt.savefig(imageFolder + '/' + eventFile + 'IMAGE.png')

plt.show()