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
    print(config.allPushers)
    for pusher in config.allPushers:
        getBestTimes(config.allPushers[pusher])
        getAverageTimes(config.allPushers[pusher])

def getBestTimes(pusher):
    # print(config.allPushers[pusher])
    print(pusher, pusher.times, pusher.bestTimes)
    for hill in pusher.times:
        bestTime = None
        for tag in pusher.times[hill]:
            time = pusher.times[hill][tag]
            print(bestTime, time)
            if bestTime == None or time < bestTime:
                pusher.bestTimes[hill] = (time, tag)
                bestTime = time
    print(pusher.bestTimes)

def getAverageTimes(pusher):
    # print(str(pusher), config.allPushers[pusher].avgTimes)
    for hill in pusher.times:
        totalTime = 0
        for tag in pusher.times[hill]:
            time = pusher.times[hill][tag]
            totalTime += time
        pusher.avgTimes[hill] = totalTime
    print(pusher.avgTimes)
        


def drawGrid():
    drawLabels()
    for r in range(rows):
        row = []
        for c in range(cols):
            (x0, y0) = getTopLeft(r, c, cellWidth, cellHeight)
            cell = canvas.create_rectangle(x0, y0, x0 + cellWidth, y0 + cellHeight, fill = None)
            row.append(cell)
        allCells.append(row)

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
    agDivision = IntVar()
    agDivisionBox = Checkbutton(selectionFrame, text = "All Gender", variable = agDivision, 
                           onvalue = 1, offvalue = 0)
    agDivisionBox.pack(side = LEFT, padx= pad)
    global wDivision
    wDivision = IntVar()
    wDivisionBox = Checkbutton(selectionFrame, text = "Womens", variable = wDivision, 
                           onvalue = 1, offvalue = 0)
    wDivisionBox.pack(side = LEFT, padx= pad)
    global mDivision
    mDivision = IntVar()
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
#     displayData(selectionDict)

# def displayData():
#     return 42

def getSelection():
    selectionDict = dict()
    raw = sortChoicesBox.get() 
    selectionDict['category'] = raw[:raw.find('\n')] + raw[raw.find('\n') + 1:]
    selectionDict['All Gender'] = agDivision.get()
    selectionDict['Womens'] = wDivision.get()
    selectionDict['Mens'] = mDivision.get()
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

# timesDisplayScreenRun()