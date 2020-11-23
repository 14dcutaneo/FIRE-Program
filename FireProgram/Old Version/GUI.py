#imports
import tkinter.ttk as ttk
import tkinter as tk
from threading import Thread
import time
from tkinter import StringVar
from tkinter.font import Font
#from PIL import Image, ImageTk
from math import sqrt
from tkinter import Tk, Frame, PhotoImage, Label
#classes
class Chord(Frame):
    '''Tkinter Frame with title argument'''

    def __init__(self, parent, title='', *args, **kw):
        Frame.__init__(self, parent, *args, **kw)
        self.title = title
class Accordion(Frame):
    def __init__(self, parent, accordion_style=None):
        Frame.__init__(self, parent)

        # if no style dict, assign default style
        if accordion_style:
            self.style = accordion_style
        else:
            self.style = accordion_style = {
                'title_bg': 'ghost white',
                'title_fg': 'black',
                'highlight': 'white smoke'
            }
            self.columnconfigure(0, weight=1)

    def append_chords(self, chords=[]):
        '''pass a [list] of Chords to the Accordion object'''

        self.update_idletasks()
        row = 0
        width = max([c.winfo_reqwidth() for c in chords])

        for c in chords:
            i = PhotoImage()  # blank image to force Label to use pixel size
            label = Label(self, text=c.title,
                        image=i,
                        compound='center',
                        width=width,
                        bg=self.style['title_bg'],
                        fg=self.style['title_fg'],
                        bd=2, relief='groove')

            label.grid(row=row, column=0)
            c.grid(row=row + 1, column=0, sticky='nsew')
            c.grid_remove()
            row += 2

            label.bind('<Button-1>', lambda e,
                                            c=c: self._click_handler(c))
            label.bind('<Enter>', lambda e,
                                        label=label, i=i: label.config(bg=self.style['highlight']))
            label.bind('<Leave>', lambda e,
                                        label=label, i=i: label.config(bg=self.style['title_bg']))

    def _click_handler(self, chord):
        if len(chord.grid_info()) == 0:
            chord.grid()
        else:
            chord.grid_remove()
#arrays to keep track of modules placed 1 = true, 0 = false
FFarr = 0
MOarr = 0
MAarr = 0

# Functions of the first zoomed in tab (3rd tab)

def updateLinesFF(): # Auto generate the lines between the 5 modules when both rectangles each line is between are placed on the canvas
    if (canvas3.coords(rectFF1)[0] != 0 and canvas3.coords(rectFF1)[1] != 0) and (canvas3.coords(rectFF2)[0] != 0 and canvas3.coords(rectFF2)[1] != 0):
        canvas3.coords(lines3[0],canvas3.coords(rectFF1)[0],canvas3.coords(rectFF1)[1],canvas3.coords(rectFF2)[0],canvas3.coords(rectFF2)[1])

    if (canvas3.coords(rectFF2)[0] != 0 and canvas3.coords(rectFF2)[1] != 0) and (canvas3.coords(rectFF3)[0] != 0 and canvas3.coords(rectFF3)[1] != 0):
        canvas3.coords(lines3[1],canvas3.coords(rectFF2)[0],canvas3.coords(rectFF2)[1],canvas3.coords(rectFF3)[0],canvas3.coords(rectFF3)[1])

    if (canvas3.coords(rectFF3)[0] != 0 and canvas3.coords(rectFF3)[1] != 0) and (canvas3.coords(rectFF4)[0] != 0 and canvas3.coords(rectFF4)[1] != 0):
        canvas3.coords(lines3[2],canvas3.coords(rectFF3)[0],canvas3.coords(rectFF3)[1],canvas3.coords(rectFF4)[0],canvas3.coords(rectFF4)[1])

    if (canvas3.coords(rectFF4)[0] != 0 and canvas3.coords(rectFF4)[1] != 0) and (canvas3.coords(rectFF5)[0] != 0 and canvas3.coords(rectFF5)[1] != 0):
        canvas3.coords(lines3[3],canvas3.coords(rectFF4)[0],canvas3.coords(rectFF4)[1],canvas3.coords(rectFF5)[0],canvas3.coords(rectFF5)[1])

def createRectFF(event): # Add/move the rectangles that represent the equipment
    global FFarr
    if int(f.get()) == 1:
        with open('activity log.txt', 'a') as the_file:
            the_file.write("Create module 1 inside"+names[0]+"\t," + en1.get() + ":" + en2.get() +"\n")
        canvas3.coords(rectFF1,event.x,event.y,event.x+50,event.y+50)
        canvas3.tag_raise(rectFF1)
        FFarr += 1
    if int(f.get()) == 2:
        with open('activity log.txt', 'a') as the_file:
            the_file.write("Create module 2 inside"+names[0]+"\t," + en1.get() + ":" + en2.get() +"\n")
        canvas3.coords(rectFF2,event.x,event.y,event.x+50,event.y+50)
        canvas3.tag_raise(rectFF2)
        FFarr += 1
    if int(f.get()) == 3:
        with open('activity log.txt', 'a') as the_file:
            the_file.write("Create module 3 inside "+names[0]+"\t," + en1.get() + ":" + en2.get() +"\n")
        canvas3.coords(rectFF3,event.x,event.y,event.x+50,event.y+50)
        canvas3.tag_raise(rectFF3)
        FFarr += 1
    if int(f.get()) == 4:
        with open('activity log.txt', 'a') as the_file:
            the_file.write("Create Module 4 inside "+names[0]+"\t," + en1.get() + ":" + en2.get() +"\n")
        canvas3.coords(rectFF4,event.x,event.y,event.x+50,event.y+50)
        canvas3.tag_raise(rectFF4)
        FFarr += 1
    if int(f.get()) == 5:
        with open('activity log.txt', 'a') as the_file:
            the_file.write("Create module 5 inside "+names[0]+"\t," + en1.get() + ":" + en2.get() +"\n")
        canvas3.coords(rectFF5,event.x,event.y,event.x+50,event.y+50)
        canvas3.tag_raise(rectFF5)
        FFarr += 1
    updateLinesFF()
    canvas3.create_line(0, 500, 0, -500, width = 1)

def addLabelFF(): # Add a label to the GUI at the coordinates specified in the entries
    with open('activity log.txt', 'a') as the_file:
        the_file.write("Add a label inside "+names[0]+"\t," + en1.get() + ":" + en2.get()+"\n")

    labelsFF.append(canvas3.create_text(entryFF1.get(),entryFF2.get(), text=entryFF3.get(), fill="blue"))

def trackPositionFF(this): # Track the position displayed in the entries via a 100 milisecond loop between these two functions
    funcFF(this)
    root3.after(100, trackPositionFF, funcFF(this))

def funcFF(this):
    if not str(entryFF1.get()):
        entryFF1.insert(0,0)

    if not str(entryFF2.get()):
        entryFF2.insert(0,0)

    canvas3.coords(rectTrackFF, entryFF1.get(), int(entryFF2.get())+7, int(entryFF1.get())+10, int(entryFF2.get())+7)
    canvas3.tag_raise(rectTrackFF)

def clearFF(): # Clear all the labels from the canvas

    for label in labelsFF:
        canvas3.delete(label)

    with open('activity log.txt', 'a') as the_file:
            the_file.write("Clear ALL lines and modules inside "+names[0]+"\t," + en1.get() + ":" + en2.get()+"\n")

# Functions on the second zoomed in tab (4th tab)

def updateLinesMO(): # Autogenerate the lines between the 5 modules when they are placed in the canvas
    if (canvas4.coords(rectMO1)[0] != 0 and canvas4.coords(rectMO1)[1] != 0) and (canvas4.coords(rectMO2)[0] != 0 and canvas4.coords(rectMO2)[1] != 0):
        canvas4.coords(lines4[0],canvas4.coords(rectMO1)[0],canvas4.coords(rectMO1)[1],canvas4.coords(rectMO2)[0],canvas4.coords(rectMO2)[1])

    if (canvas4.coords(rectMO2)[0] != 0 and canvas4.coords(rectMO2)[1] != 0) and (canvas4.coords(rectMO3)[0] != 0 and canvas4.coords(rectMO3)[1] != 0):
        canvas4.coords(lines4[1],canvas4.coords(rectMO2)[0],canvas4.coords(rectMO2)[1],canvas4.coords(rectMO3)[0],canvas4.coords(rectMO3)[1])

    if (canvas4.coords(rectMO3)[0] != 0 and canvas4.coords(rectMO3)[1] != 0) and (canvas4.coords(rectMO4)[0] != 0 and canvas4.coords(rectMO4)[1] != 0):
        canvas4.coords(lines4[2],canvas4.coords(rectMO3)[0],canvas4.coords(rectMO3)[1],canvas4.coords(rectMO4)[0],canvas4.coords(rectMO4)[1])

    if (canvas4.coords(rectMO4)[0] != 0 and canvas4.coords(rectMO4)[1] != 0) and (canvas4.coords(rectMO5)[0] != 0 and canvas4.coords(rectMO5)[1] != 0):
        canvas4.coords(lines4[3],canvas4.coords(rectMO4)[0],canvas4.coords(rectMO4)[1],canvas4.coords(rectMO5)[0],canvas4.coords(rectMO5)[1])

def createRectMO(event): # Add/move the rectangles that represent the equipment
    global MOarr
    if int(m.get()) == 1:
        with open('activity log.txt', 'a') as the_file:
            the_file.write("Create module 1 inside "+names[1]+"\t," + en1.get() + ":" + en2.get() +"\n")
        canvas4.coords(rectMO1,event.x,event.y,event.x+50,event.y+50)
        canvas4.tag_raise(rectMO1)
        MOarr += 1
    if int(m.get()) == 2:
        with open('activity log.txt', 'a') as the_file:
            the_file.write("Create module 2 inside "+names[1]+"\t," + en1.get() + ":" + en2.get() +"\n")
        canvas4.coords(rectMO2,event.x,event.y,event.x+50,event.y+50)
        canvas4.tag_raise(rectMO2)
        MOarr += 1
    if int(m.get()) == 3:
        with open('activity log.txt', 'a') as the_file:
            the_file.write("Create module 3 inside "+names[1]+"\t," + en1.get() + ":" + en2.get() +"\n")
        canvas4.coords(rectMO3,event.x,event.y,event.x+50,event.y+50)
        canvas4.tag_raise(rectMO3)
        MOarr += 1
    if int(m.get()) == 4:
        with open('activity log.txt', 'a') as the_file:
            the_file.write("Create module 4 inside "+names[1]+"\t," + en1.get() + ":" + en2.get() +"\n")
        canvas4.coords(rectMO4,event.x,event.y,event.x+50,event.y+50)
        canvas4.tag_raise(rectMO4)
        MOarr += 1
    if int(m.get()) == 5:
        with open('activity log.txt', 'a') as the_file:
            the_file.write("Create module 5 inside "+names[1]+"\t," + en1.get() + ":" + en2.get() +"\n")
        canvas4.coords(rectMO5,event.x,event.y,event.x+50,event.y+50)
        canvas4.tag_raise(rectMO5)
        MOarr += 1
    updateLinesMO()
    canvas4.create_line(0, 500, 0, -500, width = 1)

