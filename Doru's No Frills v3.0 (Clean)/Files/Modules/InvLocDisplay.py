'''
    Version ALPHA 30/11/2011 Kyuho (display logic)
'''


import csv
from ReadCSV import *

def loc_displayed(self, upd_list):
    if upd_list != False:
        self.InvLoc.ItemsInAisle.delete(0, 'end')
                
        Inventorylist=Inv_Read()

        item_number = Inventorylist[0]
        item_name = Inventorylist[1]
        item_qty = Inventorylist[2]
        store_price = Inventorylist[3]
        supplier_price = Inventorylist[4]

        item_number = item_number[1:]
        item_name = item_name[1:]
        item_qty = item_qty[1:]
        store_price = store_price[1:]
        supplier_price = supplier_price[1:]

        fix_list = []
        for i in range(len(upd_list)):
            for j in range(len(item_number)):
                if upd_list[i] == item_number[j]:
                    if item_qty[j] != '0':
                        fix_list.append(upd_list[i])
                        break
        upd_list = fix_list
        ### updated list = all item number of the updated aisle ###

        dis_item_number = upd_list
        dis_item_name = []
        dis_item_qty = []

        if dis_item_number == ['0']:
            dis_item_name = ['0']
            dis_item_qty = ['0']

        else:
            for i in range(len(upd_list)):
                for j in range(len(item_number)):
                    if upd_list[i] == item_number[j]:
                        dis_item_name.append(item_name[j])
                        dis_item_qty.append(item_qty[j])
                        break
            ## Alotted Spaces ##
            char1 = 13
            char2 = 20
            char3 = 6

            for i in range(len(dis_item_number)):
                space0 = 1 * ' '
                space1 = (char1-len(dis_item_number[i])) * ' '
                space2 = (char2-len(dis_item_name[i])) * ' '
                space3 = (char3-len(dis_item_qty[i])) * ' '

                displaylist = dis_item_name[i] + space2 + dis_item_qty[i]
                self.InvLoc.ItemsInAisle.insert('end', displaylist)

def loc_undisplayed_list():
    Und_list = Undisplayed_Read()

    lis = Und_list[0]
    lis = lis[1:]

    copy_lis = lis
    lis = lis[:]

    for i in range(len(copy_lis)):
        copy_lis[i] = int(copy_lis[i])

    copy_lis.sort()

    for i in range(len(copy_lis)):
        copy_lis[i] = str(copy_lis[i])

    return copy_lis


def loc_undisplayed(self):
    self.InvLoc.Warehouse.delete(0, 'end')

    lis = loc_undisplayed_list()

    Inventorylist=Inv_Read()
    item_number = Inventorylist[0]
    item_name = Inventorylist[1]
    item_qty = Inventorylist[2]
    store_price = Inventorylist[3]
    supplier_price = Inventorylist[4]

    item_number = item_number[1:]
    item_name = item_name[1:]
    item_qty = item_qty[1:]
    store_price = store_price[1:]
    supplier_price = supplier_price[1:]

    update_lis = []

    for i in range(len(lis)):
        for j in range(len(item_number)):
            if lis[i] == item_number[j]:
                if item_qty[j] != '0':
                    update_lis.append(lis[i])
                    break

    lis = update_lis

    ### updated list = all item number of the updated aisle ###

    dis_item_number = lis
    dis_item_name = []
    dis_item_qty = []

    for i in range(len(lis)):
        for j in range(len(item_number)):
            if lis[i] == item_number[j]:
                dis_item_name.append(item_name[j])
                dis_item_qty.append(item_qty[j])
                break

    ## Alotted Spaces ##
    char1 = 13
    char2 = 20
    char3 = 6

    for i in range(len(dis_item_number)):
        space0 = 1 * ' '
        space1 = (char1-len(dis_item_number[i])) * ' '
        space2 = (char2-len(dis_item_name[i])) * ' '
        space3 = (char3-len(dis_item_qty[i])) * ' '

        displaylist = dis_item_name[i] + space2 + dis_item_qty[i]
        self.InvLoc.Warehouse.insert('end', displaylist)
