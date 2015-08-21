''' File Log:
    Version 0.01 22/12/2011 Jonathan (started GUI)

'''

from Swampy.Gui import *                   
from Tkinter import *
import Modules.Check
from Modules.AddAccount import *
from Modules.DeleteAccount import *
import AccountErrorPopup
import Modules.AccountsDisplay
import tkMessageBox
from Modules.AddItemToInventory import *
from Modules.RemoveItemFromInventory import *
from Modules.AddCSVToInventory import *
import InvErrorPopup
import Modules.InventoryDisplay
import Project


def Create(self):
    Modules.Check.login_error=False
    Modules.Check.openwindow = "Setup"
    self.title('Doru\'s No Frills - Store Setup')
    self.Setup = self.col()
    self.Setup.focus_force()
    self.Setup.logospace=self.la(height=1)
    self.Setup.logo=Tkinter.PhotoImage(file='Files\Images\SetupLogo.gif')
    self.Setup.labellogo=self.la(image=self.Setup.logo)

    self.Setup.instruct=self.la(font = 'Calibri,12',text='This wizard is designed to help you set-up your store.\nUse the directional arrows to move between setup screens.')
    self.Setup.arrowrow = self.row(weights=[1,1,0])
    self.Setup.arrowrsep = self.la(width=23)
    self.Setup.rarrow=Tkinter.PhotoImage(file='Files\Images\RArrow.gif')
    self.Setup.rarrowbu=self.bu(image=self.Setup.rarrow, justify='right', command=Callable(Screen2,self), bd=0, pady=2)
    self.endrow()
    self.protocol("WM_DELETE_WINDOW", Callable(shutdown, self))

def shutdown(self):
    tkMessageBox.showwarning("Attention", 'Please complete the setup process in its entierty!') # Show error in box


def Screen2(self):
    self.Setup.arrowrow.destroy()
    self.Setup.arrowrsep.destroy()
    self.Setup.rarrowbu.destroy()

    sw = self.winfo_screenwidth()
    sh = self.winfo_screenheight()
    x = (sw/2) - (500/2) 
    y = (sh/2) - (460/2)
    self.geometry('%dx%d+%d+%d' % (500, 460, x, y))

    self.Setup.instruct.config(text='Please set up an administrator account for the store.\nBe sure to write down your account information!')
    self.Setup.entrygrid = self.gr(cols=4)
    self.Setup.entrygrid.sepr = self.la(width=10)    
    self.Setup.entrygrid.UserLabel = self.la(text = 'Username:', pady=2, font = ('Calibri, 12'))
    self.Setup.entrygrid.UserEntry = self.en(pady=2, highlightthickness = 2, highlightcolor = '#4f81bd')
    self.Setup.entrygrid.sepr = self.la(width=10)
    self.Setup.entrygrid.sepr = self.la(width=10)    
    self.Setup.entrygrid.PassLabel = self.la(text = 'Password:', font = ('Calibri, 12'), pady=2)
    self.Setup.entrygrid.PassEntry = self.en(font='Calibri, 13', pady=2, show='*', highlightthickness = 2, highlightcolor = '#4f81bd')
    self.Setup.entrygrid.sepr = self.la(width=10)
    self.Setup.entrygrid.sepr = self.la(width=10)    
    self.Setup.entrygrid.LevelLabel = self.la(text = 'User Level:', font = ('Calibri, 12'), pady=2)
    self.Setup.entrygrid.LevelEntry = self.en(text='1', font='Calibri, 13', pady=2, highlightthickness = 2, highlightcolor = '#4f81bd')
    self.Setup.entrygrid.LevelEntry.config(state='readonly')
    self.Setup.entrygrid.sepr = self.la(width=10)
    self.Setup.entrygrid.sepr = self.la(width=10)    
    self.Setup.entrygrid.WageLabel = self.la(text = 'Hourly Wage:', font = ('Calibri, 12'), pady=2)
    self.Setup.entrygrid.WageEntry = self.en(font='Calibri, 13', pady=2, highlightthickness = 2, highlightcolor = '#4f81bd')
    self.Setup.entrygrid.sepr = self.la(width=10)
    self.Setup.entrygrid.sepr = self.la(width=10)    
    self.Setup.entrygrid.SecQLabel = self.la(text = 'Security Question:', font = ('Calibri, 12'), pady=2)
    self.Setup.entrygrid.SecQEntry = self.en(font='Calibri, 13', pady=2, highlightthickness = 2, highlightcolor = '#4f81bd')
    self.Setup.entrygrid.sepr = self.la(width=10)
    self.Setup.entrygrid.sepr = self.la(width=10)    
    self.Setup.entrygrid.SecALabel = self.la(text = 'Security Answer:', font = ('Calibri, 12'), pady=2)
    self.Setup.entrygrid.SecAEntry = self.en(font='Calibri, 13', pady=2, highlightthickness = 2, highlightcolor = '#4f81bd')
    self.Setup.entrygrid.sepr = self.la(width=10)    
    self.endgr()

    self.Setup.arrowrow = self.row(weights=[1,1,0])
    self.Setup.arrowrsep = self.la(width=23)
    self.Setup.rarrow=Tkinter.PhotoImage(file='Files\Images\RArrow.gif')
    self.Setup.rarrowbu=self.bu(image=self.Setup.rarrow, justify='right', command=Callable(Screen3,self), bd=0)
    self.endrow()

