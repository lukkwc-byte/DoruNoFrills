'''
    Version 0.01 02/11/2011 Mackenzie (Started GUI)
    Version 0.02 04/11/2011 Jonathan (Initial GUI)
    Version 0.03 07/11/2011 Jonathan (Semi-Final GUI)
    Version 0.04 08/11/2011 Jonathan (Final GUI)
    Version 0.05 17/11/2011 Jonathan (Reports >> ReportsSumm)
    Version 0.06 09/12/2011 Jonathan (Errorproofing, Deleting entries)
    


'''


from Tkinter import *
from Swampy.Gui import * # Handles Graphics
import Modules.ReportsCalc
import datetime
import ReportsErrorPopup
from Modules.ReadCSV import *

def Create(self):
    self.ReportsSumm = self.col()   
    self.ReportsSumm.seperatela = self.la(height=1)
    self.ReportsSumm.empty_la = self.la()
    self.ReportsSumm.sep2 = self.la(height=3)
    self.ReportsSumm.statusrow = self.row(weights=[0,1,0])
    self.ReportsSumm.seperatela6 = self.la(width=20)

    self.ReportsSumm.gridrow = self.row(border=3, bg='#404040')
    self.ReportsSumm.displaygrid = self.gr(cols=2)
    self.ReportsSumm.inv_la = self.la(text='Inventory Cost:', font='Calibri, 12', background='#bfbfbf')
    self.ReportsSumm.inv_en = self.en(font='Calibri, 12',justify=CENTER, readonlybackground='white', state='readonly')
    self.ReportsSumm.hr_la = self.la(text='Human Resources Cost:', font='Calibri, 12', background='#bfbfbf')
    self.ReportsSumm.hr_en = self.en(font='Calibri, 12', justify=CENTER, readonlybackground='white', state='readonly')
    self.ReportsSumm.hour_la = self.la(text='# of Hours Worked', font='Calibri, 12', background='#bfbfbf')
    self.ReportsSumm.hour_en = self.en(font='Calibri, 12', justify=CENTER, readonlybackground='white', state='readonly')
    self.ReportsSumm.trans_la = self.la(text='# of Sales Transactions:', font='Calibri, 12', background='#bfbfbf')
    self.ReportsSumm.trans_en = self.en(font='Calibri, 12', justify=CENTER, readonlybackground='white', state='readonly')
    self.ReportsSumm.rev_la = self.la(text='Total Revenue:', font='Calibri, 12', background='#bfbfbf')
    self.ReportsSumm.rev_en = self.en(font='Calibri, 12', justify=CENTER, readonlybackground='white', state='readonly')
    self.ReportsSumm.hst_la = self.la(text='Total HST Payable:', font='Calibri, 12', background='#bfbfbf')
    self.ReportsSumm.hst_en = self.en(font='Calibri, 12', justify=CENTER, readonlybackground='white', state='readonly')
    self.ReportsSumm.profit_la = self.la(text='Net Profit:', font='Calibri, 12', background='#bfbfbf')
    self.ReportsSumm.profit_en = self.en(font='Calibri, 12', justify=CENTER, readonlybackground='white', state='readonly')
    

    self.endgr()
    self.endrow()

    self.ReportsSumm.seperatela5 = self.la(width=20)                                     
    self.endrow()

    self.ReportsSumm.seperatela1 = self.la(height=7)  
    self.ReportsSumm.photo = Tkinter.PhotoImage(file='Files/Images/Logo.gif')
    self.ReportsSumm.photoLA = self.la(image=self.ReportsSumm.photo)
    self.ReportsSumm.seperatela0 = self.la(height=7)  


    self.endcol() # Main Row
    RefreshEntries(self, 'screenmove')
    
def RefreshEntries(self, all):
    bdate = self.ReportsBar.bdate_en.get()
    edate = self.ReportsBar.edate_en.get()

    if bdate == 'ALL' and edate == 'ALL':
        entrylist = Modules.ReportsCalc.CalcSummary(bdate,edate,True)
    else:
        entrylist = Modules.ReportsCalc.CalcSummary(bdate,edate,False)

    if entrylist == False:
        ClearEntries(self)
        self.ReportsSumm.empty_la.config(text='There is no data to be shown for the specified date range!', font='Calibri, 12', width=2, fg='black', background='#bfbfbf')

    else:
        self.ReportsSumm.empty_la.config(text='', background='#d4d0c8')
        self.ReportsSumm.inv_en.config(state='normal')    
        self.ReportsSumm.inv_en.delete(0, 'end')
        self.ReportsSumm.inv_en.insert('end', entrylist[0])
        self.ReportsSumm.inv_en.config(state='readonly')

        self.ReportsSumm.hr_en.config(state='normal')    
        self.ReportsSumm.hr_en.delete(0, 'end')
        self.ReportsSumm.hr_en.insert('end', entrylist[1])
        self.ReportsSumm.hr_en.config(state='readonly')

        self.ReportsSumm.hour_en.config(state='normal')    
        self.ReportsSumm.hour_en.delete(0, 'end')
        self.ReportsSumm.hour_en.insert('end', entrylist[2])
        self.ReportsSumm.hour_en.config(state='readonly')

        self.ReportsSumm.trans_en.config(state='normal')    
        self.ReportsSumm.trans_en.delete(0, 'end')
        self.ReportsSumm.trans_en.insert('end', entrylist[3])
        self.ReportsSumm.trans_en.config(state='readonly')

        self.ReportsSumm.rev_en.config(state='normal')    
        self.ReportsSumm.rev_en.delete(0, 'end')
        self.ReportsSumm.rev_en.insert('end', entrylist[4])
        self.ReportsSumm.rev_en.config(state='readonly')

        self.ReportsSumm.hst_en.config(state='normal')    
        self.ReportsSumm.hst_en.delete(0, 'end')
        self.ReportsSumm.hst_en.insert('end', entrylist[5])
        self.ReportsSumm.hst_en.config(state='readonly')

        self.ReportsSumm.profit_en.config(state='normal')    
        self.ReportsSumm.profit_en.delete(0, 'end')
        self.ReportsSumm.profit_en.insert('end', entrylist[6])
        self.ReportsSumm.profit_en.config(state='readonly')

def ClearEntries(self):
        self.ReportsSumm.empty_la.config(text='', background='#d4d0c8')
        self.ReportsSumm.inv_en.config(state='normal')    
        self.ReportsSumm.inv_en.delete(0, 'end')
        self.ReportsSumm.inv_en.config(state='readonly')

        self.ReportsSumm.hr_en.config(state='normal')    
        self.ReportsSumm.hr_en.delete(0, 'end')
        self.ReportsSumm.hr_en.config(state='readonly')

        self.ReportsSumm.hour_en.config(state='normal')    
        self.ReportsSumm.hour_en.delete(0, 'end')
        self.ReportsSumm.hour_en.config(state='readonly')

        self.ReportsSumm.trans_en.config(state='normal')    
        self.ReportsSumm.trans_en.delete(0, 'end')
        self.ReportsSumm.trans_en.config(state='readonly')

        self.ReportsSumm.rev_en.config(state='normal')    
        self.ReportsSumm.rev_en.delete(0, 'end')
        self.ReportsSumm.rev_en.config(state='readonly')

        self.ReportsSumm.hst_en.config(state='normal')    
        self.ReportsSumm.hst_en.delete(0, 'end')
        self.ReportsSumm.hst_en.config(state='readonly')

        self.ReportsSumm.profit_en.config(state='normal')    
        self.ReportsSumm.profit_en.delete(0, 'end')
        self.ReportsSumm.profit_en.config(state='readonly')    
