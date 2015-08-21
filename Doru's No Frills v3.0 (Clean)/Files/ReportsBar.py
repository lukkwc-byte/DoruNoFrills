'''
    Version 0.01 16/11/2011 Jonathan (Initial Linking)
    Version 0.02 17/11/2011 Jonathan (Date support)
    Version 0.02 26/12/2011 Jonathan (Fixed error with switching screens)

    


'''


from Tkinter import *
from Swampy.Gui import * # Handles Graphics
import HRReports
import ReportsSumm
import SalesReports
import PurchReports
#import ICReports
import Modules.Check
import ReportsErrorPopup
import datetime

from Modules.ReadCSV import *


def Create(self):
    self.ReportsBar = self.col()
    self.ReportsBar.buttons = self.row()
    self.ReportsBar.buttons.Summary=self.bu('Summary', activebackground='#4f81bd',height=1, width=15, pady=15, padx=30, font=', 11', bg='#4f81bd', overrelief='groove', relief='sunken',bd=2, state='disabled', disabledforeground='black', command = Callable(Nav_Summary, self))
    self.ReportsBar.buttons.Sales=self.bu('Sales', activebackground='#4f81bd', disabledforeground = 'black', height=1, width=15, pady=15, padx=30, font=', 11', overrelief='groove', bg='#4f81bd',  bd=2,  command = Callable(Nav_Sales, self))
    self.ReportsBar.buttons.Purch=self.bu('Purchases', activebackground='#4f81bd',height=1, width=15, pady=15, padx=30, font=', 11',  bg='#4f81bd',  disabledforeground='black', bd=2,overrelief='groove',  command = Callable(Nav_Purch, self))
    #self.ReportsBar.buttons.IC=self.bu('Item Comparison', activebackground='#4f81bd',height=1, width=15, font=', 11', pady=15, padx=30,  bg='#4f81bd', disabledforeground='black', bd=2, overrelief='groove', command = Callable(Nav_IC, self))
    self.ReportsBar.buttons.HR=self.bu('Human Resources', activebackground='#4f81bd',height=1, width=15, font=', 11', pady=15, padx=30,  bg='#4f81bd', disabledforeground='black', bd=2, overrelief='groove', command = Callable(Nav_HR, self))
    self.endrow()
    self.ReportsBar.seperatedate = self.la(height=1)
    self.ReportsBar.daterow = self.row(weights=[0,1,1,1,1,1,1,0])
    self.ReportsBar.seperatela7 = self.la(width=25)
    
    bdate = datetime.date.today()
    bdate = bdate.strftime("%d/%m/%Y")
    edate = datetime.date.today()
    edate = edate.strftime("%d/%m/%Y") 

    self.ReportsBar.bdate_la = self.la(text='Date From:',font='Calibri,12', padx=5)
    self.ReportsBar.bdate_en = self.en(text=bdate, bg='white',font='Calibri,12')
    self.ReportsBar.edate_la = self.la(text='Date To:',font='Calibri,12', padx=5)
    self.ReportsBar.edate_en = self.en(text=edate, bg='white',font='Calibri,12')
    self.ReportsBar.enterbutton = self.bu(text='Refresh',font='Calibri,12', padx=10, bg='#47c57f', command=Callable(Refresh, self, False))   
    self.ReportsBar.showbutton =self.bu(text='Show All', font='Calibri,12', bg='#d94444', command = Callable(Refresh, self, True))


    self.ReportsBar.seperatela8 = self.la(width=25)
    self.endrow() #Date Row
    self.endcol() # Main Row