def Screen3(self):
    list3 = AccountSetup(self)
    if list3[0] == False:
        errorcodes(list3[1])
    else:
        tkMessageBox.showwarning("Success!", 'The account has been created successfully!') # Show error in box
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw/2) - (500/2) 
        y = (sh/2) - (400/2)
        self.geometry('%dx%d+%d+%d' % (500, 400, x, y))

        self.Setup.arrowrow.destroy()
        self.Setup.arrowrsep.destroy()
        self.Setup.rarrowbu.destroy()
        self.Setup.entrygrid.destroy()
        self.Setup.instruct.destroy()
        self.Setup.topla = self.la()
        self.Setup.instruct = self.la(font = 'Calibri,12', text='You may now import an inventory database\nfrom a previous back-up (optional)\n\n******* Do not include ".csv" in the filename *******')
        self.Setup.instructsep = self.la()        
        self.Setup.entrygrid = self.gr(cols=4)
        self.Setup.entrygrid.sepr = self.la(width=10)    
        self.Setup.entrygrid.CSVLabel = self.la(text = '.CSV File Name:', pady=2, font = ('Calibri, 12'))
        self.Setup.entrygrid.CSVEntry = self.en(pady=2, highlightthickness = 2, highlightcolor = '#4f81bd')
        self.Setup.entrygrid.sepr = self.la(width=10)
        self.endgr()

        self.Setup.buttrow = self.row()
        self.Setup.buttrow.okbutt = self.bu(text='Import', command=Callable(Screen4, self, True),bg= '#47c57f',pady=40, padx=20, font='Calibri, 14', )
        self.Setup.buttrow.skipbutt = self.bu(text='Skip', command=Callable(Screen4, self, False),bg= '#d94444',pady=40, padx=20, font='Calibri, 14', )
        self.endrow()

def add_csv(self):                              
    CSV_Name = self.Setup.entrygrid.CSVEntry.get()
    list1 = inv_ImportCSV(CSV_Name)
    return list1


def functionname(error_testing):
    InvErrorPopup.Create(error_testing)

def Screen4(self, arg):
    if arg == True:
        list3=add_csv(self)
        if list3 != None:
            functionname(list3[0])
        else:
            tkMessageBox.showwarning("Success!", 'The inventory has been imported successfully!') # Show error in box
            FinalScreen(self)
    if arg == False:
        FinalScreen(self)

def FinalScreen(self):
    self.Setup.arrowrow.destroy()
    self.Setup.arrowrsep.destroy()
    self.Setup.rarrowbu.destroy()
    self.Setup.entrygrid.destroy()
    self.Setup.buttrow.destroy()
    self.Setup.topla.destroy()
    self.Setup.instructsep.destroy()  
    
    sw = self.winfo_screenwidth()
    sh = self.winfo_screenheight()
    x = (sw/2) - (500/2) 
    y = (sh/2) - (300/2)
    self.geometry('%dx%d+%d+%d' % (500, 300, x, y))
    self.Setup.instruct.config(text='Congratulations! The setup process is complete.\nShould you wish to make any changes, please launch\nthe "Store Settings" screen from the main program.')
    self.Setup.okbutt = self.bu(text='Proceed to Login', command=Callable(ProceedLogin, self),bg= 'yellow', padx=50, font='Calibri, 12', )
    self.Setup.loginsep = self.la()

def ProceedLogin(self):
    self.destroy()
    Project.CreateProject('NoFrills')


def errorcodes(error_testing):
    AccountErrorPopup.Create(error_testing)

def AccountSetup(self):
    list1 = add_into_list(self)
    list2 = ReadAccountsCSV(list1)
    list3 = AddAccount(list2)
    return list3

def add_into_list(self):
    new_list=[]
    UserName=self.Setup.entrygrid.UserEntry.get()
    new_list.append(UserName)
    PassWord=self.Setup.entrygrid.PassEntry.get()    
    new_list.append(PassWord)
    UserLevel=self.Setup.entrygrid.LevelEntry.get()    
    new_list.append(UserLevel)
    HourWage=self.Setup.entrygrid.WageEntry.get()
    new_list.append(HourWage)

    Secure1 = self.Setup.entrygrid.SecQEntry.get()
    new_list.append(Secure1)

    Secure2 = self.Setup.entrygrid.SecAEntry.get()
    new_list.append(Secure2)

    return(new_list)
