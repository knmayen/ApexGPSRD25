import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk
from commonFunctions import *
from config import *
from pusherClass import Pusher

allCells = []
topCols = ['name', 
           'Best \nhill1', 'Avg \nhill1', 
           'Best \nhill2', 'Avg \nhill2',
           'Best \nfreeroll', 'Avg \nfreeroll',
           'Best \nhill3', 'Avg \nhill3',
           'Best \nhill4', 'Avg \nhill4',
           'Best \nhill5', 'Avg \nhill5']

# find the best and average hill time for each pusher and each hill 
def updatePusherBests():
    # print(config.allPushers)
    for pusher in config.allPushers:
        getBestTimes(config.allPushers[pusher])
        getAverageTimes(config.allPushers[pusher])

def getBestTimes(pusher):
    # print(config.allPushers[pusher])
    # print(pusher, pusher.times, pusher.bestTimes)
    for hill in pusher.times:
        bestTime = None
        for tag in pusher.times[hill]:
            time = pusher.times[hill][tag]
            if bestTime == None or time < bestTime:
                pusher.bestTimes[hill] = (time, tag)
                bestTime = time
        # print(pusher, hill, 'best', bestTime)
    # print(pusher.bestTimes)

def getAverageTimes(pusher):
    # print(str(pusher), config.allPushers[pusher].avgTimes)
    for hill in pusher.times:
        totalTime = 0
        for tag in pusher.times[hill]:
            time = pusher.times[hill][tag]
            totalTime += time
        if len(pusher.times[hill]) > 0:
            pusher.avgTimes[hill] = totalTime / len(pusher.times[hill])
            # print(pusher, hill, 'average', totalTime / len(pusher.times[hill]))
        else:
            pusher.avgTimes[hill] = None
        

# starting the actual display for the grid
def drawGrid():
    drawLabels()
    for r in range(rows):
        row = []
        for c in range(cols):
            (x0, y0) = getTopLeft(r, c, cellWidth, cellHeight)
            cell = canvas.create_rectangle(x0, y0, x0 + cellWidth, y0 + cellHeight, fill = None)
            row.append(cell)
        allCells.append(row)
    updateDisplay()

def drawLabels():
    for c in range(cols):
        (x0, y0) = getTopLeft(0, c, cellWidth, cellHeight)
        centerX = x0 + cellWidth / 2
        centerY = y0 + cellHeight / 2
        lb = Label(canvas, text = topCols[c])
        lb.place(x = centerX, y = centerY, anchor = 'center')

def getTopLeft(r, c, cellWidth, cellHeight):
    x0 = leftX + c * cellWidth
    y0 = topY + r * cellHeight 
    return (x0, y0)

def displaySelectionFrame():
    pad = 20
    selectionFrame = Frame(canvas)
    selectionFrame.place(x = appWidth // 2, y = topY // 2, anchor = 'center')
    lb1 = Label(selectionFrame, text = 'Divisions: ')
    lb1.pack(side = LEFT, padx= pad)
    global agDivision
    agDivision = IntVar(selectionFrame)
    agDivisionBox = Checkbutton(selectionFrame, text = "All Gender", variable = agDivision, 
                           onvalue = 1, offvalue = 0)
    agDivisionBox.pack(side = LEFT, padx= pad)
    global wDivision
    wDivision = IntVar(selectionFrame)
    wDivisionBox = Checkbutton(selectionFrame, text = "Womens", variable = wDivision, 
                           onvalue = 1, offvalue = 0)
    wDivisionBox.pack(side = LEFT, padx= pad)
    global mDivision
    mDivision = IntVar(selectionFrame)
    mDivisionBox = Checkbutton(selectionFrame, text = "Mens", variable = mDivision, 
                           onvalue = 1, offvalue = 0)
    mDivisionBox.pack(side = LEFT, padx= pad)

    lb2 = Label(selectionFrame, text = 'Sort By:')
    lb2.pack(side=LEFT)
    sortChoices = StringVar()
    global sortChoicesBox
    sortChoicesBox = ttk.Combobox(selectionFrame, textvariable= sortChoices)
    sortChoicesBox['values'] = topCols
    sortChoicesBox.pack(side = LEFT, padx = pad // 2)

    global showDataButton
    showDataButton = Button(selectionFrame, text = 'Show Selection', command = updateDisplay)
    showDataButton.pack(side = LEFT, padx = pad)

def updateDisplay():
    selectionDict = getSelection()
    names = getSortedNames(selectionDict)
#   displayData(selectionDict)

def getSortedNames(selectionDict):
    print(selectionDict)
    names = getPushersInDivision(selectionDict)
    print(names)
    if selectionDict['category'] == 'name':
        return names.sort()
    else:
        type = selectionDict['category'][:selectionDict['category'].find('\n')]
        hill = selectionDict['category'][selectionDict['category'].find('\n'):]
        print(type, hill)
        namesDict = dict()
        for pusher in names:
            if type == 'Best':
                namesDict[config.allPushers[pusher].bestTimes[hill]] = pusher
        print(namesDict)



def getPushersInDivision(selectionDict):
    print(config.allPushers)
    divs = ['ag', 'w', 'm']
    pushers = set()
    for div in divs:
        print(selectionDict[div]) 
        if selectionDict[div] == 1:
            print('div', div)
            for pusher in config.allPushers:
                if getattr(config.allPushers[pusher], div) == 1:
                    pushers.add(pusher)
    return list(pushers)

# def displayData():
#     return 42

def getSelection():
    selectionDict = dict()
    raw = sortChoicesBox.get() 
    if raw == 'name':
        selectionDict['category'] = 'name'
    else:
        selectionDict['category'] = raw[:raw.find('\n')] + raw[raw.find('\n') + 1:]
    selectionDict['ag'] = agDivision.get()
    selectionDict['w'] = wDivision.get()
    selectionDict['m'] = mDivision.get()
    return selectionDict


def timesDisplayScreenRun():

    updatePusherBests()

    global timesDisplayScreen
    timesDisplayScreen = tkinter.Tk()
    global appWidth
    appWidth = 800
    global appHeight
    appHeight = 600
    timesDisplayScreen.geometry(f'{appWidth}x{appHeight}')
    timesDisplayScreen.title('Times Display')
 
    global rows
    rows = 11
    global cols
    cols = 13
    global topY 
    topY = 75
    global leftX
    leftX = 50
    global cellWidth 
    cellWidth = (appWidth - leftX * 2) / cols
    global cellHeight
    cellHeight = (appHeight - topY * 2 - 5) / rows

   
    global canvas
    canvas = tk.Canvas(timesDisplayScreen, width = appWidth, height = appHeight)
    canvas.place(x = 0, y = 0, anchor='nw')

    displaySelectionFrame()
    

    drawGrid()


    # global backButton 
    # backButton = Button(canvas, text = 'Back', command = lambda : back(timesDisplayScreen))

    timesDisplayScreen.mainloop()

timesDisplayScreenRun()