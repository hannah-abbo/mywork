# -*- coding: utf-8 -*-
"""
DS2001 (S23-Matherly) Week 4

@author: [Hannah Abbo]
"""
"""
In this week's exercise, we're going to write an app that reads in receipts
from files which are in a specific format. As in last week's assignment, we'll
be assigning amounts categories, but some are new this week.

Here are the categories:
TR - Transportation
FO - Food
CL - Clothing
PE - Personal
ME - Medical

For each receipt read in from a file, each line contains the type of expense
and the amount in the following format, with two letter codes to identify the
expense type, three spaces, and then the amount.
    
TR   28.00
FO   8.90
CL   45.00
PE   12.95
ME   260.00


There are ten days worth of receipts in the files:
    day01.txt
    day02.txt
    ...
    day10.txt
    
"""
import matplotlib.pyplot as plt 
 
 # create a list with the 10 file names, each as strings, i.e. "day01.txt"
 # The file list is a constant, so put it above the main function definition

FILE_NAMES = ["day01.txt", "day02.txt", "day03.txt","day04.txt","day05.txt",
              "day06.txt","day07.txt","day08.txt","day09.txt","day10.txt"]

def main():
    
# Q1:  

    # ask user's name and greet them 
    name = input("What is your name?\n")
    print("Welcome,", name)
    
    # Initialize empty lists for each type of expense
    TR = []
    FO = []
    CL = []
    PE = []
    ME = []
    
    # Initialize three other lists that will track the daily total expense,
    # the daily total number of items, and the single most expensive item that day
    daily_total_exp = []
    daily_total_items = []
    most_exp_item = []
    

# Q2: Write a for loop to iterate over the file names in the file list
    # Print out which file is being processed

    for file in FILE_NAMES:
        print("\rProcessing: ", file, end="")
        daily_receipts = []
        with open(file, "r") as infile:
            while True: 
                temp = infile.readline().strip()
                # Create an empty list to track the daily receipts, so that we can figure out 
                # the total/count/maximum once all of the file has been read in
             
                # Q3: Within the file processing loop, after reading in the line,
                # separate each line into two parts using list slicing, and assign them
                # to variables for the type and amount of the receipt
                expense_type = temp[0:2]
                print(expense_type)
                   
                amount = temp[5:]
                print(amount)
                
                # Then use if statements to identify the type of the expense, 
                # and append it to the appropriate list
                if expense_type == "TR": 
                    TR.append(amount)
                elif expense_type == "FO":
                    FO.append(amount)
                elif expense_type == "CL":
                    CL.append(amount)
                elif expense_type == "PE":
                    PE.append(amount)
                else:
                    ME.append(amount)
                
                daily_receipts.append(amount)
                
    
                # Within the for loop, open the file, then read in each line 
                # until the EOF
                if not temp: 
                    break 
    
    
# Q4: After the file processing is done:
    # - total up the daily receipts and add this to the daily total list
    # - get the length of the daily receipts and add it to the daily count list
    # - get the maximum amount and add that to the daily max list
    daily_total_exp.append(sum(daily_receipts))
    daily_total_items.append(len(daily_receipts))
    most_exp_item.append(max(daily_receipts))
    
# Q5: Let's do the require calculations.
# Create a new list to store the percentages by category, and then append
# each percentage to it
    percentages = []
    
# Then, calculate the daily average expenditure.
# How can you calculate the average? You need to divide every element in the
# daily list by every element in the daily count list. Think about using a 
# for loop and an incrementing counter together...



# Q6: Let's prepare the report.
# First, show them their overall average daily expenditure
# Then show the percentage they spent on each category.
# Finally, let's prepare some visualizations of the data.
# Make a bar chart showing the overall percentages. 
# plt.bar needs three arguments, which can be list:
# - x, the x position of the bars,
# - height, the height of the bars (in our case, the percentages)
# - tick_label, the labels the bars will have on the x-axis
# Make one line chart showing the daily totals, daily max and daily average
# Don't forget to put labels on the axes!

    
    
main()