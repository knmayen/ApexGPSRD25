import pandas
import pickle
import tkinter
from tkinter import *
import tkintermapview
import PIL
from PIL import *

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
print(roll1.gpx)

# addRoll(file)

# screen = tkinter.Tk()
# screen.geometry(f"{800}x{600}")
# screen.title('map')

# mapWidget = tkintermapview.TkinterMapView(screen, width = 800, height = 600)
# mapWidget.place(relx = .5, rely = .5, anchor = tkinter.CENTER)

# mapWidget.set_position(41.648136, -70.491481)  
# mapWidget.set_zoom(18)

# # l = Label(screen, text = 'Hello!')
# # l.pack()
# # b = Button(screen, text = 'Click', width = 15)
# # b.pack()
# screen.mainloop()



# file = open(r"C:\Users\knmay\OneDrive\Documents\GitHub\ApexGPSRD25\data.txt", 'r')

# lines = file.readlines()

# for line in lines:
#     print(line)

# var = 'hello'
# pickle.dump(var, file)


# file.close()
# print('here')

# nfile = open(r"C:\Users\knmay\OneDrive\Documents\GitHub\ApexGPSRD25\data.txt", 'rb')
# db = pickle.load(nfile)
# for line in nfile.readlines():
#     print(lines)

# nfile.close()