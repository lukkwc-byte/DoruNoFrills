'''
    Version 0.01 19/10/2011 Justin (Payroll GUI) 
    Version 0.02 27/10/2011 Mackenzie (fully integrated with PayrollLog)

'''

from Swampy.Gui import *
import time
from Modules.PayrollLog import *
from Modules.Check import * 


from Modules.ReadCSV import *
import Modules.Check
from Modules.WriteCSV import *

time1 = ''
    
def checkin(self):

    time3 = time.strftime(' %I:%M:%S %p')
    self.Payroll.checkin.config(relief='ridge',state='disabled', cursor='X_cursor')
    self.Payroll.checkout.config(relief='raised',state='normal', cursor='circle')
    self.Payroll.statuslabel.config(text='Status: Checked In at'+time3)
    #place where check in stuff will go.
    Check_in()
    Modules.Check.shiftstat = 'Checked In'
    return

def checkout(self):

    time4 = time.strftime(' %I:%M:%S %p')
    self.Payroll.checkin.config(relief='raised',state='normal', cursor='circle')
    self.Payroll.checkout.config(relief='ridge',state='disabled', cursor='X_cursor')
    self.Payroll.statuslabel.config(text=('Status: Checked Out at'+time4))
    #place where check out stuff will go
    Check_out()
    Modules.Check.shiftstat = 'Checked Out'
    return

def Create(self):
    
    check = test()
    if check == 1:
        self.Payroll = self.col()
        self.Payroll.label5 = self.la()
        self.row(pady=18)
        self.endrow()
        self.Payroll.timelabel = self.la(text='Time', font=('Calibri', '28', 'bold'), justify='center', sticky=N)
        self.Payroll.grid1=self.gr(cols=1)
        
        self.row(pady=5)
        self.endrow()
        self.statrow.time = self.la(text='', width=3, font=('Calibri', '30'))
        tick2(self.statrow.time)
        
        self.endgr()
        self.Payroll.grid2=self.gr(cols=2)
        self.Payroll.checkin = self.bu(text='Check In', pady=60, padx=30, font=('Calibri', '18'), bg='#47c57f', bd=10, relief='raised', activebackground='#A6C332', state='normal', disabledforeground='black', cursor='circle')
        self.Payroll.checkin.config(command=Callable(checkin, self))
        
        self.Payroll.checkout = self.bu(text='Check Out', pady=60, padx=30, font=('Calibri', '18'), bg='#d94444', bd=10, relief='ridge', activebackground='#D2732E', state='disabled', disabledforeground='black', cursor='X_cursor', command=Callable(checkout,self))
        self.endgr()
        self.Payroll.statuslabel = self.la(text='Status: Checked Out', font=('Calibri', '24', 'bold'), justify='center')
        
        self.Payroll.label5 = self.la()
        self.Payroll.label5 = self.la()
        self.Payroll.label5 = self.la()
        self.Payroll.label5 = self.la()
        self.Payroll.label5 = self.la()


        #self.Payroll.photolabel = self.la(text='Ben\'s photo goes here', font=('Impact', '85', 'bold'))
        self.Payroll.photo = Tkinter.PhotoImage(file='Files/Images/SmallLogo.gif')
        self.Payroll.photoLA = self.la(image=self.Payroll.photo)
        self.Payroll.label2 = self.la(text='Copywright (c) Doru Solutions 2011')

        self.Payroll.label5 = self.la()
        self.Payroll.label5 = self.la()
        self.Payroll.label5 = self.la()
        self.Payroll.label5 = self.la()
        self.Payroll.label5 = self.la()
        

        
        self.endcol()
    else:
        self.Payroll = self.col()
        self.Payroll.label5 = self.la()
        self.row(pady=18)
        self.endrow()
        self.Payroll.timelabel = self.la(text='Time:', font=('Calibri', '28', 'bold'), justify='center', sticky=N)
        self.Payroll.grid1=self.gr(cols=1)
        
        self.row(pady=5)
        self.endrow()
        self.statrow.time = self.la(text='', width=3, font=('Calibri', '30'))
        tick2(self.statrow.time)
        
        self.endgr()
        self.Payroll.grid2=self.gr(cols=2)
        self.Payroll.checkin = self.bu(text='Check In', pady=60, padx=30, font=('Calibri', '18'), bg='#47c57f', bd=10, relief='ridge', activebackground='#A6C332', state='disabled', disabledforeground='black', cursor='X_cursor')
        self.Payroll.checkin.config(command=Callable(checkin, self))
        
        self.Payroll.checkout = self.bu(text='Check Out', pady=60, padx=30, font=('Calibri', '18'), bg='#d94444', bd=10, relief='raised',activebackground='#D2732E', state='normal', disabledforeground='black', cursor='circle', command=Callable(checkout,self))
        self.endgr()
        checkhours = int(check[0:2])
        if checkhours > 12:
            checkhour = str(checkhours - 12)
            check = str(check)
            check= checkhour+check[2:]+' PM'
            check ='Status: Checked in at '+check
        else:
            check= str(checkhours)+str(check[2:])+' AM'
        self.Payroll.statuslabel = self.la(text=check, font=('Calibri', '24', 'bold'), justify='center')
        self.Payroll.label5 = self.la()
        self.Payroll.label5 = self.la()
        self.Payroll.label5 = self.la()
        self.Payroll.label5 = self.la()
        self.Payroll.label5 = self.la()
        



        #self.Payroll.photolabel = self.la(text='Ben\'s photo goes here', font=('Impact', '85', 'bold'))
        self.Payroll.photo = Tkinter.PhotoImage(file='Files/Images/SmallLogo.gif')
        self.Payroll.photoLA = self.la(image=self.Payroll.photo)
        self.Payroll.label2 = self.la(text='Copywright (c) Doru Solutions 2011')

        self.Payroll.label5 = self.la()
        self.Payroll.label5 = self.la()
        self.Payroll.label5 = self.la()
        self.Payroll.label5 = self.la()
        self.Payroll.label5 = self.la()
        

        
        self.endcol()
