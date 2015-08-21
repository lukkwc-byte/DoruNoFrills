'''
Ben - Oct 31, 2011 (Halloween Update) - Started and finished ClearDisplay and FillDisplay
'''
import csv
from ReadCSV import *
def FillDisplay(self):
    Acclist=Account_Read()
    user_name = Acclist[0]
    pass_word = Acclist[1]
    user_lvl = Acclist[2]
    hour_wage = Acclist[3]
    del user_name[0]
    del pass_word[0]
    del user_lvl[0]
    del hour_wage[0]
    for i in range(len(user_name)):
        User = user_name[i]
        Pass = pass_word[i]
        Level = user_lvl[i]
        Wage = hour_wage[i]

        char1 = 15
        char2 = 15
        char3 = 10
        char4 = 16

        space1 = (char1-len(user_name[i]))*' '
        space2 = (char1-len(pass_word[i]))*' '
        space3 = (char1-len(user_lvl[i]))*' '
        #space4 = (char1-len(hour_wage[i]))*' '
        itemlist= user_name[i]+space1+pass_word[i]+space2+user_lvl[i]+space3+'$ '+('%.2f' % float(hour_wage[i]))+' '
        self.EmpAccounts.Display.insert('end', itemlist)
def ClearDisplay(self):
    self.EmpAccounts.Display.delete(0, 'end')
