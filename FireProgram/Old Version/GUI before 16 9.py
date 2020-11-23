#imports
import tkinter, time
import tkinter.ttk as ttk
import tkinter as tk
import tkinter.font as tkfont
from threading import Thread
from tkinter import messagebox
from tkinter import *
from tkinter import StringVar
from tkinter.font import Font
from PIL import Image, ImageTk
from tkinter import Tk, Frame, PhotoImage, Label

#global variable
answers = ["", "","","","","",""]
factoryData = [[0,0,0,0,0,0] ,[0,0,0,0,0,0],[0,0,0,0,0,0] ,[0,0,0,0,0,0]]
helpIndex = 0

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

def createHelpwindow():
    global helpIndex 
    helpIndex += 1
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
    else:
        messagebox.showerror("something went wrong")
    label.config(font = ("Times New Roman", 10))
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

def displayYesorNo(xframe, Xrow):
    optionsVar = StringVar(demotab)
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

def requirementList():
    root = tkinter.Tk()
    #Title
    root.title("Requirement Check List")
    root.iconbitmap("asset/fire logo icon2.ico")
    tkinter.Label(root, text="Requirements List:", borderwidth=1, justify=RIGHT, font=('Times', '18', 'bold')).grid(row=0, column=0)
    tkinter.Label(root, text="✔", borderwidth=1, justify=CENTER, font=('Times', '18', 'bold') ).grid(row=0,column=1)
    #Receiving Room Req
    tkinter.Label(root, text="Receiving Room:    ", borderwidth=1, justify=LEFT,font =('Times', '18') ).grid(row=2,column=0)
    tkinter.Label(root, text="                       ", borderwidth=1, justify=CENTER ).grid(row=2,column=1)
    tkinter.Label(root, text= "Along Grid Border", borderwidth=1, justify=CENTER ).grid(row=3,column=0)
    tkinter.Label(root, text="                       ", borderwidth=1, justify=CENTER ).grid(row=3,column=1)
    tkinter.Label(root, text="At Least 300 Square Feet", borderwidth=1, justify=CENTER ).grid(row=4,column=0)
    tkinter.Label(root, text="                       ", borderwidth=1, justify=CENTER ).grid(row=4,column=1)
    #Module Assemble
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
    MyButton = tkinter.Button(root, text='Update Checklist', command=update)
    MyButton.grid(row=25, column=0)

def update():
    tkinter.Label(root, text="✔", borderwidth=1, justify=CENTER).grid(row=2, column=1)

def save(): #function to save all of the demo info to the activity log text file
    global answers
    with open('Data/info.txt', 'a') as the_file:
        the_file.write(answers[0].get()+ " " + answers[1].get()+ " " + answers[2].get()+ " "+ answers[3].get()+ " "+ answers[4].get()+ " "+ answers[5].get())    

#error pop-up window for out of bounds message
def errorWindow():
    messagebox.showerror("Error", "Can't place area outside of factory area")
#error pop-up window for area size message
def error1Window():
    messagebox.showerror("Error2", "Area does not fit requirements")

#********************************************Window*******************************************************#
#Main Window Creation

root = tk.Tk() #Instantiate main window
root.title("FIRE - Designing Innovations Application") #adds window title
notebook = ttk.Notebook(root) #instantiates notebook
root.iconbitmap("asset/fire logo icon2.ico")#adds the fire logo to the top left of the frame

#Tab Creation (adding tabs to the main window and giving them a title)
probstab = ttk.Frame(root) #problem statement frame
demotab = ttk.Frame(root) #demographic frame
canvastab = ttk.Frame(root) #canvas frame
notebook.add(probstab, text='Problem Statement\n') #adds the problem statement frame to the notebook with it's title
notebook.add(demotab, text='Demographic Information\n' ) #adds the demographic frame to the notebook with it's title
notebook.add(canvastab, text='Factory Layout\n') #adds the canvas frame to the notebook with it's title
menu = Menu(root)
root.config(menu = menu)
menu.add_command(label = 'Demographic Questions', command = createHelpwindow)
menu.add_command(label = 'Factory Layout Questions', command = createHelpwindow)
menu.add_command(label = 'About the Design Problem', command = createHelpwindow)

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
img = ImageTk.PhotoImage(Image.open("asset/Factory Process.png"))
panel = tk.Label(probstab, image = img)
panel.grid(row = 6, column =  0, columnspan = 2)
#Add the Fire Logo to the GUI
img2 = ImageTk.PhotoImage(Image.open("asset/fire logo.png"))
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

