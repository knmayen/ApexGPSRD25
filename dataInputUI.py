# from rollClass import *
import tkinter
from tkinter import *
import pusherClass
from pusherClass import *

allPushers = dict()

def addPusher():
    print('add pusher')
    print(nameInput.get())
    print(allGender.get())
    print(womens.get())
    print(mens.get())


    pusher = Pusher(nameInput.get(), allGender.get(), womens.get(), mens.get())
    print(pusher)
    # name = nameInput.get()
    # value = Pusher(allGender.get(), womens.get(), mens.get())
    # exec(f"{name} = {value}")
    # print(name)
    # allPushers[nameInput.get()] = [Pusher(allGender.get(), womens.get(), mens.get())]
    # print(nameInput.get())

dataInputScreen = tkinter.Tk()
dataInputScreen.geometry(f"{800}x{600}")
dataInputScreen.title('map')

lb1 = Label(dataInputScreen, text = "Pusher Name:")
lb1.place(relx= .66, rely = .25, anchor = CENTER)
nameInput = Entry(dataInputScreen)
nameInput.place(relx= .66, rely = .3, anchor = CENTER)

lb2 = Label(dataInputScreen, text = 'Pusher Division:')
lb2.place(relx= .66, rely = .4, anchor=CENTER)
allGender = IntVar()
womens = IntVar()
mens = IntVar()
agButton = Checkbutton(dataInputScreen, text = "All Gender", variable = allGender, onvalue = 1, offvalue = 0, height = 4, width = 10)
wButton = Checkbutton(dataInputScreen, text = "Womens", variable = womens, onvalue = 1, offvalue = 0, height = 4, width = 10)
mButton = Checkbutton(dataInputScreen, text = "Mens", variable = mens, onvalue = 1, offvalue = 0, height = 4, width = 10)
agButton.place(relx= .6, rely = .5, anchor=W)
wButton.place(relx= .6, rely = .6, anchor=W)
mButton.place(relx= .6, rely = .7, anchor=W)


pusherAdd = Button(dataInputScreen, text = 'Done', command = addPusher)
pusherAdd.place(relx = .6, rely = .8, anchor = CENTER)


dataInputScreen.mainloop()