from mappingUI import mapScreenRun
from rollInputUI import rollInputScreenRun
from pusherInputUI import pusherInputScreenRun
import tkinter
from tkinter import *
from PIL import ImageTk, Image

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

    global addPusher
    addPusher = Button(mainScreen, text = 'Add Pusher', command= pusherInputScreenRun)
    addPusher.pack(pady = pad)

    global mapRolls
    mapRolls = Button(mainScreen, text = 'Map Rolls', command= mapScreenRun)
    mapRolls.pack(pady = pad)

    # global seePusherTimes

    img = ImageTk.PhotoImage(Image.open(r"C:\Users\knmay\OneDrive\Documents\GitHub\ApexGPSRD25\ApexLogoRed.png"))
    logo = Label(mainScreen, image= img)
    logo.pack(side = 'bottom', fill = 'both', expand = 'No')


    mainScreen.mainloop()

mainScreenRun()
