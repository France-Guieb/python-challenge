# import os module
import os

# module for reading csv files
import csv

file = os.path.join('Resources', 'election_data.csv')

voters = []
candidates = []
otooley = "O'Tooley"

with open(file) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    
    # first row is header
    csv_header = next(csv_reader)

    # read each row of data below the header
    for row in csv_reader:       
        # count all voters
        voters.append(row[0])

        # put all votes in a list
        candidates.append(row[2])

# get the total number of votes
total_votes = len(voters)

# count each candidate's votes and percentage
khan_votes = candidates.count("Khan")
khan_percent = "{:.3%}".format(khan_votes/total_votes)

correy_votes = candidates.count("Correy")
correy_percent = "{:.3%}".format(correy_votes/total_votes)

li_votes = candidates.count("Li")
li_percent = "{:.3%}".format(li_votes/total_votes)

otooley_votes = candidates.count(otooley)
otooley_percent = "{:.3%}".format(otooley_votes/total_votes)

# summarise results candidates vs percentage votes
all_candidates = ["Khan", "Correy", "Li", otooley]
percent_votes = [khan_percent, correy_percent, li_percent, otooley_percent]

def my_max(percent_votes):
    value = percent_votes[0]
    for x in percent_votes:
        if x > value:
            value = x
    return value

leading = my_max(percent_votes)
winner = all_candidates[percent_votes.index(leading)]

# set variable for output file
output_file = os.path.join("results.csv")

details = [total_votes, khan_percent, khan_votes, correy_votes, correy_percent, li_votes, li_percent, otooley, otooley_votes, otooley_percent, winner]

# summary / final report
print("Election Results")
print("-------------------------")
print("Total Votes:", total_votes)
print("-------------------------")
print(f'Khan: {khan_percent} ({khan_votes})')
print(f'Correy: {correy_percent} ({correy_votes})')
print(f'Li: {li_percent} ({li_votes})')
print(f'{otooley}: {otooley_percent} ({otooley_votes})')
print("-------------------------")
print(f'Winner: {winner}')
print("-------------------------")

#  Open the output file
with open(output_file, "w", newline ='') as datafile:
    csv_writer = csv.writer(datafile, delimiter=",")
    
    csv_writer.writerow(["Election Results"])
    csv_writer.writerow(["-------------------------"])
    csv_writer.writerow(["-------------------------"])
    csv_writer.writerow(["-------------------------"])

# can't writerow variables
