''' File Log:
    Version 0.01 27/09/2011 Kevin (GUI + Login Logic)
    Version ALPHA 27/09/2011 Jonathan (Link to Navigation, edit GUI + Errors)
    Version 0.03 05/10/2011 Kevin (Updated GUI, Logic)
    Version 0.04 08/10/2011 Jonathan (Added Userlevel Logic, StatusBar integration)
    Version 0.05 11/10/2011 Ben (Added Forgot Password button)
    Version 0.06 22/12/2011 Jonathan (Merged "Forgot" with login. final formatting)
    
'''

import csv
import Modules.ValidateLogic
from Swampy.Gui import *                   
from Tkinter import *
import Modules.Check
import MenuBar
import StatusBar
import WelcomeScreen
from Forgot import *
from Modules.ReadCSV import *
import Modules.Check
import LoginErrorPopup

index=0
Password=[]

def Create(self):
    Modules.Check.openwindow = "Login"
    self.title('Doru\'s No Frills - Login')
    self.Login = self.col()
    self.Login.focus_force()
    self.Login.logospace=self.la(height=1)
    self.Login.logo=Tkinter.PhotoImage(file='Files\Images\Logo.gif')
    self.Login.labellogo=self.la(image=self.Login.logo)
    self.Login.label5=self.la(pady=4)
    self.Login.grid = self.gr(cols=4)
    self.Login.label7=self.la(pady=2)
    self.Login.userlabel=self.la(text='Username:', font='Calibri', fg= 'black')
    self.Login.userentry=self.en(justify=LEFT, text='', width=3, pady=3)
    self.Login.label1=self.la(pady=2)
    self.Login.label2=self.la(pady=2)
    self.Login.passwordlabel=self.la(text='Password:', font='Calibri', fg= 'black')
    self.Login.passentry=self.en(justify=LEFT, text='', width=3, pady=3, show='*')
    self.Login.label3=self.la()
    self.Login.label4=self.la()
    self.endgr()
    self.Login.grid2=self.gr(cols=3,pady=1)
    self.Login.label9=self.la()
    self.Login.button = self.bu(text='Login', font= 'Calibri', width=4, command=Callable(ValidateLogin, self), background='yellow')    
    self.Login.label10=self.la()
    self.endgr()
    self.Login.label11=self.la(height=1)   
    self.Login.button2 = self.bu(text='Forgot Password?...', font= ( 'Calibri', '11', 'underline'), width=4, padx=150, fg='red', borderwidth=0, command=Callable(ForgotPass, self))
    self.Login.label12=self.la(height=1)    
    # Not Functioning // self.bind('<Return>', ValidateLogin)

def LoginCr(self):
    self.Login.instruction.destroy()
    self.Login.sep1.destroy()
    self.Login.grid.destroy()
    self.Login.label7.destroy()
    self.Login.userlabel.destroy()
    self.Login.userentry.destroy()
    self.Login.label1.destroy()
    self.Login.label2.destroy()
    self.Login.grid2.destroy()
    self.Login.label9.destroy()
    self.Login.button.destroy() 
    self.Login.label10.destroy()
    self.Login.label11.destroy()  
    self.Login.button2.destroy()
    self.Login.label12.destroy()

    Modules.Check.openwindow = "Login"
    self.title('Doru\'s No Frills - Login')
    self.Login.label5=self.la(pady=4)
    self.Login.grid = self.gr(cols=4)
    self.Login.label7=self.la(pady=2)
    self.Login.userlabel=self.la(text='Username:', font='Calibri', fg= 'black')
    self.Login.userentry=self.en(justify=LEFT, text='', width=3, pady=3)
    self.Login.label1=self.la(pady=2)
    self.Login.label2=self.la(pady=2)
    self.Login.passwordlabel=self.la(text='Password:', font='Calibri', fg= 'black')
    self.Login.passentry=self.en(justify=LEFT, text='', width=3, pady=3, show='*')
    self.Login.label3=self.la()
    self.Login.label4=self.la()
    self.endgr()
    self.Login.grid2=self.gr(cols=3,pady=1)
    self.Login.label9=self.la()
    self.Login.button = self.bu(text='Login', font= 'Calibri', width=4, command=Callable(ValidateLogin, self), background='yellow')    
    self.Login.label10=self.la()
    self.endgr()
    self.Login.label11=self.la(height=1)   
    self.Login.button2 = self.bu(text='Forgot Password?...', font= ( 'Calibri', '11', 'underline'), width=4, padx=150, fg='red', borderwidth=0, command=Callable(ForgotPass, self))
    self.Login.label12=self.la(height=1)

