#Import the os module and the module for reading CSV files
import os
import csv

#Create path to the budget data csv file
datapath = os.path.join('Resources','election_data.csv')

#open and read csv
with open(datapath, mode='r') as df:
    reader = csv.reader(df)
    
    #skip header
    next(df)

    #create variables
    totalvotes = 0                  #create variable for counting votes
    c1votes = 0
    c2votes = 0
    c3votes = 0
    c4votes = 0
    prev_val = None                 #previous value in array

    #create lists       
    candidates = []                 #for csv column "candidates"
    uniquecandidates = []           #for list of each unique candidate

    #loop through data
    for row in reader:
        totalvotes += 1                 #calc total number of votes
        candidates.append(row[2])       #fill list candidates (per vote)

        #loop through candidate column list
        for val in candidates:
            if val not in uniquecandidates:     #if candidate name is not in uniquecandidates list
                uniquecandidates.append(val)    #add the name to the list
    
    if row[2] == uniquecandidates[0]:
       c1votes += 1
    #if row[2] == uniquecandidates[1]:
    #   c2votes += 1
    #if row[2] == uniquecandidates[2]:
    #   c3votes += 1
    #if row[2] == uniquecandidates[3]:
    #   c4votes += 1
    print(c1votes)
#print(uniquecandidates[0])
#print(c1votes)

    #votetotals = {uniquecandidates[0]:c1votes, uniquecandidates[0]:c2votes}
    #print(votetotals)   
    
    #create a dictionary called castvotes that contains a
    #castvotes = {row[0]:row[1]}     #fill dictionary with voteid and candidate name
        
#with open(datapath) as datafile:
#    reader = csv.reader(datafile, delimiter=",")

    #skip header
#    next(datafile)

    #create variables 
#    votecount=0         #to count votes
    
    #for loop to read csv
#    for rows in csv.reader(df):
#        if rows[2] == uniquecandidates[0]:
#            c1votes += 1
#    print(c1votes)



#Print information to terminal and export text file with results
print(f"""
```
Election Results
-------------------------
Total Votes: {totalvotes}
-------------------------
: ()
Correy: ()
Li: ()
O'Tooley: ()
-------------------------
Winner:
-------------------------
```
""")

#save file to .bas in analysis folder
#with open('C:/Users/Joshua/Desktop/GT Bootcamp/gt-virt-data-pt-12-2021-u-c-master/03-Python/Homework/python--challenge/PyPoll/analysis/PyPollAnalysis.bas', 'w') as f:
#    f.write(f"""
#```
#Election Results
#-------------------------
#Total Votes: {totalvotes}
#-------------------------
#Khan: ()
#Correy: ()
#Li: ()
#O'Tooley: ()
#-------------------------
#Winner:
#-------------------------
#```
#""")