def addLabelMO(): # Add a label to the GUI at the coordinates specified in the entries
    with open('activity log.txt', 'a') as the_file:
        the_file.write("Add a Label inside "+names[1]+"\t," + en1.get() + ":" + en2.get()+"\n")

    labelsMO.append(canvas4.create_text(entryMO1.get(),entryMO2.get(), text=entryMO3.get(), fill="red"))

def trackPositionMO(this): # Track the position displayed in the entries via a 100 milisecond loop between these two functions
    funcMO(this)
    root4.after(100, trackPositionMO, funcMO(this))

def funcMO(this):
    if not str(entryMO1.get()):
        entryMO1.insert(0,0)

    if not str(entryMO2.get()):
        entryMO2.insert(0,0)

    canvas4.coords(rectTrackMO, entryMO1.get(), int(entryMO2.get())+6, int(entryMO1.get())+10, int(entryMO2.get())+6)
    canvas4.tag_raise(rectTrackMO)

def clearMO(): # Clear all the modules and lines from the canvas

    for label in labelsMO:
        canvas4.delete(label)

    with open('activity log.txt', 'a') as the_file:
            the_file.write("Clear ALL lines and modules inside, "+names[1]+"\t," + en1.get() + ":" + en2.get()+"\n")

# Functions on the third zoomed tab (5th tab)

def updateLinesMA(): # Autogenerate the lines between the 5 modules when they are placed in the canvas
    if (canvas5.coords(rectMA1)[0] != 0 and canvas5.coords(rectMA1)[1] != 0) and (canvas5.coords(rectMA2)[0] != 0 and canvas4.coords(rectMA2)[1] != 0):
        canvas5.coords(lines5[0],canvas5.coords(rectMA1)[0],canvas5.coords(rectMA1)[1],canvas5.coords(rectMA2)[0],canvas5.coords(rectMA2)[1])

    if (canvas5.coords(rectMA2)[0] != 0 and canvas5.coords(rectMA2)[1] != 0) and (canvas5.coords(rectMA3)[0] != 0 and canvas4.coords(rectMA3)[1] != 0):
        canvas5.coords(lines5[1],canvas5.coords(rectMA2)[0],canvas5.coords(rectMA2)[1],canvas5.coords(rectMA3)[0],canvas5.coords(rectMA3)[1])

    if (canvas5.coords(rectMA3)[0] != 0 and canvas5.coords(rectMA3)[1] != 0) and (canvas5.coords(rectMA4)[0] != 0 and canvas4.coords(rectMA4)[1] != 0):
        canvas5.coords(lines5[2],canvas5.coords(rectMA3)[0],canvas5.coords(rectMA3)[1],canvas5.coords(rectMA4)[0],canvas5.coords(rectMA4)[1])

    if (canvas5.coords(rectMA4)[0] != 0 and canvas5.coords(rectMA4)[1] != 0) and (canvas5.coords(rectMA5)[0] != 0 and canvas4.coords(rectMA5)[1] != 0):
        canvas5.coords(lines5[3],canvas5.coords(rectMA4)[0],canvas5.coords(rectMA4)[1],canvas5.coords(rectMA5)[0],canvas5.coords(rectMA5)[1])

def createRectMA(event): # Add/move the rectangles that represent the equipment
    global MAarr
    if int(a.get()) == 1:
        with open('activity log.txt', 'a') as the_file:
            the_file.write("Create module 1 inside "+names[2]+"\t," + en1.get() + ":" + en2.get() +"\n")
        canvas5.coords(rectMA1,event.x,event.y,event.x+100,event.y+50)
        canvas5.tag_raise(rectMA1)
        MAarr += 1
    if int(a.get()) == 2:
        with open('activity log.txt', 'a') as the_file:
            the_file.write("Create module 2 inside "+names[2]+"\t," + en1.get() + ":" + en2.get() +"\n")
        canvas5.coords(rectMA2,event.x,event.y,event.x+100,event.y+50)
        canvas5.tag_raise(rectMA2)
        MAarr += 1
    if int(a.get()) == 3:
        with open('activity log.txt', 'a') as the_file:
            the_file.write("Create module 3 inside "+names[2]+"\t," + en1.get() + ":" + en2.get() +"\n")
        canvas5.coords(rectMA3,event.x,event.y,event.x+100,event.y+50)
        canvas5.tag_raise(rectMA3)
        MAarr += 1
    if int(a.get()) == 4:
        with open('activity log.txt', 'a') as the_file:
            the_file.write("Create module 4 inside "+names[2]+"\t," + en1.get() + ":" + en2.get() +"\n")
        canvas5.coords(rectMA4,event.x,event.y,event.x+100,event.y+50)
        canvas5.tag_raise(rectMA4)
        MAarr += 1
    if int(a.get()) == 5:
        with open('activity log.txt', 'a') as the_file:
            the_file.write("Create module 5 inside "+names[2]+"\t," + en1.get() + ":" + en2.get() +"\n")
        canvas5.coords(rectMA5,event.x,event.y,event.x+100,event.y+50)
        canvas5.tag_raise(rectMA5)
        MAarr += 1
    updateLinesMA()
    canvas5.create_line(0, 500, 0, -500, width = 1)

def addLabelMA(): # Add a label to the GUI at the coordinates specified in the entries
    with open('activity log.txt', 'a') as the_file:
        the_file.write("Add a label inide "+names[2]+"\t," + en1.get() + ":" + en2.get()+"\n")

    labelsMA.append(canvas5.create_text(entryMA1.get(),entryMA2.get(), text=entryMA3.get(), fill="orange"))

def trackPositionMA(this): # Track the position displayed in the entries via a 100 milisecond loop between these two functions
    funcMA(this)
    root5.after(100, trackPositionMA, funcMA(this))

def funcMA(this):
    if not str(entryMA1.get()):
        entryMA1.insert(0,0)

    if not str(entryMA2.get()):
        entryMA2.insert(0,0)

    canvas5.coords(rectTrackMA, entryMA1.get(), int(entryMA2.get())+6, int(entryMA1.get())+10, int(entryMA2.get())+6)
    canvas5.tag_raise(rectTrackMA)

def clearMA(): # Clear all the modules and lines from the canvas

    for label in labelsMA:
        canvas5.delete(label)
    
    with open('activity log.txt', 'a') as the_file:
        the_file.write("Clear ALL lines and modules inside "+names[2]+"\t," + en1.get() + ":" + en2.get()+"\n")

# Functions on the buildings tab (2nd tab) 

def create_window():
    window = tk.Toplevel(roota)  
    #✔

    if __name__ == '__main__':
        from tkinter import Entry, Button, Text
        
        # create the Accordion
        acc = Accordion(window)
        # Total
        completed = Label(window, textvariable=totalcounter)
        completed.pack()
        # first chord, Recieving Room Req
        first_chord = Chord(acc, title='Receiving Room:', bg='white')
        #Label(first_chord, text='Along Grid Border', bg='white').pack()
        Label(first_chord, textvariable=recDepText, bg='white', width = 20).pack()

        # second chord, Module Assembly
        second_chord = Chord(acc, title='Module Assembly:', bg='white')
        Label(second_chord, textvariable=modAssemblyAreaText, bg='white').pack()
        Label(second_chord, textvariable=modAssemblyText, bg='white').pack()

        # third chord, Machine Assembly
        third_chord = Chord(acc, title='Machine Assembly:', bg='white')
        Label(third_chord, textvariable=machAssemblyAreaText, bg='white').pack()
        Label(third_chord, textvariable=machAssemblyText, bg='white').pack()

        # fourth chord, Paint Shop
        fourth_chord = Chord(acc, title='Paint Shop:', bg='white')
        Label(fourth_chord, textvariable=paintText, bg='white').pack()

        # fifth chord, Frame Fabrication
        fifth_chord = Chord(acc, title='Frame Fabrication:', bg='white')
        Label(fifth_chord, textvariable=frameFabAreaText, bg='white').pack()
        Label(fifth_chord, textvariable=frameFabText, bg='white').pack()

        # sixth chord, Quality Control
        sixth_chord = Chord(acc, title='Quality Control:', bg='white')
        Label(sixth_chord, textvariable=qualControlText, bg='white').pack()

        # seventh chord, Packaging
        seventh_chord = Chord(acc, title='Packaging:', bg='white')
        Label(seventh_chord, textvariable=packgText, bg='white').pack()

        # eighth chord, Storage
        eighth_chord = Chord(acc, title='Storage:', bg='white')
        Label(eighth_chord, textvariable=storageText, bg='white').pack()

        # ninth chord, Loading Dock
        ninth_chord = Chord(acc, title='Loading Dock:', bg='white')
        Label(ninth_chord, textvariable=loadingDepText, bg='white').pack()

        # append list of chords to Accordion instance
        acc.append_chords([first_chord, second_chord, third_chord, fourth_chord, fifth_chord, sixth_chord, seventh_chord, eighth_chord, ninth_chord])
        acc.pack(fill='both', expand=1)

        # Update Button
        update_button = Button(window, text='Update Checklist', command= update)
        update_button.pack()   
    
