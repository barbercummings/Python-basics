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
print(candidate_names)

#finding percent and number of votes per candidate
#Khan
khan_num = candidate_list.count('Khan')
khan_percent = khan_num / votes_count
print(khan_percent)

#Correy
correy_num = candidate_list.count('Correy')
correy_percent = correy_num / votes_count
print(correy_percent)

#Li
li_num = candidate_list.count('Li')
li_percent = li_num / votes_count
print(li_percent)

#O'Tooley
otooley_num = candidate_list.count('O\'Tooley')
otooley_percent = otooley_num / votes_count
print(otooley_percent)

#finding a winner

print(max(set(candidate_list), key=candidate_list.count))


#print findings
print("Election Results")
print("----------")
print(f"Total Results: {votes_count}")
print("----------")
