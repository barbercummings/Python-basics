#import the os module
import os

# Module for reading CSV files
import csv

#import counter
from collections import Counter

csvpath = 'election_data.csv'

#lists to store data
id_list = []
county_list = []
candidate_list = []

with open(csvpath, newline='') as csvfile:
        # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')

        # Read the header row first
        csv_header = next(csvreader)  

        #separating into two lists    
        for row in csvreader:
                id_list.append(row[0])
                county_list.append(row[1])
                candidate_list.append(row[2])

#finding total number of votes
votes_count = len(id_list)

#finding list of candidates
candidate_names = list(set(candidate_list))

#print findings
print("Election Results")
print("----------")
print(f"Total Votes: {votes_count}")
print("----------")

#loop through each name and print count and percent
for name in candidate_names:
        name_num = candidate_list.count(name)
        name_percent = "{:.3%}".format(name_num / votes_count)
        print(f"{name}: {name_percent} ({(name_num)})")

print("----------")

#finding a winner

print(f"Winner: {max(set(candidate_list), key=candidate_list.count)}")
print("----------")