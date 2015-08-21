''' File Log:
    Version 0.01 26/12/2011 Jonathan

'''

from Tkinter import *
from Swampy.Gui import *
import tkMessageBox
import Modules.Check

def Create():
    self = Gui(debug=False)
    self.grab_set_global()
    self.focus_force()
    sw = self.winfo_screenwidth()
    sh = self.winfo_screenheight()
    x = (sw/2) - (456/2) 
    y = (sh/2) - (450/2)
    self.geometry('%dx%d+%d+%d' % (456, 450, x, y))
    self.resizable(width=False, height=False)
    self.title('About')
    photo = PhotoImage(file='Files\Images\About.gif', master=self) 
    canvas = self.ca(width=456, height=388)
    canvas.image([0,0], image=photo)
    self.protocol("WM_DELETE_WINDOW", Callable(shutdown, self))
    self.bu('EXIT', padx=100, font='Calibri', background='#d94444', justify=CENTER, width='40', command=Callable(shutdown, self))
    self.la()
    self.mainloop()
    
def shutdown(self):
    Modules.Check.about = 'closed'
    self.destroy()
