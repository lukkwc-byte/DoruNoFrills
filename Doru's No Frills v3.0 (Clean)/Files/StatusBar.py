''' File Log:
    Version 0.01 05/10/2011 Jonathan (Stat Bar Demo - Commented Out)
    Version 0.02 08/10/2011 Jonathan (Timer working)
    Version 0.03 11/10/2011 Jonathan (GUI fixes)
    Version 0.04 24/12/2011 Jonathan (Now includes the Logout button)
    Version 0.05 29/12/2011 Jonathan (Now includes shift status)

'''
from Tkinter import *
from Swampy.Gui import * # Handles Graphics
import Modules.Check # Window Creation/Destroy Modules.Checks
import time
import Project
import Payroll

def Create(self):
    self.statrow = self.row(border=3, bg='grey', weights=[1,0])
    self.tryrow = self.row()

    self.statrow.user = self.la(text='Logged In: '+Modules.Check.loggeduser, fg='#404040')
    self.statrow.status = self.la(text='Status: '+Modules.Check.shiftstat, fg='#404040')
    self.statrow.time = self.la(text='', fg='#404040')
    tick(self.statrow.time)
    shift_up(self.statrow.status)
    Payroll.test()
    self.statrow.version = self.la(text=Modules.Check.version, fg='#404040')
    self.endrow()
    self.statrow.logout = self.bu(text='Logout', command=Callable(Nav_Logout, self), width=15, padx=5, bg='#d94444')
    self.endrow()
    self.protocol("WM_DELETE_WINDOW", Callable(Nav_Logout, self))

def tick(self):
    time1 = ''
    # get the current local time from the PC
    time2 = time.strftime('%A, %B %d, %Y                                     %I:%M:%S %p')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        self.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky

    self.after(200, tick, self)


def shift_up(self):
    self.config(text='Status: '+Modules.Check.shiftstat, fg='#404040')
    self.after(200, shift_up, self)

def Nav_Logout(self):
    if Modules.Check.BUSY == False:
        self.destroy()
        Project.CreateProject('NoFrills')
    else:
        Modules.Check.BusyAlert(self)
