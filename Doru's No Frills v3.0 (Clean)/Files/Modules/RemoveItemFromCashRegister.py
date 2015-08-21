'''
    Version ALPHA 27/09/2011 Kyuho
    Version 0.02 28/09/2011 Kyuho
    Edited: - updates inventory csv file with all the attributes included
            - returns False if user wishes to delete more items than the quantity in cash register csv
            - DeletePreviousItem()
    Version 0.03 10/10/2011 Kyuho (edited function names to avoid error)
    Version 0.04 12~13/10/2011 Kyuho (fixed major error/crash)
    Version 0.05 14/10/2011 Kyuho (fixed negative value error)
    Version 0.06 28/10/2011 Kyuho (validity 1,2,3,6,7,9)
    Version 0.07 04/11/2011 Kyuho (implemented time / employee + trying to implement session limit)
            --> problem with remove last item
    Version 0.08 23/11/2011 Kyuho (undisplayed item implementation)
    Version 0.09 29/11/2011 Kyuho (implementing invlocator logic)
'''

import csv
import time
from WriteCSV import *
from ReadCSV import *

def locator_update(i_num):
    Locatorlist = InventoryLoc_Read()
    loc_item = Locatorlist[0]
    a_1 = Locatorlist[1]
    a_2 = Locatorlist[2]
    a_3 = Locatorlist[3]
    a_4 = Locatorlist[4]
    a_5 = Locatorlist[5]
    a_6 = Locatorlist[6]
    a_7 = Locatorlist[7]
    a_8 = Locatorlist[8]


    Historylist = HistoryInvLoc_Read()
    his_item = Historylist[0]
    b_1 = Historylist[1]
    b_2 = Historylist[2]
    b_3 = Historylist[3]
    b_4 = Historylist[4]
    b_5 = Historylist[5]
    b_6 = Historylist[6]
    b_7 = Historylist[7]
    b_8 = Historylist[8]

    if i_num not in his_item:
        Undisplayed_list = Undisplayed_Read()
        und_item = Undisplayed_list[0]
        und_item.append(i_num)

        Undisplayed_csvfile = 'Files\Modules\Database\undisplayeditem.csv'
        WriteCSV([und_item], Undisplayed_csvfile)

    else:
        if i_num not in loc_item:
            valid_num = []
            for i in range(len(his_item)):
                if his_item[i] in loc_item or his_item[i] == i_num:
                    valid_num.append(his_item[i])

            new_ind = 0
            for i in range(len(valid_num)):
                if valid_num[i] not in loc_item:
                    new_ind = i
                    break

            if new_ind == 1:
                loc_item = [loc_item[0]] + [i_num] + loc_item[1:]
                a_1 = [a_1[0]] + ['No'] + a_1[1:]
                a_2 = [a_2[0]] + ['No'] + a_2[1:]
                a_3 = [a_3[0]] + ['No'] + a_3[1:]
                a_4 = [a_4[0]] + ['No'] + a_4[1:]
                a_5 = [a_5[0]] + ['No'] + a_5[1:]
                a_6 = [a_6[0]] + ['No'] + a_6[1:]
                a_7 = [a_7[0]] + ['No'] + a_7[1:]
                a_8 = [a_8[0]] + ['No'] + a_8[1:]
            elif new_ind == (len(valid_num)-1):
                loc_item = loc_item + [i_num]
                a_1 = a_1 + ['No']
                a_2 = a_2 + ['No']
                a_3 = a_3 + ['No']
                a_4 = a_4 + ['No']
                a_5 = a_5 + ['No']
                a_6 = a_6 + ['No']
                a_7 = a_7 + ['No']
                a_8 = a_8 + ['No']
            else:
                loc_item = loc_item[:new_ind] + [i_num] + loc_item[new_ind:]
                a_1 = a_1[:new_ind] + ['No'] + a_1[new_ind:]
                a_2 = a_2[:new_ind] + ['No'] + a_2[new_ind:]
                a_3 = a_3[:new_ind] + ['No'] + a_3[new_ind:]
                a_4 = a_4[:new_ind] + ['No'] + a_4[new_ind:]
                a_5 = a_5[:new_ind] + ['No'] + a_5[new_ind:]
                a_6 = a_6[:new_ind] + ['No'] + a_6[new_ind:]
                a_7 = a_7[:new_ind] + ['No'] + a_7[new_ind:]
                a_8 = a_8[:new_ind] + ['No'] + a_8[new_ind:]

            history_ind = 0
            for i in range(len(his_item)):
                if his_item[i] == i_num:
                    history_ind = i
                    break

            if b_1[history_ind] == 'Yes':
                a_1[new_ind] = 'Yes'
            elif b_2[history_ind] == 'Yes':
                a_2[new_ind] = 'Yes'
            elif b_3[history_ind] == 'Yes':
                a_3[new_ind] = 'Yes'
            elif b_4[history_ind] == 'Yes':
                a_4[new_ind] = 'Yes'
            elif b_5[history_ind] == 'Yes':
                a_5[new_ind] = 'Yes'
            elif b_6[history_ind] == 'Yes':
                a_6[new_ind] = 'Yes'
            elif b_7[history_ind] == 'Yes':
                a_7[new_ind] = 'Yes'
            elif b_8[history_ind] == 'Yes':
                a_8[new_ind] = 'Yes'

                
        a_list = [loc_item, a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8]
        loc_csvfile = 'Files\Modules\Database\inventorylocator.csv'
        WriteCSV(a_list, loc_csvfile)





