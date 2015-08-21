'''
    0.01 31/10/2011-Justin-Set up 2 displays
    0.02 01/11/2011-Justin-Logic for calculating total time worked per shift
    0.03 02/11/2011-Justin-Logic for calculating total amount earned per shift
    0.04 03/11/2011-Justin-Logic for calculating total sales per shift
    0.05 09/11/2011-Justin-Logic for calculating total shifts, time worked, amount earned in all shifts
    0.06 11/11/2011-Justin-Logic for calculating total sales in all shifs
    0.07 11/11/2011-Jonathan - Redone main logic for new CSVs
    0.08 11/14/2011-Jonathan - Redone logic for sales transactions
    0.09 11/15/2011-Jonathan - Logic update for transaction display
    0.10 11/21/2011-Jonathan - Date display is fixed, support for ALL
    0.11 11/24/2011-Jonathan - Beginning support for Employee totals - not complete
    0.12 11/29/2011-Jonathan - Finalized version
    0.13 10/29/2011-Jonathan - Support for elimination of Payroll.csv - all from PayDB

'''





import csv
from datetime import date
import datetime
from ReadCSV import *


def FillDisplay(self, bdate, edate, all):
    self.HRReports.Display.delete(0, 'end')

    if all == False:
        # Convert Dates #
        bdate = bdate.split('/')
        edate = edate.split('/')
        for i in range(len(bdate)):
            bdate[i] = int(bdate[i])
        for i in range(len(edate)):
            edate[i] = int(edate[i])
            
        bdate=datetime.date(bdate[2],bdate[1],bdate[0])
        edate=datetime.date(edate[2],edate[1],edate[0])

    # Payroll Stuff #
    Payroll = EmployeePay_Read()
    
    Employee = Payroll[0]
    Date = Payroll[1]
    Shift = Payroll[2]
    Time_Worked = Payroll[4]
    Paid = Payroll[3]
    Hourly_Wage=Payroll[5]
    
    del Employee[0]
    del Shift[0]
    del Date[0]
    del Time_Worked[0]
    del Hourly_Wage[0]
    del Paid[0]

    trueindexs = []
    for i in range(len(Date)):
        if all == True:
            Date[i] = Date[i].split('-')
            convert_date = datetime.date(int(Date[i][0]),int(Date[i][1]),int(Date[i][2]))
            trueindexs.append(i)
        else:
            Date[i] = Date[i].split('-')
            convert_date = datetime.date(int(Date[i][0]),int(Date[i][1]),int(Date[i][2]))
            if convert_date >= bdate and convert_date <= edate:
                trueindexs.append(i)
    new_paid = []
    new_employee = []
    new_shift = []
    new_date = []
    new_time_worked = []
    new_hourly_wage = []
   
    for i in trueindexs:
        new_paid.append(Paid[i])
        new_employee.append(Employee[i])
        new_shift.append(Shift[i])
        new_date.append(Date[i])
        new_time_worked.append(Time_Worked[i])
        new_hourly_wage.append(Hourly_Wage[i])


    # Cash Stuff #

    CashList = Cash_Read()


    CashDate = CashList[0]
    CashEmp = CashList[9]

    del CashDate[0]
    del CashEmp[0]

    cashindexs = []
    for i in range(len(CashDate)):
        if all == True:
            CashDate[i] = CashDate[i].split(':')
            cashindexs.append(i)
        else:
            CashDate[i] = CashDate[i].split(':')
            if CashDate[i] in new_date:
                cashindexs.append(i)
            
    for i in range(len(new_date)):
        salesnum = 0      
        for h in range(len(CashDate)):
            if new_date[i] == CashDate[h]:
                if CashEmp[h] == new_employee[i]:
                    salesnum += 1
        salesnum_1 = str(salesnum) # 7
        new_paid_1 = '$'+str("%.2f" % (float(new_paid[i])))
        new_employee_1 = str(new_employee[i])
        new_shift_1 = str(new_shift[i])   
        new_date_1 = new_date[i][2]+'/'+new_date[i][1]+'/'+new_date[i][0]
        new_time_worked_1 = str("%.4f" % (float(new_time_worked[i])))+' hr(s)'
        new_hourly_wage_1 = '$'+str("%.3f" % (float(new_hourly_wage[i])))

        ## Alotted Spaces ##
        char1 = 18 # Max 12 Dig
        char2 = 12 # Max 6 Dig
        char3 = 14 # Max 12 Dig
        char4 = 16 # Max 6 Dig
        char5 = 11 # Max 5 Dig
        char6 = 12 # Max 6 Dig
        char7 = 12 # Max 6 Dig
        
        space1 = (char1-len(new_employee_1))*' ' # Employee Name
        space2 = (char2-len(new_shift_1))*' ' # Shift ID
        space3 = (char3-len(new_date_1))*' '
        space4 = (char4-len(new_time_worked_1))*' '
        space5 = (char5-len(new_hourly_wage_1))*' '
        space6 = (char6-len(new_paid_1))*' '

    
        display = ''+new_employee_1+space1+new_shift_1+space2+new_date_1+space3+new_time_worked_1+space4+new_hourly_wage_1+space5+new_paid_1
        self.HRReports.Display.insert('end', display)

    if len(new_date) == 0:
        return False

