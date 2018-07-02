import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")
totalnumber = 0
canvote = 0
candidatelist = {}



with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvfile)

    for pypoll in csvreader:
        totalnumber = totalnumber +1  
        
        if pypoll[2] in candidatelist:
           candidatelist[pypoll[2]] += 1
        else:
           candidatelist[pypoll[2]] = 1

    print("------------------------------------------------------------------")    
    print("Total Votes: " + str(totalnumber))
    print("------------------------------------------------------------------")
    
    maxvote = max(candidatelist.values())
    for canvote in candidatelist:
        voterate = candidatelist[canvote] / totalnumber * 100
        if candidatelist[canvote] == maxvote:
           x = canvote
        print(canvote + ": " + "{0:.3f}".format(voterate) + "% " + "(" + str(candidatelist[canvote]) + ")")
    print("------------------------------------------------------------------") 
    print("Winner: " + x)
        


  

      
