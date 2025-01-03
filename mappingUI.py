import tkinter
from tkinter import *
import tkintermapview
import PIL
from PIL import Image, ImageTk
from rollClass import *
import os
from CoordinateData import *
from rollInputUI import allRolls
from commonFunctions import *

buggyColors = {
                'Solaris' : 'blue',
                'Scorch' : 'black',
                'Helios' : 'cyan',
                'Firefly' : 'green',
                'Molotov' : 'orange'
}

################################### SCREEN STUFF #######################################

# path by individual dots
def drawDots(roll):
    current_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    dotIcon = ImageTk.PhotoImage(Image.open(os.path.join(current_path, r"C:\Users\knmay\OneDrive\Documents\GitHub\ApexGPSRD25\redDot.png")).resize((5, 5)))
    for row in roll.gpx.itertuples():
        lat = row[3]
        lon = row[4]
        marker = mapWidget.set_marker(lat, lon, text = '', icon = dotIcon)

# path by polygon
def drawPoints(roll):
    L = []
    for row in roll.gpx.itertuples():
        lat = row[3]
        lon = row[4]
        L.append((lat, lon))
    rev = L[::-1]
    L.extend(rev)
    color = buggyColors[roll.buggy]
    polygon = mapWidget.set_polygon(L, fill_color = None, outline_color = color, border_width = 1)

# transition zone lines
def drawTransitions(coords):
    for key in coords.coordsDict:
        point1 = coords.coordsDict[key][0]
        point2 = coords.coordsDict[key][1]
        L = [point1, point2, point1]
        polygon = mapWidget.set_polygon(L, fill_color = None, outline_color = 'blue', border_width = 2)

# for debugging, points in which the timing changes over
def drawHandoffs(roll):
    for key in roll.splitsDict:
        lat = roll.splitsDict[key][1]
        lon = roll.splitsDict[key][2]
        marker = mapWidget.set_marker(lat, lon)


def mapScreenRun():
    # actual screen calls
    global mapScreen
    mapScreen = tkinter.Tk()
    width = 800
    height = 600
    mapScreen.geometry(f"{width}x{height}")
    mapScreen.title('map')

    global mapWidget
    mapWidget = tkintermapview.TkinterMapView(mapScreen, width = 800, height = 600)
    mapWidget.pack(fill = 'both', expand = True)

    mapWidget.place(relx = .5, rely = .5, anchor = tkinter.CENTER)

    mapWidget.set_position(41.648136, -70.491481)  
    mapWidget.set_zoom(18)

    # drawDots(allRolls['2024-12-29']['Emma']['2024-12-29-EB-Mol-3'])
    drawPoints(allRolls['2024-12-29']['Emma']['2024-12-29-EB-Mol-3'])
    drawTransitions(mashpeeCoords)
    drawHandoffs(allRolls['2024-12-29']['Emma']['2024-12-29-EB-Mol-3'])

    global backButton 
    backButton = Button(mapScreen, text = 'Back', command = lambda: back(mapScreen))
    backButton.place(x = width - 50, y = height - 50, anchor = "center")

    mapScreen.mainloop()

# mapScreenRun()
