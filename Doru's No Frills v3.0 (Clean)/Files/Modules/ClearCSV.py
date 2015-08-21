import csv



def ClearPay():
    #Clears PayrollDB and EmployeePayDB

    #PayrollDB
    DB = csv.writer(open('Files\Modules\Database\PayrollDB.csv', 'wb'), delimiter = ',', quotechar = '|')
    row = ['employee', 'date', 'shift', 'checkin', 'checkout', 'wage', 'ID', 'Approval']
    DB.writerow(row)

    #EmployeePayDB
    DB = csv.writer(open('Files\Modules\Database\EmployeePayDB.csv', 'wb'), delimiter = ',', quotechar = '|')
    row = ['employee', 'date', 'shift', 'paid', 'time', 'wage']
    DB.writerow(row)

def ClearHR():
    #Clears useraccounts

    #useraccounts
    DB = csv.writer(open('Files\Modules\Database\useraccounts.csv', 'wb'), delimiter = ',', quotechar = '|')
    row = ['username', 'password', 'userlevel', 'hourlywage', 'SecQ', 'SecA']
    DB.writerow(row)

def ClearInv():
    #Clears Inventory, importitem, Inventory List, Inventory Locator, historyinvloc, undisplayeditem, InvChange

    #Inventory
    DB = csv.writer(open('Files\Modules\Database\inventory.csv', 'wb'), delimiter = ',', quotechar = '|')
    row = ['itemnumber', 'itemname', 'itemquantity', 'supplierprice', 'storeprice']
    DB.writerow(row)

    #Importitem
    DB = csv.writer(open('Files\Modules\Database\importitem.csv', 'wb'), delimiter = ',', quotechar = '|')
    row = ['itemnumber', 'itemname', 'itemquantity', 'supplierprice', 'storeprice']
    DB.writerow(row)

    #Inventorylist
    DB = csv.writer(open('Files\Modules\Database\Inventory List.csv', 'wb'), delimiter = ',', quotechar = '|')
    row = ['itemnumber', 'itemname']
    DB.writerow(row)

    #InventoryLoc
    DB = csv.writer(open('Files\Modules\Database\inventorylocator.csv', 'wb'), delimiter = ',', quotechar = '|')
    row = ['item', 'aisle1', 'aisle2', 'aisle3', 'aisle4', 'aisle5', 'aisle6', 'aisle7', 'aisle8']
    DB.writerow(row)

    #historyinvloc
    DB = csv.writer(open('Files\Modules\Database\historyinvloc.csv', 'wb'), delimiter = ',', quotechar = '|')
    row = ['item', 'aisle1', 'aisle2', 'aisle3', 'aisle4', 'aisle5', 'aisle6', 'aisle7', 'aisle8']
    DB.writerow(row)

    #undisplayeditem
    DB = csv.writer(open('Files\Modules\Database\undisplayeditem.csv', 'wb'), delimiter = ',', quotechar = '|')
    row = ['item']
    DB.writerow(row)

    #InventoryChange
    DB = csv.writer(open('Files\Modules\Database\inventorychange.csv', 'wb'), delimiter = ',', quotechar = '|')
    row = ['itemnumber', 'itemname', 'quantityadded', 'itemprice', 'total', 'date', 'time']
    DB.writerow(row)


def ClearCash():
    #Clears CashRegister, SessionDB, Check

    #CashRegister
    DB = csv.writer(open('Files\Modules\Database\cashregister.csv', 'wb'), delimiter = ',', quotechar = '|')
    row = ['date', 'session', 'itemnumber', 'itemname', 'itemquantity', 'supplierprice', 'itemtransaction', 'storeprice', 'time', 'employee']
    DB.writerow(row)

    #SessionDB
    DB = csv.writer(open('Files\Modules\Database\SessionDB.csv', 'wb'), delimiter = ',', quotechar = '|')
    row = ['date', 'session', 'subtotal', 'tax', 'total', 'employee', 'time']
    DB.writerow(row)

    #Check
    DB = csv.writer(open('Files\Modules\Database\check.csv', 'wb'), delimiter = ',', quotechar = '|')
    row = ['transactionID']
    row2 = ['1']
    DB.writerow(row)
    DB.writerow(row2)