def Refresh(self, all):
    bdate = self.ReportsBar.bdate_en.get()
    edate = self.ReportsBar.edate_en.get()  
    if all == True:
        self.ReportsBar.bdate_en.delete(0, 'end')
        self.ReportsBar.bdate_en.insert('end', 'ALL')
        self.ReportsBar.edate_en.delete(0, 'end')
        self.ReportsBar.edate_en.insert('end', 'ALL')
        window = Modules.Check.openwindow
        if window == 'Reports Summary':
            ReportsSumm.RefreshEntries(self, all)
        elif window == 'HR Reports':
            HRReports.RefreshDisplay(self, all)
        elif window == 'Sales Reports':
            SalesReports.RefreshDisplay(self, all)
        elif window == 'Purchase Reports':
            PurchReports.RefreshDisplay(self, all)
        #elif window == 'IC Reports':
         #   ICReports.RefreshEntries(self, all)
         
    elif bdate == 'ALL' and edate == 'ALL':
        window = Modules.Check.openwindow
        if window == 'Reports Summary':
            ReportsSumm.RefreshEntries(self, all)
        elif window == 'HR Reports':
            HRReports.RefreshDisplay(self, all)
        elif window == 'Sales Reports':
            SalesReports.RefreshDisplay(self, all)
        elif window == 'Purchase Reports':
            PurchReports.RefreshDisplay(self, all)
        #elif window == 'IC Reports':
         #   ICReports.RefreshEntries(self, all)
         
    else:
        try:                       
            bdate = bdate.split('/')
            edate = edate.split('/')
            for i in range(len(bdate)):
                bdate[i] = int(bdate[i])
            for i in range(len(edate)):
                edate[i] = int(edate[i])            
            bdate=datetime.date(bdate[2],bdate[1],bdate[0])
            edate=datetime.date(edate[2],edate[1],edate[0])
            todaysdate = datetime.date.today()
            
        
            if todaysdate >= bdate and todaysdate >= edate:
                if edate >= bdate:
                    window = Modules.Check.openwindow
                    if window == 'Reports Summary':
                        ReportsSumm.RefreshEntries(self, all)
                    elif window == 'HR Reports':
                        HRReports.RefreshDisplay(self, all)
                    elif window == 'Sales Reports':
                        SalesReports.RefreshDisplay(self, all)
                    elif window == 'Purchase Reports':
                        PurchReports.RefreshDisplay(self, all)
                    #elif window == 'IC Reports':
                     #   ICReports.RefreshEntries(self, all)
                else:
                    window = Modules.Check.openwindow
                    if window == 'Reports Summary':
                        ReportsSumm.ClearEntries(self)
                    elif window == 'HR Reports':
                        HRReports.ClearDisplay(self)
                    elif window == 'Sales Reports':
                        SalesReports.ClearDisplay(self)
                    elif window == 'Purchase Reports':
                        PurchReports.ClearDisplay(self)

                    ReportsErrorPopup.Create(5)
            else:
                window = Modules.Check.openwindow
                if window == 'Reports Summary':
                    ReportsSumm.ClearEntries(self)
                elif window == 'HR Reports':
                    HRReports.ClearDisplay(self)
                elif window == 'Sales Reports':
                    SalesReports.ClearDisplay(self)
                elif window == 'Purchase Reports':
                    PurchReports.ClearDisplay(self)

                ReportsErrorPopup.Create(2)
        except:
            window = Modules.Check.openwindow
            if window == 'Reports Summary':
                ReportsSumm.ClearEntries(self)
            elif window == 'HR Reports':
                HRReports.ClearDisplay(self)
            elif window == 'Sales Reports':
                SalesReports.ClearDisplay(self)
            elif window == 'Purchase Reports':
                PurchReports.ClearDisplay(self)


            ReportsErrorPopup.Create(1)

def Nav_Summary(self):
    if Modules.Check.openwindow != 'HR Reports Summary':
        if Modules.Check.BUSY == False:
            if DateValidation(self) == True:
                DestroyWindow(self)
                self.ReportsBar.buttons.Summary.config(state='disabled',relief='sunken')
                self.ReportsBar.buttons.HR.config(state='active',relief='raised')
                self.ReportsBar.buttons.Sales.config(state='active',relief='raised')
                self.ReportsBar.buttons.Purch.config(state='active',relief='raised')
                #self.ReportsBar.buttons.IC.config(state='active',relief='raised')
                ReportsSumm.Create(self)
                self.title('Doru\'s No Frills - Reports (Summary)') 
                Modules.Check.openwindow = "Reports Summary"
        else:
            Modules.Check.BusyAlert(self)
    else:
        Modules.Check.InstanceAlert(self)

