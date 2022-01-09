from statistics import mean

pressureList = []

with open('Data/weather-s3001-20211228.txt') as fa:
# Read the data from file
    for line_aa in fa.readlines(): # First 100 lines only, for testing purposes. Remove the range [0:100] in final script
        line_aa = line_aa.strip()
# Read each single column
        col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col17 = line_aa.split('\t',17)
# Now you have all the columns and you can do your analysis. As an example, put column 4 (pulse height in detector 1) in a vector
        #ph_1.append(md.date2num(dt.datetime.fromtimestamp(int(col3))))
        pressureList.append(float(col8))
    
print(mean(pressureList))
        
        