def cash_out_ReadItemCSV(lis):
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
        if len(lis[1]) > 1:
            if lis[1][0] == '0':
                validity = 37
                break
        if int(lis[1]) <= 0:
            validity = 17
            break
        if len(lis[1])> 4:
            validity = 9
            break


    if validity > 0:
        return [validity]
    else:
        C_Registerlist = Cash_Read()

        total_date = C_Registerlist[0]
        total_session = C_Registerlist[1]
        total_item_number = C_Registerlist[2]
        total_item_name = C_Registerlist[3]
        total_item_qty = C_Registerlist[4]
        total_store_price = C_Registerlist[5]
        total_item_trans = C_Registerlist[6]
        total_supplier_price = C_Registerlist[7]
        total_item_time = C_Registerlist[8]
        total_employee = C_Registerlist[9]

        valid_session_lis = []

        for i in range(len(total_session)):
            if total_session[i] == str(lis[2]):
                valid_session_lis.append(i)

        if valid_session_lis == []:
            validity = 24
            return [validity]
        else:            
            start_date = total_date[:valid_session_lis[0]]
            date = total_date[valid_session_lis[0]:]
            
            start_session = total_session[:valid_session_lis[0]]
            session = total_session[valid_session_lis[0]:]
            
            start_item_number = total_item_number[:valid_session_lis[0]]
            item_number = total_item_number[valid_session_lis[0]:]
            
            start_item_name = total_item_name[:valid_session_lis[0]]
            item_name = total_item_name[valid_session_lis[0]:]
            
            start_item_qty = total_item_qty[:valid_session_lis[0]]
            item_qty = total_item_qty[valid_session_lis[0]:]
            
            start_store_price = total_store_price[:valid_session_lis[0]]
            store_price = total_store_price[valid_session_lis[0]:]
            
            start_item_trans = total_item_trans[:valid_session_lis[0]]
            item_trans = total_item_trans[valid_session_lis[0]:]
            
            start_supplier_price = total_supplier_price[:valid_session_lis[0]]
            supplier_price = total_supplier_price[valid_session_lis[0]:]

            start_item_time = total_item_time[:valid_session_lis[0]]
            item_time = total_item_time[valid_session_lis[0]:]

            start_employee = total_employee[:valid_session_lis[0]]
            employee = total_employee[valid_session_lis[0]:]


        returnlis_cashregister = 0

        if lis[0] in item_number:
            now_date = time.localtime()
            comp_date = '%.4d:%.2d:%.2d:%.2d:%.2d:%.2d' % (now_date[0], now_date[1], now_date[2], now_date[3], now_date[4], now_date[5])

            adding_item_name = 0
            adding_store_price = 0
            adding_supplier_price = 0

            for i in range(len(item_number)):
                if item_number[i] == lis[0] and session[i] == lis[2]:
                    adding_item_name = item_name[i]
                    adding_store_price = store_price[i]
                    adding_supplier_price = supplier_price[i]
                    if int(item_qty[i]) >= int(lis[1]):
                        item_qty[i] = str(int(item_qty[i])-int(lis[1]))
                        if item_qty[i] == '0':
                            date.pop(i)
                            session.pop(i)
                            item_number.pop(i)
                            item_name.pop(i)
                            item_qty.pop(i)
                            store_price.pop(i)
                            item_trans.pop(i)
                            supplier_price.pop(i)
                            item_time.pop(i)
                            employee.pop(i)
                    else:           # deleting more than possible
                        validity = 23
                        return [validity]
                    break

            returnlis_cashregister = 0

            date = start_date + date
            session = start_session + session
            item_number = start_item_number + item_number
            item_name = start_item_name + item_name
            item_qty = start_item_qty + item_qty
            store_price = start_store_price + store_price
            item_trans = start_item_trans + item_trans
            supplier_price = start_supplier_price + supplier_price
            item_time = start_item_time + item_time
            employee = start_employee + employee

            returnlis_cashregister = [date, session, item_number, item_name, item_qty, store_price, item_trans, supplier_price, item_time, employee]
            
            Inventorylist = Inv_Read()
            
            inv_item_number = Inventorylist[0]
            inv_item_name = Inventorylist[1]
            inv_item_qty = Inventorylist[2]
            inv_supplier_price = Inventorylist[3]
            inv_store_price = Inventorylist[4]

            ind = 0
            check = 0
            while ind < len(inv_item_number):
                if inv_item_number[ind] == lis[0]:
                    inv_item_qty[ind] = str(int(inv_item_qty[ind])+int(lis[1]))
                    check = 1
                    break
                ind+=1

            locator_update(lis[0])
            
            returnlis_inventory = [inv_item_number, inv_item_name, inv_item_qty, inv_supplier_price, inv_store_price]
            returnlis = [returnlis_cashregister, returnlis_inventory]

            return returnlis

        else:
            validity = 24
            return [validity]

                

