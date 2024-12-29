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
   
        agEditButton.place(relx= x - .08 + .5, rely = .5, anchor=W)
        wEditButton.place(relx= x - .08 + .5, rely = .6, anchor=W)
        mEditButton.place(relx= x - .08 + .5, rely = .7, anchor=W)
    else:
        editLabel.config(text = '')

        agEditButton.place_forget()
        wEditButton.place_forget()
        mEditButton.place_forget()
    
    pusherInputScreen.after(1000, pusherInfoDisplay)


x = .25

pusherInputScreen = tkinter.Tk()
pusherInputScreen.geometry(f"{800}x{600}")
pusherInputScreen.title('map')

# pusher name input
lb1 = Label(pusherInputScreen, text = "Pusher Name:")
lb1.place(relx= x, rely = .25, anchor = CENTER)
nameInput = Entry(pusherInputScreen)
nameInput.place(relx= x, rely = .3, anchor = CENTER)

# division checkbuttons
lb2 = Label(pusherInputScreen, text = 'Pusher Division:')
lb2.place(relx= x, rely = .4, anchor=CENTER)
allGender = IntVar()
womens = IntVar()
mens = IntVar()
agButton = Checkbutton(pusherInputScreen, text = "All Gender", variable = allGender, onvalue = 1, offvalue = 0, height = 4, width = 10)
wButton = Checkbutton(pusherInputScreen, text = "Womens", variable = womens, onvalue = 1, offvalue = 0, height = 4, width = 10)
mButton = Checkbutton(pusherInputScreen, text = "Mens", variable = mens, onvalue = 1, offvalue = 0, height = 4, width = 10)
agButton.place(relx= x - .08, rely = .5, anchor=W)
wButton.place(relx= x - .08, rely = .6, anchor=W)
mButton.place(relx= x - .08, rely = .7, anchor=W)

# add pusher button
pusherAdd = Button(pusherInputScreen, text = 'Done', command = addPusher)
pusherAdd.place(relx = x, rely = .8, anchor = CENTER)

# lb3 is the error messages
lb3 = Label(pusherInputScreen, text = '', fg = 'red')
lb3.place(relx= x, rely = .9, anchor=CENTER)

lb4 = Label(pusherInputScreen, text = 'Current Pushers:')
lb4.place(relx = x + .3, rely = .2, anchor = CENTER)


stringNames = tkinter.StringVar(value = pusherNames)
nameBox = Listbox(pusherInputScreen, listvariable = stringNames, width = 30, height = 20) #width and height are measured in characters and lines
updateListbox()
nameBox.place(relx = x + .3, rely = .5, anchor = CENTER)

# scroll bars are hard
scrollBar = Scrollbar(pusherInputScreen) 
scrollBar.place(relx = x + .4, rely = .233, height = 16 * 20) 
scrollBar.config(command = nameBox.yview) 
# nameBox.bind("<<ListboxSelect>>", editPusher())

editLabel = Label(pusherInputScreen, text = '')
editLabel.place(relx= x + .6, rely = .2, anchor=CENTER)

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