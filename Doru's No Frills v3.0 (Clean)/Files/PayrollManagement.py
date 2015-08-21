''' File Log:
    Version 0.01 24/12/2011 (Jonathan) - Dummy Screen
'''

from Tkinter import *
from Swampy.Gui import *
import time
import datetime
from datetime import date
import Modules.PayrollMGMTdisplay
from Modules.ReadCSV import *
#import PMGMTErrorPopup
import tkMessageBox
import Payroll

AddUser=''
AddDate=''
AddCI=''
AddCO=''
EditID=''
EditCI=''
EditCO=''
DateID=''

def ShiftError():
    label='No shift has been selected'
    tkMessageBox.showwarning("Error", label) # Show error in box

def AddError(addself, errorcode):
    if errorcode==3:
        addself.ErrorLabel.config(text='ERROR: USERNAME IS EMPTY', fg='red')
    elif errorcode==4:
        addself.ErrorLabel.config(text='ERROR: USERNAME DOES NOT EXIST', fg='red')
    elif errorcode==5:
        addself.ErrorLabel.config(text='ERROR: DATE IS EMPTY', fg='red')
    elif errorcode==6:
        addself.ErrorLabel.config(text='ERROR: DATE IS INVALID', fg='red')
    elif errorcode==7:
        addself.ErrorLabel.config(text='ERROR: DATE IS INVALID', fg='red')
    elif errorcode==8:
        addself.ErrorLabel.config(text='ERROR: DATE IS INVALID', fg='red')
    elif errorcode==45:
        addself.ErrorLabel.config(text='ERROR: DATE DOES NOT EXIST YET', fg='red')
    elif errorcode==46:
        addself.ErrorLabel.config(text='ERROR: DATE DOES NOT EXIST YET', fg='red')
    elif errorcode==47:
        addself.ErrorLabel.config(text='ERROR: DATE DOES NOT EXIST YET', fg='red')
    elif errorcode==48:
        addself.ErrorLabel.config(text='ERROR: DATE DOES NOT EXIST', fg='red')
    elif errorcode==49:
        addself.ErrorLabel.config(text='ERROR: DATE DOES NOT EXIST', fg='red')
    elif errorcode==50:
        addself.ErrorLabel.config(text='ERROR: DATE DOES NOT EXIST', fg='red')
    elif errorcode==51:
        addself.ErrorLabel.config(text='ERROR: DATE DOES NOT EXIST', fg='red')
    elif errorcode==52:
        addself.ErrorLabel.config(text='ERROR: DATE DOES NOT EXIST', fg='red')
    elif errorcode==53:
        addself.ErrorLabel.config(text='ERROR: DATE DOES NOT EXIST', fg='red')
    elif errorcode==10:
        addself.ErrorLabel.config(text='ERROR: CHECK IN IS EMPTY', fg='red')
    elif errorcode==11:
        addself.ErrorLabel.config(text='ERROR: CHECK IN IS INVALID', fg='red')
    elif errorcode==12:
        addself.ErrorLabel.config(text='ERROR: CHECK IN IS INVALID', fg='red')
    elif errorcode==13:
        addself.ErrorLabel.config(text='ERROR: CHECK IN IS INVALID', fg='red')
    elif errorcode==9:
        addself.ErrorLabel.config(text='ERROR: CHECK IN IS INVALID', fg='red')
    elif errorcode==14:
        addself.ErrorLabel.config(text='ERROR: CHECK IN IS INVALID', fg='red')
    elif errorcode==15:
        addself.ErrorLabel.config(text='ERROR: CHECK OUT IS EMPTY', fg='red')
    elif errorcode==16:
        addself.ErrorLabel.config(text='ERROR: CHECK OUT IS INVALID', fg='red')
    elif errorcode==17:
        addself.ErrorLabel.config(text='ERROR: CHECK OUT IS INVALID', fg='red')
    elif errorcode==18:
        addself.ErrorLabel.config(text='ERROR: CHECK OUT IS INVALID', fg='red')
    elif errorcode==29:
        addself.ErrorLabel.config(text='ERROR: CHECK OUT IS BEFORE CHECK IN', fg='red')
    elif errorcode==30:
        addself.ErrorLabel.config(text='ERROR: CHECK OUT IS BEFORE CHECK IN', fg='red')
    elif errorcode==31:
        addself.ErrorLabel.config(text='ERROR: CHECK OUT IS NOT AFTER CHECK IN', fg='red')
    elif errorcode==32:
        addself.ErrorLabel.config(text='ERROR: TIME DOES NOT EXIST YET', fg='red')
    elif errorcode==33:
        addself.ErrorLabel.config(text='ERROR: TIME DOES NOT EXIST YET', fg='red')
    elif errorcode==34:
        addself.ErrorLabel.config(text='ERROR: TIME DOES NOT EXIST YET', fg='red')

    

