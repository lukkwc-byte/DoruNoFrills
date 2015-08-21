import csv
from ReadCSV import *
from WriteCSV import *
import os

def Create(session, paid, change):
    Cashlist=Cash_Read()
    applicabledate=[]
    for i in range(len(Cashlist[1])):
        if session==Cashlist[1][i]:
            applicabledate.append(i)
    date=Cashlist[0][applicabledate[0]]
    date2 = date.replace(':', '/')
    employee=Cashlist[9][applicabledate[0]]
    time=Cashlist[8][applicabledate[0]]
    text_file = open("cash_receipt.txt", "w")
    text_file.write("      ************************************** \n")
    text_file.write("      ********** Doru's  NoFrills ********** \n")
    text_file.write("      ****** 1000 New Westminster Dr. ****** \n")
    text_file.write("      ******* Thornhill, ON L4J 8G3 ******** \n") 
    text_file.write("      ********* Tel: (905) 882-0277 ******** \n")
    text_file.write("      ************************************** \n")
    text_file.write('\n')
    text_file.write("   Employee: " + employee + "   Transaction ID: " + session + " \n")    
    text_file.write("         Date: " + date2 + " at " + time + " ")   
    text_file.write('\n')
    text_file.write('================================================== \n')
    text_file.write('  Item              Quantity    Price')
    text_file.write('\n')
    for i in range(len(applicabledate)):
        Item = Cashlist[3][applicabledate[i]]
        Quant = Cashlist[4][applicabledate[i]]
        Price = '$'+str("%.2f"%(float(Cashlist[5][applicabledate[i]])))

        char = 18
        char2 = 12

        space = (char-len(Item))*' '
        space2 = (char2-len(Quant))*' '
        
        text_file.write('  '+Item + space + Quant + space2 + Price +'\n')

    Money=Session_Read()
    Subtotal = '$'+str("%.2f"%(float(Money[2][int(session)])))
    Tax = '$'+str("%.2f"%(float(Money[3][int(session)])))
    Total = '$'+str("%.2f"%(float(Money[4][int(session)])))
    text_file.write('================================================== \n')
    text_file.write('          Subtotal:    ' +Subtotal+'\n')
    text_file.write('               Tax:    ' +Tax+'\n')
    text_file.write('             Total:    ' +Total+'\n')
    text_file.write('================================================== \n')
    text_file.write('       Amount Paid:    ' +Subtotal+'\n')
    text_file.write('   Change Tendered:    ' +Tax+'\n')

    text_file.close()
    
    os.startfile('cash_receipt.txt')
