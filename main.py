import csv

csvpath ="PyBank/Resources/budget_data.csv"

counter = 0

month = []

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
       # print(row)

# Get the total number of months included in the dataset

        month.append(row[0])
        

        counter +=1


    print(counter)



#The net total amount of "Profit/Losses" over the entire period

#The changes in "Profit/Losses" over the entire period, and then the average of those changes

#The greatest increase in profits(date and amount) over the entire period

#The greatest decrease in profits (date and amount) over the entire period