def EditError(editself, errorcode):
    if errorcode==20:
        editself.ErrorLabel.config(text='ERROR: CHECK IN IS EMPTY', fg='red')
    if errorcode==21:
        editself.ErrorLabel.config(text='ERROR: CHECK IN IS INVALID', fg='red')
    if errorcode==22:
        editself.ErrorLabel.config(text='ERROR: CHECK IN IS INVALID', fg='red')
    if errorcode==23:
        editself.ErrorLabel.config(text='ERROR: CHECK IN IS INVALID', fg='red')
    if errorcode==35:
        editself.ErrorLabel.config(text='ERROR: CHECK IN IS INVALID', fg='red')
    if errorcode==36:
        editself.ErrorLabel.config(text='ERROR: CHECK IN IS INVALID', fg='red')
    if errorcode==25:
        editself.ErrorLabel.config(text='ERROR: CHECK OUT IS EMPTY', fg='red')
    if errorcode==26:
        editself.ErrorLabel.config(text='ERROR: CHECK OUT IS INVALID', fg='red')
    if errorcode==27:
        editself.ErrorLabel.config(text='ERROR: CHECK OUT IS INVALID', fg='red')
    if errorcode==28:
        editself.ErrorLabel.config(text='ERROR: CHECK OUT IS INVALID', fg='red')
    if errorcode==37:
        editself.ErrorLabel.config(text='ERROR: CHECK OUT IS INVALID', fg='red')
    if errorcode==38:
        editself.ErrorLabel.config(text='ERROR: CHECK OUT IS INVALID', fg='red')
    if errorcode==39:
        editself.ErrorLabel.config(text='ERROR: CHECK OUT IS BEFORE CHECK IN', fg='red')
    if errorcode==40:
        editself.ErrorLabel.config(text='ERROR: CHECK OUT IS BEFORE CHECK IN', fg='red')
    if errorcode==41:
        editself.ErrorLabel.config(text='ERROR: CHECK OUT IS NOT AFTER CHECK IN', fg='red')
    if errorcode==42:
        editself.ErrorLabel.config(text='ERROR: TIME DOES NOT EXIST YET', fg='red')
    if errorcode==43:
        editself.ErrorLabel.config(text='ERROR: TIME DOES NOT EXIST YET', fg='red')
    if errorcode==44:
        editself.ErrorLabel.config(text='ERROR: TIME DOES NOT EXIST YET', fg='red')
                     

def Approval(self):
    index=self.PayrollManagement.ListBox.curselection()
    if index==():
        ShiftError()
        return
    else:
        ID= index[0]
        Modules.PayrollMGMTdisplay.ApproveShift(self, ID)

def Outstanding(self):
    Modules.PayrollMGMTdisplay.Outstanding_Shifts(self)
    
    self.PayrollManagement.outstanding.config(state='disabled',relief='sunken')
    self.PayrollManagement.completed.config(state='active',relief='raised')

    
    
    self.PayrollManagement.approve.config(state='disabled', relief='ridge')
    self.PayrollManagement.add.config(state='disabled', relief='ridge')
    self.PayrollManagement.edit.config(text='End Shift', command=Callable(Complete_Shift, self))
    
