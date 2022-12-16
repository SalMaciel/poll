import csv
import os

load_file = os.path.join("data", "elections_results.csv")
save_file = os.path.join("data", "elections_results.txt")

# Open election results and read read file
with open(load_file) as election_data:
    file_reader = csv.read(election_data)

    # Read header row
    headers = next(file_reader)

    # Print each row in csv file
    for roe in file_reader:
        print(row)