import pickle
import tkinter
from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk 
from rollClass import Roll
import pandas

# get all of the pusher names in a sorted list
pusherFile = open(r"C:\Users\knmay\OneDrive\Documents\GitHub\ApexGPSRD25\pusherPickle", 'rb')
allPushers = pickle.load(pusherFile)
pusherFile.close()

pusherNames = [key for key in allPushers]
pusherNames.sort()
print(pusherNames)

# driver and buggy data
drivers = ['Maggie', 'Bella', 'Sara', 'Lily', 'Emma']
buggies = ['Solaris', 'Scorch', 'Helios', 'Firefly', 'Molotov']
allRolls = set()
filename = ''

# rollFile = open(r"C:\Users\knmay\OneDrive\Documents\GitHub\ApexGPSRD25\rollPickle", 'rb')
# allRolls = pickle.load(rollFile)
# rollFile.close()


# def storeData():
#     file = open(r"C:\Users\knmay\OneDrive\Documents\GitHub\ApexGPSRD25\rollPickle", 'wb')
#     pickle.dump(allRolls, file)
#     file.close()



def addRollFile():
    filename = fd.askopenfilename()
    print(filename)
    fileText = Label(rollInputScreen, text = f'{filename}')
    fileText.pack()

def saveRoll():
    # get gpx
    print(filename)
    gpx = pandas.read_csv(filename, sep = '\t')

    infoDict = {}

    infoDict['rollNum'] = int(rollNumEntry.get())
    infoDict['driver']= driverBox.get()
    infoDict['buggy'] = buggyBox.get()
    pushers = []
    for box in hillBoxes:
        pushers.append(box.get())
    # print(pushers)
    for i in range(5):
        infoDict[f'hill{i+1}'] = pushers[i]
    print(infoDict)
    allRolls.add(Roll(gpx, infoDict))
    
def driverFrame():
    lb2 = Label(rollInputScreen, text = 'Driver Input')
    lb2.pack()

    driverInfoFrame = Frame(rollInputScreen)
    driverInfoFrame.pack()

    lb3 = Label(driverInfoFrame, text = "Roll #: ")
    lb3.pack(side = LEFT)
    rollNumEntry = Entry(driverInfoFrame)
    rollNumEntry.pack(side = LEFT)

    lb4 = Label(driverInfoFrame, text = "Driver Name: ")
    lb4.pack(side = LEFT)

    driverVar = StringVar()
    driverBox = ttk.Combobox(driverInfoFrame, textvariable= driverVar )
    driverBox['values'] = drivers
    driverBox.pack(side = LEFT)

    lb5 = Label(driverInfoFrame, text = "Buggy: ")
    lb5.pack(side = LEFT)
    buggyVar = StringVar()
    buggyBox = ttk.Combobox(driverInfoFrame, textvariable= buggyVar )
    buggyBox['values'] = buggies
    buggyBox.pack(side = LEFT)

def pusherFrame():
    lb6 = Label(rollInputScreen, text = 'Pusher Input')
    lb6.pack()

    pusherInfoFrame = Frame(rollInputScreen)
    pusherInfoFrame.pack()
    
    for i in range(1, 6):
        lb = Label(pusherInfoFrame, text = f"Hill {i}: ")
        lb.pack(side = LEFT)

        pusherVar = StringVar()
        box = ttk.Combobox(pusherInfoFrame, textvariable=pusherVar, width = 10)
        hillBoxes.append(box)
        box['values'] = pusherNames
        box.pack(side=LEFT)

    

# actual screen
rollInputScreen = tkinter.Tk()
rollInputScreen.geometry(f"{800}x{600}")

lb1 = Label(rollInputScreen, text = "Roll Input Path:")
lb1.pack()

fileSelectButton = Button(rollInputScreen, text = 'Select Roll .txt File', command = addRollFile)
fileSelectButton.pack()

driverFrame()

hillBoxes = []
pusherFrame()

# save roll button
saveRollButton = Button(rollInputScreen, text = 'Save Roll Data', command = saveRoll)
saveRollButton.pack()

rollInputScreen.mainloop()
