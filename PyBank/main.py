#import the os module
import os

# Module for reading CSV files
import csv

csvpath = 'budget_data.csv'

# Calculating The Data
def print_data(bank_data):

        #Defining Variables
        month = str(bank_data[0])
        profit = int(bank_data[1])

# Total number of months
months_count = 0



with open(csvpath, newline='') as csvfile:

     # CSV reader specifies delimiter and variable that holds contents
     csvreader = csv.reader(csvfile, delimiter=',')

     print(csvreader)

     # Read the header row first (skip this step if there is now header)
     csv_header = next(csvreader)
     print(f"CSV Header: {csv_header}")

     Data_list = list(csvreader)

     # Read each row of data after the header

     for row in Data_list:
                months_count += 1
print(f"Total Months: {months_count}")


