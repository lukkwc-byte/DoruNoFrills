'''
    Version 0.01 31/10/2011 Justin (started GUI)
    Version 0.02 04/11/2011 Justin (fixed spacing)
    Version 0.03 10/11/2011 Justin (fixed GUI)
    Version 0.04 10/11/2011 Jonathan (Sending date to GUI)
    Version 0.05 10/22/2011 Jonathan (GUI in finishing stages)
    


'''

from Tkinter import *
from Swampy.Gui import *
import Modules.PurchReportsDisplay
from Modules.ReadCSV import *


def Create(self):
    self.PurchReports = self.col()
    self.PurchReports.seperatela3 = self.la()
    self.PurchReports.empty_la = self.la()
    self.PurchReports.seperatela4 = self.la()
    self.PurchReports.DispRow = self.row(weights=[0,1,0])
    self.PurchReports.displa = self.la(width=2)
    self.PurchReports.displaygrid=self.gr(cols=2)
    
    self.PurchReports.toplabels = self.la(padx=10,text='  Item ID           Item Name                                      Quantity            Unit Price                          Total Price                                          Occured On (DD/MM/YYYY)                                      ', bg='#404040', fg='White', font=('Calibri', 11), height=1)
    self.PurchReports.toplabel2 = self.la()


    
    self.PurchReports.Display = self.lb(height=23,padx=10,pady=5,font=('Courier'))
    self.PurchReports.scrollbar = self.sb(command=self.PurchReports.Display.yview)
    self.PurchReports.Display.config(yscrollcommand=self.PurchReports.scrollbar.set)
    self.endgr()
    self.PurchReports.displa3 = self.la(width=2)

    self.endrow()
    
    RefreshDisplay(self, 'inhertidte')

    self.ReportsSumm.seperatela6 = self.la(height=2)

    self.endcol()

def RefreshDisplay(self, all):
    bdate = self.ReportsBar.bdate_en.get()
    edate = self.ReportsBar.edate_en.get()

    if bdate == 'ALL' and bdate == 'ALL':
        returnlist = Modules.PurchReportsDisplay.FillDisplay(self, bdate, edate, True)
    else:
        returnlist = Modules.PurchReportsDisplay.FillDisplay(self, bdate, edate, False)

    if returnlist == False:
        self.PurchReports.empty_la.config(text='There is no data to be shown for the specified date range!', font='Calibri, 12', width=2, fg='red', background='#bfbfbf')
    else:
        self.PurchReports.empty_la.config(text='', background='#d4d0c8')
