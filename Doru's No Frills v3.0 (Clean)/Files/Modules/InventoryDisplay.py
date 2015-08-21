'''
    Version 0.xx 23/11/2011 Jonathan (Spacing fix)
    Version 0.01 05/12/2011 Kyuho (quantity 0 display)
'''

import csv
from ReadCSV import *

def FillDisplay(self):  
    Inventorylist=Inv_Read()
    item_number = Inventorylist[0]
    item_name = Inventorylist[1]
    item_qty = Inventorylist[2]
    supplier_price = Inventorylist[3]
    store_price = Inventorylist[4]
    
    del item_number[0]
    del item_name[0]
    del item_qty[0]
    del supplier_price[0]
    del store_price[0]
    
    for i in range(len(item_number)):
        store = float(store_price[i])
        supplier = float(supplier_price[i])
        store = "%.2f" % store
        supplier = "%.2f" % supplier
        store = '$'+str(store)
        supplier = '$'+str(supplier)

        ## Alotted Spaces ##
        char1 = 8 # Max 6 Dig
        char2 = 18 # Max 15 Dig
        char3 = 6 # Max 4 Dig
        char4 = 14 # Max 8 Dig
        char5 = 14 # Max 8 Dig
        
        space1 = (char1-len(item_number[i]))*' '
        space2 = (char2-len(item_name[i]))*' '
        space3 = (char3-len(item_qty[i]))*' '
        space4 = (char4-len(supplier))*' '
        space5 = (char5-len(store))*' '

        itemlist = item_number[i]+space1+item_name[i]+space2+item_qty[i]+space3+supplier+space4+store
        self.InvManage.Display.insert('end', itemlist)

def ClearDisplay(self):
    self.InvManage.Display.delete(0, 'end')
