'''
    Version ALPHA 18/11/2011 Shimmy (finished GUI)
    Version 0.01 22/11/2011 Kyuho (implemented additem + display item logic)
'''

### SAMPLE SCREEN - TESTING PURPOSES ###

from Tkinter import *
from Swampy.Gui import * # Handles Graphics
import InvLocatorErrorPopup
from Modules.InvLocDisplay import *
from Modules.AddItemToInvLocator import *
from Modules.RemoveItemFromInvLocator import *
from Modules.DisplayItemInAisle import *
import Modules.Check
    
def Aisle_1(self, event):
    self.InvLoc.destroy()
    Create(self)
    self.InvLoc.ItemAisle.config(text='Items In Aisle 1')
    self.InvLoc.Aisle1=self.InvLoc.canvas.rectangle([[-205,-225], [215,-175]],fill='#47c57f',outline='black', width=2, activefill='#47c57f')
    self.InvLoc.Aisle1Text=self.InvLoc.canvas.text([5,-200],text='Aisle 1', fill='black')
    Modules.Check.Aisle_num = '1'
    display_list = loc_Aisle_DisplayItem('1')
    self.InvLoc.ItemsInAisle.delete('end')
    if display_list != False:
        loc_displayed(self, display_list)

        
def Aisle_2(self, event):
    self.InvLoc.destroy()
    Create(self)
    self.InvLoc.ItemAisle.config(text='Items In Aisle 2')
    self.InvLoc.Aisle2=self.InvLoc.canvas.rectangle([[-205,-100], [215,-50]],fill='#47c57f',outline='black', width=2, activefill='#47c57f')
    self.InvLoc.Aisle2Text=self.InvLoc.canvas.text([5,-75],text='Aisle 2', fill='black')
    Modules.Check.Aisle_num = '2'
    display_list = loc_Aisle_DisplayItem('2')
    self.InvLoc.ItemsInAisle.delete('end')
    if display_list != False:
        loc_displayed(self, display_list)


def Aisle_3(self, event):
    self.InvLoc.destroy()
    Create(self)
    self.InvLoc.ItemAisle.config(text='Items In Aisle 3')
    self.InvLoc.Aisle3=self.InvLoc.canvas.rectangle([[-205,25], [215,75]],fill='#47c57f',outline='black', width=2, activefill='#47c57f')
    self.InvLoc.Aisle3Text=self.InvLoc.canvas.text([5,50],text='Aisle 3', fill='black')
    Modules.Check.Aisle_num = '3'
    display_list = loc_Aisle_DisplayItem('3')
    self.InvLoc.ItemsInAisle.delete('end')
    if display_list != False:
        loc_displayed(self, display_list)


def Aisle_4(self, event):
    self.InvLoc.destroy()
    Create(self)
    self.InvLoc.ItemAisle.config(text='Items In Aisle 4')
    self.InvLoc.Aisle4=self.InvLoc.canvas.rectangle([[-205,150], [215,200]],fill='#47c57f',outline='black', width=2, activefill='#47c57f')
    self.InvLoc.Aisle4Text=self.InvLoc.canvas.text([5,175],text='Aisle 4', fill='black')
    Modules.Check.Aisle_num = '4'
    display_list = loc_Aisle_DisplayItem('4')
    self.InvLoc.ItemsInAisle.delete('end')
    if display_list != False:
        loc_displayed(self, display_list)


def Aisle_5(self, event):
    self.InvLoc.destroy()
    Create(self)
    self.InvLoc.ItemAisle.config(text='Items In Aisle 5')
    self.InvLoc.Aisle5=self.InvLoc.canvas.rectangle([[-205,275], [215,325]],fill='#47c57f',outline='black', width=2, activefill='#47c57f')
    self.InvLoc.Aisle5Text=self.InvLoc.canvas.text([5,300],text='Aisle 5', fill='black')
    Modules.Check.Aisle_num = '5'
    display_list = loc_Aisle_DisplayItem('5')
    self.InvLoc.ItemsInAisle.delete('end')
    if display_list != False:
        loc_displayed(self, display_list)


