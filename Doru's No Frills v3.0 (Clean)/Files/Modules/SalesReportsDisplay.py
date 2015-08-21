'''
    0.01 29/11/2011- Jonathan - initial logic
    0.02 08/12/2011- Jonathan & Kevin - completed logic
'''





import csv
from datetime import date
import datetime
from ReadCSV import *

def FillDisplay(self, bdate, edate, all):
    self.SalesReports.Display.delete(0, 'end')

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

    # Cash Stuff #    
    
    Sessionlist = Session_Read()
    
    date = Sessionlist[0]
    transnum = Sessionlist[1]
    subtotal = Sessionlist[2]
    tax = Sessionlist[3]
    total = Sessionlist[4]
    employee = Sessionlist[5]
    time = Sessionlist[6]

    del date[0]
    del transnum[0]
    del subtotal [0]
    del tax[0]
    del total[0]
    del employee[0]
    del time[0]
    
    trueindexs = []
    
    for i in range(len(date)):
        if all == True:
            date[i] = date[i].split(':')
            convert_date = datetime.date(int(date[i][0]),int(date[i][1]),int(date[i][2]))
            trueindexs.append(i)
        else:
            date[i] = date[i].split(':')
            convert_date = datetime.date(int(date[i][0]),int(date[i][1]),int(date[i][2]))
            if convert_date >= bdate and convert_date <= edate:
                trueindexs.append(i)

    if len(trueindexs) == 0: # Nothing applicable
        return False
    
    new_date = []
    new_transnum = []
    new_subtotal = []
    new_tax = []
    new_total = []
    new_employee = []
    new_time = []
   
    for i in trueindexs:
        new_date.append(date[i])
        new_employee.append(employee[i])
        new_transnum.append(transnum[i])
        new_tax.append(tax[i])
        new_total.append(total[i])
        new_subtotal.append(subtotal[i])
        new_time.append(time[i])
            
    for i in range(len(new_date)):
        new_tax_1 = '$'+str("%.2f" % (float(new_tax[i])))
        new_total_1 = '$'+str("%.2f" % (float(new_total[i])))
        new_subtotal_1 = '$'+str("%.2f" % (float(new_subtotal[i])))
        new_employee_1 = str(new_employee[i])
        new_transnum_1 = str("%.0f" % (float(new_transnum[i]))) 
        new_date_1 = new_date[i][2]+'/'+new_date[i][1]+'/'+new_date[i][0]
        new_time_1 = str(new_time[i])

        
        if int(new_time_1[0:2]) == 12:
            times_1 = new_time_1
            ampm = 'PM'
        elif int(new_time_1[0:2]) < 12:
            times_1 = new_time_1
            ampm = 'AM'
        else:
            times_1 = str(int(new_time_1[0:2])-12)+new_time_1[2:]
            ampm = 'PM'
        
        ## Alotted Spaces ##
        char1 = 12 # Max 12 Dig
        char2 = 14 # Max 6 Dig
        char3 = 14 # Max 12 Dig
        char4 = 14 # Max 6 Dig
        char5 = 14 # Max 5 Dig
        char6 = 9 # Max 6 Dig

      
        
        space1 = (char1-len(new_transnum_1))*' ' # Employee Name
        space2 = (char2-len(new_subtotal_1))*' ' # Shift ID
        space3 = (char3-len(new_tax_1))*' '
        space4 = (char4-len(new_total_1))*' '
        space5 = (char5-len(new_employee_1))*' '
        space6 = (char6-len(times_1))*' '

        display = ''+new_transnum_1+space1+new_subtotal_1+space2+new_tax_1+space3+new_total_1+space4+new_employee_1+space5+new_date_1+' at '+times_1+space6+ampm
        self.SalesReports.Display.insert('end', display)

def FillTransDisplay(self, ID):
    self.SalesReports.TransDisplay.delete(0, 'end')

    Cashlist= Cash_Read()
    
    datelist=Cashlist[0]
    transid=Cashlist[1]
    itemnumber=Cashlist[2]
    itemname=Cashlist[3]
    itemqty=Cashlist[4]
    storeprice=Cashlist[5]
    del datelist[0]
    del transid[0]
    del itemnumber[0]
    del itemqty[0]
    del itemname[0]
    del storeprice[0]
    applicabledates = []
    for i in range(len(datelist)):
        datelist[i] = datelist[i].split(':')
        convert_date = datetime.date(int(datelist[i][0]),int(datelist[i][1]),int(datelist[i][2]))        
    for i in range(len(transid)):
        if transid[i]==ID:
            applicabledates.append(i)
    if len(applicabledates)==0:
        return False
    else:
        itemnum = []
        itemnames = []
        qty = []
        itemprices = []
        dates = []
        for ind in range(len(applicabledates)):
            itemnum.append(itemnumber[applicabledates[ind]])
            itemnames.append(itemname[applicabledates[ind]])
            qty.append(itemqty[applicabledates[ind]])
            itemprices.append(storeprice[applicabledates[ind]])
    for i in range(len(applicabledates)):
        totalprice = '$'+str("%.2f" % (float(itemprices[i])*float(qty[i])))
        itemprice = '$'+str("%.2f" % (float(itemprices[i])))
        ## Alotted Spaces ##
        char1 = 15 # Max 6 Dig
        char2 = 25 # Max 15 Dig
        char3 = 15 # Max 4 Dig
        char4 = 16 # Max 8 Dig
        
        space1 = (char1-len(itemnum[i]))*' '
        space2 = (char2-len(itemnames[i]))*' '
        space3 = (char3-len(qty[i]))*' '
        space4 = (char4-len(itemprice))*' '


        itemlist = str(itemnum[i])+space1+str(itemnames[i])+space2+str(qty[i])+space3+str(itemprice)+space4+str(totalprice)
        self.SalesReports.TransDisplay.insert('end', itemlist)
