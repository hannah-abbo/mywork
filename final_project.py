#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

DS2001
Final Project Code
Nina and Hannah

Comparing Ad Platform Success


"""


FILENAME = 'Ad-data-Assignment-1.csv'

import csv
import matplotlib.pyplot as plt

# Function to read the CSV file and return a 2D list
def read_csv(filename):
    data = []
    with open(filename, 'r') as infile:
        csv_reader = csv.reader(infile)
        next(csv_reader) # skip header
        for row in csv_reader:
            data.append(row)
    return data

# Function to split data by campaign platform and return a dictionary
def split_by_platform(data):
    platform_dict = {}
    for row in data:
        platform = row[3] # campaign_platform column
        if platform not in platform_dict:
            platform_dict[platform] = []
        platform_dict[platform].append(row)
    return platform_dict

# Function to calculate cumulative spend and create a bar graph
def cumulative_spend(platform_dict):
    google_spend = 0
    facebook_spend = 0
    for value in platform_dict['Google Ads']:
        google_spend += float(value[12]) # spends column
    for value in platform_dict['Facebook Ads']:
        facebook_spend += float(value[12]) # spends column
    plt.bar(['Google Ads', 'Facebook Ads'], [google_spend, facebook_spend], 
            color=['red', 'blue'])
    plt.title('Cumulative Spend by Platform')
    plt.xlabel('Campaign Platform')
    plt.ylabel('Total Spend')
    plt.ticklabel_format(style='plain', axis='y')
    plt.show()
    return google_spend, facebook_spend
    
def success_by_platform(platform_dict):
    google_success = 0
    google_total = 0
    for line in platform_dict["Google Ads"]:
        if line[13] != '':
            google_success += int(line[13])
            google_total += 1
        if line[14] != '':
            google_success += int(line[14])
            google_total += 1
        if line[15] != '':
            google_success += int(line[15])
            google_total += 1
    
    facebook_success = 0
    facebook_total = 0
    for line in platform_dict["Facebook Ads"]:
        if line[13] != '':
            facebook_success += int(line[13])
            facebook_total += 1
        if line[14] != '':
            facebook_success += int(line[14])
            facebook_total += 1
        if line[15] != '':
            facebook_success += int(line[15])
            facebook_total += 1
    
    google_proportion = google_success / google_total
    facebook_proportion = facebook_success / facebook_total   
    
    plt.bar(['Google Ads', 'Facebook Ads'], [google_success, facebook_success],
            color=['red', 'blue'])
    plt.title('Proportional Success')
    plt.xlabel('Campaign Platform')
    plt.ylabel('Proportional Success')
    plt.show()

def success_by_age(data, platform_dict):
    '''
    Function: success_by_age
    Parameters: take in the 2D list of data created by the read_csv function
    Does: Uses the split_by_platform function to split the data into two separate 
    lists for Google Ads and Facebook Ads
    Calculates the success of each platform (i.e. sum of impressions, clicks, 
    and link clicks) for each age group
    Returns:Plots the results on a scatter plot to show which platform is more 
    successful for each age group
    '''
    google_success_by_age = {}
    facebook_success_by_age = {}
    
    for value in platform_dict['Google Ads']:
        age = value[6] # age column
        impressions = int(value[13]) # impressions column
        clicks = int(value[14]) # clicks column
        link_clicks = int(value[15]) # link clicks column
        success = impressions + clicks + link_clicks
        if age not in google_success_by_age:
            google_success_by_age[age] = success
            google_success_by_age[age] = success
        else:
            google_success_by_age[age] += success
    
    for value in platform_dict['Facebook Ads']:
        age = value[6] # age column
        impressions = int(value[13]) # impressions column
        clicks = int(value[14]) # clicks column
        link_clicks = int(value[15]) # link clicks column
        success = impressions + clicks + link_clicks
        if age not in facebook_success_by_age:
            facebook_success_by_age[age] = success
        else:
            facebook_success_by_age[age] += success
    
    plt.scatter(google_success_by_age.keys(), google_success_by_age.values(), 
                color='red', label='Google Ads')
    plt.scatter(facebook_success_by_age.keys(), facebook_success_by_age.values(), 
                color='blue', label='Facebook Ads')
    plt.title('Success by Age')
    plt.xlabel('Age')
    plt.ylabel('Total Success')
    plt.legend()
    plt.show()
    

# Function 6: overall_success_by_platform
# Question: Which platform, Google Ads or Facebook Ads, has more successful ads overall in the marketing campaigns of "Product 1" from October 2019 to July 2020?
# Uses the split_by_platform function to split the data into two separate lists for Google Ads and Facebook Ads
# Calculates the success of each ad (i.e. sum of impressions, clicks, and link clicks) for each platform
# Sorts the list of ads by success in descending order
# Selects the top 1000 ads from each platform and compares their success using a bar graph to determine which platform has more successful ads overall. 

# Main function
def main():
    data = read_csv(FILENAME)
    
    total = []
    for line in data:
        dollars = float(line[12])
        total.append(dollars)
    total_spend = float(sum(total))
    print("The total spend was $", round(total_spend, 2))
        
    platform_dict = split_by_platform(data)
    google_spend, facebook_spend = cumulative_spend(platform_dict)
    
    print("Total spend for Google Ads $", round(google_spend,2))
    print("Total spend for Facebook Ads $", round(facebook_spend,2))
    
    success_by_platform(platform_dict)
    success_by_age(data, platform_dict)
    plt.show()
            

    
main()






