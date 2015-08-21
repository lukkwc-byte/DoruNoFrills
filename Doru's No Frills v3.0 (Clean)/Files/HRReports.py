'''
    Version 0.01 31/10/2011 Justin (started GUI)
    Version 0.02 04/11/2011 Justin (fixed spacing)
    Version 0.03 10/11/2011 Justin (fixed GUI)
    Version 0.04 10/11/2011 Jonathan (Sending date to GUI)
    Version 0.05 10/22/2011 Jonathan (GUI in finishing stages)
    Version 0.06 10/24/2011 Jonathan (GUI for Employee Totals)
    


'''

from Tkinter import *
from Swampy.Gui import *
import Modules.HRReportsDisplay
import ReportsErrorPopup
import csv
from Modules.ReadCSV import *


def Create(self):
    self.HRReports = self.col()
    self.HRReports.seperatela3 = self.la(height=1)
    self.HRReports.empty_la = self.la()
    self.HRReports.sep2 = self.la(height=1)
    self.HRReports.DispRow = self.row(weights=[0,1,0])
    self.HRReports.displa = self.la(width=2)
    self.HRReports.displaygrid=self.gr(cols=2)
    
    self.HRReports.toplabels = self.la(padx=10,text='  Employee                                       Shift ID                         Date                                     Time Worked                         Hourly Wage           Paid                                                                          ', bg='#404040', fg='White', font=('Calibri', 11), height=1)
    self.HRReports.toplabel2 = self.la()


    
    self.HRReports.Display = self.lb(height=15,padx=10,pady=5,font=('Courier'))
    self.HRReports.scrollbar = self.sb(command=self.HRReports.Display.yview)
    self.HRReports.Display.config(yscrollcommand=self.HRReports.scrollbar.set)
    self.endgr()
    self.HRReports.displa3 = self.la(width=2)

    self.endrow()
    
    self.HRReports.title = self.la(padx=150, font=('Arial', '16', 'bold','underline'), disabledforeground='black', text='Employee Totals', justify=CENTER, pady=3)
    self.HRReports.title.config(state='disabled')
    self.ReportsSumm.seperatela8 = self.la()
    self.HRReports.spec_enrow = self.row(weights=[1,1,3,1,12])
    self.HRReports.spect = self.la()
    self.HRReports.option_title = self.la(text='Employee Name:', font='Calibri,12')
 

    self.HRReports.option_en = self.en(bg='white',font='Calibri,12', width=5, padx=5)

    self.HRReports.spec_refresh = self.bu(text='Go',font='Calibri,12', padx=10, bg='#47c57f', command=Callable(RefreshSpecDisplay, self))   

    self.HRReports.empty_la2 = self.la()
    
    self.endrow()

    self.ReportsSumm.seperatela6 = self.la(height=1)

    self.HRReports.SpecLaRow = self.row()
    self.HRReports.specla1 = self.la()
    self.HRReports.speclar1 = self.en(text='# Of Shifts', justify=CENTER, bd=0, disabledbackground='#404040', disabledforeground='white')
    self.HRReports.speclar2 = self.en(text='Time Worked', justify=CENTER, bd=0, disabledbackground='#404040', disabledforeground='white')
    self.HRReports.speclar4 = self.en(text='Total Pay', justify=CENTER, bd=0, disabledbackground='#404040', disabledforeground='white')
    self.HRReports.speclar5 = self.en(text='# Of Transactions', justify=CENTER, bd=0, disabledbackground='#404040', disabledforeground='white')
    self.HRReports.speclar1.config(state='disabled')
    self.HRReports.speclar2.config(state='disabled')
    self.HRReports.speclar4.config(state='disabled')
    self.HRReports.speclar5.config(state='disabled')
    self.HRReports.specla2 = self.la()
    self.endrow()

    self.HRReports.SpecRow = self.row()
    self.HRReports.specla1 = self.la()
    self.HRReports.spec1 = self.en(justify=CENTER, state='readonly', readonlybackground='white')
    self.HRReports.spec2 = self.en(justify=CENTER, state='readonly', readonlybackground='white')
    self.HRReports.spec4 = self.en(justify=CENTER, state='readonly', readonlybackground='white')
    self.HRReports.spec5 = self.en(justify=CENTER, state='readonly', readonlybackground='white')
    self.HRReports.specla2 = self.la()
    self.endrow()

    self.HRReports.bottomsep = self.la(height=5)
    self.endcol()

    RefreshDisplay(self, 'inhertidte')

def RefreshDisplay(self, all):
    bdate = self.ReportsBar.bdate_en.get()
    edate = self.ReportsBar.edate_en.get()

    if bdate == 'ALL' and bdate == 'ALL':
        returnlist = Modules.HRReportsDisplay.FillDisplay(self, bdate, edate, True)
    else:
        returnlist = Modules.HRReportsDisplay.FillDisplay(self, bdate, edate, False)

    ClearSpecDisplay(self)
    if returnlist == False:
        self.HRReports.empty_la.config(text='There is no data to be shown for the specified date range!', font='Calibri, 12', width=2, fg='red', background='#bfbfbf')
    else:
        self.HRReports.empty_la.config(text='', background='#d4d0c8')
        
def RefreshSpecDisplay(self):
    bdate = self.ReportsBar.bdate_en.get()
    edate = self.ReportsBar.edate_en.get()
    
    Emplis = Account_Read()

    employees = Emplis[0]

    del employees[0]
    
    given_employee = self.HRReports.option_en.get()
    if given_employee in employees:  
        if bdate == 'ALL' and bdate == 'ALL':
            returnlist = Modules.HRReportsDisplay.FillSpecDisplay(self, bdate, edate, True)
        else:
            returnlist = Modules.HRReportsDisplay.FillSpecDisplay(self, bdate, edate, False)
        if returnlist == False:
            self.HRReports.empty_la2.config(text='There is no data for this employee during the specified dates!', font='Calibri, 12', width=2, fg='red', background='#bfbfbf')
        else:
            self.HRReports.empty_la2.config(text='', background='#d4d0c8')

    else:
        ReportsErrorPopup.Create(3)
        ClearSpecDisplay(self)
    
def ClearDisplay(self):
    self.HRReports.spec1.config(state='normal')
    self.HRReports.spec2.config(state='normal')
    self.HRReports.spec4.config(state='normal')
    self.HRReports.spec5.config(state='normal')
    
    self.HRReports.spec1.delete(0, 'end')
    self.HRReports.spec2.delete(0, 'end')
    self.HRReports.spec4.delete(0, 'end')
    self.HRReports.spec5.delete(0, 'end')
    
    self.HRReports.Display.delete(0, 'end')

    self.HRReports.spec1.config(state='readonly')
    self.HRReports.spec2.config(state='readonly')
    self.HRReports.spec4.config(state='readonly')
    self.HRReports.spec5.config(state='readonly')
    

def ClearSpecDisplay(self):
    self.HRReports.spec1.config(state='normal')
    self.HRReports.spec2.config(state='normal')
    self.HRReports.spec4.config(state='normal')
    self.HRReports.spec5.config(state='normal')
    
    self.HRReports.spec1.delete(0, 'end')
    self.HRReports.spec2.delete(0, 'end')
    self.HRReports.spec4.delete(0, 'end')
    self.HRReports.spec5.delete(0, 'end')

    self.HRReports.spec1.config(state='readonly')
    self.HRReports.spec2.config(state='readonly')
    self.HRReports.spec4.config(state='readonly')
    self.HRReports.spec5.config(state='readonly')
    
    self.HRReports.empty_la2.config(text='', background='#d4d0c8')
   