saveButton = tk.Button(demotab, text = 'Save', command=save)
saveButton.grid(row = 8, column = 0, columnspan = 3)
saveButton.config(width = 10)
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
displayText(areaFrame,2,3,"Position",12,1)
displayText(areaFrame,1,3,"Size",12,1)
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
displayText(areaFrame, 0, 5, "Select work area to make changes", 11 ,1)
displayText(areaFrame, 3, 5, "Select object to make changes", 11 ,1)
displayText(areaFrame, 8, 5, "Switch from placing to removing",11, 1)

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
factoryData[2][2] = displayBox(areaFrame,8,2,10)
#Quality control boxes
factoryData[0][3] = displayBox(areaFrame,10,1,10)
factoryData[1][3] = displayBox(areaFrame,10,2,10)
factoryData[2][3] = displayBox(areaFrame,11,1,10)
factoryData[2][3] = displayBox(areaFrame,11,2,10)
# Packaging dept. boxes
factoryData[0][4] = displayBox(areaFrame,13,1,10)
factoryData[1][4] = displayBox(areaFrame,13,2,10)
factoryData[2][4] = displayBox(areaFrame,14,1,10)
factoryData[2][4] = displayBox(areaFrame,14,2,10)
# Storage department
factoryData[0][5] = displayBox(areaFrame,16,1,10)
factoryData[1][5] = displayBox(areaFrame,16,2,10)
factoryData[2][5] = displayBox(areaFrame,17,1,10)
factoryData[2][5] = displayBox(areaFrame,17,2,10)
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
workAreaMenu = displayDropdown(areaFrame,1,5,18,["Recieving", "Frame Fabrication", "Painting", "Module Asembly", "Machine Assembly", "Quality Control", "Packaging", "Storage"])
#Workstation selection
workStation = displayDropdown(areaFrame,2,5,18,["Recieve Raw Materials","Sort Raw Materials", "Make Module Frame Cuts", "Make Machine Frame Cuts", "Frame Tack-Welding","Painting Preparation", "Painting", "Frame Drying","Internal Assembly", "External Assembly","Machine Wiring", "Welding Components Together", "Installing the Casing","Conduct Quality Tests","Packaging the Machines","Storing the Packaged Machines"])
#Area station line
objectsVar = StringVar(areaFrame)
areaStationLine = [('Work Area', 'Work Area'), ('Work Station', 'Work Station'), ('Machine Path', 'Machine Path')]
objectsVar.set('Work Area')
count = 4
for text, mode in areaStationLine:
    areaStationLineRB = Radiobutton(areaFrame, variable=objectsVar, value=mode, text=text)
    areaStationLineRB.grid(row=count, column=5)
    areaStationLineRB.config(font=("Times New Roman", 10))
    count += 1
#Placing or removing
actionsVar = StringVar(areaFrame)
placeRemove = [('Placing Path', 'Placing Objects'), ('Removing Path', 'Removin Objects'),('Show Path Distance', 'Show Path Distance')]
actionsVar.set('Placing Objects')
count = 9
for text, mode in placeRemove:
    placeRemoveRB = Radiobutton(areaFrame, variable=actionsVar, value=mode, text=text)
    placeRemoveRB.grid(row=count, column=5)
    placeRemoveRB.config(font=("Times New Roman", 10))
    count += 1

requirementButton = tk.Button(areaFrame, text = 'Show requirment', command=requirementList)
requirementButton.grid(row = 20, column = 5)
requirementButton.config(width = 15)
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^Canvas Frame Creation^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
canvas = tk.Canvas(canvasFrame, width = 720, height = 720, bg = "white", bd=2, relief='groove')#creates the canvas
# Vertical lines for the grid on the 3rd tab
xcounter = 0
for i in range(0,36): #range of lines to create
    x = 20*i #calc the distance of where line should be placed
    canvas.create_text(x,710,text=xcounter) #adds text label at each line
    canvas.create_line(x, 700, x, -700, width = 1)#createsthe acutal line
    xcounter += 10
# Horizontal lines for the grid
ycounter = 0
for i in range(0,36): #range of lines to create
    y = 20*i #calc the distance of where the line should be placed
    if(y != 700 and y != 0):#contitional for label formatting
        canvas.create_text(710,y,text=ycounter)#adds text label at each line
    canvas.create_line(0, y, 700, y, width = 1)#creates the line
    ycounter += 10
