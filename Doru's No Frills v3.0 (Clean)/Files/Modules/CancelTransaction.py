import csv
import Check
from WriteCSV import *
from ReadCSV import *
from RemoveItemFromCashRegister import *


def cancel_transaction():
    Check_List = Check_Read()
    session_number = Check_List[0]
    session_latest = session_number[1]

    C_Registerlist = Cash_Read()
    cs_date = C_Registerlist[0]
    cs_session = C_Registerlist[1]
    cs_item_number = C_Registerlist[2]
    cs_item_name = C_Registerlist[3]
    cs_item_qty = C_Registerlist[4]
    cs_store_price = C_Registerlist[5]
    cs_item_trans = C_Registerlist[6]
    cs_supplier_price = C_Registerlist[7]
    cs_item_time = C_Registerlist[8]
    cs_employee = C_Registerlist[9]

    if len(cs_date) == 1:
        Check.BUSY = False
        return True
    if Check.BUSY == False:
        validity = 29
        return [validity]
    
    else: #busy = True
        valid_session = 0
        for i in range(len(cs_session)):
            if cs_session[i] == session_latest:
                valid_session = i
                break

        if valid_session == 0:
            Check.BUSY = False
            return True

        else:
            add_date = cs_date[valid_session:]
            add_session = cs_session[valid_session:]
            add_item_number = cs_item_number[valid_session:]
            add_item_name = cs_item_name[valid_session:]
            add_item_qty = cs_item_qty[valid_session:]
            add_store_price = cs_store_price[valid_session:]
            add_item_trans = cs_item_trans[valid_session:]
            add_supplier_price = cs_supplier_price[valid_session:]
            add_item_time = cs_item_time[valid_session:]
            add_employee = cs_employee[valid_session:]

            cs_date = cs_date[:valid_session]
            cs_session = cs_session[:valid_session]
            cs_item_number = cs_item_number[:valid_session]
            cs_item_name = cs_item_name[:valid_session]
            cs_item_qty = cs_item_qty[:valid_session]
            cs_store_price = cs_store_price[:valid_session]
            cs_item_trans = cs_item_trans[:valid_session]
            cs_supplier_price = cs_supplier_price[:valid_session]
            cs_item_time = cs_item_time[:valid_session]
            cs_employee = cs_employee[:valid_session]

            cs_total = [cs_date, cs_session, cs_item_number, cs_item_name, cs_item_qty, cs_store_price, cs_item_trans, cs_supplier_price, cs_item_time, cs_employee]
            cash_csvfile = 'Files\Modules\Database\cashregister.csv'
            WriteCSV(cs_total, cash_csvfile)

            Inventorylist = Inv_Read()
            item_number = Inventorylist[0]
            item_name = Inventorylist[1]
            item_qty = Inventorylist[2]
            supplier_price = Inventorylist[3]
            store_price = Inventorylist[4]

            for i in range(len(add_item_number)):
                for j in range(len(item_number)):
                    if add_item_number[i] == item_number[j]:
                        item_qty[j] = str(int(item_qty[j]) + int(add_item_qty[i]))

######################################################################################

            Undisplayed_list = Undisplayed_Read()
            und_item = Undisplayed_list[0]

            Historylist = HistoryInvLoc_Read()
            his_item = Historylist[0]

            for i in range(len(add_item_number)):
                for j in range(len(item_number)):
                    if add_item_number[i] == item_number[j]:
                        if item_qty[j] == '0':
                            item_qty[j] = add_item_qty[i]

            for i in range(len(add_item_number)):
                locator_update(add_item_number[i])

            inv_total = [item_number, item_name, item_qty, supplier_price, store_price]
            inv_csvfile = 'Files\Modules\Database\inventory.csv'
            WriteInvCSV(inv_total, inv_csvfile)
            
            Check.BUSY = False
            return True

            