def Hide_Outstanding(self):
    Modules.PayrollMGMTdisplay.FillDisplay(self)
    self.PayrollManagement.outstanding.config(state='active',relief='raised')
    self.PayrollManagement.completed.config(state='disabled',relief='sunken')
    
    self.PayrollManagement.approve.config(state='normal', relief='raised')
    self.PayrollManagement.add.config(state='normal', relief='raised')
    self.PayrollManagement.edit.config(text='Edit Shift', command=Callable(Edit_Shift_Screen, self))
    

    
def Complete_Shift(self):
    index=self.PayrollManagement.ListBox.curselection()
    if index==():
        ShiftError()
        return
    else:
        ID= index[0]
        Modules.PayrollMGMTdisplay.CompleteShift(self, ID)
        Payroll.test()

def Add_Shift_Screen(self):
    global AddUser
    global AddDate
    global AddCI
    global AddCO

    Today=time.strftime('%d/%m/%Y')
    addself=Gui(debug=False)
    sw = addself.winfo_screenwidth()
    sh = addself.winfo_screenheight()
    x = (sw/2) - (480/2) 
    y = (sh/2) - (310/2)
    addself.geometry('%dx%d+%d+%d' % (480, 310, x, y))
    addself.resizable(width=False, height=False)
    addself.title('Add Shift')
    addself.ErrorLabel=addself.la()
    addself.gr(cols=2)
    addself.la('Username:',font='Calibri',pady=15)
    AddUser = addself.en(font='Calibri', padx=15,pady=15, justify=CENTER, readonlybackground='white')
    addself.la('Date:',font='Calibri',pady=15)
    AddDate = addself.en(font='Calibri',  padx=15,pady=15, text=Today, justify=CENTER, readonlybackground='white')
    addself.la('Check In Time:',font='Calibri',pady=15)
    AddCI = addself.en(font='Calibri',  padx=15, pady=15,text='00:00:00 AM', justify=CENTER, readonlybackground='white')
    addself.la('Check Out Time:',font='Calibri',pady=15)
    AddCO = addself.en(font='Calibri',  padx=15, pady=15,text='00:00:00 AM', justify=CENTER, readonlybackground='white')
    #paidentry.config(state='readonly')
    #changeentry.config(state='readonly')
    addself.endgr()
    addself.row()
    addself.bu('Add Shift', font='Calibri',pady=15, padx=40,  bg='#47c57f',activebackground='lightgreen', fg='black',justify=CENTER, width='5', command=Callable(Add_Shift, self, addself))
    addself.bu('Cancel', font='Calibri',pady=15, padx=40, bg='#d94444',activebackground='#CD5555', fg='black',justify=CENTER, width='5', command=Callable(CancelAdd, self, addself))
    addself.endrow()
    addself.grab_set_global()
    addself.focus_force()
    addself.mainloop()

def CancelAdd(self, addself):
    addself.destroy()

    
