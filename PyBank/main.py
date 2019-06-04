#import the os module
import os

# Module for reading CSV files
import csv

csvpath = 'budget_data.csv'

#lists to store data
dates_list = []
profit_list = []

with open(csvpath, newline='') as csvfile:
        # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')

        # Read the header row first
        csv_header = next(csvreader)  

        #separating into two lists    
        for row in csvreader:
                dates_list.append(row[0])
                profit_list.append(row[1])

#finding total months
months_count = len(dates_list)

#changing list of str to list of int
profit_list = [int(i) for i in profit_list]

#adding all profits/losses
net_profit = sum(profit_list)

list_changes = [j-i for i, j in zip(profit_list[:-1], profit_list[1:])]
#we have dropped the last term from profit_list
#we have dropped the first term from profit_lst
#and subtracted the list without the last term from that without the first term
#to get a list of the changes
#profit_list[:-1] starts at jan-2010 but ends with jan-2017
#profit_list[1:] starts at feb-2010 and ends with feb-2017
#index of list_changes begins with 0 = from jan-2010 to feb 2010 (call feb change)
#so if max/min index is num, add 1 to num for appropriate index match in dates_list (where index 0 gives jan 2010)


#create average function for calculating average change
def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total / length

#finding greatest increase
greatest_increase = max(list_changes)
max_index = list_changes.index(greatest_increase)

#gives index of prior month so must adjust by adding one to get correct date

#finding greatest decrease
greatest_decrease = min(list_changes)
min_index = list_changes.index(greatest_decrease)

#print findings
print("Financial Analysis of Budget Data")
print("----------")
print(f"Total Months: {months_count}")
print(f"Total: ${net_profit}")
print(f"Average Change: ${round(average(list_changes),2)}")
print(f"Greatest Increase in Profits: {(dates_list[max_index + 1])} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {(dates_list[min_index +1])} (${greatest_decrease})")
print("----------")

#opening financial analysis in new text file
with open("Financial_Analysis.txt", "w") as text_file:
        print("Financial Analysis of Budget Data", file = text_file)
        print("----------", file = text_file)
        print(f"Total Months: {months_count}", file = text_file)
        print(f"Total: ${net_profit}", file = text_file)
        print(f"Average Change: ${round(average(list_changes),2)}", file = text_file)
        print(f"Greatest Increase in Profits: {(dates_list[max_index + 1])} (${greatest_increase})", file = text_file)
        print(f"Greatest Decrease in Profits: {(dates_list[min_index +1])} (${greatest_decrease})", file = text_file)
        print("----------", file = text_file)