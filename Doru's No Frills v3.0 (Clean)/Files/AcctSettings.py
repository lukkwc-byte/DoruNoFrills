'''
    Version 0.01 01/11/2011 Michael (Change Password GUI)
    Version 0.02 01/16/2011 Michael (Password Logic)
    Version 0.03 01/18/2011 Michael (Security Question Logic)
    Version 0.04 01/18/2011 Michael (Error Proofing)
    
'''
from Swampy.Gui import *
import csv
import Modules.Check
import ChangePassPopup
from Modules.ReadCSV import *
from Modules.WriteCSV import *

def Passwords(self,ReadAccountsCSV):
    old_pass= self.AcctSettings.Old_password_entry.get()
    new_pass=self.AcctSettings.New_password_entry.get()
    confirm_pass=self.AcctSettings.Confirm_password_entry.get()
    ReadAccountlist=ReadAccountsCSV()
    usernamelist= ReadAccountlist[0]
    passwordlist= ReadAccountlist[1]
    userlevellist= ReadAccountlist[2]
    hourlywagelist= ReadAccountlist[3]
    secureQ = ReadAccountlist[4]
    secureA = ReadAccountlist[5]
    validity = 0
    match=0
    for i in range(len(usernamelist)):
        if old_pass == '':
            validity = 3
            break
        if new_pass == '':
            validity = 4
            break
        if confirm_pass == '':
            validity = 5
            break
        if '|' in old_pass or ',' in old_pass:
            validity = 8
            break
        if ' ' in old_pass:
            validity = 21
            break
        if '|' in new_pass or ',' in new_pass:
            validity = 9
            break
        if ' ' in new_pass:
            validity = 22
            break
        if '|' in confirm_pass or ',' in confirm_pass:
            validity = 10
            break
        if ' ' in confirm_pass:
            validity = 23
            break
        if len(old_pass) > 12:
            validity = 11
            break        
        if len(new_pass) > 12:
            validity = 12
            break
        if len(confirm_pass) > 12:
            validity = 13
            break
        if usernamelist[i] == Modules.Check.loggeduser:
            index = i
            if passwordlist[index] == old_pass:
                if new_pass != confirm_pass:
                    validity = 2              
                elif new_pass == confirm_pass:
                    passwordlist[index]= new_pass
                    match=1
            elif passwordlist[index] != old_pass:
                validity = 1

    if validity > 0:
        returnval=validity
        PasswordRefreshEntries(self)
        Validity_Test(returnval)
    else:
        returnlis=[usernamelist,passwordlist,userlevellist,hourlywagelist,secureQ,secureA]
        Add_Into_CSV(returnlis)
        PasswordRefreshEntries(self)
    return 
def Validity_Test(returnval):
    if returnval > 0:
        errorcodes(returnval)
def errorcodes(error_testing):
    ChangePassPopup.Create(error_testing)         
def SecurityQuestions(self,ReadAccountsCSV):
    old_security_answer= self.AcctSettings.Old_security_answer_entry.get()
    new_security_question=self.AcctSettings.New_security_question_entry.get()
    new_security_answer=self.AcctSettings.New_security_answer_entry.get()
    ReadAccountlist=ReadAccountsCSV()
    usernamelist= ReadAccountlist[0]
    passwordlist= ReadAccountlist[1]
    userlevellist= ReadAccountlist[2]
    hourlywagelist= ReadAccountlist[3]
    secureQ = ReadAccountlist[4]
    secureA = ReadAccountlist[5]
    validity = 0
    for i in range(len(usernamelist)):
        if usernamelist[i] == Modules.Check.loggeduser:
            index = i
            question=secureQ[i]
    for i in range(len(secureQ)):
        if new_security_question == '':
            validity = 6
            break
        if new_security_answer == '':
            validity = 7
            break
        if old_security_answer == '':
            validity = 20
            break
        if '|' in old_security_answer or ',' in old_security_answer:
            validity = 14
            break
        if ' ' in old_security_answer:
            validity = 24
            break
        if '|' in new_security_question or ',' in new_security_question:
            validity = 15
            break
        if ' ' in new_security_question:
            validity = 25
            break
        if '|' in new_security_answer or ',' in new_security_answer:
            validity = 16
            break
        if ' ' in new_security_answer:
            validity = 26
            break
        if len(old_security_answer) > 14:
            validity = 19
            break        
        if len(new_security_question) > 35:
            validity = 17
            break        
        if len(new_security_answer) > 14:
            validity = 18
            break
        if secureQ[i] == question:
            if secureA[i] == old_security_answer:
                index = i
                secureQ[index] = new_security_question
                secureA[index] = new_security_answer
                returnlis2=[usernamelist,passwordlist,userlevellist,hourlywagelist,secureQ,secureA]
                FindOldQuestion(returnlis2)
            elif secureA[i] != old_security_answer:
                validity = 8
    if validity > 0:
        returnval=validity
        SecurityRefreshEntries(self)
        Validity_Test(returnval)
    else:
        returnlis=[usernamelist,passwordlist,userlevellist,hourlywagelist,secureQ,secureA]
        Add_Into_CSV(returnlis)
        SecurityRefreshEntries(self)
    return 

def ReadAccountsCSV():
    Accountlist = Account_Read()
    username = Accountlist[0]
    password = Accountlist[1]
    userlevel = Accountlist[2]
    hourlywage = Accountlist[3]
    secureQ = Accountlist[4]
    secureA = Accountlist[5]
    return [username, password,userlevel,hourlywage,secureQ,secureA]

