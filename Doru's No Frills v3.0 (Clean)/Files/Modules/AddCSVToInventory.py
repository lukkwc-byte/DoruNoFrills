'''
    Version ALPHA1.2 27/09/2011 Kyuho
    Version 0.01 28/09/2011 Kyuho
    Version 0.02 10/10/2011 Kyuho (edited function names to avoid error)
    Version 0.03 25/10/2011 Kyuho+Michael (implemented validity variable + validity 1)
    Version 0.04 26/10/2011 Kyuho+Michael (implemented validity 16)
    Version 0.05 27/10/2011 Kyuho (error proofing)
    Version 0.06 03/11/2011 Kyuho (fixed supplier-store confusion, implemented purchase transaction, validity 18)
'''


import csv
import time
from ReadCSV import *
from WriteCSV import *

def inv_ImportCSV(csv_name):
    validity = 0
    if '|' in csv_name or ',' in csv_name:
        validity = 1
        return [validity]
    else:
        CSVlist = []
        csvfile_input = 'Files\Modules\Database\\' + csv_name + '.csv'
        try:
            CSV_DB = csv.reader(open(csvfile_input, 'rb'), delimiter = ',', quotechar = '|')
        except:
            validity = 16
        if validity == 16:
            return [validity]
        else:

            #1. check if it's in proper format *
            #2. check for validity for each variable *
            #3. if item number already exists and item name is not the same *
            #4. if item does not exist in inventory

            try:
                CSVlist = InvCSV_Read(csvfile_input)
            except:
                validity = 33

            if validity == 33:
                return [validity]
            else:
                if len(CSVlist) != 5:
                    validity = 33
                    return [validity]
                else:
                    Invlist = Inv_Read()
                    CSV_line1 = [CSVlist[0][0], CSVlist[1][0], CSVlist[2][0], CSVlist[3][0], CSVlist[4][0]]
                    Inv_line1 = [Invlist[0][0], Invlist[1][0], Invlist[2][0], Invlist[3][0], Invlist[4][0]]
                    if CSV_line1 != Inv_line1:
                        validity = 33
                        return [validity]
                    else:
                        item_number = Invlist[0][1:]
                        item_name = Invlist[1][1:]
                        item_qty = Invlist[2][1:]
                        store_price = Invlist[3][1:]
                        supplier_price = Invlist[4][1:]
                        
                        CSV_item_number = CSVlist[0][1:]
                        CSV_item_name = CSVlist[1][1:]
                        CSV_item_qty = CSVlist[2][1:]
                        CSV_store_price = CSVlist[3][1:]
                        CSV_supplier_price = CSVlist[4][1:]

                        if len(CSV_item_number) != len(CSV_item_name) or len(CSV_item_number) != len(CSV_item_qty) or len(CSV_item_number) != len(CSV_store_price) or len(CSV_item_number) != len(CSV_supplier_price):
                            validity = 34
                            return [validity]
                        else:
                            numlist = "0123456789"
                            for i in range(len(CSV_item_number)):
                                seperate = str(CSV_item_number[i])
                                for j in range(len(seperate)):
                                    if seperate[j] not in numlist:
                                        validity = 34
                                        break

                            for i in range(len(CSV_item_name)):
                                seperate = str(CSV_item_name[i])
                                if '|' in seperate or ',' in seperate:
                                    validity = 34
                                    break

                            for i in range(len(CSV_item_qty)):
                                seperate = str(CSV_item_qty[i])
                                for j in range(len(seperate)):
                                    if seperate[j] not in numlist:
                                        validity = 34
                                        break

                            floatlist = ".0123456789"
                            for i in range(len(CSV_store_price)):
                                seperate = str(CSV_store_price[i])
                                for j in range(len(seperate)):
                                    if seperate[j] not in floatlist:
                                        validity = 34
                                        break

                            for i in range(len(CSV_supplier_price)):
                                seperate = str(CSV_supplier_price[i])
                                for j in range(len(seperate)):
                                    if seperate[j] not in floatlist:
                                        validity = 34
                                        break

                            if validity == 34:
                                return [validity]

                            else:
                                repetition_check = CSV_item_number
                                CSV_item_number = CSV_item_number[:]
                                repetition_check.sort()

                                for i in range(len(repetition_check)-1):
                                    if repetition_check[i] == repetition_check[i+1]:
                                        validity = 33
                                        break

                                repetition_check = CSV_item_name
                                CSV_item_name = CSV_item_name[:]
                                repetition_check.sort()

                                for i in range(len(repetition_check)-1):
                                    if repetition_check[i] == repetition_check[i+1]:
                                        validity = 33
                                        break

                                if validity == 33:
                                    return [validity]

                                else:
                                    InventoryChangelist = InvChange_Read()
                                    c_item_number = InventoryChangelist[0]
                                    c_item_name = InventoryChangelist[1]
                                    c_item_qty_added = InventoryChangelist[2]
                                    c_item_price = InventoryChangelist[3]
                                    c_total_price = InventoryChangelist[4]
                                    c_date_bought = InventoryChangelist[5]
                                    c_time_bought = InventoryChangelist[6]

                                    now_date = time.localtime()
                                    comp_date = '%.4d:%.2d:%.2d' % (now_date[0], now_date[1], now_date[2])
                                    comp_time = '%.2d:%.2d:%.2d' % (now_date[3], now_date[4], now_date[5])

                                    
                                    for i in range(len(CSV_item_number)):
                                        for j in range(len(item_number)):
                                            if CSV_item_number[i] == item_number[j]:
                                                if CSV_item_name[i] == item_name[j]:
                                                    updated_item_qty = str(int(item_qty[j]) + int(CSV_item_qty[i]))
                                                    if int(updated_item_qty) > 9999:
                                                        validity = 18
                                                        return [validity]
                                                    else:
                                                        item_qty[j] = updated_item_qty
                                                        
                                                        c_item_number.append(item_number[j])
                                                        c_item_name.append(item_name[j])
                                                        c_item_qty_added.append(CSV_item_qty[i])
                                                        c_item_price.append(store_price[j])
                                                        price_sum = "%.2f" % float(float(store_price[j]) * int(CSV_item_qty[i]))
                                                        c_total_price.append(price_sum)
                                                        c_date_bought.append(comp_date)
                                                        c_time_bought.append(comp_time)
                                                        
                                                else:
                                                    validity = 35
                                                    break

                                    if validity == 35:
                                        return [validity]

                                    else:
                                        not_there = []
                                        for i in range(len(CSV_item_number)):
                                            if CSV_item_number[i] not in item_number:
                                                not_there.append(i)

                                        for i in range(len(not_there)):
                                            item_number.append(CSV_item_number[not_there[i]])
                                            item_name.append(CSV_item_name[not_there[i]])
                                            item_qty.append(CSV_item_qty[not_there[i]])
                                            store_price.append(CSV_store_price[not_there[i]])
                                            supplier_price.append(CSV_supplier_price[not_there[i]])

                                            c_item_number.append(CSV_item_number[not_there[i]])
                                            c_item_name.append(CSV_item_name[not_there[i]])
                                            c_item_qty_added.append(CSV_item_qty[not_there[i]])
                                            c_item_price.append(CSV_store_price[not_there[i]])
                                            price_sum = "%.2f" % float(float(CSV_store_price[not_there[i]]) * int(CSV_item_qty[not_there[i]]))
                                            c_total_price.append(price_sum)
                                            c_date_bought.append(comp_date)
                                            c_time_bought.append(comp_time)

                                        item_number = ['itemnumber'] + item_number
                                        item_name = ['itemname'] + item_name
                                        item_qty = ['itemquantity'] + item_qty
                                        store_price = ['storeprice'] + store_price
                                        supplier_price = ['supplierprice'] + supplier_price

                                        total_inv = [item_number, item_name, item_qty, store_price, supplier_price]
                                        inv_url = 'Files\Modules\Database\inventory.csv'
                                        WriteInvCSV(total_inv, inv_url)

                                        total_c = [c_item_number, c_item_name, c_item_qty_added, c_item_price, c_total_price, c_date_bought, c_time_bought]
                                        c_url = 'Files\Modules\Database\inventorychange.csv'
                                        WriteCSV(total_c, c_url)



