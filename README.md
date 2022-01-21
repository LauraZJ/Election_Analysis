# Election_Analysis

## Purpose
The purpose of this exercise is to analyze the election results for three counties in a precinct.  To do this, we used Python to read and analyze the data in a CSV file and then print the results in a git bash terminal and write the results to a .txt file.

# Election Audit Results

## Total Votes
Total votes cast in this election:  369,711
    
To obtain the total votes, we first set the total_votes to 0 (not pictured below) and then used a for loop to go through each row and add each vote to the number of total_votes.

!["total votes image"](https://github.com/LauraZJ/Election_Analysis/blob/main/Resources/total_votes_code2.png)

### Vote count by County
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
!["County vote breakdown code"](https://github.com/LauraZJ/Election_Analysis/blob/main/Resources/county_vote_breakdown_code.png)