def Aisle_6(self, event):
    self.InvLoc.destroy()
    Create(self)
    self.InvLoc.ItemAisle.config(text='Items In Aisle 6')
    self.InvLoc.Aisle6=self.InvLoc.canvas.rectangle([[-275,400], [-335,-600]],fill='#47c57f',outline='black', width=2, activefill='#47c57f')        
    self.InvLoc.Aisle6Text=self.InvLoc.canvas.text([-305, 0],text='Aisle 6', fill='black')
    Modules.Check.Aisle_num = '6'
    display_list = loc_Aisle_DisplayItem('6')
    self.InvLoc.ItemsInAisle.delete('end')
    if display_list != False:
        loc_displayed(self, display_list)


def Aisle_7(self, event):
    self.InvLoc.destroy()
    Create(self)
    self.InvLoc.ItemAisle.config(text='Items In Aisle 7')
    self.InvLoc.Aisle7=self.InvLoc.canvas.rectangle([[285,400], [345,-600]],fill='#47c57f',outline='black', width=2, activefill='#47c57f')
    self.InvLoc.Aisle7Text=self.InvLoc.canvas.text([315,0],text='Aisle 7', fill='black')
    Modules.Check.Aisle_num = '7'
    display_list = loc_Aisle_DisplayItem('7')
    self.InvLoc.ItemsInAisle.delete('end')
    if display_list != False:
        loc_displayed(self, display_list)


def CashRegister(self, event):
    self.InvLoc.destroy()
    Create(self)
    self.InvLoc.ItemAisle.config(text='Items In Cash Register')
    self.InvLoc.Cash_Register=self.InvLoc.canvas.rectangle([[160,-250], [250,-300]],fill='#47c57f',outline='black', width=2, activefill='#47c57f')
    self.InvLoc.CashText=self.InvLoc.canvas.text([205, -266],text='Cash', fill='black')
    self.InvLoc.RegisterText=self.InvLoc.canvas.text([205,-282],text='Register', fill='black')
    Modules.Check.Aisle_num = '8'
    display_list = loc_Aisle_DisplayItem('8')
    self.InvLoc.ItemsInAisle.delete('end')
    if display_list != False:
        loc_displayed(self, display_list)

def errorcodes(error_testing):
    InvLocatorErrorPopup.Create(error_testing)


##############################LOGIC##############################


def ClearEntries(self):
    return self


def refresh_undisplayed(self):
    loc_undisplayed(self)


def functionname(error_testing):
    InvLocatorErrorPopup.Create(error_testing)


def add_add_into_list(self):
    returnlis = []
    returnlis.append(Modules.Check.Aisle_num)
    invlist = Undisplayed_Read()
    try:
        ai = int(self.InvLoc.Warehouse.curselection()[0])
        i_number = invlist[0][ai+1]
        returnlis.append(i_number)
        return returnlis
    except:
        errorcodes(13)

def remove_add_into_list(self):
    returnlis = []
    returnlis.append(Modules.Check.Aisle_num)
    invlist = InventoryLoc_Read()
    try:
        ai = int(self.InvLoc.ItemsInAisle.curselection()[0])
        aislelist=[]
        for i in range(len(invlist[0])):
            if invlist[int(Modules.Check.Aisle_num)][i]=='Yes':
                aislelist.append(invlist[0][i])
        i_number = aislelist[ai]
        returnlis.append(i_number)
        return returnlis
    except:
        errorcodes(13)
        
def add_item(self):
    list1 = add_add_into_list(self)
    if list1 != None:
        list2 = loc_in_AddItem(list1[0], list1[1])
        if len(list2) == 1:
            functionname(list2[0])
        else:
            loc_displayed(self, list2[1])
            refresh_undisplayed(self)
            ClearEntries(self)

