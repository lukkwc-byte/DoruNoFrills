''' File Log:
    Version 0.01 27/10/2011 Kevin (Popup GUI)
    Version 0.02 31/10/2011 Jonathan (Re-order errors, fixed GUI)
'''

from Tkinter import *
from Swampy.Gui import * # Handles Graphics
import tkMessageBox

def Create(errorcode):
    if errorcode==13:
        label='Error: One or more entry is empty'
    elif errorcode==1:
        label='Error: Illegal characters entered'
    elif errorcode==2:
        label='Error: There is a space in the username'
    elif errorcode==4:
        label='Error: Too many characters in the username \n (must be less than 12)'
    elif errorcode==3:
        label='Error: There is a space in the password'
    elif errorcode==5:
        label='Error: Too many characters in the password \n (must be less than 12)'
    elif errorcode==6:
        label='Error: Level must be either a 0 or 1'
    elif errorcode==8:
        label='Error: Level must be either a 0 or 1'
    elif errorcode==9:
        label='Error: Hourly Wage must only have numbers and decimals'
    elif errorcode==7:
        label='Error: Hourly Wage is too long (must be \n less than 6 characters, four before the decimal and 2 after the decimal)'
    elif errorcode==10:
        label='Error: The Hourly Wage must be greater than .'
    elif errorcode==12:
        label='Error: There are too many decimal points in the hourly wage'
    elif errorcode==14:
        label='Error: Your security question can not be longer than 35 characters.'
    elif errorcode==15:
        label='Error: Your security answer can not be longer than 15 characters.'
    elif errorcode==17:
        label='Error: The username entry can not be empty when you delete something'
    elif errorcode==16:
        label='Error: The user you are trying to delete does not exist'
    elif errorcode==11:
        label='Error: The username is already taken'
    elif errorcode==22:
        label='Error: Please select a user'
    elif errorcode==23:
        label='Error: You cannot delete the user that is currently logged in'

    tkMessageBox.showwarning("Error", label) # Show error in box