def clearR(): # Function that resets all the rectangles on both the buildings tab
    with open('activity log.txt', 'a') as the_file:
        the_file.write("Reset ALL rectangles in building,\t" + en1.get() + ":" + en2.get()+"\n")

    canvas.coords(rect1,0,0,0,0)
    canvas.coords(rect2,0,0,0,0)
    canvas.coords(rect3,0,0,0,0)
    canvas.coords(rect5,0,0,0,0)
    canvas.coords(rect6,0,0,0,0)
    canvas.coords(rect7,0,0,0,0)
    canvas.coords(rect8,0,0,0,0)
    canvas.coords(rect9,0,0,0,0)
    canvas.coords(rect10,0,0,0,0)
    canvas.coords(rect11,0,0,0,0)

    for l in lines:
        canvas.coords(l,0,0,0,0)

def updateLines(): # A method that draws lines specified in the Building connections.txt each time a rectangle is moved
    index = 0
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    pos1 = "1"
    pos2 = "1"
    distIndex = 0
    
    for l in lines: # Go through each line and re-place each one, use the if statements to identify the buildings each line will be connected to
        if connections[index][0] == "1" and int(entry1.get())!=0 and int(entry2.get())!=0:
            x1=int(entry1.get())
            y1=int(entry2.get())
            pos1="1"
        if connections[index][0] == "2" and int(entry5.get())!=0 and int(entry6.get())!=0:
            x1=int(entry5.get())
            y1=int(entry6.get())
            pos1="2"
        if connections[index][0] == "3" and int(entry9.get())!=0 and int(entry10.get())!=0:
            x1=int(entry9.get())
            y1=int(entry10.get())
            pos1="3"
        if connections[index][0] == "4":
            x1=240
            y1=200
            pos1="4"
        if connections[index][0] == "5" and int(entry21.get())!=0 and int(entry22.get())!=0:
            x1=int(entry21.get())
            y1=int(entry22.get())
            pos1="5"
        if connections[index][0] == "6" and int(entry25.get())!=0 and int(entry26.get())!=0:
            x1=int(entry25.get())
            y1=int(entry26.get())
            pos1="6"
        if connections[index][0] == "7" and int(entry29.get())!=0 and int(entry30.get())!=0:
            x1=int(entry29.get())
            y1=int(entry30.get())
            pos1="7"
        if connections[index][0] == "8" and int(entry33.get())!=0 and int(entry34.get())!=0:
            x1=int(entry33.get())
            y1=int(entry34.get())
            pos1="8"
        if connections[index][0] == "9":
            x1=400
            y1=400
            pos1="9"
        if connections[index][0] == "0" and int(entry41.get())!=0 and int(entry42.get())!=0:
            x1=int(entry41.get())
            y1=int(entry42.get())
            pos1="0"
        if connections[index][2] == "1" and int(entry1.get())!=0 and int(entry2.get())!=0:
            x2=int(entry1.get())
            y2=int(entry2.get())
            pos2="1"
        if connections[index][2] == "2" and int(entry5.get())!=0 and int(entry6.get())!=0:
            x2=int(entry5.get())
            y2=int(entry6.get())
            pos2="2"
        if connections[index][2] == "3" and int(entry9.get())!=0 and int(entry10.get())!=0:
            x2=int(entry9.get())
            y2=int(entry10.get())
            pos2="3"
        if connections[index][2] == "4":
            x2=240
            y2=200
            pos2="4"
        if connections[index][2] == "5" and int(entry21.get())!=0 and int(entry22.get())!=0:
            x2=int(entry21.get())
            y2=int(entry22.get())
            pos2="5"
        if connections[index][2] == "6" and int(entry25.get())!=0 and int(entry26.get())!=0:
            x2=int(entry25.get())
            y2=int(entry26.get())
            pos2="6"
        if connections[index][2] == "7" and int(entry29.get())!=0 and int(entry30.get())!=0:
            x2=int(entry29.get())
            y2=int(entry30.get())
            pos2="7"
        if connections[index][2] == "8" and int(entry33.get())!=0 and int(entry34.get())!=0:
            x2=int(entry33.get())
            y2=int(entry34.get())
            pos2="8"
        if connections[index][2] == "9":
            x2=400
            y2=400
            pos2="9"
        if connections[index][2] == "0" and int(entry41.get())!=0 and int(entry42.get())!=0:
            x2=int(entry41.get())
            y2=int(entry42.get())
            pos2="0"

        if x1!=0 and y1!=0 and x2!=0 and y2!=0: # Only move the line if both the rectangles have been placed
            canvas.coords(l,x1,y1,x2,y2)

        for n in connections: # Keep track of the current distance each line covers
            if n[0]==pos1 and n[2]==pos2:
                distIndex = connections.index(n)

        distances[distIndex] = distance(x1,y1,x2,y2)
        index+=1

def distance(x1, y1, x2, y2): # Function that calculates the distance between any two points on the canvas on any tab (used in the program by several methods)
    x = (x1-x2)**2
    y = (y1-y2)**2

    return str(int(sqrt(int(x)+int(y))/2))

# Functions to move and resize the rectangles on the second and third tabs
def addRec1(): # The first three rectangles have cooresponding rectangles on there cooresponding tabs

    if int(entry3.get()) > 100: # Limit the buildings to 100X100 pixels
        entry3.delete(0,'end')
        entry3.insert(0,100)
    if int(entry4.get()) > 100:
        entry4.delete(0,'end')
        entry4.insert(0,100)

    with open('activity log.txt', 'a') as the_file: # Calculate the distance before sending the information to the activity log
        the_file.write("Added "+names[0]+" , "+distance(int(tx[0]),int(ty[0]),int(entry1.get()),int(entry2.get()))+",\t"+en1.get()+":"+en2.get()+"\n")
    canvas.coords(rect1,entry1.get(),entry2.get(),int(entry1.get())+int(entry3.get()),int(entry2.get())+int(entry4.get()))
    
    tx[0] = entry1.get()
    ty[0] = entry2.get()
    time.sleep(0.1)
    updateLines()
    if int(entry4.get()) > 0: # update the rectangle on the zoomed in tab
        if int(entry3.get()) > 0:
            canvas3.coords(rectFF,0,0,int(entry3.get())*5, int(entry4.get())*5)

def addRec2():

    if int(entry7.get()) > 100: # Limit the buildings to 100X100 pixels
        entry7.delete(0,'end')
        entry7.insert(0,100)
    if int(entry8.get()) > 100:
        entry8.delete(0,'end')
        entry8.insert(0,100)

    with open('activity log.txt', 'a') as the_file:
        the_file.write("Added "+names[1]+" , "+distance(int(tx[1]),int(ty[1]),int(entry5.get()),int(entry6.get()))+",\t"+en1.get()+":"+en2.get()+"\n")
    canvas.coords(rect2,entry5.get(),entry6.get(),int(entry5.get())+int(entry7.get()),int(entry6.get())+int(entry8.get()))
    
    tx[1] = entry5.get()
    ty[1] = entry6.get()
    updateLines()
    if int(entry8.get()) > 0: # update the rectangle on the zoomed in tab
        if int(entry7.get()) > 0:
            canvas4.coords(rectMO, 0,0, int(entry7.get())*5, int(entry8.get())*5)

def addRec3():

    if int(entry11.get()) > 100: # Limit the buildings to 100X100 pixels
        entry11.delete(0,'end')
        entry11.insert(0,100)
    if int(entry12.get()) > 100:
        entry12.delete(0,'end')
        entry12.insert(0,100)

    with open('activity log.txt', 'a') as the_file:
        the_file.write("Added "+names[2]+" , "+distance(int(tx[2]),int(ty[2]),int(entry9.get()),int(entry10.get()))+",\t"+en1.get()+":"+en2.get()+"\n")
    canvas.coords(rect3,entry9.get(),entry10.get(),int(entry9.get())+int(entry11.get()),int(entry10.get())+int(entry12.get()))
    
    tx[2] = entry9.get()
    ty[2] = entry10.get()
    updateLines()
    if int(entry12.get()) > 0: # update the rectangle on the zoomed in tab
        if int(entry11.get()) > 0:
            canvas5.coords(rectMA, 0,0, int(entry11.get())*5, int(entry12.get())*5)

def addRec4(): # The last 6 rectangles only move cooresponding rectangles on the second tab
    if int(entry19.get()) > 100: # Limit the buildings to 100X100 pixels
        entry19.delete(0,'end')
        entry19.insert(0,100)
    if int(entry20.get()) > 100:
        entry20.delete(0,'end')
        entry20.insert(0,100)

    with open('activity log.txt', 'a') as the_file:
        the_file.write("Added "+names[3]+",\t" + en1.get() + ":" + en2.get()+"\n")
    canvas.coords(rect5,240,200,240+int(entry19.get()),200+int(entry20.get()))
    
    updateLines()

def addRec5():

    if int(entry23.get()) > 100: # Limit the buildings to 100X100 pixels
        entry23.delete(0,'end')
        entry23.insert(0,100)
    if int(entry24.get()) > 100:
        entry24.delete(0,'end')
        entry24.insert(0,100)

    with open('activity log.txt', 'a') as the_file:
        the_file.write("Added "+names[4]+" , "+distance(int(tx[5]),int(ty[5]),int(entry21.get()),int(entry22.get()))+",\t"+en1.get()+":"+en2.get()+"\n")
    canvas.coords(rect6,entry21.get(),entry22.get(),int(entry21.get())+int(entry23.get()),int(entry22.get())+int(entry24.get()))
    
    tx[5] = entry21.get()
    ty[5] = entry22.get()
    updateLines()

def addRec6():

    if int(entry27.get()) > 100: # Limit the buildings to 100X100 pixels
        entry27.delete(0,'end')
        entry27.insert(0,100)
    if int(entry28.get()) > 100:
        entry28.delete(0,'end')
        entry28.insert(0,100)

    with open('activity log.txt', 'a') as the_file:
        the_file.write("Added "+names[5]+" , "+distance(int(tx[6]),int(ty[6]),int(entry25.get()),int(entry26.get()))+",\t"+en1.get()+":"+en2.get()+"\n")
    canvas.coords(rect7,entry25.get(),entry26.get(),int(entry25.get())+int(entry27.get()),int(entry26.get())+int(entry28.get()))
    
    tx[6] = entry25.get()
    ty[6] = entry26.get()
    updateLines()

