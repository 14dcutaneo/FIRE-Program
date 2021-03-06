#imports
import tkinter
from tkinter import messagebox
from tkinter import *
import tkinter.ttk as ttk
import tkinter as tk
from threading import Thread
import time
from tkinter import StringVar
from tkinter.font import Font
from PIL import Image, ImageTk
from math import sqrt
from tkinter import Tk, Frame, PhotoImage, Label

#********************************************Window*******************************************************#
#Main Window Creation
root = tk.Tk() #Instantiate main window
root.title("FIRE - Designing Innovations Application") #adds window title
notebook = ttk.Notebook(root) #instantiates notebook
root.iconbitmap("fire logo icon2.ico")#adds the fire logo to the top left of the frame

#Tab Creation (adding tabs to the main window and giving them a title)
probstab = ttk.Frame(root) #problem statement frame
demotab = ttk.Frame(root) #demographic frame
canvastab = ttk.Frame(root) #canvas frame
notebook.add(probstab, text='Problem Statement\n') #adds the problem statement frame to the notebook with it's title
notebook.add(demotab, text='Demographic Information\n' ) #adds the demographic frame to the notebook with it's title
notebook.add(canvastab, text='Factory Layout\n') #adds the canvas frame to the notebook with it's title

#Demographic
def create_helpWindow1():
    helpWindow1 = tk.Toplevel(root) 
    demoHelpLabel = tk.Label(helpWindow1, text = 'Demographic Questions Help Menu')
    demoHelpLabel.config(font = ("Times New Roman", 12))
    demoHelpText = tk.Label(helpWindow1, text = 'Answer the questions to the best of you ability to help our data collection. If one of the dropdowns does not have an option that accurately describes you, simply choose one that is as close as possible. Be sure to read the questions carefully and make sure you answer them all.', wraplength = 500)
    demoHelpText.config(font = ("Times New Roman", 10))
    demoHelpLabel.pack()
    demoHelpText.pack()
def create_helpWindow2():
    helpWindow2 = tk.Toplevel(root)
    factoryHelpLabel = tk.Label(helpWindow2, text = 'Factory Layout Help Menu')
    factoryHelpLabel.config(font = ("Times New Roman", 12))
    factoryHelpText = tk.Label(helpWindow2, text = "To place a work area"+"\n"+"- Fill in the size parameter for that area"+"\n"+"- Click where you want the center of the area to be located."+"\n"+" "+"\n"+"To place a work station"+"\n"+"- Use the dropdowns to select both the work area and work station that belongs in the work area"+"\n"+"- Click where you want the area or station's center."+"\n"+" ""\n"+"Note: If you can not remember which stations go to which areas, review the diagram on the first tab."+"\n"+" "+"\n"+" To place the lines between work stations"+"\n"+"- Left-click for the starting point"+"\n"+"- Then right-click for the end point", wraplength = 200)
    factoryHelpText.config(font = ("Times New Roman", 10), justify = LEFT)
    factoryHelpLabel.pack()
    factoryHelpText.pack()
def create_helpWindow3():
    helpWindow3 = tk.Toplevel(root)
    aboutHelpLabel = tk.Label(helpWindow3, text = 'More About Background Info. and Problem Statement')
    aboutHelpLabel.config(font = ("Times New Roman", 12))
    aboutHelpText = tk.Label(helpWindow3, text = 'WASTE Inc. desires a streamlined facility layout to help save its business. Currently, they are struggling with many problems. Because their capital is tied up in inventory, they have perpetual cash flow problems. They believe that they need this inventory, however, to meet their customers’ demands for short delivery times. When an order for a machine hits the production floor, they need to complete it and ship it within five days. They currently keep stockpiles of module frames, machine frames, and assembled modules. Despite the current level of inventory, they still have trouble meeting this delivery target due to the various delays and bottlenecks within the operation. WASTE Inc. currently manufactures and sells one product called a “machine”. Each machine is built with 5 of the same parts known as modules. The size of a completed machine is 7 ft. x 11 ft. Overall, WASTE Inc. is in trouble. And they believe that their current facility layout and production management system are major contributing factors to these problems. Thus, they have asked your team to redesign the facility to support its goals.', wraplength = 500)
    aboutHelpText.config(font = ("Times New Roman", 10))
    aboutHelpLabel.pack()
    aboutHelpText.pack()
#file menu
menu = Menu(root)
root.config(menu = menu)
fileMenu = Menu(menu)
menu.add_cascade(label = 'File', menu=fileMenu)
fileMenu.add_command(label = 'New')
fileMenu.add_command(label = 'Open')
fileMenu.add_command(label = 'Save')
fileMenu.add_separator()
fileMenu.add_command(label = 'Exit', command = root.quit)
helpMenu = Menu(menu)
menu.add_cascade(label = 'Help', menu=helpMenu)
helpMenu.add_command(label = 'Demographic Questions', command = create_helpWindow1)
helpMenu.add_command(label = 'Factory Layout Questions', command = create_helpWindow2)
helpMenu.add_command(label = 'About the Design Problem', command = create_helpWindow3)

#*********************************Problem Statement Tab*****************************************************#
#Title
probstaTitleLabel = tk.Label(probstab, text="Factory Layout Problem Statement and Description")#adds the text label
probstaTitleLabel.grid(row = 1, column = 0)#places it in a specified grid spot
probstaTitleLabel.config(font = ("Times New Roman", 16 ))#adjust the font and font size
#Overview Header
probstaOvHeader = tk.Label(probstab, text = "Overview")
probstaOvHeader.grid(row = 2, column = 0)
probstaOvHeader.config(font = ("Times New Roman", 12, "bold"), anchor = 'w')
#Overview Text
probstaOverViewLabel = tk.Label(probstab, text="A new factory layout needs to be designed to reduce product travel distance and material handling effort. Each work area within the factory has certain processes that need to be accomplished in order to move to the next area. The path of the machine starts and ends at the loading dock where parts are received and the final product is shipped out. After the processes have been completed at each of the corresponding workstations, the parts are moved to the next area using a forklift. The travel distance of the machine as it moves through the factory is measured by its path between workstations and being transported from one area or department to the next. The path between both workstations and work areas should be considered for maximum productivity.", wraplength = 1500)
probstaOverViewLabel.grid(row = 3, column = 0)
probstaOverViewLabel.config(font = ("Times New Roman", 12), anchor = 'w')
#Production Area Header
probstaPAHeader = tk.Label(probstab, text = "Production Area")
probstaPAHeader.grid(row = 4, column = 0)
probstaPAHeader.config(font = ("Times New Roman", 12, "bold"), anchor = 'w')
#Production Area Text
probstaTextLabel = tk.Label(probstab, text="The following image describes the major components of a ‘machine’, the processing steps, and the key departments in the facility. Note each completed ‘machine’ requires 1 Machine Frame and 5 Modules. Also keep in mind that this is just a description of the steps needed to make a machine and this is not necessarily what your solution should look like.", wraplength = 1500)
probstaTextLabel.grid(row = 5, column = 0)
probstaTextLabel.config(font = ("Times New Roman", 12, "bold"), anchor = 'w')
#Add the Factory Area Image
factIMG = "Factory Process.jpg"#instantiates an image object for our Factory Process Image
img = ImageTk.PhotoImage(Image.open(factIMG))#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
panel = tk.Label(probstab, image = img)#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel.grid(row = 6, column =  0, columnspan = 2)#The Pack geometry manager packs widgets in rows or columns.
#Add the Fire Logo to the GUI
fireIMG = "fire logo.png"
img2 = ImageTk.PhotoImage(Image.open(fireIMG))
panel2 = tk.Label(probstab, image = img2)
panel2.grid(row = 0, column =  0, columnspan = 3)

