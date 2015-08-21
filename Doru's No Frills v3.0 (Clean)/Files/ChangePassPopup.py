''' File Log:
    Version 0.01 27/10/2011 Kevin (Popup GUI)
    Version 0.02 31/10/2011 Jonathan (Re-order errors, fixed GUI)
'''

from Tkinter import *
from Swampy.Gui import * # Handles Graphics
import tkMessageBox

def Create(errorcode):
    if errorcode==1:
        label='Error: The Old Password inputted is incorrect'
    elif errorcode==2:
        label='Error: The New Password does not match the Confirmed Password'
    elif errorcode==3:
        label='Error: The old password was not inputted'
    elif errorcode==4:
        label='Error: The new password was not inputted'        
    elif errorcode==5:
        label='Error: The confirm password was not inputted'
    elif errorcode==6:
        label='Error: The new security question was not inputted'
    elif errorcode==7:
        label='Error: The new security answer was not inputted'
    elif errorcode==8:
        label='Error: Illegal symbol inputted in the old password entry'
    elif errorcode==9:
        label='Error: Illegal symbol inputted in the new password entry'
    elif errorcode==10:
        label='Error: Illegal symbol inputted in the confirm password entry'
    elif errorcode==11:
        label='Error: The old password cannot be longer than 12 characters'
    elif errorcode==12:
        label='Error: The new password cannot be longer than 12 characters'
    elif errorcode==13:
        label='Error: The confirm password cannot be longer than 12 characters'
    elif errorcode==14:
        label='Error: Illegal symbol inputted in the old security answer entry'
    elif errorcode==15:
        label='Error: Illegal symbol inputted in the new security question entry'
    elif errorcode==16:
        label='Error: Illegal symbol inputted in the new security answer entry'
    elif errorcode==17:
        label='Error: The new security question cannot be longer than 35 characters'
    elif errorcode==18:
        label='Error: The  new security answer cannot be longer than 14 characters'
    elif errorcode==19:
        label='Error: The old security answer cannot be longer than 14 characters'
    elif errorcode==20:
        label='Error: The old security answer was not inputted'
    elif errorcode==21:
        label='Error: Spaces were inputted in the old password entry'
    elif errorcode==22:
        label='Error: Spaces were inputted in the new password entry'
    elif errorcode==23:
        label='Error: Spaces were inputted in the confirm password entry'
    elif errorcode==24:
        label='Error: Spaces were inputted in the old security answer entry'
    elif errorcode==25:
        label='Error: Spaces were inputted in the new security question entry'
    elif errorcode==26:
        label='Error: Spaces were inputted in the new security answer entry'

    tkMessageBox.showwarning("Error", label) # Show MULTIPLE INSTANCE
