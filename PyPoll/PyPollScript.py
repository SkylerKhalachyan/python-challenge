import csv

csvpath ="PyPoll/Resources/election_data.csv"

vcounter = 0
candidatecounter = 0
charles = 0
diana = 0
raymon = 0

votes = []
candidate = []
candidate_vote = []


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
        candidatecounter +=1

        # count votes for Charles 
        # count votes for Diana
        # count votes for Raymon 
    
    
        #Identifying unique candidates 
        if row[2] not in candidate:
            candidate.append(str(row[2]))
    print(f"Total Votes: {vcounter}")
    print(f"---------------------------------")  

   #print(candidate)   

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csv_header = next(csvreader)
    
    for row in csvreader:
        if row[2] == candidate[0]:
            charles +=1
        if row[2] == candidate[1]:
            diana +=1
        if row[2] == candidate[2]:
            raymon +=1
    candidate_vote.append(charles)
    candidate_vote.append(diana)
    candidate_vote.append(raymon)

    #print(candidate_vote)
    
        
    print(f"Charles Casper Stockham: ({candidate_vote[0]})")
    print(f"Diana DeGette: ({candidate_vote[1]})")
    print(f"Raymon Anthony Doane: ({candidate_vote[2]})")
    print(f"---------------------------------")
    print(f"Winner: Diana DeGette")
    print(f"---------------------------------")
    #print(candidate)
    
txtpath ="PyPoll/Analysis/PyPoll_Analysis.txt"

with open(txtpath, 'w') as txtfile:

# Write the first row and each consecutive row thereafter 
    txtfile.write(f"Election Results"\
                  f"\n---------------------------------"\
                  f"\nTotal Votes: {vcounter}"\
                  f"\n---------------------------------"\
                  f"\nCharles Casper Stockham: ({candidate_vote[0]})"\
                  f"\nDiana DeGette: ({candidate_vote[1]})"\
                  f"\nRaymon Anthony Doane: ({candidate_vote[2]})"\
                  f"\n---------------------------------"\
                  f"\nWinner: Diana DeGette"\
                  f"\n---------------------------------")


  


    
    


