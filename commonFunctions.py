from tkinter import *
import pickle
from pusherClass import *
from rollClass import *

def back(screen):
    screen.destroy()

def storeData():
    file = open(r"C:\Users\knmay\OneDrive\Documents\GitHub\ApexGPSRD25\pusherPickle", 'wb')
    pickle.dump(allPushers, file)
    # pickle.dump(dict(), file)
    file.close()

    file = open(r"C:\Users\knmay\OneDrive\Documents\GitHub\ApexGPSRD25\rollPickle", 'wb')
    pickle.dump(allRolls, file)
    # pickle.dump(dict(), file)
    file.close()

def loadData():
    rollFile = open(r"C:\Users\knmay\OneDrive\Documents\GitHub\ApexGPSRD25\rollPickle", 'rb')
    allRolls = pickle.load(rollFile)
    rollFile.close()

    pusherFile = open(r"C:\Users\knmay\OneDrive\Documents\GitHub\ApexGPSRD25\pusherPickle", 'rb')
    allPushers = pickle.load(pusherFile)
    pusherFile.close()