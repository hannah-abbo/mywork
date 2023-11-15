#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 23:32:34 2023

@author: Hannah Abbo 
"""


COFFEE = "coffee.csv"
INSURANCE = "insurance.csv"


import csv
import matplotlib.pyplot as plt
import numpy as np


def summary_by_group(data, group, value, 
                     summary_stat = 'mean', 
                     sort = False,
                     reverse = False):
    # name: summary_by_group
    # input: data (list of dicts)
    #        group - the key in each row containing the group identifer (string)
    #        value - the key in each row containing the value (string)
    #        summary_stat - type of summary stat to calculate, either 'mean',
    #           'count' or 'sum' (string)
    #        sort - whether to sort the dictionary, and based on what - either
    #           the names of the groups 'group' or the values of the summary 
    #           statistic 'value', defaults to False
    #        reverse - False sorts ascending, True sorts descending
    #        
    # returns: summary stats by group, with each key representing a group and 
    #          value as the chosen summary stat(dict)
    # Take a list of dicts as data, and then calculate a sumamry stat for every
    # group in the list 

    sums = {}
    obs = {}
    for row in data:
        if row[group] not in sums:
            sums[row[group]] = float(row[value])
            obs[row[group]] = 1
        else:
            sums[row[group]] += float(row[value])
            obs[row[group]] += 1
   
    if summary_stat == 'count':
        if sort == 'group':
            obs = dict(sorted(obs.items(), reverse = reverse))
        if sort == 'value': 
            obs = dict(sorted(obs.items(), key=lambda d: d[1], 
                              reverse = reverse))
        return obs
    
    if summary_stat == 'sum':
        if sort == 'group':
            sums = dict(sorted(sums.items(), reverse =  reverse))
        if sort == 'value':
            sums = dict(sorted(sums.items(), key=lambda d: d[1], 
                               reverse = reverse))
        return sums
    
    if summary_stat == 'mean':
        means = {}
        for k, v in sums.items():
            means[k] = v / obs[k]
        if sort == 'group':
            means = dict(sorted(means.items(), reverse = reverse))
        if sort == 'value':
            means = dict(sorted(means.items(), key=lambda d: d[1], 
                                reverse = reverse))
        return means
            
def read_csv_file(filename):
    # name: read_csv_file
    # input: filename (str)
    # returns: contents of the file, (list of str)
    lst = []
    
    csvfile = csv.DictReader(open(filename))
    for line in csvfile:
        lst.append(line)
    return lst



coffee = read_csv_file(COFFEE)
insurance = read_csv_file(INSURANCE)

###########################################################################
### Bar charts
###########################################################################

# Get the total (sum) of sales (line_item_amount) by the category (product_group)
sums = summary_by_group(coffee, 'product_group', 'line_item_amount', 'sum')

products = list(sums.keys()) # Unpack the keys to make the labels
sales = list(sums.values()) # Unpack the values to make the bar heights
plt.figure(figsize=(6.5, 8))
plt.bar(products, sales)
plt.show()


## Zoom in/Zoom out
products = list(sums.keys())
sales = list(sums.values())
plt.figure(figsize=(6.5, 8))
plt.bar(products, sales)
plt.show()

products = list(sums.keys())[1:] # Drop the first value from the list
sales = list(sums.values())[1:]
plt.figure(figsize=(6.5, 8))
plt.bar(products, sales)
plt.show()

## Removing tick marks, adding light grid lines
products = list(sums.keys())
sales = list(sums.values())
plt.figure(figsize=(6.5, 8))
plt.rc('axes', axisbelow=True) # Set the gridlines to appear behind bars
plt.grid(axis = 'y',linestyle = '--', linewidth = 0.5)
plt.bar(products, sales)
plt.tick_params(left = False, bottom = False)
plt.show()


## Sort the groups alphabetically
sums = summary_by_group(coffee, 'product_group', 'line_item_amount', 'sum',
                        sort = 'group')
products = list(sums.keys())
sales = list(sums.values())
plt.figure(figsize=(6.5, 8))
plt.rc('axes', axisbelow=True) # Set the gridlines to appear behind bars
plt.grid(axis = 'y',linestyle = '--', linewidth = 0.5)
plt.bar(products, sales)
plt.tick_params(left = False, bottom = False)
plt.show()  

## Sort the groups by value
sums = summary_by_group(coffee, 'product_group', 'line_item_amount', 'sum',
                        sort = 'value', reverse = True) ## Sort descending
products = list(sums.keys())
sales = list(sums.values())
plt.figure(figsize=(6.5, 8))
plt.rc('axes', axisbelow=True) # Set the gridlines to appear behind bars
plt.grid(axis = 'y',linestyle = '--', linewidth = 0.5)
plt.bar(products, sales)
plt.tick_params(left = False, bottom = False)
plt.show()  
   
## Rotate the value labels
sums = summary_by_group(coffee, 'product_group', 'line_item_amount', 'sum',
                        sort = 'value', reverse = True) ## Sort descending
products = list(sums.keys())
sales = list(sums.values())
plt.figure(figsize=(6.5, 8))
plt.rc('axes', axisbelow=True) # Set the gridlines to appear behind bars
plt.grid(axis = 'y',linestyle = '--', linewidth = 0.5)
plt.bar(products, sales)
plt.tick_params(left = False, bottom = False)
plt.xticks(rotation=90)
plt.show() 

## Rotate the bars
sums = summary_by_group(coffee, 'product_group', 'line_item_amount', 'sum',
                        sort = 'value', reverse = False) ## Sort descending
products = list(sums.keys())
sales = list(sums.values())
plt.figure(figsize=(8, 6))
plt.rc('axes', axisbelow=True) # Set the gridlines to appear behind bars
plt.grid(axis = 'x',linestyle = '--', linewidth = 0.5) # Note change in direction
plt.barh(products, sales)
plt.tick_params(left = False, bottom = False)
plt.show()   


## Bar chart of total sales by product_type
sums = summary_by_group(coffee, 'product_type', 'line_item_amount', 'sum',
                        sort = 'value', reverse = False) ## Sort descending
products = list(sums.keys())
sales = list(sums.values())
plt.figure(figsize=(8, 6))
plt.rc('axes', axisbelow=True) # Set the gridlines to appear behind bars
plt.grid(axis = 'x',linestyle = '--', linewidth = 0.5) # Note change in direction
plt.barh(products, sales)
plt.tick_params(left = False, bottom = False)
plt.show() 



## Q1: Make a bar plot of only the top 10 products within product_type by sales  

sums = summary_by_group(coffee, 'product_type', 'line_item_amount', 'sum',
                        sort = 'value', reverse = False) ## Sort descending
products = list(sums.keys())[:10]
sales = list(sums.values())[:10]
plt.figure(figsize=(8, 6))
plt.rc('axes', axisbelow=True) # Set the gridlines to appear behind bars
plt.grid(axis = 'x',linestyle = '--', linewidth = 0.5) # Note change in direction
plt.barh(products, sales)
plt.tick_params(left = False, bottom = False)
plt.show() 



###########################################################################
### Line charts
###########################################################################
 
   
# Get the total (sum) of sales (line_item_amount) by the date (transaction_date)
sums = summary_by_group(coffee, 'transaction_date', 'line_item_amount', 'sum')

dates = list(sums.keys()) # Unpack the keys to make the labels
sales = list(sums.values()) # Unpack the values to make the bar heights
plt.figure(figsize=(6.5, 8))
plt.plot(products, sales)
plt.show()




# We need to get rid of some of the tick marks
sums = summary_by_group(coffee, 'transaction_date', 'line_item_amount', 'sum')

dates = list(sums.keys()) 
# Create data labels using a list comprehension
date_labels = [date if date in dates[0::7] else "" for date in dates]
sales = list(sums.values()) 
plt.figure(figsize=(6.5, 8))
plt.plot(dates, sales)
plt.xticks(dates, date_labels)
plt.tick_params(left = False, bottom = False)
plt.show()




# Let's add titles and labels
sums = summary_by_group(coffee, 'transaction_date', 'line_item_amount', 'sum')

dates = list(sums.keys()) 
# Create data labels using a list comprehension
date_labels = [date if date in dates[0::7] else "" for date in dates]
sales = list(sums.values()) 
plt.figure(figsize=(6.5, 8))
plt.plot(dates, sales)
plt.xticks(dates, date_labels)
plt.tick_params(left = False, bottom = False)
plt.title("Retail sales peaked on April 17")
plt.ylabel("Sales ($)")
plt.show()


# Making the Y axis label horizontal

sums = summary_by_group(coffee, 'transaction_date', 'line_item_amount', 'sum')

dates = list(sums.keys()) 
# Create data labels using a list comprehension
date_labels = [date if date in dates[0::7] else "" for date in dates]
sales = list(sums.values()) 
plt.figure(figsize=(6.5, 8))
plt.plot(dates, sales)
plt.xticks(dates, date_labels)
plt.tick_params(left = False, bottom = False)
plt.title("Retail sales peaked on April 17")
plt.gcf().text(0.03, 0.85, "Sales ($)")
plt.show()





# Making the Y axis lable horizontal

sums = summary_by_group(coffee, 'transaction_date', 'line_item_amount', 'sum')

dates = list(sums.keys()) 
# Create data labels using a list comprehension
date_labels = [date if date in dates[0::7] else "" for date in dates]
sales = list(sums.values()) 
plt.figure(figsize=(6.5, 8))
plt.plot(dates, sales)
plt.xticks(dates, date_labels)
plt.tick_params(left = False, bottom = False)
plt.title("Retail sales peaked on April 17")
plt.gcf().text(0.03, 0.85, "Sales ($)")
plt.text("2019-04-18", max(sales), "Peak sales (April 17)")
plt.axvline("2019-04-17", color = "gray", ls = "--")
plt.show()






###########################################################################
### Scatter plots
###########################################################################

bmi = [float(d['bmi']) for d in insurance]
charges = [float(d['charges']) for d in insurance]
smoker = [d['smoker'] for d in insurance]

plt.figure(figsize=(6.5, 8))
plt.scatter(bmi, charges)
plt.tick_params(left = False, bottom = False)
plt.title("Relationship between BMI and insurance charges")
plt.show()


## Adding a regression line

plt.figure(figsize=(6.5, 8))
plt.scatter(bmi, charges)

slope, intercept = np.polyfit(bmi, charges, 1)
yhat = [v*slope + intercept for v in bmi]
plt.plot(bmi, yhat, color = "black")
plt.tick_params(left = False, bottom = False)
plt.title("Relationship between BMI and insurance charges")
plt.show()


## Setting dot color by smoker

colors = ["red" if v == "yes" else "blue" for v in smoker]
plt.figure(figsize=(6.5, 8))
plt.scatter(bmi, charges, color = colors)
slope, intercept = np.polyfit(bmi, charges, 1)
yhat = [v*slope + intercept for v in bmi]
plt.plot(bmi, yhat, color = "black")
plt.tick_params(left = False, bottom = False)
plt.title("Relationship between BMI and insurance charges")

plt.show()



#Q2 : Add text labels for colors

colors = ["red" if v == "yes" else "blue" for v in smoker]
plt.figure(figsize=(6.5, 8))
plt.scatter(bmi, charges, color = colors)
slope, intercept = np.polyfit(bmi, charges, 1)
yhat = [v*slope + intercept for v in bmi]
plt.plot(bmi, yhat, color = "black")
plt.tick_params(left = False, bottom = False)
plt.title("Relationship between BMI and insurance charges")
plt.text(46, 15000, "nonsmokers", color = "blue")
plt.text(48, 51000, "smokers", color = "red")

plt.show()
