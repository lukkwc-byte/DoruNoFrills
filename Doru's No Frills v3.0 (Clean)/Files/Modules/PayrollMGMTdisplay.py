import csv
import time
from ReadCSV import *
from WriteCSV import *
from PayrollPayments import *

time1 = ''
def FillDisplay(self):
    ShiftDB=Payroll_Read()
    if ShiftDB=='':
        return
    Employee=ShiftDB[0]
    Date=ShiftDB[1]
    ShiftID=ShiftDB[6]
    CheckIn=ShiftDB[3]
    CheckOut=ShiftDB[4]
    Approval=ShiftDB[7]

    del Employee[0]
    del Date[0]
    del ShiftID[0]
    del CheckIn[0]
    del CheckOut[0]
    del Approval[0]

    NewDB=[]
    NewDB.append(Employee)
    NewDB.append(Date)
    NewDB.append(ShiftID)
    NewDB.append(CheckIn)
    NewDB.append(CheckOut)

    ShiftID2=ShiftID[::-1]
    for i in ShiftID2:
        number=int(i)-1
        if Approval[number]=='yes' or Approval[number]=='Yes':
            del Employee[number]
            del Date[number]
            del ShiftID[number]
            del CheckIn[number]
            del CheckOut[number]
            del Approval[number]
        elif CheckOut[number]=='None':
            del Employee[number]
            del Date[number]
            del ShiftID[number]
            del CheckIn[number]
            del CheckOut[number]
            del Approval[number]



    for i in range(len(Date)):
        Day=Date[i][8::]
        Month=Date[i][5:7]
        Year=Date[i][0:4]
        Date[i]=Day+'/'+Month+'/'+Year

    for i in range(len(CheckIn)):
        Hour=int(CheckIn[i][0:2])
        if Hour==12:
            CheckIn[i]=CheckIn[i]+' PM'
        elif Hour==0:
            Hour='12'
            CheckIn[i]=str(Hour)+CheckIn[i][2::]+' AM'
        elif Hour>12 and Hour<22:
            Hour=str(Hour-12)
            CheckIn[i]='0'+str(Hour)+CheckIn[i][2::]+' PM'
        elif Hour>21:
            Hour=str(Hour-12)
            CheckIn[i]=str(Hour)+CheckIn[i][2::]+' PM'
        else:
            CheckIn[i]=CheckIn[i]+' AM'

    for i in range(len(CheckOut)):
        Hour=int(CheckOut[i][0:2])
        if Hour==12:
            CheckOut[i]=CheckOut[i]+' PM'
        elif Hour==0:
            Hour='12'
            CheckOut[i]=str(Hour)+CheckOut[i][2::]+' AM'
        elif Hour>12 and Hour<22:
            Hour=str(Hour-12)
            CheckOut[i]='0'+str(Hour)+CheckOut[i][2::]+' PM'
        elif Hour>21:
            Hour=str(Hour-12)
            CheckOut[i]=str(Hour)+CheckOut[i][2::]+' PM'
        else:
            CheckOut[i]=CheckOut[i]+' AM'
    
    self.PayrollManagement.ListBox.delete(0, 'end')
    for i in range(len(Employee)):

        ## Alotted Spaces ##
        char1 = 15 
        char2 = 15
        char3 = 8 
        char4 = 16 


        space1 = (char1-len(Employee[i]))*' '
        space2 = (char2-len(Date[i]))*' '
        space3 = (char3-len(ShiftID[i]))*' '
        space4 = (char4-len(CheckIn[i]))*' '


        
        display=Employee[i]+space1+Date[i]+space2+ShiftID[i]+space3+CheckIn[i]+space4+CheckOut[i]
        self.PayrollManagement.ListBox.insert('end', display)

    return NewDB

