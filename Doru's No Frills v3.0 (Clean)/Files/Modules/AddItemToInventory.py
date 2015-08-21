'''
    Version ALPHA 27/09/2011 Kyuho
    Version 0.01 28/09/2011 Kyuho
    Version 0.02 10/10/2011 Kyuho (edited function names to avoid error)
    Version 0.03 17/10/2011 Kyuho+Michael (implemented validity variable)
    Version 0.04 18/10/2011 Kyuho+Michael (validity 1~5)
    Version 0.05 19/10/2011 Kyuho+Michael (validity 6~15)
    Version 0.06 20/10/2011 Kyuho+Michael (fixed logic implementation issues in inv_AddItem)
    Version 0.07 21/10/2011 Kyuho+Michael (checking for possible errors)
    Version 0.08 24/10/2011 Kyuho+Michael (validity 17)
    Version 0.09 25/10/2011 Kyuho+Michael (error proofing)
    Version 0.10 02/11/2011 Kyuho (inventory save transaction)
    Version 0.11 03/11/2011 Kyuho (fixed supplier-store confusion)
    Version 0.12 29/11/2011 Kyuho (implementing undisplayed item logic)
    Version 0.13 08/12/2011 Kyuho (implementing new csv read/write)
'''



import csv
import time
from WriteCSV import *
from ReadCSV import *

def inv_in_ReadItemCSV(lis):
    number_list = '0123456789.'                 # Kyuho
    validity = 0
    for i in range(len(lis)):
        if lis[0] == '' or lis[1] == '' or lis[2] == '' or lis[3] == '' or lis[4] =='':
            validity=6
            break
        if '|' in lis[i] or ',' in lis[i]:
            validity = 1
            break
        if '.' in lis[0]:
            validity = 2
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
        for i in range(len(lis[3])):
            if lis[3][i] not in number_list:
                validity = 4
                break
        for i in range(len(lis[4])):
            if lis[4][i] not in number_list:
                validity = 5
                break
        if '.' in lis[2]:
            validity = 7
            break
        for i in range(len(lis[2])):
            if lis[2][i] not in number_list[:-1]:
                validity = 7
                break
        if len(lis[2]) > 1:
            if lis[2][0] == '0':
                validity = 37
                break        
        if len(lis[1])> 15:
            validity = 8
            break
        if len(lis[2])> 4:
            validity = 9
            break
        if len(lis[3])> 8:
            validity = 10
            break
        if len(lis[3]) > 1:
            if lis[3][0] == '0':
                validity = 37
                break        
        if len(lis[4])> 8:
            validity = 11
            break
        if len(lis[4]) > 1:
            if lis[4][0] == '0':
                validity = 37
                break        
        if int(lis[2]) <= 0:
            validity = 17
            break

    if validity > 0:
        return [validity]                       # Kyuho
    else:
        lis[3] = "%.2f" % float(lis[3])
        lis[4] = "%.2f" % float(lis[4])

        Inventorylist = Inv_Read()
        
        item_number = Inventorylist[0]
        item_name = Inventorylist[1]
        item_qty = Inventorylist[2]
        supplier_price = Inventorylist[3]
        store_price = Inventorylist[4]

        for i in range(len(item_name)):
            item_name[i] = item_name[i].upper()

        lis[1] = lis[1].upper()

        for i in range(len(item_name)):
            if item_name[i] == lis[1]:
                if item_number[i] != lis[0]:
                    validity = 36
                    break

        if validity == 36:
            return [validity]

        else:
            for i in range(len(item_number)):
                if lis[0] == item_number[i]:
                    if lis[1] != item_name[i]:
                        validity = 30
                        return [validity]
                    else:
                        if lis[3] != supplier_price[i] or lis[4] != store_price[i]:
                            validity = 30
                            return [validity]


            for i in range(len(supplier_price)-1):
                supplier_price[i+1] = "%.2f" % float(supplier_price[i+1])
                
            for i in range(len(store_price)-1):
                store_price[i+1] = "%.2f" % float(store_price[i+1])
            
            repetition = 0

            for i in range(len(item_number)):
                if item_number[i] == lis[0]:
                    if item_name[i] == lis[1]:
                        if supplier_price[i] == lis[3] and store_price[i] == lis[4]:########
                            if int(lis[2]) + int(item_qty[i]) > 9999:
                                validity = 18
                                return [validity]
                            else:
                                if int(item_qty[i]) == 0:
                                    repetition = 2
                                else:
                                    repetition = 1
                                item_qty[i] = str(int(item_qty[i]) + int(lis[2]))
                                break
                        else:
                            if lis[3] == '' or lis[4] == '':
                                validity = 6
                                return [validity]
                            else:
                                if store_price[i] == lis[4] and supplier_price[i] != lis[3]:
                                    validity = 13
                                    return [validity]
                                elif store_price[i] != lis[4] and supplier_price[i] == lis[3]:
                                    validity = 14
                                    return [validity]
                                elif store_price[i] != lis[4] and supplier_price[i] != lis[3]:
                                    validity = 15
                                    return [validity]
                    else:
                        validity = 12
                        return [validity]


            if repetition == 0 or repetition == 2:
                if repetition == 0:
                    item_number.append(lis[0])
                    item_name.append(lis[1])
                    item_qty.append(lis[2])
                    supplier_price.append(lis[3])
                    store_price.append(lis[4])

                Undisplayed_list = Undisplayed_Read()
                und_item = Undisplayed_list[0]

                if lis[0] not in und_item:
                    und_item.append(lis[0])
                    Undisplayed_csvfile = 'Files\Modules\Database\undisplayeditem.csv'
                    WriteCSV([und_item], Undisplayed_csvfile)


            returnlis = [item_number, item_name, item_qty, supplier_price, store_price]

            return returnlis


