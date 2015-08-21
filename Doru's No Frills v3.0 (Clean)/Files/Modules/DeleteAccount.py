import csv
from ReadCSV import *
from WriteCSV import *
#
def ReadDelAccountsCSV(username):
    lis = Account_Read()
    usernamelist = lis[0]
    password = lis[1]
    userlevel = lis[2]
    hourlywage = lis[3]
    secureQ = lis[4]
    secureA = lis[5]

    a=usernamelist.pop(0)
    b=password.pop(0)
    c=userlevel.pop(0)
    d=hourlywage.pop(0)
    e=secureQ.pop(0)
    f=secureA.pop(0)
    breaks=False
    for i in range(len(usernamelist)):
        if breaks==False:
            if usernamelist[i]==username:
                usernamelist.pop(i)
                password.pop(i)
                userlevel.pop(i)
                hourlywage.pop(i)
                secureQ.pop(i)
                secureA.pop(i)
                breaks=True
                
    usernamelist.insert(0,a)
    password.insert(0,b)
    userlevel.insert(0,c)
    hourlywage.insert(0,d)
    secureQ.insert(0,e)
    secureA.insert(0,f)
    
    fulllist = [usernamelist, password, userlevel, hourlywage, secureQ, secureA]
    WriteCSV(fulllist, 'Files/Modules/Database/useraccounts.csv')