"""
def inv_MergeItem(lis):                     # 'inv_SaveTransaction' will be applied within this function
    if len(lis) == 1:
        return lis
    else:
        CSVitem_number = lis[0]
        CSVitem_name = lis[1]
        CSVitem_qty = lis[2]
        CSVsupplier_price = lis[3]
        CSVstore_price = lis[4]

        CSVitem_number = CSVitem_number[1:]
        CSVitem_name = CSVitem_name[1:]
        CSVitem_qty = CSVitem_qty[1:]
        CSVsupplier_price = CSVsupplier_price[1:]
        CSVstore_price = CSVstore_price[1:]

        Inventorylist = Inv_Read()

        item_number = Inventorylist[0]
        item_name = Inventorylist[1]
        item_qty = Inventorylist[2]
        supplier_price = Inventorylist[3]
        store_price = Inventorylist[4]

        InventoryChangelist = InvChange_Read()

        c_item_number = InventoryChangelist[0]
        c_item_name = InventoryChangelist[1]
        c_item_qty_added = InventoryChangelist[2]
        c_item_price = InventoryChangelist[3]
        c_total_price = InventoryChangelist[4]
        c_date_bought = InventoryChangelist[5]
        c_time_bought = InventoryChangelist[6]

        now_date = time.localtime()
        comp_date = '%.4d:%.2d:%.2d' % (now_date[0], now_date[1], now_date[2])
        comp_time = '%.2d:%.2d:%.2d' % (now_date[3], now_date[4], now_date[5])

        CSVind = 0
        while CSVind < len(CSVitem_number):
            ind = 0
            while ind < len(item_number):
                if CSVitem_number[CSVind] == item_number[ind]:
                    updated_item_qty = int(item_qty[ind]) + int(CSVitem_qty[CSVind])
                    if updated_item_qty > 9999:
                        validity = 18
                        return [validity]
                    else:
                        item_qty[ind] = str(updated_item_qty)
                        c_item_number.append(item_number[ind])
                        c_item_name.append(item_name[ind])
                        c_item_qty_added.append(CSVitem_qty[CSVind])
                        c_item_price.append(store_price[ind])
                        price_sum = float(store_price[ind]) * int(CSVitem_qty[CSVind])
                        c_total_price.append(price_sum)
                        c_date_bought.append(comp_date)
                        c_time_bought.append(comp_time)
                ind += 1
            CSVind += 1

        for i in range(len(CSVitem_number)):
            if CSVitem_number[i] not in item_number:
                item_number.append(CSVitem_number[i])    
                item_name.append(CSVitem_name[i])
                item_qty.append(CSVitem_qty[i])
                supplier_price.append(CSVsupplier_price[i])
                store_price.append(CSVstore_price[i])

                c_item_number.append(CSVitem_number[i])
                c_item_name.append(CSVitem_name[i])
                c_item_qty_added.append(CSVitem_qty[i])
                c_item_price.append(CSVstore_price[i])
                price_sum = float(CSVstore_price[i]) * int(CSVitem_qty[i])
                c_total_price.append(price_sum)
                c_date_bought.append(comp_date)
                c_time_bought.append(comp_time)

        lis=[c_item_number,c_item_name,c_item_qty_added,c_item_price,c_total_price,c_date_bought,c_time_bought]
        WriteCSV(lis, change_csvfile)

        returnlis = [item_number, item_name, item_qty, supplier_price, store_price]

        return returnlis


def inv_csv_AddItems(lis):
    if len(lis) == 1:
        return False, lis[0]
    else:
        csvfile = 'Files\Modules\Database\inventory.csv'
        WriteCSV(lis, csvfile)
        return [True]


# csv file name is 'inventory.csv'
"""
"""
list1 = ImportCSV('inventorylol.csv')#      --> declare a list for ImportCSV
list2 = MergeItem(list1)              #--> declare a list for MergeItem
AddItems(list2)
"""
