# import some things we may need later
#import numpy as np
#import pylab as pl
import matplotlib.pyplot as plt
import matplotlib.dates as md
import datetime as dt
#import matplotlib.dates as d
#import datetime as dt

# Initialize vector(s)
ph_1 = []


# Define a proper binning
rangeStart = 0
rangeEnd = 23

num_bins = 20

counter = 0

# Loop over the data file (saved as data_kaal.txt)
with open('Data/OUTPUTevents-s3001-20211228.txt') as fa:
# Read the data from file
    for line_aa in fa.readlines(): # First 100 lines only, for testing purposes. Remove the range [0:100] in final script
        line_aa = line_aa.strip()
        counter = counter +1
# Read each single column
        col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col17,col18,col19,col20,col21,col22,col23,col24 = line_aa.split('\t',24)
# Now you have all the columns and you can do your analysis. As an example, put column 4 (pulse height in detector 1) in a vector
        #ph_1.append(md.date2num(dt.datetime.fromtimestamp(int(col3))))
        ph_1.append(float(col24))
# Check that everything went well by printing to the screen
print("Lines read: ",counter)
#print(ph_1)
#dateData = mdates.epoch2num(ph_1)

# Fill a histogram to show your data
n, bins, patches = plt.hist(ph_1, num_bins, density = False,  histtype='bar',facecolor='red')

# Print n, bins, patches to the screen to investigate what they mean, remove later
#print(n,bins,patches)

# Add grid and axis labels to the histogram
plt.xlabel(r'Time')
plt.ylabel(r'Counts')        
plt.grid(True)

# Show the plot on the screen
plt.show()