'''
    Version 0.01 xxx Ben (Initial 5-box setup)
    Version 0.02 21/10/2011 Jonathan (revamp - 1 listbox)
    Version 0.03 25/10/2011 Jonathan (Session support)
    Version 0.04 26/10/2011 Jonathan (GUI improvements)
'''

import csv
import Check
from ReadCSV import *

def FillDisplay(self, currsession):
    currsession = int(currsession)
    Inventorylist=Cash_Read()
    session_number = Inventorylist[1] 
    item_number = Inventorylist[2]                                                      # Kyuho
    item_name = Inventorylist[3]                                                        #
    item_qty = Inventorylist[4]                                                         #
    store_price = Inventorylist[7]                                                      #
    del session_number[0]
    del item_number[0]
    del item_name[0]
    del item_qty[0]
    del store_price[0]

    for i in range(len(session_number)):
        csv_session = int(session_number[i])

        if csv_session == currsession:
            store = '$'+str("%.2f" % (float(store_price[i])))
            total = '$'+str("%.2f" % (float(store_price[i])*int(item_qty[i])))
            lead = '@ '
            follow = ' ea.'


            ## Alotted Spaces ##
            char1 = 8 # Max 6 Dig
            char2 = 18 # Max 15 Dig
            char3 = 6 # Max 4 Dig
            char4 = 10 # Max 8 Dig
            
            space1 = (char1-len(item_number[i]))*' '
            space2 = (char2-len(item_name[i]))*' '
            space3 = (char3-len(item_qty[i]))*' '
            space4 = (char4-len(store))*' '

            itemlist = item_number[i]+space1+item_name[i]+space2+item_qty[i]+space3+lead+store+follow+space4+total
            self.CashRegister.Display.insert('end', itemlist)

def ClearDisplay(self):
    self.CashRegister.Display.delete(0, 'end')
