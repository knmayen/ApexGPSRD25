import pickle
import tkinter
from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk 
from rollClass import Roll
from pusherClass import Pusher
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
allRolls = dict()
hillBoxes = []
# filename = ''


# rollFile = open(r"C:\Users\knmay\OneDrive\Documents\GitHub\ApexGPSRD25\rollPickle", 'rb')
# allRolls = pickle.load(rollFile)
# rollFile.close()


# def storeData():
#     file = open(r"C:\Users\knmay\OneDrive\Documents\GitHub\ApexGPSRD25\rollPickle", 'wb')
#     pickle.dump(allRolls, file)
#     file.close()



def addRollFile():
    global filename
    filename = fd.askopenfilename()
    print(filename)
    fileText = Label(rollInputScreen, text = f'{filename}')
    fileText.pack()

def saveRoll(filename):
    error = Label(rollInputScreen, text = "Please Check all Inputs", fg = 'red')
    if checkInputs(filename) == True:
        # get gpx
        gpx = pandas.read_csv(filename, sep = '\t')

        # create the infoDict
        infoDict = {}
        infoDict['rollNum'] = int(rollNumEntry.get())
        infoDict['driver']= driverBox.get()
        infoDict['buggy'] = buggyBox.get()

        for i in range(len(hillBoxes)):
            box = hillBoxes[i]
            pusher = box.get()
            infoDict[f'hill{i+1}'] = pusher

        # get tag for the dictionary
        driverTag = getDriverTag(infoDict['driver'])
        date = getDate(gpx)
        tag = date + '-' + driverTag + '-' + infoDict['buggy'][0] + '-' + str(infoDict['rollNum'])
        print('tag: ', tag)
        
        # add to dictionary
        allRolls[tag] = Roll(gpx, infoDict)
        print(allRolls)

        error.pack_forget()

        clearInputs()
        assignSplits(tag, infoDict)
    else:
        error.pack()

# there is a bug here with filename AHHHHHHHHHHHH
def checkInputs(filename):
    boxes = [driverBox, buggyBox, rollNumEntry] + hillBoxes
    for box in boxes:
        if box.get() == '':
            return False
        
    if filename == '':
        return False
    
    return True

def getDate(gpx):
    date = gpx.at[1, 'time']
    date = date[:date.find(' ')]
    return date

# adds their last intial to the first inital of their name
def getDriverTag(driver):
    if driver == 'Maggie':
        lastInitial = 'B'
    elif driver == 'Bella':
        lastInitial = 'C'
    elif driver == 'Sara':
        lastInitial = 'O'
    elif driver == 'Lily':
        lastInitial = 'Q'
    elif driver == 'Emma':
        lastInitial = 'B'
    return driver[0] + lastInitial

# deal with filename
def clearInputs():
    boxes = [driverBox, buggyBox] + hillBoxes
    print(boxes)
    for box in boxes:
        box.set('')
    rollNumEntry.delete(0, tkinter.END)

def assignSplits(tag, infoDict):
    print(allRolls[tag].hillTimes)
    # reverse dictionary so it is pusher : hill
    revDict = dict()
    for hill in allRolls[tag].hillTimes:
        if 'hill' in hill:
            pusher = allRolls[tag].hillTimes[hill]
            revDict[pusher] = (hill

    # loop through reversed dictonary and add times from allrolls[tag].hillTimes to pusher instances
        # pusher hill properties are a dictionary of hills with nested dicts, inseter tag : time


    


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

# Driver Frame 
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


pusherFrame()

# save roll button
saveRollButton = Button(rollInputScreen, text = 'Save Roll Data', command = lambda : saveRoll(filename))
saveRollButton.pack()

rollInputScreen.mainloop()
