import csv
import os

load_file = os.path.join("data", "election_results.csv")
save_file = os.path.join("data", "election_results.txt")

total_votes = 0

# Open election results and read read file
with open(load_file) as election_data:
    file_reader = csv.reader(election_data)

    # Read header row
    headers = next(file_reader)

    # Print each row in csv file
    for roe in file_reader:
        total_votes += 1

print(total_votes)