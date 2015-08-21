''' File Log:
    Version 0.01 16/12/2011 Kevin (Popup GUI)
'''

from Tkinter import *
from Swampy.Gui import * # Handles Graphics
import tkMessageBox

def Create(errorcode):
    if errorcode==1:
        label='Error: The Old Password inputted is incorrect'

    tkMessageBox.showwarning("Error", label) # Show MULTIPLE INSTANCE
