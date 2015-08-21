''' File Log:
    Version 0.01 27/09/2011 Justin (Welcome Screen Logic)
    Version ALPHA 27/09/2011 Jonathan (Linking to Navigation, modifying GUI)
    Version 0.03 03/10/2011 Jonathan (Folder Path)
    Version 0.04 22/12/2011 Jonathan (Build Info)
'''

from Tkinter import *
from Swampy.Gui import *
import tkMessageBox
from Modules.ClearCSV import *
import Project
from Modules.ReadCSV import *
import Payroll

def Create(self):
    self.StoreSettings = self.col()
    self.row(pady=20)
    self.endrow()
    self.StoreSettings.title = self.la(text='Store Settings', font=('Calibri', '28', 'underline'))
    self.row(pady=20)
    self.endrow()

    self.StoreSettings.subtitle = self.la(text='Summary of Data', font=('Calibri', '18'))

    self.row(pady=5)
    self.endrow()
    self.StoreSettings.ticsrow = self.row()

    self.StoreSettings.ticrow = self.row(border=3, bg='#404040', padx=145)
    self.StoreSettings.ticgrid = self.gr(cols=2)
    self.StoreSettings.emp = self.la(text='# of Employees', font='Calibri, 12', bg='lightgrey')
    self.StoreSettings.empst = self.la(font='Calibri, 12')
    self.StoreSettings.shift = self.la(text='# of Approved Shifts', font='Calibri, 12', bg='lightgrey')
    self.StoreSettings.shiftst = self.la(font='Calibri, 12')
    self.StoreSettings.sale = self.la(text='# of Sales', font='Calibri, 12', bg='lightgrey')
    self.StoreSettings.salest = self.la(font='Calibri, 12')
    self.StoreSettings.inv = self.la(text='# of Inventory Items', font='Calibri, 12', bg='lightgrey')
    self.StoreSettings.invst = self.la(font='Calibri, 12')    
    self.endgr()

    self.endrow()
    self.endrow()    

    self.StoreSettings.seperatela1 = self.la(height=1)
    
    self.StoreSettings.statrow = self.row(weights=[0,1,0])
    self.StoreSettings.sep = self.la(width=20)
    self.StoreSettings.gridrow = self.row(border=3, bg='#404040')
    self.StoreSettings.gridrow.grid = self.gr(cols=3, bd=2)
    self.StoreSettings.gridrow.grid.HR = self.la(text='Human Resources', font='Calibri, 12', bg='lightgrey')
    self.StoreSettings.gridrow.grid.HRst = self.la(font='Calibri, 12')
    self.StoreSettings.gridrow.grid.HRcl = self.bu(text='Reset Database', background='#41627E', fg='white', pady=4, padx=30, font='Calibri, 11', command=Callable(clear_csv, self, 'HR'))
    self.StoreSettings.gridrow.grid.Pay = self.la(text='Payroll', font='Calibri, 12', bg='lightgrey')
    self.StoreSettings.gridrow.grid.Payst = self.la(font='Calibri, 12')
    self.StoreSettings.gridrow.grid.Paycl = self.bu(text='Reset Database', background='#41627E', fg='white', pady=4, padx=30, font='Calibri, 11', command=Callable(clear_csv, self, 'Pay'))
    self.StoreSettings.gridrow.grid.Inv = self.la(text='Inventory', font='Calibri, 12', bg='lightgrey')
    self.StoreSettings.gridrow.grid.Invst = self.la(font='Calibri, 12')
    self.StoreSettings.gridrow.grid.Invcl = self.bu(text='Reset Database', background='#41627E', fg='white', pady=4, padx=30, font='Calibri, 11', command=Callable(clear_csv, self, 'Inv'))
    self.StoreSettings.gridrow.grid.Cash = self.la(text='Cash Register', font='Calibri, 12', bg='lightgrey')
    self.StoreSettings.gridrow.grid.Cashst = self.la(font='Calibri, 12')
    self.StoreSettings.gridrow.grid.Cashcl = self.bu(text='Reset Database', background='#41627E', fg='white', pady=4, padx=30, font='Calibri, 11', command=Callable(clear_csv, self, 'Cash'))


    
    self.endgr()
    
    self.endrow()
    self.StoreSettings.sep = self.la(width=20)
    self.endrow()
    self.row(pady=5)
    self.endrow()
    

    self.StoreSettings.resetall = self.bu(text='Reset Store', background='#41627E', fg='white', height=2, pady=4, padx=145, font='Calibri, 11', command=Callable(clear_csv, self, 'ALL'))
    self.row(pady=500)
    self.endrow()
    self.endcol()
    RefreshStatus(self)
    RefreshStic(self)