def Add_Into_CSV(lis):
    csvfile = 'Files\Modules\Database\useraccounts.csv'
    WriteCSV(lis, csvfile)
    
def PasswordRefreshEntries(self):
    self.AcctSettings.New_password_entry.delete(0, 'end')
    self.AcctSettings.Old_password_entry.delete(0, 'end')
    self.AcctSettings.Confirm_password_entry.delete(0, 'end')

def SecurityRefreshEntries(self):
    Question=FindOldQuestion(Modules.Check.loggeduser)
    self.AcctSettings.New_security_question_entry.delete(0, 'end')
    self.AcctSettings.New_security_answer_entry.delete(0, 'end')
    self.AcctSettings.Old_security_question_label.config(text=Question,font=('Calibri','12','bold'), highlightthickness=2, highlightcolor= '#4f81bd')
    self.AcctSettings.Old_security_answer_entry.delete(0, 'end')
def FindOldQuestion(user):
    ReadAccountlist = ReadAccountsCSV()
    usernamelist= ReadAccountlist[0]
    passwordlist= ReadAccountlist[1]
    userlevellist= ReadAccountlist[2]
    hourlywagelist= ReadAccountlist[3]
    secureQ = ReadAccountlist[4]
    secureA = ReadAccountlist[5]
    index=0
    for i in range(len(usernamelist)):
        if usernamelist[i] == user:
            index = i
            question=secureQ[i]
            return question
def Create(self):
    Question=FindOldQuestion(Modules.Check.loggeduser)
    self.AcctSettings = self.col()
    self.row(pady=5)
    self.endrow()
    self.AcctSettings.fake_label= self.la(text=''+Modules.Check.loggeduser, font=('Calibri','30','bold','underline'))
    self.AcctSettings.fake_label= self.la(height=1)
    self.AcctSettings.title_lable= self.la(text='Change Password', justify= 'center', font=('Calibri','20'))
    self.AcctSettings.fake_label= self.la(height=2)
    self.AcctSettings.grid_1=self.gr(cols=2)
    self.AcctSettings.Old_password_label= self.la(text='Old Password:', font=('Calibri','14','bold'))
    self.AcctSettings.Old_password_entry= self.en(font=('Calibri','12','bold'),show='*',padx=100, highlightthickness=2, highlightcolor= '#4f81bd')
    self.AcctSettings.New_password_label= self.la(text='New Password:', font=('Calibri','14','bold'))
    self.AcctSettings.New_password_entry= self.en(font=('Calibri','12','bold'), show='*',padx=100, highlightthickness=2, highlightcolor= '#4f81bd')
    self.AcctSettings.Confirm_password_label= self.la(text='Confirm Password:', font=('Calibri','14','bold'))
    self.AcctSettings.Confirm_password_entry= self.en(font=('Calibri','12','bold'), show='*',padx=100, highlightthickness=2, highlightcolor= '#4f81bd')
    self.AcctSettings.endgrid_1= self.endgr()
    self.AcctSettings.fake_label= self.la()
    self.AcctSettings.Confirm_Changes_button=self.bu(text='Confirm Change', font=('Calibri','14','bold'), bg= '#4f81bd',activebackground='#4f81bd', padx=420,command= Callable(Passwords,self,ReadAccountsCSV)) 
    self.AcctSettings.fake_label= self.la(height=1)
    self.row()
    self.AcctSettings.labelline=self.la(text='_____________________________________________________________________________________________', font=('Calibri', '14'), justify='center', pady=8)
    self.endrow()
    self.row(pady=5)
    self.endrow()
    self.AcctSettings.Security_change_lable= self.la(text='Change Security Question', justify= 'center', font=('Calibri','20'), pady=10)
    self.AcctSettings.fake_label= self.la(height=1)
    self.AcctSettings.row_1= self.row()
    self.AcctSettings.column= self.col()
    self.AcctSettings.Old_security_question_label= self.la(text='Old Security Question:', font=('Calibri','13','bold'))    
    self.AcctSettings.Old_security_answer_label= self.la(text='Old Security Answer:', font=('Calibri','13','bold'))
    self.AcctSettings.New_security_question_label= self.la(text='New Security Question:', font=('Calibri','12','bold'))    
    self.AcctSettings.New_security_answer_label= self.la(text='New Security Answer:', font=('Calibri','12','bold'))
    self.AcctSettings.endcolumn= self.endcol()
    self.AcctSettings.column= self.col(padx=25)
    self.AcctSettings.Old_security_question_label= self.la(text=Question,font=('Calibri','12','bold'),padx=70, highlightthickness=2, highlightcolor= '#4f81bd')
    self.AcctSettings.Old_security_answer_entry= self.en(font=('Calibri','12','bold'),show='*',padx=70, highlightthickness=2, highlightcolor= '#4f81bd')
    self.AcctSettings.New_security_question_entry= self.en(font=('Calibri','12','bold'),padx=70, highlightthickness=2, highlightcolor= '#4f81bd')
    self.AcctSettings.New_security_answer_entry=self.en(font=('Calibri','12','bold'),show='*',padx=70, highlightthickness=2, highlightcolor= '#4f81bd')
    self.AcctSettings.endcolumn= self.endcol()
    self.AcctSettings.endrow_1= self.endrow()   
    self.AcctSettings.fake_label= self.la()    
    self.AcctSettings.Confirm_security_question_button=self.bu(text='Confirm Change', font=('Calibri','14','bold'), bg= '#4f81bd',activebackground='#4f81bd',padx=420,command= Callable(SecurityQuestions,self,ReadAccountsCSV))
    self.AcctSettings.fake_label= self.la(height=7)
    self.endcol()


    




   
   
