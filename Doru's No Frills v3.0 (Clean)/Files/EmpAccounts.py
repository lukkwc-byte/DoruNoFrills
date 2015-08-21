'''
Ben - Oct 18, 2011 - Finished the Gui Setup of the screen
Ben - Oct 19, 2011 - Implemented Kyuho's AddAccount Module and updated GUI
Ben - Oct 20, 2011 - Finished implementing Kyuho's Module and finished implementing Justin's Module (Justin's Module needs fixing)
Ben - Oct 27, 2011 - Finished Error Proofing
Ben - Oct 28, 2011 - Made entries refresh
Ben - Oct 31, 2011 - (Halloween Update) - Added and finished display and display-related functions
Ben - Nov 2, 2011 - Fixed the spacing for the display and label
Ben - Nov 4, 2011 - Finished the security question and answer implementation
'''

#Make a Security Question and Security answer stuff


from Tkinter import *
from Swampy.Gui import * # Handles Graphics
from Modules.AddAccount import *
from Modules.DeleteAccount import *
import AccountErrorPopup
import Modules.AccountsDisplay
from Modules.ReadCSV import *
import Modules.Check

def add_account(self):
    list1 = add_into_list(self)
    list2 = ReadAccountsCSV(list1)
    list3 = AddAccount(list2)
    if list3[0] == False:
        errorcodes(list3[1])
        return False
    else:
        self.EmpAccounts.LeftSide.Left1.UserEntry.config(state='normal')
        RefreshEntries(self)
        RefreshDisplay(self)
        return True

def edit_account(self):
    ai = Modules.Check.editacct
    ReadDelAccountsCSV(ai)
    addtest = add_account(self)
    if addtest == True:
        change_back(self)   

def change_to(self):   
    try:
        ai = int(self.EmpAccounts.Display.curselection()[0])
        self.EmpAccounts.LeftSide.Left2.AddAcc.config(text='Save', command = Callable(edit_account, self))
        self.EmpAccounts.LeftSide.Left2.EditAcc.config(text='Cancel', command = Callable(change_back, self))
        self.EmpAccounts.LeftSide.Left2.DelAcc.config(state='disabled') 
        acctlist = Account_Read()
        self.EmpAccounts.LeftSide.Left1.UserEntry.config(state='normal')
        RefreshEntries(self)
        self.EmpAccounts.LeftSide.Left1.UserEntry.insert('end', acctlist[0][ai+1])
        self.EmpAccounts.LeftSide.Left1.UserEntry.config(state='readonly')

        self.EmpAccounts.LeftSide.Left1.PassEntry.insert('end', acctlist[1][ai+1])
        self.EmpAccounts.LeftSide.Left1.LevelEntry.insert('end', acctlist[2][ai+1])
        if Modules.Check.loggeduser == acctlist[0][ai+1]:   
            self.EmpAccounts.LeftSide.Left1.LevelEntry.config(state='readonly')
        self.EmpAccounts.LeftSide.Left1.WageEntry.insert('end', acctlist[3][ai+1])
        self.EmpAccounts.LeftSide.Left1.SecQEntry.insert('end', acctlist[4][ai+1])
        self.EmpAccounts.LeftSide.Left1.SecAEntry.insert('end', acctlist[5][ai+1])
        Modules.Check.editacct = acctlist[0][ai+1]
    except:
        errorcodes(22)

def change_back(self):
    self.EmpAccounts.LeftSide.Left2.AddAcc.config(text='Add Account', command = Callable(add_account, self))
    self.EmpAccounts.LeftSide.Left2.EditAcc.config(text='Edit Account', command = Callable(change_to, self))
    self.EmpAccounts.LeftSide.Left2.DelAcc.config(state='normal') 
    self.EmpAccounts.LeftSide.Left1.UserEntry.config(state='normal')
    self.EmpAccounts.LeftSide.Left1.LevelEntry.config(state='normal')
    RefreshEntries(self)


def errorcodes(error_testing):
    AccountErrorPopup.Create(error_testing)
    
def del_account(self):
    try:
        ai = int(self.EmpAccounts.Display.curselection()[0])
        acctlist = Account_Read()
        if Modules.Check.loggeduser != acctlist[0][ai+1]:
            ReadDelAccountsCSV(acctlist[0][ai+1])
        else:
            errorcodes(23)            
        self.EmpAccounts.LeftSide.Left1.UserEntry.config(state='normal')
        RefreshEntries(self)
        RefreshDisplay(self)
        change_back(self)
    except:
        errorcodes(22)

def add_into_list(self):
    new_list=[]
    UserName=self.EmpAccounts.LeftSide.Left1.UserEntry.get()
    new_list.append(UserName)
    PassWord=self.EmpAccounts.LeftSide.Left1.PassEntry.get()    
    new_list.append(PassWord)
    UserLevel=self.EmpAccounts.LeftSide.Left1.LevelEntry.get()    
    new_list.append(UserLevel)
    HourWage=self.EmpAccounts.LeftSide.Left1.WageEntry.get()
    new_list.append(HourWage)

    Secure1 = self.EmpAccounts.LeftSide.Left1.SecQEntry.get()
    new_list.append(Secure1)

    Secure2 = self.EmpAccounts.LeftSide.Left1.SecAEntry.get()
    new_list.append(Secure2)

    return(new_list)
def RefreshEntries(self):
    self.EmpAccounts.LeftSide.Left1.UserEntry.delete(0, 'end')
    self.EmpAccounts.LeftSide.Left1.PassEntry.delete(0, 'end')
    self.EmpAccounts.LeftSide.Left1.LevelEntry.delete(0, 'end')
    self.EmpAccounts.LeftSide.Left1.WageEntry.delete(0, 'end')
    self.EmpAccounts.LeftSide.Left1.SecQEntry.delete(0, 'end')
    self.EmpAccounts.LeftSide.Left1.SecAEntry.delete(0, 'end')