canvas.pack()#packs canvas into the canvas frame
#Department Areas
#Receiving Dept
receivingDept = canvas.create_rectangle(400,600,600,700, fill="red")#the receiving department will be permanantly located
receiveRawMaterialsWKS = canvas.create_rectangle(440,640,530,680, fill="grey")
recLabel = canvas.create_text((500,620), text="Receiving Department")
recWksLabel = canvas.create_text((485,660), text="Receive Raw Materials", width = 55)
#Loading Dock
loadingDock = canvas.create_rectangle(600,540,700,700,fill = "light green")#the loading dock will be permanantly located
loadingLabel = canvas.create_text((650,560), text="Loading Dock")
#Painting Dept
paintDept = canvas.create_rectangle(280,260,420,460,fill="yellow")#the paint department will be permantly located
paintPrepWKS = canvas.create_rectangle(280,260,370,300, fill="grey") #45x20ft
paintingWKS = canvas.create_rectangle(280,260,370,300, fill="grey")
dryingWKS = canvas.create_rectangle(280,260,370,300, fill="grey")
paintLabel = canvas.create_text((340,280), text="Painting Department")
paintPrepWksLabel = canvas.create_text((0,0), text="Painting Preparation", width = 65)
paintingWksLabel = canvas.create_text((0,0), text="Painting", width = 55)
dryingWksLabel = canvas.create_text((0,0), text="Frame Drying", width = 55)
#Module Assembly
moduleAssemblyDept = canvas.create_rectangle(0,0,10,10, fill="green")
internalAssemblyWKS = canvas.create_rectangle(0,0,10,10, fill="grey")
externalAssemblyWKS = canvas.create_rectangle(0,0,10,10, fill="grey")
modLabel = canvas.create_text((0,0), text="Module Assembly Department")
internalAssemWksLabel = canvas.create_text((0,0), text="Internal Assembly", width = 55)
externalAssemWksLabel = canvas.create_text((0,0), text="External Assembly", width = 55)
#Machine Assembly
machineAssemblyDept = canvas.create_rectangle(0,0,10,10, fill="cyan")
wiringWKS = canvas.create_rectangle(0,0,10,10, fill="grey")
weldingWKS = canvas.create_rectangle(0,0,10,10, fill="grey")
installCasingWKS = canvas.create_rectangle(0,0,10,10, fill="grey")
machLabel = canvas.create_text((0,0), text="Machine Assembly Department")
wiringWksLabel = canvas.create_text((0,0), text="Machine Wiring", width = 55)
weldingWksLabel = canvas.create_text((0,0), text="Welding Components Together", width = 100)
installCasingWksLabel = canvas.create_text((0,0), text="Installing the Casing", width = 55)
#Frame Fabrication Dept
frameFabricationDept = canvas.create_rectangle(0,0,10,10, fill="blue")
sortRawMaterialsWKS = canvas.create_rectangle(0,0,10,10, fill="grey")
makeModuleCutsWKS = canvas.create_rectangle(0,0,10,10, fill="grey")
makeMachineCutsWKS = canvas.create_rectangle(0,0,10,10, fill="grey")
frameTackWeldingWKS = canvas.create_rectangle(0,0,10,10, fill="grey")
FFLabel = canvas.create_text((0,0), text="Frame Fabrication Department")
sortRawMaterialsWksLabel = canvas.create_text((0,0), text="Sort Raw Materials", width = 55)
makeModuleCutsWksLabel = canvas.create_text((0,0), text="Make Module Cuts", width = 55)
makeMachineCutsWksLabel = canvas.create_text((0,0), text="Make Machine Frame Cuts", width = 100)
frameTackWeldingWksLabel = canvas.create_text((0,0), text="Frame Tack-Welding", width = 55)
#Quality Control Dept
qualityControlDept = canvas.create_rectangle(0,0,10,10, fill="orange")
conductQualityTestingWKS = canvas.create_rectangle(0,0,10,10, fill="grey")
qcLabel = canvas.create_text((0,0), text="Quality Control Department")
conductQualityTestingWksLabel = canvas.create_text((0,0), text="Conduct Quality Tests", width = 55)
#Crate & Packgage Dept
crateAndPackageDept = canvas.create_rectangle(0,0,10,10, fill="magenta")
packagingWKS = canvas.create_rectangle(0,0,10,10, fill="grey")
cpLabel = canvas.create_text((0,0), text="Crate & Packaging Department")
packagingWksLabel = canvas.create_text((0,0), text="Packaging the Machines", width = 55)
#Storage Dept
storageDept = canvas.create_rectangle(0,0,10,10, fill="gold")
storageWKS = canvas.create_rectangle(0,0,10,10, fill="grey")
stLabel = canvas.create_text((0,0), text="Storage")
storageWksLabel = canvas.create_text((0,0), text="Storing the Packaged Machines", width = 100)
canvas.pack()

#Function to find center of a given rectangle area
def findCenter(area):
    x1,y1,x2,y2 = canvas.coords(area)
    xcenter = (int(x1) + int(x2))/2
    ycenter =  (int(y1) + int(y2))/2
    coordArr = [xcenter,ycenter]
    return coordArr
#get dimension
def factor(rectangle):
    a = float(rectangle.get())
    w = int(a)
    return w