def remove_item(self):
    list1 = remove_add_into_list(self)
    if list1 != None:
        list2 = loc_out_RemoveItem(list1[0], list1[1])

        if len(list2) == 1:
            functionname(list2[0])

        else:
            loc_displayed(self, list2[1])
            refresh_undisplayed(self)
            ClearEntries(self)


#################################################################


def Create(self):
    self.InvLoc=self.row()
    self.InvLoc.gridleft=self.gr(cols=1)
    self.InvLoc.gridleft=self.gr(cols=1)
    self.InvLoc.column=self.col(weights=[1])
    self.InvLoc.ItemAisle=self.la(font=('Calibri', '16', 'bold','underline'),text='Items In Aisle', padx=10)
    self.InvLoc.toplabels = self.la(text='Item Name                                               Quantity                   ', bg='#404040', fg='White', font=('Calibri', 9))
    self.endcol()
    self.InvLoc.gridscroll=self.gr(cols=3)
    self.InvLoc.label=self.la()
    self.InvLoc.ItemsInAisle=self.lb(width=30, height=12,font=('Courier'))
    self.InvLoc.ItemsInAisle.Scroll = self.sb(command=self.InvLoc.ItemsInAisle.yview)
    self.InvLoc.ItemsInAisle.config(yscrollcommand=self.InvLoc.ItemsInAisle.Scroll.set)
    



    self.endgr()
    self.InvLoc.label=self.la()
    self.endgr()

    self.InvLoc.gridleft2=self.gr(cols=2)
    self.InvLoc.row=self.row()
    if int(Modules.Check.userlevel) == 1:
        self.InvLoc.AddItem=self.bu(font=('Calibri', '14'),text='    Place Item    ', padx=8, height=1, bg= '#47c57f', activebackground='#009C42', command = Callable(add_item, self))
        self.InvLoc.RemoveItem=self.bu(font=('Calibri', '14'),text='Remove Item', padx=8, height=1, bg = '#d94444', activebackground='#B44242', command = Callable(remove_item, self))
    else:
        self.InvLoc.AddItem=self.bu(font=('Calibri', '14'),text='    Place Item    ', padx=8, height=1, bg= '#47c57f', activebackground='#009C42', state='disabled')
        self.InvLoc.RemoveItem=self.bu(font=('Calibri', '14'),text='Remove Item', padx=8, height=1, bg = '#d94444', activebackground='#B44242', state='disabled')        
    self.endrow()
    self.endgr()

    self.InvLoc.gridleft2=self.gr(cols=1)
    self.InvLoc.column=self.col(weights=[1])
    self.InvLoc.NotInAisle=self.la(font=('Calibri', '16', 'bold','underline'),text='Unplaced Items', padx=10, pady=1)
    self.InvLoc.toplabels = self.la(text='Item Name                                               Quantity                   ', bg='#404040', fg='White', font=('Calibri', 9))
    self.endcol()
    self.InvLoc.warehouselb=self.gr(cols=3)
    self.InvLoc.label=self.la()
    self.InvLoc.Warehouse=self.lb(width=30, height=12,font=('Courier'))
    self.InvLoc.Warehouse.Scroll = self.sb(command=self.InvLoc.Warehouse.yview)
    self.InvLoc.Warehouse.config(yscrollcommand=self.InvLoc.Warehouse.Scroll.set)
    self.endgr() 
    self.InvLoc.label=self.la(padx=6)
    self.endgr()                
    self.endgr()
    
    


    self.InvLoc.gridright=self.gr(cols=1)
    self.InvLoc.canvas = self.ca(width=700, height=700, bg='#A2ABA5', borderwidth=1,relief='sunken')
                  

    self.InvLoc.Door=self.InvLoc.canvas.rectangle([[-95, -400], [105, -275]],fill='#2B2E2E',outline='black', width=2, activefill='#d94444')
    self.InvLoc.Aisle1=self.InvLoc.canvas.rectangle([[-205,-225], [215,-175]],fill='#313F54',outline='black', width=2, activefill='#47c57f')
    self.InvLoc.Aisle2=self.InvLoc.canvas.rectangle([[-205,-100], [215,-50]],fill='#313F54',outline='black', width=2, activefill='#47c57f')
    self.InvLoc.Aisle3=self.InvLoc.canvas.rectangle([[-205,25], [215,75]],fill='#313F54',outline='black', width=2, activefill='#47c57f')
    self.InvLoc.Aisle4=self.InvLoc.canvas.rectangle([[-205,150], [215,200]],fill='#313F54',outline='black', width=2, activefill='#47c57f')
    self.InvLoc.Aisle5=self.InvLoc.canvas.rectangle([[-205,275], [215,325]],fill='#313F54',outline='black', width=2, activefill='#47c57f')
    self.InvLoc.Aisle6=self.InvLoc.canvas.rectangle([[-275,400], [-335,-600]],fill='#313F54',outline='black', width=2, activefill='#47c57f')
    self.InvLoc.Aisle7=self.InvLoc.canvas.rectangle([[285,400], [345,-600]],fill='#313F54',outline='black', width=2, activefill='#47c57f')
    self.InvLoc.Cash_Register=self.InvLoc.canvas.rectangle([[160,-250], [250,-300]],fill='#313F54',outline='black', width=2, activefill='#47c57f')

    self.InvLoc.canvas.tag_bind(self.InvLoc.Aisle1,'<ButtonPress-1>', Callable(Aisle_1, self))
    self.InvLoc.canvas.tag_bind(self.InvLoc.Aisle2,'<ButtonPress-1>', Callable(Aisle_2, self))
    self.InvLoc.canvas.tag_bind(self.InvLoc.Aisle3,'<ButtonPress-1>', Callable(Aisle_3, self))
    self.InvLoc.canvas.tag_bind(self.InvLoc.Aisle4,'<ButtonPress-1>', Callable(Aisle_4, self))
    self.InvLoc.canvas.tag_bind(self.InvLoc.Aisle5,'<ButtonPress-1>', Callable(Aisle_5, self))
    self.InvLoc.canvas.tag_bind(self.InvLoc.Aisle6,'<ButtonPress-1>', Callable(Aisle_6, self))
    self.InvLoc.canvas.tag_bind(self.InvLoc.Aisle7,'<ButtonPress-1>', Callable(Aisle_7, self))
    self.InvLoc.canvas.tag_bind(self.InvLoc.Cash_Register,'<ButtonPress-1>', Callable(CashRegister, self))

    self.InvLoc.DoorText=self.InvLoc.canvas.text([5,-300],text='Door', fill='#CAE6E8')
    self.InvLoc.Aisle1Text=self.InvLoc.canvas.text([5,-200],text='Aisle 1', fill='#CAE6E8')
    self.InvLoc.Aisle2Text=self.InvLoc.canvas.text([5,-75],text='Aisle 2', fill='#CAE6E8')
    self.InvLoc.Aisle3Text=self.InvLoc.canvas.text([5,50],text='Aisle 3', fill='#CAE6E8')
    self.InvLoc.Aisle4Text=self.InvLoc.canvas.text([5,175],text='Aisle 4', fill='#CAE6E8')
    self.InvLoc.Aisle5Text=self.InvLoc.canvas.text([5,300],text='Aisle 5', fill='#CAE6E8')
    self.InvLoc.Aisle6Text=self.InvLoc.canvas.text([-305, 0],text='Aisle 6', fill='#CAE6E8')
    self.InvLoc.Aisle7Text=self.InvLoc.canvas.text([315,0],text='Aisle 7', fill='#CAE6E8')
    self.InvLoc.CashText=self.InvLoc.canvas.text([205, -266],text='Cash', fill='#CAE6E8')
    self.InvLoc.RegisterText=self.InvLoc.canvas.text([205,-282],text='Register', fill='#CAE6E8')

    refresh_undisplayed(self)

    self.endgr()



















    
    self.endcol()
