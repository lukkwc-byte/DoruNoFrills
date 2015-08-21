import csv
def Account_Read():
    C_Registerlist = [] # csv register
    cash_csvfile = 'Files\Modules\Database\useraccounts.csv'
    C_RegisterDB = csv.reader(open(cash_csvfile, 'rb'), delimiter = ',', quotechar = '|')
    for listrow in C_RegisterDB:
        C_Registerlist.append(listrow)
    date=[]
    session=[]
    item_number=[]
    item_name=[]
    item_qty=[]
    store_price=[]
    for i in range(len(C_Registerlist)):
        date.append(C_Registerlist[i][0])
        session.append(C_Registerlist[i][1])
        item_number.append(C_Registerlist[i][2])
        item_name.append(C_Registerlist[i][3])
        item_qty.append(C_Registerlist[i][4])
        store_price.append(C_Registerlist[i][5])
    returnlist=[date, session, item_number, item_name, item_qty, store_price]    
    return returnlist

def Cash_Read():
    C_Registerlist = [] # csv register
    cash_csvfile = 'Files\Modules\Database\cashregister.csv'
    C_RegisterDB = csv.reader(open(cash_csvfile, 'rb'), delimiter = ',', quotechar = '|')
    for listrow in C_RegisterDB:
        C_Registerlist.append(listrow)
    date=[]
    session=[]
    item_number=[]
    item_name=[]
    item_qty=[]
    supplier_price=[]
    item_trans=[]
    store_price=[]
    item_time=[]
    employee=[]
    for i in range(len(C_Registerlist)):
        date.append(C_Registerlist[i][0])
        session.append(C_Registerlist[i][1])
        item_number.append(C_Registerlist[i][2])
        item_name.append(C_Registerlist[i][3])
        item_qty.append(C_Registerlist[i][4])
        supplier_price.append(C_Registerlist[i][5])
        item_trans.append(C_Registerlist[i][6])
        store_price.append(C_Registerlist[i][7])
        item_time.append(C_Registerlist[i][8])
        employee.append(C_Registerlist[i][9])
    returnlist=[date, session, item_number, item_name, item_qty, supplier_price, item_trans, store_price, item_time, employee]    
    return returnlist

def Check_Read():
    CheckList = [] 
    check_csvfile = 'Files\Modules\Database\Check.csv'
    CheckDB = csv.reader(open(check_csvfile, 'rb'), delimiter = ',', quotechar = '|')
    for listrow in CheckDB:
        CheckList.append(listrow)
    session=[]
    for i in range(len(CheckList)):
        session.append(CheckList[i][0])
    returnlist=[session]
    return returnlist

def EmployeePay_Read():
    EmployeePay = [] # csv register
    cash_csvfile = 'Files\Modules\Database\EmployeePayDB.csv'
    EmployeePayDB = csv.reader(open(cash_csvfile, 'rb'), delimiter = ',', quotechar = '|')
    for listrow in EmployeePayDB:
        EmployeePay.append(listrow)
    Employee=[]
    Date=[]
    Shift=[]
    Time_Worked=[]
    Paid=[]
    Wage=[]
    for i in range(len(EmployeePay)):
        Employee.append(EmployeePay[i][0])
        Date.append(EmployeePay[i][1])
        Shift.append(EmployeePay[i][2])
        Time_Worked.append(EmployeePay[i][3])
        Paid.append(EmployeePay[i][4])
        Wage.append(EmployeePay[i][5])
    returnlist=[Employee, Date, Shift, Time_Worked, Paid, Wage]    
    return returnlist

def InvChange_Read():
    InvChangeList = [] # csv register
    Inventorychange_csvfile = 'Files\Modules\Database\inventorychange.csv'
    InvChangeDB = csv.reader(open(Inventorychange_csvfile, 'rb'), delimiter = ',', quotechar = '|')
    for listrow in InvChangeDB:
        InvChangeList.append(listrow)
    itemnumber=[]
    itemname=[]
    quantityadded=[]
    itemprice=[]
    total=[]
    date=[]
    time=[]
    for i in range(len(InvChangeList)):
        itemnumber.append(InvChangeList[i][0])
        itemname.append(InvChangeList[i][1])
        quantityadded.append(InvChangeList[i][2])
        itemprice.append(InvChangeList[i][3])
        total.append(InvChangeList[i][4])
        date.append(InvChangeList[i][5])
        time.append(InvChangeList[i][6])
    returnlist=[itemnumber, itemname, quantityadded, itemprice, total, date, time]    
    return returnlist

def InventoryLoc_Read():
    InventoryLocList = [] # csv register
    InventoryLoc_csvfile = 'Files\Modules\Database\inventorylocator.csv'
    InvChangeDB = csv.reader(open(InventoryLoc_csvfile, 'rb'), delimiter = ',', quotechar = '|')
    for listrow in InvChangeDB:
        InventoryLocList.append(listrow)
    itemnumber=[]
    aisle1=[]
    aisle2=[]
    aisle3=[]
    aisle4=[]
    aisle5=[]
    aisle6=[]
    aisle7=[]
    aisle8=[]
    for i in range(len(InventoryLocList)):
        itemnumber.append(InventoryLocList[i][0])
        aisle1.append(InventoryLocList[i][1])
        aisle2.append(InventoryLocList[i][2])
        aisle3.append(InventoryLocList[i][3])
        aisle4.append(InventoryLocList[i][4])
        aisle5.append(InventoryLocList[i][5])
        aisle6.append(InventoryLocList[i][6])
        aisle7.append(InventoryLocList[i][7])
        aisle8.append(InventoryLocList[i][8])
    returnlist=[itemnumber,aisle1,aisle2,aisle3,aisle4,aisle5,aisle6,aisle7,aisle8]
    return returnlist

