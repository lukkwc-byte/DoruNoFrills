import csv
from datetime import date
import datetime

def FillDisplay(self, id):
    Cashlist=[]
    csvfile='Files\Modules\Database\cashregister.csv'                                   # Kyuho
    CashDB = csv.reader(open(csvfile, 'rb'), delimiter = ',', quotechar = '|')
    for listrow in CashDB:
        Cashlist.append(listrow)
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
        if transid[i]==id:
            applicabledates.append(i)
    if len(applicabledates)==0:
        return False
    else:
        itemnum = []
        transids=[]
        itemnames = []
        qty = []
        itemprices = []
        dates = []
        for ind in range(len(applicabledates)):
            itemnum.append(itemnumber[applicabledates[ind]])
            transids.append(transid[applicabledates[ind]])
            itemnames.append(itemname[applicabledates[ind]])
            qty.append(itemqty[applicabledates[ind]])
            itemprices.append(storeprice[applicabledates[ind]])
            dates.append(datelist[applicabledates[ind]])
    for i in range(len(applicabledates)):
        ## Alotted Spaces ##
        char1 = 8 # Max 6 Dig
        char2 = 18 # Max 15 Dig
        char3 = 6 # Max 4 Dig
        char4 = 10 # Max 8 Dig
        char5 = 5
        char6 = 6
        
        space1 = (char1-len(itemnum[i]))*' '
        space2 = (char2-len(transids[i]))*' '
        space3 = (char3-len(itemnames[i]))*' '
        space4 = (char4-len(qty[i]))*' '
        space5 = (char5-len(itemprices[i]))*' '
        space6 = (char6-len(dates[i])) * ' '

        itemlist = itemnum[i]+space1+transid[i]+space2+itemnames[i]+space3+qty[i]+space4+itemprices[i]+space5+dates[i]+space6
        self.SalesReports.TransDisplay.insert('end', itemlist)
