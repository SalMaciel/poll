import csv
import os

load_file = os.path.join("data", "election_results.csv")
save_file = os.path.join("data", "election_results.txt")

total_votes = 0

candidate_options = []

# Open election results and read read file
with open(load_file) as election_data:
    file_reader = csv.reader(election_data)

    # Read header row
    headers = next(file_reader)

    # Print each row in csv file
    for row in file_reader:

        total_votes += 1
        
        # Print the candidate name from each row
        candidate_name = row[2]

        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

print(candidate_options)