#******************************************Demographic tab***************************************************#
#Title
demotabTitleLabel = tk.Label(demotab, text="\nDemographic Information\n") #Creates the title
demotabTitleLabel.grid(row = 0, column = 0, columnspan = 3) #Places the title
demotabTitleLabel.config(font = ("Times New Roman", 16)) #Changes the font and size of title
#Instructions
demotabInstructions = tk.Label(demotab, text="\nPlease answer the following questions before starting the timer and beginning the design problem.\n") #Creates the instructions
demotabInstructions.grid(row=1, column=0, columnspan = 3) #Places the instructions
demotabInstructions.config(font = ("Times New Roman", 12)) #changes the font and size of instructions
#Question 1: Age (label)
ageQuestionLabel = tk.Label(demotab, text="\nWhat is your age?\n") #Creates the label
ageQuestionLabel.grid(row = 2, column = 0) #Places the label
ageQuestionLabel.config(font = ("Times New Roman", 10), anchor = 'w') #Changes the font and size of label
#Question 1: Age (textbox)
ageQuestionTextbox = tk.Entry(demotab, width = 10) #Creates the textbox
ageQuestionTextbox.grid(row = 2, column = 1) #Places the textbox
#Question 2: Educational background (label)
educationBackgroundText = tk.Label(demotab, text='\nWhat is your educational background?\n') #Creates the label
educationBackgroundText.grid(row = 3, column = 0) #Places the label
educationBackgroundText.config(font = ("Times New Roman", 10)) #Chantes the font and size of label
#Question 2: Educational background (drop down)
optionMenuVar = StringVar(demotab) #Sets the variable for list
backgrounds = ["Student at a public or private university", "Faculty at a public or private university", "Student at a High school"] #Creates list of options for drop down
optionMenuVar.set(backgrounds[0]) #Sets default to first background in the list
educationBackgroundDropDown = OptionMenu(demotab, optionMenuVar, *backgrounds) #Creates the drop down
educationBackgroundDropDown.grid(row = 3, column = 1) #Places the drop down in the tab
educationBackgroundDropDown.config(width = 35) #Locks the width of drop down
#Question 3: Highest level of education (label)
levelOfEducationText = tk.Label(demotab, text='\nWhat is the highest level of education you have completed?\n') #Creates the label
levelOfEducationText.grid(row = 4, column = 0) #Places the label
levelOfEducationText.config(font = ("Times New Roman", 10)) #Changes the font and size
#Question 3: Highest level of education (drop down)
optionMenuVar1 = StringVar(demotab) #Sets the variable for list
levels = ["9th Grade", "10th Grade", "11th Grade", "12th Grade", "Graduated High School", "1 Year of College", "2 Years of College", "3 Years of College", "4 Years of College", "Graduated College", "Some Graduate School", "Completed Graduate School"] #Creates the list of options for drop down
optionMenuVar1.set(levels[0]) #Sets the default to the first level in the list
levelOfEducationDropDown = OptionMenu(demotab, optionMenuVar1, *levels) #Creates the drop down
levelOfEducationDropDown.grid(row = 4, column = 1) #Places the drop down
levelOfEducationDropDown.config(width = 25) #Locks the width of the drop down
#Question 4: Desired college major (label)
desiredMajorLabel = tk.Label(demotab, text = '\nWhat is your desired college major? (If applicable)\n') #Creates the label
desiredMajorLabel.grid(row = 5, column = 0) #Places the label
desiredMajorLabel.config(font = ("Times New Roman", 10)) #Changes the font and size of label
#Question 4: Desired college major (textbox)
desiredMajorTextbox = tk.Entry(demotab, width = 35) #Locks the width of the textbox
desiredMajorTextbox.grid(row = 5, column = 1) #Places the textbox
#Question 5: Experience in design problems (label)
designExperienceLabel = tk.Label(demotab, text = '\nHave you had any experience with solving design problems?\n')
designExperienceLabel.grid(row = 6, column = 0)
designExperienceLabel.config(font = ("Times New Roman", 10))
#Question 5: Experience in design problems (radiobutton)
optionsVar = StringVar(demotab)
yesOrNo = [('Yes', 'Yes'), ('No', 'No')]
optionsVar.set('Yes')
count = 1
for text, mode in yesOrNo:
    designExperienceRB = Radiobutton(demotab, variable = optionsVar, value = mode, text = text)
    designExperienceRB.grid(row = 6, column = count)
    designExperienceRB.config(font = ("Times New Roman", 10))
    count += 1
#Question 6: Experience in factory design (label)
factoryExperienceLabel = tk.Label(demotab, text = '\nHave you had any experience in designing a factory layout?\n')
factoryExperienceLabel.grid(row = 7, column = 0)
factoryExperienceLabel.config(font = ("Times New Roman", 10))
#Question 6: Experience in factory design (radiobutton)
optionsVar1 = StringVar(demotab)
yesOrNo1 = [('Yes', 'Yes'), ('No', 'No')]
optionsVar1.set('Yes')
count = 1
for text, mode in yesOrNo1:
    factoryExperienceRB = Radiobutton(demotab, variable = optionsVar1, value = mode, text = text)
    factoryExperienceRB.grid(row = 7, column = count)
    factoryExperienceRB.config(font = ("Times New Roman", 10))
    count += 1
