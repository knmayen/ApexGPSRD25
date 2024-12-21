import tkinter
from tkinter import *
import tkintermapview
import PIL
from PIL import Image, ImageTk
from rollClass import *
import os
from CoordinateData import *

roll1 = Roll(file, infoDict)



################################### SCREEN STUFF #######################################

# path by individual dots
def drawDots(self):
    current_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    dotIcon = ImageTk.PhotoImage(Image.open(os.path.join(current_path, r"C:\Users\knmay\OneDrive\Documents\GitHub\ApexGPSRD25\redDot.png")).resize((5, 5)))
    for row in self.gpx.itertuples():
        lat = row[3]
        lon = row[4]
        marker = mapWidget.set_marker(lat, lon, text = '', icon = dotIcon)

# path by polygon
def drawPoints(self):
    L = []
    for row in self.gpx.itertuples():
        lat = row[3]
        lon = row[4]
        L.append((lat, lon))
    rev = L[::-1]
    L.extend(rev)
    polygon = mapWidget.set_polygon(L, fill_color = None, outline_color = 'red', border_width = 1)

# transition zone lines
def drawTransitions(self):
    for key in self.coorsDict:
        point1 = self.coorsDict[key][0]
        point2 = self.coorsDict[key][1]
        L = [point1, point2, point1]
        polygon = mapWidget.set_polygon(L, fill_color = None, outline_color = 'blue', border_width = 2)

# not really relevant anymore
def drawBoundingBoxes(self):
    for key in self.bounds:
        # add first point back in
        l = self.bounds[key]
        self.bounds[key] = self.bounds[key] + [self.bounds[key][0]]
        polygon = mapWidget.set_polygon(self.bounds[key], fill_color = None, outline_color = 'purple', border_width = 1)

# for debugging, points in which the timing changes over
def drawHandoffs(self):
    for key in self.splitsDict:

        lat = self.splitsDict[key][1]
        lon = self.splitsDict[key][2]
        num = self.splitsDict[key][3]
        print(lat, lon)
        marker = mapWidget.set_marker(lat, lon, text = num)

# only for debugging, not needed anymore
def drawLines(self):
    for key in self.coorsDict:
        coorsList = self.coorsDict[key]
        x0 = coorsList[0][0]
        y0 = self.getVal(key, x0)
        x1 = coorsList[1][0]
        y1 = self.getVal(key, x1)
        x5 = abs(x0-x1)/2 + x0
        y5 = self.getVal(key, x5)
        
        polygon = mapWidget.set_polygon([(x0, y0), (x5, y5), (x1, y1), (x0, y0)], fill_color = None, outline_color = "purple")


# actual screen calls
screen = tkinter.Tk()
screen.geometry(f"{800}x{600}")
screen.title('map')

mapWidget = tkintermapview.TkinterMapView(screen, width = 800, height = 600)
mapWidget.pack(fill = 'both', expand = True)

mapWidget.place(relx = .5, rely = .5, anchor = tkinter.CENTER)

mapWidget.set_position(41.648136, -70.491481)  
mapWidget.set_zoom(18)

drawDots(roll1)
# drawPoints(roll1)
drawTransitions(mashpeeCoords)
# drawBoundingBoxes(mashpeeCoords)
drawHandoffs(roll1)
# drawLines(mashpeeCoords)

screen.mainloop()