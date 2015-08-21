'''
    Version 0.01 27/09/2011 Michael (Inventory GUI)
    Version 0.02 27/09/2011 Kyuho (Add Item Logic)
    Version 0.03 27/09/2011 Ben (Display GUI)
    Version ALPHA 27/09/2011 Jonathan (Integration into Navigation module, modifying GUI's + importing Display)
    Version 0.05 03/10/2011 Justin ('Remove Item Logic' button)
    Version 0.06 03/10/2011 Ben (Implemented Justin's Code and started Scrollbar)
    Version 0.07 04/10/2011 Ben (Made Store and Supplier Price show 2 decimal places and updated the GUI)
    Version 0.08 10/10/2011 Michael (Created the Clear and Backspace functions and binded them to keys)
    Version 0.09 10/10/2011 Jonathan (Removed error)
    Version 0.10 19/10/2011 Jonathan (Complete GUI Revamp, New Display)
    Version 0.11 20/10/2011 Kevin, Kyuho, Michael (Errorproofing)
    Version 0.12 21/10/2011 Kyuho+Michael (checking for possible errors)
    Version 0.13 24/10/2011 Kyuho+Michael (implementing validity 17)
    Version 0.14 26/10/2011 Kyuho+Michael (implementing validity 16)
    Version 0.15 27/10/2011 Kyuho (error proofing)
    Version 0.16 01/11/2011 Jonathan (GUI Improvements)
    Version 0.17 02/11/2011 Kyuho (inventory save transaction)
    Version 0.18 03/11/2011 Jonathan (Label change)
    Version 0.19 23/11/2011 Jonathan (Spacing fix)
    Version 0.20 14/12/2011 Jonathan (Inventory Printing)
'''
#Need to add in an Edit button, have it congif the Add and Edit buttons into Save and Cancel and back

from Swampy.Gui import *
from Modules.AddItemToInventory import *
from Modules.RemoveItemFromInventory import *
from Modules.AddCSVToInventory import *
import InvErrorPopup
import Modules.InventoryDisplay
import tkMessageBox
import Modules.PrintInv

def add_item(self):
    list1 = add_into_list(self)
    list2 = inv_in_ReadItemCSV(list1) # Kyuho
    inv_SaveTransaction(list2, list1)
    list3 = inv_AddItem(list2)
    if list3[0] == False:
        functionname(list3[1])
        return False
    else:                              # Kyuho
        self.InvManage.buttons.entry_1.config(state='normal')
        self.InvManage.buttons.entry_2.config(state='normal')
        self.InvManage.buttons.entry_3.config(state='normal')
        RefreshDisplay(self)
        RefreshEntries(self)
        return True

def edit_item(self):
    lis1 = add_into_list(self)
    lis2 = edit_item_inv(lis1)
    if lis2 != None:
        functionname(lis2[0])
    else:
        self.InvManage.buttons.entry_1.config(state='normal')
        self.InvManage.buttons.entry_2.config(state='normal')
        self.InvManage.buttons.entry_3.config(state='normal')
        RefreshDisplay(self)
        RefreshEntries(self)
        edit_back(self)  


        
def edit_switch(self):
    try:
        RefreshEntries(self)
        ai = int(self.InvManage.Display.curselection()[0])
        invlist = Inv_Read()
        self.InvManage.buttons.entry_1.insert('end', invlist[0][ai+1])
        self.InvManage.buttons.entry_2.insert('end', invlist[1][ai+1])
        self.InvManage.buttons.entry_3.insert('end', invlist[2][ai+1])
        self.InvManage.buttons.entry_4.insert('end', invlist[3][ai+1])
        self.InvManage.buttons.entry_5.insert('end', invlist[4][ai+1])
        self.InvManage.buttons.entry_1.config(state='readonly')
        self.InvManage.buttons.entry_2.config(state='readonly')
        self.InvManage.buttons.entry_3.config(state='readonly')
        Modules.Check.editinv = invlist[0][ai+1]  
        self.InvManage.buttons.button_add_item.config(text='  Save  ', command=Callable(edit_item, self))
        self.InvManage.buttons.button_edit_item.config(text=' Cancel  ', command = Callable(edit_back, self))
        self.InvManage.buttons.button_remove_item.config(state='disabled')
        self.InvManage.buttons.button_accept_csv.config(state='disabled')
        self.InvManage.buttons.printinv.config(state='disabled')   
    except:
        functionname(50)        