#Save button
def save(): #function to save all of the demo info to the activity log text file
    question1 = str(ageQuestionTextbox.get())
    question2 = str(optionMenuVar.get())
    question3 = str(optionMenuVar1.get())
    question4 = str(desiredMajorTextbox.get())
    question5 = str(optionsVar.get())
    question6 = str(optionsVar1.get())
    with open('activity log.txt', 'a') as the_file:
        the_file.write(question1+"\t"+question2+"\t"+question3+"\t"+question4+"\t"+question5+"\t"+question6+"\n")
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
xLabel = tk.Label(areaFrame, text = 'X')
xLabel.grid(row = 0, column = 1)
yLabel = tk.Label(areaFrame, text = 'Y')
yLabel.grid(row = 0, column = 2)
positionLabel = tk.Label(areaFrame, text = 'Position')
positionLabel.grid(row = 2, column = 3)
sizeLabel = tk.Label(areaFrame, text = 'Size')
sizeLabel.grid(row = 1, column = 3)
#Locked areas
lockedAreas = tk.Label(areaFrame, text = "*Note: The following work areas are locked in size and position*")
lockedAreas.grid(row = 19, column = 0, columnspan = 4)
#Frame fabrication (blue)
workAreaLabel1 = tk.Label(areaFrame, text = "Frame Fabrication")
workAreaLabel1.config(width = 15, bg = "Blue")
workAreaLabel1.grid(row = 1, column =0)
#Module assembly (green)
workAreaLabel2 = tk.Label(areaFrame, text = "Module Assembly")
workAreaLabel2.config(width = 15, bg = "Green")
workAreaLabel2.grid(row = 4, column =0)
#Machine assembly (cyan)
workAreaLabel3 = tk.Label(areaFrame, text = "Machine Assembly")
workAreaLabel3.config(width = 15, bg = "Cyan")
workAreaLabel3.grid(row = 7, column =0)
#Quality control (orange)
workAreaLabel4 = tk.Label(areaFrame, text = "Quality Control")
workAreaLabel4.config(width = 15, bg = "Orange")
workAreaLabel4.grid(row = 10, column =0)
#Packaging (magenta)
workAreaLabel5 = tk.Label(areaFrame, text = "Packaging")
workAreaLabel5.config(width = 15, bg = "Magenta")
workAreaLabel5.grid(row = 13, column =0)
#Storage (gold)
workAreaLabel6 = tk.Label(areaFrame, text = "Storage")
workAreaLabel6.config(width = 15, bg = "Gold")
workAreaLabel6.grid(row = 16, column =0)
#Recieving (red)
workAreaLabel7 = tk.Label(areaFrame, text = "Recieving")
workAreaLabel7.config(width = 15, bg = "Red")
workAreaLabel7.grid(row = 20, column =0)
#Painting (yellow)
workAreaLabel8 = tk.Label(areaFrame, text = "Painting")
workAreaLabel8.config(width = 15, bg = "Yellow")
workAreaLabel8.grid(row = 23, column =0)
#Loading dock (light green)
workAreaLabel9 = tk.Label(areaFrame, text = "Loading Dock")
workAreaLabel9.config(width = 15, bg = "Light Green")
workAreaLabel9.grid(row = 26, column =0)
#Work area selection
workAreaSelection = tk.Label(areaFrame, text = "Select work area to make changes")
workAreaSelection.grid(row = 0, column = 6)
workAreaSelection.config(font = ("Times New Roman", 11))
#Work area selection
workAreaSelection = tk.Label(areaFrame, text = "Select work station to make changes")
workAreaSelection.grid(row = 2, column = 6)
workAreaSelection.config(font = ("Times New Roman", 11))
#Area, station, line 
areaStaionLineLabel = tk.Label(areaFrame, text = "Select object to make changes")
areaStaionLineLabel.grid(row = 4, column = 6)
areaStaionLineLabel.config(font = ("Times New Roman", 11))
#Placing and deleting 
placeRemoveLabel = tk.Label(areaFrame, text = "Switch from placing to removing")
placeRemoveLabel.grid(row = 9, column = 6)
placeRemoveLabel.config(font = ("Times New Roman", 11))
#Apply buttons
# applyButton1 = tk.Button(areaFrame, text = "Apply")
# applyButton1.grid(row = 2, column = 0)
# applyButton1.config(height = 1, width = 10)
# applyButton2 = tk.Button(areaFrame, text = "Apply")
# applyButton2.grid(row = 5, column = 0)
# applyButton2.config(height =1, width = 10)
# applyButton3 = tk.Button(areaFrame, text = "Apply")
# applyButton3.grid(row = 8, column = 0)
# applyButton3.config(height = 1, width = 10)
# applyButton4 = tk.Button(areaFrame, text = "Apply")
# applyButton4.grid(row = 11, column = 0)
# applyButton4.config(height = 1, width = 10)
# applyButton5 = tk.Button(areaFrame, text = "Apply")
# applyButton5.grid(row = 14, column = 0)
# applyButton5.config(height = 1, width = 10)
# applyButton6 = tk.Button(areaFrame, text = "Apply")
# applyButton6.grid(row = 17, column = 0)
# applyButton6.config(height = 1, width = 10)
#Spaces
space1 = tk.Label(areaFrame, text = " ")
space1.grid(row = 3, column = 0,  columnspan =3)
space2 = tk.Label(areaFrame, text = " ")
space2.grid(row = 6, column = 0,  columnspan =3)
space3 = tk.Label(areaFrame, text = " ")
space3.grid(row = 9, column = 0,  columnspan =3)
space4 = tk.Label(areaFrame, text = " ")
space4.grid(row = 12, column = 0,  columnspan =3)
space5 = tk.Label(areaFrame, text = " ")
space5.grid(row = 15, column = 0,  columnspan =3)
space6 = tk.Label(areaFrame, text = " ")
space6.grid(row = 18, column = 0, columnspan = 3)
space7 = tk.Label(areaFrame, text = " ")
space7.grid(row = 22, column = 0, columnspan = 3)
space8 = tk.Label(areaFrame, text = " ")
space8.grid(row = 25, column = 0, columnspan = 3)
space9 = tk.Label(areaFrame, text = '     ')
space9.grid(row = 0, column = 5, rowspan = 15)
# Position and size text boxes
# Frame fabrication boxes
    # X dimension
sizeBox1x = tk.Entry(areaFrame, width = 10)
sizeBox1x.grid(row = 1, column = 1)
positionBox1x = tk.Entry(areaFrame, width = 10)
positionBox1x.grid(row = 2, column = 1)
    # Y dimension
sizeBox1y = tk.Entry(areaFrame, width = 10)
sizeBox1y.grid(row = 1, column = 2)
positionBox1y = tk.Entry(areaFrame, width = 10)
positionBox1y.grid(row = 2, column = 2)
# Module assembly boxes
    # X dimension
sizeBox2x = tk.Entry(areaFrame, width = 10)
sizeBox2x.grid(row = 4, column = 1)
positionBox2x = tk.Entry(areaFrame, width = 10)
positionBox2x.grid(row = 5, column = 1)
    # Y dimension
sizeBox2y = tk.Entry(areaFrame, width = 10)
sizeBox2y.grid(row = 4, column = 2)
positionBox2y = tk.Entry(areaFrame, width = 10)
positionBox2y.grid(row = 5, column = 2)
# Machine assembly boxes
    # X dimension
sizeBox3x = tk.Entry(areaFrame, width = 10)
sizeBox3x.grid(row = 7, column = 1)
positionBox3x = tk.Entry(areaFrame, width = 10)
positionBox3x.grid(row = 8, column = 1)
    # Y dimension
sizeBox3y = tk.Entry(areaFrame, width = 10)
sizeBox3y.grid(row = 7, column = 2)
positionBox3y = tk.Entry(areaFrame, width = 10)
positionBox3y.grid(row = 8, column = 2)
#Quality control boxes
    # X dimension
sizeBox4x = tk.Entry(areaFrame, width = 10)
sizeBox4x.grid(row = 10, column = 1)
positionBox4x = tk.Entry(areaFrame, width = 10)
positionBox4x.grid(row = 11, column = 1)
    # Y dimension
sizeBox4y = tk.Entry(areaFrame, width = 10)
sizeBox4y.grid(row = 10, column = 2)
positionBox4y = tk.Entry(areaFrame, width = 10)
positionBox4y.grid(row = 11, column = 2)
# Packaging dept. boxes
    # X dimension
sizeBox5x = tk.Entry(areaFrame, width = 10)
sizeBox5x.grid(row = 13, column = 1)
positionBox5x = tk.Entry(areaFrame, width = 10)
positionBox5x.grid(row = 14, column = 1)
    # Y dimension
sizeBox5y = tk.Entry(areaFrame, width = 10)
sizeBox5y.grid(row = 13, column = 2)
positionBox5y = tk.Entry(areaFrame, width = 10)
positionBox5y.grid(row = 14, column = 2)
# Storage department
    # X dimension
sizeBox6x = tk.Entry(areaFrame, width = 10)
sizeBox6x.grid(row = 16, column = 1)
positionBox6x = tk.Entry(areaFrame, width = 10)
positionBox6x.grid(row = 17, column = 1)
    # Y dimension
sizeBox6y = tk.Entry(areaFrame, width = 10)
sizeBox6y.grid(row = 16, column = 2)
positionBox6y = tk.Entry(areaFrame, width = 10)
positionBox6y.grid(row = 17, column = 2)
# The work areas that don't move have text boxes
# Recieving dept.
    # X dimension
sizeBox7x = tk.Label(areaFrame, text = "100", width = 10)
sizeBox7x.grid(row = 20, column = 1)
sizeBox7x.config(bg = "white", relief = SUNKEN)
positionBox7x = tk.Label(areaFrame, text = "250", width = 10)
positionBox7x.grid(row = 21, column = 1)
positionBox7x.config(bg = "white", relief = SUNKEN)
    # Y dimension
sizeBox7y = tk.Label(areaFrame, text = "50", width = 10)
sizeBox7y.grid(row = 20, column = 2)
sizeBox7y.config(bg = "white", relief = SUNKEN)
positionBox7y = tk.Label(areaFrame, text = "325", width = 10)
positionBox7y.grid(row = 21, column = 2)
positionBox7y.config(bg = "white", relief = SUNKEN)
#Painting dept.
    # X dimension