#This function places the areas along with their labels and workstations
def placeArea(event):
    pointerx = event.x
    pointery = event.y
    if(str(workAreaMenu.get()) == "Recieving"):#Does not actually get placed
        print("x")
    elif(str(workAreaMenu.get()) == "Frame Fabrication"):
        if((int(pointerx - factor(factoryData[0][0]))<0) or (int(pointery - factor(factoryData[1][0])) < 0) or (int(pointerx + factor(factoryData[0][0])) >700) or (int(pointery + factor(factoryData[1][0])) > 700)):
            errorWindow()
        elif((int(factoryData[0][0].get())*int(factoryData[1][0].get())) < 8000 or (int(factoryData[0][0].get())*int(factoryData[1][0].get())) > 16900):
            error1Window()
        else:
            factoryData[2][0].delete(0,END)
            factoryData[2][0].insert(0,str(round(pointerx / 2)))
            factoryData[3][0].delete(0,END)
            factoryData[3][0].insert(0, str(round(pointery / 2)))
            canvas.coords(frameFabricationDept, int(pointerx - factor(factoryData[0][0])), int(pointery - factor(factoryData[1][0])),int(pointerx + factor(factoryData[0][0])), int(pointery + factor(factoryData[1][0])))
            canvas.coords(sortRawMaterialsWKS,int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20))
            canvas.coords(makeModuleCutsWKS,int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20))
            canvas.coords(makeMachineCutsWKS,int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20)) 
            canvas.coords(frameTackWeldingWKS,int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20))
            canvas.coords(FFLabel,int(pointerx), int(pointery + factor(factoryData[1][1]) - 10)) 
            canvas.coords(sortRawMaterialsWksLabel,0,0)
            canvas.coords(makeModuleCutsWksLabel,0,0)
            canvas.coords(makeMachineCutsWksLabel,0,0)
            canvas.coords(frameTackWeldingWksLabel,0,0)
            with open('Data/activity log.txt', 'a') as the_file:
                the_file.write(TimeEntry1.get() + ":" + TimeEntry2.get() + " ")
                the_file.write("Frame Fabrication " + "Size Set to: " + str(factor(factoryData[0][0])*factor(factoryData[1][0])) + " Coordinates: " + "(" + str(pointerx/2) + "," + str(pointery/2) + ")" + "\n")
    elif(str(workAreaMenu.get()) == "Painting"):#Does not actually get placed
         print("x")
    elif(str(workAreaMenu.get()) == "Module Asembly"):#
        if((int(pointerx - factor(factoryData[0][1]))<0) or (int(pointery - factor(factoryData[1][1])) < 0) or (int(pointerx + factor(factoryData[0][1])) >700) or (int(pointery + factor(factoryData[1][1])) > 700)):
            errorWindow()
        elif((int(factoryData[0][1].get())*int(factoryData[1][1].get())) < 6000 or (int(factoryData[0][1].get())*int(factoryData[1][1].get())) > 16900):
            error1Window()
        else:
            factoryData[2][1].delete(0,END)
            factoryData[2][1].insert(0,str(round(pointerx / 2)))
            factoryData[3][1].delete(0,END)
            factoryData[3][1].insert(0, str(round(pointery / 2)))
            canvas.coords(moduleAssemblyDept, int(pointerx - factor(factoryData[0][1])), int(pointery - factor(factoryData[1][1])),int(pointerx + factor(factoryData[0][1])), int(pointery + factor(factoryData[1][1])))
            canvas.coords(internalAssemblyWKS, int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20)) 
            canvas.coords(externalAssemblyWKS, int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20))
            canvas.coords(modLabel, int(pointerx), int(pointery + factor(factoryData[1][1]) - 10))
            canvas.coords(internalAssemWksLabel,0,0)
            canvas.coords(externalAssemWksLabel,0,0)
            with open('Data/activity log.txt', 'a') as the_file:
                the_file.write(TimeEntry1.get() + ":" + TimeEntry2.get() + " ")
                the_file.write("Module Assembly " + "Size Set to: " + str(factor(factoryData[0][1])*factor(factoryData[1][1])) + " Coordinates: " + "(" + str(pointerx/2) + "," + str(pointery/2) + ")" + "\n")
    elif(str(workAreaMenu.get()) == "Machine Assembly"):#
        if((int(pointerx - factor(factoryData[0][2]))<0) or (int(pointery - factor(factoryData[1][2])) < 0) or (int(pointerx + factor(factoryData[0][2])) >700) or (int(pointery + factor(factoryData[1][2])) > 700)):
            errorWindow()
        elif((int(factoryData[0][2].get())*int(factoryData[1][2].get())) < 7000 or (int(factoryData[0][2].get())*int(factoryData[1][2].get())) > 16900):
            error1Window()
        else:
            factoryData[2][2].delete(0,END)
            factoryData[2][2].insert(0,str(round(pointerx / 2)))
            factoryData[3][2].delete(0,END)
            factoryData[3][2].insert(0, str(round(pointery / 2)))
            canvas.coords(machineAssemblyDept, int(pointerx - factor(factoryData[0][2])), int(pointery - factor(factoryData[1][2])),int(pointerx + factor(factoryData[0][2])), int(pointery + factor(factoryData[1][2])))
            canvas.coords(wiringWKS, int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20))
            canvas.coords(weldingWKS, int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20)) 
            canvas.coords(installCasingWKS, int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20))
            canvas.coords(machLabel, int(pointerx), int(pointery + factor(factoryData[1][1]) - 10))
            canvas.coords(wiringWksLabel,0,0)
            canvas.coords(weldingWksLabel,0,0)
            canvas.coords(installCasingWksLabel,0,0)
            with open('Data/activity log.txt', 'a') as the_file:
                the_file.write(TimeEntry1.get() + ":" + TimeEntry2.get() + " ")
                the_file.write("Machine Assembly " + "Size Set to: " + str(factor(factoryData[0][2])*factor(factoryData[1][2])) + " Coordinates: " + "(" + str(pointerx/2) + "," + str(pointery/2) + ")" + "\n")
    elif(str(workAreaMenu.get()) == "Quality Control"):
        if((int(pointerx - factor(factoryData[0][3]))<0) or (int(pointery - factor(factoryData[1][3])) < 0) or (int(pointerx + factor(factoryData[0][3])) >700) or (int(pointery + factor(factoryData[1][3])) > 700)):
            errorWindow()
        elif((int(factoryData[0][3].get())*int(factoryData[1][3].get())) < 5000 or (int(factoryData[0][3].get())*int(factoryData[1][3].get())) > 16900):
            error1Window()
        else:
            factoryData[2][3].delete(0,END)
            factoryData[2][3].insert(0,str(round(pointerx / 2)))
            factoryData[3][3].delete(0,END)
            factoryData[3][3].insert(0, str(round(pointery / 2)))
            canvas.coords(qualityControlDept, int(pointerx - factor(factoryData[0][3])), int(pointery - factor(factoryData[1][3])),int(pointerx + factor(factoryData[0][3])), int(pointery + factor(factoryData[1][3])))
            canvas.coords(conductQualityTestingWKS, int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20))
            canvas.coords(qcLabel, int(pointerx), int(pointery + factor(factoryData[1][1]) - 10))
            canvas.coords(conductQualityTestingWksLabel,0,0)
            with open('Data/activity log.txt', 'a') as the_file:
                the_file.write(TimeEntry1.get() + ":" + TimeEntry2.get() + " ")
                the_file.write("Quality Control " + "Size Set to: " + str(factor(factoryData[0][3])*factor(factoryData[1][3])) + " Coordinates: " + "(" + str(pointerx/2) + "," + str(pointery/2) + ")" + "\n")
    elif(str(workAreaMenu.get()) == "Packaging"):
        if((int(pointerx - factor(factoryData[0][4]))<0) or (int(pointery - factor(factoryData[1][4])) < 0) or (int(pointerx + factor(factoryData[0][4])) >700) or (int(pointery + factor(factoryData[1][4])) > 700)):
            errorWindow()
        elif((int(factoryData[0][4].get())*int(factoryData[1][4].get())) < 5000 or (int(factoryData[0][4].get())*int(factoryData[1][4].get())) > 16900):
            error1Window()
        else:
            factoryData[2][4].delete(0,END)
            factoryData[2][4].insert(0,str(round(pointerx / 2)))
            factoryData[3][4].delete(0,END)
            factoryData[3][4].insert(0, str(round(pointery / 2)))
            canvas.coords(crateAndPackageDept, int(pointerx - factor(factoryData[0][4])), int(pointery - factor(factoryData[1][4])),int(pointerx + factor(factoryData[0][4])), int(pointery + factor(factoryData[1][4])))
            canvas.coords(packagingWKS, int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20))
            canvas.coords(cpLabel, int(pointerx), int(pointery + factor(factoryData[1][1]) - 10))
            canvas.coords(packagingWksLabel,0,0)
            with open('Data/activity log.txt', 'a') as the_file:
                the_file.write(TimeEntry1.get() + ":" + TimeEntry2.get() + " ")
                the_file.write("Packaging " + "Size Set to: " + str(factor(factoryData[0][4])*factor(factoryData[1][4])) + " Coordinates: " + "(" + str(pointerx/2) + "," + str(pointery/2) + ")" + "\n")
    elif(str(workAreaMenu.get()) == "Storage"):
        if((int(pointerx - factor(factoryData[0][5]))<0) or (int(pointery - factor(factoryData[1][5])) < 0) or (int(pointerx + factor(factoryData[0][5])) >700) or (int(pointery + factor(factoryData[1][5])) > 700)):
            errorWindow()
        elif((int(factoryData[0][5].get())*int(factoryData[1][5].get())) < 5000 or (int(factoryData[0][5].get())*int(factoryData[1][5].get())) > 16900):
            error1Window()
        else:
            factoryData[2][5].delete(0,END)
            factoryData[2][5].insert(0,str(round(pointerx / 2)))
            factoryData[3][5].delete(0,END)
            factoryData[3][5].insert(0, str(round(pointery / 2)))
            canvas.coords(storageDept, int(pointerx - factor(factoryData[0][5])), int(pointery - factor(factoryData[1][5])),int(pointerx + factor(factoryData[0][5])), int(pointery + factor(factoryData[1][5])))
            canvas.coords(storageWKS, int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20))
            canvas.coords(stLabel, int(pointerx), int(pointery + factor(factoryData[1][1]) - 10))
            canvas.coords(storageWksLabel,0,0)
            with open('Data/activity log.txt', 'a') as the_file:
                the_file.write(TimeEntry1.get() + ":" + TimeEntry2.get() + " ")
                the_file.write("Storage " + "Size Set to: " + str(factor(factoryData[0][5])*factor(factoryData[1][5])) + " Coordinates: " + "(" + str(pointerx/2) + "," + str(pointery/2) + ")" + "\n")
    elif(str(workAreaMenu.get()) == "Loading Dock"):#Does not actually get placed
         print("x")
