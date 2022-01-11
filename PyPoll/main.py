#Import the os module and the module for reading CSV files
import os
import csv

#Create path to the budget data csv file
datapath = os.path.join('Resources','election_data.csv')

#open and read csv
with open(datapath, mode='r') as df:
    reader = csv.reader(df)

    next(df)            #skip header

    #create variables
    totalvotes = 0      #for counting votes
    c0votes = 0         #candidate 1's total votes
    c0percent = 0       #candidate 1's percent of total votes
    c1votes = 0         #candidate 2's total votes
    c1percent = 0       #candidate 2's percent of total votes
    c2votes = 0         #candidate 3's total votes
    c2percent = 0       #candidate 3's percent of total votes
    c3votes = 0         #candidate 4's total votes
    c3percent = 0       #candidate 4's percent of total votes

    #create lists       
    candidate = []      #list of each unique candidate
  
    #loop through data
    for row in reader:
        totalvotes += 1                #calc total number of votes
        if row[2] not in candidate:    #check if candidate name has been added to list
            candidate.append(row[2])   #fill list candidates (per vote)     
        if row[2] == candidate[0]:     #check if cand. name is candidate 1
            c0votes += 1               #tally candidate 1's votes
        elif row[2] == candidate[1]:   #candidate 2?
            c1votes += 1                #tally candidate 2's votes
        elif row[2] == candidate[2]:   #candidate 3?
            c2votes += 1                #tally candidate 3's votes
        elif row[2] == candidate[3]:   #candidate 4?
            c3votes += 1                #tally candidate 4's votes

#calculate each candidate's percent votes of total
c0percent = "{:.00%}".format(c0votes / totalvotes)      #candidate 1
c1percent = "{:.00%}".format(c1votes / totalvotes)      #candidate 2
c2percent = "{:.00%}".format(c2votes / totalvotes)      #candidate 3
c3percent = "{:.00%}".format(c3votes / totalvotes)      #candidate 4

#find who had the most votes
maxvotes = max(c0votes, c1votes, c2votes, c3votes)
if maxvotes == c0votes:
    maxcand = candidate[0]
elif maxvotes == c1votes:
    maxcand = candidate[1]
elif maxvotes == c2votes:
    maxcand = candidate[2]
elif maxvotes == c3votes:
    maxcand = candidate[3]
elif maxvotes == c4votes:
    maxcand = candidate[4]

#Print information to terminal and export text file with results
print(f"""
```
Election Results
-------------------------
Total Votes: {totalvotes}
-------------------------
{candidate[0]}: {c0percent} ({c0votes})
{candidate[1]}: {c1percent} ({c1votes})
{candidate[2]}: {c2percent} ({c2votes})
{candidate[3]}: {c3percent} ({c3votes})
-------------------------
Winner: {maxcand}
-------------------------
```
""")

#save file to .bas in analysis folder
with open('C:/Users/Joshua/Desktop/GT Bootcamp/gt-virt-data-pt-12-2021-u-c-master/03-Python/Homework/python--challenge/PyPoll/analysis/PyPollAnalysis.bas', 'w') as f:
    f.write(f"""
```
Election Results
-------------------------
Total Votes: {totalvotes}
-------------------------
{candidate[0]}: {c0percent} ({c0votes})
{candidate[1]}: {c1percent} ({c1votes})
{candidate[2]}: {c2percent} ({c2votes})
{candidate[3]}: {c3percent} ({c3votes})
-------------------------
Winner:
-------------------------
```
""")