sizeBox8x = tk.Label(areaFrame, text = "80", width = 10)
sizeBox8x.grid(row = 23, column = 1)
sizeBox8x.config(bg = "white", relief = SUNKEN)
positionBox8x = tk.Label(areaFrame, text = "175", width = 10)
positionBox8x.grid(row = 24, column = 1)
positionBox8x.config(bg = "white", relief = SUNKEN)
    # Y dimension
sizeBox8y = tk.Label(areaFrame, text = "100", width = 10)
sizeBox8y.grid(row = 23, column = 2)
sizeBox8y.config(bg = "white", relief = SUNKEN)
positionBox8y = tk.Label(areaFrame, text = "180", width = 10)
positionBox8y.grid(row = 24, column = 2)
positionBox8y.config(bg = "white", relief = SUNKEN)
# Loading dock
sizeBox9x = tk.Label(areaFrame, text = "50", width = 10)
sizeBox9x.grid(row = 26, column = 1)
sizeBox9x.config(bg = "white", relief = SUNKEN)
positionBox9x = tk.Label(areaFrame, text = "80", width = 10)
positionBox9x.grid(row = 27, column = 1)
positionBox9x.config(bg = "white", relief = SUNKEN)
    # Y dimension
sizeBox9y = tk.Label(areaFrame, text = "325", width = 10)
sizeBox9y.grid(row = 26, column = 2)
sizeBox9y.config(bg = "white", relief = SUNKEN)
positionBox9y = tk.Label(areaFrame, text = "310", width = 10)
positionBox9y.grid(row = 27, column = 2)
positionBox9y.config(bg = "white", relief = SUNKEN)
# Work area selection dropdown
workAreaMenu = StringVar(areaFrame)  # Sets the variable for list
workAreas = ["Recieving", "Frame Fabrication", "Painting", "Module Asembly", "Machine Assembly", "Quality Control", "Packaging", "Storage"]  # Creates the list of options for drop down
workAreaMenu.set(workAreas[0])  # Sets the default to the first level in the list
workAreaDropDown = OptionMenu(areaFrame, workAreaMenu, *workAreas)  # Creates the drop down
workAreaDropDown.grid(row=1, column=6)  # Places the drop down
workAreaDropDown.config(width=18)  # Locks the width of the drop down
#Workstation selection
workStationMenu = StringVar(areaFrame)  # Sets the variable for list
workStations = ["Recieve Raw Materials","Sort Raw Materials", "Make Module Frame Cuts", "Make Machine Frame Cuts", "Frame Tack-Welding","Painting Preparation", "Painting", "Frame Drying","Internal Assembly", "External Assembly","Machine Wiring", "Welding Components Together", "Installing the Casing","Conduct Quality Tests","Packaging the Machines","Storing the Packaged Machines"]
workStationMenu.set(workStations[0])  # Sets the default to the first level in the list
workStationDropDown = OptionMenu(areaFrame, workStationMenu, *workStations)  # Creates the drop down
workStationDropDown.grid(row=3, column=6)  # Places the drop down
workStationDropDown.config(width=18)  # Locks the width of the drop down
#Radio button
#Area station line
objectsVar = StringVar(areaFrame)
areaStationLine = [('Work Area', 'Work Area'), ('Work Station', 'Work Station'), ('Machine Path', 'Machine Path')]
objectsVar.set('Work Area')
count = 5
for text, mode in areaStationLine:
    areaStationLineRB = Radiobutton(areaFrame, variable=objectsVar, value=mode, text=text)
    areaStationLineRB.grid(row=count, column=6)
    areaStationLineRB.config(font=("Times New Roman", 10))
    count += 1
#Placing or removing
actionsVar = StringVar(areaFrame)
placeRemove = [('Placing Path', 'Placing Objects'), ('Removing Path', 'Removin Objects'),('Show Path Distance', 'Show Path Distance')]
actionsVar.set('Placing Objects')
count = 10
for text, mode in placeRemove:
    placeRemoveRB = Radiobutton(areaFrame, variable=actionsVar, value=mode, text=text)
    placeRemoveRB.grid(row=count, column=6)
    placeRemoveRB.config(font=("Times New Roman", 10))
    count += 1

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

workAreasArr = [receivingDept,frameFabricationDept,paintDept,loadingDock,moduleAssemblyDept,machineAssemblyDept,qualityControlDept,storageDept,crateAndPackageDept]
workStationsArr = [receiveRawMaterialsWKS,sortRawMaterialsWKS,makeMachineCutsWKS,makeModuleCutsWKS,frameTackWeldingWKS,paintPrepWKS,paintingWKS,dryingWKS,internalAssemblyWKS,externalAssemblyWKS,wiringWKS,weldingWKS,installCasingWKS,conductQualityTestingWKS,packagingWKS,storageWKS]
canvas.pack()

# linesRWKS = {}

# linesSRMWKS = {}
# linesMMODCWKS = {}
# linesMMACWKS = {}
# linesFTWWKS = {}

# linesPPWKS = {}
# linesPWKS = {}
# linesPDWKS = {}

# linesIAWKS = {}
# linesEAWKS = {}

# linesWiringWKS = {}
# linesWeldWKS = {}
# linesICWKS = {}

# linesQT = {}

# linesCP = {}

# linesS = {}

# linesL = {}

# shapesDictionary = []

# shapesDictionary.append(linesRWKS)
# shapesDictionary.append(linesSRMWKS) 
# shapesDictionary.append(linesMMODCWKS) 
# shapesDictionary.append(linesMMACWKS) 
# shapesDictionary.append(linesFTWWKS) 
# shapesDictionary.append(linesPPWKS) 
# shapesDictionary.append(linesPWKS) 
# shapesDictionary.append(linesPDWKS) 
# shapesDictionary.append(linesIAWKS) 
# shapesDictionary.append(linesEAWKS) 
# shapesDictionary.append(linesWiringWKS)
# shapesDictionary.append(linesWeldWKS) 
# shapesDictionary.append(linesICWKS) 
# shapesDictionary.append(linesQT) 
# shapesDictionary.append(linesCP)
# shapesDictionary.append(linesS) 
# shapesDictionary.append(linesL) 

#error pop-up window for out of bounds message
def errorWindow():
    messagebox.showerror("Error", "Can't place area outside of factory area")
#error pop-up window for area size message
def error1Window():
    messagebox.showerror("Error2", "Area does not fit requirements")
#Function to find center of a given rectangle area
def findCenter(area):
    x1,y1,x2,y2 = canvas.coords(area)
    xcenter = (int(x1) + int(x2))/2
    ycenter =  (int(y1) + int(y2))/2
    coordArr = [xcenter,ycenter]
    return coordArr
#get expansion width
def factor1(rectangle):
    a = float(rectangle.get())
    w = int(a)
    return w
#get expansion height
def factor2(rectangle):
    a = float(rectangle.get())
    h = int(a)
    return h