def Add_Shift(self, addself):
    global AddUser
    global AddDate
    global AddCI
    global AddCO
    numberlist='1234567890'
    AddList=[]
    Username=AddUser.get()
    Employee=Account_Read()
    AllEmployees=Employee[0]
    if Username=='':
        AddError(addself, 3)
        return
    elif Username not in AllEmployees:
        AddError(addself, 4)
        return
    else:
        AddList.append(Username)
    Date=AddDate.get()
    Today=time.strftime('%d/%m/%Y')
    if Date=='':
        AddError(addself, 5)
        return
    elif Date[2]!='/' or Date[5]!='/':
        AddError(addself, 6)
        return
    elif len(Date)!=10:
        AddError(addself, 7)
        return
    elif Date[0] not in numberlist or Date[1] not in numberlist or Date[3] not in numberlist or Date[4] not in numberlist or Date[6] not in numberlist or Date[7] not in numberlist or Date[8] not in numberlist or Date[9] not in numberlist:
        AddError(addself, 8)
        return
    Day=int(Date[0:2])
    Month=int(Date[3:5])
    Year=int(Date[6::])
    CDay=int(Today[0:2])
    CMonth=int(Today[3:5])
    CYear=int(Today[6::])
    if Year>CYear:
        AddError(addself, 45)
        return
    elif Year==CYear and Month>CMonth:
        AddError(addself, 46)
        return
    elif Year==CYear and Month==CMonth and Day>CDay:
        AddError(addself, 47)
        return
    elif Year%4==0 and Month==2 and Day>29:
        AddError(addself, 48)
        return
    elif Year%4!=0 and Month==2 and Day>28:
        AddError(addself, 49)
        return
    elif Month==4 and Day>30:
        AddError(addself, 50)
        return
    elif Month==6 and Day>30:
        AddError(addself, 51)
        return
    elif Month==9 and Day>30:
        AddError(addself, 52)
        return
    elif Month==11 and Day>30:
        AddError(addself, 53)
        return
    else:
        Date2=Date[6::]+'-'+Date[3:5]+'-'+Date[0:2]
        AddList.append(Date2)
    CheckIn=AddCI.get()
    CheckOut=AddCO.get()
    Now=time.strftime('%H:%M:%S')
    Today=time.strftime('%d/%m/%Y')
    if CheckIn=='':
        AddError(addself, 10)
        return
    elif CheckIn[2]!=':' or CheckIn[5]!=':':
        AddError(addself, 11)
        return
    elif len(CheckIn)!=11:
        AddError(addself, 12)
        return
    elif CheckIn[0] not in numberlist or CheckIn[1] not in numberlist or CheckIn[3] not in numberlist or CheckIn[4] not in numberlist or CheckIn[6] not in numberlist or CheckIn[7] not in numberlist:
        AddError(addself, 13)
        return
    elif int(CheckIn[0:2])>12 or int(CheckIn[0:2])<1 or int(CheckIn[3:5])>59 or int(CheckIn[6:8])>59:
        AddError(addself, 9)
        return
    hour=int(CheckIn[0:2])
    
    if CheckIn[9::]=='AM' and CheckIn[0:2]=='12':
        hour='00'
        CheckInF=str(hour)+CheckIn[2:8]
    elif CheckIn[9::]=='AM':
        CheckInF=CheckIn[0:8]
    elif CheckIn[9::]=='PM' and CheckIn[0:2]=='12':
        CheckInF=CheckIn[0:8]
    elif CheckIn[9::]=='PM':
        hour=hour+12
        CheckInF=str(hour)+CheckIn[2:8]
    elif CheckIn[9::]!='AM' and CheckIn[9::]!='PM':
        AddError(addself, 14)
        return
    if CheckOut=='':
        AddError(addself, 15)
        return
    elif CheckOut[2]!=':' or CheckOut[5]!=':':
        AddError(addself, 16)
        return
    elif len(CheckOut)!=11:
        AddError(addself, 17)
        return
    elif CheckOut[0] not in numberlist or CheckOut[1] not in numberlist or CheckOut[3] not in numberlist or CheckOut[4] not in numberlist or CheckOut[6] not in numberlist or CheckOut[7] not in numberlist:
        AddError(addself, 18)
        return
    elif int(CheckOut[0:2])>12 or int(CheckOut[0:2])<1 or int(CheckOut[3:5])>59 or int(CheckOut[6:8])>59:
        AddError(addself, 9)
        return
    hour2=int(CheckOut[0:2])
    if CheckOut[9::]=='AM' and CheckOut[0:2]=='12':
        hour2='00'
        CheckOutF=str(hour2)+CheckOut[2:8]
    elif CheckOut[9::]=='AM':
        CheckOutF=CheckOut[0:8]
    elif CheckOut[9::]=='PM' and CheckOut[0:2]=='12':
        CheckOutF=CheckOut[0:8]
    elif CheckOut[9::]=='PM':
        hour2=hour2+12
        CheckOutF=str(hour2)+CheckOut[2:8]
    elif CheckOut[9::]!='AM' and CheckOut[9::]!='PM':
        AddError(addself, 14)
        return
    if int(CheckOutF[0:2])<int(CheckInF[0:2]):
        AddError(addself, 29)
        return
    elif int(CheckOutF[0:2])==int(CheckInF[0:2]) and int(CheckOutF[3:5])<int(CheckInF[3:5]):
        AddError(addself, 30)
        return
    elif int(CheckOutF[0:2])==int(CheckInF[0:2]) and int(CheckOutF[3:5])==int(CheckInF[3:5]) and int(CheckOutF[6::])<=int(CheckInF[6::]):
        AddError(addself, 31)
        return
    elif Date==Today and int(CheckOutF[0:2])>int(Now[0:2]):
        AddError(addself, 32)
        return
    elif Date==Today and int(CheckOutF[0:2])==int(Now[0:2]) and int(CheckOutF[3:5])>int(Now[3:5]):
        AddError(addself, 33)
        return
    elif Date==Today and int(CheckOutF[0:2])==int(Now[0:2]) and int(CheckOutF[3:5])==int(Now[3:5]) and int(CheckOutF[6::])>int(Now[6::]):
        AddError(addself, 34)
        return
    else:
        AddList.append(CheckInF)
        AddList.append(CheckOutF)
    Modules.PayrollMGMTdisplay.AddShift(self, AddList)
    addself.destroy()

