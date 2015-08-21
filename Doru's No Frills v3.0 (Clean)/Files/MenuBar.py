''' File Log:
    Version 0.01 19/09/2011 Jonathan (GUI only)
    Version 0.02 20/09/2011 Jonathan (Updated GUI, began logic for inheritance)
    Version 0.03 22/09/2011 Jonathan (Experimenting with screen layout and inheritance. Completed visuals)
    Version 0.04 24/09/2011 Jonathan (Destroy methods)
    Version ALPHA 27/09/2011 Jonathan (Navigation complete with exisisting screens)
    Version 0.06 04/10/2011 Jonathan (Folder path)
    Version 0.07 08/10/2011 Jonathan (Dealing with userlevel logic)
    Version 0.08 01/11/2011 Jonathan (Added support for AcctSettings screen)
    Version 0.09 08/11/2011 Jonathan (Added support for date inheritance in Reports)
    Version 0.10 08/11/2011 Jonathan (Acct Management > Employee Management // Change Pass >> Acct Settings)
    Version 0.11 10/11/2011 Jonathan (Nav support for new Reports screens)
    Version 0.12 10/16/2011 Jonathan (Continued Nav support for new Reports screens)
    Version 0.13 17/16/2011 Jonathan (Namechange - Reports >> ReportsSumm)


'''
from Tkinter import *
import tkMessageBox # Handles Textbox
from Swampy.Gui import * # Handles Graphics
import Modules.Check # Window Creation/Destroy Modules.Checks
import CashRegister
import InvLoc
import InvManage
import EmpAccounts
import Payroll
import ReportsSumm
import Help
import Project
import time
import AcctSettings
import ReportsBar
import StoreSettings
import PayrollManagement
import About

time1 = ''
 


def Create(self):
    ### Setup Error-proofing ###

    Modules.Check.CashError()
    
    self.geometry('1024x768')
    self.state(newstate='zoomed')
    self.menu = self.row(background='#4f81bd')

    self.menu.cash = self.bu(text='Cash Register', bd=1, font=', 10', background='#404040', fg='white', pady=15, padx=8, activebackground='#404040', activeforeground='white', command=Callable(Nav_Cash, self))
    self.menu.inventory = self.mb(text='  Inventory  ', font=', 10', background='#404040', fg='white', pady=15, padx=8, activebackground='#404040', activeforeground='white')
    if Modules.Check.userlevel == '1':
        self.menu.inventory.manage = self.mi(self.menu.inventory, font=', 10', text='Inventory Management', command=Callable(Nav_InvManage, self))
    self.menu.inventory.locator = self.mi(self.menu.inventory, font=', 10', text='Inventory Locator', command=Callable(Nav_InvLoc, self))
    if Modules.Check.userlevel == '1':
        self.menu.employment = self.mb(text='Management', font=', 10', background='#404040', fg='white', pady=15, padx=8, activebackground='#404040', activeforeground='white')

        self.menu.employment.acc = self.mi(self.menu.employment, font=', 10', text='Employee Management', command=Callable(Nav_EmpAccounts, self))
        self.menu.employment.PayrollManagement = self.mi(self.menu.employment, font=', 10', text='Payroll Management', command=Callable(Nav_PayrollManagement, self))

    if Modules.Check.userlevel == '1':
        self.menu.reports = self.bu(text='   Reports   ', bd=1, font=', 10', background='#404040', fg='white', pady=15, padx=8, command=Callable(Nav_ReportsSumm, self), activebackground='#404040', activeforeground='white')
        
    self.menu.cp = self.mb(text='Control Panel', font=', 10', background='#404040', fg='white', pady=15, padx=8, activebackground='#404040', activeforeground='white')
    self.menu.cp.payroll = self.mi(self.menu.cp, font=', 10', text='Start / End Shift', command=Callable(Nav_Payroll, self))
    self.menu.cp.AcctSettings = self.mi(self.menu.cp, font=', 10', text='Account Settings', command=Callable(Nav_AcctSettings, self))
    if Modules.Check.userlevel == '1':
        self.menu.employment.StoreSettings = self.mi(self.menu.cp, font=', 10', text='Store Settings', command=Callable(Nav_StoreSettings, self))

    self.menu.help = self.mb(text='     Help     ', font=', 10', background='#404040', fg='white', pady=15, padx=8, activebackground='#404040', activeforeground='white')
        
    self.menu.help.manual = self.mi(self.menu.help, text='Program Manual', font=', 10', command=Callable(Nav_Manual, self))
    self.menu.help.about = self.mi(self.menu.help, text='About', font=', 10',  command=Callable(Nav_About, self))
    self.protocol("WM_DELETE_WINDOW", Callable(shutdown, self))
    self.endrow()


def shutdown(self):
    if Modules.Check.BUSY == False:            
        self.destroy()
    else:
        Modules.Check.BusyAlert(self)        

def DestroyWindow(self):
    try:
        self.WelcomeScreen.destroy()
    except:
        None
    try: 
        self.CashRegister.destroy()
    except:
        None
    try:
        self.Login.destroy()
    except:
        None
    try:
        self.InvLoc.destroy()
        Modules.Check.Aisle_number = None
    except:
        None
    try:
        self.InvManage.destroy()
    except:
        None
    try:   
        self.ReportsSumm.destroy()
    except:
        None
    try:
        self.Help.destroy()
    except:
        None
    try:
        self.EmpAccounts.destroy()
    except:
        None
    try:
        self.Payroll.destroy()
    except:
        None
    try:
        self.AcctSettings.destroy()
    except:
        None
    try: 
        self.HRReports.destroy()
    except:
        None
    try:
        self.SalesReports.destroy()
    except:
        None
    try:
        self.PurchReports.destroy()
    except:
        None
    try:
        self.ReportsBar.destroy()
    except:
        None
    try:
        self.StoreSettings.destroy()
    except:
        None
    try:
        self.PayrollManagement.destroy()
    except:
        None

           
                                        
def Nav_Cash(self):
    if Modules.Check.openwindow != 'CashRegister':
        if Modules.Check.BUSY == False:
            if Modules.Check.userlevel == '1':             
                DestroyWindow(self)
                CashRegister.Create(self)
                self.title('Doru\'s No Frills - Cash Register') 
                Modules.Check.openwindow = "CashRegister"
                self.menu.cash.config(state='disabled',relief='sunken')
                self.menu.inventory.config(state='active',relief='raised')
                if Modules.Check.userlevel == '1':
                    self.menu.employment.config(state='active',relief='raised')
                    self.menu.reports.config(state='active',relief='raised')
                self.menu.cp.config(state='active',relief='raised')
            else:
                if Modules.Check.shiftstat == 'Checked Out':   
                    Modules.Check.ShiftAlert(self)
                else:
                    DestroyWindow(self)
                    CashRegister.Create(self)
                    self.title('Doru\'s No Frills - Cash Register') 
                    Modules.Check.openwindow = "CashRegister"
                    self.menu.cash.config(state='disabled',relief='sunken')
                    self.menu.inventory.config(state='active',relief='raised')
                    if Modules.Check.userlevel == '1':
                        self.menu.employment.config(state='active',relief='raised')
                        self.menu.reports.config(state='active',relief='raised')
                    self.menu.cp.config(state='active',relief='raised')
        else:
            Modules.Check.BusyAlert(self)
    else:
        Modules.Check.InstanceAlert(self)


def Nav_InvManage(self):
    if Modules.Check.openwindow != 'InvManage':
        if Modules.Check.BUSY == False:
            DestroyWindow(self)
            InvManage.Create(self)
            self.title('Doru\'s No Frills - Inventory Management') 
            Modules.Check.openwindow = "InvManage"
            self.menu.cash.config(state='active',relief='raised')
            self.menu.inventory.config(state='active',relief='sunken')
            if Modules.Check.userlevel == '1':
                self.menu.employment.config(state='active',relief='raised')
                self.menu.reports.config(state='active',relief='raised')
            self.menu.cp.config(state='active',relief='raised')
        else:
            Modules.Check.BusyAlert(self)
    else:
        Modules.Check.InstanceAlert(self)
        
def Nav_InvLoc(self):
    if Modules.Check.openwindow != 'InvLoc':
        if Modules.Check.BUSY == False:
            DestroyWindow(self)
            InvLoc.Create(self)
            self.title('Doru\'s No Frills - StockLocator') 
            Modules.Check.openwindow = "InvLoc"
            self.menu.cash.config(state='active',relief='raised')
            self.menu.inventory.config(state='disabled',relief='sunken')
            if Modules.Check.userlevel == '1':
                self.menu.inventory.config(state='active',relief='sunken')
                self.menu.employment.config(state='active',relief='raised')
                self.menu.reports.config(state='active',relief='raised')
            self.menu.cp.config(state='active',relief='raised')
        else:
            Modules.Check.BusyAlert(self)
    else:
        Modules.Check.InstanceAlert(self)

def Nav_EmpAccounts(self):
    if Modules.Check.openwindow != 'Employee Management':
        if Modules.Check.BUSY == False:
            DestroyWindow(self)
            EmpAccounts.Create(self)
            self.title('Doru\'s No Frills - Employee Management') 
            Modules.Check.openwindow = "Employee Management"
            self.menu.cash.config(state='active',relief='raised')
            self.menu.inventory.config(state='active',relief='raised')
            if Modules.Check.userlevel == '1':
                self.menu.employment.config(state='active',relief='sunken')
                self.menu.reports.config(state='active',relief='raised')
            self.menu.cp.config(state='active',relief='raised')
        else:
            Modules.Check.BusyAlert(self)
    else:
        Modules.Check.InstanceAlert(self)

def Nav_PayrollManagement(self):
    if Modules.Check.openwindow != 'Payroll Management':
        if Modules.Check.BUSY == False:
            DestroyWindow(self)
            PayrollManagement.Create(self)
            self.title('Doru\'s No Frills - Payroll Management') 
            Modules.Check.openwindow = "Payroll Management"
            self.menu.cash.config(state='active',relief='raised')
            self.menu.inventory.config(state='active',relief='raised')
            if Modules.Check.userlevel == '1':
                self.menu.employment.config(state='active',relief='sunken')
                self.menu.reports.config(state='active',relief='raised')
            self.menu.cp.config(state='active',relief='raised')
        else:
            Modules.Check.BusyAlert(self)
    else:
        Modules.Check.InstanceAlert(self)

def Nav_StoreSettings(self):
    if Modules.Check.openwindow != 'Store Settings':
        if Modules.Check.BUSY == False:
            DestroyWindow(self)
            StoreSettings.Create(self)
            self.title('Doru\'s No Frills - Store Settings') 
            Modules.Check.openwindow = "Store Settings"
            self.menu.cash.config(state='active',relief='raised')
            self.menu.inventory.config(state='active',relief='raised')
            if Modules.Check.userlevel == '1':
                self.menu.employment.config(state='active',relief='raised')
                self.menu.reports.config(state='active',relief='raised')
            self.menu.cp.config(state='active',relief='sunken')
        else:
            Modules.Check.BusyAlert(self)
    else:
        Modules.Check.InstanceAlert(self)
        
def Nav_Payroll(self):
    if Modules.Check.openwindow != 'Start / End Shift':
        if Modules.Check.BUSY == False:
            DestroyWindow(self)
            Payroll.Create(self)
            self.title('Doru\'s No Frills - Start / End Shift') 
            Modules.Check.openwindow = "Start / End Shift"
            self.menu.cash.config(state='active',relief='raised')
            self.menu.inventory.config(state='active',relief='raised')
            if Modules.Check.userlevel == '1':
                self.menu.employment.config(state='active',relief='raised')
                self.menu.reports.config(state='active',relief='raised')
            self.menu.cp.config(state='active',relief='sunken')
        else:
            Modules.Check.BusyAlert(self)
    else:
        Modules.Check.InstanceAlert(self)

def Nav_AcctSettings(self):
    if Modules.Check.openwindow != 'Account Settings':
        if Modules.Check.BUSY == False:
            DestroyWindow(self)
            AcctSettings.Create(self)
            self.title('Doru\'s No Frills - Account Settings') 
            Modules.Check.openwindow = "Account Settings"
            self.menu.cash.config(state='active',relief='raised')
            self.menu.inventory.config(state='active',relief='raised')
            if Modules.Check.userlevel == '1':
                self.menu.employment.config(state='active',relief='raised')
                self.menu.reports.config(state='active',relief='raised')
            self.menu.cp.config(state='active',relief='sunken')
        else:
            Modules.Check.BusyAlert(self)
    else:
        Modules.Check.InstanceAlert(self)
        
def Nav_ReportsSumm(self):
    if Modules.Check.openwindow != 'Reports Summary' and Modules.Check.openwindow != 'Sales Reports' and Modules.Check.openwindow != 'Purchase Reports' and Modules.Check.openwindow != 'HR Reports' and Modules.Check.openwindow != 'IC Reports':
        if Modules.Check.BUSY == False:
            DestroyWindow(self)
            ReportsBar.Create(self)
            ReportsSumm.Create(self)
            self.title('Doru\'s No Frills - Reports Summary') 
            Modules.Check.openwindow = "Reports Summary"
            self.menu.cash.config(state='active',relief='raised')
            self.menu.inventory.config(state='active',relief='raised')
            if Modules.Check.userlevel == '1':
                self.menu.employment.config(state='active',relief='raised')
                self.menu.reports.config(state='disabled',relief='sunken')
            self.menu.cp.config(state='active',relief='raised')
        else:
            Modules.Check.BusyAlert(self)
    else:
        Modules.Check.InstanceAlert(self)

def Nav_Manual(self):    
    Help.Create(self)

def Nav_About(self):
    if Modules.Check.about != 'open':
        if Modules.Check.BUSY == False:
            Modules.Check.about = 'open'
            About.Create()
        else:
            Modules.Check.BusyAlert(self)
    else:
        Modules.Check.InstanceAlert(self)