#This function places the areas along with their labels and workstations
def placeArea(event):
    pointerx = event.x
    pointery = event.y
    if(str(workAreaMenu.get()) == "Recieving"):#Does not actually get placed
        print("x")
    elif(str(workAreaMenu.get()) == "Frame Fabrication"):
        if((int(pointerx - factor1(sizeBox1x))<0) or (int(pointery - factor2(sizeBox1y)) < 0) or (int(pointerx + factor1(sizeBox1x)) >700) or (int(pointery + factor2(sizeBox1y)) > 700)):
            errorWindow()
        elif((int(sizeBox1x.get())*int(sizeBox1y.get())) > 16900):
            error1Window()
        else:
            positionBox1x.delete(0,END)
            positionBox1x.insert(0,str(round(pointerx / 2)))
            positionBox1y.delete(0,END)
            positionBox1y.insert(0, str(round(pointery / 2)))
            canvas.coords(frameFabricationDept, int(pointerx - factor1(sizeBox1x)), int(pointery - factor2(sizeBox1y)),int(pointerx + factor1(sizeBox1x)), int(pointery + factor2(sizeBox1y)))
            canvas.coords(sortRawMaterialsWKS,int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20))
            canvas.coords(makeModuleCutsWKS,int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20))
            canvas.coords(makeMachineCutsWKS,int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20)) 
            canvas.coords(frameTackWeldingWKS,int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20))
            canvas.coords(FFLabel,int(pointerx), int(pointery + factor2(sizeBox2y) - 10)) 
            canvas.coords(sortRawMaterialsWksLabel,0,0)
            canvas.coords(makeModuleCutsWksLabel,0,0)
            canvas.coords(makeMachineCutsWksLabel,0,0)
            canvas.coords(frameTackWeldingWksLabel,0,0)
            with open('activity log.txt', 'a') as the_file:
                the_file.write(TimeEntry1.get() + ":" + TimeEntry2.get() + " ")
                the_file.write("Frame Fabrication " + "Size Set to: " + str(factor1(sizeBox1x)*factor2(sizeBox1y)) + " Coordinates: " + "(" + str(pointerx/2) + "," + str(pointery/2) + ")" + "\n")
    elif(str(workAreaMenu.get()) == "Painting"):#Does not actually get placed
         print("x")
    elif(str(workAreaMenu.get()) == "Module Asembly"):#
        if((int(pointerx - factor1(sizeBox2x))<0) or (int(pointery - factor2(sizeBox2y)) < 0) or (int(pointerx + factor1(sizeBox2x)) >700) or (int(pointery + factor2(sizeBox2y)) > 700)):
            errorWindow()
        elif((int(sizeBox2x.get())*int(sizeBox2y.get())) > 16900):
            error1Window()
        else:
            positionBox2x.delete(0,END)
            positionBox2x.insert(0,str(round(pointerx / 2)))
            positionBox2y.delete(0,END)
            positionBox2y.insert(0, str(round(pointery / 2)))
            canvas.coords(moduleAssemblyDept, int(pointerx - factor1(sizeBox2x)), int(pointery - factor2(sizeBox2y)),int(pointerx + factor1(sizeBox2x)), int(pointery + factor2(sizeBox2y)))
            canvas.coords(internalAssemblyWKS, int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20)) 
            canvas.coords(externalAssemblyWKS, int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20))
            canvas.coords(modLabel, int(pointerx), int(pointery + factor2(sizeBox2y) - 10))
            canvas.coords(internalAssemWksLabel,0,0)
            canvas.coords(externalAssemWksLabel,0,0)
            with open('activity log.txt', 'a') as the_file:
                the_file.write(TimeEntry1.get() + ":" + TimeEntry2.get() + " ")
                the_file.write("Module Assembly " + "Size Set to: " + str(factor1(sizeBox2x)*factor2(sizeBox2y)) + " Coordinates: " + "(" + str(pointerx/2) + "," + str(pointery/2) + ")" + "\n")
    elif(str(workAreaMenu.get()) == "Machine Assembly"):#
        if((int(pointerx - factor1(sizeBox3x))<0) or (int(pointery - factor2(sizeBox3y)) < 0) or (int(pointerx + factor1(sizeBox3x)) >700) or (int(pointery + factor2(sizeBox3y)) > 700)):
            errorWindow()
        elif((int(sizeBox3x.get())*int(sizeBox3y.get())) > 16900):
            error1Window()
        else:
            positionBox3x.delete(0,END)
            positionBox3x.insert(0,str(round(pointerx / 2)))
            positionBox3y.delete(0,END)
            positionBox3y.insert(0, str(round(pointery / 2)))
            canvas.coords(machineAssemblyDept, int(pointerx - factor1(sizeBox3x)), int(pointery - factor2(sizeBox3y)),int(pointerx + factor1(sizeBox3x)), int(pointery + factor2(sizeBox3y)))
            canvas.coords(wiringWKS, int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20))
            canvas.coords(weldingWKS, int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20)) 
            canvas.coords(installCasingWKS, int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20))
            canvas.coords(machLabel, int(pointerx), int(pointery + factor2(sizeBox2y) - 10))
            canvas.coords(wiringWksLabel,0,0)
            canvas.coords(weldingWksLabel,0,0)
            canvas.coords(installCasingWksLabel,0,0)
            with open('activity log.txt', 'a') as the_file:
                the_file.write(TimeEntry1.get() + ":" + TimeEntry2.get() + " ")
                the_file.write("Machine Assembly " + "Size Set to: " + str(factor1(sizeBox3x)*factor2(sizeBox3y)) + " Coordinates: " + "(" + str(pointerx/2) + "," + str(pointery/2) + ")" + "\n")
    elif(str(workAreaMenu.get()) == "Quality Control"):
        if((int(pointerx - factor1(sizeBox4x))<0) or (int(pointery - factor2(sizeBox4y)) < 0) or (int(pointerx + factor1(sizeBox4x)) >700) or (int(pointery + factor2(sizeBox4y)) > 700)):
            errorWindow()
        elif((int(sizeBox4x.get())*int(sizeBox4y.get())) > 16900):
            error1Window()
        else:
            positionBox4x.delete(0,END)
            positionBox4x.insert(0,str(round(pointerx / 2)))
            positionBox4y.delete(0,END)
            positionBox4y.insert(0, str(round(pointery / 2)))
            canvas.coords(qualityControlDept, int(pointerx - factor1(sizeBox4x)), int(pointery - factor2(sizeBox4y)),int(pointerx + factor1(sizeBox4x)), int(pointery + factor2(sizeBox4y)))
            canvas.coords(conductQualityTestingWKS, int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20))
            canvas.coords(qcLabel, int(pointerx), int(pointery + factor2(sizeBox2y) - 10))
            canvas.coords(conductQualityTestingWksLabel,0,0)
            with open('activity log.txt', 'a') as the_file:
                the_file.write(TimeEntry1.get() + ":" + TimeEntry2.get() + " ")
                the_file.write("Quality Control " + "Size Set to: " + str(factor1(sizeBox4x)*factor2(sizeBox4y)) + " Coordinates: " + "(" + str(pointerx/2) + "," + str(pointery/2) + ")" + "\n")
    elif(str(workAreaMenu.get()) == "Packaging"):
        if((int(pointerx - factor1(sizeBox5x))<0) or (int(pointery - factor2(sizeBox5y)) < 0) or (int(pointerx + factor1(sizeBox5x)) >700) or (int(pointery + factor2(sizeBox5y)) > 700)):
            errorWindow()
        elif((int(sizeBox5x.get())*int(sizeBox5y.get())) > 16900):
            error1Window()
        else:
            positionBox5x.delete(0,END)
            positionBox5x.insert(0,str(round(pointerx / 2)))
            positionBox5y.delete(0,END)
            positionBox5y.insert(0, str(round(pointery / 2)))
            canvas.coords(crateAndPackageDept, int(pointerx - factor1(sizeBox5x)), int(pointery - factor2(sizeBox5y)),int(pointerx + factor1(sizeBox5x)), int(pointery + factor2(sizeBox5y)))
            canvas.coords(packagingWKS, int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20))
            canvas.coords(cpLabel, int(pointerx), int(pointery + factor2(sizeBox2y) - 10))
            canvas.coords(packagingWksLabel,0,0)
            with open('activity log.txt', 'a') as the_file:
                the_file.write(TimeEntry1.get() + ":" + TimeEntry2.get() + " ")
                the_file.write("Packaging " + "Size Set to: " + str(factor1(sizeBox5x)*factor2(sizeBox5y)) + " Coordinates: " + "(" + str(pointerx/2) + "," + str(pointery/2) + ")" + "\n")
    elif(str(workAreaMenu.get()) == "Storage"):
        if((int(pointerx - factor1(sizeBox6x))<0) or (int(pointery - factor2(sizeBox6y)) < 0) or (int(pointerx + factor1(sizeBox6x)) >700) or (int(pointery + factor2(sizeBox6y)) > 700)):
            errorWindow()
        elif((int(sizeBox6x.get())*int(sizeBox6y.get())) > 16900):
            error1Window()
        else:
            positionBox6x.delete(0,END)
            positionBox6x.insert(0,str(round(pointerx / 2)))
            positionBox6y.delete(0,END)
            positionBox6y.insert(0, str(round(pointery / 2)))
            canvas.coords(storageDept, int(pointerx - factor1(sizeBox6x)), int(pointery - factor2(sizeBox6y)),int(pointerx + factor1(sizeBox6x)), int(pointery + factor2(sizeBox6y)))
            canvas.coords(storageWKS, int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20))
            canvas.coords(stLabel, int(pointerx), int(pointery + factor2(sizeBox2y) - 10))
            canvas.coords(storageWksLabel,0,0)
            with open('activity log.txt', 'a') as the_file:
                the_file.write(TimeEntry1.get() + ":" + TimeEntry2.get() + " ")
                the_file.write("Storage " + "Size Set to: " + str(factor1(sizeBox6x)*factor2(sizeBox6y)) + " Coordinates: " + "(" + str(pointerx/2) + "," + str(pointery/2) + ")" + "\n")
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
            with open('activity log.txt', 'a') as the_file:
                the_file.write(TimeEntry1.get() + ":" + TimeEntry2.get() + " ")
                the_file.write("Recieve Raw Materials " + " Coordinates: " + "(" + str(pointerx/2) + "," + str(pointery/2) + ")" + "\n")
    elif(str(workAreaMenu.get()) == "Frame Fabrication" and (str(workStationMenu.get()) == "Sort Raw Materials")):
        x1,y1,x2,y2 = canvas.coords(frameFabricationDept)
        if(((int(pointerx) - 45) < int(x1) ) or ((int(pointery) - 20) < int(y1)) or ((int(pointerx) + 45) > int(x2) or ((int(pointery) + 20) > int(y2)))):
            errorWindow()
        else:
            canvas.coords(sortRawMaterialsWKS,int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20))
            canvas.coords(sortRawMaterialsWksLabel,pointerx,pointery)
            with open('activity log.txt', 'a') as the_file:
                the_file.write(TimeEntry1.get() + ":" + TimeEntry2.get() + " ")
                the_file.write("Sort Raw Materials " + " Coordinates: " + "(" + str(pointerx/2) + "," + str(pointery/2) + ")" + "\n")
    elif(str(workAreaMenu.get()) == "Frame Fabrication" and (str(workStationMenu.get()) == "Make Module Frame Cuts")):
        x1,y1,x2,y2 = canvas.coords(frameFabricationDept)
        if(((int(pointerx) - 45) < int(x1) ) or ((int(pointery) - 20) < int(y1)) or ((int(pointerx) + 45) > int(x2) or ((int(pointery) + 20) > int(y2)))):
            errorWindow()
        else:
            canvas.coords(makeModuleCutsWKS,int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20))
            canvas.coords(makeModuleCutsWksLabel,pointerx,pointery)
            with open('activity log.txt', 'a') as the_file:
                the_file.write(TimeEntry1.get() + ":" + TimeEntry2.get() + " ")
                the_file.write("Make Module Frame Cuts " + " Coordinates: " + "(" + str(pointerx/2) + "," + str(pointery/2) + ")" + "\n")
    elif(str(workAreaMenu.get()) == "Frame Fabrication" and (str(workStationMenu.get()) == "Make Machine Frame Cuts")):
        x1,y1,x2,y2 = canvas.coords(frameFabricationDept)
        if(((int(pointerx) - 45) < int(x1) ) or ((int(pointery) - 20) < int(y1)) or ((int(pointerx) + 45) > int(x2) or ((int(pointery) + 20) > int(y2)))):
            errorWindow()
        else:
            canvas.coords(makeMachineCutsWKS,int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20))
            canvas.coords(makeMachineCutsWksLabel,pointerx,pointery)
            with open('activity log.txt', 'a') as the_file:
                the_file.write(TimeEntry1.get() + ":" + TimeEntry2.get() + " ")
                the_file.write("Make Machine Frame Cuts " + " Coordinates: " + "(" + str(pointerx/2) + "," + str(pointery/2) + ")" + "\n")
    elif(str(workAreaMenu.get()) == "Frame Fabrication" and (str(workStationMenu.get()) == "Frame Tack-Welding")):
        x1,y1,x2,y2 = canvas.coords(frameFabricationDept)
        if(((int(pointerx) - 45) < int(x1) ) or ((int(pointery) - 20) < int(y1)) or ((int(pointerx) + 45) > int(x2) or ((int(pointery) + 20) > int(y2)))):
            errorWindow()
        else:
            canvas.coords(frameTackWeldingWKS,int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20))
            canvas.coords(frameTackWeldingWksLabel,pointerx,pointery)
            with open('activity log.txt', 'a') as the_file:
                the_file.write(TimeEntry1.get() + ":" + TimeEntry2.get() + " ")
                the_file.write("Frame Tack-Welding " + " Coordinates: " + "(" + str(pointerx/2) + "," + str(pointery/2) + ")" + "\n")
    elif(str(workAreaMenu.get()) == "Painting" and (str(workStationMenu.get()) == "Painting Preparation")):
        x1,y1,x2,y2 = canvas.coords(paintDept)
        if(((int(pointerx) - 45) < int(x1) ) or ((int(pointery) - 20) < int(y1)) or ((int(pointerx) + 45) > int(x2) or ((int(pointery) + 20) > int(y2)))):
            errorWindow()
        else:
            canvas.coords(paintPrepWKS,int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20))
            canvas.coords(paintPrepWksLabel,pointerx,pointery)
            with open('activity log.txt', 'a') as the_file:
                the_file.write(TimeEntry1.get() + ":" + TimeEntry2.get() + " ")
                the_file.write("Painting Preparation " + " Coordinates: " + "(" + str(pointerx/2) + "," + str(pointery/2) + ")" + "\n")
    elif(str(workAreaMenu.get()) == "Painting" and (str(workStationMenu.get()) == "Painting")):
        x1,y1,x2,y2 = canvas.coords(paintDept)
        if(((int(pointerx) - 45) < int(x1) ) or ((int(pointery) - 20) < int(y1)) or ((int(pointerx) + 45) > int(x2) or ((int(pointery) + 20) > int(y2)))):
            errorWindow()
        else:
            canvas.coords(paintingWKS,int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20))
            canvas.coords(paintingWksLabel,pointerx,pointery)
            with open('activity log.txt', 'a') as the_file:
                the_file.write(TimeEntry1.get() + ":" + TimeEntry2.get() + " ")
                the_file.write("Painting " + " Coordinates: " + "(" + str(pointerx/2) + "," + str(pointery/2) + ")" + "\n")
    elif(str(workAreaMenu.get()) == "Painting" and (str(workStationMenu.get()) == "Frame Drying")):
        x1,y1,x2,y2 = canvas.coords(paintDept)
        if(((int(pointerx) - 45) < int(x1) ) or ((int(pointery) - 20) < int(y1)) or ((int(pointerx) + 45) > int(x2) or ((int(pointery) + 20) > int(y2)))):
            errorWindow()
        else:
            canvas.coords(dryingWKS,int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20))
            canvas.coords(dryingWksLabel,pointerx,pointery)
            with open('activity log.txt', 'a') as the_file:
                the_file.write(TimeEntry1.get() + ":" + TimeEntry2.get() + " ")
                the_file.write("Frame Drying " + " Coordinates: " + "(" + str(pointerx/2) + "," + str(pointery/2) + ")" + "\n")
    elif(str(workAreaMenu.get()) == "Module Asembly" and (str(workStationMenu.get()) == "Internal Assembly")):#
        x1,y1,x2,y2 = canvas.coords(moduleAssemblyDept)
        if(((int(pointerx) - 45) < int(x1) ) or ((int(pointery) - 20) < int(y1)) or ((int(pointerx) + 45) > int(x2) or ((int(pointery) + 20) > int(y2)))):
            errorWindow()
        else:
            canvas.coords(internalAssemblyWKS,int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20))
            canvas.coords(internalAssemWksLabel,pointerx,pointery)
            with open('activity log.txt', 'a') as the_file:
                the_file.write(TimeEntry1.get() + ":" + TimeEntry2.get() + " ")
                the_file.write("Internal Assembly " + " Coordinates: " + "(" + str(pointerx/2) + "," + str(pointery/2) + ")" + "\n")
    elif(str(workAreaMenu.get()) == "Module Asembly" and (str(workStationMenu.get()) == "External Assembly")):#
        x1,y1,x2,y2 = canvas.coords(moduleAssemblyDept)
        if(((int(pointerx) - 45) < int(x1) ) or ((int(pointery) - 20) < int(y1)) or ((int(pointerx) + 45) > int(x2) or ((int(pointery) + 20) > int(y2)))):
            errorWindow()
        else:
            canvas.coords(externalAssemblyWKS,int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20))
            canvas.coords(externalAssemWksLabel,pointerx,pointery)
            with open('activity log.txt', 'a') as the_file:
                the_file.write(TimeEntry1.get() + ":" + TimeEntry2.get() + " ")
                the_file.write("External Assembly " + " Coordinates: " + "(" + str(pointerx/2) + "," + str(pointery/2) + ")" + "\n")
    elif(str(workAreaMenu.get()) == "Machine Assembly" and (str(workStationMenu.get()) == "Machine Wiring")):#
        x1,y1,x2,y2 = canvas.coords(machineAssemblyDept)
        if(((int(pointerx) - 45) < int(x1) ) or ((int(pointery) - 20) < int(y1)) or ((int(pointerx) + 45) > int(x2) or ((int(pointery) + 20) > int(y2)))):
            errorWindow()
        else:
            canvas.coords(wiringWKS,int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20))
            canvas.coords(wiringWksLabel,pointerx,pointery)
            with open('activity log.txt', 'a') as the_file:
                the_file.write(TimeEntry1.get() + ":" + TimeEntry2.get() + " ")
                the_file.write("Machine Wiring " + " Coordinates: " + "(" + str(pointerx/2) + "," + str(pointery/2) + ")" + "\n")
    elif(str(workAreaMenu.get()) == "Machine Assembly" and (str(workStationMenu.get()) == "Welding Components Together")):#
        x1,y1,x2,y2 = canvas.coords(machineAssemblyDept)
        if(((int(pointerx) - 45) < int(x1) ) or ((int(pointery) - 20) < int(y1)) or ((int(pointerx) + 45) > int(x2) or ((int(pointery) + 20) > int(y2)))):
            errorWindow()
        else:
            canvas.coords(weldingWKS,int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20))
            canvas.coords(weldingWksLabel,pointerx,pointery)
            with open('activity log.txt', 'a') as the_file:
                the_file.write(TimeEntry1.get() + ":" + TimeEntry2.get() + " ")
                the_file.write("Welding Components Together " + " Coordinates: " + "(" + str(pointerx/2) + "," + str(pointery/2) + ")" + "\n")
    elif(str(workAreaMenu.get()) == "Machine Assembly" and (str(workStationMenu.get()) == "Installing the Casing")):#
        x1,y1,x2,y2 = canvas.coords(machineAssemblyDept)
        if(((int(pointerx) - 45) < int(x1) ) or ((int(pointery) - 20) < int(y1)) or ((int(pointerx) + 45) > int(x2) or ((int(pointery) + 20) > int(y2)))):
            errorWindow()
        else:
            canvas.coords(installCasingWKS,int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20))
            canvas.coords(installCasingWksLabel,pointerx,pointery)
            with open('activity log.txt', 'a') as the_file:
                the_file.write(TimeEntry1.get() + ":" + TimeEntry2.get() + " ")
                the_file.write("Installing the Casing " + " Coordinates: " + "(" + str(pointerx/2) + "," + str(pointery/2) + ")" + "\n")
    elif(str(workAreaMenu.get()) == "Quality Control" and (str(workStationMenu.get()) == "Conduct Quality Tests")):
        x1,y1,x2,y2 = canvas.coords(qualityControlDept)
        if(((int(pointerx) - 45) < int(x1) ) or ((int(pointery) - 20) < int(y1)) or ((int(pointerx) + 45) > int(x2) or ((int(pointery) + 20) > int(y2)))):
            errorWindow()
        else:
            canvas.coords(conductQualityTestingWKS,int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20))
            canvas.coords(conductQualityTestingWksLabel,pointerx,pointery)
            with open('activity log.txt', 'a') as the_file:
                the_file.write(TimeEntry1.get() + ":" + TimeEntry2.get() + " ")
                the_file.write("Conduct Quality Tests " + " Coordinates: " + "(" + str(pointerx/2) + "," + str(pointery/2) + ")" + "\n")
    elif(str(workAreaMenu.get()) == "Packaging" and (str(workStationMenu.get()) == "Packaging the Machines")):
        x1,y1,x2,y2 = canvas.coords(crateAndPackageDept)
        if(((int(pointerx) - 45) < int(x1) ) or ((int(pointery) - 20) < int(y1)) or ((int(pointerx) + 45) > int(x2) or ((int(pointery) + 20) > int(y2)))):
            errorWindow()
        else:     
            canvas.coords(packagingWKS,int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20))  
            canvas.coords(packagingWksLabel,pointerx,pointery)
            with open('activity log.txt', 'a') as the_file:
                the_file.write(TimeEntry1.get() + ":" + TimeEntry2.get() + " ")
                the_file.write("Packaging the Machines " + " Coordinates: " + "(" + str(pointerx/2) + "," + str(pointery/2) + ")" + "\n")
    elif(str(workAreaMenu.get()) == "Storage" and (str(workStationMenu.get()) == "Storing the Packaged Machines")):
        x1,y1,x2,y2 = canvas.coords(storageDept)
        if(((int(pointerx) - 45) < int(x1) ) or ((int(pointery) - 20) < int(y1)) or ((int(pointerx) + 45) > int(x2) or ((int(pointery) + 20) > int(y2)))):
            errorWindow()
        else:   
            canvas.coords(storageWKS,int(pointerx - 45), int(pointery - 20),int(pointerx + 45), int(pointery + 20))  
            canvas.coords(storageWksLabel,pointerx,pointery)
            with open('activity log.txt', 'a') as the_file:
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
        with open('activity log.txt', 'a') as the_file:
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