def RefreshStatus(self):
    HRCheck = HRFuncCheck()
    PayCheck = PayFuncCheck()
    InvCheck = InvFuncCheck()
    CashCheck = CashFuncCheck()
    
    if HRCheck == True:
        self.StoreSettings.gridrow.grid.HRst.config(text='OK', fg='green')
    elif HRCheck == False:
        self.StoreSettings.gridrow.grid.HRst.config(text='Corrupt', fg='red')

    if PayCheck == True:
        self.StoreSettings.gridrow.grid.Payst.config(text='OK', fg='green')
    elif PayCheck == False:
        self.StoreSettings.gridrow.grid.Payst.config(text='Corrupt', fg='red')

    if InvCheck == True:
        self.StoreSettings.gridrow.grid.Invst.config(text='OK', fg='green')
    elif InvCheck == False:
        self.StoreSettings.gridrow.grid.Invst.config(text='Corrupt', fg='red')

    if CashCheck == True:
        self.StoreSettings.gridrow.grid.Cashst.config(text='OK', fg='green')
    elif CashCheck == False:
        self.StoreSettings.gridrow.grid.Cashst.config(text='Corrupt', fg='red')

def RefreshStic(self):
    HRCheck = HRFuncCheck()
    PayCheck = PayFuncCheck()
    InvCheck = InvFuncCheck()
    CashCheck = CashFuncCheck()
    
    if HRCheck == True:
        SticCheck = SticFuncCheck()
        self.StoreSettings.empst.config(text=SticCheck[0], fg='black')
    elif HRCheck == False:
        self.StoreSettings.empst.config(text='Corrupt', fg='red')

    if PayCheck == True:
        SticCheck = SticFuncCheck()
        self.StoreSettings.shiftst.config(text=SticCheck[1], fg='black')
    elif PayCheck == False:
        self.StoreSettings.shiftst.config(text='Corrupt', fg='red')

    if CashCheck == True:
        SticCheck = SticFuncCheck()
        self.StoreSettings.salest.config(text=SticCheck[2], fg='black')
    elif CashCheck == False:
        self.StoreSettings.salest.config(text='Corrupt', fg='red')

    if InvCheck == True:
        SticCheck = SticFuncCheck()
        self.StoreSettings.invst.config(text=SticCheck[3], fg='black')
    elif InvCheck == False:
        self.StoreSettings.invst.config(text='Corrupt', fg='red')
        

def SticFuncCheck():
    returnlist = []

    Emplist = Account_Read()
    returnlist.append(len(Emplist[0])-1)

    Shiftlist = EmployeePay_Read()
    returnlist.append(len(Shiftlist[0])-1)

    Salelist = Session_Read()
    returnlist.append(len(Salelist[0])-1)

    Invlist = Inv_Read()
    returnlist.append(len(Invlist[0])-1)

    return returnlist
                      
