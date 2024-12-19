import pandas
import pickle
import tkinter
from tkinter import *


file = pandas.read_csv(r"C:\Users\knmay\OneDrive\Documents\GitHub\ApexGPSRD25\neighborhoodLap.csv")
print(file)

screen = tkinter.Tk()
# l = Label(screen, text = 'Hello!')
# l.pack()
b = Button(screen, text = 'Click', width = 15)
b.pack()
screen.mainloop()

# file = open(r"C:\Users\knmay\OneDrive\Documents\GitHub\ApexGPSRD25\data.txt", 'r')

# lines = file.readlines()

# for line in lines:
#     print(line)

# var = 'hello'
# pickle.dump(var, file)


# file.close()
# print('here')

# nfile = open(r"C:\Users\knmay\OneDrive\Documents\GitHub\ApexGPSRD25\data.txt", 'rb')
# db = pickle.load(nfile)
# for line in nfile.readlines():
#     print(lines)

# nfile.close()