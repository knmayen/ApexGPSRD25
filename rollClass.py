import pandas
import copy
from CoordinateData import *

class Roll:
    def __init__(self, rawGPX, infoDict):
        self.rollNum = infoDict['rollNum']
        self.driver = infoDict['driver']
        self.buggy = infoDict['buggy']
        self.hill1 = infoDict['hill1']
        self.hill2 = infoDict['hill2']
        self.hill3 = infoDict['hill3']
        self.hill4 = infoDict['hill4']
        self.hill5 = infoDict['hill5']
        self.getDateAndResetTimes(rawGPX)

    def __repr__(self):
        return f'Roll Number {self.rollNum} for {self.driver} in {self.buggy} on {self.date}'
    
    def __eq__(self, other):
        if (self.date == other.date) and (self.rollNum == other.rollNum) and (self.driver == other.driver):
            return True
        return False
    
    def getDateAndResetTimes(self, rawGPX):
        # get the initial date from the timing data
        self.date = rawGPX.at[1, 'time']
        self.date = self.date[:self.date.find(' ')]

        # go through the timing data and cut the date out of it
        i = 0
        for row in rawGPX.itertuples():
            full = row[2]
            partial = full[full.find(" ") :]
            rawGPX.at[i, 'time'] = partial
            i += 1
        self.gpx = rawGPX

    def getSplits(self, coords):
        # start looping through the gps pings

        currentSplitChecking = 0 # maps to the index of the split list that is being checked
        for row in self.gpx.itertuples():
            lat = row[3]
            lon = row[4]
            # check if coor is in bonding box
                # if so, store time and move on to next split
                # if at last split, exit
            # if not, continue


########################################### TESTING DATA AND CALLS ##########################################################

# def dateparse (timestamp):
#     return pandas.to_datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')

# file = pandas.read_csv(r"C:\Users\knmay\OneDrive\Documents\GitHub\ApexGPSRD25\neighborhoodLap.csv", parse_dates=['time'], date_parser=dateparse)

file = pandas.read_csv(r"C:\Users\knmay\OneDrive\Documents\GitHub\ApexGPSRD25\neighborhoodLap.csv")

infoDict = {'rollNum' : 1, 
            'driver' : 'Maggie', 
            'buggy' : 'Solaris', 
            'hill1' : 'Wesley',
            'hill2' : 'Anthony',
            'hill3' : 'Michelle',
            'hill4' : 'Sam G', 
            'hill5' : 'Sam L'}
roll1 = Roll(copy.deepcopy(file), infoDict)

# print(roll1)
# print(roll1 == roll2)

print(roll1.gpx)
# print(roll1.hill5)