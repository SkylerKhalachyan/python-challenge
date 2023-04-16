import csv

csvpath ="PyPoll/Resources/election_data.csv"

vcounter = 0


votes = []



with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    print(f"Election Results")
    print(f"---------------------------------")
    for row in csvreader:
       # print(row)

# Get the total number of votes cast

        votes.append(row[0])
       
        vcounter +=1
        

    print(f"Total Votes: {vcounter}")
    print(f"---------------------------------")  
   
    
txtpath ="PyPoll/Analysis/PyPoll_Analysis.txt"

with open(txtpath, 'w') as txtfile:

# Write the first row 
    txtfile.write(f"Election Results"\
                  f"\n---------------------------------"\
                  f"\nTotal Votes: {vcounter}"\
                  f"\n---------------------------------"\
                  
                  f"\n---------------------------------"\
                  f"\nWinner: ")


  


    
    