def PassShutdown(self):
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
    
    self.Login.instruction.destroy()
    self.Login.sep1.destroy()
    self.Login.grid.destroy()
    self.Login.label7.destroy()
    self.Login.userlabel.destroy()
    self.Login.userentry.destroy()
    self.Login.label1.destroy()
    self.Login.label2.destroy()
    self.Login.grid2.destroy()
    self.Login.label9.destroy()
    self.Login.button.destroy() 
    self.Login.label10.destroy()
    self.Login.label11.destroy()  
    self.Login.button2.destroy()
    self.Login.label12.destroy()
    self.Login.userlabel.destroy()       
    self.Login.Passla2.destroy()
    self.Login.label11.destroy()
    self.Login.okbutt.destroy()
    self.Login.label12.destroy()    

    Modules.Check.openwindow = "Login"
    self.title('Doru\'s No Frills - Login')
    self.Login.label5=self.la(pady=4)
    self.Login.grid = self.gr(cols=4)
    self.Login.label7=self.la(pady=2)
    self.Login.userlabel=self.la(text='Username:', font='Calibri', fg= 'black')
    self.Login.userentry=self.en(justify=LEFT, text='', width=3, pady=3)
    self.Login.label1=self.la(pady=2)
    self.Login.label2=self.la(pady=2)
    self.Login.passwordlabel=self.la(text='Password:', font='Calibri', fg= 'black')
    self.Login.passentry=self.en(justify=LEFT, text='', width=3, pady=3, show='*')
    self.Login.label3=self.la()
    self.Login.label4=self.la()
    self.endgr()
    self.Login.grid2=self.gr(cols=3,pady=1)
    self.Login.label9=self.la()
    self.Login.button = self.bu(text='Login', font= 'Calibri', width=4, command=Callable(ValidateLogin, self), background='yellow')    
    self.Login.label10=self.la()
    self.endgr()
    self.Login.label11=self.la(height=1)   
    self.Login.button2 = self.bu(text='Forgot Password?...', font= ( 'Calibri', '11', 'underline'), width=4, padx=150, fg='red', borderwidth=0, command=Callable(ForgotPass, self))
    self.Login.label12=self.la(height=1)    

def CheckUser(self, Event=None):
    global screen
    global index
    global Password
    found = 0
    Accountlist=Account_Read()
    UserList = Accountlist[0][1:]
    user = self.Login.userentry.get()
    Password=''
    for i in range(len(UserList)):
        if UserList[i] == user:
            screen='2'
            index=i            
            found=1
            break
    Question = Accountlist[4][index+1]
    if found==1:
        self.Login.userentry.delete(0, 'end')     
        self.Login.instruction.config(text=Question)
        self.Login.userlabel.config(text='Answer:')
        self.Login.button.config(command=Callable(CheckAns, self))
    elif found==0:
        self.Login.userentry.delete(0, 'end')    
        tkMessageBox.showwarning('Error', 'That is not a valid username')


