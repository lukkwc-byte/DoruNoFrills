'''

    Version 0.01 17/10/2011 - Mackenzie
    Version 0.02 18/10/2011 - Mackenzie
    Version 0.03 10/11/2011 - Jonathan (adjusted Rounding)
    
'''
import PayrollPayments
import csv
import Check
import datetime
from ReadCSV import *
from WriteCSV import *
   

def Check_in():
    user = Check.loggeduser #who is logged in
    hourly_wage = Check.hourlywage #hourly wage from Check file
    Payrolllist = Payroll_Read()
    employeelist = Payrolllist[0]
    datelist = Payrolllist[1]
    shiftlist = Payrolllist[2]
    check_inlist = Payrolllist[3]
    check_outlist = Payrolllist[4]
    hourly_wagelist = Payrolllist[5]
    shift_idlist= Payrolllist[6]
    approval_list = Payrolllist[7]
    shiftcounter=0
    for i in employeelist:
        if i == user:
            shiftcounter+=1
    shift_amount = shiftcounter+1
    if len(shift_idlist)==1:
        shiftid=1
    if len(shift_idlist)> 1:
        shiftid= shift_idlist[-1]
        shiftid = int(shiftid)
        shiftid +=1
        

    
            
    from datetime import datetime
    datetime = str(datetime.now())
    currentdate=datetime[:10]
    currenttime=datetime[11:19]
    check_outtime= 'None'
    approval = 'No'
    listasofcheckin = [user, currentdate, shift_amount,currenttime,check_outtime,hourly_wage,shiftid,approval]
    employee=employeelist+[listasofcheckin[0]]
    date = datelist+[listasofcheckin[1]]
    shift = shiftlist+[listasofcheckin[2]]
    check_in = check_inlist+[listasofcheckin[3]]
    check_outlist.append(check_outtime)
    approval_list.append(approval)
    hourly_wage = hourly_wagelist+[listasofcheckin[5]]
    shift_id = shift_idlist+[listasofcheckin[6]]
    all = [employee,date,shift,check_in,check_outlist,hourly_wage,shift_id,approval_list]
    csvfile = 'Files\Modules\Database\PayrollDB.csv'
    WriteCSV(all, csvfile)
    return 


def Check_out():
    user = Check.loggeduser
    from datetime import datetime
    datetime = str(datetime.now())
    currenttime=datetime[11:19]
    check_out = currenttime
    Payrolllist2 = Payroll_Read()
    employeelist = Payrolllist2[0]
    datelist = Payrolllist2[1]
    shiftlist = Payrolllist2[2]
    check_inlist = Payrolllist2[3]
    check_outlist = Payrolllist2[4]
    hourly_wagelist = Payrolllist2[5]
    shift_idlist = Payrolllist2[6]
    approval_list = Payrolllist2[7]
    
    applicable = []
    number=0
    for i in employeelist:
        if i == user:
        
            applicable.append(number)
        number+=1
    index = int(applicable[-1])
    check_outlist[index] = check_out

    all = [employeelist,datelist,shiftlist,check_inlist,check_outlist,hourly_wagelist, shift_idlist, approval_list]
    csvfile = 'Files\Modules\Database\PayrollDB.csv'
    WriteCSV(all, csvfile)
    lis1 = ([int(shift_idlist[-1])])
    #PayrollPayments.add_EmployeePay(lis1)