#Placing Workstation
def placeWorkStation(event):
    pointerx = event.x
    pointery = event.y
    if((str(workAreaMenu.get()) == "Recieving") and (str(workStationMenu.get()) == "Recieve Raw Materials") ):
        x1,y1,x2,y2 = canvas.coords(receivingDept)
        if(((int(pointerx) - 45) < int(x1) ) or ((int(pointery) - 20) < int(y1)) or ((int(pointerx) + 45) > int(x2) or ((int(pointery) + 20) > int(y2)))):
            errorWindow()
        else:
            canvas.coords(receiveRawMaterialsWKS,int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20))
            canvas.coords(recWksLabel,pointerx,pointery)
            with open('Data/activity log.txt', 'a') as the_file:
                the_file.write(TimeEntry1.get() + ":" + TimeEntry2.get() + " ")
                the_file.write("Recieve Raw Materials " + " Coordinates: " + "(" + str(pointerx/2) + "," + str(pointery/2) + ")" + "\n")
    elif(str(workAreaMenu.get()) == "Frame Fabrication" and (str(workStationMenu.get()) == "Sort Raw Materials")):
        x1,y1,x2,y2 = canvas.coords(frameFabricationDept)
        if(((int(pointerx) - 45) < int(x1) ) or ((int(pointery) - 20) < int(y1)) or ((int(pointerx) + 45) > int(x2) or ((int(pointery) + 20) > int(y2)))):
            errorWindow()
        else:
            canvas.coords(sortRawMaterialsWKS,int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20))
            canvas.coords(sortRawMaterialsWksLabel,pointerx,pointery)
            with open('Data/activity log.txt', 'a') as the_file:
                the_file.write(TimeEntry1.get() + ":" + TimeEntry2.get() + " ")
                the_file.write("Sort Raw Materials " + " Coordinates: " + "(" + str(pointerx/2) + "," + str(pointery/2) + ")" + "\n")
    elif(str(workAreaMenu.get()) == "Frame Fabrication" and (str(workStationMenu.get()) == "Make Module Frame Cuts")):
        x1,y1,x2,y2 = canvas.coords(frameFabricationDept)
        if(((int(pointerx) - 45) < int(x1) ) or ((int(pointery) - 20) < int(y1)) or ((int(pointerx) + 45) > int(x2) or ((int(pointery) + 20) > int(y2)))):
            errorWindow()
        else:
            canvas.coords(makeModuleCutsWKS,int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20))
            canvas.coords(makeModuleCutsWksLabel,pointerx,pointery)
            with open('Data/activity log.txt', 'a') as the_file:
                the_file.write(TimeEntry1.get() + ":" + TimeEntry2.get() + " ")
                the_file.write("Make Module Frame Cuts " + " Coordinates: " + "(" + str(pointerx/2) + "," + str(pointery/2) + ")" + "\n")
    elif(str(workAreaMenu.get()) == "Frame Fabrication" and (str(workStationMenu.get()) == "Make Machine Frame Cuts")):
        x1,y1,x2,y2 = canvas.coords(frameFabricationDept)
        if(((int(pointerx) - 45) < int(x1) ) or ((int(pointery) - 20) < int(y1)) or ((int(pointerx) + 45) > int(x2) or ((int(pointery) + 20) > int(y2)))):
            errorWindow()
        else:
            canvas.coords(makeMachineCutsWKS,int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20))
            canvas.coords(makeMachineCutsWksLabel,pointerx,pointery)
            with open('Data/activity log.txt', 'a') as the_file:
                the_file.write(TimeEntry1.get() + ":" + TimeEntry2.get() + " ")
                the_file.write("Make Machine Frame Cuts " + " Coordinates: " + "(" + str(pointerx/2) + "," + str(pointery/2) + ")" + "\n")
    elif(str(workAreaMenu.get()) == "Frame Fabrication" and (str(workStationMenu.get()) == "Frame Tack-Welding")):
        x1,y1,x2,y2 = canvas.coords(frameFabricationDept)
        if(((int(pointerx) - 45) < int(x1) ) or ((int(pointery) - 20) < int(y1)) or ((int(pointerx) + 45) > int(x2) or ((int(pointery) + 20) > int(y2)))):
            errorWindow()
        else:
            canvas.coords(frameTackWeldingWKS,int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20))
            canvas.coords(frameTackWeldingWksLabel,pointerx,pointery)
            with open('Data/activity log.txt', 'a') as the_file:
                the_file.write(TimeEntry1.get() + ":" + TimeEntry2.get() + " ")
                the_file.write("Frame Tack-Welding " + " Coordinates: " + "(" + str(pointerx/2) + "," + str(pointery/2) + ")" + "\n")
    elif(str(workAreaMenu.get()) == "Painting" and (str(workStationMenu.get()) == "Painting Preparation")):
        x1,y1,x2,y2 = canvas.coords(paintDept)
        if(((int(pointerx) - 45) < int(x1) ) or ((int(pointery) - 20) < int(y1)) or ((int(pointerx) + 45) > int(x2) or ((int(pointery) + 20) > int(y2)))):
            errorWindow()
        else:
            canvas.coords(paintPrepWKS,int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20))
            canvas.coords(paintPrepWksLabel,pointerx,pointery)
            with open('Data/activity log.txt', 'a') as the_file:
                the_file.write(TimeEntry1.get() + ":" + TimeEntry2.get() + " ")
                the_file.write("Painting Preparation " + " Coordinates: " + "(" + str(pointerx/2) + "," + str(pointery/2) + ")" + "\n")
    elif(str(workAreaMenu.get()) == "Painting" and (str(workStationMenu.get()) == "Painting")):
        x1,y1,x2,y2 = canvas.coords(paintDept)
        if(((int(pointerx) - 45) < int(x1) ) or ((int(pointery) - 20) < int(y1)) or ((int(pointerx) + 45) > int(x2) or ((int(pointery) + 20) > int(y2)))):
            errorWindow()
        else:
            canvas.coords(paintingWKS,int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20))
            canvas.coords(paintingWksLabel,pointerx,pointery)
            with open('Data/activity log.txt', 'a') as the_file:
                the_file.write(TimeEntry1.get() + ":" + TimeEntry2.get() + " ")
                the_file.write("Painting " + " Coordinates: " + "(" + str(pointerx/2) + "," + str(pointery/2) + ")" + "\n")
    elif(str(workAreaMenu.get()) == "Painting" and (str(workStationMenu.get()) == "Frame Drying")):
        x1,y1,x2,y2 = canvas.coords(paintDept)
        if(((int(pointerx) - 45) < int(x1) ) or ((int(pointery) - 20) < int(y1)) or ((int(pointerx) + 45) > int(x2) or ((int(pointery) + 20) > int(y2)))):
            errorWindow()
        else:
            canvas.coords(dryingWKS,int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20))
            canvas.coords(dryingWksLabel,pointerx,pointery)
            with open('Data/activity log.txt', 'a') as the_file:
                the_file.write(TimeEntry1.get() + ":" + TimeEntry2.get() + " ")
                the_file.write("Frame Drying " + " Coordinates: " + "(" + str(pointerx/2) + "," + str(pointery/2) + ")" + "\n")
    elif(str(workAreaMenu.get()) == "Module Asembly" and (str(workStationMenu.get()) == "Internal Assembly")):#
        x1,y1,x2,y2 = canvas.coords(moduleAssemblyDept)
        if(((int(pointerx) - 45) < int(x1) ) or ((int(pointery) - 20) < int(y1)) or ((int(pointerx) + 45) > int(x2) or ((int(pointery) + 20) > int(y2)))):
            errorWindow()
        else:
            canvas.coords(internalAssemblyWKS,int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20))
            canvas.coords(internalAssemWksLabel,pointerx,pointery)
            with open('Data/activity log.txt', 'a') as the_file:
                the_file.write(TimeEntry1.get() + ":" + TimeEntry2.get() + " ")
                the_file.write("Internal Assembly " + " Coordinates: " + "(" + str(pointerx/2) + "," + str(pointery/2) + ")" + "\n")
    elif(str(workAreaMenu.get()) == "Module Asembly" and (str(workStationMenu.get()) == "External Assembly")):#
        x1,y1,x2,y2 = canvas.coords(moduleAssemblyDept)
        if(((int(pointerx) - 45) < int(x1) ) or ((int(pointery) - 20) < int(y1)) or ((int(pointerx) + 45) > int(x2) or ((int(pointery) + 20) > int(y2)))):
            errorWindow()
        else:
            canvas.coords(externalAssemblyWKS,int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20))
            canvas.coords(externalAssemWksLabel,pointerx,pointery)
            with open('Data/activity log.txt', 'a') as the_file:
                the_file.write(TimeEntry1.get() + ":" + TimeEntry2.get() + " ")
                the_file.write("External Assembly " + " Coordinates: " + "(" + str(pointerx/2) + "," + str(pointery/2) + ")" + "\n")
    elif(str(workAreaMenu.get()) == "Machine Assembly" and (str(workStationMenu.get()) == "Machine Wiring")):#
        x1,y1,x2,y2 = canvas.coords(machineAssemblyDept)
        if(((int(pointerx) - 45) < int(x1) ) or ((int(pointery) - 20) < int(y1)) or ((int(pointerx) + 45) > int(x2) or ((int(pointery) + 20) > int(y2)))):
            errorWindow()
        else:
            canvas.coords(wiringWKS,int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20))
            canvas.coords(wiringWksLabel,pointerx,pointery)
            with open('Data/activity log.txt', 'a') as the_file:
                the_file.write(TimeEntry1.get() + ":" + TimeEntry2.get() + " ")
                the_file.write("Machine Wiring " + " Coordinates: " + "(" + str(pointerx/2) + "," + str(pointery/2) + ")" + "\n")
    elif(str(workAreaMenu.get()) == "Machine Assembly" and (str(workStationMenu.get()) == "Welding Components Together")):#
        x1,y1,x2,y2 = canvas.coords(machineAssemblyDept)
        if(((int(pointerx) - 45) < int(x1) ) or ((int(pointery) - 20) < int(y1)) or ((int(pointerx) + 45) > int(x2) or ((int(pointery) + 20) > int(y2)))):
            errorWindow()
        else:
            canvas.coords(weldingWKS,int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20))
            canvas.coords(weldingWksLabel,pointerx,pointery)
            with open('Data/activity log.txt', 'a') as the_file:
                the_file.write(TimeEntry1.get() + ":" + TimeEntry2.get() + " ")
                the_file.write("Welding Components Together " + " Coordinates: " + "(" + str(pointerx/2) + "," + str(pointery/2) + ")" + "\n")
    elif(str(workAreaMenu.get()) == "Machine Assembly" and (str(workStationMenu.get()) == "Installing the Casing")):#
        x1,y1,x2,y2 = canvas.coords(machineAssemblyDept)
        if(((int(pointerx) - 45) < int(x1) ) or ((int(pointery) - 20) < int(y1)) or ((int(pointerx) + 45) > int(x2) or ((int(pointery) + 20) > int(y2)))):
            errorWindow()
        else:
            canvas.coords(installCasingWKS,int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20))
            canvas.coords(installCasingWksLabel,pointerx,pointery)
            with open('Data/activity log.txt', 'a') as the_file:
                the_file.write(TimeEntry1.get() + ":" + TimeEntry2.get() + " ")
                the_file.write("Installing the Casing " + " Coordinates: " + "(" + str(pointerx/2) + "," + str(pointery/2) + ")" + "\n")
    elif(str(workAreaMenu.get()) == "Quality Control" and (str(workStationMenu.get()) == "Conduct Quality Tests")):
        x1,y1,x2,y2 = canvas.coords(qualityControlDept)
        if(((int(pointerx) - 45) < int(x1) ) or ((int(pointery) - 20) < int(y1)) or ((int(pointerx) + 45) > int(x2) or ((int(pointery) + 20) > int(y2)))):
            errorWindow()
        else:
            canvas.coords(conductQualityTestingWKS,int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20))
            canvas.coords(conductQualityTestingWksLabel,pointerx,pointery)
            with open('Data/activity log.txt', 'a') as the_file:
                the_file.write(TimeEntry1.get() + ":" + TimeEntry2.get() + " ")
                the_file.write("Conduct Quality Tests " + " Coordinates: " + "(" + str(pointerx/2) + "," + str(pointery/2) + ")" + "\n")
    elif(str(workAreaMenu.get()) == "Packaging" and (str(workStationMenu.get()) == "Packaging the Machines")):
        x1,y1,x2,y2 = canvas.coords(crateAndPackageDept)
        if(((int(pointerx) - 45) < int(x1) ) or ((int(pointery) - 20) < int(y1)) or ((int(pointerx) + 45) > int(x2) or ((int(pointery) + 20) > int(y2)))):
            errorWindow()
        else:     
            canvas.coords(packagingWKS,int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20))  
            canvas.coords(packagingWksLabel,pointerx,pointery)
            with open('Data/activity log.txt', 'a') as the_file:
                the_file.write(TimeEntry1.get() + ":" + TimeEntry2.get() + " ")
                the_file.write("Packaging the Machines " + " Coordinates: " + "(" + str(pointerx/2) + "," + str(pointery/2) + ")" + "\n")
    elif(str(workAreaMenu.get()) == "Storage" and (str(workStationMenu.get()) == "Storing the Packaged Machines")):
        x1,y1,x2,y2 = canvas.coords(storageDept)
        if(((int(pointerx) - 45) < int(x1) ) or ((int(pointery) - 20) < int(y1)) or ((int(pointerx) + 45) > int(x2) or ((int(pointery) + 20) > int(y2)))):
            errorWindow()
        else:   
            canvas.coords(storageWKS,int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20))  
            canvas.coords(storageWksLabel,pointerx,pointery)
            with open('Data/activity log.txt', 'a') as the_file:
                the_file.write(TimeEntry1.get() + ":" + TimeEntry2.get() + " ")
                the_file.write("Storing the Packaged Machines " + " Coordinates: " + "(" + str(pointerx/2) + "," + str(pointery/2) + ")" + "\n")
    elif(str(workAreaMenu.get()) == "Loading Dock"):#Does not actually get placed
         print("x")
