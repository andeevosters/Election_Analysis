# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("/Users/andee/Desktop/Data_Analytics/Module_3/Homework/Election_Analysis/Resources/election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("/Users/andee/Desktop/Data_Analytics/Module_3/Homework/Election_Analysis/Analysis/election_analysis.txt")

#1. Initialize a total vote counter before the with open() statement.
total_votes = 0

#DECLARE LISTS, DICTIONARIES AND TRACKERS
#Candidate_options = [] by adding it before the with open() statement in our script.
candidate_options = []
# Declare candidate_votes dictionary using {}. To print the candidate vote dictionary, use code: print(candidate_votes). To get each name only once, the "if" statement needs to nest in the for loop.
candidate_votes = {}

# Track the winning candidate, vote count, and percentage.
    # Declare a variable that holds an empty string value for the winning candidate.
winning_candidate = ""
    # Declare a variable for the "winning count" equal to zero.
winning_count = 0
    # Declare a variable for the "winning_percentage" equal to zero.
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
            
        #2. Increment the total_votes by 1 after the for loop.
        total_votes += 1

        #2. Find the candidate name for each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            #3. Add it to the list of candidates.
            candidate_options.append(candidate_name)

            #2. Begin tracking that candidate's vote count, starting at 0.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

#OVERALL RESULTS SECTION
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    
    # Print the final vote count to the terminal.
    # Initiate election_results variable
    election_results = (
        f"\nElection Results\n"
        f"-----------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------------------\n")
    
    print(election_results, end="")
    # end="" signifies an empty string. It is added to ensure that nothing will be printed on the last last with/after the last result. Anything new will go on a new line.
    
    #Save the final vote count to the text file.
    txt_file.write(election_results)

    #CANDIDATE SECTION
    # # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
                            
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
                
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
                        
        # Initiate a variable for candidate results.
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's name, vote count, and percentage of votes to the terminal.
        print(candidate_results)

        #Save the candidate results to our text file. Note: this only works if this command is indented within the "with open" command. Otherwise, the file is closed.
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
                                
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    #WINNER SECTION
    #  Print out the winning candidate, vote count and percentage to terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
            
    print(winning_candidate_summary)

    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)