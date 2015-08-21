'''
    Version ALPHA 17/11/2011 Kyuho
'''

from Tkinter import *
from Swampy.Gui import * # Handles Graphics
import tkMessageBox

def Create(errorcode):
    if errorcode==1:
        label='Error: No input for item number'
    elif errorcode==2:
        label='Error: Illegal variable inputted for item number'
    elif errorcode==3:
        label='Error: Invalid input for item number'
    elif errorcode==4:
        label='Error: Item number exceeds the limited number of digits (maximum 6 digits).'
    elif errorcode==5:
        label='Error: Inputted item number does not exist in the inventory'
    elif errorcode==6:
        label='Error: The item is already placed in the aisles.'
    elif errorcode==7:
        label='Error: No item in the chosen aisle'
    elif errorcode==8:
        label='Error: Selected item not present in the chosen aisle'
    elif errorcode==9:
        label='Error: Aisle not selected: please choose an aisle'
    elif errorcode==10:
        label='Error: Aisle number is invalid'
    elif errorcode==11:
        label='Error: Wrong input for aisle number'
    elif errorcode==12:
        label='Error: Item is not present in the inventory'
    elif errorcode==13:
        label='Error: Item not selected: please choose an item'
        
    tkMessageBox.showwarning("Error", label) # Show Error in box
