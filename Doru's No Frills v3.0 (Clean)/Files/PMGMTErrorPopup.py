''' File Log:
    Version 0.01 27/10/2011 Kevin (Popup GUI)
    Version 0.02 31/10/2011 Jonathan (Re-order errors, fixed GUI)
'''

from Tkinter import *
from Swampy.Gui import * # Handles Graphics
import tkMessageBox

def Create(errorcode):
    if errorcode==1:
        label='Error: No shift has been selected'
    elif errorcode==2:
        label='Error: Illegal characters entered'
    elif errorcode==3:
        label='Error: Illegal characters entered'
    elif errorcode==4:
        label='Error: Illegal characters entered'
    elif errorcode==5:
        label='Error: Illegal characters entered'
    elif errorcode==6:
        label='Error: Illegal characters entered'
    elif errorcode==7:
        label='Error: Illegal characters entered'
    elif errorcode==8:
        label='Error: Illegal characters entered'
    elif errorcode==9:
        label='Error: Illegal characters entered'
    elif errorcode==10:
        label='Error: Illegal characters entered'
    elif errorcode==11:
        label='Error: Illegal characters entered'
    elif errorcode==12:
        label='Error: Illegal characters entered'
    elif errorcode==13:
        label='Error: Illegal characters entered'
    elif errorcode==14:
        label='Error: Illegal characters entered'
    elif errorcode==15:
        label='Error: Illegal characters entered'
    elif errorcode==16:
        label='Error: Illegal characters entered'
    elif errorcode==17:
        label='Error: Illegal characters entered'
    elif errorcode==18:
        label='Error: Illegal characters entered'
    elif errorcode==19:
        label='Error: Illegal characters entered'
    elif errorcode==20:
        label='Error: Illegal characters entered'
    elif errorcode==21:
        label='Error: Illegal characters entered'
    elif errorcode==22:
        label='Error: Illegal characters entered'
    elif errorcode==23:
        label='Error: Illegal characters entered'
    elif errorcode==24:
        label='Error: Illegal characters entered'
    elif errorcode==25:
        label='Error: Illegal characters entered'
    elif errorcode==26:
        label='Error: Illegal characters entered'
    elif errorcode==27:
        label='Error: Illegal characters entered'
    elif errorcode==28:
        label='Error: Illegal characters entered'
    elif errorcode==29:
        label='Error: Illegal characters entered'

    tkMessageBox.showwarning("Error", label) # Show error in box
