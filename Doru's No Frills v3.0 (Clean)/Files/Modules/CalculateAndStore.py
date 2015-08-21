'''
    Version x - Jonathan (added writing employee to SessionDB)

'''

import csv
import Check
import time
from WriteCSV import *
from ReadCSV import *

def Calculate(SessionNum):
    SessionNum=float(SessionNum)
    C_Registerlist = Cash_Read()
    datelist= C_Registerlist[0]
    sessionlist = C_Registerlist[1]
    item_number = C_Registerlist[2]
    item_name = C_Registerlist[3]
    item_qty = C_Registerlist[4]
    supplier_price = C_Registerlist[5]
    item_trans = C_Registerlist[6]
    store_price = C_Registerlist[7] 

    subtotal=0
    tax=0
    total=0
    date=None

    for i in range(1, len(sessionlist)):
        sessionlist[i]=float(sessionlist[i])

    for i in range(1, len(store_price)):
        store_price[i]=float(store_price[i])

    for i in range(1, len(item_qty)):
        item_qty[i]=float(item_qty[i])
    
    for i in range(len(sessionlist)):
        if sessionlist[i] == SessionNum:
            subtotal= subtotal + (store_price[i]*item_qty[i])
            date=datelist[i]
    tax=subtotal*0.13
    total=subtotal+tax

    moneyreturn=[]
    moneyreturn.append(subtotal)
    moneyreturn.append(tax)
    moneyreturn.append(total)
    moneyreturn.append(date)
    moneyreturn.append(SessionNum)
    return moneyreturn

def CalculateFinal(moneyreturn,paid):
    paid=float(paid)
    if moneyreturn[2]>paid:
        return False
    else:
        change=paid-moneyreturn[2]
        SessionDB_list=Session_Read()
        datelist2 = SessionDB_list[0]
        sessionlist2 = SessionDB_list[1]
        subtotallis= SessionDB_list[2]
        taxlis= SessionDB_list[3]
        totallis= SessionDB_list[4]
        employeelis = SessionDB_list[5]
        timelis = SessionDB_list[6]

        datelist2.append(moneyreturn[3])
        sessionlist2.append(moneyreturn[4])
        subtotallis.append(moneyreturn[0])
        taxlis.append(moneyreturn[1])
        totallis.append(moneyreturn[2])
        employeelis.append(Check.loggeduser)
        now_time = time.localtime()
        comp_time = '%.2d:%.2d:%.2d' % (now_time[3], now_time[4], now_time[5])
        timelis.append(comp_time)

        returnlist=[]
        returnlist.append(datelist2)
        returnlist.append(sessionlist2)
        returnlist.append(subtotallis)
        returnlist.append(taxlis)
        returnlist.append(totallis)
        returnlist.append(employeelis)
        returnlist.append(timelis)
        Store(returnlist)

        moneylist=[]
        moneylist.append(moneyreturn[0])
        moneylist.append(moneyreturn[1])
        moneylist.append(moneyreturn[2])
        change='$ ' + str("%.2f" % float(change))
        moneylist.append(change)    
        return moneylist

def Store(lis):
    csvfile3 = 'Files\Modules\Database\SessionDB.csv'
    WriteCSV(lis, csvfile3)
