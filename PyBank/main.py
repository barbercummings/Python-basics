#import the os module
import os

# Module for reading CSV files
import csv

csvpath = 'budget_data.csv'

# Calculating The Data
#def print_data(bank_data):

        #Defining Variables
        #month = str(bank_data[0])
        #profit = int(bank_data[1])

#lists to store data
dates_list = []
profit_list = []


with open(csvpath, newline='') as csvfile:
        # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')

        # Read the header row first
        csv_header = next(csvreader)
        #print(f"CSV Header: {csv_header}")       

        for row in csvreader:
                dates_list.append(row[0])
                profit_list.append(row[1])


months_count = len(dates_list)

#changing list of str to list of int
profit_list = [int(i) for i in profit_list]

net_profit = sum(profit_list)

list_changes = [j-i for i, j in zip(profit_list[:-1], profit_list[1:])]
#we have dropped the last term from profit_list and subtracted from profit_list without the first term
#profit_list[:-1] starts at jan-2010 but ends with jan-2017
#profit_list[1:] starts at feb-2010 and ends with feb-2017
#index of list_changes begins with 0 = from jan-2010 to feb 2010 so call index 0 feb change

def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total / length

greatest_increase = max(list_changes)

max_index = list_changes.index(greatest_increase)

#gives index of prior month so must adjust by adding one to get correct date

greatest_decrease = min(list_changes)

min_index = list_changes.index(greatest_decrease)

print("Financial Analysis of Budget Data")
print("----------")
print(f"Total Months: {months_count}")
print(f"Total: ${net_profit}")
print(f"Average Change: ${round(average(list_changes),2)}")
print(f"Greatest Increase in Profits: {(dates_list[max_index + 1])} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {(dates_list[min_index +1])} (${greatest_decrease})")
print("----------")

