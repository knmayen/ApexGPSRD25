from mappingUI import *
from rollInputUI import *
from pusherInputUI import *
# from timeDataDisplayUI import *
import tkinter
from tkinter import *
from PIL import ImageTk, Image
from commonFunctions import *
import config

loadData()

def mainScreenRun():
    pad = 10

    global mainScreen
    mainScreen = tkinter.Tk()
    mainScreen.geometry(f"{800}x{600}")
    mainScreen.title('Main Screen')

    global title
    title = Label(mainScreen, text = 'ApexGPS Project for RD25')
    title.pack(pady = pad)

    global addRoll
    addRoll = Button(mainScreen, text = 'Add Roll', command= rollInputScreenRun)
    addRoll.pack(pady = pad)

    global pusherAdd
    pusherAdd = Button(mainScreen, text = 'Add Pusher', command= pusherInputScreenRun)
    pusherAdd.pack(pady = pad)

    global mapRolls
    mapRolls = Button(mainScreen, text = 'Map Rolls', command= mapScreenRun)
    mapRolls.pack(pady = pad)

    # global seePusherTimes
    # seePusherTimes = Button(mainScreen, text = 'See Times', command = timesDisplayScreenRun)
    # seePusherTimes.pack(pady = pad)

    # img = ImageTk.PhotoImage(Image.open(r"C:\Users\knmay\OneDrive\Documents\GitHub\ApexGPSRD25\ApexLogoRed.png"))
    # logo = Label(mainScreen, image= img)
    # logo.pack(side = 'bottom', fill = 'both', expand = 'No')


    mainScreen.mainloop()

mainScreenRun()
