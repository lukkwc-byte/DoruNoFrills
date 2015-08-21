'''
    Version 0.01 31/10/2011 Jonathan (initial logic)
    Version 0.02 01/11/2011 Jonathan (total revenue, # of transactions, total tax done)
    Version 0.03 02/11/2011 Jonathan (Date conversions)
    Version 0.04 03/11/2011 Jonathan (Inventory, Payroll Logic, Total profit)
    Version 0.05 07/11/2011 Jonathan (Logic for display ALL data)
    Version 0.06 08/11/2011 Jonathan (Logic for new Payroll databases + rounding)

'''
import csv
from datetime import date
import datetime
from ReadCSV import *

def CalcSummary(bdate, edate, all):
    # Convert Dates #
    if all == False:
        bdate = bdate.split('/')
        edate = edate.split('/')
        for i in range(len(bdate)):
            bdate[i] = int(bdate[i])
        for i in range(len(edate)):
            edate[i] = int(edate[i])
            
        bdate=datetime.date(bdate[2],bdate[1],bdate[0])
        edate=datetime.date(edate[2],edate[1],edate[0])
            
    ########################## CASH STUFF ##################################
    
    Sessionlist = Session_Read()


    csv_date = Sessionlist[0] 
    session = Sessionlist[1]                                                      
    subtotal = Sessionlist[2]                                                        
    tax = Sessionlist[3]                                                         
    total = Sessionlist[4]                                                      
    del csv_date[0]
    del session[0]
    del subtotal[0]
    del tax[0]
    del total[0]


    # SORTING BY DATES #
    
    trueindexs = []
    for i in range(len(csv_date)):
        if all == True:
            trueindexs.append(i)
        else:
            csv_date[i] = csv_date[i].split(':')
            convert_date = datetime.date(int(csv_date[i][0]),int(csv_date[i][1]),int(csv_date[i][2]))
            if convert_date >= bdate and convert_date <= edate:
                trueindexs.append(i)

    # TOT REVENUE #
        
    new_total = []
    for i in trueindexs:
        new_total.append(total[i])

    tot_revenue = 0
    for i in range(len(new_total)):
        
        tot_revenue = tot_revenue + float(new_total[i])


        
    #tot_revenue = int((float(tot_revenue)+10**(-3))*100)*1.00/100
    # number_transaction #

    number_transaction = len(trueindexs)

    # HST_PAYABLE #

    new_tax = []
    for i in trueindexs:
        new_tax.append(tax[i])

    hst_pay = 0
    for i in range(len(new_total)):
        hst_pay = hst_pay + float(new_tax[i])


    ################## HR STUFF ########################
    
    HRlist = EmployeePay_Read()


    employee = HRlist[0] 
    hr_date = HRlist[1] 
    shift_id = HRlist[2]                                                        
    tot_time = HRlist[4]                                                         
    tot_pay = HRlist[3]
    del employee[0]
    del hr_date[0]
    del shift_id[0]
    del tot_pay[0]
    del tot_time[0]

    trueindexs = []
    for i in range(len(hr_date)):
        if all == True:
            trueindexs.append(i)
        else:
            hr_date[i] = hr_date[i].split('-')
            convert_date = datetime.date(int(hr_date[i][0]),int(hr_date[i][1]),int(hr_date[i][2]))
            if convert_date >= bdate and convert_date <= edate:
                trueindexs.append(i)

    # COST HR #
        
    new_tot_pay = []
    for i in trueindexs:
        new_tot_pay.append(tot_pay[i])

    cost_hr = 0
    for i in range(len(new_tot_pay)):
        cost_hr = cost_hr + float(new_tot_pay[i])

    cost_hr=("%.3f" % cost_hr)

    # TOTAL HOUR #
        
    new_tot_time = []
    for i in trueindexs:
        new_tot_time.append(tot_time[i])

    total_hour = 0
    for i in range(len(new_tot_time)):
        total_hour = total_hour + float(new_tot_time[i])

    
    total_hour=("%.4f" % total_hour)
    
    ################## INVENTORY STUFF ########################
    
    Invlist = InvChange_Read()

    item_number = Invlist[0]
    item_name = Invlist[1]
    quantity_added = Invlist[2]
    item_price = Invlist[3]
    inv_total = Invlist[4]
    inv_date = Invlist[5]
    inv_time = Invlist[6]
    del item_number[0]
    del item_name[0]
    del quantity_added[0]
    del item_price[0]
    del inv_total[0]
    del inv_date[0]
    del inv_time[0]

    # SORTING BY DATES #
    
    trueindexs = []
    for i in range(len(inv_date)):
        if all == True:
            trueindexs.append(i)
        else:
            inv_date[i] = inv_date[i].split(':')
            convert_date = datetime.date(int(inv_date[i][0]),int(inv_date[i][1]),int(inv_date[i][2]))
            if convert_date >= bdate and convert_date <= edate:
                trueindexs.append(i)

    # COST INV #
        
    new_inv_total = []
    for i in trueindexs:
        new_inv_total.append(inv_total[i])

    cost_inv = 0
    for i in range(len(new_inv_total)):
        cost_inv = cost_inv + float(new_inv_total[i])


################## PROFIT STUFF ########################

    tot_profit = tot_revenue-hst_pay-cost_inv-(float(cost_hr))

    if float(cost_inv) == 0 and float(cost_hr) == 0 and float(tot_revenue == 0) and float(hst_pay == 0) and float(tot_profit) == 0:
        return False
    else:
        cost_inv = '$'+str("%.2f" % (float(cost_inv)))
        cost_hr = '$'+str("%.2f" % (float(cost_hr)))
        tot_revenue = '$'+str("%.2f" % (float(tot_revenue)))
        hst_pay = '$'+str("%.2f" % (float(hst_pay)))
        tot_profit = '$'+str("%.2f" % (round(float(tot_profit),2)))


        
        return [cost_inv, cost_hr, total_hour, number_transaction, tot_revenue, hst_pay, tot_profit]
