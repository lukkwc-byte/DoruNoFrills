'''
    Version ALPHA 14/11/2011 Kyuho
    Version 0.01 16/11/2011 Kyuho (completed logic)
'''

import csv
from ReadCSV import *
from WriteCSV import *
def loc_Aisle_DisplayItem(aisle_num):
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

    loc_item = loc_item[1:]
    a_1 = a_1[1:]
    a_2 = a_2[1:]
    a_3 = a_3[1:]
    a_4 = a_4[1:]
    a_5 = a_5[1:]
    a_6 = a_6[1:]
    a_7 = a_7[1:]
    a_8 = a_8[1:]

    num_list = []
    
    if aisle_num == '1':
        for i in range(len(a_1)):
            if a_1[i] == 'Yes':
                num_list.append(loc_item[i])
        if num_list == []:
            return False
        else:
            return num_list

    if aisle_num == '2':
        for i in range(len(a_2)):
            if a_2[i] == 'Yes':
                num_list.append(loc_item[i])
        if num_list == []:
            return False
        else:
            return num_list

    if aisle_num == '3':
        for i in range(len(a_3)):
            if a_3[i] == 'Yes':
                num_list.append(loc_item[i])
        if num_list == []:
            return False
        else:
            return num_list

    if aisle_num == '4':
        for i in range(len(a_4)):
            if a_4[i] == 'Yes':
                num_list.append(loc_item[i])
        if num_list == []:
            return False
        else:
            return num_list

    if aisle_num == '5':
        for i in range(len(a_5)):
            if a_5[i] == 'Yes':
                num_list.append(loc_item[i])
        if num_list == []:
            return False
        else:
            return num_list

    if aisle_num == '6':
        for i in range(len(a_6)):
            if a_6[i] == 'Yes':
                num_list.append(loc_item[i])
        if num_list == []:
            return False
        else:
            return num_list

    if aisle_num == '7':
        for i in range(len(a_7)):
            if a_7[i] == 'Yes':
                num_list.append(loc_item[i])
        if num_list == []:
            return False
        else:
            return num_list

    if aisle_num == '8':
        for i in range(len(a_8)):
            if a_8[i] == 'Yes':
                num_list.append(loc_item[i])
        if num_list == []:
            return False
        else:
            return num_list

