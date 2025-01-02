import tkinter
from tkinter import *
import tkinter as tk

allCells = []
topCols = ['name', 
           'Best \nhill1', 'Avg \nhill1', 
           'Best \nhill2', 'Avg \nhill2',
           'Best \nfreeroll', 'Avg \nfreeroll',
           'Best \nhill3', 'Avg \nhill3',
           'Best \nhill4', 'Avg \nhill4',
           'Best \nhill5', 'Avg \nhill5']

def drawGrid():
    global topY 
    topY = 100
    global leftX
    leftX = 50
    global cellWidth 
    cellWidth = (appWidth - leftX * 2) / cols
    global cellHeight
    cellHeight = (appHeight - topY * 2) / rows
    # cellHeight = 10
    for r in range(rows):
        row = []
        for c in range(cols):
            (x0, y0) = getTopLeft(r, c, cellWidth, cellHeight)
            cell = canvas.create_rectangle(x0, y0, x0 + cellWidth, y0 + cellHeight, fill = None)
            row.append(cell)
        allCells.append(row)
    drawLabels()

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

def back():
    timesDisplayScreen.destroy()

def timesDisplayScreenRun():
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

    # 100 pixels at top for division selections
    # 100 pixels at bottom for balance
    # 50 pixels at on each side for buffer
    global canvas
    canvas = tk.Canvas(timesDisplayScreen, width = appWidth, height = appHeight)
    canvas.place(x = 0, y = 0, anchor='nw')

    drawGrid()

    global backButton 
    backButton = Button(timesDisplayScreen, text = 'Back', command = back)

    timesDisplayScreen.mainloop()

timesDisplayScreenRun()