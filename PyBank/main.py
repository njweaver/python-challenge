import os
import csv

csvpath = os.path.join('budget_data.csv')

#Make lists
floatnet = []
monthlist = []
#Open file
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader)

    
    # Read row
    for row in csvreader:
        floatnet.append(float(row[1]))
        monthlist.append(row[0])


#Make calculations
totalmonth = len(floatnet)
total = sum(floatnet)
mean = round(sum(floatnet)/len(floatnet), 2)
greatincrease = max(floatnet)
greatdecrease = min(floatnet)
indexincrease = floatnet.index(greatincrease)
indexdecrease = floatnet.index(greatdecrease)
monthincrease = monthlist[indexincrease]
monthdecrease = monthlist[indexdecrease]

#Print Output
print(f"Financial Analysis")
print(f"------------------------------------")
print(f"Total Months: {totalmonth}")
print(f"Total: ${total}")
print(f"Average Change: ${mean}")
print(f"Greatest Increase in Profits: {monthincrease} ${greatincrease}")
print(f"Greatest Decrease in Profits: {monthdecrease} ${greatdecrease}")
        
#Write Output to File    
output_file = os.path.join("financialsummery.txt")


file = open("financialsummery.txt","w")
file.write("Financial Analysis \n")
file.write("--------------------------------- \n")
file.write("Total Months:" + str(totalmonth) + "\n")
file.write("Total: $" + str(total) + "\n")
file.write("Average Change: $" + str(mean) + "\n")
file.write("Greatest Change in Profits: " + monthincrease + " $" + str(greatincrease) + "\n")
file.write("Greatest Decrease in Profits: " + monthdecrease + " $" + str(greatdecrease))