#Function to place down lines
global lineDict
lineDict = []
linex1 = -1
liney1 = -1
linex2 = -1
liney2 = -1
#grabs first point
def point1(event):
   global linex1,liney1
   linex1 = int(event.x)
   liney1 = int(event.y)
   print("a")
#grabs second point
def point2(event):
   global linex2,liney2
   linex2 = int(event.x)
   liney2 = int(event.y)
   placeLine()
   print("b")
#places line down
#note this does not save the line in the converted values
def placeLine():
    global linex2,liney2,linex1,liney1
    print("placing")
    if(linex1 != -1 and liney1 != -1 and linex2 != -1 and liney2 != -1):
        if(abs(linex1 - linex2) < abs(liney1 - liney2)):
            lineDict.append(canvas.create_line(linex1,liney1,linex1,liney2,width=15, arrow=LAST))
        else:
            lineDict.append(canvas.create_line(linex1,liney1,linex2,liney1,width=15, arrow=LAST))
        linex1 = -1
        liney1 = -1
        linex2 = -1
        liney2 = -1
#used to delete a line 
def deleteLine(event):
    pointerx = int(event.x)#grabs the mouses x
    pointery = int(event.y)#grabs the mouses y
    for z in lineDict: #checks each existing line placed 
        x1,y1,x2,y2 = canvas.coords(z) #grabs coordinates of lines
        if(((abs(pointerx - x1) <= 10) or (abs(pointerx - x2) <=10)) and ((abs(pointery - y1) <= 10) or (abs(pointery - y2) <= 10))): #checks end values of 
            canvas.delete(z) #deletes the line 
            lineDict.remove(z) #deletes the line from the array
