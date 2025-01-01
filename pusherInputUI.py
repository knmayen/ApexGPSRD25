# from rollClass import *
import tkinter 
from tkinter import *
import tkinter as tk
from pusherClass import *
import pickle

allPushers = dict()
pusherNames = []

pusherFile = open(r"C:\Users\knmay\OneDrive\Documents\GitHub\ApexGPSRD25\pusherPickle", 'rb')
allPushers = pickle.load(pusherFile)
pusherFile.close()
print(allPushers)

def addPusher():
    # take inputs and create pusher object
    name = nameInput.get()

    if name in allPushers:
        clearInputs()
        lb3.config(text = 'Name Already Taken')
    else:
        lb3.config(text = '')
        allPushers[name] = Pusher(name, allGender.get(), womens.get(), mens.get())
        clearInputs()
        updateListbox()
        storeData()
        
    # print(allPushers)

    # clear all input values
def clearInputs():
    nameInput.delete(0, tkinter.END)
    allGender.set(False)
    womens.set(False)
    mens.set(False)

def updateListbox():
    pusherNames = [str(name) for name in allPushers] # Update your list here
    pusherNames.sort()
    nameBox.delete(0, tkinter.END)  # Clear the existing items
    for item in pusherNames:
        nameBox.insert(tkinter.END, item)

def storeData():
    file = open(r"C:\Users\knmay\OneDrive\Documents\GitHub\ApexGPSRD25\pusherPickle", 'wb')
    pickle.dump(allPushers, file)
    file.close()

def editPusher():
    print('editing')
    


def pusherInfoDisplay():
    selectedPusher = nameBox.curselection()
    # print(selectedPusher)
    allGenderEditing = IntVar()
    womensEditing = IntVar()
    mensEditing = IntVar()
    # allGenderEditing.set(1)
    agEditButton = Checkbutton(pusherInputScreen, text = "All Gender", variable = allGenderEditing, onvalue = 1, offvalue = 0, height = 4, width = 10)
    wEditButton = Checkbutton(pusherInputScreen, text = "Womens", variable = womensEditing, onvalue = 1, offvalue = 0, height = 4, width = 10)
    mEditButton = Checkbutton(pusherInputScreen, text = "Mens", variable = mensEditing, onvalue = 1, offvalue = 0, height = 4, width = 10)

    
    # agEditButton.select()
    

    if selectedPusher != ():
        # print('selected', selectedPusher, pusherNames)
        name = nameBox.get(selectedPusher[0])
        print(allPushers[name].w)

        # womensEditing.set(allPushers[name].w)
        # mensEditing.set(allPushers[name].m)

        editLabel.config(text = f'Edit Pusher: {name}')

        # if allPushers[name].ag:
        #     allGenderEditing = TRUE
        # else:
        #     allGenderEditing = FALSE

        # if allPushers[name].w:
        #     womensEditing = TRUE
        # else:
        #     womensEditing = FALSE

        # if allPushers[name].m:
        #     mensEditing = TRUE
        # else:
        #     mensEditing = FALSE

        print(allGenderEditing)
        print(womensEditing)
        print(mensEditing)
        print(' ')
   
    else:
        editLabel.config(text = '')

        agEditButton.place_forget()
        wEditButton.place_forget()
        mEditButton.place_forget()
    
    pusherInputScreen.after(1000, pusherInfoDisplay)



def pusherInputScreenRun():
    global pusherInputScreen
    pusherInputScreen = tkinter.Tk()
    pusherInputScreen.geometry(f"{800}x{600}")
    pusherInputScreen.title('map')

    pusherInputFrame = Frame(pusherInputScreen)
    pusherInputFrame.pack()

    inputFrame = Frame(pusherInputFrame)
    inputFrame.pack(side = LEFT)
    # pusher name input
    lb1 = Label(inputFrame, text = "Pusher Name:")
    lb1.pack(side = TOP)
    global nameInput
    nameInput = Entry(inputFrame)
    nameInput.pack(side = TOP)

    # division checkbuttons
    lb2 = Label(inputFrame, text = 'Pusher Division:')
    lb2.pack(side = TOP)
    global allGender
    allGender = IntVar()
    global womens
    womens = IntVar()
    global mens
    mens = IntVar()
    global agButton
    agButton = Checkbutton(inputFrame, text = "All Gender", variable = allGender, onvalue = 1, offvalue = 0, height = 4, width = 10)
    global wButton
    wButton = Checkbutton(inputFrame, text = "Womens", variable = womens, onvalue = 1, offvalue = 0, height = 4, width = 10)
    global mButton
    mButton = Checkbutton(inputFrame, text = "Mens", variable = mens, onvalue = 1, offvalue = 0, height = 4, width = 10)
    agButton.pack(side = TOP)
    wButton.pack(side = TOP)
    mButton.pack(side = TOP)

    # add pusher button
    pusherAdd = Button(inputFrame, text = 'Done', command = addPusher)
    pusherAdd.pack(side = TOP)

    # lb3 is the error messages
    global lb3
    lb3 = Label(inputFrame, text = '', fg = 'red')
    lb3.pack(side = TOP)

    currentPusherFrame = Frame(pusherInputFrame)
    currentPusherFrame.pack(side = LEFT)
    lb4 = Label(currentPusherFrame, text = 'Current Pushers:')
    lb4.pack(side = TOP)


    stringNames = tkinter.StringVar(value = pusherNames)
    global nameBox
    nameBox = Listbox(currentPusherFrame, listvariable = stringNames, width = 30, height = 20) #width and height are measured in characters and lines
    updateListbox()
    nameBox.pack(side = TOP)

    # # scroll bars are hard
    # scrollBar = Scrollbar(pusherInputScreen) 
    # scrollBar.place(relx = x + .4, rely = .233, height = 16 * 20) 
    # scrollBar.config(command = nameBox.yview) 
    # # nameBox.bind("<<ListboxSelect>>", editPusher())

    editFrame = Frame(pusherInputFrame)
    editFrame.pack(side = LEFT)
    global editLabel
    editLabel = Label(editFrame, text = '')
    editLabel.pack(side = TOP)

    # allGenderEditing = IntVar()
    # womensEditing = IntVar()
    # mensEditing = IntVar()
    # agEditButton = Checkbutton(pusherInputScreen, text = "All Gender", variable = allGenderEditing, onvalue = 1, offvalue = 0, height = 4, width = 10)
    # wEditButton = Checkbutton(pusherInputScreen, text = "Womens", variable = womensEditing, onvalue = 1, offvalue = 0, height = 4, width = 10)
    # mEditButton = Checkbutton(pusherInputScreen, text = "Mens", variable = mensEditing, onvalue = 1, offvalue = 0, height = 4, width = 10)
    # agEditButton.place(relx= x - .08 + .5, rely = .5, anchor=W)
    # wEditButton.place(relx= x - .08 + .5, rely = .6, anchor=W)
    # mEditButton.place(relx= x - .08 + .5, rely = .7, anchor=W)


    # pusherInfoDisplay()

    # print(nameBox.curselection)


    pusherInputScreen.mainloop()

pusherInputScreenRun()