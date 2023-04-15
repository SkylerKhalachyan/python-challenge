import csv

csvpath ="PyBank/Resources/budget_data.csv"

mcounter = 0
plcounter = 0



month = []
pl = []
pldifference = []



with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    print(f"Financial Analysis")
    print(f"---------------------------------")
    
    for row in csvreader:
       # print(row)

# Get the total number of months included in the dataset

        month.append(row[0])
        pl.append(int(row[1]))
       
        

        mcounter +=1
        plcounter +=1

        #print(mcounter)
    print(f"Total Months: {mcounter}")
        
        ##trying to solve step 2
        ##pracitcing 
        #print(month[2])
        #print(sum([pl]))


#The net total amount of "Profit/Losses" over the entire period
        #print(plcounter)
        #print(sum(pl))
    sumpl = sum(pl)
    print(f"Total: ${sumpl}")

#The changes in "Profit/Losses" over the entire period, and then the average of those changes
    for i in range(1, len(pl)):
        pldifference.append(pl[i]-pl[i-1])
    
        #print(pldifference)

        avgpldf = round(sum(pldifference)/len(pldifference),2)
        #print(avgpldf)
    print(f"Average Change: ${avgpldf}")

#The greatest increase in profits(date and amount) over the entire period
gi = max(pldifference)
gd = min(pldifference)

#print(gd) 
maxmonth = (month[pldifference.index(gi)+1])
#print(maxmonth)
print(f"Greatest Increase in Profits: {maxmonth}  (${gi})")
#The greatest decrease in profits (date and amount) over the entire period


minmonth = (month[pldifference.index(gd)+1])

print(f"Greatest Decrease in Profits: {minmonth}  (${gd})")

txtpath ="PyBank/Analysis/PyBank_Analysis.txt"

with open(txtpath, 'w') as txtfile:

# Write the first row 
    txtfile.write(f"Financial Analysis"\
                  f"\n---------------------------------"\
                  f"\nTotal Months: {mcounter}"\
                  f"\nTotal: ${sumpl}"\
                  f"\nAverage Change: ${avgpldf}"\
                  f"\nGreatest Increase in Profits: {maxmonth}  (${gi})"\
                  f"\nGreatest Decrease in Profits: {minmonth}  (${gd})"  )

        # "print(f"Financial Analysis"),
        #                 print(f"---------------------------------"),print(f"Total Months: {mcounter}",),
        #                 print(f"Total: ${sumpl}"),print(f"Average Change: ${avgpldf}"),
        #                  print(f"Greatest Increase in Profits: {maxmonth}  (${gi})"),
        #                   print(f"Greatest Decrease in Profits: {minmonth}  (${gd})"))


    
    