def addRec7():

    if int(entry31.get()) > 100: # Limit the buildings to 100X100 pixels
        entry31.delete(0,'end')
        entry31.insert(0,100)
    if int(entry32.get()) > 100:
        entry32.delete(0,'end')
        entry32.insert(0,100)

    with open('activity log.txt', 'a') as the_file:
        the_file.write("Added "+names[6]+" , "+distance(int(tx[7]),int(ty[7]),int(entry29.get()),int(entry30.get()))+",\t"+en1.get()+":"+en2.get()+"\n")
    canvas.coords(rect8,entry29.get(),entry30.get(),int(entry29.get())+int(entry31.get()),int(entry30.get())+int(entry32.get()))
    
    tx[7] = entry29.get()
    ty[7] = entry30.get()
    updateLines()

def addRec8():

    if int(entry35.get()) > 100: # Limit the buildings to 100X100 pixels
        entry35.delete(0,'end')
        entry35.insert(0,100)
    if int(entry36.get()) > 100:
        entry36.delete(0,'end')
        entry36.insert(0,100)

    with open('activity log.txt', 'a') as the_file:
        the_file.write("Added "+names[7]+" , "+distance(int(tx[8]),int(ty[8]),int(entry33.get()),int(entry34.get()))+",\t"+en1.get()+":"+en2.get()+"\n")
    canvas.coords(rect9,entry33.get(),entry34.get(),int(entry33.get())+int(entry35.get()),int(entry34.get())+int(entry36.get()))
    
    tx[8] = entry33.get()
    ty[8] = entry34.get()
    updateLines()

def addRec9():
    if int(entry39.get()) > 100: # Limit the buildings to 100X100 pixels
        entry39.delete(0,'end')
        entry39.insert(0,100)
    if int(entry40.get()) > 100:
        entry40.delete(0,'end')
        entry40.insert(0,100)

    with open('activity log.txt', 'a') as the_file:
        the_file.write("Added "+names[8]+",\t" + en1.get() + ":" + en2.get()+"\n")
    canvas.coords(rect10,400,400,400+int(entry39.get()),400+int(entry40.get()))
    
    updateLines()

def addRec0():
    if int(entry43.get()) > 100: # Limit the buildings to 100X100 pixels
        entry43.delete(0,'end')
        entry43.insert(0,100)
    if int(entry44.get()) > 100:
        entry44.delete(0,'end')
        entry44.insert(0,100)

    with open('activity log.txt', 'a') as the_file:
        the_file.write("Added "+names[9]+" , "+distance(int(tx[8]),int(ty[8]),int(entry41.get()),int(entry42.get()))+",\t" + en1.get() + ":" + en2.get()+"\n")
    canvas.coords(rect11,entry41.get(),entry42.get(),int(entry41.get())+int(entry43.get()),int(entry42.get())+int(entry44.get()))
    updateLines()

def dragRect(event): # Function that moves the selected rectangle on both of the second and third tabs by clicking
    if int(s.get()) == 1:
        with open('activity log.txt', 'a') as the_file:
            the_file.write("Moved "+names[0]+" , "+distance(event.x,event.y,int(entry1.get()),int(entry2.get()))+",\t"+en1.get()+":"+en2.get()+"\n")
        canvas.coords(rect1,event.x,event.y,int(entry3.get())+event.x,int(entry4.get())+event.y)
        
        entry1.delete(0,'end')
        entry2.delete(0,'end')
        entry1.insert(0,event.x)
        entry2.insert(0,event.y)
        tx[0] = entry1.get()
        ty[0] = entry2.get()
        updateLines()
    if int(s.get()) == 2:
        with open('activity log.txt', 'a') as the_file:
            the_file.write("Moved "+names[1]+" , "+distance(event.x,event.y,int(entry5.get()),int(entry6.get()))+" , "+en1.get()+":"+en2.get()+"\n")
        canvas.coords(rect2,event.x,event.y,int(entry7.get())+event.x,int(entry8.get())+event.y)
        
        entry5.delete(0,'end')
        entry6.delete(0,'end')
        entry5.insert(0,event.x)
        entry6.insert(0,event.y)
        tx[1] = entry5.get()
        ty[1] = entry6.get()
        updateLines()
    if int(s.get()) == 3:
        with open('activity log.txt', 'a') as the_file:
            the_file.write("Moved "+names[2]+ " , "+distance(event.x,event.y,int(entry9.get()),int(entry10.get()))+",\t"+en1.get()+":"+en2.get()+"\n") 
        canvas.coords(rect3,event.x,event.y,int(entry11.get())+event.x,int(entry12.get())+event.y)
        
        entry9.delete(0,'end')
        entry10.delete(0,'end')
        entry9.insert(0,event.x)
        entry10.insert(0,event.y)
        tx[2] = entry9.get()
        ty[2] = entry10.get()
        updateLines()
    if int(s.get()) == 4:
        with open('activity log.txt', 'a') as the_file:
            the_file.write("Moved "+names[3]+ ",\t"+en1.get()+":"+en2.get()+"\n")
        canvas.coords(rect5,240,200,int(entry19.get())+240,int(entry20.get())+200)
        
        entry17.delete(0,'end')
        entry18.delete(0,'end')
        entry17.insert(0,240)
        entry18.insert(0,200)
        updateLines()
    if int(s.get()) == 5:
        with open('activity log.txt', 'a') as the_file:
            the_file.write("Moved "+names[4]+" , "+distance(event.x,event.y,int(entry21.get()),int(entry22.get()))+ ",\t"+en1.get()+":"+en2.get()+"\n")
        canvas.coords(rect6,event.x,event.y,int(entry23.get())+event.x,int(entry24.get())+event.y)

        entry21.delete(0,'end')
        entry22.delete(0,'end')
        entry21.insert(0,event.x)
        entry22.insert(0,event.y)
        tx[5] = entry21.get()
        ty[5] = entry22.get()
        updateLines()
    if int(s.get()) == 6:
        with open('activity log.txt', 'a') as the_file:
            the_file.write("Moved "+names[5]+ " , "+distance(event.x,event.y,int(entry25.get()),int(entry26.get()))+ ",\t"+en1.get()+":"+en2.get()+"\n")
        canvas.coords(rect7,event.x,event.y,int(entry27.get())+event.x,int(entry28.get())+event.y)
        
        entry25.delete(0,'end')
        entry26.delete(0,'end')
        entry25.insert(0,event.x)
        entry26.insert(0,event.y)
        tx[6] = entry25.get()
        ty[6] = entry26.get()
        updateLines()
    if int(s.get()) == 7:
        with open('activity log.txt', 'a') as the_file:
            the_file.write("Moved "+names[6]+ " , "+distance(event.x,event.y,int(entry29.get()),int(entry30.get()))+ ",\t"+en1.get()+":"+en2.get()+"\n")
        canvas.coords(rect8,event.x,event.y,int(entry31.get())+event.x,int(entry32.get())+event.y)
        
        entry29.delete(0,'end')
        entry30.delete(0,'end')
        entry29.insert(0,event.x)
        entry30.insert(0,event.y)
        tx[7] = entry29.get()
        ty[7] = entry30.get()
        updateLines()
    if int(s.get()) == 8:
        with open('activity log.txt', 'a') as the_file:
            the_file.write("Moved "+names[7]+" , "+distance(event.x,event.y,int(entry33.get()),int(entry34.get()))+ ",\t"+en1.get()+":"+en2.get()+"\n")
        canvas.coords(rect9,event.x,event.y,int(entry35.get())+event.x,int(entry36.get())+event.y)
        
        entry33.delete(0,'end')
        entry34.delete(0,'end')
        entry33.insert(0,event.x)
        entry34.insert(0,event.y)
        tx[8] = entry33.get()
        ty[8] = entry34.get()
        updateLines()
    if int(s.get()) == 9:
        with open('activity log.txt', 'a') as the_file:
            the_file.write("Moved "+names[8]+ ",\t"+en1.get()+":"+en2.get()+"\n")
        canvas.coords(rect10,400,400,int(entry39.get())+400,int(entry40.get())+400)
        
        entry37.delete(0,'end')
        entry38.delete(0,'end')
        entry37.insert(0,400)
        entry38.insert(0,400)
        updateLines()
    if int(s.get()) == 10:
        with open('activity log.txt', 'a') as the_file:
            the_file.write("Moved "+names[9]+ " , "+distance(event.x,event.y,int(entry41.get()),int(entry42.get()))+ ",\t"+en1.get()+":"+en2.get()+"\n")
        canvas.coords(rect11,event.x,event.y,int(entry43.get())+event.x,int(entry44.get())+event.y)

        entry41.delete(0,'end')
        entry42.delete(0,'end')
        entry41.insert(0,event.x)
        entry42.insert(0,event.y)
        tx[10] = entry43.get()
        ty[10] = entry44.get()
        updateLines()

roota = tk.Tk() # Root for the window

roota.title("FIRE - Designing Innovations Application")

nb = ttk.Notebook(roota) # Create and label all the tabs

demo = ttk.Frame(roota) # Create and add all of the roots
root = ttk.Frame(roota)
root3 = ttk.Frame(roota)
root4 = ttk.Frame(roota)
root5 = ttk.Frame(roota)
root6 = ttk.Frame(roota)

global names # Read in all the names from the file and store them in this array
names = []

f = open('Building names.txt')
lineStr = str(f.readline())
while lineStr:
    names.append(lineStr)
    lineStr = str(f.readline())
nb.add(demo, text='Demographic Information\n') # Add all the tabs to the window
nb.add(root, text='Buildings\n')
if len(names) > 0:
    nb.add(root3, text=names[0])
if len(names) > 1:
    nb.add(root4, text=names[1])
if len(names) > 2:
    nb.add(root5, text=names[2])

nb.pack(expand=1, fill="both")

canvas  = tk.Canvas(root, width = 500, height = 500, bg = "white", bd=2, relief='groove') # Create the canvas
canvas.grid(row=0,column=0, columnspan=1, rowspan=30, padx = 50, pady = 15)

for i in range(0,26): # Vertical lines of the grid on the first tab
    x = 20*i
    canvas.create_line(x, 500, x, -500, width = 1)

for i in range(0,26): # Horizontal lines of the grid on the first tab
    y = 20*i
    canvas.create_line(0, y, 500, y, width = 1)

