'''
    Version 0.01 02/12/2011 Jonathan
    Version 0.02 26/12/2011 Jonathan (Added additional scenario for sales reports)
'''

from Tkinter import *
from Swampy.Gui import * # Handles Graphics
import tkMessageBox

def Create(errorcode):
    if errorcode==1:
        label='Error: Invalid Date (must be proper dates formatted in DD/MM/YYYY)'
    elif errorcode==2:
        label='Error: The date range is invalid (includes dates which have not yet occured)'
    elif errorcode==3:
        label='Error: Invalid username entered (case-sensetive)'
    elif errorcode==4:
        label='Error: Please enter a valid date (must be DD/MM/YYYY) before launching a different report'
    elif errorcode==5:
        label='Error: The date range is invalid (starting date must be before ending date)'
    elif errorcode==6:
        label='Error: The transaction ID entered does not match with any transactions in the database'
    elif errorcode==7:
        label='Error: Please enter a transaction ID before proceeding'

    tkMessageBox.showwarning("Error", label) # Show Error in box
