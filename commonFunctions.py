from tkinter import *
import pickle
from pusherClass import *
from rollClass import *
import config

def back(screen):
    screen.destroy()

def storeData():
    file = open(r"C:\Users\knmay\OneDrive\Documents\GitHub\ApexGPSRD25\pusherPickle", 'wb')
    pickle.dump(config.allPushers, file)
    # pickle.dump(dict(), file)
    file.close()

    file = open(r"C:\Users\knmay\OneDrive\Documents\GitHub\ApexGPSRD25\rollPickle", 'wb')
    pickle.dump(config.allRolls, file)
    # pickle.dump(dict(), file)
    file.close()

def loadData():
    rollFile = open(r"C:\Users\knmay\OneDrive\Documents\GitHub\ApexGPSRD25\rollPickle", 'rb')
    config.allRolls = pickle.load(rollFile)
    rollFile.close()

    pusherFile = open(r"C:\Users\knmay\OneDrive\Documents\GitHub\ApexGPSRD25\pusherPickle", 'rb')
    config.allPushers = pickle.load(pusherFile)
    pusherFile.close()