### func_lis = list from inv_in_ReadItemCSV      lis = user_inputted list
def inv_SaveTransaction(func_lis, lis):
    if len(func_lis) != 1:
        InventoryChangelist = InvChange_Read()

        item_number = InventoryChangelist[0]
        item_name = InventoryChangelist[1]
        item_qty_added = InventoryChangelist[2]
        item_price = InventoryChangelist[3]
        total_price = InventoryChangelist[4]
        date_bought = InventoryChangelist[5]
        time_bought = InventoryChangelist[6]

        now_date = time.localtime()
        comp_date = '%.4d:%.2d:%.2d' % (now_date[0], now_date[1], now_date[2])
        comp_time = '%.2d:%.2d:%.2d' % (now_date[3], now_date[4], now_date[5])

        price_sum = float(lis[3]) * int(lis[2])

        item_number.append(lis[0])
        item_name.append(lis[1])
        item_qty_added.append(lis[2])
        item_price.append(lis[3])
        total_price.append(price_sum)
        date_bought.append(comp_date)
        time_bought.append(comp_time)
        
        change_list = [item_number, item_name, item_qty_added, item_price, total_price, date_bought, time_bought]

        changefile = 'Files\Modules\Database\inventorychange.csv'
        WriteCSV(change_list, changefile)


### supplier price x item quantity (from user input) --> new csv where total money spent is displayed


def inv_AddItem(lis):
    if len(lis) == 1:
        return [False, lis[0]]
    else:
        csvfile = 'Files\Modules\Database\inventory.csv'
        WriteInvCSV(lis, csvfile)
        return [True]


def edit_item_inv(lis):
    number_list = '0123456789.'                 # Kyuho
    validity = 0
    for i in range(len(lis)):
        if lis[0] == '' or lis[1] == '' or lis[2] == '' or lis[3] == '' or lis[4] =='':
            validity=6
            break
        if '|' in lis[i] or ',' in lis[i]:
            validity = 1
            break
        if '.' in lis[0]:
            validity = 2
            break
        for i in range(len(lis[0])):
            if lis[0][i] not in number_list:
                validity = 2
                break
        if len(lis[0])> 6:
            validity = 3
            break
        for i in range(len(lis[3])):
            if lis[3][i] not in number_list:
                validity = 4
                break
        for i in range(len(lis[4])):
            if lis[4][i] not in number_list:
                validity = 5
                break
        if '.' in lis[2]:
            validity = 7
            break
        for i in range(len(lis[2])):
            if lis[2][i] not in number_list[:-1]:
                validity = 7
                break
        if len(lis[1])> 15:
            validity = 8
            break
        if len(lis[2])> 4:
            validity = 9
            break
        if len(lis[3])> 8:
            validity = 10
            break
        if len(lis[4])> 8:
            validity = 11
            break

    if validity > 0:
        return [validity]
    else:
        Inventorylist = Inv_Read()
        
        item_number = Inventorylist[0]
        item_name = Inventorylist[1]
        item_qty = Inventorylist[2]
        supplier_price = Inventorylist[3]
        store_price = Inventorylist[4]

        lis[3] = "%.2f" % float(lis[3])
        lis[4] = "%.2f" % float(lis[4])

        for i in range(len(item_number)):
            if item_number[i] == lis[0]:
                supplier_price[i] = lis[3]
                store_price[i] = lis[4]
                break

        change_list = [item_number, item_name, item_qty, supplier_price, store_price]
        changefile = 'Files\Modules\Database\inventory.csv'
        WriteInvCSV(change_list, changefile)


            



# csv file name is 'inventory.csv'
# 1. declare a user-inputted list
# 2. 'new_list' = ReadItemCSV('user_list')
# 3. AddItem('new_list')

"""
list1 = ['8','8','8','8','8']
list2 = inv_ReadItemCSV(list1)
inv_AddItem(list2)
"""
