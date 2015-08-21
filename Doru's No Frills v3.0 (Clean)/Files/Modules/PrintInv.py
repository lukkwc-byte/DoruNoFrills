'''

'''



import csv
import time
from WriteCSV import *
from ReadCSV import *

def Create():
    Inv=Inv_Read()

    if len(Inv[1]) == 1:
        return False

    else:
        
        Itemnumber=Inv[0]
        Itemname=Inv[1]
        lis=[Itemnumber,Itemname]
        WriteCSV(lis, "Files\Modules\Database\Inventory List.csv")

        return True