def Outstanding_Shifts(self):
    
    ShiftDB=Payroll_Read()    
    Employee=ShiftDB[0]
    Date=ShiftDB[1]
    ShiftID=ShiftDB[6]
    CheckIn=ShiftDB[3]
    CheckOut=ShiftDB[4]
    Approval=ShiftDB[7]

    del Employee[0]
    del Date[0]
    del ShiftID[0]
    del CheckIn[0]
    del CheckOut[0]
    del Approval[0]

    OEmployee=[]
    ODate=[]
    OShiftID=[]
    OCheckIn=[]
    OCheckOut=[]


    ShiftID2=ShiftID[::-1]
    for i in ShiftID2:
        number=int(i)-1
        if CheckOut[number]=='None':
            OEmployee.append(Employee[number])
            ODate.append(Date[number])
            OShiftID.append(ShiftID[number])
            OCheckIn.append(CheckIn[number])
            OCheckOut.append(CheckOut[number])

    for i in range(len(OCheckIn)):
        Hour=int(OCheckIn[i][0:2])
        if Hour==12:
            OCheckIn[i]=OCheckIn[i]+' PM'
        elif Hour==0:
            Hour='12'
            OCheckIn[i]=str(Hour)+OCheckIn[i][2::]+' AM'
        elif Hour>12 and Hour<22:
            Hour=str(Hour-12)
            OCheckIn[i]='0'+str(Hour)+OCheckIn[i][2::]+' PM'
        elif Hour>21:
            Hour=str(Hour-12)
            OCheckIn[i]=str(Hour)+OCheckIn[i][2::]+' PM'
        else:
            OCheckIn[i]=OCheckIn[i]+' AM'
            

    for i in range(len(ODate)):
        Day=ODate[i][8::]
        Month=ODate[i][5:7]
        Year=ODate[i][0:4]
        ODate[i]=Day+'/'+Month+'/'+Year

    OEmployee=OEmployee[::-1]
    ODate=ODate[::-1]
    OShiftID=OShiftID[::-1]
    OCheckIn=OCheckIn[::-1]
    OCheckOut=OCheckOut[::-1]

    NewDB=[]
    NewDB.append(OEmployee)
    NewDB.append(ODate)
    NewDB.append(OShiftID)
    NewDB.append(OCheckIn)
    NewDB.append(OCheckOut)

    self.PayrollManagement.ListBox.delete(0, 'end')
    for i in range(len(OEmployee)):

         ## Alotted Spaces ##
        char1 = 15 
        char2 = 15
        char3 = 8 
        char4 = 16

        space1 = (char1-len(OEmployee[i]))*' '
        space2 = (char2-len(ODate[i]))*' '
        space3 = (char3-len(OShiftID[i]))*' '
        space4 = (char4-len(OCheckIn[i]))*' '
        
        display=OEmployee[i]+space1+ODate[i]+space2+OShiftID[i]+space3+OCheckIn[i]+space4+OCheckOut[i]
        self.PayrollManagement.ListBox.insert('end', display)
    return NewDB
    
def CompleteShift(self, ID):
    ID=int(ID)
    Payroll = Payroll_Read()
    employeelist = Payroll[0]
    datelist = Payroll[1]
    shiftlist = Payroll[2]
    check_inlist = Payroll[3]
    check_outlist = Payroll[4]
    hourly_wagelist = Payroll[5]
    shift_idlist = Payroll[6]
    approval_list = Payroll[7]
    Shift=int(Outstanding_Shifts(self)[2][ID])
    check_outlist[Shift]=time.strftime('%H:%M:%S')
    all = [employeelist, datelist, shiftlist, check_inlist, check_outlist, hourly_wagelist, shift_idlist, approval_list]
    csvfile = 'Files/Modules/Database/PayrollDB.csv'
    WriteCSV (all, csvfile)
    #add_EmployeePay([Shift])
    Outstanding_Shifts(self)
    
    
def ApproveShift(self, ID):

    ID = int(ID)
    
    Payroll = Payroll_Read()
    employeelist = Payroll[0]
    datelist = Payroll[1]
    shiftlist = Payroll[2]
    check_inlist = Payroll[3]
    check_outlist = Payroll[4]
    hourly_wagelist = Payroll[5]
    shift_idlist = Payroll[6]
    approval_list = Payroll[7]


    Shift=int(FillDisplay(self)[2][ID])
    approval_list[Shift] = 'Yes'

    all = [employeelist, datelist, shiftlist, check_inlist, check_outlist, hourly_wagelist, shift_idlist, approval_list]
    
    add_EmployeePay([Shift])
    FillDisplay(self)

  