rect1 = canvas.create_rectangle(0, 0, 0, 0, fill="red") # all the rectangles on the first tab, rect4 and rect10 cannot be moved from their specified positions
rect2 = canvas.create_rectangle(0, 0, 0, 0, fill="sky blue")
rect3 = canvas.create_rectangle(0, 0, 0, 0, fill="green")
rect5 = canvas.create_rectangle(0, 0, 0, 0, fill="orange")
rect6 = canvas.create_rectangle(0, 0, 0, 0, fill="white")
rect7 = canvas.create_rectangle(0, 0, 0, 0, fill="lawngreen")
rect8 = canvas.create_rectangle(0, 0, 0, 0, fill="cyan")
rect9 = canvas.create_rectangle(0, 0, 0, 0, fill="royalblue")
rect10= canvas.create_rectangle(0, 0, 0, 0, fill="gold")
rect11= canvas.create_rectangle(0, 0, 0, 0, fill="grey79")

for i in range(0, len(names)): # Add new lines for each space in each name in the names array
    names[i] = names[i].replace(' ','\n')

global lines # Declare the arrays that store the lines between the recnangles and the distances
lines = []

global distances
distances = []

global connections
connections = tuple(open('Building connections.txt','r')) # Read the data from the file to determine the material roots between the buildings

for i in range(0, len(connections)):
    lines.append(canvas.create_line(0,0,0,0,arrow=tk.LAST))
    distances.append(0.0)

global tx # Declare two arrays of integers that store the coordinates of each rectangle so the distance can be calculated
tx=[0,0,0,0,0,0,0,0,0,0,0]

global ty
ty=[0,0,0,0,0,0,0,0,0,0,0]

# Create and place all the entries on the Buildings tab, where 4 entries are associated with each building.

entry1 = ttk.Entry(root)
entry2 = ttk.Entry(root)
entry3 = ttk.Entry(root)
entry4 = ttk.Entry(root)

entry1.grid(row=1, column=2)
entry2.grid(row=1, column=3)
entry3.grid(row=2, column=2, sticky = tk.N)
entry4.grid(row=2, column=3, sticky = tk.N)

entry1.insert(0,0)
entry2.insert(0,0)
entry3.insert(0,0)
entry4.insert(0,0)

lineStr = str(f.readline())


entry5 = ttk.Entry(root)
entry6 = ttk.Entry(root)
entry7 = ttk.Entry(root)
entry8 = ttk.Entry(root)

entry5.grid(row=3, column=2)
entry6.grid(row=3, column=3)
entry7.grid(row=4, column=2, sticky = tk.N)
entry8.grid(row=4, column=3, sticky = tk.N)

entry5.insert(0,0)
entry6.insert(0,0)
entry7.insert(0,0)
entry8.insert(0,0)

entry9 = ttk.Entry(root)
entry10 = ttk.Entry(root)
entry11 = ttk.Entry(root)
entry12 = ttk.Entry(root)

entry9.grid(row=5, column=2)
entry10.grid(row=5, column=3)
entry11.grid(row=6, column=2, sticky = tk.N)
entry12.grid(row=6, column=3, sticky = tk.N)

entry9.insert(0,0)
entry10.insert(0,0)
entry11.insert(0,0)
entry12.insert(0,0)

#entry13 = ttk.Entry(root)
#entry14 = ttk.Entry(root)
#entry15 = ttk.Entry(root)
#entry16 = ttk.Entry(root)

entry17 = ttk.Entry(root)
entry18 = ttk.Entry(root)
entry19 = ttk.Entry(root)
entry20 = ttk.Entry(root)

entry17.grid(row=7, column=2)
entry18.grid(row=7, column=3)
entry19.grid(row=8, column=2, sticky = tk.N)
entry20.grid(row=8, column=3, sticky = tk.N)

entry17.insert(0,200)
entry18.insert(0,240)
entry19.insert(0,0)
entry20.insert(0,0)

entry21 = ttk.Entry(root)
entry22 = ttk.Entry(root)
entry23 = ttk.Entry(root)
entry24 = ttk.Entry(root)

entry21.grid(row=1, column=7)
entry22.grid(row=1, column=8)
entry23.grid(row=2, column=7, sticky = tk.N)
entry24.grid(row=2, column=8, sticky = tk.N)

entry21.insert(0,0)
entry22.insert(0,0)
entry23.insert(0,0)
entry24.insert(0,0)

entry25 = ttk.Entry(root)
entry26 = ttk.Entry(root)
entry27 = ttk.Entry(root)
entry28 = ttk.Entry(root)

entry25.grid(row=3, column=7)
entry26.grid(row=3, column=8)
entry27.grid(row=4, column=7, sticky = tk.N)
entry28.grid(row=4, column=8, sticky = tk.N)

entry25.insert(0,0)
entry26.insert(0,0)
entry27.insert(0,0)
entry28.insert(0,0)

entry29 = ttk.Entry(root)
entry30 = ttk.Entry(root)
entry31 = ttk.Entry(root)
entry32 = ttk.Entry(root)

entry29.grid(row=5, column=7)
entry30.grid(row=5, column=8)
entry31.grid(row=6, column=7, sticky = tk.N)
entry32.grid(row=6, column=8, sticky = tk.N)

entry29.insert(0,0)
entry30.insert(0,0)
entry31.insert(0,0)
entry32.insert(0,0)

entry33 = ttk.Entry(root)
entry34 = ttk.Entry(root)
entry35 = ttk.Entry(root)
entry36 = ttk.Entry(root)

entry33.grid(row=7, column=7)
entry34.grid(row=7, column=8)
entry35.grid(row=8, column=7, sticky = tk.N)
entry36.grid(row=8, column=8, sticky = tk.N)

entry33.insert(0,0)
entry34.insert(0,0)
entry35.insert(0,0)
entry36.insert(0,0)

entry37 = ttk.Entry(root)
entry38 = ttk.Entry(root)
entry39 = ttk.Entry(root)
entry40 = ttk.Entry(root)

entry37.grid(row=9, column=7)
entry38.grid(row=9, column=8)
entry39.grid(row=10, column=7, sticky = tk.N)
entry40.grid(row=10, column=8, sticky = tk.N)

entry37.insert(0,400)
entry38.insert(0,400)
entry39.insert(0,0)
entry40.insert(0,0)

entry41 = ttk.Entry(root)
entry42 = ttk.Entry(root)
entry43 = ttk.Entry(root)
entry44 = ttk.Entry(root)

entry41.grid(row=11, column=7)
entry42.grid(row=11, column=8)
entry43.grid(row=12, column=7, sticky = tk.N)
entry44.grid(row=12, column=8, sticky = tk.N)

entry41.insert(0,0)
entry42.insert(0,0)
entry43.insert(0,0)
entry44.insert(0,0)

if len(names) > 0: # Do not place the label unless the array has a name for the cooresponding building
    labelFF = tk.Label(root, text=names[0], bg="red") # Create and place all the labels for the rectangles that represent the buildings
    labelFF.grid(row=1, column=4, columnspan=1, rowspan=2)

label1 = tk.Label(root, text="position x, y") # Add labels that describe this part of the app for the user
label2 = tk.Label(root, text="size x, y")

label1.grid(row=1, column=5)
label2.grid(row=2, column=5, sticky = tk.N)

if len(names) > 1:
    labelMO = tk.Label(root, text=names[1], bg="sky blue")
    labelMO.grid(row=3, column=4, columnspan=1, rowspan=2)

label3 = tk.Label(root, text="position x, y")
label4 = tk.Label(root, text="size x, y")

label3.grid(row=3, column=5)
label4.grid(row=4, column=5, sticky = tk.N)

if len(names) > 2:
    labelMA = tk.Label(root, text=names[2], bg="green")
    labelMA.grid(row=5, column=4, columnspan=1, rowspan=2)

label5 = tk.Label(root, text="position x, y")
label6 = tk.Label(root, text="size x, y")

label5.grid(row=5, column=5)
label6.grid(row=6, column=5, sticky = tk.N)

label7 = tk.Label(root, text="position x, y")
label8 = tk.Label(root, text="size x, y")

label7.grid(row=7, column=5)
label8.grid(row=8, column=5, sticky = tk.N)

if len(names) > 3:
    labelPA = tk.Label(root, text=names[3], bg="orange")
    labelPA.grid(row=7, column=4, columnspan=1, rowspan=2)

label9 = tk.Label(root, text="position x, y")
label10 = tk.Label(root, text="size x, y")

label9.grid(row=9, column=5)
label10.grid(row=10, column=5, sticky = tk.N)

label11 = tk.Label(root, text="position x, y")
label12 = tk.Label(root, text="size x, y")

label11.grid(row=11, column=5)
label12.grid(row=12, column=5, sticky = tk.N)

if len(names) > 4:
    labelCB = tk.Label(root, text=names[4], bg="white")
    labelCB.grid(row=1, column=9, columnspan=1, rowspan=2)

if len(names) > 5:
    labelQC = tk.Label(root, text=names[5], bg="lawngreen")
    labelQC.grid(row=3, column=9, columnspan=1, rowspan=2)

if len(names) > 6:
    labelQC = tk.Label(root, text=names[6], bg="cyan")
    labelQC.grid(row=5, column=9, columnspan=1, rowspan=2)

if len(names) > 7:
    labelS = tk.Label(root, text=names[7], bg="royalblue")
    labelS.grid(row=7, column=9, columnspan=1, rowspan=2)

if len(names) > 8:
    labelFS = tk.Label(root, text=names[8], bg="gold")
    labelFS.grid(row=9, column=9, columnspan=1, rowspan=2)

if len(names) > 9:
    labelOT = tk.Label(root, text=names[9], bg="grey79")
    labelOT.grid(row=11, column=9, columnspan=1, rowspan=2)

button1 = ttk.Button(root, text="Apply", command=addRec1) # Create the apply buttons to activate the add rec functions
button1.grid(row=1, column=1)

button2 = ttk.Button(root, text="Apply", command=addRec2)
button2.grid(row=3, column=1)

button3 = ttk.Button(root, text="Apply", command=addRec3)
button3.grid(row=5, column=1)

button5 = ttk.Button(root, text="Apply", command=addRec4)
button5.grid(row=7, column=1)

button6 = ttk.Button(root, text="Apply", command=addRec5)
button6.grid(row=1, column=6)

button7 = ttk.Button(root, text="Apply", command=addRec6)
button7.grid(row=3, column=6)