def tick2(self):
    
    global time1
    # get the current local time from the PC
    time2 = time.strftime(' %I:%M:%S %p')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        self.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    self.after(200, tick2, self)
    
def test():
    user = Check.loggeduser
    
    Payrolllist3 = Payroll_Read()
    employeelist = Payrolllist3[0]
    datelist = Payrolllist3[1]
    shiftlist = Payrolllist3[2]
    check_inlist = Payrolllist3[3]
    check_outlist = Payrolllist3[4]
    hourly_wagelist = Payrolllist3[5]
    shift_idlist= Payrolllist3[6]
    approval_list = Payrolllist3[7]

    applicable=[]
    number=0

    for i in employeelist:
        if i == user:     
            applicable.append(number)
        number += 1
    if applicable == []:
        Modules.Check.shiftstat = 'Checked Out'
        return 1
    if applicable != []:
    
        last=int(applicable[-1])
        if check_outlist[last] == 'None':
            from datetime import datetime
            datetime = str(datetime.now())
            currentdate=datetime[:10]
            olddate = datelist[last]
            if olddate != currentdate:
                Modules.Check.shiftstat = 'Checked out'
                del employeelist[last]
                del datelist[last]
                del shiftlist[last]
                del check_inlist[last]
                del check_outlist[last]
                del hourly_wagelist[last]
                del shift_idlist[last]
                del approval_list[last]

                all = [employeelist, datelist, shiftlist, check_inlist, check_outlist, hourly_wagelist, shift_idlist, approval_list]
        
                csvfile = 'Files\Modules\Database\PayrollDB.csv'
                WriteCSV(all, csvfile)
                return 1 
            if olddate == currentdate:
                Modules.Check.shiftstat = 'Checked In'
                
                return check_inlist[last]
        if check_outlist[last] != 'None':      
    
            Modules.Check.shiftstat = 'Checked Out'
            return 1


