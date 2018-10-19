# Import modules and csv path
import os
import pandas as pd

file = "Resources/budget_data.csv"

# Read the csv file
budget = pd.read_csv(file)

# Calculate the total number of months in the dataset
month_count = budget["Date"].count()

# Calculate the total net amount of "Profit/Losses" over the entire period
net_profit = budget["Profit/Losses"].sum()

# Calculate the greatest increase in profits (date and amount) over the entire period
max_profit = budget["Profit/Losses"].max()
df_max = budget[budget['Profit/Losses']== max_profit]
max_date = df_max['Date'].to_string(index=False, header=False)
max_profit = df_max['Profit/Losses'].to_string(index=False, header=False)

# Calculate the greatest decrease in losses (date and amount) over the entire period
min_profit = budget["Profit/Losses"].min()
df_min = budget[budget['Profit/Losses']==min_profit]
min_date = df_min['Date'].to_string(index=False, header=False)
min_profit = df_min['Profit/Losses'].to_string(index=False, header=False)

#Print to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${net_profit}")
print(f"Greatest Increase in Profits: {max_date} (${max_profit})")
print(f"Greatest Decrease in Profits: {min_date} (${min_profit})")

#Export text file
with open("Output.txt", "w") as text_file:
    print("Financial Analysis",file=text_file)
    print("----------------------------",file=text_file)
    print(f"Total Months: {month_count}",file=text_file)
    print(f"Total: ${net_profit}",file=text_file)
    print(f"Greatest Increase in Profits: {max_date} (${max_profit})",file=text_file)
    print(f"Greatest Decrease in Profits: {min_date} (${min_profit})",file=text_file)