button8 = ttk.Button(root, text="Apply", command=addRec7)
button8.grid(row=5, column=6)

button9 = ttk.Button(root, text="Apply", command=addRec8)
button9.grid(row=7, column=6)

button10= ttk.Button(root, text="Apply", command=addRec9)
button10.grid(row=9, column=6)

button11= ttk.Button(root, text="Apply", command=addRec0)
button11.grid(row=11, column=6)

canvas.bind("<Button-1>", dragRect)

s = tk.Spinbox(root, width=10,from_=1, to=len(names)) # Create the spinbox and the asociated labels for the dragrect function
s.grid(row=9, column=1,rowspan=2,columnspan=1)

for i in range(0, len(names)): # Once everything involving the names is initialized within the GUI then replace all the extra lines with spaces for functions that use the activity log
    names[i] = names[i].replace('\n',' ')

# Create labels to designate each color to a number on the spinbox
labelSpin = tk.Label(root, text="Select the number cooresponding to the building\nyou want to move", bg="white")
labelSpin1 = tk.Label(root, text=" 1 ", bg="red") # Colored labels to designate which color to the cooresponding rectangle
labelSpin2 = tk.Label(root, text=" 2 ", bg="sky blue")
labelSpin3 = tk.Label(root, text=" 3 ", bg="green")
labelSpin5 = tk.Label(root, text=" 4 ", bg="orange")

labelSpin6 = tk.Label(root, text=" 5 ", bg="white")
labelSpin7 = tk.Label(root, text=" 6 ", bg="lawngreen")
labelSpin8 = tk.Label(root, text=" 7 ", bg="cyan")
labelSpin9 = tk.Label(root, text=" 8 ", bg="royalblue")
labelSpin10= tk.Label(root, text=" 9 ", bg="gold")
labelSpin11= tk.Label(root, text=" 0 ", bg="grey79")

labelSpin.grid(row=9, column=2, columnspan=5, rowspan=2, sticky=tk.W)
labelSpin1.grid(row=11, column=2, sticky = tk.W)
labelSpin2.grid(row=11, column=2)
labelSpin3.grid(row=12, column=2, sticky = tk.W)
labelSpin5.grid(row=12, column=2)

labelSpin6.grid(row=11, column=3, sticky = tk.W)
labelSpin7.grid(row=11, column=3)
labelSpin8.grid(row=11, column=3, sticky = tk.E)
labelSpin9.grid(row=12, column=3, sticky = tk.W)
labelSpin10.grid(row=12, column=3)
labelSpin11.grid(row=12, column=3, sticky = tk.E)

button5 = ttk.Button(root, text="Reset Buildings", command=clearR) # Add a button that resets all the rectangles
button5.grid(row=13, column=1, rowspan=1, columnspan=2, sticky = tk.W)

labelInstruction1 = tk.Label(root, text="Each building is controled by four of the text entries above as labeled, the top two entries for each\n\nbuilding are the x coordinates across and y coordinates down from the top left corner of the grid")
labelInstruction2 = tk.Label(root, text="and the bottom two entries are the same for the dimensions of each building from the top left corner of the building.")
labelInstruction3 = tk.Label(root, text="Place and resize buildings by typing coordinates and sizes and clicking apply, once a size is typed in ")
labelInstruction4 = tk.Label(root, text="buildings can be moved by selecting the cooresponding number in the box above and clicking a position. ")
labelInstruction5 = tk.Label(root, text="Each pixel on the first two tabs is 1/2 ft and each box on the grid is 10 ft long.", bg="red", fg="yellow")

labelInstruction1.grid(row=17, column=1, columnspan=16, rowspan=1, sticky = tk.W) # Create and place the labels that explain how to use the application
labelInstruction2.grid(row=18, column=1, columnspan=16, rowspan=1, sticky = tk.W)
labelInstruction3.grid(row=19, column=1, columnspan=16, rowspan=1, sticky = tk.W)
labelInstruction4.grid(row=20, column=1, columnspan=16, rowspan=1, sticky = tk.W)
labelInstruction5.grid(row=21, column=1, columnspan=16, rowspan=1, sticky = tk.W)

labelInstruction1.config(font=("Average", 12)) # Resize the labels to make them as apparent as possible for the user
labelInstruction2.config(font=("Average", 12))
labelInstruction3.config(font=("Average", 12))
labelInstruction4.config(font=("Average", 12))
labelInstruction5.config(font=("Average", 14))

# 3rd tab

canvas3 = tk.Canvas(root3, width = 500, height = 500, bg = "white", bd=2, relief='groove')
canvas3.grid(row=0, column=0, columnspan=1, rowspan=30, padx = 50, pady = 15)

for i in range(0,26): # Vertical lines for the grid on the 3rd tab
    x = 20*i
    canvas3.create_line(x, 500, x, -500, width = 1)

for i in range(0,26): # Horizontal lines for the grid
    y = 20*i
    canvas3.create_line(0, y, 500, y, width = 1)

rectFF = canvas3.create_rectangle(0, 0, 0, 0, fill="red") # rectangle to represent the building
rectTrackFF = canvas3.create_rectangle(0, 0, 0, 0, fill="orange") # rectangle to track where labels will be placed

rectFF1 = canvas3.create_rectangle(0, 0, 0, 0, fill="grey") # Create four rectangles to represent the fabrication modules
rectFF2 = canvas3.create_rectangle(0, 0, 0, 0, fill="grey")
rectFF3 = canvas3.create_rectangle(0, 0, 0, 0, fill="grey")
rectFF4 = canvas3.create_rectangle(0, 0, 0, 0, fill="grey")
rectFF5 = canvas3.create_rectangle(0, 0, 0, 0, fill="grey")

global lines3 # Create four lines that represent the material routes between the buildings
lines3 = [canvas3.create_line(0,0,0,0),canvas3.create_line(0,0,0,0),canvas3.create_line(0,0,0,0),canvas3.create_line(0,0,0,0)]

global labelsFF
labelsFF = []

canvas3.bind("<Button-3>", createRectFF)

buttonFF = ttk.Button(root3, text="Clear", command=clearFF)
buttonFF.grid(row=0, column=1)

labelFF = tk.Label(root3, text="Insert a label,     x                       y                                                    text                             ")
labelFF.grid(row=1, column=1, columnspan=3, rowspan=1)

entryFF1 = ttk.Entry(root3) # Entries that allow the user to label the design
entryFF2 = ttk.Entry(root3)
entryFF3 = ttk.Entry(root3)

entryFF1.grid(row=2, column=1)
entryFF2.grid(row=2, column=2)
entryFF3.grid(row=2, column=3)

entryFF1.insert(0,0)
entryFF2.insert(0,0)
entryFF3.insert(0,"text")

buttonFF = ttk.Button(root3, text="Add Label", command=addLabelFF)
buttonFF.grid(row=3, column=1)

trackPositionFF(funcFF) # Activate the function loop that will track the coordinates that the user types in the entries

labelFFspinbox = tk.Label(root3, text="There are 5 fabrication modules you can add, select the number of the one you want to add and right click on the grid to add it.")
labelFFspinbox.grid(row=4, column=1, columnspan=10, rowspan=1)

labelFFspinbox.config(font=("Average", 12))

f = tk.Spinbox(root3, from_=1, to=5) # Create the spinbox and the asociated labels for the dragrect function
f.grid(row=5, column=1)

labelFFInstruction1 = tk.Label(root3, text="Add labels by typing in coordinates and text and clicking add, the orange box will show where the    ")
labelFFInstruction2 = tk.Label(root3, text="selected coordinates are, To delete the last object placed press shift-L, click clear to clear all   ")
labelFFInstruction3 = tk.Label(root3, text="labels, rectangles, and lines. The only equipment in this building is fabricator equipment.          ")
labelFFInstruction4 = tk.Label(root3, text="Each box on the grid is 2 ft long.", bg="red", fg="yellow")

labelFFInstruction1.grid(row=6, column=1, columnspan=4, rowspan=1) # Create and place the labels that explain this tab
labelFFInstruction2.grid(row=7, column=1, columnspan=4, rowspan=1)
labelFFInstruction3.grid(row=8, column=1, columnspan=4, rowspan=1)
labelFFInstruction4.grid(row=9, column=1, columnspan=4, rowspan=1)

labelFFInstruction1.config(font=("Average", 12))
labelFFInstruction2.config(font=("Average", 12))
labelFFInstruction3.config(font=("Average", 12))
labelFFInstruction4.config(font=("Average", 12))

# 4th tab

canvas4 = tk.Canvas(root4, width = 500, height = 500, bg = "white", bd=2, relief='groove')
canvas4.grid(row=0, column=0, columnspan=1, rowspan=30, padx = 50, pady = 15)

for i in range(0,26): # Vertical lines for the grid on the 4th tab
    x = 20*i
    canvas4.create_line(x, 500, x, -500, width = 1)

for i in range(0,26): # Horizontal lines for the grid
    y = 20*i
    canvas4.create_line(0, y, 500, y, width = 1)

rectMO = canvas4.create_rectangle(0, 0, 0, 0, fill="sky blue") # rectangle to represent the building
rectTrackMO = canvas4.create_rectangle(0, 0, 0, 0, fill="orange") # rectangle to track where labels will be placed

rectMO1 = canvas4.create_rectangle(0, 0, 0, 0, fill="grey") # Create four rectangles to represent the modules
rectMO2 = canvas4.create_rectangle(0, 0, 0, 0, fill="grey")
rectMO3 = canvas4.create_rectangle(0, 0, 0, 0, fill="grey")
rectMO4 = canvas4.create_rectangle(0, 0, 0, 0, fill="grey")
rectMO5 = canvas4.create_rectangle(0, 0, 0, 0, fill="grey")

global lines4 # Create four lines that represent the material routes between the modules
lines4 = [canvas4.create_line(0,0,0,0),canvas4.create_line(0,0,0,0),canvas4.create_line(0,0,0,0),canvas4.create_line(0,0,0,0)]

global labelsMO
labelsMO = []

canvas4.bind("<Button-3>", createRectMO) 

buttonMO = ttk.Button(root4, text="Clear", command=clearMO)
buttonMO.grid(row=0, column=1)

