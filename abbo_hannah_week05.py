"""
In this week's exercise, we're going to finish our app that reads in receipts.
You should reuse the code from last week for Q1-3.

This week, we'll add data from each day to the daily summaries, specifically:
    - Sum up all the receipts for the day then add to the daily total list
    - Get the number of expenses for each day and add to the daily count list
    - Get the daily maximum amount and add that to the daily max list
Then, we'll calculate percentages by category and the daily average, and 
prepare a report for the user summarizing the information and presenting it in
bar and line charts.


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
                if not temp:
                    # Q4: After processing the file for each days 
                    # (but within the file list loop)
                    # - total up the daily receipts and add this to 
                    # the daily total list
                    ## Use the sum() function to get the total of all values in the list
                    # - get the length of the daily receipts and add it to the 
                    # daily count list
                    ## Use the len() function to get the number of items in a list
                    # - get the maximum amount and add that to the daily max list
                    ## Use the max() function to get the maximum value in a list

                    daily_total_exp.append(sum(daily_receipts))
                    daily_total_items.append(len(daily_receipts))
                    most_exp_item.append(max(daily_receipts))
                    break 
                
                # Create an empty list to track the daily receipts, so that we can figure out 
                # the total/count/maximum once all of the file has been read in
             
                # Q3: Within the file processing loop, after reading in the line,
                # separate each line into two parts using list slicing, and assign them
                # to variables for the type and amount of the receipt
                
                expense_type = temp[0:2]
                # print(expense_type)
                amount = float(temp[5:])
                # print(amount)
                
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
    
       
    # Q5: After processing all the files and outside the file list loop, 
    # let's do the required calculations.
    # Create a new list to store the percentages by category, and then append
    # each percentage to it
    # Then, calculate the daily average expenditure.
    # How can you calculate the average? You need to divide every element in the
    # daily list by every element in the daily count list. Think about using a 
    # for loop and an incrementing counter together...
    
    # Calculate the percentage of each category
    
    percentages = []
    #print(daily_total_exp)
    percentages.append(sum(TR) / sum(daily_total_exp))
    percentages.append(sum(FO) / sum(daily_total_exp))
    percentages.append(sum(CL) / sum(daily_total_exp))
    percentages.append(sum(PE) / sum(daily_total_exp))
    percentages.append(sum(ME) / sum(daily_total_exp))


    for i in range(len(daily_total_exp)):
        averages = daily_total_exp[i] / daily_total_items[i]
        
   
    # Q6: Let's prepare the report.
    # First, show them their overall average daily expenditure
    print("Your overall average expenditure is", round(averages, 2))
    # Then show the percentage they spent on each category.
    perc_TR = percentages[0]
    print("Your Transportation percentage is... ", perc_TR)
    perc_FO = percentages[1]
    print("Your Food percentage is... ", perc_FO)
    perc_CL = percentages[2]
    print("Your Clothes percentage is... ", perc_CL)
    perc_PE = percentages[3]
    print("Your Personal percentage is... ", perc_PE)
    perc_ME = percentages[4]
    print("Your Medical percentage is... ", perc_ME)
    
    # Finally, let's prepare some visualizations of the data.
    # Make a bar chart showing the overall percentages. 
    # plt.bar needs three arguments, which can be list:
    # - x, the x position of the bars,
    # - height, the height of the bars (in our case, the percentages)
    # - tick_label, the labels the bars will have on the x-axis
    plt.bar(x = list(range(5)),
            tick_label = ["TR", "FO", "CL", "PE", "ME"], 
            height = percentages)
    plt.show()
    
    
    # Make one line chart showing the daily totals, daily max and daily average
    # Don't forget to put labels on the axes!
    plt.axhline(averages, color = "orange")
    plt.plot(daily_total_exp, color = "blue")
    plt.plot(most_exp_item, color = "purple")
    
    plt.legend(["Avg Daily Amt", "Daily Total", "Daily Max"], ncol = 1)
    plt.xlabel("Number of Days")
    plt.ylabel("Amount ($)")
    plt.show()
    

main()
