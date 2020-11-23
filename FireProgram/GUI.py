
#imports
import tkinter, time
import tkinter.ttk as ttk
import tkinter as tk
import uuid 
from math import sqrt
from tkinter import *
from threading import Thread
from tkinter import messagebox
from tkinter import StringVar
from tkinter.font import Font
from PIL import Image, ImageTk
from tkinter import Tk, Frame, PhotoImage, Label

#global variable
answers = ["", "","","","","",""]
factoryData = [[0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [None,None,None,None,None,None], [None,None,None,None,None,None], [["Sorter","Module Cutter","Machine Cutter"],["Internal Assemb.", "External Assemb."],["Wiring","Welding Components","Installing the Casing"],["Quality Tests"],["Packaging"],["Storing"]]]
coordSystem = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
coordLine = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
continuingLine = False
startCoord = [None,None],
coordObject = []
DataIndex = None
arealist = ["Receiving Department","Frame Fabrication","Painting Department","Module Assembly","Machine Assembly","Quality Control","Create & Package","Storage","Loading Dock"]
newList = ["Frame Fabrication"]
moveableObject = [[[],[],[]],[[],[],[]],[["Raw Material Recpt."],["Drying","Paint Prep","Painting"],["Loading"]]]
workArea = ["Receiving Department","Frame Fabrication","Painting Department","Module Assembly","Machine Assembly","Quality Control","Create & Package","Storage","Loading Dock"]
t=None #variable for mins
sec=None #variable for seconds
createWorkstationStatus = None
workstationCoord = [None,None],
workstationObject = []
topcanvas = None
requirement = [None,None,None,None,None,None,None,None,None,None]
requirementWindows = None
pathbetweenBuilding = [[],[],[],[],[],[],[],[],[],[],[]]
uuid.uuid1()
DataFileLocation = 'Data/' + str(uuid.uuid1()) + '.txt'
# DataFileLocation = 'Data/info.txt'
#timer 
class Timer(Thread):#class used to manage the counting of a clock
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

class ResizableCanvasFrame(Frame):

    labelObject = None
    workstationList = None
    color = None
    name = None
    move = None

    def __init__(self, master, xCord, yCord, wSize, hSize, xColor,xlableObject,xwordstationList,xName,xmove,*args, **kwargs):
        if (xName == "Receiving Department" or xName == "Painting Department" or xName == "Loading Dock"):
            None
        else:    
            if(TimeEntry1.get() == "" and TimeEntry2.get() == ""):
                st()
        try:
            
            # master should be a Canvas
            self.move = xmove
            x = float(xCord)*2
            y = float(yCord)*2
            w = float(wSize)*2
            h = float(hSize)*2
            # xWorkstation = canvas.create_rectangle(x,y,45,20,fill="grey")
            self.labelObject = xlableObject
            self.workstationList = xwordstationList
            self.frame_thickness = 10
            self.name = xName
            Frame.__init__(
                self,
                master,
                *args,
                borderwidth = self.frame_thickness,
                cursor = 'fleur',
                **kwargs
            )

            self.canvas = master
            self.resize_state = None
            self.bind('<Button-1>', self.mousedown)
            self.bind('<B1-Motion>', self.mousemove)
            self.bind('<ButtonRelease-1>', self.mouseup)
            # add self to canvas
            self.itemid = self.canvas.create_window(
                x,
                y,
                window=self,
                anchor="nw",
                width=w,
                height=h,
            )
            self.color = xColor
            self.configure(bg=xColor)
            self.save_callback = None

            for i in range(len(self.workstationList)):
                self.workstationList[i] = MoveableCanvasFrame(self.canvas,x,y,self.workstationList[i],w,h)
            with open(DataFileLocation, 'a') as the_file:
                the_file.write("Work Area, " +str(self.name) + " , Add, " + TimeEntry1.get() + ":" + TimeEntry2.get() + " ,(" + str(x/2) + "," + str(y/2) + "),("+str(w/2)+","+str(h/2)+")\n")

        except(ValueError):
            None
        
    def canvas_coords(self):
        returnlist = list(map(int, self.canvas.coords(self.itemid)))
        return returnlist

    def canvas_width(self):
        return int(''.join(map(str, self.canvas.itemcget(self.itemid, 'width'))))

    def canvas_height(self):
        return int(''.join(map(str, self.canvas.itemcget(self.itemid, 'height'))))

    def set_canvas(self,new_x,new_y ,new_width,new_height,label):
        self.canvas.coords(self.labelObject,float(new_x)*2+(float(new_width)),(float(new_y)*2)-10)
        self.canvas.coords(self.itemid,  float(new_x)*2,  float(new_y)*2)
        self.canvas.itemconfig(self.itemid, width=float(new_width)*2, height=float(new_height)*2)

    def getColor(self):
        return self.color

    def move(self, dx, dy):
        self.canvas.move(self.itemid, dx, dy)

    def mousedown(self, event):
        window_width = self.winfo_width()
        window_height = self.winfo_height()
        self.resize_state = {
            'start_coords': (event.x, event.y),
            'last_coords': (event.x, event.y),
            'left_edge': (0 <= event.x < self.frame_thickness),
            'right_edge': (window_width - self.frame_thickness <= event.x < window_width),
            'top_edge': (0 <= event.y < self.frame_thickness),
            'bottom_edge': (window_height - self.frame_thickness <= event.y < window_height),
        }            

    def mousemove(self, event):
        if(self.move):
            if self.resize_state:
                resize = self.resize_state # debug var
                event_x = event.x
                event_y = event.y
                # distance of cursor from original position of window
                delta = map(int, (event.x - self.resize_state['start_coords'][0], event.y - self.resize_state['start_coords'][1]))
                # load current pos, size
                new_x, new_y = self.canvas_coords()
                new_width = int(self.canvas.itemcget(self.itemid, 'width'))
                new_height = int(self.canvas.itemcget(self.itemid, 'height'))
                deltaList = list(delta)
                # handle x resize/move
                if self.resize_state['left_edge']:
                    # must move pos and resize
                    new_x += deltaList[0]
                    new_width -= deltaList[0]
                elif self.resize_state['right_edge']:
                    new_width += (event.x - self.resize_state['last_coords'][0])
                # handle y resize/move
                if self.resize_state['top_edge']:
                    new_y += deltaList[1]
                    new_height -= deltaList[1]
                elif self.resize_state['bottom_edge']:
                    new_height += (event.y - self.resize_state['last_coords'][1])
                # save new settings in item, not card yet
                self.resize_state['last_coords'] = (event.x, event.y)
                self.canvas.coords(self.labelObject,new_x+(new_width/2),new_y-10)
                self.canvas.coords(self.itemid, new_x, new_y)
                self.canvas.itemconfig(self.itemid, width=new_width, height=new_height)
                for i in range(len(self.workstationList)):
                    self.workstationList[i].setWidthheight(new_x,new_y,new_width,new_height)
                refreshCoord()
        else:
            None

    def mouseup(self, event):
        with open(DataFileLocation, 'a') as the_file:
            listCoord = list(map(int, self.canvas.coords(self.itemid)))
            the_file.write("Work Area, " +str(self.name) + " , Resize, " + TimeEntry1.get() + ":" + TimeEntry2.get() + " ,(" + str(listCoord[0]/2) + "," + str(listCoord[1]/2) + "),("+str(int(''.join(map(str, self.canvas.itemcget(self.itemid, 'width'))))/2)+","+str(int(''.join(map(str, self.canvas.itemcget(self.itemid, 'height'))))/2)+")\n")
        if self.resize_state:
            self.resize_state = None
            if self.save_callback:
                self.save_callback()

class MoveableCanvasFrame(Frame):
    
    xValue = None
    yValue = None
    width = None
    height = None
    label = None

    def __init__(self, master, x, y,xlabel,xwidth,xheight, *args, **kwargs):
        # master should be a Canvas
        self.label = xlabel
        self.xValue = x
        self.yValue = y
        self.width = xwidth
        self.height = xheight
        self.frame_thickness = 90
        Frame.__init__(
            self,
            master,
            *args,
            borderwidth = self.frame_thickness,
            cursor = 'fleur',
            **kwargs
        )
        self.canvas = master
        self.resize_state = None

        text = tk.Label(self.canvas, text= xlabel)
        text.bind('<Button-1>', self.mousedown)
        text.bind('<B1-Motion>', self.mousemove)
        text.bind('<ButtonRelease-1>', self.mouseup)
        text.config(font=("Courier", 8))
        text.config(state=DISABLED)
        text.config(cursor = 'fleur')
        self.itemid = self.canvas.create_window(
            x,
            y,
            window=text,
            anchor="nw",
            width=90,
            height=40,
        )

        self.configure(bg='Grey')
        self.save_callback = None
        with open(DataFileLocation, 'a') as the_file:
            the_file.write("Work Station, " +str(self.label) + " , Add, " + TimeEntry1.get() + ":" + TimeEntry2.get() + " ,(" + str(self.xValue/2) + "," + str(self.yValue/2) + ")\n")

    def setWidthheight(self,x,y,xwidth,xheight):
        self.xValue = x
        self.yValue = y
        self.width = xwidth
        self.height = xheight

    def getName(self):
        return self.label

    def mousedown(self, event):
        window_width = self.winfo_width()
        window_height = self.winfo_height()
        self.resize_state = {
            'start_coords': (event.x, event.y),
            'last_coords': (event.x, event.y),
        } 

    def getName(self):
        return self.label

    def mousemove(self, event):
        if self.resize_state:
            resize = self.resize_state # debug var
            event_x = event.x
            event_y = event.y
            # distance of cursor from original position of window
            delta = map(int, (event.x - self.resize_state['start_coords'][0], event.y - self.resize_state['start_coords'][1]))
            # load current pos, size
            new_x, new_y = self.canvas_coords()
            deltaList = list(delta)
            # handle x move
            new_x += deltaList[0]
            # handle y move
            new_y += deltaList[1]
            # save new settings in item, not card yet
            self.resize_state['last_coords'] = (event.x, event.y)
            if((new_x < int(self.xValue)) and (new_y < int(self.yValue))):
                self.canvas.coords(self.itemid, self.xValue, self.yValue)
            elif(new_x + 45 > int(self.width)+int(self.xValue) and new_y < int(self.yValue)):
                self.canvas.coords(self.itemid, (int(self.width)+int(self.xValue)-45), self.yValue)
            elif(new_x + 45 > int(self.width)+int(self.xValue) and (new_y + 20 > int(self.height)+int(self.yValue))):
                self.canvas.coords(self.itemid, (int(self.width)+int(self.xValue)-45), (int(self.height)+int(self.yValue)-20))
            elif((new_x < int(self.xValue))and(new_y + 20 > int(self.height)+int(self.yValue))):
                self.canvas.coords(self.itemid, self.xValue, (int(self.height)+int(self.yValue)-20))
            elif(new_x < int(self.xValue)):
                self.canvas.coords(self.itemid, self.xValue, new_y)
            elif(new_y < int(self.yValue)):
                self.canvas.coords(self.itemid, new_x, self.yValue)
            elif(new_x + 45 > int(self.width)+int(self.xValue)):
                self.canvas.coords(self.itemid, (int(self.width)+int(self.xValue)-45), new_y)
            elif(new_y + 20 > (int(self.height)+int(self.yValue))):    
                self.canvas.coords(self.itemid, new_x, (int(self.height)+int(self.yValue)-20))    
            else:
                self.canvas.coords(self.itemid, new_x, new_y)
            
            # with open(DataFileLocation, 'a') as the_file:
                # the_file.write("Workstation" +" "+ str(self.itemid.window) + "," + "Move" + "," + TimeEntry1.get() + ":" + TimeEntry2.get() + "," + "(" + str(new_x) + "," + str(new_y) + ")")

    def mouseup(self, event):
        with open(DataFileLocation, 'a') as the_file:
            listCoord = list(map(int, self.canvas.coords(self.itemid)))
            the_file.write("Work Station, " +str(self.label) + " , Resize, " + TimeEntry1.get() + ":" + TimeEntry2.get() + " ,(" + str(listCoord[0]/2) + "," + str(listCoord[1]/2) + ")\n")
        if self.resize_state:
            self.resize_state = None
            if self.save_callback:
                self.save_callback()

    def canvas_coords(self):
        returnlist = list(map(int, self.canvas.coords(self.itemid)))
        # print(returnlist)
        return returnlist
             
def uploadGoogleDrive():
    from pydrive.auth import GoogleAuth
    from pydrive.drive import GoogleDrive
    #Login to Google Drive and create drive object
    g_login = GoogleAuth()
    g_login.LocalWebserverAuth()
    drive = GoogleDrive(g_login)
    # Importing os and glob to find all PDFs inside subfolder
    import glob, os
    os.chdir("Data/")
    for file in glob.glob("*.txt"):
        # print (file)
        with open(file,"r") as f:
            fn = os.path.basename(f.name)
            file_drive = drive.CreateFile({'title': fn })  
        # file_drive.SetContentString(f.read()) 
        file_drive.Upload()
        print("The file: " + fn + " has been uploaded")
    
    print ("All files have been uploaded")

def createHelpwindow(helpIndex):
    label = tk.Label()
    if helpIndex == 1:
        helpwindows1 = tk.Toplevel(root) 
        label = tk.Label(helpwindows1, text = 'Answer the questions to the best of you ability to help our data collection. If one of the dropdowns does not have an option that accurately describes you, simply choose one that is as close as possible. Be sure to read the questions carefully and make sure you answer them all.', wraplength = 500)    
    elif helpIndex == 2:
        helpwindows2 = tk.Toplevel(root) 
        label = tk.Label(helpwindows2, text = "To place a work area, fill in the size parameter for that area then click where you want the center of the area to be located."+"\n" + "To place a work station, use the dropdowns to select both the work area and work station that belongs in the work area, then click where you want its center."+"\n"+" Note: If you can not remember which stations go to which areas, review the diagram on the first tab."+ "\n" + " To place the lines between work stations, left-click for the starting point and then right-click for the end point.", wraplength = 500)
    elif helpIndex == 3:
        helpwindows3 = tk.Toplevel(root) 
        label = tk.Label(helpwindows3, text = 'More About Background Info. and Problem Statement')
    label.pack()

def displayText(xframe, Xrow, Xcol, Xtext, size, XcolSpan):
    Label = tk.Label(xframe, text= Xtext, wraplength = root.winfo_screenwidth()-400)
    Label.grid(row = Xrow, column = Xcol , columnspan = 1)
    Label.config(font = ("Times New Roman", size ), anchor = 'center')

def displayTextBox(xframe, Xrow, Xcol, Xtext, Xwidth, Xcolor):
    Label1 = tk.Label(xframe, text = Xtext)
    Label1.config(width = Xwidth, bg = Xcolor)
    Label1.grid(row = Xrow, column =Xcol)    

def displayBox(xframe, Xrow, Xcol, Xwidth):
    data = tk.Entry(xframe, width = Xwidth) 
    data.grid(row = Xrow, column = Xcol)
    return data

def displayDropdown(xframe, Xrow, Xcol, width, Xlist):
    MenuVar = StringVar(xframe)
    backgrounds = Xlist
    MenuVar.set(backgrounds[0]) 
    dropDown = OptionMenu(xframe, MenuVar, *backgrounds)
    dropDown.grid(row = Xrow, column = Xcol)
    dropDown.config(width = width)
    return MenuVar

def updateDropdownWorkstation2():

    var = StringVar(areaFrame)
    workstation2.delete(0, 'end')
    for choice in newList:
        workstation2['menu'].add_command(label=choice, command=tk._setit(newList[0], choice))
    var.set(newList[0])

def displayYesorNo(xframe, Xrow):
    optionsVar = StringVar(xframe)
    yesOrNo = [('Yes', 'Yes'), ('No', 'No')]
    optionsVar.set('Yes')
    count = 1
    for text, mode in yesOrNo:
        designExperienceRB = Radiobutton(xframe, variable = optionsVar, value = mode, text = text)
        designExperienceRB.grid(row = Xrow, column = count)
        designExperienceRB.config(font = ("Times New Roman", 10))
        count += 1
    return optionsVar

def displayBoxFreeze(xframe, Xrow, Xcol, Xtext, xWidth, Xcolor, xBorder):
    box = tk.Label(xframe, text = Xtext, width = xWidth)
    box.grid(row = Xrow, column = Xcol)
    box.config(bg = Xcolor, relief = xBorder)

def displayRadiobutton(xframe, Xrow, Xcol, choices):
    optionsVar = StringVar(xframe)
    optionsVar.set(choices[0])
    for val, choices in enumerate(choices):
        radioButton = tk.Radiobutton(xframe ,variable=optionsVar, value=val,text=choices)
        radioButton.grid(row=Xrow+val, column=Xcol)
        radioButton.config(font=("Times New Roman", 10))
    return optionsVar

def displayButton(xframe, xrow,xcol,xcolspan,xwidth,xtext,xCommand):
    button = tk.Button(xframe, text = xtext, command=xCommand)
    button.grid(row = xrow, column = xcol, columnspan = xcolspan)
    button.config(width = xwidth)

def checkValue(): 
    global factoryData
    localdata = [[0 for x in range(4)] for y in range(6)]
    # for i in range(len(factoryData)-2):
    #     for j in range(len(factoryData[i])):
    #         print( factoryData[i][j].get())
    return True        

def updateDropdown(self= None, *arg):

    global newList
    if(workstation1.get() == "Receiving Department"):
        newList = ["Frame Fabrication"]
    elif(workstation1.get() == "Frame Fabrication"):
        newList = ["Painting Department"]
    elif(workstation1.get() == "Painting Department"):
        newList = ["Module Assembly","Machine Assembly"]
    elif(workstation1.get() == "Module Assembly"):
        newList = ["Machine Assembly"]
    elif(workstation1.get() == "Machine Assembly"):
        newList = ["Quality Control"]
    elif(workstation1.get() == "Quality Control"):
        newList = ["Create & Package"]
    elif(workstation1.get() == "Create & Package"):
        newList = ["Storage"]
    elif(workstation1.get() == "Storage"):
        newList = ["Loading Dock"]        
    refresh()
    
def refresh():
    # Reset var and delete all old options
    global newList
    var.set('')
    workstation2['menu'].delete(0, 'end')

    # Insert list of new options (tk._setit hooks them up to var)
    new_choices = newList
    for choice in new_choices:
        workstation2['menu'].add_command(label=choice, command=tk._setit(var, choice))

def getWorkstation2():
    return var.get() 
   
def applyCoord(self=None):
    
    try:
        global factoryData
        if(checkValue()):  
            if(factoryData[4][0] == None):
                factoryData[5][0] = canvas.create_text((((float(factoryData[0][0].get())*2)+int(factoryData[2][0].get())),((float(factoryData[1][0].get())*2)-10)), text="Frame Fabrication")
                factoryData[4][0] = ResizableCanvasFrame(canvas,factoryData[0][0].get(),factoryData[1][0].get(),factoryData[2][0].get(),factoryData[3][0].get(),"Blue",factoryData[5][0],factoryData[6][0],"Frame Fabrication",True)
            
            else:    
                factoryData[4][0].set_canvas(factoryData[0][0].get(),factoryData[1][0].get(),factoryData[2][0].get(),factoryData[3][0].get(),factoryData[5][0])
            
            if(factoryData[4][1] == None):
                factoryData[5][1] = canvas.create_text((((float(factoryData[0][1].get())*2)+int(factoryData[2][1].get())),((float(factoryData[1][1].get())*2)-10)), text="Module Assembly")
                factoryData[4][1] = ResizableCanvasFrame(canvas,factoryData[0][1].get(),factoryData[1][1].get(),factoryData[2][1].get(),factoryData[3][1].get(),"Green",factoryData[5][1],factoryData[6][1],"Module Assembly",True)

            else: 
                factoryData[4][1].set_canvas(factoryData[0][1].get(),factoryData[1][1].get(),factoryData[2][1].get(),factoryData[3][1].get(),factoryData[5][1])
            
            if(factoryData[4][2] == None):
                factoryData[5][2] = canvas.create_text((((float(factoryData[0][2].get())*2)+int(factoryData[2][2].get())),((float(factoryData[1][2].get())*2)-10)), text="Machine assembly")
                factoryData[4][2] = ResizableCanvasFrame(canvas,factoryData[0][2].get(),factoryData[1][2].get(),factoryData[2][2].get(),factoryData[3][2].get(),"Cyan",factoryData[5][2],factoryData[6][2],"Machine assembly",True)

            else:    
                factoryData[4][2].set_canvas(factoryData[0][2].get(),factoryData[1][2].get(),factoryData[2][2].get(),factoryData[3][2].get(),factoryData[5][2])
            
            if(factoryData[4][3] == None):
                factoryData[5][3] = canvas.create_text((((float(factoryData[0][3].get())*2)+int(factoryData[2][3].get())),((float(factoryData[1][3].get())*2)-10)), text="Quality Control")
                factoryData[4][3] = ResizableCanvasFrame(canvas,factoryData[0][3].get(),factoryData[1][3].get(),factoryData[2][3].get(),factoryData[3][3].get(),"Orange",factoryData[5][3],factoryData[6][3],"Quality Control",True)

            else:    
                factoryData[4][3].set_canvas(factoryData[0][3].get(),factoryData[1][3].get(),factoryData[2][3].get(),factoryData[3][3].get(),factoryData[5][3])

            if(factoryData[4][4] == None):
                factoryData[5][4] = canvas.create_text((((float(factoryData[0][4].get())*2)+int(factoryData[2][4].get())),((float(factoryData[1][4].get())*2)-10)), text="Packaging")
                factoryData[4][4] = ResizableCanvasFrame(canvas,factoryData[0][4].get(),factoryData[1][4].get(),factoryData[2][4].get(),factoryData[3][4].get(),"Magenta",factoryData[5][4],factoryData[6][4],"Packaging",True)
            
            else:    
                factoryData[4][4].set_canvas(factoryData[0][4].get(),factoryData[1][4].get(),factoryData[2][4].get(),factoryData[3][4].get(),factoryData[5][4])
                
            if(factoryData[4][5] == None):
                factoryData[5][5] = canvas.create_text((((float(factoryData[0][5].get())*2)+int(factoryData[2][5].get())),((float(factoryData[1][5].get())*2)-10)), text="Storage")
                factoryData[4][5] = ResizableCanvasFrame(canvas,factoryData[0][5].get(),factoryData[1][5].get(),factoryData[2][5].get(),factoryData[3][5].get(),"Gold",factoryData[5][5],factoryData[6][5],"Storage",True)
            
            else:    
                factoryData[4][5].set_canvas(factoryData[0][5].get(),factoryData[1][5].get(),factoryData[2][5].get(),factoryData[3][5].get(),factoryData[5][5])
        else:
            errorWindow()
    except TclError:
        None
    except ValueError:
        None    

def refreshCoord():
    if(factoryData[4][0] != None):
        coord = factoryData[4][0].canvas_coords()
        coord[0] = '%g'%(coord[0]/2)
        coord[1] = '%g'%(coord[1]/2)
        factoryData[0][0].delete(0, 'end')
        factoryData[0][0].insert(0, coord[0])
        factoryData[1][0].delete(0, 'end')
        factoryData[1][0].insert(0, coord[1])
        factoryData[2][0].delete(0, 'end')
        factoryData[2][0].insert(0, factoryData[4][0].canvas_width()/2)
        factoryData[3][0].delete(0, 'end')
        factoryData[3][0].insert(0, factoryData[4][0].canvas_height()/2)
    if(factoryData[4][1] != None):
        coord = factoryData[4][1].canvas_coords()
        coord[0] = '%g'%(coord[0]/2)
        coord[1] = '%g'%(coord[1]/2)
        factoryData[0][1].delete(0, 'end')
        factoryData[0][1].insert(0, coord[0])
        factoryData[1][1].delete(0, 'end')
        factoryData[1][1].insert(0, coord[1])
        factoryData[2][1].delete(0, 'end')
        factoryData[2][1].insert(0, factoryData[4][1].canvas_width()/2)
        factoryData[3][1].delete(0, 'end')
        factoryData[3][1].insert(0, factoryData[4][1].canvas_height()/2)
    if(factoryData[4][2] != None):
        coord = factoryData[4][2].canvas_coords()
        coord[0] = '%g'%(coord[0]/2)
        coord[1] = '%g'%(coord[1]/2)
        factoryData[0][2].delete(0, 'end')
        factoryData[0][2].insert(0, coord[0])
        factoryData[1][2].delete(0, 'end')
        factoryData[1][2].insert(0, coord[1])
        factoryData[2][2].delete(0, 'end')
        factoryData[2][2].insert(0, factoryData[4][2].canvas_width()/2)
        factoryData[3][2].delete(0, 'end')
        factoryData[3][2].insert(0, factoryData[4][2].canvas_height()/2)
    if(factoryData[4][3] != None):
        coord = factoryData[4][3].canvas_coords()
        coord[0] = '%g'%(coord[0]/2)
        coord[1] = '%g'%(coord[1]/2)
        factoryData[0][3].delete(0, 'end')
        factoryData[0][3].insert(0, coord[0])
        factoryData[1][3].delete(0, 'end')
        factoryData[1][3].insert(0, coord[1])
        factoryData[2][3].delete(0, 'end')
        factoryData[2][3].insert(0, factoryData[4][3].canvas_width()/2)
        factoryData[3][3].delete(0, 'end')
        factoryData[3][3].insert(0, factoryData[4][3].canvas_height()/2)    
    if(factoryData[4][4] != None):
        coord = factoryData[4][4].canvas_coords()
        coord[0] = '%g'%(coord[0]/2)
        coord[1] = '%g'%(coord[1]/2)        
        factoryData[0][4].delete(0, 'end')
        factoryData[0][4].insert(0, coord[0])
        factoryData[1][4].delete(0, 'end')
        factoryData[1][4].insert(0, coord[1])
        factoryData[2][4].delete(0, 'end')
        factoryData[2][4].insert(0, factoryData[4][4].canvas_width()/2)
        factoryData[3][4].delete(0, 'end')
        factoryData[3][4].insert(0, factoryData[4][4].canvas_height()/2)
    if(factoryData[4][5] != None):
        coord = factoryData[4][5].canvas_coords()
        coord[0] = '%g'%(coord[0]/2)
        coord[1] = '%g'%(coord[1]/2)
        factoryData[0][5].delete(0, 'end')
        factoryData[0][5].insert(0, coord[0])
        factoryData[1][5].delete(0, 'end')
        factoryData[1][5].insert(0, coord[1])
        factoryData[2][5].delete(0, 'end')
        factoryData[2][5].insert(0, factoryData[4][5].canvas_width()/2)
        factoryData[3][5].delete(0, 'end')
        factoryData[3][5].insert(0, factoryData[4][5].canvas_height()/2)       

def requirementList():
    global requirement
    requirementWindows = Toplevel()
    #Title
    requirementWindows.title("Requirement Check List")
    requirementWindows.iconbitmap('asset/fire logo icon2.ico')
    msg1 = Label(requirementWindows, text="Requirements List:   ✔  ", borderwidth=1, justify=RIGHT, font=('Times', '18', 'bold')).pack()
    #Receiving Room Req
    #Module Assemble
    msg2 = Label(requirementWindows, text="Module Assembly:  ", borderwidth=1, justify=LEFT,font =('Times', '18') ).pack()
    requirement[0] = Label(requirementWindows, text= "At Least 6000 Square Feet", borderwidth=1, justify=CENTER )
    requirement[0].pack()
    #Machine Assembly
    msg3 = Label(requirementWindows, text="Machine Assembly:", borderwidth=1, justify=LEFT,font =('Times', '18') ).pack()
    requirement[1] = Label(requirementWindows, text= "At least 7000 Square Feet", borderwidth=1, justify=CENTER )
    requirement[1].pack()
    #Frame Fabrication
    msg4 = Label(requirementWindows, text="Frame Fabrication: ", borderwidth=1, justify=LEFT,font =('Times', '18') ).pack()
    requirement[2] = Label(requirementWindows, text= "At Least 8000 Square Feet", borderwidth=1, justify=CENTER )
    requirement[2].pack()
    #Quality Control
    msg5 = Label(requirementWindows, text="Quality Control:      ", borderwidth=1, justify=LEFT,font =('Times', '18') ).pack()
    requirement[3] = Label(requirementWindows, text="At Least 5000 Square Feet", borderwidth=1, justify=CENTER )
    requirement[3].pack()
    #Packaging
    msg6 = Label(requirementWindows, text="Packaging:                ", borderwidth=1, justify=LEFT,font =('Times', '18') ).pack()
    requirement[4] = Label(requirementWindows, text="At Least 5000 Square Feet", borderwidth=1, justify=CENTER )
    requirement[4].pack()
    #Storage
    msg7 = Label(requirementWindows, text="Storage:                   ", borderwidth=1, justify=LEFT,font =('Times', '18')).pack()
    requirement[5] = Label(requirementWindows, text="At Least 5000 Square Feet", borderwidth=1, justify=CENTER )
    requirement[5].pack()
    #Update Button
    
    msg8 = Label(requirementWindows, text="General Requirement:                   ", borderwidth=1, justify=CENTER,font =('Times', '18')).pack()
    msg9 = Label(requirementWindows, text="Path Between building", borderwidth=1, justify=LEFT ).pack()

    #pathbetweenBuilding[0] = Label(requirementWindows, text="Recieving Department to Frame Frabication", borderwidth=1, justify=LEFT )
    #pathbetweenBuilding[0].pack()
    #pathbetweenBuilding[1] = Label(requirementWindows, text="Frame Frabication to Painting Department", borderwidth=1, justify=LEFT )
    #pathbetweenBuilding[1].pack()
    #pathbetweenBuilding[2] = Label(requirementWindows, text = "Painting Department to Module Assembly",borderwidth=1, justify=LEFT)
    #pathbetweenBuilding[2].pack()
    #pathbetweenBuilding[3] = Label(requirementWindows, text = "Painting Department to Machine Assembly",borderwidth=1, justify=LEFT)
    #pathbetweenBuilding[3].pack()
    #pathbetweenBuilding[4] = Label(requirementWindows, text = "Module Assembly to Machine Assembly",borderwidth=1, justify=LEFT)    
    #pathbetweenBuilding[4].pack()
    #pathbetweenBuilding[5] = Label(requirementWindows, text = "Machine Assembly to Quality Control",borderwidth=1, justify=LEFT)    
    #pathbetweenBuilding[5].pack()
    #pathbetweenBuilding[6] = Label(requirementWindows, text = "Quality Control to Crate & Package",borderwidth=1, justify=LEFT)    
    #pathbetweenBuilding[6].pack()
    #pathbetweenBuilding[7] = Label(requirementWindows, text = "Crate & Package to Storage",borderwidth=1, justify=LEFT)    
    #pathbetweenBuilding[7].pack()
    #pathbetweenBuilding[8] = Label(requirementWindows, text = "Storage to Loading Dock",borderwidth=1, justify=LEFT)    
    #pathbetweenBuilding[8].pack()
    #MyButton = Button(requirementWindows, text='Update Checklist', command=update).pack()
    with open(DataFileLocation, 'a') as the_file:
        the_file.write("Checklist, Show," + TimeEntry1.get() + ":" + TimeEntry2.get()+"\n")    

def getSize(area):
    w = area.canvas_width()/2
    h = area.canvas_height()/2
    return w*h

def checkIfpathexist(building1, building2, path):
    coords1 = building1.canvas_coords()
    width1 = building1.canvas_width()*2
    height1 = building1.canvas_height()*2
    coords2 = building2.canvas_coords()
    width2 = building2.canvas_width()*2
    height2 = building2.canvas_height()*2
    counter = 0
    for x in range(len(path)):
        if((coords2[0] + width2 + 10) > path[x][0] and coords2[1] + height2 + 10 > path[x][1]):
            counter += 1
        elif((coords2[0] + width2 + 10) > path[x][0] and coords2[1] - 10 < path[x][1]):
            counter += 1
        elif(coords1[0] - 10 > path[x][0] and coords2[1] + height2 + 10 > path[x][1]):
                counter += 1
        elif(coords1[0] - 10 > path[x][0] and coords2[1] - 10 < path[x][1]):
            counter += 1 
        
        elif((coords1[0] + width1 + 10) > path[x][0] and coords1[1] + height1 + 10 > path[x][1]):
                counter += 1
        elif((coords1[0] + width1 + 10) > path[x][0] and coords1[1] - 10 < path[x][1]):
            counter += 1

        elif(coords2[0] - 10 > path[x][0] and coords1[1] + height1 + 10 > path[x][1]):
                counter += 1
        elif(coords2[0] - 10 > path[x][0] and coords1[1] - 10 < path[x][1]):
            counter += 1            
        if(counter >= 2):
            return True    
    return False

#def update():
    global requirement,factoryData,pathbetweenBuilding
    count = 0
    #FF
    if(int(getSize(factoryData[4][0])) >= 8000):
        requirement[2].config(text="At Least 8000 Square Feet      ✔   ")
        count += 1
    else:
        requirement[2].config(text="At Least 8000 Square Feet          ")

    #ModA
    if(int(getSize(factoryData[4][1]) >= 6000)):
        requirement[0].config(text="At Least 6000 Square Feet      ✔   ")
        count += 1
    else:
        requirement[0].config(text="At Least 6000 Square Feet          ")
    
    #MACH A
    if(int(getSize(factoryData[4][2]) >= 7000)):
        requirement[1].config(text="At Least 7000 Square Feet      ✔   ")
        count += 1
    else:
        requirement[1].config(text="At Least 7000 Square Feet         ")

    if(int(getSize(factoryData[4][3]) >= 5000)):
        requirement[3].config(text="At Least 5000 Square Feet      ✔   ")
        count += 1
    else:
        requirement[3].config(text="At Least 5000 Square Feet         ")
    
    if(int(getSize(factoryData[4][4]) >= 5000)):
        requirement[4].config(text="At Least 5000 Square Feet      ✔   ")
        count += 1
    else:
        requirement[4].config(text="At Least 5000 Square Feet         ")

    if(int(getSize(factoryData[4][5]) >= 5000)):
        requirement[5].config(text="At Least 5000 Square Feet      ✔   ")
        count += 1
    else:
        requirement[5].config(text="At Least 5000 Square Feet         ") 

    if(checkIfpathexist(moveableObject[1][0],factoryData[4][0],coordLine[0])):
        pathbetweenBuilding[0].config(text="Recieving Department to Frame Frabication      ✔   ")
        count += 1
    else:
        pathbetweenBuilding[0].config(text="Recieving Department to Frame Frabication         ") 

    if(checkIfpathexist(factoryData[4][0],moveableObject[1][1],coordLine[1])):
        pathbetweenBuilding[1].config(text="Frame Frabication to Painting Department      ✔   ")
        count += 1
    else:
        pathbetweenBuilding[1].config(text="Frame Frabication to Painting Department         ")     

    if(checkIfpathexist(moveableObject[1][1],factoryData[4][1],coordLine[2])):
        pathbetweenBuilding[2].config(text="Painting Department to Module Assembly      ✔   ")
        count += 1
    else:
        pathbetweenBuilding[2].config(text="Painting Department to Module Assembly         ")    

    if(checkIfpathexist(factoryData[4][1],factoryData[4][2],coordLine[3])):
        pathbetweenBuilding[3].config(text="Module Assembly to Machine Assembly      ✔   ")
        count += 1
    else:
        pathbetweenBuilding[3].config(text="Module Assembly to Machine Assembly         ")

    if(checkIfpathexist(moveableObject[1][1],factoryData[4][2],coordLine[4])):
        pathbetweenBuilding[4].config(text="Painting Department to Machine Assembly      ✔   ")
        count += 1
    else:
        pathbetweenBuilding[4].config(text="Painting Department to Machine Assembly         ")

    if(checkIfpathexist(factoryData[4][2],factoryData[4][3],coordLine[5])):
        pathbetweenBuilding[5].config(text="Painting Department to Quality Control      ✔   ")
        count += 1
    else:
        pathbetweenBuilding[5].config(text="Painting Department to Quality Control         ") 

    if(checkIfpathexist(factoryData[4][3],factoryData[4][4],coordLine[6])):
        pathbetweenBuilding[6].config(text="Quality Control to Create & Package      ✔   ")
        count += 1
    else:
        pathbetweenBuilding[6].config(text="Quality Control to Create & Package         ")

    if(checkIfpathexist(factoryData[4][4],factoryData[4][5],coordLine[7])):
        pathbetweenBuilding[7].config(text="Create & Package to Storage      ✔   ")
        count += 1
    else:
        pathbetweenBuilding[7].config(text="Create & Package to Storage         ") 

    if(checkIfpathexist(factoryData[4][5],moveableObject[1][2],coordLine[8])):
        pathbetweenBuilding[8].config(text="Storage to Loading Dock       ✔   ")
        count += 1
    else:
        pathbetweenBuilding[8].config(text="Storage to Loading Dock         ") 

    with open(DataFileLocation, 'a') as the_file:
        the_file.write("Checklist, Update, " + TimeEntry1.get() + ":" + TimeEntry2.get() + " , finish " + str(count)+"\n")        

def save(): #function to save all of the demo info to the activity log text file
    global answers
    with open(DataFileLocation, 'a') as the_file:
        the_file.write(answers[0].get()+ " " + answers[1].get()+ " " + answers[2].get()+ " "+ answers[3].get()+ " "+ answers[4].get()+ " "+ answers[5].get())    

#pop-up window for out of bounds message
def errorWindow():
    messagebox.showerror("Error", "Can't place area outside of factory area")
#error pop-up window for area size message
def error1Window():
    messagebox.showerror("Error2", "Area does not fit requirements")

def show(): #function that shows the time on the GUI
    global TimeEntry1, TimeEntry2,sec #uses these global variables
    TimeEntry1.set('%.2d'%(sec/60)) #sets the min section
    TimeEntry2.set('%.2d'%(sec%60)) #sets the secs section

def up(): #counts up the timer
    global sec
    sec+=1;show()
    return False   

def st():#starts the timer that will be displayed
    global sec,t
    if t:t.cont();return
    sec=0;show()
    t=Timer(up)
    t.start()

def stp():#stops the timer that will be displayed
    global t,sec
    sec=0;show()
    if t: t.kill()
    t=None
    uploadGoogleDrive()

def distanceFunction():
    global coordLine
    allTotaldistance = 0
    for i in range(len(coordLine)):
        totaldistance = 0
        for j in range(len(coordLine[i])):
            if j < len(coordLine[i]) - 1 :
                None
            else:
                firstValue = list(coordLine[i][j])
                secondValue = list(coordLine[i][j-1])
                x1 = firstValue[0]
                y1 = firstValue[1]
                x2 = secondValue[0]
                y2 = secondValue[1]
                totaldistance += pow( pow((x2 - x1),2) +  pow((y2 - y1),2) , 1/2)
        allTotaldistance += totaldistance

    with open(DataFileLocation, 'a') as the_file:
        the_file.write("Distance Calculator, Show, " + TimeEntry1.get() + ":" + TimeEntry2.get() + "," + str(allTotaldistance))              

    messagebox.showinfo("Total Distance", "Total Distance are " + str(allTotaldistance))
    
def createLineobject():
    global factoryData,continuingLine,DataIndex
    doLoop = True
    for i in range(len(factoryData[4])):
        if(factoryData[4][i] == None):
            doLoop = False
    doLoop = True            
    if(doLoop):
        if(workstation1.get() == "Receiving Department" and getWorkstation2() == "Frame Fabrication"):
            DataIndex = 0
        elif(workstation1.get() == "Frame Fabrication" and getWorkstation2() == "Painting Department"):
            DataIndex = 1
        elif(workstation1.get() == "Painting Department" and getWorkstation2() == "Module Assembly"):
            DataIndex = 2
        elif(workstation1.get() == "Module Assembly" and getWorkstation2() == "Machine Assembly"):
            DataIndex = 3
        elif(workstation1.get() == "Painting Department" and getWorkstation2() == "Machine Assembly"):
            DataIndex = 4              
        elif(workstation1.get() == "Machine Assembly" and getWorkstation2() == "Quality Control"):
            DataIndex = 5
        elif(workstation1.get() == "Quality Control" and getWorkstation2() == "Create & Package"):
            DataIndex = 6
        elif(workstation1.get() == "Create & Package" and getWorkstation2() == "Storage"):
            DataIndex = 7
        elif(workstation1.get() == "Storage" and getWorkstation2() == "Loading Dock"):
            DataIndex = 8
        else:
            messagebox.showinfo("Something went wrong", "Contact Sam")
        continuingLine = True
    else:
        
        messagebox.showerror("Error3", "Place all of the building first")

def stopAdd():
    global continuingLine,coordObject,coordSystem,DataIndex,startCoord
    continuingLine = False
    coordSystem[DataIndex]=coordObject.copy()
    coordLine[DataIndex] = startCoord.copy()
    startCoord = [None,None],
    coordObject = []

def deleteLineobject():
    global coordObject,startCoord

    for i in range (len(coordObject)):
        canvas.delete(coordObject[i])
    startCoord = [None,None],
    coordObject = []

def drawLine(event):
    global startCoord,coordObject
    if(continuingLine):
        if(startCoord[0] == [None,None]):
            startCoord = [[event.x, event.y]]
        else:
            if( abs(startCoord[len(startCoord)-1][0] - event.x) > abs(startCoord[len(startCoord)-1][1] - event.y)):
                startCoord.append([event.x, startCoord[len(startCoord)-1][1]])
            else:
                startCoord.append([startCoord[len(startCoord)-1][0], event.y])
            coordObject.append(canvas.create_line(startCoord[len(startCoord)-2][0],startCoord[len(startCoord)-2][1],startCoord[len(startCoord)-1][0],startCoord[len(startCoord)-1][1],width=10))

def drawWorkstation(event):
    global createWorkstationStatus,workstationCoord,topcanvas
    if(createWorkstationStatus):
        if(workstationCoord[0] == [None,None]):
            workstationCoord = [[event.x, event.y]]
        else:
            if(abs(workstationCoord[len(workstationCoord)-1][0] - event.x) > abs(workstationCoord[len(workstationCoord)-1][1] - event.y)):
                workstationCoord.append([event.x, workstationCoord[len(workstationCoord)-1][1]])
            else:
                workstationCoord.append([workstationCoord[len(workstationCoord)-1][0], event.y])
            workstationObject.append(topcanvas.create_line(workstationCoord[len(workstationCoord)-2][0],workstationCoord[len(workstationCoord)-2][1],workstationCoord[len(workstationCoord)-1][0],workstationCoord[len(workstationCoord)-1][1],width=10))
            
def testFunction():
    print("Ttest")

def createLineWorkstation():
    global createWorkstationStatus
    createWorkstationStatus = True
    
def stopCreateLine():
    global createWorkstationStatus,workstationCoord,workstationObject
    createWorkstationStatus = False
    topcanvas.delete(workstationObject[-1])
    # print(workstationCoord)
    del workstationCoord[-1]
    del workstationObject[-1]
    
def createWorkArea():
    
    global factoryData,topcanvas, moveableObject
    top = tk.Toplevel(root)

    if(WorkArea.get() == "Receiving Department"):

        coords = moveableObject[1][0].canvas_coords()
        width = moveableObject[1][0].canvas_width()*2
        height = moveableObject[1][0].canvas_height()*2
        topcanvas = tk.Canvas(top, bg='white',width = width*2, height = height*2)
        
        top.title("Receiving Department Building")
        color  =  moveableObject[1][0].getColor()
        topcanvas.create_rectangle(20,20,20+width,20+height,fill = color)
        workstationData = moveableObject[2][0]

        coordsWorkStation = workstationData[0].canvas_coords()
        topcanvas.create_rectangle((abs(coords[0] - coordsWorkStation[0])*2) + 20 ,(abs(coords[1] - coordsWorkStation[1])*2) +20, (abs(coords[0] - coordsWorkStation[0])*2) + 200,(abs(coords[1] - coordsWorkStation[1])*2) + 100,fill = "GREY")
        topcanvas.create_text((abs(coords[0] - coordsWorkStation[0])*2) + 110,(abs(coords[1] - coordsWorkStation[1])*2) + 60, text =  workstationData[0].getName())
       
        #button1 = Button(top, text = "Create Line", command = createLineWorkstation, anchor = W)
        #button1.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
        #button1_window = topcanvas.create_window(width*1.5, 10, anchor=NW, window=button1)
        #button2 = Button(top, text = "Stop", command = stopCreateLine, anchor = W)
        #button2.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
        #button2_window = topcanvas.create_window(width*1.5, 30, anchor=NW, window=button2)
        
    elif(WorkArea.get() == "Frame Fabrication"): 
        coords = factoryData[4][0].canvas_coords()
        # print(coords)
        width = factoryData[4][0].canvas_width()*2
        height = factoryData[4][0].canvas_height()*2
        topcanvas = tk.Canvas(top, bg='white',width = width*2, height = height*2)
        
        top.title("Fram Frabications Building")
        color  =  factoryData[4][0].getColor()
        topcanvas.create_rectangle(20,20,20+width,20+height,fill = color)
        workstationData = factoryData[6][0]

        coordsWorkStation = workstationData[0].canvas_coords()
        topcanvas.create_rectangle((abs(coords[0] - coordsWorkStation[0])*2) + 20 ,(abs(coords[1] - coordsWorkStation[1])*2) +20, (abs(coords[0] - coordsWorkStation[0])*2) + 200,(abs(coords[1] - coordsWorkStation[1])*2) + 100,fill = "GREY")
        topcanvas.create_text((abs(coords[0] - coordsWorkStation[0])*2) + 110,(abs(coords[1] - coordsWorkStation[1])*2) + 60, text =  workstationData[0].getName())
       
        coordsWorkStation = workstationData[1].canvas_coords()
        topcanvas.create_rectangle((abs(coords[0] - coordsWorkStation[0])*2) + 20 ,(abs(coords[1] - coordsWorkStation[1])*2) +20, (abs(coords[0] - coordsWorkStation[0])*2) + 200,(abs(coords[1] - coordsWorkStation[1])*2) + 100,fill = "GREY")
        topcanvas.create_text((abs(coords[0] - coordsWorkStation[0])*2) + 110,(abs(coords[1] - coordsWorkStation[1])*2) + 60, text =  workstationData[1].getName())

        coordsWorkStation = workstationData[2].canvas_coords()
        topcanvas.create_rectangle((abs(coords[0] - coordsWorkStation[0])*2) + 20 ,(abs(coords[1] - coordsWorkStation[1])*2) +20, (abs(coords[0] - coordsWorkStation[0])*2) + 200,(abs(coords[1] - coordsWorkStation[1])*2) + 100,fill = "GREY")
        topcanvas.create_text((abs(coords[0] - coordsWorkStation[0])*2) + 110,(abs(coords[1] - coordsWorkStation[1])*2) + 60, text =  workstationData[2].getName())

        button1 = Button(top, text = "Create Line", command = createLineWorkstation, anchor = W)
        button1.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
        button1_window = topcanvas.create_window(width*1.5, 10, anchor=NW, window=button1)
        button2 = Button(top, text = "Stop", command = stopCreateLine, anchor = W)
        button2.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
        button2_window = topcanvas.create_window(width*1.5, 30, anchor=NW, window=button2)
        
    elif(WorkArea.get() == "Painting Department"):
        coords = moveableObject[1][1].canvas_coords()
        # print(coords)
        width = moveableObject[1][1].canvas_width()*2
        height = moveableObject[1][1].canvas_height()*2
        topcanvas = tk.Canvas(top, bg='white',width = width*2, height = height*2)
        
        top.title("Painting Department Building")
        color  =  moveableObject[1][1].getColor()
        topcanvas.create_rectangle(20,20,20+width,20+height,fill = color)
        workstationData = moveableObject[2][1]

        coordsWorkStation = workstationData[0].canvas_coords()
        topcanvas.create_rectangle((abs(coords[0] - coordsWorkStation[0])*2) + 20 ,(abs(coords[1] - coordsWorkStation[1])*2) +20, (abs(coords[0] - coordsWorkStation[0])*2) + 200,(abs(coords[1] - coordsWorkStation[1])*2) + 100,fill = "GREY")
        topcanvas.create_text((abs(coords[0] - coordsWorkStation[0])*2) + 110,(abs(coords[1] - coordsWorkStation[1])*2) + 60, text =  workstationData[0].getName())
       
        coordsWorkStation = workstationData[1].canvas_coords()
        topcanvas.create_rectangle((abs(coords[0] - coordsWorkStation[0])*2) + 20 ,(abs(coords[1] - coordsWorkStation[1])*2) +20, (abs(coords[0] - coordsWorkStation[0])*2) + 200,(abs(coords[1] - coordsWorkStation[1])*2) + 100,fill = "GREY")
        topcanvas.create_text((abs(coords[0] - coordsWorkStation[0])*2) + 110,(abs(coords[1] - coordsWorkStation[1])*2) + 60, text =  workstationData[1].getName())

        coordsWorkStation = workstationData[2].canvas_coords()
        topcanvas.create_rectangle((abs(coords[0] - coordsWorkStation[0])*2) + 20 ,(abs(coords[1] - coordsWorkStation[1])*2) +20, (abs(coords[0] - coordsWorkStation[0])*2) + 200,(abs(coords[1] - coordsWorkStation[1])*2) + 100,fill = "GREY")
        topcanvas.create_text((abs(coords[0] - coordsWorkStation[0])*2) + 110,(abs(coords[1] - coordsWorkStation[1])*2) + 60, text =  workstationData[2].getName())

        button1 = Button(top, text = "Create Line", command = createLineWorkstation, anchor = W)
        button1.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
        button1_window = topcanvas.create_window(width*1.5, 10, anchor=NW, window=button1)
        button2 = Button(top, text = "Stop", command = stopCreateLine, anchor = W)
        button2.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
        button2_window = topcanvas.create_window(width*1.5, 30, anchor=NW, window=button2)
        
    elif(WorkArea.get() == "Module Assembly"):
        coords = factoryData[4][1].canvas_coords()
        # "Internal Assembly", "External Assembly"
        coords = factoryData[4][1].canvas_coords()
        # print(coords)
        width = factoryData[4][1].canvas_width()*2
        height = factoryData[4][1].canvas_height()*2
        topcanvas = tk.Canvas(top, bg='white',width = width*2, height = height*2)
        
        top.title("Module Assembly Building")
        color  =  factoryData[4][1].getColor()
        topcanvas.create_rectangle(20,20,20+width,20+height,fill = color)
        workstationData = factoryData[6][1]

        coordsWorkStation = workstationData[0].canvas_coords()
        topcanvas.create_rectangle((abs(coords[0] - coordsWorkStation[0])*2) + 20 ,(abs(coords[1] - coordsWorkStation[1])*2) +20, (abs(coords[0] - coordsWorkStation[0])*2) + 200,(abs(coords[1] - coordsWorkStation[1])*2) + 100,fill = "GREY")
        topcanvas.create_text((abs(coords[0] - coordsWorkStation[0])*2) + 110,(abs(coords[1] - coordsWorkStation[1])*2) + 60, text =  workstationData[0].getName())
       
        coordsWorkStation = workstationData[1].canvas_coords()
        topcanvas.create_rectangle((abs(coords[0] - coordsWorkStation[0])*2) + 20 ,(abs(coords[1] - coordsWorkStation[1])*2) +20, (abs(coords[0] - coordsWorkStation[0])*2) + 200,(abs(coords[1] - coordsWorkStation[1])*2) + 100,fill = "GREY")
        topcanvas.create_text((abs(coords[0] - coordsWorkStation[0])*2) + 110,(abs(coords[1] - coordsWorkStation[1])*2) + 60, text =  workstationData[1].getName())

        button1 = Button(top, text = "Create Line", command = createLineWorkstation, anchor = W)
        button1.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
        button1_window = topcanvas.create_window(width*1.5, 10, anchor=NW, window=button1)
        button2 = Button(top, text = "Stop", command = stopCreateLine, anchor = W)
        button2.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
        button2_window = topcanvas.create_window(width*1.5, 30, anchor=NW, window=button2)

    elif(WorkArea.get() == "Machine Assembly"):

        coords = factoryData[4][2].canvas_coords()
        # "Internal Assembly", "External Assembly"
        coords = factoryData[4][2].canvas_coords()
        # print(coords)
        width = factoryData[4][2].canvas_width()*2
        height = factoryData[4][2].canvas_height()*2
        topcanvas = tk.Canvas(top, bg='white',width = width*2, height = height*2)
        
        top.title("Machine Assembly Building")
        color  =  factoryData[4][2].getColor()
        topcanvas.create_rectangle(20,20,20+width,20+height,fill = color)
        workstationData = factoryData[6][2]

        coordsWorkStation = workstationData[0].canvas_coords()
        topcanvas.create_rectangle((abs(coords[0] - coordsWorkStation[0])*2) + 20 ,(abs(coords[1] - coordsWorkStation[1])*2) +20, (abs(coords[0] - coordsWorkStation[0])*2) + 200,(abs(coords[1] - coordsWorkStation[1])*2) + 100,fill = "GREY")
        topcanvas.create_text((abs(coords[0] - coordsWorkStation[0])*2) + 110,(abs(coords[1] - coordsWorkStation[1])*2) + 60, text =  workstationData[0].getName())

        coordsWorkStation = workstationData[1].canvas_coords()
        topcanvas.create_rectangle((abs(coords[0] - coordsWorkStation[0])*2) + 20 ,(abs(coords[1] - coordsWorkStation[1])*2) +20, (abs(coords[0] - coordsWorkStation[0])*2) + 200,(abs(coords[1] - coordsWorkStation[1])*2) + 100,fill = "GREY")
        topcanvas.create_text((abs(coords[0] - coordsWorkStation[0])*2) + 110,(abs(coords[1] - coordsWorkStation[1])*2) + 60, text =  workstationData[1].getName())
        
        coordsWorkStation = workstationData[2].canvas_coords()
        topcanvas.create_rectangle((abs(coords[0] - coordsWorkStation[0])*2) + 20 ,(abs(coords[1] - coordsWorkStation[1])*2) +20, (abs(coords[0] - coordsWorkStation[0])*2) + 200,(abs(coords[1] - coordsWorkStation[1])*2) + 100,fill = "GREY")
        topcanvas.create_text((abs(coords[0] - coordsWorkStation[0])*2) + 110,(abs(coords[1] - coordsWorkStation[1])*2) + 60, text =  workstationData[2].getName())
        
        button1 = Button(top, text = "Create Line", command = createLineWorkstation, anchor = W)
        button1.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
        button1_window = topcanvas.create_window(width*1.5, 10, anchor=NW, window=button1)
        button2 = Button(top, text = "Stop", command = stopCreateLine, anchor = W)
        button2.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
        button2_window = topcanvas.create_window(width*1.5, 30, anchor=NW, window=button2)

    elif(WorkArea.get() == "Quality Control"):
        coords = factoryData[4][3].canvas_coords()
        coords = factoryData[4][3].canvas_coords()
        width = factoryData[4][3].canvas_width()*2
        height = factoryData[4][3].canvas_height()*2
        topcanvas = tk.Canvas(top, bg='white',width = width*2, height = height*2)
        
        top.title("Quality Control Building")
        color  =  factoryData[4][3].getColor()
        topcanvas.create_rectangle(20,20,20+width,20+height,fill = color)
        workstationData = factoryData[6][3]

        coordsWorkStation = workstationData[0].canvas_coords()
        topcanvas.create_rectangle((abs(coords[0] - coordsWorkStation[0])*2) + 20 ,(abs(coords[1] - coordsWorkStation[1])*2) +20, (abs(coords[0] - coordsWorkStation[0])*2) + 200,(abs(coords[1] - coordsWorkStation[1])*2) + 100,fill = "GREY")
        topcanvas.create_text((abs(coords[0] - coordsWorkStation[0])*2) + 110,(abs(coords[1] - coordsWorkStation[1])*2) + 60, text =  workstationData[0].getName())
        
        button1 = Button(top, text = "Create Line", command = createLineWorkstation, anchor = W)
        button1.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
        button1_window = topcanvas.create_window(width*1.5, 10, anchor=NW, window=button1)
        button2 = Button(top, text = "Stop", command = stopCreateLine, anchor = W)
        button2.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
        button2_window = topcanvas.create_window(width*1.5, 30, anchor=NW, window=button2)

    elif(WorkArea.get() == "Create & Package"):
        coords = factoryData[4][4].canvas_coords()
        coords = factoryData[4][4].canvas_coords()
        width = factoryData[4][4].canvas_width()*2
        height = factoryData[4][4].canvas_height()*2
        topcanvas = tk.Canvas(top, bg='white',width = width*2, height = height*2)
        
        top.title("Create & Package Building")
        color  =  factoryData[4][4].getColor()
        topcanvas.create_rectangle(20,20,20+width,20+height,fill = color)
        workstationData = factoryData[6][4]

        coordsWorkStation = workstationData[0].canvas_coords()
        topcanvas.create_rectangle((abs(coords[0] - coordsWorkStation[0])*2) + 20 ,(abs(coords[1] - coordsWorkStation[1])*2) +20, (abs(coords[0] - coordsWorkStation[0])*2) + 200,(abs(coords[1] - coordsWorkStation[1])*2) + 100,fill = "GREY")
        topcanvas.create_text((abs(coords[0] - coordsWorkStation[0])*2) + 110,(abs(coords[1] - coordsWorkStation[1])*2) + 60, text =  workstationData[0].getName())
        
        button1 = Button(top, text = "Create Line", command = createLineWorkstation, anchor = W)
        button1.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
        button1_window = topcanvas.create_window(width*1.5, 10, anchor=NW, window=button1)
        button2 = Button(top, text = "Stop", command = stopCreateLine, anchor = W)
        button2.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
        button2_window = topcanvas.create_window(width*1.5, 30, anchor=NW, window=button2)
    
    elif(WorkArea.get() == "Storage"):
        coords = factoryData[4][5].canvas_coords()
        coords = factoryData[4][5].canvas_coords()
        width = factoryData[4][5].canvas_width()*2
        height = factoryData[4][5].canvas_height()*2
        topcanvas = tk.Canvas(top, bg='white',width = width*2, height = height*2)
        
        top.title("Storage Building")
        color  =  factoryData[4][5].getColor()
        topcanvas.create_rectangle(20,20,20+width,20+height,fill = color)
        workstationData = factoryData[6][5]

        coordsWorkStation = workstationData[0].canvas_coords()
        topcanvas.create_rectangle((abs(coords[0] - coordsWorkStation[0])*2) + 20 ,(abs(coords[1] - coordsWorkStation[1])*2) +20, (abs(coords[0] - coordsWorkStation[0])*2) + 200,(abs(coords[1] - coordsWorkStation[1])*2) + 100,fill = "GREY")
        topcanvas.create_text((abs(coords[0] - coordsWorkStation[0])*2) + 110,(abs(coords[1] - coordsWorkStation[1])*2) + 60, text =  workstationData[0].getName())
        
        button1 = Button(top, text = "Create Line", command = createLineWorkstation, anchor = W)
        button1.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
        button1_window = topcanvas.create_window(width*1.5, 10, anchor=NW, window=button1)
        button2 = Button(top, text = "Stop", command = stopCreateLine, anchor = W)
        button2.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
        button2_window = topcanvas.create_window(width*1.5, 30, anchor=NW, window=button2)
    
    elif(WorkArea.get() == "Loading Dock"):
        coords = moveableObject[1][2].canvas_coords()
        width = moveableObject[1][2].canvas_width()*2
        height = moveableObject[1][2].canvas_height()*2
        topcanvas = tk.Canvas(top, bg='white',width = width*2, height = height*2)
        
        top.title("Receiving Department Building")
        color  =  moveableObject[1][2].getColor()
        topcanvas.create_rectangle(20,20,20+width,20+height,fill = color)
        workstationData = moveableObject[2][2]

        coordsWorkStation = workstationData[0].canvas_coords()
        topcanvas.create_rectangle((abs(coords[0] - coordsWorkStation[0])*2) + 20 ,(abs(coords[1] - coordsWorkStation[1])*2) +20, (abs(coords[0] - coordsWorkStation[0])*2) + 200,(abs(coords[1] - coordsWorkStation[1])*2) + 100,fill = "GREY")
        topcanvas.create_text((abs(coords[0] - coordsWorkStation[0])*2) + 110,(abs(coords[1] - coordsWorkStation[1])*2) + 60, text =  workstationData[0].getName())
       
        button1 = Button(top, text = "Create Line", command = createLineWorkstation, anchor = W)
        button1.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
        button1_window = topcanvas.create_window(width*1.5, 10, anchor=NW, window=button1)
        button2 = Button(top, text = "Stop", command = stopCreateLine, anchor = W)
        button2.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
        button2_window = topcanvas.create_window(width*1.5, 30, anchor=NW, window=button2)
            
    else:
        messagebox.showerror("Error", "Can't place area outside of factory area")
    topcanvas.pack()    


#********************************************Window*******************************************************#
#Main Window Creation
root = tk.Tk() #Instantiate main window


root.title("FIRE - Designing Innovations Application") #adds window title
notebook = ttk.Notebook(root) #instantiates notebook
root.iconbitmap('asset/fire logo icon2.ico')#adds the fire logo to the top left of the frame

#Tab Creation (adding tabs to the main window and giving them a title)
probstab = ttk.Frame(root) #problem statement frame
demotab = ttk.Frame(root) #demographic frame
canvastab = ttk.Frame(root) #canvas frame
notebook.add(probstab, text='Problem Statement\n') #adds the problem statement frame to the notebook with it's title
notebook.add(demotab, text='Demographic Information\n' ) #adds the demographic frame to the notebook with it's title
notebook.add(canvastab, text='Factory Layout\n') #adds the canvas frame to the notebook with it's title
menu = Menu(root)
root.config(menu = menu)
menu.add_command(label = 'Demographic Questions', command = lambda: createHelpwindow(1))
menu.add_command(label = 'Factory Layout Questions', command = lambda: createHelpwindow(2))
menu.add_command(label = 'About the Design Problem', command = lambda: createHelpwindow(3))

#*********************************Problem Statement Tab*****************************************************#
#Title probstaTitle
displayText(probstab, 1, 0, "Factory Layout Problem Statement and Description", 16, 1)
#Overview Header probstaOv
displayText(probstab, 2, 0, "Overview", 12, 1)
#Overview Text probstaOverView
displayText(probstab, 3, 0, "A new factory layout needs to be designed to reduce product travel distance and material handling effort. Each work area within the factory has certain processes that need to be accomplished in order to move to the next area. The path of the machine starts and ends at the loading dock where parts are received and the final product is shipped out. After the processes have been completed at each of the corresponding workstations, the parts are moved to the next area using a forklift. The travel distance of the machine as it moves through the factory is measured by its path between workstations and being transported from one area or department to the next. The path between both workstations and work areas should be considered for maximum productivity.", 12, 1)
#Production Area HeaderprobstaPAHeader
displayText(probstab, 4, 0, "Production Area" , 12, 1)
#Production Area Text probstaTextLabel
displayText(probstab, 5, 0, "The following image describes the major components of a ‘machine’, the processing steps, and the key departments in the facility. Note each completed ‘machine’ requires 1 Machine Frame and 5 Modules. Also keep in mind that this is just a description of the steps needed to make a machine and this is not necessarily what your solution should look like." , 12, 1)
#Add the Factory Area Image
img = ImageTk.PhotoImage(Image.open('asset/Factory Proces.png'))
panel = tk.Label(probstab, image = img)
panel.grid(row = 6, column =  0, columnspan = 2)
#Add the Fire Logo to the GUI
img2 = ImageTk.PhotoImage(Image.open('asset/Fire logo.png'))
panel2 = tk.Label(probstab, image = img2)
panel2.grid(row = 0, column =  0, columnspan = 3)
#******************************************Demographic tab***************************************************#
displayText(demotab, 0, 1, "Demographic Information", 16, 3)
displayText(demotab, 1, 1,"Please answer the following questions before starting the timer and beginning the design problem." ,12 ,3)
displayText(demotab, 2, 0, "What is your age?" , 10 , 1)
answers[0] = displayBox(demotab, 2, 1, 10)
displayText(demotab, 3, 0, "What is your educational background?", 10, 1)
answers[1] = displayDropdown(demotab, 3, 1, 35, ["Student at a public or private university", "Faculty at a public or private university", "Student at a High school"])
displayText(demotab, 4, 0, "What is the highest level of education you have completed?", 10, 1)
answers[2] = displayDropdown(demotab, 4, 1, 25, ["9th Grade", "10th Grade", "11th Grade", "12th Grade", "Graduated High School", "1 Year of College", "2 Years of College", "3 Years of College", "4 Years of College", "Graduated College", "Some Graduate School", "Completed Graduate School"])
displayText(demotab, 5, 0, "What is your desired college major? (If applicable)", 10, 1)
answers[3] = displayBox(demotab, 5, 1, 35)
displayText(demotab, 6, 0, "Have you had any experience with solving design problems?", 10, 1)
answers[4] = displayYesorNo(demotab, 6)
displayText(demotab, 7, 0, "Have you had any experience in designing a factory layout?", 10, 1)
answers[5] = displayYesorNo(demotab, 7)

saveButton = displayButton(demotab, 8,0,3,10,'Save',save)
#************************************************************Canvas Tab**********************************************#
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^Canvas Tab Frame Creation and placement^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
canvasFrame = tkinter.Frame(canvastab, borderwidth=2, relief='ridge')#creates the frame for the canvas
areaFrame = tkinter.Frame(canvastab, borderwidth=2, relief='ridge')#creates the frame for the area settings
utilFrame = tkinter.Frame(canvastab, borderwidth=2, relief='ridge')#creates the frame for the util section
canvasFrame.grid(row=0,column=0, rowspan=10, columnspan=5, sticky='nsew')#adds the Canvas frame to the grid
areaFrame.grid(row=0,column=6, rowspan=8, columnspan=5, sticky='nsew')#adds the area frame to the grid
utilFrame.grid(row=9,column=6, rowspan=2, columnspan=5, sticky='nsew')#adds the util frame to the grid
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^Area Frame Creation^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
#Labels
displayText(areaFrame,0,1,'X',12,1)
displayText(areaFrame,0,2,'Y',12,1)
displayText(areaFrame,2,3,"Size",12,1)
displayText(areaFrame,1,3,"Position",12,1)
displayText(areaFrame,19,0,"*Note: The following work areas are locked in size and position*",10,2)
displayTextBox(areaFrame, 1, 0, "Frame Fabrication", 15 ,"Blue")
displayTextBox(areaFrame, 4, 0, "Module Assembly", 15 ,"Green")
displayTextBox(areaFrame, 7, 0, "Machine Assembly", 15 ,"Cyan")
displayTextBox(areaFrame, 10, 0, "Quality Control", 15 ,"Orange")
displayTextBox(areaFrame, 13, 0, "Packaging", 15 ,"Magenta")
displayTextBox(areaFrame, 16, 0, "Storage", 15 ,"Gold")
displayTextBox(areaFrame, 20, 0, "Recieving", 15 ,"Red")
displayTextBox(areaFrame, 23, 0, "Painting", 15 ,"Yellow")
displayTextBox(areaFrame, 26, 0, "Loading Dock", 15 ,"Light Green")
displayText(areaFrame, 0, 5, "Set the path between Building", 11 ,1)
#Spaces
displayText(areaFrame,3,0,"",0,1)
displayText(areaFrame,6,0,"",0,1)
displayText(areaFrame,9,0,"",0,1)
displayText(areaFrame,12,0,"",0,1)
displayText(areaFrame,15,0,"",0,1)
displayText(areaFrame,18,0,"",0,1)
displayText(areaFrame,22,0,"",0,1)
displayText(areaFrame,25,0,"",0,1)
# Position and size text boxes
# go X Y positionX Postion Y
# Frame fabrication boxes 
factoryData[0][0] = displayBox(areaFrame,1,1,10)
factoryData[1][0] = displayBox(areaFrame,1,2,10)
factoryData[2][0] = displayBox(areaFrame,2,1,10)
factoryData[3][0] = displayBox(areaFrame,2,2,10)

# Module assembly boxes
factoryData[0][1] = displayBox(areaFrame,4,1,10)
factoryData[1][1] = displayBox(areaFrame,4,2,10)
factoryData[2][1] = displayBox(areaFrame,5,1,10)
factoryData[3][1] = displayBox(areaFrame,5,2,10)
# Machine assembly boxes
factoryData[0][2] = displayBox(areaFrame,7,1,10)
factoryData[1][2] = displayBox(areaFrame,7,2,10)
factoryData[2][2] = displayBox(areaFrame,8,1,10)
factoryData[3][2] = displayBox(areaFrame,8,2,10)
#Quality control boxes
factoryData[0][3] = displayBox(areaFrame,10,1,10)
factoryData[1][3] = displayBox(areaFrame,10,2,10)
factoryData[2][3] = displayBox(areaFrame,11,1,10)
factoryData[3][3] = displayBox(areaFrame,11,2,10)
# Packaging dept. boxes
factoryData[0][4] = displayBox(areaFrame,13,1,10)
factoryData[1][4] = displayBox(areaFrame,13,2,10)
factoryData[2][4] = displayBox(areaFrame,14,1,10)
factoryData[3][4] = displayBox(areaFrame,14,2,10)
# Storage department
factoryData[0][5] = displayBox(areaFrame,16,1,10)
factoryData[1][5] = displayBox(areaFrame,16,2,10)
factoryData[2][5] = displayBox(areaFrame,17,1,10)
factoryData[3][5] = displayBox(areaFrame,17,2,10)
# The work areas that don't move have text boxes
# Recieving dept.
displayBoxFreeze(areaFrame, 20, 1, "100", 10, "white" , SUNKEN) 
displayBoxFreeze(areaFrame, 20, 2, "50", 10, "white" , SUNKEN)
displayBoxFreeze(areaFrame, 21, 1, "250", 10, "white" , SUNKEN)
displayBoxFreeze(areaFrame, 21, 2, "325", 10, "white" , SUNKEN) 
#Painting dept.
displayBoxFreeze(areaFrame, 23, 1, "80", 10, "white" , SUNKEN) 
displayBoxFreeze(areaFrame, 23, 2, "100", 10, "white" , SUNKEN)
displayBoxFreeze(areaFrame, 24, 1, "175", 10, "white" , SUNKEN)
displayBoxFreeze(areaFrame, 24, 2, "180", 10, "white" , SUNKEN)
# Loading dock
displayBoxFreeze(areaFrame, 26, 1, "50", 10, "white" , SUNKEN) 
displayBoxFreeze(areaFrame, 26, 2, "325", 10, "white" , SUNKEN)
displayBoxFreeze(areaFrame, 27, 1, "80", 10, "white" , SUNKEN)
displayBoxFreeze(areaFrame, 27, 2, "310", 10, "white" , SUNKEN)

# Work area selection dropdown
workstation1 = displayDropdown(areaFrame,1,5,25,arealist)
#Workstation selection
var = tk.StringVar(areaFrame)
var.set(newList[0])
workstation2 = tk.OptionMenu(areaFrame, var, *newList)
workstation2.grid(row = 2, column = 5, columnspan = 25)


#createLine = displayButton(areaFrame,4,5,1,20,'Create Line between building', createLineobject)
#stopaddline = displayButton(areaFrame,5,5,1,20,'Stop add',stopAdd)
#DeleteLine = displayButton(areaFrame,6,5,1,20,'Delete last line',deleteLineobject)
#WorkArea = displayDropdown(areaFrame,13,5,25,workArea)
#createLine = displayButton(areaFrame,14,5,1,20,'Create line in work area', createWorkArea)
#applyButton = displayButton(areaFrame,16,5,1,20,'Apply',applyCoord)


#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^Canvas Frame Creation^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
canvas = tk.Canvas(canvasFrame, width = 720, height = 720, bg = "white", bd=2, relief='groove')#creates the canvas
# Vertical lines for the grid on the 3rd tab
for i in range(0,36): #range of  lines to create
    x = 20*i #calc the distance of where line should be placed
    canvas.create_text(x,710,text=i*10) #adds text label at each line
    canvas.create_line(x, 700, x, -700, width = 1)#createsthe acutal line
# Horizontal lines for the grid
for i in range(0,36): #range of lines to create
    y = 20*i #calc the distance of where the line should be placed
    if(y != 700 and y != 0):#contitional for label formatting
        canvas.create_text(710,y,text=i*10)#adds text label at each line
    canvas.create_line(0, y, 700, y, width = 1)#creates the line

canvas.pack()
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^Util Frame Creation^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

TimeEntry1=tk.StringVar() #holds the min value
TimeEntry2=tk.StringVar() #holds the secs value

#Widgits
clockUtil1 = ttk.Entry(utilFrame, textvariable = TimeEntry1 ,width=10).grid(row=0,column=0)#shows the mins
clockUtil2 = ttk.Entry(utilFrame, textvariable = TimeEntry2 ,width=10).grid(row=0,column=2)#shows the secs

clockColon = displayText(utilFrame,0,1,':',12,1)
startTimer = displayButton(utilFrame,1,0,1,10,'start',st)
stopTimer = displayButton(utilFrame,1,2,1,10,'stop',stp)
#distanceButton = displayButton(utilFrame,1,3,1,20,"Total Distance", distanceFunction)
#requirementButton = displayButton(utilFrame,1,4,1,20,"Show Requirments", requirementList)


moveableObject[0][0] = canvas.create_text((400)+100,(600)-20, text="Receiving Department")
moveableObject[1][0] = ResizableCanvasFrame(canvas,400/2,600/2,200/2,100/2,"red",moveableObject[0][0],moveableObject[2][0],"Receiving Department",False)

moveableObject[0][1] = canvas.create_text(280+70,260-20, text="Painting Department")
moveableObject[1][1] = ResizableCanvasFrame(canvas,280/2,260/2,140/2,200/2,"yellow",moveableObject[0][1],moveableObject[2][1],"Painting Department",False)

moveableObject[0][2] = canvas.create_text(600+50,540-20, text="Loading Dock")
moveableObject[1][2] = ResizableCanvasFrame(canvas,600/2,540/2,100/2,160/2,"light green",moveableObject[0][2],moveableObject[2][2],"Loading Dock",False)

#***************************End of Program********************************************#
#packs in tabs to frame
notebook.pack(expand = 1, fill = 'both')
def task():
    # global continuingLine
    # print(continuingLine)
    root.after(1000, task)  # reschedule event in 2 seconds

root.after(1000, task)
workstation1.trace("w",updateDropdown)
root.bind('<Double-Button-1>',drawLine)
root.bind('<Return>', applyCoord)
root.bind_all('<Button-1>', drawWorkstation)


#End Loop
root.mainloop()
