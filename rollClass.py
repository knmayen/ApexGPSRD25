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
        self.getSplits(mashpeeCoords)

    def __repr__(self):
        return f'Roll Number {self.rollNum} for {self.driver} in {self.buggy} on {self.date}'
    
    def __eq__(self, other):
        if (self.date == other.date) and (self.rollNum == other.rollNum) and (self.driver == other.driver):
            return True
        return False
    
    # gets the date of the roll, and cuts the date out of every timestamp
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

    # gets the timing splits, creates a dictionary of the handoff times
    def getSplits(self, coords):
        # start looping through the gps pings
        self.splitsDict = dict()
        currentSplitChecking = 0 # maps to the index of the split list that is being checked
        threshold = .001
        for row in self.gpx.itertuples():
            lat = row[3]
            lon = row[4]
            split = coords.orderedList[currentSplitChecking]
            # get y value of current split and position
            y = coords.getVal(split, lat)
            print(y, lon, abs(y - lon), split)
            x0 = coords.coorsDict[split][0][0]

            # check if coor is in bonding box
            if abs(y - lon) < threshold and abs(x0 - lat) < threshold:     # within 10 feet
                # if so, store time and move on to next split
                self.splitsDict[split] = [row[2], lat, lon, currentSplitChecking]
                if currentSplitChecking < len(coords.orderedList) - 1:
                    currentSplitChecking += 1
                # if at last split, exit
            # if not, continue
        print('splitsDict')
        print(self.splitsDict)


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

print(roll1)
# print(roll1 == roll2)

# print(roll1.gpx)
# print(roll1.hill5)
print('DEBUGGING HERE')
print(mashpeeCoords.getVal('Hill 1/Hill 2', 41.648226))