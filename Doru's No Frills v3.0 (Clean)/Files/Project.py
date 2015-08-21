''' File Log:
    Version 0.01 22/09/2011 Jonathan (Testing)
    Version 0.02 24/09/2011 Jonathan (Implementation of Navigation Module)
    Version ALPHA 27/09/2011 Jonathan (Linking of Cash Register, Login, Inventory Stock)
    Version 0.04 28/09/2011 Jonathan (Debug mode implemented)
    Version 0.05 03/10/2011 Jonathan (Folder path)
    Version 0.06 08/10/2011 Jonathan (Status Bar integration)
    Version 0.07 09/12/2011 Jonathan (Login window centering)

'''
from Tkinter import *
from Swampy.Gui import * # Handles Graphics
import Login
import WelcomeScreen
import MenuBar
import Modules.Check
import StatusBar
import Setup
import StoreSettings
from Modules.ReadCSV import *

def CreateProject(self):
    Users=Account_Read()
    del Users[0][0], Users[1][0], Users[2][0], Users[3][0], Users[4][0], Users[5][0]
    if Users != [[], [], [], [], [], []]:            
        self = Gui(debug=False)
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw/2) - (450/2) 
        y = (sh/2) - (350/2)
        self.geometry('%dx%d+%d+%d' % (450, 350, x, y))
        self.resizable(width=False, height=False)
        self.maxsize(width=1024, height=768)
        self.maincol = self.col(weights=[0,0,0,1]) # Resizing of Windows
        Login.Create(self)
        self.mainloop()
    else:
        CreateSetup(self)

def CreateDebug(self):
    self = Gui(debug=False)
    self.resizable(width=False, height=False)
    self.maxsize(width=1024, height=768)
    self.maincol = self.col(weights=[0,0,1]) # Resizing of Windows
    MenuBar.Create(self)
    self.title('Doru\'s No Frills - Welcome')
    StatusBar.Create(self)
    WelcomeScreen.Create(self)
    Modules.Check.openwindow = "WelcomeScreen"
    self.mainloop()

def CreateSettings(self):
    self = Gui(debug=False)
    self.resizable(width=False, height=False)
    self.maxsize(width=1024, height=768)
    self.maincol = self.col(weights=[0,0,1]) # Resizing of Windows
    MenuBar.Create(self)
    self.title('Doru\'s No Frills - Store Settings')
    StatusBar.Create(self)
    StoreSettings.Create(self)
    Modules.Check.openwindow = "Store Settings"
    self.mainloop()

def CreateSetup(self):
    self = Gui(debug=False)
    sw = self.winfo_screenwidth()
    sh = self.winfo_screenheight()
    x = (sw/2) - (500/2) 
    y = (sh/2) - (260/2)
    self.geometry('%dx%d+%d+%d' % (500, 260, x, y))
    self.resizable(width=False, height=False)
    Setup.Create(self)
    self.mainloop()

