import os
import csv

csvpath = os.path.join('election_data.csv')

idlist = []
candidatelist =[]
votelist = []
countylist =[]
cand1list = []
cand2list = []
cand3list = []
cand4list = []

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    for row in csvreader:
        idlist.append(float(row[0]))
        if row[1] not in countylist:
            countylist.append(row[1])
        if row[2] not in candidatelist:   
            candidatelist.append(row[2])
        votelist.append(row[2])
        


cand1 = candidatelist[0]
cand2 = candidatelist[1]
cand3 = candidatelist[2]
cand4 = candidatelist[3]


for x in votelist:
    if x == cand1:
     cand1list.append(x)    
    elif x == cand2:
        cand2list.append(x)
    elif x == cand3:
        cand3list.append(x)
    elif x == cand4:
        cand4list.append(x)
    else:
        print("Candidate Not Found")



totalvote = len(idlist)
cand1total = len(cand1list)
cand2total = len(cand2list)
cand3total = len(cand3list)
cand4total = len(cand4list)
cand1perc = round((cand1total / totalvote) * 100, 3)
cand2perc = round((cand2total / totalvote) * 100, 3)
cand3perc = round((cand3total / totalvote) * 100, 3)
cand4perc = round((cand4total / totalvote) * 100, 3)
templist = [cand1total, cand2total, cand3total, cand4total]

if cand1total == max(templist):
    winner = cand1
elif cand2total == max(templist):
    winner = cand2
elif cand3total == max(templist):
    winner = cand3
elif cand4total == max(templist):
    winner = cand4


print(f"Election Results \n-------------------------------------- \n Total Votes: {totalvote} \n-------------------------------------- \n")
print(f"{cand1}: {cand1perc}% ({cand1total})")
print(f"{cand2}: {cand2perc}% ({cand2total})")
print(f"{cand3}: {cand3perc}% ({cand3total})")
print(f"{cand4}: {cand4perc}% ({cand4total})")
print(f"-------------------------------------- \n Winner: {winner} \n--------------------------------------")

    
output_file = os.path.join("election_reulsts.txt")


file = open("election_results.txt","w")
file.write("Election Results \n")
file.write("-------------------------------------- \n")
file.write("Total Votes:" + str(totalvote) + "\n")
file.write("--------------------------------------\n")
file.write("" + str(cand1) + ": "  + str(cand1perc) + "% "  + "(" + str(cand1total) + ")\n")
file.write("" + str(cand2) + ": "  + str(cand2perc) + "% "  + "(" + str(cand2total) + ")\n")
file.write("" + str(cand3) + ": "  + str(cand3perc) + "% "  + "(" + str(cand3total) + ")\n")
file.write("" + str(cand4) + ": "  + str(cand4perc) + "% "  + "(" + str(cand4total) + ")\n")
file.write("--------------------------------------\n" + "Winner: " + str(winner) + "\n--------------------------------------")
