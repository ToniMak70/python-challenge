# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
Candidates = {}


# Winning Candidate and Winning Count Tracker
Winner = ""
max_votes = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
                   
        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        Candidate_name = row[2]
        
        # If the candidate is not already in the candidate list, add them
        if Candidate_name in Candidates:
            Candidates[Candidate_name] += 1
        else:
            Candidates[Candidate_name] = 1
                

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    print("Election Results" )
    print("---------------------------------------")
    print(f"Total Votes: {total_votes}")
    print("---------------------------------------")

    # Write the total vote count to the text file
    txt_file.write("Election Results\n")
    txt_file.write("-------------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")           
    txt_file.write("-------------------------------\n")

    # Loop through the candidates to determine vote percentages and identify the winner
    
        # Get the vote count and calculate the percentage
    Results = []

    for candidate, votes in Candidates.items():
        percentage = (votes / total_votes) *100
        Results.append((candidate, votes, percentage))

        # Update the winning candidate if this one has more votes
    for candidate, votes, percentage in Results:
        if votes > max_votes:
            max_votes = votes
            Winner = candidate
        print(f"{candidate}: {percentage:.2f}% ({votes})\n")
        txt_file.write(f"{candidate}:{percentage:.2f}% ({votes})\n")
      
    print("---------------------------------------")
    txt_file.write("-------------------------------\n")

    # Generate and print the winning candidate summary
    print(f"Winner: {Winner}")
    print("---------------------------------------")
    
    # Save the winning candidate summary to the text file
    txt_file.write(f"Winner: {Winner}\n")
    txt_file.write("-------------------------------\n")