def clear_csv(self, name):
    if name == 'HR':
        check = show_warning(1)
        if check == True:
            ClearHR()
            RunSetup(self) # Setup a new admin account since database empty
    if name == 'Pay':
        check = show_warning(2)
        if check == True:
            ClearPay()
            RefreshStatus(self)
            RefreshStic(self)
            Payroll.test()
    if name == 'Inv':
        check = show_warning(3)
        if check == True:
            ClearInv()
            RefreshStatus(self)
            RefreshStic(self)
    if name == 'Cash':
        check = show_warning(4)
        if check == True:
            ClearCash()
            RefreshStatus(self)
            RefreshStic(self)
    if name == 'ALL':
        check = show_warning(5)
        if check == True:
            ClearCash()
            ClearInv()
            ClearPay()
            ClearHR()
            RunSetup(self) # Setup a new admin account since database empty
            
def show_warning(warncode):
    if warncode==1:
        label = 'Performing this task will clear the Human Resources database and erase all user accounts. However, any transactions and inventory informatin will remain. The store setup will be run in order to create a new administor account. \n\nAre you sure you want to proceed?'
    if warncode==2:
        label = 'Performing this task will clear the Payroll databases and erase all shifts worked. This change is permenant and cannot be reversed.\n\nAre you sure you want to proceed?'
    if warncode==3:
        label = 'Performing this task will clear the Inventory and Stock Locator databases and erases all purchase history. This change is permenant and cannot be reversed.\n\nAre you sure you want to proceed?'
    if warncode==4:
        label = 'Performing this task will clear the Cash Register databases and erase all transaction history. This change is permenant and cannot be reversed.\n\nAre you sure you want to proceed?'
    if warncode==5:
        label = 'Performing this task will clear the ALL of the store databases and return the store to its original state. The store setup will be run in order to create a new administrator account. \n\nAre you sure you want to proceed?'

    result = tkMessageBox.askyesno("Warning", label) # Show error in box
    return result

def RunSetup(self): # Setup a new admin account since database empty
    self.destroy()
    Project.CreateSetup('NoFrills')

def HRFuncCheck():
    try:
        returnlist = Account_Read()
        for i in range(len(returnlist)):
            for p in range(len(returnlist[i])):
                if returnlist[i][p] == '':
                    return False
        return True
    except:
        return False


def PayFuncCheck():
    try:
        returnlist = Payroll_Read()
        for i in range(len(returnlist)):
            for p in range(len(returnlist[i])):
                if returnlist[i][p] == '':
                    return False
        returnlist = EmployeePay_Read()
        for i in range(len(returnlist)):
            for p in range(len(returnlist[i])):
                if returnlist[i][p] == '':
                    return False
        return True
    except:
        return False

def InvFuncCheck():
    try:
        returnlist = Inv_Read()
        for i in range(len(returnlist)):
            for p in range(len(returnlist[i])):
                if returnlist[i][p] == '':
                    return False
        returnlist = InvChange_Read()
        for i in range(len(returnlist)):
            for p in range(len(returnlist[i])):
                if returnlist[i][p] == '':
                    return False
        returnlist = InventoryLoc_Read()
        for i in range(len(returnlist)):
            for p in range(len(returnlist[i])):
                if returnlist[i][p] == '':
                    return False
        returnlist = HistoryInvLoc_Read()
        for i in range(len(returnlist)):
            for p in range(len(returnlist[i])):
                if returnlist[i][p] == '':
                    return False
        returnlist = Undisplayed_Read()
        for i in range(len(returnlist)):
            for p in range(len(returnlist[i])):
                if returnlist[i][p] == '':
                    return False
        return True
    except:
        return False

def CashFuncCheck():
    try:
        returnlist = Cash_Read()
        for i in range(len(returnlist)):
            for p in range(len(returnlist[i])):
                if returnlist[i][p] == '':
                    return False
        returnlist = Session_Read()
        for i in range(len(returnlist)):
            for p in range(len(returnlist[i])):
                if returnlist[i][p] == '':
                    return False
        returnlist = Check_Read()
        for i in range(len(returnlist)):
            for p in range(len(returnlist[i])):
                if returnlist[i][p] == '':
                    return False
        return True
    except:
        return False
