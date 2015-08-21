'''
    Version ALPHA 27/09/2011 Jonathan (Basic check variables implemented)
    Version 0.02 28/09/2011 Jonathan (Added version variable)
    Version 0.03 08/10/2011 Jonathan (Support for userlevels, integration with statusbar)
    Version 0.04 10/10/2011 Jonathan (Build 1.3a)
    Version 0.05 10/10/2011 Jonathan (Build 1.3b)
    Version 0.06 21/10/2011 Jonathan (Build 1.4)
    Version 0.07 27/10/2011 Jonathan (Build 1.5)
    Version 0.08 03/11/2011 Jonathan (Build 1.6)
    Version 0.09 08/11/2011 Kyuho (CashError)
    Version 0.10 10/11/2011 Kyuho (Updated CashError)
    Version 0.11 10/11/2011 Jonathan (Build 1.7)
    Version 0.12 xx/11/2011 Jonathan (Build 1.8)
    Version 0.13 24/11/2011 Jonathan (Build 1.9)
    Version 0.14 02/12/2011 Jonathan (Build 2.0), Kyuho - Aislenum
    Version 0.15 15/12/2011 Jonathan (Build 2.1, Test Build 2.1b)
    Version 0.16 22/12/2011 Jonathan (Build 2.2)
    Version 0.17 30/12/2011 Jonathan (Build 2.3)
    Version 0.18 08/01/2012 Jonathan (Build 2.4) 
'''

from Tkinter import *
import tkMessageBox
import csv
from ReadCSV import *
from WriteCSV import *

BUSY = False #Indicates whether window is currently busy - to be determined by individual modules.
openwindow = '' # Currently open window
DESTROYED = False
version = 'Store Suite Version 3.0'
# version = 'Store System v1.0'
userlevel = '1' # Automatic Admin - For Debug
loggeduser = 'TEST Mode' #who is logged in?
hourlywage = ''
Aisle_num = None
about = 'closed' #About screen
shiftstat = 'Checked Out'
editacct = ''
editinv = ''

def BusyAlert(self):
    tkMessageBox.showwarning("Alert", "A transaction is in progress. Please complete or cancel the transaction before performing other actions!") # Show BUSY box

def InstanceAlert(self):
    tkMessageBox.showwarning("Warning", "That window is already open.") # Show MULTIPLE INSTANCE

def ShiftAlert(self):
    tkMessageBox.showwarning("Warning", "Please check in before accessing the Cash Register.") # Show MULTIPLE INSTANCE


def CashError():
    Check_List = Check_Read()
    session_number = Check_List[0]
    session_latest = session_number[1]

    C_Registerlist = Cash_Read()
    cs_date = C_Registerlist[0]
    cs_session = C_Registerlist[1]
    cs_item_number = C_Registerlist[2]
    cs_item_name = C_Registerlist[3]
    cs_item_qty = C_Registerlist[4]
    cs_supplier_price = C_Registerlist[5]
    cs_item_trans = C_Registerlist[6]
    cs_store_price = C_Registerlist[7]
    cs_item_time = C_Registerlist[8]
    cs_employee = C_Registerlist[9]

    if len(cs_date) != 1:
        improper = 0

        for i in range(len(cs_session)):
            if cs_session[i] == session_latest:
                improper += 1

        if improper != 0:
            add_date = cs_date[-improper:]
            add_session = cs_session[-improper:]
            add_item_number = cs_item_number[-improper:]
            add_item_name = cs_item_name[-improper:]
            add_item_qty = cs_item_qty[-improper:]
            add_item_trans = cs_item_trans[-improper:]
            add_supplier_price = cs_supplier_price[-improper:]
            add_store_price = cs_store_price[-improper:]
            add_item_time = cs_item_time[-improper:]
            add_employee = cs_employee[-improper:]
            
            cs_date = cs_date[:-improper]
            cs_session = cs_session[:-improper]
            cs_item_number = cs_item_number[:-improper]
            cs_item_name = cs_item_name[:-improper]
            cs_item_qty = cs_item_qty[:-improper]
            cs_store_price = cs_store_price[:-improper]
            cs_item_trans = cs_item_trans[:-improper]
            cs_supplier_price = cs_supplier_price[:-improper]
            cs_item_time = cs_item_time[:-improper]
            cs_employee = cs_employee[:-improper]

            cash_csvfile = 'Files\Modules\Database\cashregister.csv'
            cs_list = [cs_date, cs_session, cs_item_number, cs_item_name, cs_item_qty, cs_supplier_price, cs_item_trans, cs_store_price, cs_item_time, cs_employee]
            WriteCSV(cs_list, cash_csvfile)

            Inventorylist = Inv_Read()
            item_number = Inventorylist[0]
            item_name = Inventorylist[1]
            item_qty = Inventorylist[2]
            supplier_price = Inventorylist[3]
            store_price = Inventorylist[4]

            cash_ind = 0
            while cash_ind < len(add_item_number):
                inv_ind = 0
                while inv_ind < len(item_number):
                    if add_item_number[cash_ind] == item_number[inv_ind]:
                        item_qty[inv_ind] = str(int(item_qty[inv_ind]) + int(add_item_qty[cash_ind]))
                    inv_ind += 1
                cash_ind += 1

            for i in range(len(add_item_number)):
                if add_item_number[i] not in item_number:
                    item_number.append(add_item_number[i])
                    item_name.append(add_item_name[i])
                    item_qty.append(add_item_qty[i])
                    supplier_price.append(add_supplier_price[i])
                    store_price.append(add_store_price[i])

            inv_csvfile = 'Files\Modules\Database\inventory.csv'
            inv_list = [item_number, item_name, item_qty, supplier_price, store_price]
            WriteInvCSV(inv_list, inv_csvfile)



