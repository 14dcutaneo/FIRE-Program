from tkinter import *
import tkinter
# import tkinter.ttk as ttk
# import tkinter as tk
# from threading import Thread
# import time
# from tkinter.font import Font
# #from PIL import Image, ImageTk
# from math import sqrt
from tkinter import StringVar

root = tkinter.Tk()


#Update Function
def update():
    tkinter.Label(root, text="✔", borderwidth=1, justify=CENTER).grid(row=2, column=1)

#Title
tkinter.Label(root, text="Requirements List:", borderwidth=1, justify=RIGHT, font=('Times', '18', 'bold')).grid(row=0, column=0)
tkinter.Label(root, text="✔", borderwidth=1, justify=CENTER, font=('Times', '18', 'bold') ).grid(row=0,column=1)

#Receiving Room Req
tkinter.Label(root, text="Receiving Room:    ", borderwidth=1, justify=LEFT,font =('Times', '18') ).grid(row=2,column=0)
tkinter.Label(root, text="                       ", borderwidth=1, justify=CENTER ).grid(row=2,column=1)

tkinter.Label(root, text= "Along Grid Border", borderwidth=1, justify=CENTER ).grid(row=3,column=0)
tkinter.Label(root, text="                       ", borderwidth=1, justify=CENTER ).grid(row=3,column=1)

tkinter.Label(root, text="At Least 300 Square Feet", borderwidth=1, justify=CENTER ).grid(row=4,column=0)
tkinter.Label(root, text="                       ", borderwidth=1, justify=CENTER ).grid(row=4,column=1)

#Module Assembly
tkinter.Label(root, text="Module Assembly:  ", borderwidth=1, justify=LEFT,font =('Times', '18') ).grid(row=5,column=0)
tkinter.Label(root, text="                       ", borderwidth=1, justify=CENTER ).grid(row=5,column=1)

tkinter.Label(root, text= "At Least 500 Square Feet", borderwidth=1, justify=CENTER ).grid(row=6,column=0)
tkinter.Label(root, text="                       ", borderwidth=1, justify=CENTER ).grid(row=6,column=1)

tkinter.Label(root, text="Contains 5 Modules", borderwidth=1, justify=CENTER ).grid(row=7,column=0)
tkinter.Label(root, text="                       ", borderwidth=1, justify=CENTER ).grid(row=7,column=1)

#Machine Assembly

tkinter.Label(root, text="Machine Assembly:", borderwidth=1, justify=LEFT,font =('Times', '18') ).grid(row=8,column=0)
tkinter.Label(root, text="                       ", borderwidth=1, justify=CENTER ).grid(row=8,column=1)

tkinter.Label(root, text= "At least 500 Square Feet", borderwidth=1, justify=CENTER ).grid(row=9,column=0)
tkinter.Label(root, text="                       ", borderwidth=1, justify=CENTER ).grid(row=9,column=1)

tkinter.Label(root, text="Contains 5 Modules", borderwidth=1, justify=CENTER ).grid(row=10,column=0)
tkinter.Label(root, text="                       ", borderwidth=1, justify=CENTER ).grid(row=10,column=1)

#Paint Shop
tkinter.Label(root, text="Paint Shop:             ", borderwidth=1, justify=LEFT,font =('Times', '18') ).grid(row=11,column=0)
tkinter.Label(root, text="                       ", borderwidth=1, justify=CENTER ).grid(row=11,column=1)

tkinter.Label(root, text="At Least 400 Square Feet", borderwidth=1, justify=CENTER ).grid(row=12,column=0)
tkinter.Label(root, text="                       ", borderwidth=1, justify=CENTER ).grid(row=12,column=1)

#Frame Fabrication
tkinter.Label(root, text="Frame Fabrication: ", borderwidth=1, justify=LEFT,font =('Times', '18') ).grid(row=13,column=0)
tkinter.Label(root, text="                       ", borderwidth=1, justify=CENTER ).grid(row=13,column=1)

tkinter.Label(root, text= "At Least 500 Square Feet", borderwidth=1, justify=CENTER ).grid(row=14,column=0)
tkinter.Label(root, text="                       ", borderwidth=1, justify=CENTER ).grid(row=14,column=1)

tkinter.Label(root, text="Contains 5 Frame Modules", borderwidth=1, justify=CENTER ).grid(row=15,column=0)
tkinter.Label(root, text="                       ", borderwidth=1, justify=CENTER ).grid(row=15,column=1)

#Quality Control
tkinter.Label(root, text="Quality Control:      ", borderwidth=1, justify=LEFT,font =('Times', '18') ).grid(row=16,column=0)
tkinter.Label(root, text="                       ", borderwidth=1, justify=CENTER ).grid(row=16,column=1)

tkinter.Label(root, text="At Least 400 Square Feet", borderwidth=1, justify=CENTER ).grid(row=17,column=0)
tkinter.Label(root, text="                       ", borderwidth=1, justify=CENTER ).grid(row=17,column=1)

#Packaging
tkinter.Label(root, text="Receiving Room:    ", borderwidth=1, justify=LEFT,font =('Times', '18') ).grid(row=18,column=0)
tkinter.Label(root, text="                       ", borderwidth=1, justify=CENTER ).grid(row=18,column=1)

tkinter.Label(root, text="At Least 400 Square Feet", borderwidth=1, justify=CENTER ).grid(row=19,column=0)
tkinter.Label(root, text="                       ", borderwidth=1, justify=CENTER ).grid(row=19,column=1)

#Storage
tkinter.Label(root, text="Storage:                   ", borderwidth=1, justify=LEFT,font =('Times', '18') ).grid(row=20,column=0)
tkinter.Label(root, text="                       ", borderwidth=1, justify=CENTER ).grid(row=20,column=1)

tkinter.Label(root, text="At Least 300 Square Feet", borderwidth=1, justify=CENTER ).grid(row=21,column=0)
tkinter.Label(root, text="                       ", borderwidth=1, justify=CENTER ).grid(row=21,column=1)

#Loading Dock
tkinter.Label(root, text="Loading Dock:        ", borderwidth=1, justify=LEFT,font =('Times', '18') ).grid(row=22,column=0)
tkinter.Label(root, text="                       ", borderwidth=1, justify=CENTER ).grid(row=22,column=1)

tkinter.Label(root, text="At Least 300 Square Feet", borderwidth=1, justify=CENTER ).grid(row=23,column=0)
tkinter.Label(root, text="                       ", borderwidth=1, justify=CENTER ).grid(row=23,column=1)

#Spacer
tkinter.Label(root, text="                       ", borderwidth=1, justify=CENTER ).grid(row=24,column=1)

#Update Button
MyButton = Button(root, text='Update Checklist', command=update)
MyButton.grid(row=25, column=0)


root.mainloop()
# Requirement List:
# Need the 9 different rooms
# Receiving Room (Must be on Grid Border)
# Min: 300 square feet
# Module Assembly
# Min: 500 square feet
# 5 Modules
# Machine Assembly
# Min: 500 square feet
# 5 Modules
# Paint Shop (Cannot Move)
# Min: 400 square feet
# Frame Fabrication
# Min: 500 square feet
# 5 Frame Fabrication Modules
# Quality Control
# Min: 400 square feet
# Packaging
# Min: 400 square feet
# Storage
# Min: 300 square feet
# Loading Dock (Cannot Move)
# Min: 300 square feet
