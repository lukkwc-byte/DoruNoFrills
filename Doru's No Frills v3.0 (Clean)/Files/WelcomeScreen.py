''' File Log:
    Version 0.01 27/09/2011 Justin (Welcome Screen Logic)
    Version ALPHA 27/09/2011 Jonathan (Linking to Navigation, modifying GUI)
    Version 0.03 03/10/2011 Jonathan (Folder Path)
'''

from Tkinter import *
from Swampy.Gui import *

def Create(self):
    self.WelcomeScreen = self.row()
    self.WelcomeScreen.photo = Tkinter.PhotoImage(file='Files/Images/WelcomeLogo.gif')
    self.WelcomeScreen.photoLA = self.la(image=self.WelcomeScreen.photo, bg='#bfbfbf')
    self.endrow()

