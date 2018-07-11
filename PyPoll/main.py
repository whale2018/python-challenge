import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")
totalnumber = 0
canvote = 0
candidatelist = {}

outfile = open("analyzed_pypoll.txt", 'w')

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
    outfile.write("-----------------------------------------------------------"+ "\n")   
    print("Total Votes: " + str(totalnumber))
    outfile.write("Total Votes: " + str(totalnumber)+ "\n")
    print("------------------------------------------------------------------")
    outfile.write("-----------------------------------------------------------"+ "\n")
    maxvote = max(candidatelist.values())
    for canvote in candidatelist:
        voterate = candidatelist[canvote] / totalnumber * 100
        if candidatelist[canvote] == maxvote:
           x = canvote
        print(canvote + ": " + "{0:.3f}".format(voterate) + "% " + "(" + str(candidatelist[canvote]) + ")")
        outfile.write(canvote + ": " + "{0:.3f}".format(voterate) + "% " + "(" + str(candidatelist[canvote]) + ")"+ "\n")
    print("------------------------------------------------------------------")
    outfile.write("-----------------------------------------------------------"+ "\n")
    print("Winner: " + x)
    outfile.write("Winner: " + x+ "\n")
outfile.close()
        


  

      
