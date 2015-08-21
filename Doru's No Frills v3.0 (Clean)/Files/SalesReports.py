'''
    Version 0.01 31/10/2011 Justin (started GUI)
    Version 0.02 04/11/2011 Justin (fixed spacing)
    Version 0.03 10/11/2011 Justin (fixed GUI)
    Version 0.04 10/11/2011 Jonathan (Sending date to GUI)
    Version 0.05 10/22/2011 Jonathan (GUI in finishing stages)
    


'''

from Tkinter import *
from Swampy.Gui import *
import Modules.SalesReportsDisplay
import csv
import ReportsErrorPopup
from Modules.ReadCSV import *


def Create(self):
    self.SalesReports = self.col()
    self.SalesReports.seperatela3 = self.la(height=1)
    self.SalesReports.empty_la = self.la()
    self.SalesReports.seperatela4 = self.la(height=1)
    self.SalesReports.DispRow = self.row(weights=[0,1,0])
    self.SalesReports.displa = self.la(width=2)
    self.SalesReports.displaygrid=self.gr(cols=2)
    
    self.SalesReports.toplabels = self.la(padx=10,text='  Transaction #              Subtotal                             Tax                                        Total                                    Performed by                  Occured On (DD/MM/YYYY)                                       ', bg='#404040', fg='White', font=('Calibri', 11), height=1)
    self.SalesReports.toplabel2 = self.la()


    
    self.SalesReports.Display = self.lb(height=10,padx=10,pady=5,font=('Courier'))
    self.SalesReports.scrollbar = self.sb(command=self.SalesReports.Display.yview)
    self.SalesReports.Display.config(yscrollcommand=self.SalesReports.scrollbar.set)
    self.endgr()
    self.SalesReports.displa3 = self.la(width=2)

    self.endrow()
    
    RefreshDisplay(self, 'inhertidte')

    self.ReportsSumm.seperatela5 = self.la(height=1)

    self.SalesReports.spec_enrow = self.row(weights=[1,1,3,1,12])
    self.SalesReports.spect = self.la()
    self.SalesReports.option_mb = self.mb(text='Transaction ID')
    self.SalesReports.option_en = self.en(bg='white',font='Calibri,12', width=5, padx=5)
    self.SalesReports.spec_refresh = self.bu(text='Go',font='Calibri,12', padx=10, bg='#47c57f', command=Callable(RefreshSpecDisplay, self))   

    self.SalesReports.spec_sep = self.la()
    
    self.endrow()

    self.ReportsSumm.seperatela6 = self.la(height=1)

    self.SalesReports.SpecRow = self.row(weights=[0,1,0])
    self.SalesReports.spec = self.la(width=2)
    self.SalesReports.specgrid=self.gr(cols=2)
    
    self.SalesReports.specla = self.la(padx=10,text='  Item ID                                  Item Name                                                            Quantity                                 Unit Price                                 Total Price                                                               ', bg='#404040', fg='White', font=('Calibri', 11), height=1)
    self.SalesReports.specla2 = self.la()


    
    self.SalesReports.TransDisplay = self.lb(height=7,padx=10,pady=5,font=('Courier'))
    self.SalesReports.transscrollbar = self.sb(command=self.SalesReports.TransDisplay.yview)
    self.SalesReports.TransDisplay.config(yscrollcommand=self.SalesReports.transscrollbar.set)
    self.endgr()
    
    self.SalesReports.specdispla3 = self.la(width=2)

    self.endrow()

    self.SalesReports.bottomsep = self.la(height=5)
    self.endcol()

def RefreshDisplay(self, all):
    bdate = self.ReportsBar.bdate_en.get()
    edate = self.ReportsBar.edate_en.get()

    if bdate == 'ALL' and bdate == 'ALL':
        returnlist = Modules.SalesReportsDisplay.FillDisplay(self, bdate, edate, True)
    else:
        returnlist = Modules.SalesReportsDisplay.FillDisplay(self, bdate, edate, False)

    if returnlist == False:
        self.SalesReports.empty_la.config(text='There is no data to be shown for the specified date range!', font='Calibri, 12', width=2, fg='black', background='#bfbfbf')
    else:
        self.SalesReports.empty_la.config(text='', background='#d4d0c8')


def RefreshSpecDisplay(self):
    if self.SalesReports.option_en.get() != '':
        Cashlis = Cash_Read()
        sessions = Cashlis[1]

        del sessions[0]


        given_session = int(self.SalesReports.option_en.get())
        
        if str(given_session) in sessions:  
            TransID = self.SalesReports.option_en.get()
            Modules.SalesReportsDisplay.FillTransDisplay(self, TransID)
        else:
            ReportsErrorPopup.Create(6)
            ClearSpecDisplay(self)
    else:
        ReportsErrorPopup.Create(7)

def ClearSpecDisplay(self):
    self.SalesReports.TransDisplay.delete(0, 'end')
def ClearDisplay(self):
    self.SalesReports.Display.delete(0, 'end')
   

