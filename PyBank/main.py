import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")
totalmonth = 0
totalnet = 0
averagechange = 0
lastrecord = 0
greatestincrease = 0
greatestdecrease = 0
minmam = {
    "min":["",0],
    "max":["",0]
}
x = "min"
y = "max"
newchange =0



with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvfile)
    for row in csvreader:
        netval = int(row[1])
        totalmonth = totalmonth + 1
        totalnet = totalnet + netval
        if(lastrecord != 0):
            newchange =netval - lastrecord
            averagechange += newchange
        lastrecord = netval

        if newchange >= minmam["max"][1]:
            minmam["max"][1] = newchange
            minmam["max"][0] = row[0]
        if newchange < minmam["min"][1]:
            minmam["min"][1] = newchange
            minmam["min"][0] = row[0]
            
    
    print("-----------------------------------")      
    print("total Months: " + str(totalmonth))
    print("Total Net Amount of Profit/Loss: " + "$" + str(totalnet))
    newavrg = averagechange / (totalmonth - 1)
    print("Average Change: " + "${0:.2f}".format(newavrg))
    print("Greatest Increase in Profits: " + str(minmam["max"][0]) +" "+ "($" + str(minmam["max"][1]) + ")")
    print("Greatest Decrease in Profits: " + str(minmam["min"][0]) +" "+ "($" + str(minmam["min"][1]) + ")")
    
    
    
         
    
    

    
        
