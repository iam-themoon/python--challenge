#Import the os module and the module for reading CSV files
import os
import csv

#Create path to the budget data csv file
csv_path = os.path.join('Resources','budget_data.csv')

#open and read csv
with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #skip header
    next(csv_file)

    #create variables 
    rowcount=0          #to count rows
    netamount = 0       #to sum the P/L
    averagechange = 0   #avg change
    greatestinc = 0     #greatest increase
    greatestdec = 0     #greatest decrease
    prev_val = None     #previous value in array 

    #create arrays 
    months = []         #for all month values
    permonth = []       #for all P/L per month
    changes = []        #for the monthly changes

    #for loop to read csv
    for row in csv.reader(csv_file):
        rowcount += 1                   #count rows
        netamount += int(row[1])        #calculate sum of all P/L
        months.append(str(row[0]))       #populate month array with month values
        permonth.append(int(row[1]))    #populate permonth array with the P/L values as integers 
    
    #insert None value into start of changes array, to make it equal length as others 
    changes.insert(0,0)

    #loop through permonth array
    for val in permonth:
        if prev_val is not None:    #if it's not the first row
            diff = val - prev_val   #set diff equal to current value minus previous value
            changes.append(diff)    #populate the changes array with the monthly change values    
        prev_val = val              #set prev_val to current value (and then move to next)
    
    #find the average change by summing the changes and dividing by the number of changes
    averagechange = sum(changes) // len(changes)
    
    #find the greatest increase and decrease 
    greatestinc = max(changes)
    greatestdec = min(changes)
    
    #find the index number for above values, used to reference the corresponding month values
    incindex = changes.index(greatestinc)
    decindex = changes.index(greatestdec)

#Print information to terminal and export text file with results
print(f"""
```
Financial Analysis
----------------------------
Total Months: {rowcount}
Total: ${netamount}
Average Change: ${averagechange}
Greatest Increase in Profits: {months[incindex]} $({greatestinc})
Greatest Decrease in Profits: {months[decindex]} $({greatestdec})
```
""")

#save file to .bas in analysis folder
with open('C:/Users/Joshua/Desktop/GT Bootcamp/gt-virt-data-pt-12-2021-u-c-master/03-Python/Homework/python--challenge/PyBank/analysis/PyBankAnalysis.bas', 'w') as f:
    f.write(f"""
```
Financial Analysis
----------------------------
Total Months: {rowcount}
Total: ${netamount}
Average Change: ${averagechange}
Greatest Increase in Profits: {months[incindex]} $({greatestinc})
Greatest Decrease in Profits: {months[decindex]} $({greatestdec})
```
""")