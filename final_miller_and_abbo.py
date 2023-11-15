#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

DS2001
Final Project Code
Nina Miller and Hannah Abbo

Comparing Ad Platform Effectiveness


"""


FILENAME = 'Ad-data-Assignment-1.csv'

import csv
import matplotlib.pyplot as plt


def read_csv(filename):
    '''
    Function: read_csv
    Parameters: csv file
    Returns: a 2D list of each row in the file as a 1D list
    Does: Read in the csv file, skip the header, and append each row as a 
        list to a 2D list labeled "data"
    '''
    data = []
    with open(filename, 'r') as infile:
        csv_file = csv.reader(infile)
        next(csv_file)
        for row in csv_file:
            data.append(row)
            
    return data


def split_by_platform(lst):
    '''
    Function: split_by_platform
    Parameters: 2D list
    Returns: a dictionary
    Does: Create a dictionary where the campaign platform is the key 
        ('Facebook Ads' or 'Google Ads') and the corresponding rows are the values
    '''
    platform_dict = {}
    for row in lst:
        platform = row[3]
        if platform not in platform_dict:
            platform_dict[platform] = []
        platform_dict[platform].append(row)
        
    return platform_dict


def cumulative_spend(dictionary):
    '''
    Function: cumulative_spend
    Parameters: dictionary
    Returns: Google spend and FB spend as a tuple
    Does: For each key in the dictionary, add up the total ad spend per platform
        and plot the totals in a bar graph
    '''
    google_spend = 0
    facebook_spend = 0
    for d in dictionary['Google Ads']:
        google_spend += float(d[12])
    for d in dictionary['Facebook Ads']:
        facebook_spend += float(d[12])
    
    plt.bar(['Google Ads\n', 'Facebook Ads\n'], [google_spend, facebook_spend], 
            color=['firebrick', 'royalblue'], width = 0.6)
    plt.title('\nOver 75% of Advertising Spend\nWent to Google Ads\n')
    plt.ticklabel_format(style='plain', axis='y')  #used Stack Overflow to figure this out
    plt.gcf().text(-.14, 0.815, "Total\nSpend ($)")
    plt.show()
    
    return google_spend, facebook_spend
    

def effectiveness_by_platform(dictionary):
    '''
    Function: effectiveness_by_platform
    Parameters: dictionary
    Returns: the proportional effectiveness of each platform as a tuple
    Does: Determine the overall effectiveness of each platform by adding up the 
        nmpressions, clicks, and link clicks for each ad on that platform. 
        Since 90% of the ads are Google ads, make the effectiveness score 
        proportional by dividing by the total number of ads per platform. 
        Plot the totals in a bar graph.
    '''
    google_effect = 0
    google_total = 0
    for d in dictionary["Google Ads"]:
        google_total += 1
        if d[13] != '':
            google_effect += int(d[13])    #pos 13 = impressions
        if d[14] != '':
            google_effect += int(d[14])    #pos 14 = clicks
        if d[15] != '':
            google_effect += int(d[15])    #pos 14 = link clicks
            
    facebook_effect = 0
    facebook_total = 0
    for d in dictionary["Facebook Ads"]:
        facebook_total += 1
        if d[13] != '':
            facebook_effect += int(d[13])
        if d[14] != '':
            facebook_effect += int(d[14])
        if d[15] != '':
            facebook_effect + int(d[15])
    
    google_proportion = google_effect / google_total
    facebook_proportion = facebook_effect / facebook_total
    
    plt.bar(['Google Ads\n', 'Facebook Ads\n'], [google_proportion, facebook_proportion],
            color=['firebrick', 'royalblue'], width = 0.6)
    plt.title('\nFacebook Ads Outperformed\nGoogle Ads 40:1\n')
    plt.gcf().text(-0.15, 0.825, "Effectiveness\nScore")
    plt.ticklabel_format(style='plain', axis='y')
    plt.show()
    
    return google_proportion, facebook_proportion


def effectiveness_by_age(dictionary):
    '''
    Function: effectiveness_by_age
    Parameters: dictionary
    Returns: two dictionaries as a tuple
    Does: For each platform, determines the impressions + clicks + link clicks 
        for each age group. Plot the different scores on a scatter plot. 
    '''
    google_effect_by_age = {}
    facebook_effect_by_age = {}
    
    impressions_g = 0
    clicks_g = 0
    link_clicks_g = 0
    
    for d in dictionary['Google Ads']:
        age = d[11]                         #pos 11 = age
        if d[13] != '':
            impressions_g = int(d[13])      #pos 13 = impressions
        if d[14] != '':
            clicks_g = int(d[14])           #pos 14 = clicks
        if d[15] != '':    
            link_clicks_g = int(d[15])      #pos 15 = link clicks
        
        success_g = impressions_g + clicks_g + link_clicks_g
        
        if age != 'Undetermined':
            if age not in google_effect_by_age:
                google_effect_by_age[age] = success_g
            else:
                google_effect_by_age[age] += success_g
    
    impressions_f = 0
    clicks_f = 0
    link_clicks_f = 0
    
    for d in dictionary['Facebook Ads']:
        age = d[11]                          #pos 11 = age
        if d[13] != '':
            impressions_f = int(d[13])       #pos 13 = impressions
        if d[14] != '':
            clicks_f = int(d[14])            #pos 14 = clicks
        if d[15] != '':   
            link_clicks_f = int(d[15])       #pos 15 = link clicks
            
        success_f = (impressions_f + clicks_f + link_clicks_f)
        
        if age not in facebook_effect_by_age:
            facebook_effect_by_age[age] = success_f
        else:
            facebook_effect_by_age[age] += success_f
            
    plt.scatter(google_effect_by_age.keys(), google_effect_by_age.values(), 
                color='firebrick', label='Google Ads', marker = "o")
    plt.scatter(facebook_effect_by_age.keys(), facebook_effect_by_age.values(), 
                color='royalblue', label='Facebook Ads', marker = "^")
    plt.title('\nFacebook Ads were Much More Effective\nwith Younger Users\n')
    plt.xlabel('\nAge Groups\n')
    plt.gcf().text(-.192, 0.76, "Effectiveness\nScore")
    plt.grid(axis = 'y', color = "lightgray")
    plt.rc('axes', axisbelow=True)
    plt.ticklabel_format(style='plain', axis='y')   #used Stack Overflow to figure this out
    plt.legend()
    plt.show()
    
    return google_effect_by_age, facebook_effect_by_age



def main():
    #Read in the file and create a 2D list
    data = read_csv(FILENAME)
        
    
    #Seperate the data into a dictionary with each platform as a key
    platform_dict = split_by_platform(data)
    
    
    #For clarity, find the number of Facebooks and Google ads analyzed
    tot_f = 0
    tot_g = 0
    for d in platform_dict["Facebook Ads"]:
        tot_f += 1
    for d in platform_dict["Google Ads"]:
        tot_g += 1
        
    print("\nIn total, we are analyzing", tot_f, "Facebook Ads and", tot_g, 
          "Google Ads for Merkle Sokrati's 10-month Product 1 push.")
        

    #Find the cumulative spend per platform
    google_spend, facebook_spend = cumulative_spend(platform_dict)
    
    print("\nThe total spent on Facebook Ads was $", round(facebook_spend,2))
    print("And, he total spent on Google Ads was $", round(google_spend,2), " (WAY more)")
    print("Was the investmenst into Google Ads worth it for Merkle?")
    
    
    #Compare how each platform performed proportinally
    google_proportion, facebook_proportion = effectiveness_by_platform(platform_dict)
    ratio_f = (facebook_proportion) / (google_proportion)

    print("\nAdding up all impressions, clicks, and link clicks... proportionaly, "
              "Facebook Ads outperformed Google Ads", round(ratio_f), ": 1")
    
    
    #Compare age group effectiveness on each platform
    google_success_by_age, facebook_success_by_age = effectiveness_by_age(platform_dict)
    
    print("\nFinally, let's look at age group comparisons by platform. You will notice"
          " that Facebook was much more effective, especially with younger crowds.")
    
    
    print("\nLooks like Merkle put all of their eggs into the wrong basket!!!")


            
main()