# #used to compare lines to find neighbors
# def compareLines(line1,line2):
#     x1,y1,x2,y2 = canvas.coords(line1)
#     x3,y3,x4,y4 = canvas.coords(line2)
#     x1 = int(x1)
#     y1 = int(y1)
#     x2 = int(x2)
#     y2 = int(y2)
#     x3 = int(x3)
#     y3 = int(y3)
#     x4 = int(x4)
#     y4 = int(y4)
#     if((abs(x1 - x3) <= 10) and ((abs(y1 - y3) <= 10))):
#         return True
#     elif((abs(x1 - x4) <= 10) and ((abs(y1 - y4) <= 10))):
#         return True
#     elif((abs(x2 - x3) <= 10) and ((abs(y2 - y3) <= 10))):
#         return True
#     elif((abs(x2 - x4) <= 10) and ((abs(y2 - y4) <= 10))):
#         return True
#     else:
#         return False
# lineGroup = []
# #function to group lines into neighbors
# def CumulateLines():
#     for line in lineDict:
#         for linenum2 in lineDict:
#             if(compareLines(line,linenum2) == True):
#                 lineGroup.append(tuple([line,linenum2]))


#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^Util Frame Creation^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
#This function is used to check if work areas are overlapping 
def checkOverlapArea():
    #loops 
    for area1 in workAreasArr:
        x1,y1,x2,y2 = canvas.coords(area1)
        for area2 in workAreasArr:
            if(area1 != area2):
                x3,y3,x4,y4 = canvas.coords(area1)
                x5 = x4
                y5 = y3
                x6 = x3
                y6 = y4
                if((x3 > x1) and (x3 < x2) and (y3 > y1) and (y3 < y2)):
                    return False
                elif((x4 > x1) and (x4 < x2) and (y4 > y1) and (y4 < y2)):
                    return False
                elif((x5 > x1) and (x5 < x2) and (y5 > y1) and (y5 < y2)):
                    return False
                elif((x6 > x1) and (x6 < x2) and (y6 > y1) and (y6 < y2)):
                    return False
                else:
                    print("here")
    return True

