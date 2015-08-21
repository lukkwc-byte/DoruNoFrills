#### File Log ####

'''
    Version 0.01 27/09/2011 Mackenzie (Cash GUI)
    Version 0.02 27/09/2011 Ben (Display GUI)
    Version ALPHA 27/09/2011 Jonathan (Integration of Display GUI, Navigation Module, modifying GUI's)
    Version 0.04 03/10/2011 Ben (Updated display's look)
    Version 0.05 04/10/2011 Ben (Made the store price show 2 decimal places and updated the GUI)
    Version 0.06 05/10/2011 Jonathan (Folder path)
    Version 0.07 10/10/2011 Kyuho (changed csvfile variable to avoid error, redefined several variables)
    Version 0.08 26/10/2011 Jonathan (GUI Revamp - new display, working numpad. Logic revamp - session, create/destroy incl. clearing display) 
    Version 0.09 26/10/2011 Jonathan/Kyuho (Final version of session handling)
    Version 0.10 04/11/2011 Kyuho (implemented logic for remove item + remove last item)
    Version 0.11 07/11/2011 Jonathan (Cancel Transaction button)
    Version 0.12 09/11/2011 Kyuho (BUSY)
    Version 0.13 09/11/2011 Kyuho (Cancel Transaction)
'''

#### IMPORT ####

from Swampy.Gui import *
import csv
import time
from Modules.AddItemToCashRegister import *         
from Modules.RemoveItemFromCashRegister import *    
import Modules.Check
from Modules.CalculateAndStore import *
from Modules.CancelTransaction import *
from CashPopup import *
import Modules.CashDisplay
import InvErrorPopup            ### change it to CashErrorPopup later
from Modules.ReadCSV import *
from Modules.WriteCSV import *

#### GLOBAL VARIABLES ####

subtotal='$ 0.00'
tax='$ 0.00'
total='$ 0.00'

#### LOGIC FUNCTIONS ####

def cancel_trans(self):
    list1 = cancel_transaction()
    if list1 == True:
        DeleteDisplay(self)
        DeleteEntries(self)
    elif list1 == 29:
        functionname(list1)
        

def getsession(self):
    global session
    Check_List = Check_Read()
    session_number = Check_List[0]
    del session_number[0]
    session = session_number[0]
    return session

def update_session(self):
    currsess = getsession(self)
    self.CashRegister.buttons.ca1.config(text='Transaction #: '+currsess)    

def addsession(self, newsession):
    lis = ['session', newsession]
    csvfile = 'Files\Modules\Database\check.csv'
    WriteCSV([lis], csvfile)

def functionname(error_testing):
    InvErrorPopup.Create(error_testing)     ### change it to CashErrorPopup later

def add_item(self):
    global subtotal,tax, total, session
    getsession(self)
    list1 = add_into_list(self)
    list2 = cash_in_ReadItemCSV(list1)
    list3=cash_in_AddItem(list2)
    cash_in_UpdateInventory(list2)
    if list3[0] == False:
            functionname(list3[1])
    else:
        moneylist=Calculate(session)
        subtotal='$ ' + str("%.2f" % float(moneylist[0]))
        tax='$ ' + str("%.2f" % float(moneylist[1]))
        total='$ ' + str("%.2f" % float(moneylist[2]))
        Modules.Check.BUSY = True
        RefreshDisplay(self)
        RefreshEntries(self)
    
def RefreshDisplay(self):
    getsession(self)
    Modules.CashDisplay.ClearDisplay(self)
    Modules.CashDisplay.FillDisplay(self, session)

def DeleteDisplay(self):
    Modules.CashDisplay.ClearDisplay(self)


def RefreshEntries(self):
    self.CashRegister.subtotalentry.config(state='normal')    
    self.CashRegister.subtotalentry.delete(0, 'end')
    self.CashRegister.subtotalentry.insert('end', subtotal)
    self.CashRegister.subtotalentry.config(state='readonly')

    self.CashRegister.taxentry.config(state='normal')
    self.CashRegister.taxentry.delete(0, 'end')
    self.CashRegister.taxentry.insert('end', tax)
    self.CashRegister.taxentry.config(state='readonly')

    self.CashRegister.totalentry.config(state='normal')
    self.CashRegister.totalentry.delete(0, 'end')
    self.CashRegister.totalentry.insert('end', total)
    self.CashRegister.totalentry.config(state='readonly')
    

    self.CashRegister.buttons.entry_1.delete(0, 'end')
    self.CashRegister.buttons.entry_2.delete(0, 'end')
    self.CashRegister.buttons.paidentry.delete(0, 'end')