#this function displays the distance of the line
def getDistance(event):
    pointerx = int(event.x)#grabs the mouses x
    pointery = int(event.y)#grabs the mouses y
    for z in lineDict: #checks each existing line placed 
        x1,y1,x2,y2 = canvas.coords(z) #grabs coordinates of lines
        if(((abs(pointerx - x1) <= 10) or (abs(pointerx - x2) <=10)) and ((abs(pointery - y1) <= 10) or (abs(pointery - y2) <= 10))): #checks end values of 
            distance = (sqrt(((int(x2)-int(x1))**2) + ((int(y2)-int(y1))**2)))/2
            messagebox.showinfo("Path Distance", str(distance )+ " ft.")
            #wrtie to activity file
#this prints the total distance on the activity log
def getDistance1():
    overallDist = 0
    for z in lineDict: #checks each existing line placed 
        x1,y1,x2,y2 = canvas.coords(z) #grabs coordinates of lines
        distance = (sqrt(((int(x2)-int(x1))**2) + ((int(y2)-int(y1))**2)))/2
        overallDist += distance
        with open('Data/activity log.txt', 'a') as the_file:
            the_file.write("End Time: " + TimeEntry1.get() + ":" + TimeEntry2.get() + " ")
            the_file.write("End Distance: " + str(overallDist) + "ft" + "\n")
