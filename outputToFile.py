
eventFile = 'Data/events-s3001-20211201_20211231.txt'
weatherFile = 'Data/weather-s3001-20211201_20211231.txt'

outputFile = 'Data/' + 'OUTPUT' + str(eventFile.split('/')[1])


with open(eventFile, 'r') as events, open(weatherFile, 'r') as weather:
    eventLines = events.read().splitlines()
    weatherLines = weather.read().splitlines()
    
with open(outputFile, 'w') as output:
    for eventLine in eventLines:
        eventLine = eventLine.strip()
        col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col17,col18,col19,col20,col21,col22,col23 = eventLine.split('\t',23)
        hh, mm, ss = str(col2).split(':')
        Y, M, D = str(col1).split('-')
        seconds = int(D)*86400 + int(hh)*3600 + int(mm)*60 + int(ss)
        lineNumber = round((seconds/(30*24*60*60))*508107)

        try:
            pressure = weatherLines[lineNumber].strip().split('\t', 17)[7]
            output.write(str(eventLine) + '\t' + str(pressure) + '\n')
        except:
            print(lineNumber)
            break