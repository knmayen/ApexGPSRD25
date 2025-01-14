import tkinter 
from tkinter import *
import tkinter as tk
from pusherClass import *
import pickle
from commonFunctions import *
import config

pusherNames = []
global lastPusher
lastPusher = None



# loadData()
# print(allPushers)
def addPusher():
    global allGender
    global womens
    global mens
    # take inputs and create pusher object
    name = nameInput.get()

    if name in config.allPushers:
        clearPusherInputs()
        lb3.config(text = 'Name Already Taken')
    elif name != '':
        lb3.config(text = '')
        print(allGender.get(), womens.get(), mens.get())
        config.allPushers[name] = Pusher(name, allGender.get(), womens.get(), mens.get())
        clearPusherInputs()
        updatePusherListbox()
        storeData()
        print(config.allPushers)

# clear all input values
def clearPusherInputs():
    nameInput.delete(0, tkinter.END)
    allGender.set(0)
    womens.set(0)
    mens.set(0)

def updatePusherListbox():
    pusherNames = [str(name) for name in config.allPushers] # Update your list here
    pusherNames.sort()
    nameBox.delete(0, tkinter.END)  # Clear the existing items
    for item in pusherNames:
        nameBox.insert(tkinter.END, item)

def setPusherCheckboxes():
    # get name
    name = nameBox.get(nameBox.curselection()[0])
    # set edit checkboxes
    if config.allPushers[name].ag:
        agEditButton.select() 
    else:
        agEditButton.deselect()

    if config.allPushers[name].w:
        wEditButton.select()
    else:
        wEditButton.deselect()

    if config.allPushers[name].m:
        mEditButton.select()
    else:
        mEditButton.deselect()

def savePusherEdits():
    name = nameBox.get(nameBox.curselection()[0])

    # take inputs and edit the current pusher object -> don't want to overwrite splits data
    config.allPushers[name].ag = allGenderEditing.get()


    config.allPushers[name].w = womensEditing.get()


    config.allPushers[name].m = mensEditing.get()

    nameBox.selection_clear(0, tk.END)
    clearEdits()
    storeData()
    print(config.allPushers)

def delPusher():
    name = nameBox.get(nameBox.curselection()[0])
    del config.allPushers[name]
    updatePusherListbox()
    storeData()
    clearEdits()

def pusherInfoDisplay():
    global lastPusher
    selectedPusher = nameBox.curselection()

    if selectedPusher != ():
        name = nameBox.get(selectedPusher[0])
        editLabel.config(text = f'Edit Pusher: {name}')
        if lastPusher != name: # if the selection is new, update the checkbox values
            setPusherCheckboxes()
        lastPusher = name

        global editX
        global inputY
        agEditButton.place(x = editX, y = inputY[1], anchor = 'center')
        wEditButton.place(x = editX, y = inputY[2], anchor = 'center')
        mEditButton.place(x = editX, y = inputY[3], anchor = 'center')
        saveEditsButton.place(x = editX, y = inputY[4], anchor = 'center')
        delPusherButton.place(x = editX, y = inputY[5], anchor= 'center')

        print(config.allPushers[name].avgTimes)

    else:
        clearEdits()
    
    pusherInputScreen.after(1000, pusherInfoDisplay)

def clearEdits():
    editLabel.config(text = '')
    agEditButton.place_forget()
    wEditButton.place_forget()
    mEditButton.place_forget()
    saveEditsButton.place_forget()
    delPusherButton.place_forget()

