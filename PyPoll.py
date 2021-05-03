#The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize total vote counter
total_votes = 0
# Candidate Options
candidate_options = []
# Declare Empty dictionary
candidate_votes = {}
# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)
    # Read the header row
    headers = next(file_reader)
    #Print each row in CSV
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1
        # Print candidate name from each row
        candidate_name = row[2]
        # If candidate does not match existing candidate
        if candidate_name not in candidate_options:
            # Add candidate name to candidate list
            candidate_options.append(candidate_name)
            # Begin tracking candidates' votes
            candidate_votes[candidate_name] = 0
        # Add a vote to candidates' count
        candidate_votes[candidate_name] += 1
# Determine percentage of votes
# Iterate through list 
for candidate_name in candidate_votes:
    # Retrieve vote count
    votes = candidate_votes[candidate_name]
    # Calculate percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100
    # Print candidate name,vote count, and percentage
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and winning candidate
    # Determine if votes are greater than winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # if true, set them equal
        winning_count = votes
        winning_percentage = vote_percentage
        # set winning candidate's name
        winning_candidate = candidate_name
# Print summary
winning_candidate_summary = (
    f"------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"------------------------\n")
print(winning_candidate_summary)