def HistoryInvLoc_Read():
    InventoryLocList = [] # csv register
    InventoryLoc_csvfile = 'Files\Modules\Database\historyinvloc.csv'
    InvChangeDB = csv.reader(open(InventoryLoc_csvfile, 'rb'), delimiter = ',', quotechar = '|')
    for listrow in InvChangeDB:
        InventoryLocList.append(listrow)
    itemnumber=[]
    aisle1=[]
    aisle2=[]
    aisle3=[]
    aisle4=[]
    aisle5=[]
    aisle6=[]
    aisle7=[]
    aisle8=[]
    for i in range(len(InventoryLocList)):
        itemnumber.append(InventoryLocList[i][0])
        aisle1.append(InventoryLocList[i][1])
        aisle2.append(InventoryLocList[i][2])
        aisle3.append(InventoryLocList[i][3])
        aisle4.append(InventoryLocList[i][4])
        aisle5.append(InventoryLocList[i][5])
        aisle6.append(InventoryLocList[i][6])
        aisle7.append(InventoryLocList[i][7])
        aisle8.append(InventoryLocList[i][8])
    returnlist=[itemnumber,aisle1,aisle2,aisle3,aisle4,aisle5,aisle6,aisle7,aisle8]
    return returnlist

def Inv_Read():
    Invlist = []
    inv_csvfile = 'Files\Modules\Database\inventory.csv'
    InvDB = csv.reader(open(inv_csvfile, 'rb'), delimiter = ',', quotechar = '|')
    for listrow in InvDB:
        Invlist.append(listrow)
    itemnumber=[]
    itemname=[]
    itemquantity=[]
    supplierprice=[]
    storeprice=[]
    for i in range(len(Invlist)):
        itemnumber.append(Invlist[i][0])
        itemname.append(Invlist[i][1])
        itemquantity.append(Invlist[i][2])
        supplierprice.append(Invlist[i][3])
        storeprice.append(Invlist[i][4])
    returnlist=[itemnumber,itemname,itemquantity,supplierprice,storeprice]
    return returnlist

def InvCSV_Read(inv_csvfile):
    Invlist = []
    InvDB = csv.reader(open(inv_csvfile, 'rb'), delimiter = ',', quotechar = '|')
    for listrow in InvDB:
        Invlist.append(listrow)
    itemnumber=[]
    itemname=[]
    itemquantity=[]
    supplierprice=[]
    storeprice=[]
    for i in range(len(Invlist)):
        itemnumber.append(Invlist[i][0])
        itemname.append(Invlist[i][1])
        itemquantity.append(Invlist[i][2])
        supplierprice.append(Invlist[i][3])
        storeprice.append(Invlist[i][4])
    returnlist=[itemnumber,itemname,itemquantity,supplierprice,storeprice]
    return returnlist

def Payroll_Read():
    PayrollList = [] # csv register
    Payroll_csvfile = 'Files\Modules\Database\PayrollDB.csv'
    PayrollDB = csv.reader(open(Payroll_csvfile, 'rb'), delimiter = ',', quotechar = '|')
    for listrow in PayrollDB:
        PayrollList.append(listrow)
    Employee=[]
    Date=[]
    Shift=[]
    Checkin=[]
    Checkout=[]
    Hourlywage=[]
    ShiftID=[]
    Approval=[]
    for i in range(len(PayrollList)):
        Employee.append(PayrollList[i][0])
        Date.append(PayrollList[i][1])
        Shift.append(PayrollList[i][2])
        Checkin.append(PayrollList[i][3])
        Checkout.append(PayrollList[i][4])
        Hourlywage.append(PayrollList[i][5])
        ShiftID.append(PayrollList[i][6])
        Approval.append(PayrollList[i][7])
    returnlist=[Employee,Date,Shift,Checkin,Checkout,Hourlywage,ShiftID,Approval]    
    return returnlist

def Session_Read():
    SessionList = [] 
    session_csvfile = 'Files\Modules\Database\SessionDB.csv'
    SessionDB = csv.reader(open(session_csvfile, 'rb'), delimiter = ',', quotechar = '|')
    for listrow in SessionDB:
        SessionList.append(listrow)
    date=[]
    session=[]
    subtotal=[]
    tax=[]
    total=[]
    employee=[]
    time_lis=[]
    for i in range(len(SessionList)):
        date.append(SessionList[i][0])
        session.append(SessionList[i][1])
        subtotal.append(SessionList[i][2])
        tax.append(SessionList[i][3])
        total.append(SessionList[i][4])
        employee.append(SessionList[i][5])
        time_lis.append(SessionList[i][6])
        
    returnlist=[date,session,subtotal,tax,total,employee,time_lis]    
    return returnlist

def Undisplayed_Read():
    UndisplayedList = [] 
    undisplayed_csvfile = 'Files\Modules\Database\undisplayeditem.csv'
    UndisplayedDB = csv.reader(open(undisplayed_csvfile, 'rb'), delimiter = ',', quotechar = '|')
    for listrow in UndisplayedDB:
        UndisplayedList.append(listrow)
    itemnum=[]
    for i in range(len(UndisplayedList)):
        itemnum.append(UndisplayedList[i][0])
    returnlist=[itemnum]    
    return returnlist
