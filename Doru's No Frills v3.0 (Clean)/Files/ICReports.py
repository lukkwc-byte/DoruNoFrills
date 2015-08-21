'''
    Version 0.01 02/11/2011 Mackenzie (Started GUI)
    Version 0.02 04/11/2011 Jonathan (Initial GUI)
    Version 0.03 07/11/2011 Jonathan (Semi-Final GUI)
    Version 0.04 08/11/2011 Jonathan (Final GUI)
    Version 0.05 17/11/2011 Jonathan (Reports >> ICReports)
    


'''


from Tkinter import *
from Swampy.Gui import * # Handles Graphics
import Modules.ReportsCalc
import datetime

def Create(self):
    self.ICReports = self.col()   
    self.ICReports.seperatela = self.la(height=5)

    self.ICReports.statusrow = self.row(weights=[0,1,0])
    self.ICReports.seperatela6 = self.la(width=20)
    self.ICReports.gridrow = self.row(border=3, bg='#404040')
    self.ICReports.displaygrid = self.gr(cols=2)
    self.ICReports.inv_la = self.la(text='Inventory Cost:', font='Calibri, 12', background='#bfbfbf')
    self.ICReports.inv_en = self.en(font='Calibri, 12',justify=CENTER, readonlybackground='white', state='readonly')
    self.ICReports.hr_la = self.la(text='Human Resources Cost:', font='Calibri, 12', background='#bfbfbf')
    self.ICReports.hr_en = self.en(font='Calibri, 12', justify=CENTER, readonlybackground='white', state='readonly')
    self.ICReports.hour_la = self.la(text='# of Hours Worked', font='Calibri, 12', background='#bfbfbf')
    self.ICReports.hour_en = self.en(font='Calibri, 12', justify=CENTER, readonlybackground='white', state='readonly')
    self.ICReports.trans_la = self.la(text='# of Sales Transactions:', font='Calibri, 12', background='#bfbfbf')
    self.ICReports.trans_en = self.en(font='Calibri, 12', justify=CENTER, readonlybackground='white', state='readonly')
    self.ICReports.rev_la = self.la(text='Total Revenue:', font='Calibri, 12', background='#bfbfbf')
    self.ICReports.rev_en = self.en(font='Calibri, 12', justify=CENTER, readonlybackground='white', state='readonly')
    self.ICReports.hst_la = self.la(text='Total HST Payable:', font='Calibri, 12', background='#bfbfbf')
    self.ICReports.hst_en = self.en(font='Calibri, 12', justify=CENTER, readonlybackground='white', state='readonly')
    self.ICReports.profit_la = self.la(text='Net Profit:', font='Calibri, 12', background='#bfbfbf')
    self.ICReports.profit_en = self.en(font='Calibri, 12', justify=CENTER, readonlybackground='white', state='readonly')
    

    self.endgr()
    self.endrow()

    self.ICReports.seperatela5 = self.la(width=20)                                     
    self.endrow()

    RefreshEntries(self, 'screenmove')

    self.ICReports.seperatela1 = self.la(height=7)  
    self.ICReports.photo = Tkinter.PhotoImage(file='Files/Images/Logo.gif')
    self.ICReports.photoLA = self.la(image=self.ICReports.photo)
    self.ICReports.seperatela0 = self.la(height=7)  


    self.endcol() # Main Row

def RefreshEntries(self, all):
    bdate = self.ReportsBar.bdate_en.get()
    edate = self.ReportsBar.edate_en.get()

    if bdate == 'ALL' and edate == 'ALL':
        entrylist = Modules.ReportsCalc.CalcSummary(bdate,edate,True)
    else:
        entrylist = Modules.ReportsCalc.CalcSummary(bdate,edate,False)
        
    self.ICReports.inv_en.config(state='normal')    
    self.ICReports.inv_en.delete(0, 'end')
    self.ICReports.inv_en.insert('end', entrylist[0])
    self.ICReports.inv_en.config(state='readonly')

    self.ICReports.hr_en.config(state='normal')    
    self.ICReports.hr_en.delete(0, 'end')
    self.ICReports.hr_en.insert('end', entrylist[1])
    self.ICReports.hr_en.config(state='readonly')

    self.ICReports.hour_en.config(state='normal')    
    self.ICReports.hour_en.delete(0, 'end')
    self.ICReports.hour_en.insert('end', entrylist[2])
    self.ICReports.hour_en.config(state='readonly')

    self.ICReports.trans_en.config(state='normal')    
    self.ICReports.trans_en.delete(0, 'end')
    self.ICReports.trans_en.insert('end', entrylist[3])
    self.ICReports.trans_en.config(state='readonly')

    self.ICReports.rev_en.config(state='normal')    
    self.ICReports.rev_en.delete(0, 'end')
    self.ICReports.rev_en.insert('end', entrylist[4])
    self.ICReports.rev_en.config(state='readonly')

    self.ICReports.hst_en.config(state='normal')    
    self.ICReports.hst_en.delete(0, 'end')
    self.ICReports.hst_en.insert('end', entrylist[5])
    self.ICReports.hst_en.config(state='readonly')

    self.ICReports.profit_en.config(state='normal')    
    self.ICReports.profit_en.delete(0, 'end')
    self.ICReports.profit_en.insert('end', entrylist[6])
    self.ICReports.profit_en.config(state='readonly')
