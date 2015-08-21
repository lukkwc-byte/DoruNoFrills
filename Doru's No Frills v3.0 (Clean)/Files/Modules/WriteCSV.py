import csv



def WriteCSV(lis, csvfile):
    DB = csv.writer(open(csvfile, 'wb'), delimiter = ',', quotechar = '|')
    for i in range(len(lis[0])):
        row = []
        for j in range(len(lis)):
            row.append(lis[j][i])
        DB.writerow(row)



def WriteInvCSV(lis, csvfile):
    item_number = lis[0][1:]
    item_name = lis[1][1:]
    item_qty = lis[2][1:]
    store_price = lis[4][1:]
    supplier_price = lis[3][1:]

    copy_item = item_number
    item_number = item_number[:]

    int_copy = []
    for i in range(len(copy_item)):
        int_copy.append(int(copy_item[i]))

    copy_item = int_copy

    copy_item.sort()

    str_copy = []
    for i in range(len(copy_item)):
        str_copy.append(str(copy_item[i]))

    copy_item = str_copy

    sort_ind = []
    for i in range(len(copy_item)):
        for j in range(len(item_number)):
            if copy_item[i] == item_number[j]:
                sort_ind.append(j)


    new_item_number = []
    new_item_name = []
    new_item_qty = []
    new_store_price = []
    new_supplier_price = []
    
    for i in range(len(sort_ind)):
        new_item_number.append(item_number[sort_ind[i]])
        new_item_name.append(item_name[sort_ind[i]])
        new_item_qty.append(item_qty[sort_ind[i]])
        new_store_price.append(store_price[sort_ind[i]])
        new_supplier_price.append(supplier_price[sort_ind[i]])

    new_item_number = ['itemnumber'] + new_item_number
    new_item_name = ['itemname'] + new_item_name
    new_item_qty = ['itemquantity'] + new_item_qty
    new_store_price = ['storeprice'] + new_store_price
    new_supplier_price = ['supplierprice'] + new_supplier_price

    newlis = [new_item_number, new_item_name, new_item_qty, new_supplier_price, new_store_price]
    WriteCSV(newlis, csvfile)

### inv locator csv edit ###


def InvLoc_Edit(lis):
    longest = 0
    for i in range(len(lis)):
        if len(lis[i]) > longest:
            longest = len(lis[i])

    for i in range(len(lis)):
        if len(lis[i]) < longest:
            for i in range(longest-len(lis[i])):
                lis[i].append('')

    return lis
