# Election_Analysis

## Purpose
The purpose of this exercise is to analyze the election results for three counties in a precinct.  To do this, we used Python to read and analyze the data in a CSV file and then print the results in a git bash terminal and write the results to a .txt file.

# Election Audit Results

## Total Votes
Total votes cast in this election:  369,711
    
To obtain the total votes, we first set the total_votes to 0 (not pictured below) and then used a for loop to go through each row and add each vote to the number of total_votes.

!["total votes image"](https://github.com/LauraZJ/Election_Analysis/blob/main/Resources/total_votes_code2.png)

## Vote count by County
The table below provides the number of votes cast in each county and identifies what percentage of the total election votes took place in each county.

    |-------------------------------------------|
    |             Votes by County               |
    |-------------------------------------------|
    | County    | Votes Cast  | % of Total Votes|
    |-------------------------------------------|
    | Jefferson |   38,855    |     10.5%       |
    |-------------------------------------------|
    | Denver    |  306,055    |     82.8%       |
    |-------------------------------------------|
    | Arapahoe  |   24,801    |      6.7%       |
    |-------------------------------------------|
    
To obtain these results, we had to retrieve the votes by county and then calculate the percentage using the code below.

!["County vote breakdown code"](https://github.com/LauraZJ/Election_Analysis/blob/main/Resources/county_vote_breakdown_code2.png)


## Largest County Turnout
Denver County had the largest number of votes cast with 306,055 votes.

!["County Votes"](https://github.com/LauraZJ/Election_Analysis/blob/main/Resources/county_vote_breakdown.png)

We can see in the output (above) that Denver had the largest turnout. However, the following code was used to retrieve and print/write that directly from the data:

!["Winning_county_code"](https://github.com/LauraZJ/Election_Analysis/blob/main/Resources/winning_candidate_code.png)

## Tabulation of Candidate Votes:
This precinct had three candidates.  The results for each candidate are:

!["Candidate votes"](https://github.com/LauraZJ/Election_Analysis/blob/main/Resources/Candidate_votes2.png)

This required the use of a for loop to identify the candidates in each row and add to the vote count for each occurrence of the candidate in the data.  The next step was to calculate the percentage of total votes the candidate received.

!["county_vote_count_code"](https://github.com/LauraZJ/Election_Analysis/blob/main/Resources/candidate_vote_count_code.png)

In the last three lines of the code (above), we have asked to print to the terminal and written to the .txt file. See the terminal output below

!["candidate_count_terminal"](https://github.com/LauraZJ/Election_Analysis/blob/main/Resources/candidate_count_terminal.png)

## Winner Declared!
Diana DeGette wins the election with 73.8% of the votes (272,892).  We used a process similar to the one we used to identify the county with the largest number of votes to clarify the winner of this election.

!["Winning candidate code"](https://github.com/LauraZJ/Election_Analysis/blob/main/Resources/winning_candidate_code.png)

!["Winning Candidate Readour"](https://github.com/LauraZJ/Election_Analysis/blob/main/Resources/winning_candidate_readout.png)


# Election Audit Summary

The automated audit of this election data was made possible with the use of this code.  While it took some time to write the code, (a task that would have been faster if done by someone with more experience), it took just moments to get the results. 

The great thing about this code is that with some modifications, it could be used for a national election by replacing all county references with states.


Also, it would be a bit more complex to do, but if the election data were to include election results for more than one position or role, we could insert a for loop earlier in the code to abstract the data by role, then run the analysis get the winner for each role.

