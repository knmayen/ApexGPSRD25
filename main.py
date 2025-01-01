from mappingUI import mapScreenRun
from rollInputUI import rollInputScreenRun
from pusherInputUI import pusherInputScreenRun
import tkinter
from tkinter import *

def mainScreenRun():
    global mainScreen
    mainScreen = tkinter.Tk()
    mainScreen.geometry(f"{800}x{600}")

    mainScreen.title('Main Screen')
    global title
    title = Label(mainScreen, text = 'ApexGPS Project for RD25')
    title.pack()

    global addRoll
    addRoll = Button(mainScreen, text = 'Add Roll', command= rollInputScreenRun)
    addRoll.pack()
    global addPusher
    addPusher = Button(mainScreen, text = 'Add Pusher', command= pusherInputScreenRun)
    addPusher.pack()
    global mapRolls
    mapRolls = Button(mainScreen, text = 'Map Rolls', command= mapScreenRun)
    mapRolls.pack()
    # global seePusherTimes




    mainScreen.mainloop()

mainScreenRun()
