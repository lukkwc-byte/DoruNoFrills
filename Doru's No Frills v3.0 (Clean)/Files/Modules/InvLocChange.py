import csv
from ReadCSV import *
from WriteCSV import *


def InvLoc_Change_Remove_Inv(i_number):
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

    for i in range(len(a_1)):
        if a_1[i] == i_number:
            del a_1[i]
            break
    for i in range(len(a_2)):
        if a_2[i] == i_number:
            del a_2[i]
            break
    for i in range(len(a_3)):
        if a_3[i] == i_number:
            del a_3[i]
            break
    for i in range(len(a_4)):
        if a_4[i] == i_number:
            del a_4[i]
            break
    for i in range(len(a_5)):
        if a_5[i] == i_number:
            del a_5[i]
            break
    for i in range(len(a_6)):
        if a_6[i] == i_number:
            del a_6[i]
            break
    for i in range(len(a_7)):
        if a_7[i] == i_number:
            del a_7[i]
            break
    for i in range(len(a_8)):
        if a_8[i] == i_number:
            del a_8[i]
            break

    loc_csvfile = 'Files\Modules\Database\inventorylocator.csv'
    a_total = [loc_item, a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8]
    WriteCSV(a_total, loc_csvfile)

                                        # history csv #
    his_csvfile = 'Files\Modules\Database\historyinvloc.csv'
    WriteCSV(a_total, his_csvfile)


def Check_Cancel_Trans():
    Historylist = HistoryInvLoc_Read()
    his_item = Historylist[0]
    a_1 = Historylist[1]
    a_2 = Historylist[2]
    a_3 = Historylist[3]
    a_4 = Historylist[4]
    a_5 = Historylist[5]
    a_6 = Historylist[6]
    a_7 = Historylist[7]
    a_8 = Historylist[8]
    
    loc_csvfile = 'Files\Modules\Database\inventorylocator.csv'
    a_total = [his_item, a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8]
    WriteCSV(a_total, loc_csvfile)


def Check_Pay_Final():
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

                                        # history csv #
    his_csvfile = 'Files\Modules\Database\historyinvloc.csv'
    a_total = [loc_item, a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8]
    WriteCSV(a_total, his_csvfile)


def InvLoc_Change_Remove_Cash(i_number):
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

    loc_ind = 0

    for i in range(len(loc_item)):
        if loc_item[i] == i_number:
            loc_ind = i
            if a_1[loc_ind] == 'Yes':
                a_1[loc_ind] = 'No'                
            elif a_2[loc_ind] == 'Yes':
                a_2[loc_ind] = 'No'
            elif a_3[loc_ind] == 'Yes':
                a_3[loc_ind] = 'No'
            elif a_4[loc_ind] == 'Yes':
                a_4[loc_ind] = 'No'
            elif a_5[loc_ind] == 'Yes':
                a_5[loc_ind] = 'No'
            elif a_6[loc_ind] == 'Yes':
                a_6[loc_ind] = 'No'
            elif a_7[loc_ind] == 'Yes':
                a_7[loc_ind] = 'No'
            elif a_8[loc_ind] == 'Yes':
                a_8[loc_ind] = 'No'

            if a_1[loc_ind] == 'No' and a_2[loc_ind] == 'No' and a_3[loc_ind] == 'No' and a_4[loc_ind] == 'No' and a_5[loc_ind] == 'No' and a_6[loc_ind] == 'No' and a_7[loc_ind] == 'No' and a_8[loc_ind] == 'No':
                del loc_item[loc_ind]
                del a_1[loc_ind]
                del a_2[loc_ind]
                del a_3[loc_ind]
                del a_4[loc_ind]
                del a_5[loc_ind]
                del a_6[loc_ind]
                del a_7[loc_ind]
                del a_8[loc_ind]
            break


    a_total = [loc_item, a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8]

    loc_csvfile = 'Files\Modules\Database\inventorylocator.csv'
    WriteCSV(a_total, loc_csvfile)