def CheckAns(self, Event=None):
    global screen
    global index
    global Password
    global EntryAns
    Accountlist=Account_Read()
    RealAns = Accountlist[5][index+1]
    EntryAns = self.Login.userentry.get()
    Pass = random.sample(['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','1','2','3','4','5','6','7','8','9','0'], 6)
    for i in range(len(Pass)):
        if len(Password) < 12:
            Password = Password+Pass[i]

    if EntryAns==RealAns:
        screen='3'
        self.Login.instruction.config(text='Your New Password Is...', font = ('Calibri', '20', 'bold'))

        self.Login.sep1.destroy()
        self.Login.grid.destroy()
        self.Login.label7.destroy()
        self.Login.userlabel.destroy()
        
        self.Login.userentry.destroy()
        self.Login.label1.destroy()
        self.Login.label2.destroy()
        self.Login.grid2.destroy()
        self.Login.label9.destroy()
        self.Login.button.destroy()
        self.Login.label10.destroy()
        self.Login.label11.destroy() 
        self.Login.button2.destroy()
        self.Login.label12.destroy()


        
        self.Login.userlabel = self.en(text=Password)
        self.Login.userlabel.config(justify='center', state='readonly', font = ('Calibri', '16', 'bold'), bd=0)
           
        self.Login.Passla2 =self.la(font=('Calibri', '10', 'italic'), text='Be sure to copy your new password! \n After you log in, you may go to the \'Change Password\' screen \n to get a new password.')
        self.Login.label11=self.la(height=1)
        self.Login.okbutt =self.bu(text='Confirm & Return to Login', font = ('Calibri', '12'), padx=15,  background='yellow', command=Callable(PassShutdown, self))

        self.Login.label12=self.la(height=1)    

    elif EntryAns!=RealAns:
        self.Login.userentry.delete(0, 'end')
        tkMessageBox.showwarning('Error', 'Your security answer was not correct')
    
def AddIntoCSV(lis):
    if len(lis) != 1:
        csvfile = 'Files\Modules\Database\useraccounts.csv'
        WriteCSV(lis, csvfile)
        return [True]
    else:
        return False, lis[0] 
    
def ValidateLogin(self, Event=None):
    Accountlist=Account_Read()
    user=self.Login.userentry.get()
    passw=self.Login.passentry.get()
    result=Modules.ValidateLogic.Validate(user,passw,Accountlist)
    if result != False:
        self.endcol() # Ends original GUI column
        self.Login.destroy()
        Modules.Check.userlevel = result[0]
        Modules.Check.loggeduser = user
        Modules.Check.hourlywage= result[1]
        MenuBar.Create(self)
        StatusBar.Create(self)
        WelcomeScreen.Create(self)
        self.title('Doru\'s No Frills - Welcome') 
    else:
        tkMessageBox.showwarning('Error', 'Username or password is incorrect, please retry')


def ForgotPass(self, Event=None):
    self.Login.label5.destroy()
    self.Login.grid.destroy()
    self.Login.label7.destroy()
    self.Login.userlabel.destroy()
    self.Login.userentry.destroy()
    self.Login.label1.destroy()
    self.Login.label2.destroy()
    self.Login.passwordlabel.destroy()
    self.Login.passentry.destroy()
    self.Login.label3.destroy()
    self.Login.label4.destroy()
    self.Login.grid2.destroy()
    self.Login.label9.destroy()
    self.Login.button.destroy()
    self.Login.label11.destroy()
    self.Login.button2.destroy()
    self.Login.label12.destroy()


    Modules.Check.openwindow = "Password Recovery"
    self.title('Doru\'s No Frills - Password Recovery')

    self.Login.instruction = self.la('Please enter your username!', pady=1, font= ( 'Calibri', '11', 'underline'))
    self.Login.sep1 = self.la()
    self.Login.grid = self.gr(cols=4)
    self.Login.label7=self.la(pady=6)
    self.Login.userlabel=self.la(text='Username:', font='Calibri', fg= 'black')
    self.Login.userentry=self.en(justify=LEFT, text='', width=3, pady=3)
    self.Login.label1=self.la(pady=2)
    self.Login.label2=self.la(pady=2)
    self.endgr()
    self.Login.grid2=self.gr(cols=3,pady=1)
    self.Login.label9=self.la()
    self.Login.button = self.bu(text='OK', font= 'Calibri', width=4, command=Callable(CheckUser, self), background='yellow')    
    self.Login.label10=self.la()
    self.endgr()
    self.Login.label11=self.la(height=1)   
    self.Login.button2 = self.bu(text='Go back to Login...', font= ( 'Calibri', '11', 'underline'), width=4, padx=150, fg='red', borderwidth=0, command=Callable(LoginCr, self))
    self.Login.label12=self.la(height=1)    