def checkOverlapAreaWKS():
    for area1 in workStationsArr:
        x1,y1,x2,y2 = canvas.coords(area1)
        for area2 in workStationsArr:
            if(area1 != area2):
                x3,y3,x4,y4 = canvas.coords(area1)
                x5 = x4
                y5 = y3
                x6 = x3
                y6 = y4
                if((x3 > x1) and (x3 < x2) and (y3 > y1) and (y3 < y2)):
                    return False
                elif((x4 > x1) and (x4 < x2) and (y4 > y1) and (y4 < y2)):
                    return False
                elif((x5 > x1) and (x5 < x2) and (y5 > y1) and (y5 < y2)):
                    return False
                elif((x6 > x1) and (x6 < x2) and (y6 > y1) and (y6 < y2)):
                    return False
    return True              
#########requirements list########
class Chord(Frame):
    '''Tkinter Frame with title argument'''

    def __init__(self, parent, title='', *args, **kw):
        Frame.__init__(self, parent, *args, **kw)
        self.title = title
#Accordion class for checklist
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
#Function that creates the requirements window
def create_window():
    window = tk.Toplevel(utilFrame)  
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
        #overlap req
        tenth_chord = Chord(acc, title='No Overlap:', bg='white')
        Label(tenth_chord, textvariable=areaOverlap, bg='white').pack()
        Label(tenth_chord, textvariable=workStationOverlap,bg='white').pack()
        # append list of chords to Accordion instance
        acc.append_chords([first_chord, second_chord, third_chord, fourth_chord, fifth_chord, sixth_chord, seventh_chord, eighth_chord, ninth_chord, tenth_chord])
        acc.pack(fill='both', expand=1)

        # Update Button
        update_button = Button(window, text='Update Checklist', command= update)
        update_button.pack()   
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
areaOverlap = StringVar()
workStationOverlap = StringVar()
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
def calcSize(entryNum1, entryNum2):
    if(entryNum1.get() == "" or entryNum1.get() == " " or entryNum2.get() == "" or entryNum2.get() == " "):
        return 0
    else:
        return int(str(entryNum1.get())) * int(str(entryNum2.get()))

