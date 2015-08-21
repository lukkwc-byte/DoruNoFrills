'''
    Version 0.01 12/10/2011 - Mackenzie
    Version 0.02 13/10/2011 - Mackenzie
    Version 0.03 14/10/2011 - Mackenzie file finished

'''

import csv
from ReadCSV import *
from WriteCSV import *


def add_EmployeePay (shiftID_list):
    if len(shiftID_list) == 1:
        Payrolllistmack = Payroll_Read()
        employeelist = Payrolllistmack[0]
        datelist = Payrolllistmack[1]
        shiftlist = Payrolllistmack[2]
        check_inlist = Payrolllistmack[3]
        check_outlist = Payrolllistmack[4]
        hourly_wagelist = Payrolllistmack[5]
        shift_idlist = Payrolllistmack[6]
        approval_list = Payrolllistmack[7]
        

        all = [employeelist,datelist,shiftlist,check_inlist,check_outlist,hourly_wagelist, shift_idlist, approval_list]
        if approval_list[shiftID_list[0]] == 'No':
            approval = 'yes'    
            approval_list[shiftID_list[0]]=approval

            hourlywage=hourly_wagelist[shiftID_list[0]]

            csvfile = 'Files\Modules\Database\PayrollDB.csv'
            WriteCSV(all, csvfile)
            

            
            check_intime = check_inlist[-1]
            check_intimehour = float(check_intime[:2])
            check_intimehour = check_intimehour*3600.00
            check_intimeminutes = float(check_intime[3:5])
            check_intimeminutes=check_intimeminutes*60.00
            check_intimeseconds = float(check_intime[6:])
            check_intotal = check_intimehour+check_intimeminutes+check_intimeseconds
            check_intotal = check_intotal/3600.00
            check_outtime = check_outlist[-1]
            check_outtimehour = float(check_outtime[:2])
            check_outtimehour = check_outtimehour*3600.00
            check_outtimeminutes = float(check_outtime[3:5])
            check_outtimeminutes=check_outtimeminutes*60.00
            check_outtimeseconds = float(check_outtime[6:])
            check_outtotal = check_outtimehour+check_outtimeminutes+check_outtimeseconds
            check_outtotal = check_outtotal/3600.00
            time_worked = check_outtotal - check_intotal
            time_worked = float(time_worked)  
            hourlywage = hourly_wagelist[-1]
            hourlywage =  float(hourlywage)
            paid = time_worked * hourlywage
            returnlis = [employeelist,datelist,shift_idlist,time_worked, paid, hourlywage]
            
            EmployeePayList = EmployeePay_Read()
            employee1 = EmployeePayList[0]
            date1 = EmployeePayList[1]
            shiftID1 = EmployeePayList[2]
            time_worked1 = EmployeePayList[4]
            paid1 = EmployeePayList[3]
            hour_wage1 = EmployeePayList[5]
            
            employee1.append(returnlis[0][-1])
            date1.append(returnlis[1][-1])
            shiftID1.append(shiftID_list[0])
            time_worked1.append(returnlis[3])
            paid1.append(returnlis[4])
            hour_wage1.append(returnlis[5])
            all2=[employee1,date1,shiftID1,paid1,time_worked1,hour_wage1]
            csvfile = 'Files\Modules\Database\EmployeePayDB.csv'
            WriteCSV (all2, csvfile)
            
    if len(shiftID_list) > 1:
        Payrolllistmack2 = Payroll_Read()
        employeelist = Payrolllistmack2[0]
        datelist = Payrolllistmack2[1]
        shiftlist = Payrolllistmack2[2]
        check_inlist = Payrolllistmack2[3]
        check_outlist = Payrolllistmack2[4]
        hourly_wagelist = Payrolllistmack2[5]
        shift_idlist = Payrolllistmack2[6]
        approval_list = Payrolllistmack2[7]

        EmployeePayList2 = EmployeePay_Read()
        employee1 = EmployeePayList2[0]
        date1 = EmployeePayList2[1]
        shiftID1 = EmployeePayList2[2]
        time_worked1 = EmployeePayList2[4]
        paid1 = EmployeePayList2[3]
        hour_wage1 = EmployeePayList2[5]

        for i in range (len(shiftID_list)):
           
            a=shiftID_list[i]
            if approval_list[a] == 'No':
                approval = 'yes'    
                
                approval_list[a]=approval
                hourlywage=hourly_wagelist[a]

                all = [employeelist,datelist,shiftlist,check_inlist,check_outlist,hourly_wagelist, shift_idlist, approval_list]

                csvfile = 'Files\Modules\Database\PayrollDB.csv'
                WriteCSV(all,csvfile)
                

                
                check_intime = check_inlist[-1]
                check_intimehour = float(check_intime[:2])
                check_intimehour = check_intimehour*3600.00
                check_intimeminutes = float(check_intime[3:5])
                check_intimeminutes=check_intimeminutes*60.00
                check_intimeseconds = float(check_intime[6:])
                check_intotal = check_intimehour+check_intimeminutes+check_intimeseconds
                check_intotal = check_intotal/3600.00
                check_outtime = check_outlist[-1]
                check_outtimehour = float(check_outtime[:2])
                check_outtimehour = check_outtimehour*3600.00
                check_outtimeminutes = float(check_outtime[3:5])
                check_outtimeminutes=check_outtimeminutes*60.00
                check_outtimeseconds = float(check_outtime[6:])
                check_outtotal = check_outtimehour+check_outtimeminutes+check_outtimeseconds
                check_outtotal = check_outtotal/3600.00
                time_worked = check_outtotal - check_intotal
                time_worked = float(time_worked)  
                hourlywage = hourly_wagelist[-1]
                hourlywage =  float(hourlywage)
                paid = time_worked * hourlywage
                returnlis = [employeelist,datelist,shift_idlist,time_worked, paid, hourlywage]
                
                
                
                employee1.append(returnlis[0][-1])
                date1.append(returnlis[1][-1])
                shiftID1.append(a)
                time_worked1.append(returnlis[3])
                paid1.append(returnlis[4])
                hour_wage1.append(returnlis[5])
                 
                all2=[employee1,date1,shiftID1,paid1,time_worked1,hour_wage1]
                csvfile = 'Files\Modules\Database\EmployeePayDB.csv'
                WriteCSV(all2, csvfile)


# To test approving shifts, feed lis1 the SHIFT ID's that need to be approved + paid.
#lis1 = [1]
#add_EmployeePay(lis1)