def Edit_Shift_Screen(self):
    global EditID
    global EditCI
    global EditCO
    global DateID
    index=self.PayrollManagement.ListBox.curselection()
    if index==():
        ShiftError()
        return
    else:
        ID=index[0]
        #self.grab_set_global()
        editself=Gui(debug=False)
        sw = editself.winfo_screenwidth()
        sh = editself.winfo_screenheight()
        x = (sw/2) - (450/2) 
        y = (sh/2) - (310/2)
        editself.geometry('%dx%d+%d+%d' % (450, 310, x, y))
        editself.resizable(width=False, height=False)
        editself.title('Edit Shift')
        editself.ErrorLabel=editself.la()
        editself.gr(cols=2)
        editself.la('Shift ID:',font='Calibri',pady=15)
        Shift=Modules.PayrollMGMTdisplay.ShiftIDEdit(self, ID)
        Date=Modules.PayrollMGMTdisplay.DateEdit(self, ID)
        CheckIn=Modules.PayrollMGMTdisplay.CheckInEdit(self, ID)
        CheckOut=Modules.PayrollMGMTdisplay.CheckOutEdit(self, ID)
        EditID = editself.en(font='Calibri', padx=15,pady=15, text=Shift, justify=CENTER, readonlybackground='white')
        EditID.config(state='readonly')
        editself.la('Date:',font='Calibri',pady=15)
        DateID = editself.en(font='Calibri', padx=15,pady=15, text=Date, justify=CENTER, readonlybackground='white')
        DateID.config(state='readonly')
        

        editself.la('Check In Time:',font='Calibri',pady=15)
        EditCI = editself.en(font='Calibri',  padx=15,pady=15, text=CheckIn, justify=CENTER, readonlybackground='white')
        editself.la('Check Out Time:',font='Calibri',pady=15)
        EditCO = editself.en(font='Calibri',  padx=15, pady=15,text=CheckOut, justify=CENTER, readonlybackground='white')
        #paidentry.config(state='readonly')
        #changeentry.config(state='readonly')
        editself.endgr()

        editself.row()
        editself.bu('Edit Shift', font='Calibri',pady=15, padx=40,  bg='#47c57f',activebackground='lightgreen', fg='black',justify=CENTER, width='5', command=Callable(Edit_Shift,self, editself))
        editself.bu('Cancel', font='Calibri',pady=15, padx=40, bg='#d94444',activebackground='#CD5555', fg='black',justify=CENTER, width='5', command=Callable(CancelEdit, self, editself))
        editself.endrow()

        
        editself.grab_set_global()
        editself.focus_force()


        editself.mainloop()