def update(): #updates the checklist
    print("in checklist")
    counter = 0

    with open('checklist data.txt', 'a') as the_file:
             the_file.write(TimeEntry1.get() + ":" + TimeEntry2.get() +"\n")
    if(calcSize(sizeBox1x,sizeBox1y) >= 8000): #Frame Fabrication
        #ChecklistArr[6] = 1
        counter += 1 
        frameFabAreaText.set("At Least 8000 Square Feet ✔")   
    else:
        frameFabAreaText.set("At Least 8000 Square Feet") 
    if(calcSize(sizeBox2x,sizeBox2y) >= 6000): #Module Assembly
        #ChecklistArr[1] = 1
        counter += 1
        modAssemblyAreaText.set("At Least 6000 Square Feet ✔") 
    else:
        modAssemblyAreaText.set("At Least 6000 Square Feet ")
    if(calcSize(sizeBox3x,sizeBox3y) >= 7000): #Machine Assembly
        counter += 1
        machAssemblyAreaText.set(" At Least 7000 Square Feet ✔")
        #ChecklistArr[3] = 1
    else:
        machAssemblyAreaText.set(" At Least 7000 Square Feet ")
    # if(calcSize(entry19,entry20) >= 7000): #Paint
    #     ChecklistArr[5] = 1
    #     paintText.set("At Least 7000 Square Feet ✔")
    # else:
    #     paintText.set("At Least 400 Square Feet ")
    # if(calcSize(entry23,entry24) >= 300): #Receiving Department
    #     ChecklistArr[0] = 1
    #     recDepText.set("At Least 300 Square Feet ✔")
    # else:
    #     recDepText.set("At Least 300 Square Feet ")
    if(calcSize(sizeBox4x,sizeBox4y) >= 5000): #Quality Control
        #ChecklistArr[8] = 1
        counter += 1
        qualControlText.set("At Least 5000 Square Feet ✔")
    else:
        qualControlText.set("At Least 5000 Square Feet ") 
    if(calcSize(sizeBox5x,sizeBox5y) >= 5000): #Packaging
        #ChecklistArr[9] = 1
        counter += 1
        packgText.set("At Least 5000 Square Feet ✔")
    else:
        packgText.set("At Least 5000 Square Feet")
    if(calcSize(sizeBox6x,sizeBox6y) >= 5000): #Storage
        #ChecklistArr[10] = 1
        counter += 1
        storageText.set("At Least 5000 Square Feet ✔")
    else:
        storageText.set("At Least 5000 Square Feet")
    # if(calcSize(entry39,entry40) >= 300): #Loading Department
    #     ChecklistArr[11] = 1
    #     loadingDepText.set( "At Least 300 Square Feet ✔")
    # else:
    #     loadingDepText.set("At Least 300 Square Feet")
    if(checkOverlapArea() == True):
        counter += 1
        areaOverlap.set("No Works Areas are Overlapping ✔")
    else:
        areaOverlap.set("No Works Areas are Overlapping")
    if(checkOverlapAreaWKS() == True):
        counter += 1
        workStationOverlap.set("No Works Stations are Overlapping ✔")
    else:
        workStationOverlap.set("No Works Stations are Overlapping")
    with open('checklist data.txt', 'a') as the_file:
   
        the_file.write("Completed: " + str(counter) + "/8")
    totalcounter.set("Completed: " + str(counter) + "/8")       
#Widgits
clockUtil1 = ttk.Entry(utilFrame, textvariable = TimeEntry1 ,width=10)#shows the mins
clockUtil2 = ttk.Entry(utilFrame, textvariable = TimeEntry2 ,width=10)#shows the secs
lb = tk.Label(utilFrame, text = ':' )#colon for separation of sec and min
stbtn = ttk.Button(utilFrame, width=10, text= 'start', command = st)
stpbtn = ttk.Button(utilFrame, width=10, text= 'stop', command = stp)
reqbtn= ttk.Button(utilFrame, text="Open Requirements Window", command = create_window)
distBtn = ttk.Button(utilFrame,text="Total Distance", command = getDistance2)
clockUtil1.grid(row=0,column=0)
lb.grid(row=0,column=1)
clockUtil2.grid(row=0,column=2)
stbtn.grid(row=1,column=0)
stpbtn.grid(row=1,column=2)
reqbtn.grid(row=2,column=0,columnspan=3)
distBtn.grid(row=2,column=4)
#***************************End of Program********************************************#
#packs in tabs to frame
notebook.pack(expand = 1, fill = 'both')
#End Loop
root.mainloop()
