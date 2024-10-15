# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
Months = []
Profit_Losses = []
Profit_Loss_Changes = []

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

# Track the total and net change
    # Process each row of data
    for row in reader:
        Months.append(row[0])
        Profit_Losses.append(int(row[1]))
        
    # Track the total
    Total_Months = len(Months)
    Net_Total = sum(Profit_Losses)

    # Track the net change
    for i in range(1, len(Profit_Losses)):
        Profit_Loss_Changes.append(Profit_Losses[i] - Profit_Losses[i-1])

    # Calculate the average net change across the months
    Average_Change = sum(Profit_Loss_Changes) / len(Profit_Loss_Changes)

    # Calculate the greatest increase in profits (month and amount)
    Greatest_Increase = max(Profit_Loss_Changes)
    Greatest_Increase_Month = Months[Profit_Loss_Changes.index(Greatest_Increase)+1]

    # Calculate the greatest decrease in losses (month and amount)
    Greatest_Decrease = min(Profit_Loss_Changes)
    Greatest_Decrease_Month = Months[Profit_Loss_Changes.index(Greatest_Decrease)+1]
      
    
# Generate the output summary
    # Print the output
    print("Financial Analysis")
    print("--------------------------")
    print(f"Total Months: {Total_Months}")
    print(f"Total: ${Net_Total}")
    print(f"Average Change: ${Average_Change:.2f}")
    print(f"Greatest Increase in Profits: {Greatest_Increase_Month} (${Greatest_Increase})")
    print(f"Greatest Decrease in Profits: {Greatest_Decrease_Month} (${Greatest_Decrease})")


    # Write the results to a text file
    with open(file_to_output, "w") as txt_file:
        txt_file.write("Financial Analysis\n")
        txt_file.write("-----------------------\n")
        txt_file.write(f"Total Months: {Total_Months}\n")
        txt_file.write(f"Total: ${Net_Total}\n")
        txt_file.write(f"Average Change: ${Average_Change:.2f}\n")
        txt_file.write(f"Greatest Increase in Profits: {Greatest_Increase_Month} ${Greatest_Increase}\n")
        txt_file.write(f"Greatest Decrease in Profits: {Greatest_Decrease_Month} ${Greatest_Decrease}\n")
