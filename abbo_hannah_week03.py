"""
DS2001 (S23-Matherly) Week 3
@author: [Hannah Abbo]
"""

"""
In this week's exercise, we're going to write an app that helps users manage
a budget. For the previous week, they will enter receipts for expenses
in each of five categories. 

Housing
Transportation
Food
Clothing
Personal

"""

import matplotlib.pyplot as plt 

def main():

    # ask user's name and greet them 
    name = input("What is your name?\n")
    print("Welcome,", name)
    
    # initialize variables for the different categories
    housing = 0
    transportation = 0
    food = 0
    clothing = 0
    personal = 0
        
    """
    Q2:
    Set up a control structure that uses a while loop to keep repeating until
    the user has gone through seven days. Remember to set the day variable
    outside of the control structure to the initial value.
    
    Inside, initialize variables to hold the daily values for each category, 
    and then nest a second control structure to allow users to keep entering 
    receipts until they indicate they are done. Create a variable called 'done'
    that will be used to track whether or not the user is done entering
    receipts.
    
    """
    # use while loop to ask people for 7 days' receipts
    day = 1 
    while day <=7 :
        d_housing = 0
        d_transportation = 0 
        d_food = 0 
        d_clothing = 0 
        d_personal = 0 
    
            
        # create another while loop inside a while loop. users can enter as many 
        # receipts as they want 
        done = "n"
        while done == "n":
            print("It's day", day)
            choice = int(input("What type of expense will you be recording?\n"
                                "1. Housing\n2. Transportation\n3. Food\n4. Clothing\n5. Personal\n"))
            amount = float(input("Enter the amount of the receipt for that expense\n"))
        
        # use control structure to add amount that was entered to the appropiate
        # variable for the daily values for each category 
        
            if choice == 1: 
                d_housing = d_housing + amount 
            elif choice == 2: 
                d_transportation = d_transportation + amount  
            elif choice == 3: 
                d_food = d_food + amount 
            elif choice == 4: 
                d_clothing = d_clothing + amount 
            elif choice == 5: 
                d_personal = d_personal + amount 
        
            done = input("Are you done entering receipts? (Y/N)\n").strip().lower()
        
        # create new variables for the overall totals
        housing = d_housing + housing
        transportation = d_transportation + transportation 
        food = d_food + food 
        clothing = d_clothing + clothing 
        personal = d_personal + personal 
        
        # plot the daily data in a scatterplot
        plt.scatter(day, d_housing, color = "blue")
        plt.scatter(day, d_transportation, color = "orange")
        plt.scatter(day, d_food, color = "green")
        plt.scatter(day, d_clothing, color = "red")
        plt.scatter(day, d_personal, color = "purple")
        
        # end the loop 
        day = day + 1
       
        # add labels and legend
    plt.xlabel("Day")
    plt.ylabel("Amount")
    plt.legend(["Housing", "Transporation", "Food", "Clothing", "Personal"]) 
        
        # draw a bar plot with the compiled receipts for each category 
    fig, ax = plt.subplots()
    ax.bar(1, housing, label = "Housing")
    ax.bar(2, transportation, label = "Transportation")
    ax.bar(3, food, label = "Food")
    ax.bar(4, clothing, label = "Clothing")
    ax.bar(5, personal, label = "Personal")
        
        # add legend and labels 
    ax.legend()
    ax.set_xlabel('')
    ax.set_ylabel('Dollars')
    ax.set_xticks([])
    
    plt.show()


main()


