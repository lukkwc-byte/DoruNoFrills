''' File Log:
    Version 0.01 13/10/2011 Jonathan (Popup GUI)
    Version 0.02 20/10/2011 Kevin
    Version 0.03 26/10/2011 Michael
    Version 0.04 09/11/2011 Kyuho (Cash Errors)
    Version 0.05 09/11/2011 Jonathan (TkMessageBOX)
    Version 0.06 10/11/2011 Kyuho (Additional error)
    Version 0.07 14/12/2011 Jonathan (Additional scenario for Inv Print)
'''

from Tkinter import *
from Swampy.Gui import * # Handles Graphics
import tkMessageBox

def Create(errorcode):
    if errorcode==1:
        label='Error: Illegal characters entered'
    elif errorcode==2:
        label='Error: Item Number must only contain digits'
    elif errorcode==3:
        label='Error: Maximum limit of characters for item number is 6'
    elif errorcode==4:
        label='Error: Only numbers and decimals may be \n entered for supplier price'
    elif errorcode==5:
        label='Error: Only numbers and decimals may be \n entered for store price'
    elif errorcode==6:
        label='Error: Entries are missing'
    elif errorcode==7:
        label='Error: Illegal Quantity entered'
    elif errorcode==8:
        label='Error: Maximum character length for item name is 15'
    elif errorcode==9:
        label='Error: Maximum character length for item quantity is 4'
    elif errorcode==10:
        label='Error: Maximum character length for supplier price is 8'
    elif errorcode==11:
        label='Error: Maximum character length for store price is 8'
    elif errorcode==12:
        label='Error: Item name and number do not match the current database'
    elif errorcode==13:
        label='Error: The item\'s supplier price does not match the supplier price inputted'
    elif errorcode==14:
        label='Error: The item\'s store price does not match the store price inputted'
    elif errorcode==15:
        label='Error: The item\'s supplier and store prices do not match with the ones inputted'
    elif errorcode==16:
        label='Error: Cannot find the .CSV file'
    elif errorcode==17:
        label='Error: Quantity must be greater than 0'
    elif errorcode==18:
        label='Error: Quantity added is more than the quantity available in the Inventory'
    elif errorcode==19:
        label='Error: Invalid characters in the user payment entry'
    elif errorcode==20:
        label='Error: There are too many decimals in the user payment entry'
    elif errorcode==21:
        label='Error: Customer\'s payment is less than the total.'
    elif errorcode==22:
        label='Error: Invalid user payment was entered (must be up to 2 decimal places only)'
    elif errorcode==23:
        label='Error: Cannot delete more items'
    elif errorcode==24:
        label='Error: There is no valid item to delete for the current transaction.'
    elif errorcode==26:
        label='Error: User payment was not entered'
    elif errorcode==27:
        label='Error: The are no items present in the transaction, so it cannot be completed'
    elif errorcode==28:
        label='Error: No such item exists in the inventory.'
    elif errorcode==29:
        label='Error: There is currently no transaction in progress'
    elif errorcode==30:
        label='Error: An item with this ID # already exists in the inventory'
    elif errorcode==31:
        label='Error: The inventory is empty, so there is nothing to print'
    elif errorcode==32:
        label='Error: The quantity must be greater than 0'
    elif errorcode==33:
        label='Error: The format of the selected .CSV file is incorrect'
    elif errorcode==34:
        label='Error: Improper values and/or variables exist in the .CSV file'
    elif errorcode==35:
        label='Error: An item with this ID # already exists in the inventory, under a different item name'
    elif errorcode==36:
        label='Error: The inputted item name already exists in the inventory'
    elif errorcode==37:
        label='Error: Cannot put 0 in front of a digit i.e.) 0001 is invalid'
    elif errorcode==38:
        label='Error: The selected item is not in the inventory.'
    elif errorcode==50:
        label='Error: Please select an item'

    tkMessageBox.showwarning("Error", label) # Show Error in box