def DeleteEntries(self):
    self.CashRegister.subtotalentry.config(state='normal')    
    self.CashRegister.subtotalentry.delete(0, 'end')
    self.CashRegister.subtotalentry.config(state='readonly')

    self.CashRegister.taxentry.config(state='normal')
    self.CashRegister.taxentry.delete(0, 'end')
    self.CashRegister.taxentry.config(state='readonly')

    self.CashRegister.totalentry.config(state='normal')
    self.CashRegister.totalentry.delete(0, 'end')
    self.CashRegister.totalentry.config(state='readonly')
    
    self.CashRegister.buttons.entry_1.delete(0, 'end')
    self.CashRegister.buttons.entry_2.delete(0, 'end')
    self.CashRegister.buttons.paidentry.delete(0, 'end')
        
def remove_item(self):
    global subtotal,tax, total, session
    getsession(self)
    list1 = add_into_list(self)
    list2 = cash_out_ReadItemCSV(list1)
    list3 = cash_out_RemoveItem(list2)
    cash_out_UpdateInventory(list2)
    if list3[0] == False:
        functionname(list3[1])
    else:
        moneylist=Calculate(session)
        subtotal='$ ' + str("%.2f" % float(moneylist[0]))
        tax='$ ' + str("%.2f" % float(moneylist[1]))
        total='$ ' + str("%.2f" % float(moneylist[2]))
        RefreshDisplay(self)
        RefreshEntries(self)

def last_button(self):
    global subtotal,tax, total, session
    list1 = cash_out_DeletePreviousItem(session)
    list2 = cash_out_RemoveItem(list1)
    cash_out_UpdateInventory(list1)
    if list2[0] == False:
        functionname(list2[1])
    else:
        moneylist=Calculate(session)
        subtotal='$ ' +  str("%.2f" % float(moneylist[0]))
        tax= '$ ' + str("%.2f" % float(moneylist[1]))
        total='$ ' + str("%.2f" % float(moneylist[2]))
        RefreshDisplay(self)
        RefreshEntries(self)
    
def cash_pay(self):
    global session
    validity = 0
    number_list = '0123456789.'
    getsession(self)
    moneylist=Calculate(session)
    subtotal='$ ' + str("%.2f" % float(moneylist[0]))
    tax='$ ' +  str("%.2f" % float(moneylist[1]))
    total='$ ' + str("%.2f" % float(moneylist[2]))
    paid=self.CashRegister.paidentry.get()

    if total == '$ 0.00':
        validity = 27
        functionname(validity)
    else:
        if paid == '':
            validity = 26
            functionname(validity)
        else:
            for i in range(len(paid)):
                if paid[i] not in number_list:
                    validity = 19
                    break
            check_count = 0
            for i in range(len(paid)):
                if paid[i] == '.':
                    check_count += 1
            if check_count != 0 and check_count > 1:
                validity = 20

            if validity != 0:
                functionname(validity)
            else:
                ind_find = 0
                for i in range(len(paid)):
                    if paid[i] == '.':
                        ind_find = i
                        break
                decimal_place = paid[ind_find+1:]
                if ind_find != 0 and len(decimal_place) > 2:
                    validity = 22
                    functionname(validity)
                else:
                    if float(paid) < float("%.2f" % float(moneylist[2])):
                        validity = 21
                        functionname(validity)
                    else:
                        finallis=CalculateFinal(moneylist,paid)
                        paidsend='$ ' + str("%.2f" % float(paid))
                        newsession = str(int(session)+1)
                        addsession(self,newsession)
                        Modules.Check.BUSY = False
                        CreatePopUp(self, paidsend, finallis[3], session)


def add_into_list(self):
    new_list = []
    Item_Number = self.CashRegister.buttons.entry_1.get()
    New_Item_Number=Item_Number[0:8]
    new_list.append(New_Item_Number)
    Quantity = self.CashRegister.buttons.entry_2.get()
    new_list.append(Quantity)
    Item_Session = str(session)
    new_list.append(Item_Session)
    return new_list

def Pay(self, num):
    if num == 'clear':
        self.CashRegister.paidentry.delete(0, 'end')
    else:
        self.CashRegister.paidentry.insert('end', num)

#### GUI CREATE ####