def pusherInputScreenRun():
    global pusherInputScreen
    pusherInputScreen = tkinter.Tk()
    width = 800
    height = 600
    pusherInputScreen.geometry(f"{width}x{height}")
    pusherInputScreen.title('Pusher Input')

    # pusher name input math
    global inputY
    inputX = width // 4
    inputY = []
    widgets = 8
    delta = 40
    totalHeight = widgets * delta
    topY = (height - totalHeight) / 2
    for i in range(widgets):
        inputY.append(topY + delta * i)

    lb1 = Label(pusherInputScreen, text = "Pusher Name:")
    lb1.place(x= inputX, y = inputY[0], anchor= 'center')
    global nameInput
    nameInput = Entry(pusherInputScreen)
    nameInput.place(x = inputX, y = inputY[1], anchor= 'center')

    # division checkbuttons
    lb2 = Label(pusherInputScreen, text = 'Pusher Division:')
    lb2.place(x = inputX, y = inputY[2], anchor= 'center')
    
    global allGender
    allGender = IntVar(pusherInputScreen)
    global womens
    womens = IntVar(pusherInputScreen)
    global mens
    mens = IntVar(pusherInputScreen)

    global agButton
    agButton = Checkbutton(pusherInputScreen, text = "All Gender", variable = allGender, 
                           onvalue = 1, offvalue = 0, height = 4, width = 10)
    global wButton
    wButton = Checkbutton(pusherInputScreen, text = "Womens", variable = womens, onvalue = 1, offvalue = 0, height = 4, width = 10)
    global mButton
    mButton = Checkbutton(pusherInputScreen, text = "Mens", variable = mens, onvalue = 1, offvalue = 0, height = 4, width = 10)
    agButton.place(x = inputX, y = inputY[3], anchor= 'center')
    wButton.place(x = inputX, y = inputY[4], anchor= 'center')
    mButton.place(x = inputX, y = inputY[5], anchor= 'center')

    # add pusher button
    pusherAdd = Button(pusherInputScreen, text = 'Done', command = addPusher)
    pusherAdd.place(x = inputX, y = inputY[6], anchor= 'center')

    # lb3 is the error messages
    global lb3
    lb3 = Label(pusherInputScreen, text = '', fg = 'red')
    lb3.place(x = inputX, y = inputY[7], anchor= 'center')

    pusherX = width // 2
    lb4 = Label(pusherInputScreen, text = 'Current Pushers:')
    lb4.place(x = pusherX, y = inputY[0], anchor= 'center')

    stringNames = tkinter.StringVar(value = pusherNames)
    global nameBox
    nameBox = Listbox(pusherInputScreen, listvariable = stringNames, width = 30, height = 20) #width and height are measured in characters and lines
    updatePusherListbox()
    nameBox.place(x = pusherX, y = inputY[0] + delta // 2, anchor= 'n')

    # scroll bars are hard
    scrollBar = Scrollbar(pusherInputScreen) 
    scrollBar.place(x=pusherX + 5 * 15 , y = inputY[0] + delta // 2 + 2, height = 16 * 20 ) 
    scrollBar.config(command = nameBox.yview) 


    global editLabel
    global editX
    editX = width // 4 * 3
    editLabel = Label(pusherInputScreen, text = '')
    editLabel.place(x = editX, y = inputY[0], anchor= 'center')

    global allGenderEditing
    allGenderEditing = IntVar(pusherInputScreen)
    global womensEditing
    womensEditing = IntVar(pusherInputScreen)
    global mensEditing
    mensEditing = IntVar(pusherInputScreen)
    global agEditButton
    agEditButton = Checkbutton(pusherInputScreen, text = "All Gender", variable = allGenderEditing, onvalue = 1, offvalue = 0, height = 4, width = 10)
    global wEditButton
    wEditButton = Checkbutton(pusherInputScreen, text = "Womens", variable = womensEditing, onvalue = 1, offvalue = 0, height = 4, width = 10)
    global mEditButton
    mEditButton = Checkbutton(pusherInputScreen, text = "Mens", variable = mensEditing, onvalue = 1, offvalue = 0, height = 4, width = 10)

    global saveEditsButton
    saveEditsButton = Button(pusherInputScreen, text = 'Save Edits', command=savePusherEdits)

    global delPusherButton
    delPusherButton = Button(pusherInputScreen, text = 'Delete Pusher', command= delPusher)

    pusherInfoDisplay()

    backButton = Button(pusherInputScreen, text = 'Back', command = lambda: back(pusherInputScreen))
    backButton.place(x = width - 50, y = height - 50, anchor = "center")


    pusherInputScreen.mainloop()

# pusherInputScreenRun()