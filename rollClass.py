import pandas

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



########################################### TESTING DATA AND CALLS ##########################################################

file = pandas.read_csv(r"C:\Users\knmay\OneDrive\Documents\GitHub\ApexGPSRD25\neighborhoodLap.csv")

infoDict = {'rollNum' : 1, 
            'driver' : 'Maggie', 
            'buggy' : 'Solaris', 
            'hill1' : 'Wesley',
            'hill2' : 'Anthony',
            'hill3' : 'Michelle',
            'hill4' : 'Sam G', 
            'hill5' : 'Sam L'}
roll1 = Roll(file, infoDict)
print(roll1)
# print(roll1.gpx)
# print(roll1.hill5)