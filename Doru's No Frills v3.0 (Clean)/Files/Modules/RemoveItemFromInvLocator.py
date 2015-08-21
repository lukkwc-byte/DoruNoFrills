'''
    Version ALPHA 17/11/2011 Kyuho (started + finished logic)
    Version 0.01 16/12/2011 Kyuho (implementing new csv format)
'''

import csv
from ReadCSV import *
from WriteCSV import *

def loc_out_RemoveItem(aisle_num, i_number):
    Undisplayed_list = Undisplayed_Read()
    und_item = Undisplayed_list[0]

    Inventorylist = Inv_Read()
    
    item_number = Inventorylist[0]

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
        if i_number in und_item:
            validity = 8
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
                ##                                                              ##
                ##################################################################

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

        if aisle_num == '1':
            item_check = 0
            for i in range(len(a_1[1:])):
                if a_1[1:][i] == 'Yes':
                    item_check = 1
                    break
            if item_check == 0:
                validity = 7
                return [validity]
            else:
                for i in range(len(loc_itemnumber)):
                    if loc_itemnumber[i] == i_number:
                        if a_1[i] == 'No':
                            validity = 8
                            return [validity]
                        else:
                            a_1[i] = 'No'
                            break
        if aisle_num == '2':
            item_check = 0
            for i in range(len(a_2[1:])):
                if a_2[1:][i] == 'Yes':
                    item_check = 1
                    break
            if item_check == 0:
                validity = 7
                return [validity]
            else:
                for i in range(len(loc_itemnumber)):
                    if loc_itemnumber[i] == i_number:
                        if a_2[i] == 'No':
                            validity = 8
                            return [validity]
                        else:
                            a_2[i] = 'No'
                            break
        if aisle_num == '3':
            item_check = 0
            for i in range(len(a_3[1:])):
                if a_3[1:][i] == 'Yes':
                    item_check = 1
                    break
            if item_check == 0:
                validity = 7
                return [validity]
            else:
                for i in range(len(loc_itemnumber)):
                    if loc_itemnumber[i] == i_number:
                        if a_3[i] == 'No':
                            validity = 8
                            return [validity]
                        else:
                            a_3[i] = 'No'
                            break
        if aisle_num == '4':
            item_check = 0
            for i in range(len(a_4[1:])):
                if a_4[1:][i] == 'Yes':
                    item_check = 1
                    break
            if item_check == 0:
                validity = 7
                return [validity]
            else:
                for i in range(len(loc_itemnumber)):
                    if loc_itemnumber[i] == i_number:
                        if a_4[i] == 'No':
                            validity = 8
                            return [validity]
                        else:
                            a_4[i] = 'No'
                            break
        if aisle_num == '5':
            item_check = 0
            for i in range(len(a_5[1:])):
                if a_5[1:][i] == 'Yes':
                    item_check = 1
                    break
            if item_check == 0:
                validity = 7
                return [validity]
            else:
                for i in range(len(loc_itemnumber)):
                    if loc_itemnumber[i] == i_number:
                        if a_5[i] == 'No':
                            validity = 8
                            return [validity]
                        else:
                            a_5[i] = 'No'
                            break
        if aisle_num == '6':
            item_check = 0
            for i in range(len(a_6[1:])):
                if a_6[1:][i] == 'Yes':
                    item_check = 1
                    break
            if item_check == 0:
                validity = 7
                return [validity]
            else:
                for i in range(len(loc_itemnumber)):
                    if loc_itemnumber[i] == i_number:
                        if a_6[i] == 'No':
                            validity = 8
                            return [validity]
                        else:
                            a_6[i] = 'No'
                            break
        if aisle_num == '7':
            item_check = 0
            for i in range(len(a_7[1:])):
                if a_7[1:][i] == 'Yes':
                    item_check = 1
                    break
            if item_check == 0:
                validity = 7
                return [validity]
            else:
                for i in range(len(loc_itemnumber)):
                    if loc_itemnumber[i] == i_number:
                        if a_7[i] == 'No':
                            validity = 8
                            return [validity]
                        else:
                            a_7[i] = 'No'
                            break
        if aisle_num == '8':
            item_check = 0
            for i in range(len(a_8[1:])):
                if a_8[1:][i] == 'Yes':
                    item_check = 1
                    break
            if item_check == 0:
                validity = 7
                return [validity]
            else:
                for i in range(len(loc_itemnumber)):
                    if loc_itemnumber[i] == i_number:
                        if a_8[i] == 'No':
                            validity = 8
                            return [validity]
                        else:
                            a_8[i] = 'No'
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

        no_ind = []
        for i in range(len(loc_itemnumber)):
            if a_1[i] == 'No' and a_2[i] == 'No' and a_3[i] == 'No' and a_4[i] == 'No' and a_5[i] == 'No' and a_6[i] == 'No' and a_7[i] == 'No' and a_8[i] == 'No':
                no_ind.append(i)

        no_ind = no_ind[::-1]

        if no_ind != []:
            for i in range(len(no_ind)):
                del loc_itemnumber[no_ind[i]]
                del a_1[no_ind[i]]
                del a_2[no_ind[i]]
                del a_3[no_ind[i]]
                del a_4[no_ind[i]]
                del a_5[no_ind[i]]
                del a_6[no_ind[i]]
                del a_7[no_ind[i]]
                del a_8[no_ind[i]]

        loc_itemnumber = ['item'] + loc_itemnumber
        a_1 = ['aisle1'] + a_1
        a_2 = ['aisle2'] + a_2
        a_3 = ['aisle3'] + a_3
        a_4 = ['aisle4'] + a_4
        a_5 = ['aisle5'] + a_5
        a_6 = ['aisle6'] + a_6
        a_7 = ['aisle7'] + a_7
        a_8 = ['aisle8'] + a_8

        a_total = [loc_itemnumber, a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8]

        loc_csvfile = 'Files\Modules\Database\inventorylocator.csv'
        WriteCSV(a_total, loc_csvfile)
                                            # history csv #
        his_csvfile = 'Files\Modules\Database\historyinvloc.csv'
        WriteCSV(a_total, his_csvfile)

        if i_number not in und_item:
            und_item.append(i_number)

        lis=und_item[1:]
        for i in range(len(lis)):
            lis[i] = int(lis[i])

        lis.sort()

        for i in range(len(lis)):
            lis[i] = str(lis[i])

        lis = ['item'] + lis

        Undisplayed_csvfile = 'Files\Modules\Database\undisplayeditem.csv'
        WriteCSV([lis], Undisplayed_csvfile)


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
