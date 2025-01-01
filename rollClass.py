import pandas
import copy
from CoordinateData import *
from datetime import datetime

class Roll:
    def __init__(self, rawGPX, infoDict, filename):
        self.path = filename
        self.rollNum = infoDict['rollNum']
        self.driver = infoDict['driver']
        self.buggy = infoDict['buggy']
        self.hill1 = infoDict['hill1']
        self.hill2 = infoDict['hill2']
        self.hill3 = infoDict['hill3']
        self.hill4 = infoDict['hill4']
        self.hill5 = infoDict['hill5']
        self.info = infoDict
        self.getDateAndResetTimes(rawGPX)
        self.getSplits(mashpeeCoords)

    def __repr__(self):
        return f'Roll Number {self.rollNum} for {self.driver} in {self.buggy} on {self.date}'
    
    def __eq__(self, other):
        if (type(other) == type(self)) and (self.date == other.date) and (self.rollNum == other.rollNum) and (self.driver == other.driver):
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
            partial = full[full.find(" ")  + 1:]
            rawGPX.at[i, 'time'] = partial
            i += 1
        self.gpx = rawGPX
 
    # gets the timing splits, creates a dictionary of the handoff times
    def getSplits(self, coords):
        self.getClosePoints(coords)
        self.getBestPoints()
        self.getHillTimes()

    # gets the points close to each split
    def getClosePoints(self, coords):
        self.closePoints = dict()
        currentSplitChecking = 0 # maps to the index of the split list that is being checked
        threshold = .00007
        # start looping through the gps pings
        foundOne = False

        for row in self.gpx.itertuples():
            lat = row[3]
            lon = row[4]
            split = coords.orderedList[currentSplitChecking]
            dist1, dist2 = coords.getDoubleDist(lat, lon, split)

            if dist1 < threshold or dist2 < threshold:
                self.closePoints[split] = self.closePoints.get(split, []) + [(row[2], lat, lon, dist1 + dist2, currentSplitChecking)]
                foundOne = True

            elif foundOne:
                currentSplitChecking += 1
                foundOne = False

                if currentSplitChecking > len(coords.orderedList) - 1:
                    break

    # finds the closest point to each split from the close points dictionary created
    def getBestPoints(self):
        self.splitsDict = dict()

        for key in self.closePoints:
            points = self.closePoints[key]
            bestDistance = 10
            bestPoint = (0,0)

            for time, lat, lon, dist, n in points:
                if dist < bestDistance:
                    bestDistance = dist
                    bestPoint = (time, lat, lon)
                
            self.splitsDict[key] = bestPoint

    def getHillTimes(self):
        self.hillTimes = dict()

        for key in self.splitsDict:
            time = self.splitsDict[key][0]
            time = datetime.strptime(time, "%H:%M:%S")

            for elem in key.split('/'):

                if elem in self.hillTimes:
                    print(time, self.hillTimes[elem], self.hillTimes['Start'])
                    self.hillTimes[elem] = (time - self.hillTimes[elem]).total_seconds()
 
                else:
                    self.hillTimes[elem] = time

        # get the finish time as the total time
        self.hillTimes['Finish'] = (self.hillTimes['Finish'] - self.hillTimes['Start']).total_seconds()
        # get the start time as the starting timestamp
        self.hillTimes['Start'] = self.hillTimes['Start'].strftime("%H:%M:%S")

        
            
########################################### TESTING DATA AND CALLS ##########################################################

# file = pandas.read_csv(r"C:\Users\knmay\OneDrive\Documents\GitHub\ApexGPSRD25\neighborhoodLap.csv", parse_dates=['time'], date_parser=dateparse)

# file = pandas.read_csv(r"C:\Users\knmay\OneDrive\Documents\GitHub\ApexGPSRD25\NeighborhoodLap2.txt", sep = '\t')

# infoDict = {'rollNum' : 1, 
#             'driver' : 'Maggie', 
#             'buggy' : 'Solaris', 
#             'hill1' : 'Wesley',
#             'hill2' : 'Anthony',
#             'hill3' : 'Michelle',
#             'hill4' : 'Sam G', 
#             'hill5' : 'Sam L'}
# roll1 = Roll(copy.deepcopy(file), infoDict)

# # print(roll1)
# # print(roll1 == roll2)
# print(roll1.date)
# print(roll1.gpx)

# print(roll1.gpx['time'])
# print(roll1.hill5)
# print('DEBUGGING HERE')
# print(roll1.splitsDict)