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
    Version 0.10 03/11/2011 Kyuho (fixed supplier-store confusion)
    Version 0.11 08/12/2011 Kyuho (implementing new csv read/write)
'''

import csv
from ReadCSV import *
from WriteCSV import *

def inv_out_ReadItemCSV(lis):
    number_list = '0123456789.'                 # Kyuho
    validity = 0
    for i in range(len(lis)):
        if lis[0] == '' or lis[1] == '' or lis[2] == '' or lis[3] == '' or lis[4] == '':
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

        if lis[0] not in item_number or lis[1] not in item_name:
            validity = 38
            return [validity]

        else:
            for i in range(len(supplier_price)-1):
                supplier_price[i+1] = "%.2f" % float(supplier_price[i+1])

            for i in range(len(store_price)-1):
                store_price[i+1] = "%.2f" % float(store_price[i+1])

            for i in range(len(item_number)):
                if item_number[i] == lis[0]:
                    if item_name[i] == lis[1]:
                        if supplier_price[i] == lis[3] and store_price[i] == lis[4]:
                            item_qty[i] = str(int(item_qty[i]) - int(lis[2]))
                            if item_qty[i] == '0':
                                Locatorlist = InventoryLoc_Read()

                                loc_itemnumber = Locatorlist[0]
                                a_1 = Locatorlist[1]
                                a_2 = Locatorlist[2]
                                a_3 = Locatorlist[3]
                                a_4 = Locatorlist[4]
                                a_5 = Locatorlist[5]
                                a_6 = Locatorlist[6]
                                a_7 = Locatorlist[7]
                                a_8 = Locatorlist[8]

                                Undisplayedlist = Undisplayed_Read()
                                und_item = Undisplayedlist[0]

                                for i in range(len(und_item)):
                                    if lis[0] == und_item[i]:
                                        del und_item[i]
                                        break
                                    
                                Undisplayed_csvfile = 'Files\Modules\Database\undisplayeditem.csv'
                                WriteCSV([und_item], Undisplayed_csvfile)


                                for i in range(len(loc_itemnumber)):
                                    if loc_itemnumber[i] == lis[0]:
                                        del loc_itemnumber[i]
                                        del a_1[i]
                                        del a_2[i]
                                        del a_3[i]
                                        del a_4[i]
                                        del a_5[i]
                                        del a_6[i]
                                        del a_7[i]
                                        del a_8[i]

                                        a_total = [loc_itemnumber, a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8]
                                        loc_csvfile = 'Files\Modules\Database\inventorylocator.csv'
                                        his_csvfile = 'Files\Modules\Database\historyinvloc.csv'
                                        WriteCSV(a_total, loc_csvfile)
                                        WriteCSV(a_total, his_csvfile)
                                        
                                        break
                                    
                            elif int(item_qty[i]) < 0:
                                validity = 23
                                return [validity]
                        else:
                            if lis[3] == '' or lis[4] == '':
                                validity = 6
                                return [validity]
                            else:
                                if store_price[i] == lis[4] and supplier_price[i] != lis[3]:
                                    validity = 13
                                    return [validity]
                                elif supplier_price[i] == lis[3] and store_price[i] != lis[4]:
                                    validity = 14
                                    return [validity]
                                else:
                                    validity = 15
                                    return [validity]
                    else:
                        validity = 12
                        return [validity]


            returnlis = [item_number, item_name, item_qty, supplier_price, store_price]

            return returnlis



#list1=['8','8','4','8','8']
#new_list=ReadItemCSV2(list1)

def Remove_Item(lis):
    if len(lis) == 1:
        return False, lis[0]
    else:
        csvfile = 'Files\Modules\Database\inventory.csv'
        WriteInvCSV(lis, csvfile)
        return [True]
#Remove_Item(new_list)

