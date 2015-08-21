''' File Log:
    Version 0.01 13/10/2011 Jonathan (Popup GUI)
    Version 0.02 26/10/2011 Jonathan (Handles popup exit & recreation)
    Version 0.03 14/12/2011 Jonathan (Centered in screen)
'''

from Tkinter import *
from Swampy.Gui import * # Handles Graphics
import CashRegister
import Modules.CashReceipt

def CreatePopUp(old, paid,change, session):
    self = Gui(debug=False)
    self.protocol("WM_DELETE_WINDOW", Callable(Destroy, self, old))
    self.grab_set_global()
    self.focus_force()
    sw = self.winfo_screenwidth()
    sh = self.winfo_screenheight()
    x = (sw/2) - (450/2) 
    y = (sh/2) - (150/2)
    self.geometry('%dx%d+%d+%d' % (450, 150, x, y))
    self.resizable(width=False, height=False)
    self.title('Transaction Details')
    self.logo=Tkinter.PhotoImage(file='Files\Images\SmallLogo.gif')

    self.gr(cols=2)
    self.la('Amount Paid',font='Calibri',pady=15)
    self.la('Change Tendered',font='Calibri',pady=15)
    paidentry = self.en(font='Calibri', padx=15, text=paid, justify=CENTER, readonlybackground='white')
    changeentry = self.en(font='Calibri',  padx=15, text=change, justify=CENTER, readonlybackground='white')
    paidentry.config(state='readonly')
    changeentry.config(state='readonly')
    self.endgr()
    self.la()
    self.row(weights=[0,1])
    self.bu('OK', padx=5, pady=7, font='Calibri', background='#47c57f', justify=CENTER, width='40', command=Callable(Destroy, self, old))
    self.bu('Print Receipt', padx=7, pady=7, font='Calibri', background='#d94444', justify=CENTER, width='5', command=Callable(Print, self, old, session, paid, change))
    self.endrow()
    self.mainloop()
    
def Destroy(self,old):
    self.destroy()
    old.CashRegister.destroy()
    CashRegister.Create(old)

def Print(self,old, session, paid, change):
    self.destroy()
    old.CashRegister.destroy()
    CashRegister.Create(old)
    Modules.CashReceipt.Create(session, paid, change)