def RefreshDisplay(self):
    Modules.AccountsDisplay.ClearDisplay(self)
    Modules.AccountsDisplay.FillDisplay(self)

def Create(self):
    #self.EmpAccounts = self.gr(cols = 2)
    #Need to use a row instead
    self.EmpAccounts = self.row([1, 0])
    self.EmpAccounts.LeftSide = self.gr(cols = 1)
    self.EmpAccounts.LeftSide.topspace = self.la(height=1)
    self.EmpAccounts.LeftSide.Left1 = self.gr(cols = 2)
    self.EmpAccounts.LeftSide.Left1.UserLabel = self.la(text = 'Username:', font = ('Calibri, 14'), padx=10, pady=5, width=20)
    self.EmpAccounts.LeftSide.Left1.UserEntry = self.en(font='Calibri, 13', padx=10, pady=5, highlightthickness = 2, highlightcolor = '#4f81bd', width=20)
    self.EmpAccounts.LeftSide.Left1.PassLabel = self.la(text = 'Password:', font = ('Calibri, 14'), padx=10, pady=5, width=20)
    self.EmpAccounts.LeftSide.Left1.PassEntry = self.en(font='Calibri, 13', padx=10, pady=5, show='*', highlightthickness = 2, highlightcolor = '#4f81bd', width=20)
    self.EmpAccounts.LeftSide.Left1.LevelLabel = self.la(text = 'User Level:', font = ('Calibri, 14'), padx=10, pady=5, width=20)
    self.EmpAccounts.LeftSide.Left1.LevelEntry = self.en(font='Calibri, 13', padx=10, pady=5, highlightthickness = 2, highlightcolor = '#4f81bd', width=20)
    self.EmpAccounts.LeftSide.Left1.WageLabel = self.la(text = 'Hourly Wage:', font = ('Calibri, 14'), padx=10, pady=5, width=20)
    self.EmpAccounts.LeftSide.Left1.WageEntry = self.en(font='Calibri, 13', padx=10, pady=5, highlightthickness = 2, highlightcolor = '#4f81bd', width=20)
    self.EmpAccounts.LeftSide.Left1.SecQLabel = self.la(text = 'Security Question:', font = ('Calibri, 14'), padx=10, pady=5, width=20)
    self.EmpAccounts.LeftSide.Left1.SecQEntry = self.en(font='Calibri, 13', padx=10, pady=5, highlightthickness = 2, highlightcolor = '#4f81bd', width=20)
    self.EmpAccounts.LeftSide.Left1.SecALabel = self.la(text = 'Security Answer:', font = ('Calibri, 14'), padx=10, pady=5, width=20)
    self.EmpAccounts.LeftSide.Left1.SecAEntry = self.en(font='Calibri, 13', padx=10, pady=5, highlightthickness = 2, highlightcolor = '#4f81bd', width=20)

    self.row(pady=17)
    self.endrow()
    self.endgr()

    self.EmpAccounts.LeftSide.Left2 = self.gr(cols = 1)
    self.EmpAccounts.LeftSide.Left3 = self.gr(cols = 1)
    self.EmpAccounts.LeftSide.Left2.AddAcc = self.bu(text='Add Account', bg='#47c57f', padx=10, pady=10, height = 1, width = 12, font = 'Calibri, 14', command = Callable(add_account, self))
    self.endrow()
    self.EmpAccounts.LeftSide.Left4 = self.gr(cols = 2)
    self.EmpAccounts.LeftSide.Left2.EditAcc = self.bu(text='   Edit Account   ', bg='#4f81bd', padx=10, pady=10, height = 1, width = 12, font = 'Calibri, 14', command = Callable(change_to, self))
    self.EmpAccounts.LeftSide.Left2.DelAcc = self.bu(text='Delete Account', bg='#d94444', padx=10, pady=10, height = 1, width = 12, font = 'Calibri, 14', command = Callable(del_account, self))
    self.endrow()

    self.endgr()

    self.row(pady=9)
    self.endrow()
    
    self.EmpAccounts.MiniLogo = Tkinter.PhotoImage(file='Files\Images\SmallLogo.gif')    
    self.EmpAccounts.LeftSide.MiniLogoAcc = self.la(image=self.EmpAccounts.MiniLogo)    
    self.EmpAccounts.LeftSide.CopyrightAcc = self.la(text='Copyright (c) Doru Solutions 2011', pady=10, font='Calibri, 12')
    self.EmpAccounts.LeftSide.EmpAccountsSpacer4 = self.la(height=1)
    self.endgr()

    self.EmpAccounts.Display = self.gr(cols = 2)
    self.EmpAccounts.Display.DisUserLabel = self.la(text='Username                             Password                            User Level                               Hourly Wage                             ', bg='#404040', fg='White', font=('Calibri', 11), height=1)
    self.EmpAccounts.Display.ScrollSpacer = self.la()
    self.EmpAccounts.Display = self.lb(height = 33, width = 56,font=('Courier'))
    self.EmpAccounts.Display.Scroll = self.sb(command=self.EmpAccounts.Display.yview)
    self.EmpAccounts.Display.config(yscrollcommand=self.EmpAccounts.Display.Scroll.set)
    Modules.AccountsDisplay.FillDisplay(self)
    #self.EmpAccounts.Display.fakelabel = self.la(height=5)
    self.endgr()

    self.endcol()
    
