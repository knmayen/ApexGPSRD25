import pandas
import pickle
import tkinter
from tkinter import *
import tkintermapview
import PIL
from PIL import *



# file = pandas.read_csv(r"C:\Users\knmay\OneDrive\Documents\GitHub\ApexGPSRD25\neighborhoodLap.csv")
# print(file)

screen = tkinter.Tk()
screen.geometry(f"{800}x{600}")
screen.title('map')

mapWidget = tkintermapview.TkinterMapView(screen, width = 800, height = 600)
mapWidget.place(relx = .5, rely = .5, anchor = tkinter.CENTER)

mapWidget.set_position(40.440224, -79.945156)  
mapWidget.set_zoom(17)

# l = Label(screen, text = 'Hello!')
# l.pack()
# b = Button(screen, text = 'Click', width = 15)
# b.pack()
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