def getDistance2():
    overallDist = 0
    for z in lineDict: #checks each existing line placed 
        x1,y1,x2,y2 = canvas.coords(z) #grabs coordinates of lines
        distance = (sqrt(((int(x2)-int(x1))**2) + ((int(y2)-int(y1))**2)))/2
        overallDist += distance
    messagebox.showinfo("Total Distance", str(overallDist) + " ft.")    
#deciding functionality of mouse clicks 
def figureOutFunction(event):
    if(objectsVar.get() ==  'Work Area'):
        print("x")
        return placeArea(event)
    elif(objectsVar.get() == 'Work Station'):
        print("y")
        return placeWorkStation(event)
    else:
        if(actionsVar.get() == 'Placing Objects'):
            print("z")
            return point1(event)
        elif(actionsVar.get() == 'Removin Objects'):
            print("w")
            return deleteLine(event)
        else:
            return getDistance(event)
canvas.bind("<Button-1>", figureOutFunction)
canvas.bind("<Button-3>", point2)


#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^Util Frame Creation^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#


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
t=None #variable for mins
sec=None #variable for seconds
TimeEntry1=tk.StringVar() #holds the min value
TimeEntry2=tk.StringVar() #holds the secs value
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
    getDistance1()
    # upload()
    uploadGoogleDrive()

#Widgits
clockUtil1 = ttk.Entry(utilFrame, textvariable = TimeEntry1 ,width=10)#shows the mins
clockUtil2 = ttk.Entry(utilFrame, textvariable = TimeEntry2 ,width=10)#shows the secs
lb = tk.Label(utilFrame, text = ':' )#colon for separation of sec and min
stbtn = ttk.Button(utilFrame, width=10, text= 'start', command = st)
stpbtn = ttk.Button(utilFrame, width=10, text= 'stop', command = stp)
#reqbtn= ttk.Button(utilFrame, text="Open Requirements Window")
distBtn = ttk.Button(utilFrame,text="Total Distance", command = getDistance2)
clockUtil1.grid(row=0,column=0)
lb.grid(row=0,column=1)
clockUtil2.grid(row=0,column=2)
stbtn.grid(row=1,column=0)
stpbtn.grid(row=1,column=2)
#reqbtn.grid(row=2,column=0,columnspan=3)
distBtn.grid(row=2,column=4)
#***************************End of Program********************************************#
#packs in tabs to frame
notebook.pack(expand = 1, fill = 'both')
#End Loop
root.mainloop()