def Nav_HR(self):
    if Modules.Check.openwindow != 'HR Reports':
        if Modules.Check.BUSY == False:
            if DateValidation(self) == True:
                DestroyWindow(self)
                self.ReportsBar.buttons.Summary.config(state='active',relief='raised')
                self.ReportsBar.buttons.HR.config(state='disabled',relief='sunken')
                self.ReportsBar.buttons.Sales.config(state='active',relief='raised')
                self.ReportsBar.buttons.Purch.config(state='active',relief='raised')
                #self.ReportsBar.buttons.IC.config(state='active',relief='raised')
                HRReports.Create(self)
                self.title('Doru\'s No Frills - HR Reports') 
                Modules.Check.openwindow = "HR Reports"
        else:
            Modules.Check.BusyAlert(self)
    else:
        Modules.Check.InstanceAlert(self)
    
def Nav_Sales(self):
    if Modules.Check.openwindow != 'Sales Reports':
        if Modules.Check.BUSY == False:
            if DateValidation(self) == True:
                DestroyWindow(self)
                self.ReportsBar.buttons.Summary.config(state='active',relief='raised')
                self.ReportsBar.buttons.HR.config(state='active',relief='raised')
                self.ReportsBar.buttons.Sales.config(state='disabled',relief='sunken')
                self.ReportsBar.buttons.Purch.config(state='active',relief='raised')
                #self.ReportsBar.buttons.IC.config(state='active',relief='raised')
                SalesReports.Create(self)
                self.title('Doru\'s No Frills - Sales Reports') 
                Modules.Check.openwindow = "Sales Reports"
        else:
            Modules.Check.BusyAlert(self)
    else:
        Modules.Check.InstanceAlert(self)

def Nav_Purch(self):
    if Modules.Check.openwindow != 'Purchase Reports':
        if Modules.Check.BUSY == False:
            if DateValidation(self) == True:
                DestroyWindow(self)
                self.ReportsBar.buttons.Summary.config(state='active',relief='raised')
                self.ReportsBar.buttons.HR.config(state='active',relief='raised')
                self.ReportsBar.buttons.Sales.config(state='active',relief='raised')
                self.ReportsBar.buttons.Purch.config(state='disabled',relief='sunken')
                #self.ReportsBar.buttons.IC.config(state='active',relief='raised')
                PurchReports.Create(self)
                self.title('Doru\'s No Frills - Purchase Reports') 
                Modules.Check.openwindow = "Purchase Reports"
        else:
            Modules.Check.BusyAlert(self)
    else:
        Modules.Check.InstanceAlert(self)

#def Nav_IC(self):
 #   if Modules.Check.openwindow != 'IC Reports':
  #      if Modules.Check.BUSY == False:
            #if DateValidation(self) == True:
       #         DestroyWindow(self)
        #        self.ReportsBar.buttons.Summary.config(state='active',relief='raised')
         #       self.ReportsBar.buttons.HR.config(state='active',relief='raised')
          #      self.ReportsBar.buttons.Sales.config(state='active',relief='raised')
           #     self.ReportsBar.buttons.Purch.config(state='active',relief='raised')
            #    self.ReportsBar.buttons.IC.config(state='disabled',relief='sunken')
             #   ICReports.Create(self)
              #  self.title('Doru\'s No Frills - Item Comparison Reports') 
               # Modules.Check.openwindow = "IC Reports"
        #else:
         #   Modules.Check.BusyAlert(self)
    #else:
     #   Modules.Check.InstanceAlert(self)

def DestroyWindow(self):
    try:
        self.ReportsSumm.destroy()
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
    #try:
     #   self.ICReports.destroy()
    #except:
     #   None


def DateValidation(self):
    bdate = self.ReportsBar.bdate_en.get()
    edate = self.ReportsBar.edate_en.get()
    if bdate == 'ALL' and edate == 'ALL':
        return True
    else:
        try:
            bdate = bdate.split('/')
            edate = edate.split('/')
            for i in range(len(bdate)):
                bdate[i] = int(bdate[i])
            for i in range(len(edate)):
                edate[i] = int(edate[i])            
            bdate=datetime.date(bdate[2],bdate[1],bdate[0])
            edate=datetime.date(edate[2],edate[1],edate[0])
            todaysdate = datetime.date.today()            
            if todaysdate >= bdate and todaysdate >= edate:
                return True
            else:
                ReportsErrorPopup.Create(4)
                return False
        except:
            ReportsErrorPopup.Create(4)
            return False
