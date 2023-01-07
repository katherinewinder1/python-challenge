import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")
total_votes = 0
percentage_of_votes = {}
candidates = {}


with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    for row in csvreader:
        total_votes += 1
        if row[2] not in candidates:
            candidates[row[2]] = 1
        if row[2] in candidates:
            candidates[row[2]] = candidates[row[2]] + 1
    for name in candidates:
        percentage_of_votes[name] = round(candidates[name] / total_votes * 100, 3)

winner = (max(candidates, key=candidates.get))


keys = list(candidates)
print("Election Results")
print("-------------------------")
print(f"Total Votes: {str(total_votes)}")
print("-------------------------")
for key_names, value_names in candidates.items():
    print(f"{key_names}: {percentage_of_votes[key_names]}% ({value_names})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export text file
text_file = "output.txt"
with open(text_file,"w") as file:
    keys = list(candidates)
    file.write("Election Results")
    file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    file.write(f"Total Votes: {str(total_votes)}")
    file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    for key_names, value_names in candidates.items():
        file.write(f"{key_names}: {percentage_of_votes[key_names]}% ({value_names})")
    file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    file.write(f"Winner: {winner}")
    file.write("\n")
    file.write("-------------------------")