def edit_back(self):
    self.InvManage.buttons.button_add_item.config(text='Add Item', command=Callable(add_item, self))
    self.InvManage.buttons.button_edit_item.config(text='Edit Item', command = Callable(edit_switch, self))
    self.InvManage.buttons.entry_1.config(state='normal')
    self.InvManage.buttons.entry_2.config(state='normal')
    self.InvManage.buttons.entry_3.config(state='normal')

    RefreshEntries(self)
    self.InvManage.buttons.button_remove_item.config(state='normal',bg = '#d94444')
    self.InvManage.buttons.button_accept_csv.config(state='normal',bg= '#4f81bd')
    self.InvManage.buttons.printinv.config(state='normal', bg= '#9F5F9F')

def functionname(error_testing):
    InvErrorPopup.Create(error_testing)
        
def remove_item(self):
    if add_into_list(self) != ['', '', '', '', '']: #click remove
        list1 = add_into_list(self)
        list2 = inv_out_ReadItemCSV(list1)
        list3 = Remove_Item(list2)
        if list3[0] == False:
           functionname(list3[1])
        else:
            RefreshDisplay(self)
            RefreshEntries(self)
    else:
        try:
            ai = int(self.InvManage.Display.curselection()[0])
            invlist = Inv_Read()
            list1 = [invlist[0][ai+1],invlist[1][ai+1],invlist[2][ai+1],invlist[3][ai+1],invlist[4][ai+1]]
            list2 = inv_out_ReadItemCSV(list1)
            list3 = Remove_Item(list2)
            if list3[0] == False:
                functionname(list3[1])
            else:
                RefreshDisplay(self)
                RefreshEntries(self)
        except: 
            functionname(50)
    
def add_into_list(self):
    new_list=[]
    Item_Number=self.InvManage.buttons.entry_1.get()
    new_list.append(Item_Number)
    Item_Name=self.InvManage.buttons.entry_2.get()
    new_list.append(Item_Name)
    Quantity=self.InvManage.buttons.entry_3.get()
    new_list.append(Quantity)
    Supplier_Price=self.InvManage.buttons.entry_4.get()
    new_list.append(Supplier_Price)
    Store_Price=self.InvManage.buttons.entry_5.get()
    new_list.append(Store_Price)
    return(new_list)

def add_csv(self):                               # this is how you add csv
    CSV_Name = self.InvManage.buttons.entry_6.get()
    list1 = inv_ImportCSV(CSV_Name)

    if list1 != None:
        functionname(list1[0])
    else:
        RefreshDisplay(self)
        RefreshEntries(self)

def print_inv(self):
    returncheck = Modules.PrintInv.Create()
    if returncheck == False:
        InvErrorPopup.Create(31)
    if returncheck == True:
        tkMessageBox.showwarning("Success", 'The inventory has been printed to Inventory List.csv')

        

def RefreshDisplay(self):
    Modules.InventoryDisplay.ClearDisplay(self)
    Modules.InventoryDisplay.FillDisplay(self)

def RefreshEntries(self):
    self.InvManage.buttons.entry_1.delete(0, 'end')
    self.InvManage.buttons.entry_2.delete(0, 'end')
    self.InvManage.buttons.entry_3.delete(0, 'end')
    self.InvManage.buttons.entry_4.delete(0, 'end')
    self.InvManage.buttons.entry_5.delete(0, 'end')
    self.InvManage.buttons.entry_6.delete(0, 'end')

