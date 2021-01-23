# Election_Analysis
We were asked by an empoloyee of the Colorado Board of Elections to audit a recent congressional election, in two separate phases: candidate results and county results.

## Phase 1: Candidate Results
### Project Overview 
In the first phase of the election analysis, we were asked to perform the following tasks:
1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

### Project Summary
The analysis of the election shows that:
- There were 369,711 votes cast in the election.
- There were three(3) candidates:
    - Charles Casper Stockham
    - Diana DeGette 
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
    - Diana DeGette received 73.8% of the vote and 272,892 votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.
- The winner of the election was:
    - Diana DeGette, who received 73.8% of the vote and 272,892 votes.

## Phase 2: County Results
### Challenge Overview 
Once we provided the CBE could benefit from expanding 
with the candidate results, they asked us to perform a similar analysis, this time regarding votes cast by county. Using the same dataset, the second analysis included the following:
1. The voter turnout for each county.
2. The percentage of votes from each county out of the total count.
3. The county with the highest voter turnout.

### Challenge Summary
The analysis of the election (369,711 votes cast) shows that:
- Three(3) counties were analyzed:
    - Jefferson 
    – Denver 
    – Arapahoe 
- Each county had the following number and percentage of overall votes:
    - Jefferson County cast 38,555 votes, or 10.5%.
    – Denver cast 306,055 votes, or 82.8%.
    – Arapahoe County cast 24,801 votes, or 6.7%.
- The county with the highest votes cast was:
    - Denver, with 306,055 votes cast, or 82.8% of the 368,711 votes.

## Election Audit: Summary
The Colorado Board of Elections has the critical information they need to certify Diana Degette as the winner of the election and identify Denver as the majority location for votes being cast in this election. See below for complete results.

![Election_results.png](https://github.com/andeevosters/Election_Analysis/blob/main/Resources/Election_results.png)

### Further Analysis Potential 
We recommend the CBE take advantage of the existing script by having us modify it to perform a deeper analysis that could help them draw elections conclusions from a macro lens (statewide results) down to a micro lens, including some of the following examples:
- Add statewide results in order to compare all of the counties
– Compare counties to counties, and cities to cities (ex. Denver falls in three counties, and is not a county in itself)
– Which candidates were voted for in each county
– The number and percentage of votes for each candidate by county
– The winning candidate for each county
– The winning county for each candidate
– It could be sold to a Board of Elections in other states

## Resources
– Data Source: election_results.csv

– Software: Python 3.8.5, Visual Studio Code, 1.52.1
