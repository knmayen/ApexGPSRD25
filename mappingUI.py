import tkinter
from tkinter import *
import tkintermapview
import PIL
from PIL import Image, ImageTk
from rollClass import *
import os

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



################################### SCREEN STUFF #######################################

def drawPoints(self):

    # current_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    # dotIcon = ImageTk.PhotoImage(Image.open(os.path.join(current_path, r"C:\Users\knmay\OneDrive\Documents\GitHub\ApexGPSRD25\redDot.png")).resize((5, 5)))
    L = []
    for row in self.gpx.itertuples():
        lat = row[3]
        lon = row[4]
        # marker = mapWidget.set_marker(lat, lon, text = '', icon = dotIcon)
        L.append((lat, lon))
    rev = L[::-1]
    L.extend(rev)
    # print(L)
    polygon = mapWidget.set_polygon(L, fill_color = None, outline_color = 'red', border_width = 1)


screen = tkinter.Tk()
screen.geometry(f"{800}x{600}")
screen.title('map')

mapWidget = tkintermapview.TkinterMapView(screen, width = 800, height = 600)
mapWidget.pack(fill = 'both', expand = True)

mapWidget.place(relx = .5, rely = .5, anchor = tkinter.CENTER)

mapWidget.set_position(41.648136, -70.491481)  
mapWidget.set_zoom(18)


drawPoints(roll1)


screen.mainloop()