def CancelEdit(self, editself):
    editself.destroy()

def Edit_Shift(self, editself):
    global EditID
    global EditCI
    global EditCO
    global DateID
    numberlist='1234567890'
    EditList=[]
    ShiftID=EditID.get()
    EditList.append(ShiftID)
    CheckIn=EditCI.get()
    CheckOut=EditCO.get()
    Date=DateID.get()
    Now=time.strftime('%H:%M:%S')
    Today=time.strftime('%d/%m/%Y')
    if CheckIn=='':
        EditError(editself, 20)
        return
    elif CheckIn[2]!=':' or CheckIn[5]!=':':
        EditError(editself, 21)
        return
    elif len(CheckIn)!=11:
        EditError(editself, 22)
        return
    elif CheckIn[0] not in numberlist or CheckIn[1] not in numberlist or CheckIn[3] not in numberlist or CheckIn[4] not in numberlist or CheckIn[6] not in numberlist or CheckIn[7] not in numberlist:
        EditError(editself, 23)
        return
    elif int(CheckIn[0:2])>12 or int(CheckIn[0:2])<1 or int(CheckIn[3:5])>59 or int(CheckIn[6:8])>59:
        EditError(editself, 35)
        return
    hour=int(CheckIn[0:2])
    if CheckIn[9::]=='AM' and CheckIn[0:2]=='12':
        hour='00'
        CheckInF=str(hour)+CheckIn[2:8]
    elif CheckIn[9::]=='AM':
        CheckInF=CheckIn[0:8]
    elif CheckIn[9::]=='PM' and CheckIn[0:2]=='12':
        CheckInF=CheckIn[0:8]
    elif CheckIn[9::]=='PM':
        hour=hour+12
        CheckInF=str(hour)+CheckIn[2:8]
    elif CheckIn[9::]!='AM' and CheckIn[9::]!='PM':
        EditError(editself, 36)
        return
    
    if CheckOut=='':
        EditError(editself, 25)
        return
    elif CheckOut[2]!=':' or CheckOut[5]!=':':
        EditError(editself, 26)
        return
    elif len(CheckOut)!=11:
        EditError(editself, 27)
        return
    elif CheckOut[0] not in numberlist or CheckOut[1] not in numberlist or CheckOut[3] not in numberlist or CheckOut[4] not in numberlist or CheckOut[6] not in numberlist or CheckOut[7] not in numberlist:
        EditError(editself, 28)
        return
    elif int(CheckOut[0:2])>12 or int(CheckOut[0:2])<1 or int(CheckOut[3:5])>59 or int(CheckOut[6:8])>59:
        EditError(editself, 37)
        return
    hour2=int(CheckOut[0:2])
    if CheckOut[9::]=='AM' and CheckOut[0:2]=='12':
        hour2='00'
        CheckOutF=str(hour2)+CheckOut[2:8]
    elif CheckOut[9::]=='AM':
        CheckOutF=CheckOut[0:8]
    elif CheckOut[9::]=='PM' and CheckOut[0:2]=='12':
        CheckOutF=CheckOut[0:8]
    elif CheckOut[9::]=='PM':
        hour2=hour2+12
        CheckOutF=str(hour2)+CheckOut[2:8]
    elif CheckOut[9::]!='AM' and CheckOut[9::]!='PM':
        EditError(editself, 38)
        return
    if int(CheckOutF[0:2])<int(CheckInF[0:2]):
        EditError(editself, 39)
        return
    elif int(CheckOutF[0:2])==int(CheckInF[0:2]) and int(CheckOutF[3:5])<int(CheckInF[3:5]):
        EditError(editself, 40)
        return
    elif int(CheckOutF[0:2])==int(CheckInF[0:2]) and int(CheckOutF[3:5])==int(CheckInF[3:5]) and int(CheckOutF[6::])<=int(CheckInF[6::]):
        EditError(editself, 41)
        return
    elif Date==Today and int(CheckOutF[0:2])>int(Now[0:2]):
        EditError(editself, 42)
        return
    elif Date==Today and int(CheckOutF[0:2])==int(Now[0:2]) and int(CheckOutF[3:5])>int(Now[3:5]):
        EditError(editself, 43)
        return
    elif Date==Today and int(CheckOutF[0:2])==int(Now[0:2]) and int(CheckOutF[3:5])==int(Now[3:5]) and int(CheckOutF[6::])>int(Now[6::]):
        EditError(editself, 44)
        return
    else:
        EditList.append(CheckInF)
        EditList.append(CheckOutF)
    Modules.PayrollMGMTdisplay.EditShift(self, EditList)
    Modules.PayrollMGMTdisplay.FillDisplay(self)
    editself.destroy()


