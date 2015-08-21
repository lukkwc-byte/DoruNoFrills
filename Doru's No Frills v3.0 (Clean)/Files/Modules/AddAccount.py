'''
    Version ALPHA1.2 27/09/2011 Kyuho
    Version 0.01 28/09/2011 Kyuho
    Version 1.50 31/10/2011 Ben (Fully error proofed)
    Version 1.51 1/11/2011 Ben (Fixed error with validity 10)
    Version 1.52 2/11/2011 Ben (Made it possible to enter the wage as 4 numbers before the decimal then 2 numbers)
'''


import csv
from ReadCSV import *
from WriteCSV import *
def ReadAccountsCSV(lis):
    number_list = '0123456789.'
    levels = '01'
    validity = 0
    for i in range(len(lis)):
        if lis[0] == '' or lis[1] == '' or lis[2] == '' or lis[3] == '' or lis[4] == '' or lis[5] == '':
            validity = 13
            break
        if '|' in lis[i] or ',' in lis[i]:
            validity = 1
            break
        if ' ' in lis[0]:
            validity = 2 #Space in User
            break
        if len(lis[0]) > 12:
            validity = 4 #Too many characters in user
            break
        if ' ' in lis[1]:
            validity = 3 #Space in Pass
            break
        if len(lis[1]) > 12:
            validity = 5 #Too many characters in pass
            break
        if len(lis[2]) != 1:
            validity = 6 #User level must be 1 character
            break
        for i in range(len(lis[2])):
            if lis[2][i] not in levels:
                validity = 8 # Non-numbers in level
                break
        dot_counter = 0
        for i in range(len(lis[3])):
            if lis[3][i] == '.':
                dot_counter += 1
                dot_pos = i
        words=False
        for i in range(len(lis[3])):
            if lis[3][i] not in number_list:
                words=True
                break
        if words==True:
            validity = 9
            break                
        if dot_counter!=0:
            if len(lis[3][0:dot_pos])>4 or len(lis[3][dot_pos:-1])>2:
                validity = 7
                break
        if dot_counter==0:
            if len(lis[3])>4:
                validity = 7
                break

        if dot_counter >=2:
            validity = 12 #more than 1 decimal in wage
            break
        if float(lis[3]) <= 0:
            validity = 10 #Wage isn't zero or smaller
            break
        if len(lis[4]) > 35:
            validity = 14
            break
        if len(lis[5]) > 15:
            validity = 15
            break
        
    if validity > 0:
        return [validity]
    else:
        Accountlist = Account_Read()

        username = Accountlist[0]
        password = Accountlist[1]
        userlevel = Accountlist[2]
        hourlywage = Accountlist[3]
        secureQ = Accountlist[4]
        secureA = Accountlist[5]

        repetition = 0

        for i in range(len(username)):
            if username[i] == lis[0]:
                repetition = 1
                break

        if repetition == 0:
            username.append(lis[0])
            password.append(lis[1])
            userlevel.append(lis[2])
            hourlywage.append(lis[3])
            secureQ.append(lis[4])
            secureA.append(lis[5])

            returnlis = [username, password, userlevel, hourlywage, secureQ, secureA]

            return returnlis

        else:
            validity = 11
            return [validity]     # when there is a same username

def AddAccount(lis):
    if len(lis) != 1:
        csvfile = 'Files\Modules\Database\useraccounts.csv'
        WriteCSV(lis, csvfile)
        return [True]
    else:
        return False, lis[0]       # same username


# csv file name is 'accounts.csv'

# 1. declare a user-inputted list
# 2. 'new_list' = ReadAccountsCSV('user_list')
# 3. AddAccount('new_list')