labelMO = tk.Label(root4, text="Insert a label,     x                       y                                                    text                             ")
labelMO.grid(row=1, column=1, columnspan=3, rowspan=1)

entryMO1 = ttk.Entry(root4) # Entries that allow the user to label the design
entryMO2 = ttk.Entry(root4)
entryMO3 = ttk.Entry(root4)

entryMO1.grid(row=2, column=1)
entryMO2.grid(row=2, column=2)
entryMO3.grid(row=2, column=3)

entryMO1.insert(0,0)
entryMO2.insert(0,0)
entryMO3.insert(0,"text")

buttonMO = ttk.Button(root4, text="Add Label", command=addLabelMO)
buttonMO.grid(row=3, column=1)

trackPositionMO(funcMO) # Activate the function loop that will track the coordinates that the user types in the entries

labelMOspinbox = tk.Label(root4, text="There are 5 modules you can add, select the number of the one you want to add and right click on the grid to add it.")
labelMOspinbox.grid(row=4, column=1, columnspan=10, rowspan=1)

labelMOspinbox.config(font=("Average", 12))

m = tk.Spinbox(root4, from_=1, to=5) # Create the spinbox and the asociated labels for the dragrect function
m.grid(row=5, column=1)

labelMOInstruction1 = tk.Label(root4, text="Add labels by typing in coordinates and text and clicking add, the orange box will show where the    ")
labelMOInstruction2 = tk.Label(root4, text="selected coordinates are, To delete the last object placed press shift-L, click clear to clear all   ")
labelMOInstruction3 = tk.Label(root4, text="labels, rectangles, and lines. The equipment is module assembly equipment.                           ")
labelMOInstruction4 = tk.Label(root4, text="Each box on the grid is 2 ft long.", bg="red", fg="yellow")

labelMOInstruction1.grid(row=6, column=1, columnspan=4, rowspan=1) # Create and place the labels that explain this tab
labelMOInstruction2.grid(row=7, column=1, columnspan=4, rowspan=1)
labelMOInstruction3.grid(row=8, column=1, columnspan=4, rowspan=1)
labelMOInstruction4.grid(row=9, column=1, columnspan=4, rowspan=1)

labelMOInstruction1.config(font=("Average", 12))
labelMOInstruction2.config(font=("Average", 12))
labelMOInstruction3.config(font=("Average", 12))
labelMOInstruction4.config(font=("Average", 12))

# 5th tab

canvas5 = tk.Canvas(root5, width = 500, height = 500, bg = "white", bd=2, relief='groove')
canvas5.grid(row=0, column=0, columnspan=1, rowspan=30, padx = 50, pady = 15)

for i in range(0,26): # Vertical lines for the grid on the 5th tab
    x = 20*i
    canvas5.create_line(x, 500, x, -500, width = 1)

for i in range(0,26): # Horizontal lines for the grid
    y = 20*i
    canvas5.create_line(0, y, 500, y, width = 1)

rectMA = canvas5.create_rectangle(0, 0, 0, 0, fill="green") # rectangle to represent the building
rectTrackMA = canvas5.create_rectangle(0, 0, 0, 0, fill="orange") # rectangle to track where labels will be placed

canvas5.bind("<Button-3>", createRectMA)

rectMA1 = canvas5.create_rectangle(0, 0, 0, 0, fill="grey") # Create four rectangles to represent the modules
rectMA2 = canvas5.create_rectangle(0, 0, 0, 0, fill="grey")
rectMA3 = canvas5.create_rectangle(0, 0, 0, 0, fill="grey")
rectMA4 = canvas5.create_rectangle(0, 0, 0, 0, fill="grey")
rectMA5 = canvas5.create_rectangle(0, 0, 0, 0, fill="grey")

global lines5 # Create our lines to represent the material routes between the modules
lines5 = [canvas5.create_line(0,0,0,0),canvas5.create_line(0,0,0,0),canvas5.create_line(0,0,0,0),canvas5.create_line(0,0,0,0)]

global labelsMA
labelsMA = []

buttonMA = ttk.Button(root5, text="Clear", command=clearMA)
buttonMA.grid(row=0, column=1)

labelMA = tk.Label(root5, text="Insert a label,     x                       y                                                    text                             ")
labelMA.grid(row=1, column=1, columnspan=3, rowspan=1)

entryMA1 = ttk.Entry(root5) # Entries that allow the user to label the design
entryMA2 = ttk.Entry(root5)
entryMA3 = ttk.Entry(root5)

entryMA1.grid(row=2, column=1)
entryMA2.grid(row=2, column=2)
entryMA3.grid(row=2, column=3)

entryMA1.insert(0,0)
entryMA2.insert(0,0)
entryMA3.insert(0,"text")

buttonMA = ttk.Button(root5, text="Add Label", command=addLabelMA)
buttonMA.grid(row=3, column=1)

trackPositionMA(funcMA) # Activate the function loop that will track the coordinates that the user types in the entries

labelMAspinbox = tk.Label(root5, text="There are 5 modules you can add, select the number of the one you want to add and right click on the grid to add it.")
labelMAspinbox.grid(row=4, column=1, columnspan=10, rowspan=1)
labelMAspinbox.config(font=("Average", 12))


a = tk.Spinbox(root5, from_=1, to=5) # Create the spinbox and the asociated labels for the dragrect function
a.grid(row=5, column=1)

labelMAInstruction1 = tk.Label(root5, text="Add labels by typing in coordinates and text and clicking add, the orange box will show where the    ")
labelMAInstruction2 = tk.Label(root5, text="selected coordinates are, To delete the last object placed press shift-L, click clear to clear all   ")
labelMAInstruction3 = tk.Label(root5, text="labels, rectangles, and lines. The equipmemt is machine assembly equipment (2X the size of fabricators)")
labelMAInstruction4 = tk.Label(root5, text="Each box on the grid is 2 ft long.", bg="red", fg="yellow")

labelMAInstruction1.grid(row=6, column=1, columnspan=4, rowspan=1) # Create and place the labels that explain this tab
labelMAInstruction2.grid(row=7, column=1, columnspan=4, rowspan=1)
labelMAInstruction3.grid(row=8, column=1, columnspan=4, rowspan=1)
labelMAInstruction4.grid(row=9, column=1, columnspan=4, rowspan=1)

labelMAInstruction1.config(font=("Average", 12))
labelMAInstruction2.config(font=("Average", 12))
labelMAInstruction3.config(font=("Average", 12))
labelMAInstruction4.config(font=("Average", 12))

#8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888

frame_d = tk.Frame(demo)
frame_d.grid(rowspan = 20, columnspan = 20)

d_label = tk.Label(frame_d, text = "\nWelcome to FIRE - Facility Layout Constructor\n\nPlease answer the following questions below before proceeding\n\n Onto the next tab !\n\n ",fg  = 'blue')
d_label.grid(row = 0, column  = 10, rowspan=1, columnspan=4,padx = 100, pady = 10)
d_label.config(font = ("Average", 16 ))

# *************************************************************** Information in Demo tab *******************************************************

# labels

label_ = tk.Label(frame_d, text = " What is your age ? ")
label_.grid(row = 1, column = 11,  pady = 5)
label_.config(font = ("Ariel", 12 ))

label_1 = tk.Label(frame_d, text = " What is your educational background ? ")
label_1.grid(row = 2, column = 11, pady = 5)
label_1.config(font = ("Ariel", 12 ))

label_2 = tk.Label(frame_d, text = "What is the highest educational level you have accomplished ?")
label_2.grid(row = 3, column = 11,  pady = 5)
label_2.config(font = ("Ariel", 12 ))

label_3 = tk.Label(frame_d, text = " Please enter your desired college major (if applicable) ")
label_3.grid(row = 4, column = 11, pady = 5)
label_3.config(font = ("Ariel", 12 ))

label_4 = tk.Label(frame_d, text = "Have you had any expreince in solivng design problems ?")
label_4.grid(row = 5, column = 11,  pady = 5)
label_4.config(font = ("Ariel", 12 ))

label_5 = tk.Label(frame_d, text = "Have you had any expreince in designing a factory layout ?")
label_5.grid(row = 6, column = 11, pady = 5)
label_5.config(font = ("Ariel", 12 ))

label_6 = tk.Label(frame_d, text = "Once you have filled out the information and clicked 'Save.' Start the timer and go to the next tab\nOn the following tabs follow the instructions and your actions will be recorded", fg = 'green')
label_6.grid(row = 8, column = 11, pady = 5)
label_6.config(font = ("Ariel", 12 ))

label_7 = tk.Label(frame_d, text = " Please click Save !", fg = 'red')
label_7.grid(row = 7, column = 11, pady = 5)
label_7.config(font = ("Ariel", 12 ))

# SpinBoxe(s)

t1 = ('Student at public or private university', 'Faculty at public or private university', 'Student at high school')
sb1 = tk.Spinbox(frame_d, values=t1, width=35, font = Font(family='Ariel', size=10, weight='bold')) #textvariable=var,
sb1.grid(row = 2 , column = 12, pady = 5)

t2 = ('9th grade high school', '10th grade high school', '11th grade high school', "12th grade high school", "Graduated from high school", "1 year of college", "2 year of college" , "3 year of college", "4 year of college", "graduated from College", "Some graduate school", "Completed graduate school"   )
sb2 = tk.Spinbox(frame_d, values=t2, width=35, font = Font(family='Ariel', size=10, weight='bold')) #textvariable=var,
sb2.grid(row = 3 , column = 12, pady = 5)

t3 = ttk.Entry(frame_d, font = Font(family='Ariel', size=10, weight='bold'))
t3.grid(row = 1, column = 12)
t3.insert(0,18)

t4 = ('Yes', 'No')
sb4 = tk.Spinbox(frame_d, values=t4, width=35, font = Font(family='Ariel', size=10, weight='bold')) #textvariable=var,
sb4.grid(row = 5, column = 12, pady = 5)

t5 = ('Yes', 'No')
sb5 = tk.Spinbox(frame_d, values=t4, width=35, font = Font(family='Ariel', size=10, weight='bold')) #textvariable=var,
sb5.grid(row = 6 , column = 12, pady = 5)

t6 = ttk.Entry(frame_d, width = 25, font = Font(family='Ariel', size=10, weight='bold'))
t6.grid(row = 4, column = 12)
t6.insert(0, str("Enter you college major"))
# Save Button and the function that stores the entered data