def AddShift(self, lis):

    emp_new = lis[0]
    date_new = lis[1]
    check_in_new = lis[2]
    check_out_new = lis [3]

    
    Payroll = Payroll_Read()
    employeelist = Payroll[0]
    datelist = Payroll[1]
    shiftlist = Payroll[2]
    check_inlist = Payroll[3]
    check_outlist = Payroll[4]
    hourly_wagelist = Payroll[5]
    shift_idlist = Payroll[6]
    approval_list = Payroll[7]

    user_accounts = Account_Read()
    employeelist_useraccounts = user_accounts[0]
    hourlywage_useraccounts = user_accounts[3]

    index = 'none'
    for i in range (len(employeelist_useraccounts)):
        
        if employeelist_useraccounts[i] == emp_new:
            index = i

         
    hourly_wage_new = hourlywage_useraccounts[index]
    approval_new = 'No'

    shiftcounter = 0
    for i in employeelist:
        if i == emp_new:
            shiftcounter+=1
    shift_amount_new = shiftcounter+1

    shiftid_new = 0

    if len(shift_idlist)==1:
        shiftid_new = 1
    else:
        shiftid = shift_idlist[-1]
        shiftid = int(shiftid)
        shiftid_new = shiftid+1

    listasofnow = [emp_new, date_new, shift_amount_new,check_in_new,check_out_new,hourly_wage_new,shiftid_new,approval_new]
    employee=employeelist+[listasofnow[0]]
    date = datelist+[listasofnow[1]]
    shift = shiftlist+[listasofnow[2]]
    check_in = check_inlist+[listasofnow[3]]
    check_outlist = check_outlist+[listasofnow[4]]   
    hourly_wage = hourly_wagelist+[listasofnow[5]]
    shift_id = shift_idlist+[listasofnow[6]]   
    approval_list = approval_list+[listasofnow[7]]

    all = [employee,date,shift, check_in, check_outlist, hourly_wage, shift_id, approval_list]                           
    csvfile = 'Files/Modules/Database/PayrollDB.csv'
    WriteCSV(all, csvfile)

    FillDisplay(self)

  
def EditShift(self, lis):

    ID = int(lis[0])
    check_in_new = lis[1]
    check_out_new = lis[2]
    
    Payroll = Payroll_Read()
    employeelist = Payroll[0]
    datelist = Payroll[1]
    shiftlist = Payroll[2]
    check_inlist = Payroll[3]
    check_outlist = Payroll[4]
    hourly_wagelist = Payroll[5]
    shift_idlist = Payroll[6]
    approval_list = Payroll[7]
    
    check_inlist[ID] = check_in_new
    check_outlist[ID] = check_out_new

    all = [employeelist, datelist, shiftlist, check_inlist, check_outlist, hourly_wagelist, shift_idlist, approval_list]
    csvfile ='Files/Modules/Database/PayrollDB.csv'
    WriteCSV(all, csvfile)

'''def tick2(self):
    
    global time1
    # get the current local time from the PC
    time2 = time.strftime(' %I:%M:%S %p')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        self.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    self.after(200, tick2, self)'''

def ShiftIDEdit(self, ID):
    ID=int(ID)
    Shift=int(FillDisplay(self)[2][ID])
    return Shift

def DateEdit(self, ID):
    ID=int(ID)
    Date=FillDisplay(self)[1][ID]
    return Date

def CheckInEdit(self, ID):
    ID=int(ID)
    CheckIn=FillDisplay(self)[3][ID]
    return CheckIn

def CheckOutEdit(self, ID):
    ID=int(ID)
    CheckOut=FillDisplay(self)[4][ID]
    return CheckOut
    
