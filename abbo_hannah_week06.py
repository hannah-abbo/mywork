# -*- coding: utf-8 -*-
"""
DS2001 (S23-Matherly) Week 6

Rename this file as lastname_firstname_week06.py


@author: [YOUR NAME HERE]
"""



"""
In this week's exercise, we're going to analyze some data on ads from the
Super Bowl.

First, you'll read in the data from the file into seven lists, appending them
by row

Then, we'll use functions to identify:
    - the highest scoring video on the AdMeter
    - the worst scoring video on the AdMeter
    - the ad with the most YT views
    - the ad with the most YT likes
    - the ad with the highest likes to views ratio
    - the ad with the highest likes to AdMeter rating


Then, we'll produce scatter plots for:
    - likes to views
    - views to AdMeter scores
    - likes to AdMeter scores
    
    
    ''' Function: max_list
        parameters: list of non-negative numbers 
        returns: a number 
        does: finds and return the max value in the list 
    '''
    
"""


import matplotlib.pyplot as plt
SB_DATA_FILE = "sb2023_ads.csv"


# Q1:
# Write a function with the name find_max
# This function should take a list as a parameter
# This function should return an int, the INDEX of the maximum value in the list - 
# that is, it will give us the number of the element in the list is the largest

def find_max(lst):
    ''' Function: find_min 
        parameter: list of numbers
        returns: an int- INDEX of max value in the list  
        does: gives number of the element in the list is the largest. 
    '''
    max_ind = -1
    max_val = max(lst)
    counter = 0 # position
    
    for num in lst:
        if num == max_val:
            max_ind = counter 
        counter += 1
        
    return max_ind

# Q2:
# Write a function with the name find_min
# This function should take a list as a parameter
# This function should return an int, the INDEX of the minimum value in the list - 
# that is, it will give us the number of the element in the list is the smallest

def find_min(lst):
    ''' Function: find_min
        parameter: list of numbers
        returns: an int- INDEX of max value in the list  
        does: gives number of the element in the list is the largest. 
    '''
    min_ind = -1
    min_val = min(lst)
    counter = 0
    
    for num in lst:
        if num == min_val:
            min_ind = counter 
        counter += 1
        
    return min_ind


def main():
    with open(SB_DATA_FILE, "r") as infile:
        
        # create empty lists
        ranking = []
        title = []
        score = []
        url = []
        duration = []
        yt_views = []
        yt_likes = []
            
        for line in infile:
            lst = line.split(",")
            
            ranking_pos = lst[0]
            ranking.append(ranking_pos)
                
            title_pos = lst[1]
            title.append(title_pos)
    
            score_pos = lst[2]
            score.append(float(score_pos))
                
            url_pos = lst[3]
            url.append(url_pos)
                
            duration_pos = lst[4]
            duration.append(float(duration_pos))
                
            yt_views_pos = lst[5]
            yt_views.append(int(yt_views_pos))
                
            yt_likes_pos = lst[6]
            yt_likes.append(int(yt_likes_pos))
        

     
    # Q3:  
    # Read the data in from SB_DATA_FILE
    # The file is a comma separated values (CSV) file.
    # There are seven columns:
    # - ranking - Ad meter ranking (ties are noted)
    # - title - Ad title
    # - score - Ad Meter score (a float)
    # - url - YouTube video URL
    # - duration - length of the ad in seconds (a float)
    # - yt_views - Number of views on YouTube (an int)
    # - yt_likes - Number of likes on YouTube (an int)
    # Create seven empty lists, read a row, split it into seven values, then append
    # them to each of the lists.
    # There are 51 rows

  
    # Q4:
    # Using your find_max and find_min functions, identify which ads were the
    # highest and worst rated on the AdMeter measure.
    # Then, print out the name of the video and the URL, along with the
    # values of the AdMeter data
    
    
    max_score_pos = find_max(score)
    min_score_pos = find_min(score)
    
    max_name = title[max_score_pos]
    max_url = url[max_score_pos]
    max_score = score[max_score_pos]
    
    min_name = title[min_score_pos]
    min_url = url[min_score_pos]
    min_score = score[min_score_pos]
    
    print("The highest score video was:", max_name,"\nFound at:", max_url,
          "\nIts Admeter score was:", max_score)
    print("The lowest score video was:", min_name,"\nFound at:", min_url,
          "\nIts Admeter score was:", min_score)
    

    
    # Q5:
    # Using your find_max function, identify which ads had the most likes
    # and views on YouTube
    # Then, print out the name of the video and the URL, along with the
    # values of the YouTube likes and views
    
    max_likes_pos = find_max(yt_likes)
    max_views_pos = find_max(yt_views)
  
    likes_name = title[max_likes_pos]
    likes_url = url[max_likes_pos]
    likes_likes = yt_likes[max_likes_pos]
    views_likes = yt_views[max_likes_pos]
    
    views_name = title[max_views_pos]
    views_url = url[max_views_pos]
    views_views = yt_views[max_views_pos]
    likes_views = yt_likes[max_views_pos]

    print("The ad with the most likes was:", likes_name,"\nFound at:", 
          likes_url, "\nIt had", likes_likes, "likes, and", views_likes, 
          "views.") 
            
    print("The ad with most views was:", views_name,"\nFound at:", 
          likes_url, "\nIt had", likes_views, "likes, and", views_views, 
          "views.")
    
    # Q6:
    # Create two new empty lists to calculate...
    # - the likes to views ratio, and
    # - the likes to AdMeter ratio.
    # Then use a for loop to calculate the values of these measures for each
    # video, and append the values to the appropriate lists.
    # After you have this list, use your find_max function to 
    # identify the videos with the best likes to view and likes to AdMeter 
    # ratios.
    # Then, print out the name of the videos and the URLs, along with the 
    # values of the calculated ratios.
    
    
    # Q7:
    # Using plt.scatter(), create scatter plots of:
    # - views to likes
    # - views to AdMeter score
    # - likes to AdMeter score
    # Make sure to label the 

 
    
    
    
main()