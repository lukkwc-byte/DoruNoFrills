'''
    0.01 31/10/2011-Justin-Set up 2 displays
    0.02 01/11/2011-Justin-Logic for calculating total time worked per shift
    0.03 02/11/2011-Justin-Logic for calculating total amount earned per shift
    0.04 03/11/2011-Justin-Logic for calculating total sales per shift
    0.05 09/11/2011-Justin-Logic for calculating total shifts, time worked, amount earned in all shifts
    0.06 10/11/2011-Justin-Logic for calculating total sales in all shifs
    0.07 10/11/2011-Jonathan - Redone main logic for new CSVs
    0.08 10/14/2011-Jonathan - Redone logic for sales transactions
    0.09 10/15/2011-Jonathan - Logic update for transaction display
    0.10 10/21/2011-Jonathan - Date display is fixed, support for ALL

'''





import csv
from datetime import date
import datetime
from ReadCSV import *

def FillDisplay(self, bdate, edate, all):
    self.PurchReports.Display.delete(0, 'end')
    
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

    InventoryChangeslist= InvChange_Read()

    item_number=InventoryChangeslist[0] 
    item_name = InventoryChangeslist[1] 
    quantity_added = InventoryChangeslist[2]                                                      # Kyuho
    item_price = InventoryChangeslist[3]
    datelist = InventoryChangeslist[5]                                                         #
    timelist = InventoryChangeslist[6]
    del item_number[0]
    del item_name[0]
    del quantity_added[0]
    del item_price[0]
    del datelist[0]
    del timelist[0]


    
    applicabledates = []

    for i in range(len(datelist)):
        if all == True:
            datelist[i] = datelist[i].split(':')
            convert_date = datetime.date(int(datelist[i][0]),int(datelist[i][1]),int(datelist[i][2]))
            applicabledates.append(i)
        else:
            datelist[i] = datelist[i].split(':')
            convert_date = datetime.date(int(datelist[i][0]),int(datelist[i][1]),int(datelist[i][2]))
            if convert_date >= bdate and convert_date <= edate:
                applicabledates.append(i)

    itemnum = []
    itemname = []
    quantityadded = []
    itemprice = []
    dates = []
    times = []

    for ind in range(len(applicabledates)):
        itemnum.append(item_number[applicabledates[ind]])
        itemname.append(item_name[applicabledates[ind]])
        quantityadded.append(quantity_added[applicabledates[ind]])
        itemprice.append(item_price[applicabledates[ind]])
        dates.append(datelist[applicabledates[ind]])
        times.append(timelist[applicabledates[ind]])


    for i in range(len(applicabledates)):
        ## Alotted Spaces ##

        char1 = 8 # Max 6 Dig
        char2 = 18 # Max 15 Dig
        char3 = 9 # Max 4 Dig
        char4 = 14 #
        char5 = 19
        char6 = 9


        for a in range(len(dates)):
            date_i=str(dates[a][2])+'/'+str(dates[a][1])+'/'+str(dates[a][0])
        unitprice = itemprice[i]
        itemprice_1 = '$'+str("%.2f" % (float(itemprice[i])*float(quantityadded[i])))

        if int(times[i][0:2]) == 12:
            times_1 = times[i]
            ampm = 'PM'
        elif int(times[i][0:2]) < 12: 
            times_1 = times[i]
            ampm = 'AM'
        else:
            times_1 = str(int(times[i][0:2])-12)+times[i][2:]
            ampm = 'PM'
        
        space1 = (char1-len(itemnum[i]))*' '
        space2 = (char2-len(itemname[i]))*' '
        space3 = (char3-len(quantityadded[i]))*' '
        space4 = (char4-len(unitprice))*' '        
        space5 = (char5-len(itemprice_1))*' '
        space6 = (char6-len(times_1))*' '
            
        returnlist = str(itemnum[i])+space1+str(itemname[i])+space2+str(quantityadded[i])+space3+str(unitprice)+space4+str(itemprice_1)+space5+str(date_i)+' at '+str(times_1)+space6+ampm
        self.PurchReports.Display.insert('end', returnlist)
        
    if len(applicabledates) == 0:
        return False
