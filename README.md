# python--challenge
This is the repository for HW 3 - "Py Me Up, Charlie"

With in this repository there are two main folders - PyBank and PyPoll.

In the PyBank folder there is a main.py file that will iterate through the budget_data.csv file in the Resources folder. The code will read through the csv data and extract some financial analysis:
    The total number of months represented 
        (by counting all rows)
    The total amount of profits and losses summed together 
        (summing all values in the P/L row)
    The average change from month to month 
        (by finding the difference between the previous row and the current row, appending each difference value to a list)
    And the greatest increase and greatest decrease in profits by month 
        (found by taking the max and min of the monthly changes and finding their corresponding months)
    The code then prints this analysis to the terminal and to a .bas file to the "analysis" folder.

In the PyPoll folder there are all the same elements, except for the data file (election_data.csv) in the Resources folder. The code will read through the csv data and extract some financial analysis:
    The total number of votes cast 
        (by counting all rows)
    The name of each individual candidate 
        (by adding each unique value to a list)
    The total number of votes cast  for each candidate 
        (by checking if "candidate" value is candidate 1, adding one for each time they come up)
    The percentage of the total number of votes that each candidate received
        (their number of votes divided by the total)
    The candidate with the most votes 
        (by checking if the maximum number of votes equal each candidate's number of votes)
