import pickle
import tkinter
from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk 
from rollClass import Roll
from pusherClass import Pusher
import pandas

# load pusher data, get all of the pusher names in a sorted list
pusherFile = open(r"C:\Users\knmay\OneDrive\Documents\GitHub\ApexGPSRD25\pusherPickle", 'rb')
allPushers = pickle.load(pusherFile)
pusherFile.close()

pusherNames = [key for key in allPushers]
pusherNames.sort()


# load rolls Data
rollFile = open(r"C:\Users\knmay\OneDrive\Documents\GitHub\ApexGPSRD25\rollPickle", 'rb')
allRolls = pickle.load(rollFile)
rollFile.close()

# driver and buggy data
drivers = ['Maggie', 'Bella', 'Sara', 'Lily', 'Emma']
buggies = ['Solaris', 'Scorch', 'Helios', 'Firefly', 'Molotov']
hillBoxes = []
filename = ''

def getAllTags(dict, tags = []):
    for key in dict:
        if type(dict[key]) != type(dict):
            for tag in dict:
                tags.append(tag)
            return tags
        else:
            tags =  getAllTags(dict[key], tags)
    return tags

allTags = getAllTags(allRolls)


def addRollFile():
    global filename
    filename = fd.askopenfilename()
    print(filename)
    fileText.config(text = f'{filename}')

def saveRoll():
    global filename

    if checkInputs() == True:
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
        tag = date + '-' + driverTag + '-' + infoDict['buggy'][0:3] + '-' + str(infoDict['rollNum'])
        
        # add to dictionary
        createSubdictionaries(date, infoDict, tag)
        allRolls[date][infoDict['driver']][tag] = Roll(gpx, infoDict, filename)
        allTags.append(tag)
        print(allRolls)
        error.pack_forget()

        clearInputs()
        assignSplits(date, tag, infoDict)
        storeData()
        updateListbox()

    else:
        if not error.winfo_ismapped():
            error.pack()

def createSubdictionaries(date, infoDict, tag):
    allRolls[date] = allRolls.get(date, dict())
    driver = infoDict['driver']
    allRolls[date][driver] = allRolls[date].get(driver, dict())
    allRolls[date][driver][tag] = allRolls[date][driver].get(tag, dict())

def checkInputs():
    global filename
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

def clearInputs():
    boxes = [driverBox, buggyBox] + hillBoxes

    for box in boxes:
        box.set('')
    rollNumEntry.delete(0, tkinter.END)
    fileText.config(text = '')

def assignSplits(date, tag, infoDict):

    # reverse dictionary so it is pusher : hill
    revDict = dict()
    for hill in infoDict:
        if 'hill' in hill:
            pusher = infoDict[hill]
            revDict[pusher] = (hill)


    # loop through reversed dictonary and add times from allrolls[tag].hillTimes to pusher instances
        # pusher hill properties are a dictionary of hills with nested dicts, inseter tag : time
    for pusher in revDict:
        hill = revDict[pusher]
        allPushers[str(pusher)].times[hill].update({tag : allRolls[date][infoDict['driver']][tag].hillTimes[hill]})
        if hill == 'hill1' or hill == 'hill2':
             allPushers[str(pusher)].times['Freeroll'].update({tag : allRolls[date][infoDict['driver']][tag].hillTimes['Freeroll']})

def storeData():
    file = open(r"C:\Users\knmay\OneDrive\Documents\GitHub\ApexGPSRD25\pusherPickle", 'wb')
    pickle.dump(allPushers, file)
    file.close()

    file = open(r"C:\Users\knmay\OneDrive\Documents\GitHub\ApexGPSRD25\rollPickle", 'wb')
    pickle.dump(allRolls, file)
    # pickle.dump(dict(), file)
    file.close()

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

def updateListbox():
    global allTags
    rollListbox.delete(0, tkinter.END)  # Clear the existing items
    print('allTags: ', allTags)
    for item in allTags:
        rollListbox.insert(tkinter.END, item)

def checkSelection():
    if rollListbox.curselection() != ():
        selection = rollListbox.curselection()
        print(selection)
        showRollInfo(selection)
    rollInputScreen.after(1000, checkSelection)

def showRollInfo(selection):
    print(selection)
    print(allRolls)
    tag = allTags[selection[0]]
    roll = findRoll(allRolls, tag)
    print(roll)
    print(roll.info)

    infoString = createInfoString(roll)
    infoLabel.config(text = infoString)
    

# this dosn't work right now
def findRoll(dict, tag):
    for key in dict:
        if key == tag:
            return dict[key]
        elif type(dict[key]) == type(dict):
            solution = findRoll(dict[key], tag)
            if solution != None:
                return solution
            
def createInfoString(roll):
    result = f''
    for key in roll.info:
        if key == 'rollNum':
            continue
        result = result + f'{str(key)}: {roll.info[str(key)]} \n'
    return result



# actual screen
rollInputScreen = tkinter.Tk()
rollInputScreen.geometry(f"{800}x{600}")

lb1 = Label(rollInputScreen, text = "Roll Input Path:")
lb1.pack()

fileSelectButton = Button(rollInputScreen, text = 'Select Roll .txt File', command = addRollFile)
fileSelectButton.pack()
fileText = Label(rollInputScreen, text = '')
fileText.pack()

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
saveRollButton = Button(rollInputScreen, text = 'Save Roll Data', command = saveRoll)
saveRollButton.pack()

error = Label(rollInputScreen, text = "Please Check all Inputs", fg = 'red')

rollInfoFrame = Frame(rollInputScreen)
rollInfoFrame.pack()

stringRolls = tkinter.StringVar(value = allTags)
rollListbox = Listbox(rollInfoFrame, listvariable = stringRolls, width = 25, height = 20)
updateListbox()
rollListbox.pack(side = LEFT)

infoLabel = Label(rollInfoFrame, text ='')
infoLabel.pack(side = LEFT)
checkSelection()



rollInputScreen.mainloop()