def cash_out_DeletePreviousItem(nsession):
    C_Registerlist = Cash_Read()
    total_date = C_Registerlist[0]
    total_session = C_Registerlist[1]
    total_item_number = C_Registerlist[2]
    total_item_name = C_Registerlist[3]
    total_item_qty = C_Registerlist[4]
    total_store_price = C_Registerlist[5]
    total_item_trans = C_Registerlist[6]
    total_supplier_price = C_Registerlist[7]
    total_item_time = C_Registerlist[8]
    total_employee = C_Registerlist[9]

    check_session = 0
    for i in range(len(total_session)):
        if total_session[i] == nsession:
            check_session = 1
            break
    if check_session == 0:
        validity = 24
        return [validity]
    
    else:
        lis = [total_date[-1], total_session[-1], total_item_number[-1], total_item_name[-1], total_item_qty[-1], total_store_price[-1], total_item_trans[-1], total_supplier_price[-1], total_item_time[-1], total_employee[-1]]

        total_date = total_date[:-1]
        total_session = total_session[:-1]
        total_item_number = total_item_number[:-1]
        total_item_name = total_item_name[:-1]
        total_item_qty = total_item_qty[:-1]
        total_store_price = total_store_price[:-1]
        total_item_trans = total_item_trans[:-1]
        total_supplier_price = total_supplier_price[:-1]
        total_item_time = total_item_time[:-1]
        total_employee = total_employee[:-1]

        returnlis_cr = [total_date, total_session, total_item_number, total_item_name, total_item_qty, total_store_price, total_item_trans, total_supplier_price, total_item_time, total_employee]
        
        Inventorylist = Inv_Read()
        inv_item_number = Inventorylist[0]
        inv_item_name = Inventorylist[1]
        inv_item_qty = Inventorylist[2]
        inv_supplier_price = Inventorylist[3]
        inv_store_price = Inventorylist[4]

        for i in range(len(inv_item_number)):
            if inv_item_number[i] == lis[2]:
                inv_item_qty[i] = str(int(inv_item_qty[i]) + int(lis[4]))
                break

        locator_update(lis[2])
        
        returnlis_inv = [inv_item_number, inv_item_name, inv_item_qty, inv_supplier_price, inv_store_price]

        return [returnlis_cr, returnlis_inv]



def cash_out_RemoveItem(lis):
    if len(lis) == 1:
        return [False, lis[0]]
    else:
        lis_cr = lis[0]
        csvfile = 'Files\Modules\Database\cashregister.csv'
        WriteCSV(lis_cr, csvfile)
        return [True]

def cash_out_UpdateInventory(lis):
    if len(lis) != 1:
        lis_inv = lis[1]
        csvfile = 'Files\Modules\Database\inventory.csv'
        WriteInvCSV(lis_inv, csvfile)