def Create(self):
    self.PayrollManagement = self.col()

    self.PayrollManagement.label=self.la()

    self.buttonrow = self.row()
    self.PayrollManagement.outstanding=self.bu(text='Outstanding Shifts', activebackground='#CF9052', disabledforeground = 'black', height=1, width=15, pady=15, padx=100, font=', 11', overrelief='groove', bg='#CF9052',  bd=2,  command=Callable(Outstanding, self))
    self.PayrollManagement.completed=self.bu(text='Completed Shifts', state='disabled',relief='sunken', activebackground='#CF9052', disabledforeground = 'black', height=1, width=15, pady=15, padx=100, font=', 11', overrelief='groove', bg='#CF9052',  bd=2,  command=Callable(Hide_Outstanding, self))
    self.endrow()
    
    self.PayrollManagement.label=self.la()
    
    #self.PayrollManagement.displaygrid=self.row()
    
    self.PayrollManagement.toplabels = self.la(padx=71,text=' Employee                                Date                                          Shift ID              Check In Time                           Check Out Time                                                                                     ', bg='#404040', fg='White', font=('Calibri', 10), height=1)
    #self.PayrollManagement.toplabel2 = self.la(width=15)
    #self.endrow()

    self.PayrollManagement.disprow = self.row()
    self.PayrollManagement.la1 = self.la(width=10)
    self.PayrollManagement.ListBox = self.lb(height=20, width=85, font=('Courier'))
    self.PayrollManagement.scrollbar = self.sb(command=self.PayrollManagement.ListBox.yview)
    self.PayrollManagement.ListBox.config(yscrollcommand=self.PayrollManagement.scrollbar.set)
 
    self.PayrollManagement.la2 = self.la(width=10)
    self.endrow()
    
    self.PayrollManagement.displa3 = self.la(width=2)





    self.PayrollManagement.grid=self.gr(cols=3)
    self.PayrollManagement.label=self.la()
    self.PayrollManagement.label=self.la()
    self.PayrollManagement.label=self.la()
    self.PayrollManagement.approve=self.bu(text='Approve',padx=20, font=('Calibri', '13'), bg='#47c57f',activebackground='lightgreen', fg='black',disabledforeground='#A4C8EE',relief='raised', command=Callable(Approval, self))
    self.PayrollManagement.add=self.bu(text='Add Shift',padx=20, font=('Calibri', '13'), bg='#4f81bd',activebackground='#A4C8EE',fg='black',disabledforeground='#A4C8EE', relief='raised',command=Callable(Add_Shift_Screen, self))
    self.PayrollManagement.edit=self.bu(text='Edit Shift',padx=20, font=('Calibri', '13'), bg='#d94444',activebackground='#CD5555', fg='black',disabledforeground='#A4C8EE',relief='raised',command=Callable(Edit_Shift_Screen, self))
    self.PayrollManagement.label=self.la()
    self.PayrollManagement.label=self.la()
    self.PayrollManagement.label=self.la()
    self.endgr()


    Modules.PayrollMGMTdisplay.FillDisplay(self)

    self.PayrollManagement.liftlabel = self.la(height=3)
    
    self.endcol()