def Create(self):
    self.CashRegister = self.row(weights=[1,0])
    self.CashRegister.buttons = self.col()
    self.CashRegister.buttons.ca1 = self.la(text='Transaction Number:', background='#bfbfbf', padx=10, pady=2,  font='Calibri, 14')
    self.row(pady=1)
    self.endrow()
    self.CashRegister.buttons.grid1 = self.gr(cols=2) #  Entry Grid
    self.CashRegister.buttons.label_2 = self.la(text='Item Number:', padx=10, pady=2,  font='Calibri, 14')
    self.CashRegister.buttons.entry_1 = self.en(bg= 'white',padx=10, pady=2, font='Calibri, 14', highlightthickness = 2, highlightcolor = '#4f81bd')
    self.CashRegister.buttons.label_4 = self.la(text='Quantity:', padx=10, pady=2, font='Calibri, 14')
    self.CashRegister.buttons.entry_2 = self.en(bg= 'white', padx=10, pady=2, font='Calibri, 14', highlightthickness = 2, highlightcolor = '#4f81bd')    
    self.endgr()
    self.CashRegister.row1=self.row()
    self.CashRegister.additembutton=self.bu('Add Item', font='Calibri, 14',pady=15, padx=10, bg='#47c57f', command = Callable(add_item, self))    
    self.endrow()
    self.CashRegister.row2=self.row()
    self.CashRegister.deleteitembutton=self.bu('      Delete Item      ',font='Calibri, 14',padx=8, bg='#d94444', command = Callable(remove_item, self))
    self.CashRegister.removepreviousitembutton=self.bu('Remove Last Item', font='Calibri, 14', padx=8, bg='#4f81bd',  command = Callable(last_button, self))
    self.endrow()
    self.row()
    self.CashRegister.labelline=self.la(text='___________________________________________', font=('Calibri', '14'), justify='center', pady=8)
    self.endrow()
    self.CashRegister.grid1=self.gr(cols=2)
    self.CashRegister.paidlabel=self.la(text='Amount Paid:', padx=10, pady=12, font='Calibri, 14')
    self.CashRegister.paidentry=self.en(bg= 'white',padx=10, pady=16, font='Calibri, 14', highlightthickness = 2, highlightcolor = '#4f81bd')
    self.endgr()
    
    self.CashRegister.grid3=self.gr(cols=3, padx = 35, pady = 22)
    self.CashRegister.buttonseven=self.bu('7',font='Calibri,14', background='lightgray', command=Callable(Pay, self, '7'))
    self.CashRegister.buttoneight=self.bu('8',font='Calibri,14', background='lightgray', command=Callable(Pay, self, '8'))
    self.CashRegister.buttonnine=self.bu('9',font='Calibri,14', background='lightgray', command=Callable(Pay, self, '9'))
    self.CashRegister.buttonfour=self.bu('4',font='Calibri,14', background='lightgray', command=Callable(Pay, self, '4'))
    self.CashRegister.buttonfive=self.bu('5',font='Calibri,14', background='lightgray', command=Callable(Pay, self, '5'))
    self.CashRegister.buttonsix=self.bu('6',font='Calibri,14', background='lightgray', command=Callable(Pay, self, '6'))
    self.CashRegister.buttonthree=self.bu('1',font='Calibri,14', background='lightgray', command=Callable(Pay, self, '1'))
    self.CashRegister.buttontwo=self.bu('2',font='Calibri,14', background='lightgray', command=Callable(Pay, self, '2'))
    self.CashRegister.buttonone=self.bu('3',font='Calibri,14', background='lightgray', command=Callable(Pay, self, '3'))
    self.CashRegister.buttonzero=self.bu('0',font='Calibri,14', background='lightgray', command=Callable(Pay, self, '0'))
    self.CashRegister.buttondot=self.bu('.',font='Calibri,14', background='lightgray', command=Callable(Pay, self, '.'))
    self.CashRegister.buttonenter=self.bu('Clear',width=1,background='lightgray', font='Calibri,14', command=Callable(Pay, self, 'clear'))
    self.endgr()
    
    self.CashRegister.row4 = self.row()
    self.CashRegister.buttonpay=self.bu('Pay', bg='#47c57f', width=3, padx=8, pady=12, font='Calibri, 14', command = Callable(cash_pay, self))
    self.CashRegister.canceltrans=self.bu('Cancel Transaction', bg='#E56717', width=3, padx=8, pady=12, font='Calibri, 14', command = Callable(cancel_trans, self))

    self.endrow()

    self.endcol()
    self.col(weights=[1,0])
    
    self.CashRegister.Display = self.gr(cols=2)
    self.CashRegister.toplabels = self.la(text='Item #              Item Name                                     Qty.           Unit Price                                  Total                                       ', bg='#404040', fg='White', font=('Calibri', 11), height=1)
    self.CashRegister.toplabel2 = self.la()
    
    self.CashRegister.Display = self.lb(height=29, width = 55,font=('Courier'))
    self.CashRegister.scrollbar = self.sb(command=self.CashRegister.Display.yview)
    self.CashRegister.Display.config(yscrollcommand=self.CashRegister.scrollbar.set)
    self.endgr()

    self.gr(cols=2)
    self.CashRegister.subtotal=self.la(text='Subtotal', font='Calibri, 12', width=12)
    self.CashRegister.subtotalentry=self.en(font='Calibri, 12', width=5, justify=CENTER, readonlybackground='white')
    self.CashRegister.subtotalentry.config(state='readonly')
    self.CashRegister.tax=self.la(text='Tax',font='Calibri, 12', width=12)
    self.CashRegister.taxentry=self.en(font='Calibri, 12', width=5, justify=CENTER, readonlybackground='white')
    self.CashRegister.taxentry.config(state='readonly')
    self.CashRegister.total=self.la(text='Total', font='Calibri, 12', width=12)
    self.CashRegister.totalentry=self.en(font='Calibri, 12', width=5, justify=CENTER, readonlybackground='white')
    self.CashRegister.totalentry.config(state='readonly')

    self.endgr() #Grid for Display
    self.endcol()
    self.endgr()
    
    update_session(self)
