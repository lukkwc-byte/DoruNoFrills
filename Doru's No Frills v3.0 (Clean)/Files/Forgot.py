'''Ben - Nov 14, 2011 - Forgot Pass was created, GUI started
Ben - Nov 15, 2011 - Gui Finished
Ben - Nov 16, 2011 - CheckUser and CheckAns finished
Ben - Nov 17, 2011 - CloseDown and error proofing
Ben - Nov 22, 2011 - Random 6 character password is created and is used as the desired user's temporary password until they go into Change Pass and change it themselves instead of the program just giving them their old password
'''

import tkMessageBox
from Tkinter import *
from Swampy.Gui import *
import csv
from Modules.ReadCSV import *
from Modules.WriteCSV import *
import random
import Modules.Check
import Project

screen='1'
index=0
Password=[]

def CreateForgot():
    Modules.Check.openwindow = 'Password Recovery'
    global Password
    self = Gui(debug=False)
    sw = self.winfo_screenwidth()
    sh = self.winfo_screenheight()
    x = (sw/2) - (450/2) 
    y = (sh/2) - (175/2)
    self.geometry('%dx%d+%d+%d' % (450, 175, x, y))
    self.resizable(width=False, height=False)
    self.title('Password Recovery')
    self.row()
    self.label = self.la('Username:', font='Calibri',pady=15, padx=15, justify=CENTER, width='5')
    self.entry = self.en(padx=15, pady=15)
    self.endrow()
    self.row()
    self.okbutt = self.bu('OK', font='Calibri',pady=15, padx=15, background='yellow', justify=CENTER,  command=Callable(CheckUser, self))
    self.canbutt = self.bu('Cancel', font='Calibri',pady=15, padx=15, background='red', justify=CENTER,  command=Callable(CheckUser, self))
    self.endrow()
    self.mainloop()


def CheckUser(self, Event=None):
    global screen
    global index
    global Password
    found = 0
    Accountlist=Account_Read()
    UserList = Accountlist[0][1:]
    user = self.entry.get()
    Password=''
    for i in range(len(UserList)):
        if UserList[i] == user:
            screen='2'
            index=i            
            found=1
            break
    Question = Accountlist[4][index+1]
    if found==1:
        self.entry.delete(0, 'end')     
        self.label.config(text=Question, font = ('Calibri', '16', 'bold'))
        self.okbutt.config(command=Callable(CheckAns, self))
    elif found==0:
        self.entry.delete(0, 'end')    
        tkMessageBox.showwarning('Error', 'That is not a used username')
    return self
def CheckAns(self, Event=None):
    global screen
    global index
    global Password
    global EntryAns
    Accountlist=Account_Read()
    RealAns = Accountlist[5][index+1]
    EntryAns = self.entry.get()
    Pass = random.sample(['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','1','2','3','4','5','6','7','8','9','0'], 6)
    for i in range(len(Pass)):
        Password = Password+Pass[i]

    if EntryAns==RealAns:
        screen='3'
        self.destroy()
        self = Gui(debug=False)
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw/2) - (450/2) 
        y = (sh/2) - (175/2)
        self.geometry('%dx%d+%d+%d' % (450, 175, x, y))
        self.resizable(width=False, height=False)
        self.title('Password Recovery')
        self.passla=self.la(text='Your New Password Is...', font = ('Calibri', '20', 'bold'))
        self.passen = self.la(text=Password)
        self.Passla2 =self.la(font=('Calibri', '10', 'italic'), text='Be sure to copy your new password! \n After you log in, you may go to the \'Change Password\' screen \n to get a new password.')
        self.okbutt =self.bu(text='Confirm Password Change', font = ('Calibri', '12', 'bold'), padx=15, bg='#799AA5', command=Callable(CloseDown, self))
    elif EntryAns!=RealAns:
        self.entry.delete(0, 'end')
        tkMessageBox.showwarning('Error', 'Your security answer was not correct')
    return self
def CloseDown(self, Event=None):
    global screen
    global Password
    global index
    i = index+1
    Accountlist=Account_Read()
    
    usernamelist= Accountlist[0]
    passwordlist= Accountlist[1]
    userlevellist= Accountlist[2]
    hourlywagelist= Accountlist[3]
    secureQ = Accountlist[4]
    secureA = Accountlist[5]
    passwordlist[i]=Password
    returnlist=[usernamelist,passwordlist,userlevellist,hourlywagelist,secureQ,secureA]
    AddIntoCSV(returnlist)
    Modules.Check.openwindow = 'Login'
    self.destroy()
def AddIntoCSV(lis):
    if len(lis) != 1:
        csvfile = 'Files\Modules\Database\useraccounts.csv'
        WriteCSV(lis, csvfile)
        return [True]
    else:
        return False, lis[0] 

def CreateLogin(self, Event=None):
    self.destroy()
    Project.CreateProject()
