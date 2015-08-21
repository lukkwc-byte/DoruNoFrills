'''
    Version ALPHA 27/09/2011 Kyuho
    Version 0.02 28/09/2011 Kyuho
    Version 0.03 10/10/2011 Kyuho (edited function names to avoid error)
    Version 0.04 12~13/10/2011 Kyuho (fixed major error/crash)
    Version 0.05 14/10/2011 Kyuho (fixed negative value error)
    Version 0.06 27/10/2011 Kyuho+Michael (validity 18)
    Version 0.07 28/10/2011 Kyuho (validity 1,2,3,6,7,9)
    Version 0.08 02/11/2011 Kyuho (split time to date / time   +   included 'employee' to csv + logic)
    Version 0.09 23/11/2011 Kyuho (undisplayed item implementation)
'''

import csv
import Check
import time

from WriteCSV import *
from ReadCSV import *
from InvLocChange import *

# 1. declare a user-inputted list [itemnumber, itemquantity, session]
def cash_in_ReadItemCSV(lis):
    number_list = '0123456789.'
    validity = 0
    for i in range(len(lis)):
        if '|' in lis[i] or ',' in lis[i] or '.' in lis[i]:
            validity = 1
            break
        if lis[0] == '' or lis[1] == '':
            validity=6
            break
        for i in range(len(lis[0])):
            if lis[0][i] not in number_list:
                validity = 2
                break
        if len(lis[0]) > 1:
            if lis[0][0] == '0':
                validity = 37
                break
        if len(lis[0])> 6:
            validity = 3
            break
        for i in range(len(lis[1])):
            if lis[1][i] not in number_list:
                validity = 7
                break
        if '.' in lis[1]:
            validity = 7
            break
        for i in range(len(lis[1])):
            if lis[1][i] not in number_list[:-1]:
                validity = 7
                break
        if int(lis[1]) <= 0:
            validity = 17
            break
        if len(lis[1])> 4:
            validity = 9
            break
        if len(lis[1]) > 1:
            if lis[1][0] == '0':
                validity = 37
                break        

    if validity > 0:
        return [validity]
    else:
        lis[1] = int(lis[1])
        C_Registerlist = Cash_Read()

        date = C_Registerlist[0]
        session = C_Registerlist[1]
        item_number = C_Registerlist[2]
        item_name = C_Registerlist[3]
        item_qty = C_Registerlist[4]
        supplier_price = C_Registerlist[5]
        item_trans = C_Registerlist[6]
        store_price = C_Registerlist[7]
        item_time = C_Registerlist[8]
        employee = C_Registerlist[9]
        
        Inventorylist = Inv_Read()
        
        inv_item_number = Inventorylist[0]
        inv_item_name = Inventorylist[1]
        inv_item_qty = Inventorylist[2]
        inv_supplier_price = Inventorylist[3]
        inv_store_price = Inventorylist[4]

        for i in range(len(inv_item_number)):
            if inv_item_number[i] == lis[0]:
                if int(inv_item_qty[i]) < int(lis[1]):
                    validity = 18
                    break

        if validity == 18:
            return [validity]
        else:
            repetition = 0

            now_date = time.localtime()
            comp_date = '%.4d:%.2d:%.2d' % (now_date[0], now_date[1], now_date[2])
            comp_time = '%.2d:%.2d:%.2d' % (now_date[3], now_date[4], now_date[5])

            
            
            if lis[0] not in inv_item_number:
                validity = 28
                return [validity]
            else:
                for i in range(len(item_number)):                           # adds item count if item is already in csv file
                    if item_number[i] == lis[0] and session[i] == lis[2]:
                        item_qty[i] = str(int(item_qty[i]) + int(lis[1]))
                        repetition = 1
                        break

                check = 0

                if repetition == 0:     # creating new row
                    for i in range(len(inv_item_number)):
                        if inv_item_number[i] == lis[0]:
                            check = 1
                            if len(date) == 1:
                                date = [date[0], comp_date]
                                session = [session[0], lis[2]]
                                item_number = [item_number[0], lis[0]]
                                item_qty = [item_qty[0], lis[1]]
                                item_trans = [item_trans[0], '1']
                                item_name = [item_name[0], inv_item_name[i]]
                                supplier_price = [supplier_price[0], inv_supplier_price[i]]
                                store_price = [store_price[0], inv_store_price[i]]
                                item_time = [item_time[0], comp_time]
                                employee = [employee[0], Check.loggeduser]###
                            else:
                                date.append(comp_date)
                                session.append(lis[2])
                                item_number.append(lis[0])
                                item_qty.append(lis[1])
                                new_trans = str(int(item_trans[-1])+1)
                                item_trans.append(new_trans)
                                item_name.append(inv_item_name[i])
                                store_price.append(inv_store_price[i])
                                supplier_price.append(inv_supplier_price[i])
                                item_time.append(comp_time)
                                employee.append(Check.loggeduser)
                            break

                returnlis_cashregister = []
                if check == 1 or repetition == 1:
                    returnlis_cashregister = [date, session, item_number, item_name, item_qty, supplier_price, item_trans, store_price, item_time, employee]
                for i in range(len(inv_item_number)):
                    if inv_item_number[i] == lis[0]:
                        inv_item_qty[i] = str(int(inv_item_qty[i]) - int(lis[1]))
                        
                        if int(inv_item_qty[i]) == 0:
                            Undisplayed_list = Undisplayed_Read()
                            und_item = Undisplayed_list[0]

                            for i in range(len(und_item)):
                                if und_item[i] == lis[0]:
                                    del und_item[i]
                                    break

                            Undisplayed_csvfile = 'Files\Modules\Database\undisplayeditem.csv'
                            WriteCSV([und_item], Undisplayed_csvfile)

                            InvLoc_Change_Remove_Cash(lis[0])                            
                            break

                returnlis_inv = [inv_item_number, inv_item_name, inv_item_qty, inv_supplier_price, inv_store_price]
                
                returnlis = [returnlis_cashregister, returnlis_inv]

                return returnlis


def cash_in_AddItem(lis):
    if len(lis) == 1:
        return [False, lis[0]]
    else:
        lis_cr = lis[0]
        csvfile = 'Files\Modules\Database\cashregister.csv'
        WriteCSV(lis_cr, csvfile)
        return [True]

def cash_in_UpdateInventory(lis):
    if len(lis) != 1:
        lis_inv = lis[1]
        csvfile = 'Files\Modules\Database\inventory.csv'
        WriteInvCSV(lis_inv, csvfile)
    



# csv file name is 'cashregister.csv'

# 1. declare a user-inputted list [itemnumber, itemquantity, session]
# 2. 'new_list' = ReadItemCSV('user_list')
# 3. AddItem('new_list')
# 4. UpdateInventory('new_list')

"""
list1 = ['1','10.0', '5']
list2 = cash_ReadItemCSV(list1)
cash_AddItem(list2)
cash_UpdateInventory(list2)
"""


"""
userlist = ['1', '3', '5']
list2 = ReadItemCSV(userlist)
AddItem(list2)
#UpdateInventory(list2)
"""
