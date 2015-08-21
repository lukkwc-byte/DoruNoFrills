'''
    Version ALPHA 14/11/2011 Kyuho
    Version 0.01 15/11/2011 Kyuho (implemented validity 1~6)
    Version 0.02 16/11/2011 Kyuho (deleting item number from undisplayeditem.csv)
    Version 0.03 16/12/2011 Kyuho (implementing new csv format)
'''

import csv
from ReadCSV import *
from WriteCSV import *

def loc_in_AddItem(aisle_num, i_number):
    Inventorylist = Inv_Read()
    
    item_number = Inventorylist[0]
    item_qty = Inventorylist[2]

    validity = 0
    number_list = '0123456789'
    for i in range(1):
        if aisle_num == None:
            validity = 9
            break
        if i_number == '':      # check if it's '' or None
            validity = 1
            break
        if '|' in i_number or ',' in i_number:
            validity = 2
            break
        for i in range(len(i_number)):
            if i_number[i] not in number_list:
                validity = 3
                break
        if len(i_number) > 6:
            validity = 4
            break
        for i in range(len(aisle_num)):
            if aisle_num[i] not in number_list:
                validity = 11
                break
        if i_number not in item_number:
            validity = 5
            break
        if float(aisle_num) < 1 or float(aisle_num) > 8:
            validity = 10
            break


                ##################################################################
                ##                                                              ##
                ##    validity[1] = empty item number                           ##
                ##    validity[2] = invalid symbol for input                    ##
                ##    validity[3] = string / float for item number              ##
                ##    validity[4] = item number range                           ##
                ##    validity[5] = invalid item number (not in inventory)      ##
                ##    validity[6] = item already placed in the aisles           ##
                ##    validity[9] = aisle not selected                          ##
                ##    validity[10] = invalid aisle number                       ##
                ##    validity[11] = string / float for aisle number            ##
                ##    validity[12] = item quantity of selected item is 0        ##
                ##                                                              ##
                ##################################################################


    upd_item_number = []
    upd_item_qty = []

    for i in range(len(item_qty)):
        if item_qty[i] != '0':
            upd_item_number.append(item_number[i])
            upd_item_qty.append(item_qty[i])

    item_number = upd_item_number
    item_qty = upd_item_qty

    if i_number not in item_number:
        validity = 12


    if validity > 0:
        return [validity]

    else:
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

        new_loc_itemnumber = ['item']
        b_1 = ['aisle1']
        b_2 = ['aisle2']
        b_3 = ['aisle3']
        b_4 = ['aisle4']
        b_5 = ['aisle5']
        b_6 = ['aisle6']
        b_7 = ['aisle7']
        b_8 = ['aisle8']

        for i in range(len(loc_itemnumber)):
            if a_1[i] == 'Yes' or a_2[i] == 'Yes' or a_3[i] == 'Yes' or a_4[i] == 'Yes' or a_5[i] == 'Yes' or a_6[i] == 'Yes' or a_7[i] == 'Yes' or a_8[i] == 'Yes':
                new_loc_itemnumber.append(loc_itemnumber[i])
                b_1.append(a_1[i])
                b_2.append(a_2[i])
                b_3.append(a_3[i])
                b_4.append(a_4[i])
                b_5.append(a_5[i])
                b_6.append(a_6[i])
                b_7.append(a_7[i])
                b_8.append(a_8[i])

        loc_itemnumber = new_loc_itemnumber
        a_1 = b_1
        a_2 = b_2
        a_3 = b_3
        a_4 = b_4
        a_5 = b_5
        a_6 = b_6
        a_7 = b_7
        a_8 = b_8

        if i_number in loc_itemnumber:
            validity = 6
            return [validity]

        else:
            if i_number not in loc_itemnumber:
                loc_itemnumber.append(i_number)
                a_1.append('No')
                a_2.append('No')
                a_3.append('No')
                a_4.append('No')
                a_5.append('No')
                a_6.append('No')
                a_7.append('No')
                a_8.append('No')

            quantity_display = 0

            for i in range(len(loc_itemnumber)):
                if loc_itemnumber[i] == i_number:
                    if aisle_num == '1':
                        a_1[i] = 'Yes'
                    if aisle_num == '2':
                        a_2[i] = 'Yes'
                    if aisle_num == '3':
                        a_3[i] = 'Yes'
                    if aisle_num == '4':
                        a_4[i] = 'Yes'
                    if aisle_num == '5':
                        a_5[i] = 'Yes'
                    if aisle_num == '6':
                        a_6[i] = 'Yes'
                    if aisle_num == '7':
                        a_7[i] = 'Yes'
                    if aisle_num == '8':
                        a_8[i] = 'Yes'
            
                Undisplayed_list = Undisplayed_Read()
                und_item = Undisplayed_list[0]

                for i in range(len(und_item)):
                    if und_item[i] == i_number:
                        del und_item[i]
                        break

            loc_itemnumber = loc_itemnumber[1:]
            a_1 = a_1[1:]
            a_2 = a_2[1:]
            a_3 = a_3[1:]
            a_4 = a_4[1:]
            a_5 = a_5[1:]
            a_6 = a_6[1:]
            a_7 = a_7[1:]
            a_8 = a_8[1:]

            for i in range(len(loc_itemnumber)):
                loc_itemnumber[i] = int(loc_itemnumber[i])

            copy_itemnumber = loc_itemnumber
            loc_itemnumber = loc_itemnumber[:]

            copy_itemnumber.sort()

            order = []
            for i in range(len(copy_itemnumber)):
                for j in range(len(loc_itemnumber)):
                    if copy_itemnumber[i] == loc_itemnumber[j]:
                        order.append(j)

            for i in range(len(loc_itemnumber)):
                loc_itemnumber[i] = str(loc_itemnumber[i])

            b_itemnumber = []
            b_1 = []
            b_2 = []
            b_3 = []
            b_4 = []
            b_5 = []
            b_6 = []
            b_7 = []
            b_8 = []
            
            for i in range(len(order)):
                b_itemnumber.append(loc_itemnumber[order[i]])
                b_1.append(a_1[order[i]])
                b_2.append(a_2[order[i]])
                b_3.append(a_3[order[i]])
                b_4.append(a_4[order[i]])
                b_5.append(a_5[order[i]])
                b_6.append(a_6[order[i]])
                b_7.append(a_7[order[i]])
                b_8.append(a_8[order[i]])

            loc_itemnumber = ['item'] + b_itemnumber
            a_1 = ['aisle1'] + b_1
            a_2 = ['aisle2'] + b_2
            a_3 = ['aisle3'] + b_3
            a_4 = ['aisle4'] + b_4
            a_5 = ['aisle5'] + b_5
            a_6 = ['aisle6'] + b_6
            a_7 = ['aisle7'] + b_7
            a_8 = ['aisle8'] + b_8



            lis=und_item[1:]
            for i in range(len(lis)):
                lis[i] = int(lis[i])

            lis.sort()

            for i in range(len(lis)):
                lis[i] = str(lis[i])

            lis = ['item'] + lis
            
            csvfile='Files\Modules\Database\undisplayeditem.csv'

            WriteCSV([lis],csvfile)

            lis1=[loc_itemnumber,a_1,a_2,a_3,a_4,a_5,a_6,a_7,a_8]
            loc_csvfile = 'Files\Modules\Database\inventorylocator.csv'
            WriteCSV(lis1, loc_csvfile)


                                                # history csv #
            his_csvfile = 'Files\Modules\Database\historyinvloc.csv'
            WriteCSV(lis1, his_csvfile)

            loc_itemnumber = loc_itemnumber[1:]
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
                        num_list.append(loc_itemnumber[i])
            elif aisle_num == '2':
                for i in range(len(a_2)):
                    if a_2[i] == 'Yes':
                        num_list.append(loc_itemnumber[i])
            elif aisle_num == '3':
                for i in range(len(a_3)):
                    if a_3[i] == 'Yes':
                        num_list.append(loc_itemnumber[i])
            elif aisle_num == '4':
                for i in range(len(a_4)):
                    if a_4[i] == 'Yes':
                        num_list.append(loc_itemnumber[i])
            elif aisle_num == '5':
                for i in range(len(a_5)):
                    if a_5[i] == 'Yes':
                        num_list.append(loc_itemnumber[i])
            elif aisle_num == '6':
                for i in range(len(a_6)):
                    if a_6[i] == 'Yes':
                        num_list.append(loc_itemnumber[i])
            elif aisle_num == '7':
                for i in range(len(a_7)):
                    if a_7[i] == 'Yes':
                        num_list.append(loc_itemnumber[i])
            elif aisle_num == '8':
                for i in range(len(a_8)):
                    if a_8[i] == 'Yes':
                        num_list.append(loc_itemnumber[i])

            return True, num_list
