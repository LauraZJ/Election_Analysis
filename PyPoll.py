# Add our dependencies
import os
import csv

# Assign a variable to load the file from a path.
file_to_load = os.path.join("resources", "election_results.csv")

# assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#  To do:  read and analyze the data here.

# Open the election results and read the file.
with open(file_to_load) as election_data:
    
#read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    # read and print the header row
    headers = next(file_reader)
    print(headers)
    
 
#using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, "w") as txt_file:

# write some data to file.
    txt_file.write("Counties in the Election\n--------------------\nArapahoe\nDenver\nJefferson")
        


# 1. The total number of votes cast
# 2. The complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. the winner of the election based on popular vote.