def Create(self):
    self.InvManage = self.row(weights=[1,0])
    self.InvManage.buttons = self.col()
    self.InvManage.frow = self.la()
    

    self.InvManage.buttons.grid1 = self.gr(cols=2) #  Entry Grid
    

    self.InvManage.buttons.label_2 = self.la(text='Item Number:', padx=10, pady=2, width=40, font='Calibri, 14')
    self.InvManage.buttons.entry_1 = self.en(bg= 'white',padx=10, pady=2, width= 40, font='Calibri, 14', highlightthickness = 2, highlightcolor = '#4f81bd')
    self.InvManage.buttons.label_3 = self.la(text='Item Name:', padx=10, pady=2, width=40, font='Calibri, 14')
    self.InvManage.buttons.entry_2 = self.en(bg= 'white', padx=10, pady=2, width=40, font='Calibri, 14', highlightthickness = 2, highlightcolor = '#4f81bd')
    self.InvManage.buttons.label_4 = self.la(text='Quantity:', padx=10, pady=2, width=40, font='Calibri, 14')
    self.InvManage.buttons.entry_3 = self.en(bg= 'white', padx=10, pady=2, width=40, font='Calibri, 14', highlightthickness = 2, highlightcolor = '#4f81bd')
    self.InvManage.buttons.label_4 = self.la(text='Supplier Price:', padx=10, pady=2, width=40, font='Calibri, 14')
    self.InvManage.buttons.entry_4 = self.en(bg= 'white', padx=10, pady=2, width=40, font='Calibri, 14', highlightthickness = 2, highlightcolor = '#4f81bd')
    self.InvManage.buttons.label_5 = self.la(text='Selling Price:', padx=10, pady=2, width=40, font='Calibri, 14')
    self.InvManage.buttons.entry_5 = self.en(bg= 'white', padx=10, pady=2, width=40, font='Calibri, 14', highlightthickness = 2, highlightcolor = '#4f81bd')

    self.endgr()

    self.row(pady=2)
    self.endrow()

    self.row()
    self.InvManage.buttons.button_add_item = self.bu(text='Add Item', bg= '#47c57f',pady=10, padx=10, font='Calibri, 14', command= Callable(add_item, self))    
    self.endrow()

    self.row()
    self.InvManage.buttons.button_edit_item = self.bu(text='  Edit Item  ', bg = '#4f81bd', pady=8, padx=10, font='Calibri, 14', command = Callable(edit_switch, self))
    self.InvManage.buttons.button_remove_item = self.bu(text='Delete Item', bg = '#d94444', pady=8, padx=10, font='Calibri, 14', command= Callable(remove_item, self))
    self.endrow()

    self.row()
    self.InvManage.labelline=self.la(text='_____________________________________________', font=('Calibri', '14'), justify='center', pady=8)
    self.endrow()
    
    self.InvManage.buttons.grid1 = self.gr(cols=2)
    self.InvManage.buttons.entry_6 = self.en(bg= 'white',padx=5, pady=19, font='Calibri, 14', highlightthickness = 2, highlightcolor = '#4f81bd')
    self.InvManage.buttons.button_accept_csv = self.bu(text='Add CSV', bg= '#C38EC7',pady=20, padx=10, font='Calibri, 14', command= Callable (add_csv, self))            # edit: importing csv

    
    self.endgr()

    self.InvManage.buttons.row7 = self.row() # Gr for ADDCSV button
    
    self.InvManage.buttons.printinv = self.bu(text='Print Inventory', bg='#3EA99F', pady=5, padx=10, font='Calibri, 14', command= Callable (print_inv, self))            # edit: importing csv

    self.endrow() # Gr for ADDCSV button
    self.InvManage.photo = Tkinter.PhotoImage(file='Files\Images\SmallLogo.gif')
    self.InvManage.label_7 = self.la(image=self.InvManage.photo)

    self.InvManage.label_8 = self.la(text='Copyright (c) Doru Solutions 2011', pady=2, font='Calibri, 12')
    self.InvManage.lastla = self.la(height=2)

    self.endcol()

    self.InvManage.Display = self.gr(cols=2)
    self.InvManage.toplabels = self.la(text='Item #              Item Name                                     Qty.           Supplier Price                    Selling Price                            ', bg='#404040', fg='White', font=('Calibri', 11), height=1)
    self.InvManage.toplabel2 = self.la()
    
    self.InvManage.Display = self.lb(height=34, width = 60,font=('Courier'))

    self.InvManage.scrollbar = self.sb(command=self.InvManage.Display.yview)
    self.InvManage.Display.config(yscrollcommand=self.InvManage.scrollbar.set)

    Modules.InventoryDisplay.FillDisplay(self)
    self.endgr() #Grid for Display
    self.endcol()
    
