# Dependencies
import os
import pandas as pd

# Filepath and read file
file = "Resources/election_data.csv"
election_data = pd.read_csv(file)

# Calculate total votes cast
vote_count = election_data['Voter ID'].count()

# Create vote count dataframe with candidate name and total votes
votes = election_data["Candidate"].value_counts()
votes_df = pd.DataFrame(votes)
votes_df = votes_df.reset_index()

# Add vote percentage to dataframe, rename headers, and organize columns
vote_pct = round(votes_df["Candidate"]/vote_count*100,4)
votes_df["Vote Percentage"]= vote_pct

votes_df = votes_df.rename(columns = {"index":"Candidate Name","Candidate":"Candidate Vote Count"})
results_df = votes_df[["Candidate Name","Vote Percentage","Candidate Vote Count"]]

# Find and define winner
winner_count = results_df["Candidate Vote Count"].max()
winner_df = results_df[results_df["Candidate Vote Count"]==winner_count]
winner = winner_df["Candidate Name"].to_string(index=False,header=False)

# Print to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {vote_count}")
print("-------------------------")
for x in range(len(results_df.index)):
    print(f"{results_df.iloc[x,0]}: {results_df.iloc[x,1]}% ({results_df.iloc[x,2]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Print to text file
with open("Output.txt", "w") as text_file:
    print("Election Results",file=text_file)
    print("-------------------------",file=text_file)
    print(f"Total Votes: {vote_count}",file=text_file)
    print("-------------------------",file=text_file)
    for x in range(len(results_df.index)):
        print(f"{results_df.iloc[x,0]}: {results_df.iloc[x,1]}% ({results_df.iloc[x,2]})",file=text_file)
    print("-------------------------",file=text_file)
    print(f"Winner: {winner}",file=text_file)
    print("-------------------------",file=text_file)