def save(): # When the user saves their demographic data start the timer and write the data to the activity log
    s_1 = str(sb1.get())
    s_2 = str(sb2.get())
    s_3 = int(t3.get())
    s_4 = str(sb4.get())
    s_5 = str(sb5.get())
    with open('activity log.txt', 'a') as the_file:
        the_file.write(s_1+"\t"+s_2+"\t"+str(s_3)+"\t"+s_4+"\t"+s_5+"\n")

    st()
    
# Save Button and the function that stores the entered data

saveB = ttk.Button(frame_d, text = ' Save ! ', command = save)
saveB.grid(row = 7, column = 12)

class Timer(Thread):
    over=False
    pause=False
    def __init__(self,func):
        Thread.__init__(self)
        self.func=func
    def run(self):
        global t,root
        time.sleep(1)
        finish=False
        while not self.over and not finish:
            if not self.pause:
                finish=self.func()
            time.sleep(1)
        if finish:
            root.event_generate('<<pop>>', when='tail')
        t=None
    def kill(self): self.over=True
    def paus(self): self.pause=True
    def cont(self): self.pause=False

t=None
sec=None
roota.bind('<<pop>>',lambda event=None: showinfo('Oh!','Time is over!'))
e1=tk.StringVar()
e2=tk.StringVar()

def show():
    global e1,e2,sec
    e1.set('%.2d'%(sec/60))
    e2.set('%.2d'%(sec%60))
def down():
    global sec
    if sec:
        sec-=1;show()
        return False
    else: return True
def up():
    global sec
    sec+=1;show()
    return False
    
def st():
    global sec,t
    if t:t.cont();return
    sec=0;show()
    t=Timer(up)
    t.start()
def cd():
    global sec,t
    if t:t.cont();return
    sec=0
    try: sec=int(e1.get())*60
    except Exception:pass
    try: sec+=int(e2.get())
    except Exception:pass
    if not sec: return
    show()
    t=Timer(down)
    t.start()

    pass
def pus():
    global t
    t.paus()

def stp():
    global t,sec
    sec=0;show()
    if t: t.kill()
    t=None
    totalDistance = 0 # Calculate the total material travel distance
    for x in distances:
        totalDistance+=int(x)

    for l in lines3:
        totalDistance+=int(int(distance(int(canvas3.coords(l)[0]),int(canvas3.coords(l)[1]),int(canvas3.coords(l)[2]),int(canvas3.coords(l)[3])))/5)

    for l in lines4:
        totalDistance+=int(int(distance(int(canvas4.coords(l)[0]),int(canvas4.coords(l)[1]),int(canvas4.coords(l)[2]),int(canvas4.coords(l)[3])))/5)
    
    for l in lines5:
        totalDistance+=int(int(distance(int(canvas5.coords(l)[0]),int(canvas5.coords(l)[1]),int(canvas5.coords(l)[2]),int(canvas5.coords(l)[3])))/5)

    with open('activity log.txt', 'a') as the_file:
        the_file.write("Total Distance: " + str(totalDistance))

en1 = ttk.Entry(roota, textvariable = e1 ,width=10 ,justify=tk.RIGHT)
en2 = ttk.Entry(roota, textvariable = e2 ,width=10)
lb = tk.Label(roota, text = ':' )
stbtn = ttk.Button(roota, width=10, text= 'start',command =st)
pusbtn = ttk.Button(roota, width=10, text= 'pause',command =pus)
stpbtn = ttk.Button(roota, width=10, text= 'stop',command =stp)

#requirements button

reqbtn= ttk.Button(roota, text="Open Requirements Window", command=create_window)


en1.pack()
lb.pack()
en2.pack()
stbtn.pack()
#pusbtn.pack()
stpbtn.pack()

#pack req button
reqbtn.pack()

# *********************************************** CREATING DROP DOWN MENUS **********************************************************

menu = tk.Menu(roota)
roota.config(menu = menu) # "We are configuring a menu for this piece of software that we are going to use"

submenu = tk.Menu(menu) # submenu
menu.add_cascade(label = "File", menu = submenu)
submenu.add_cascade(label = "Info") # command=messagebox.showwarning(message="Creator: FIRE - Design Innovations at UMD LAB ANNEX \n Version: 1.0.0\n Established 2018")
submenu.add_cascade(label = "Open" )
submenu.add_cascade(label = "Save" )
submenu.add_cascade(label = "Save As" )
submenu.add_cascade(label = "Print" )
submenu.add_cascade(label = "Share" )
submenu.add_separator()
submenu.add_cascade(label = "Exit", command = quit)

editmenu = tk.Menu(menu)
menu.add_cascade(label = "Edit")
editmenu.add_cascade(label = "Redo")

#****************************************** STATUS BAR *******************************************************************************

v = StringVar()

def status_bar(event):
    x_v = event.x
    y_v = event.y
    v.set(str(" STATUS :  ") + str("  X :  "+ str(x_v)) + str("  Y :  " + str(y_v)))
roota.bind("<B1-Motion>", status_bar) 

status = tk.Label(roota, textvariable = str(v), bd = 1, relief = tk.SUNKEN, anchor = tk.W)

status.pack(side = tk.BOTTOM, fill = tk.X)

#****************************************** Change Color *******************************************************************************

#def change_color():
    #current_color = d_label.cget("foreground")
    #next_color = "red" if current_color == "blue" else "blue"
    #d_label.config(foreground=next_color)
    #root.after(500, change_color)

#change_color()
#****************************************** Import Image *******************************************************************************
    
canvas_imag = tk.Canvas(demo)
canvas_imag.grid(row = 0, column = 20)

#im = Image.open("fire logo.png")
#ph = im.resize((500,130), Image.ANTIALIAS)
#ph = ImageTk.PhotoImage(ph)

#label_im = tk.Label(canvas_imag, image = ph, width = 500, height = 130 )
#label_im.imag = ph

#label_im.grid(row = 0, column = 20, sticky = tk.N, pady = 10)

#***************************************Check List***************************************************************************************

#use the entry.get command to get the size#
def calcSize(entryNum1, entryNum2):
    return int(entryNum1.get()) * int(entryNum2.get())

#text vars
totalcounter = StringVar()
frameFabAreaText = StringVar()
frameFabText = StringVar()
modAssemblyAreaText = StringVar()
modAssemblyText = StringVar()
machAssemblyAreaText = StringVar()
machAssemblyText = StringVar()
paintText = StringVar()
recDepText = StringVar()
qualControlText = StringVar()
packgText = StringVar()
storageText = StringVar()
loadingDepText = StringVar()

def update():
    counter = 0
    ChecklistArr = [0,0,0,0,0,0,0,0,0,0,0,0]
    with open('checklist data.txt', 'a') as the_file:
            the_file.write(en1.get() + ":" + en2.get() +"\n")
    if(calcSize(entry3,entry4) >= 500): #Frame Fabrication
        counter += 1
        ChecklistArr[6] = 1
        frameFabAreaText.set("At Least 500 Square Feet ✔") 
    else:
        frameFabAreaText.set("At Least 500 Square Feet") 
    if(calcSize(entry7,entry8) >= 500): #Module Assembly
        counter += 1
        ChecklistArr[1] = 1
        modAssemblyAreaText.set("At Least 500 Square Feet ✔") 
    else:
        modAssemblyAreaText.set("At Least 500 Square Feet ")
    if(calcSize(entry11,entry12) >= 500): #Machine Assembly
        counter += 1
        machAssemblyAreaText.set(" At Least 500 Square Feet ✔")
        ChecklistArr[3] = 1
    else:
        machAssemblyAreaText.set(" At Least 500 Square Feet ")
    if(calcSize(entry19,entry20) >= 400): #Paint
        counter += 1
        ChecklistArr[5] = 1
        paintText.set("At Least 400 Square Feet ✔")
    else:
        paintText.set("At Least 400 Square Feet ")
    if(calcSize(entry23,entry24) >= 300): #Receiving Department
        counter += 1
        ChecklistArr[0] = 1
        recDepText.set("At Least 300 Square Feet ✔")
    else:
        recDepText.set("At Least 300 Square Feet ")
    if(calcSize(entry27,entry28) >= 400): #Quality Control
        counter += 1
        ChecklistArr[8] = 1
        qualControlText.set("At Least 400 Square Feet ✔")
    else:
        qualControlText.set("At Least 400 Square Feet ") 
    if(calcSize(entry31,entry32) >= 400): #Packaging
        counter += 1
        ChecklistArr[9] = 1
        packgText.set("At Least 400 Square Feet ✔")
    else:
        packgText.set("At Least 400 Square Feet")
    if(calcSize(entry35,entry36) >= 300): #Storage
        counter += 1
        ChecklistArr[10] = 1
        storageText.set("At Least 300 Square Feet ✔")
    else:
        storageText.set("At Least 300 Square Feet")
    if(calcSize(entry39,entry40) >= 300): #Loading Department
        counter += 1
        ChecklistArr[11] = 1
        loadingDepText.set( "At Least 300 Square Feet ✔")
    else:
        loadingDepText.set("At Least 300 Square Feet")
    if(FFarr == 5):
        counter += 1
        ChecklistArr[7] = 1
        frameFabText.set("Contains 5 Frame Modules ✔")
    else:
        frameFabText.set("Contains 5 Frame Modules ")
    if(MOarr == 5):
        counter += 1
        ChecklistArr[2] = 1
        machAssemblyText.set("Contains 5 Modules ✔")
    else:
        machAssemblyText.set("Contains 5 Modules")
    if(MAarr == 5):
        
        ChecklistArr[4] = 1
        modAssemblyText.set("Contains 5 Modules ✔")
    else:
        modAssemblyText.set("Contains 5 Modules")
    with open('checklist data.txt', 'a') as the_file:
        for check in ChecklistArr:
            the_file.write("%i" % check)
    totalcounter.set("Completed: " + str(counter) + "/12")
        
#work on distance labels
#Midpoint Distance
# def getMidPoint(x1, y1, x2, y2):
#     midpointarr = [0,0]
    
#     midpointarr[0] = int((x1+x2)/2)
#     midpointarr[1] = int((y1+y2)/2)
#     return midpointarr
#def addDistanceLabel(midpointcoord):
    
roota.mainloop()