def FillSpecDisplay(self, bdate, edate, all):

    given_employee = self.HRReports.option_en.get()

    if all == False:
        # Convert Dates #
        bdate = bdate.split('/')
        edate = edate.split('/')
        for i in range(len(bdate)):
            bdate[i] = int(bdate[i])
        for i in range(len(edate)):
            edate[i] = int(edate[i])
            
        bdate=datetime.date(bdate[2],bdate[1],bdate[0])
        edate=datetime.date(edate[2],edate[1],edate[0])

    # Payroll Stuff #
    

    Payroll1 = Payroll_Read()
    Payroll2 = EmployeePay_Read()
    
    Employee = Payroll2[0]
    Date = Payroll2[1]
    Shift = Payroll2[2]
    Time_Worked = Payroll2[4]
    Paid = Payroll2[3]
    Hourly_Wage=Payroll1[5]
    
    del Employee[0]
    del Shift[0]
    del Date[0]
    del Time_Worked[0]
    del Hourly_Wage[0]
    del Paid[0]

    trueindexs = []
    for i in range(len(Date)):
        if Employee[i] == given_employee:
            if all == True:
                Date[i] = Date[i].split('-')
                convert_date = datetime.date(int(Date[i][0]),int(Date[i][1]),int(Date[i][2]))
                trueindexs.append(i)
            else:
                Date[i] = Date[i].split('-')
                convert_date = datetime.date(int(Date[i][0]),int(Date[i][1]),int(Date[i][2]))
                if convert_date >= bdate and convert_date <= edate:
                    trueindexs.append(i)
            
    new_paid = []
    new_employee = []
    new_shift = []
    new_date = []
    new_time_worked = []
    new_hourly_wage = []


    for i in trueindexs:
        new_paid.append(Paid[i])
        new_employee.append(Employee[i])
        new_shift.append(Shift[i])
        new_date.append(Date[i])
        new_time_worked.append(Time_Worked[i])
        new_hourly_wage.append(Hourly_Wage[i])

    if new_employee == []:
        return False
    
    # Cash Stuff #

    CashDB = Cash_Read()

    CashDate = CashDB[0]
    CashEmp = CashDB[9]

    del CashDate[0]
    del CashEmp[0]

    cashindexs = []
    for i in range(len(CashDate)):
        if CashEmp[i] == given_employee:
            if all == True:
                CashDate[i] = CashDate[i].split(':')
                cashindexs.append(i)
            else:
                CashDate[i] = CashDate[i].split(':')
                if CashDate[i] in new_date:
                    cashindexs.append(i)

    new_cash_date = []
    new_cash_emp = []

    for i in cashindexs:
        new_cash_date.append(CashDate[i])
        new_cash_emp.append(CashEmp[i])

    shifts_num = 0
    new_paid_1 = 0
    new_time_worked_1 = 0
    
    for i in range(len(new_date)):
        shifts_num += 1
        
    salesnum = len(new_cash_emp)
    
    for i in range(len(trueindexs)):
        new_paid_1 += float(new_paid[i])
        new_time_worked_1 += float(new_time_worked[i])
        
    salesnum_1 = str(salesnum)
    new_paid_1 = '$'+str("%.2f" % (float(new_paid_1)))
    new_employee_1 = str(new_employee[0])
    shifts_num = str(shifts_num)   
    new_time_worked_1 = str("%.4f" % (float(new_time_worked_1)))+' hr(s)'
    new_hourly_wage_1 = '$'+str("%.3f" % (float(new_hourly_wage[0])))

    self.HRReports.spec1.config(state='normal')
    self.HRReports.spec1.delete(0, 'end')
    self.HRReports.spec1.insert('end', shifts_num)
    self.HRReports.spec1.config(state='readonly')

    self.HRReports.spec2.config(state='normal')
    self.HRReports.spec2.delete(0, 'end')
    self.HRReports.spec2.insert('end', new_time_worked_1)
    self.HRReports.spec2.config(state='readonly')
    
    self.HRReports.spec4.config(state='normal')
    self.HRReports.spec4.delete(0, 'end')
    self.HRReports.spec4.insert('end', new_paid_1)
    self.HRReports.spec4.config(state='readonly')
    
    self.HRReports.spec5.config(state='normal')
    self.HRReports.spec5.delete(0, 'end')
    self.HRReports.spec5.insert('end', salesnum_1)
    self.HRReports.spec5.config(state='readonly')



