import tkinter
from tkinter import *
import tkintermapview
import PIL
from PIL import Image, ImageTk
from rollClass import *
import os
from CoordinateData import *
from rollInputUI import allRolls

buggyColors = {
                'Solaris' : 'blue',
                'Scorch' : 'black',
                'Helios' : 'cyan',
                'Firefly' : 'green',
                'Molotov' : 'orange'
}

################################### SCREEN STUFF #######################################

# path by individual dots
def drawDots(self, mapWidget):
    current_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    dotIcon = ImageTk.PhotoImage(Image.open(os.path.join(current_path, r"C:\Users\knmay\OneDrive\Documents\GitHub\ApexGPSRD25\redDot.png")).resize((5, 5)))
    for row in self.gpx.itertuples():
        lat = row[3]
        lon = row[4]
        marker = mapWidget.set_marker(lat, lon, text = '', icon = dotIcon)

# path by polygon
def drawPoints(self, mapWidget):
    L = []
    for row in self.gpx.itertuples():
        lat = row[3]
        lon = row[4]
        L.append((lat, lon))
    rev = L[::-1]
    L.extend(rev)
    color = buggyColors[self.buggy]
    polygon = mapWidget.set_polygon(L, fill_color = None, outline_color = color, border_width = 1)

# transition zone lines
def drawTransitions(self, mapWidget):
    for key in self.coordsDict:
        point1 = self.coordsDict[key][0]
        point2 = self.coordsDict[key][1]
        L = [point1, point2, point1]
        polygon = mapWidget.set_polygon(L, fill_color = None, outline_color = 'blue', border_width = 2)

# not really relevant anymore
def drawBoundingBoxes(self, mapWidget):
    for key in self.bounds:
        # add first point back in
        l = self.bounds[key]
        self.bounds[key] = self.bounds[key] + [self.bounds[key][0]]
        polygon = mapWidget.set_polygon(self.bounds[key], fill_color = None, outline_color = 'purple', border_width = 1)

# for debugging, points in which the timing changes over
def drawHandoffs(self, mapWidget):
    for key in self.splitsDict:
        lat = self.splitsDict[key][1]
        lon = self.splitsDict[key][2]
        # num = self.splitsDict[key][3]
        print(lat, lon)
        marker = mapWidget.set_marker(lat, lon)

# only for debugging, not needed anymore
def drawLines(self, mapWidget):
    for key in self.coordsDict:
        coordsList = self.coordsDict[key]
        x0 = coordsList[0][0]
        y0 = self.getVal(key, x0)
        x1 = coordsList[1][0]
        y1 = self.getVal(key, x1)
        x5 = abs(x0-x1)/2 + x0
        y5 = self.getVal(key, x5)
        
        polygon = mapWidget.set_polygon([(x0, y0), (x5, y5), (x1, y1), (x0, y0)], fill_color = None, outline_color = "purple")

def mapScreenRun():
    # actual screen calls
    mapScreen = tkinter.Tk()
    mapScreen.geometry(f"{800}x{600}")
    mapScreen.title('map')

    mapWidget = tkintermapview.TkinterMapView(mapScreen, width = 800, height = 600)
    mapWidget.pack(fill = 'both', expand = True)

    mapWidget.place(relx = .5, rely = .5, anchor = tkinter.CENTER)

    mapWidget.set_position(41.648136, -70.491481)  
    mapWidget.set_zoom(18)

    # drawDots(allRolls['2024-12-29']['Emma']['2024-12-29-EB-Mol-3'], mapWidget)
    drawPoints(allRolls['2024-12-29']['Emma']['2024-12-29-EB-Mol-3'], mapWidget)
    drawTransitions(mashpeeCoords, mapWidget)
    # drawBoundingBoxes(mashpeeCoords)
    drawHandoffs(allRolls['2024-12-29']['Emma']['2024-12-29-EB-Mol-3'], mapWidget)
    # drawLines(mashpeeCoords)

    mapScreen.mainloop()

mapScreenRun()
