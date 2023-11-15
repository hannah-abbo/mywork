# -*- coding: utf-8 -*-
"""
DS2001 (S23-Matherly) Week 8

Rename this file as lastname_firstname_week08.py


@author: [YOUR NAME HERE]
"""



"""
In this week's exercise, we're going to be trying to calculate 
k-nearest-neighbors from a book data set

We'll need four functions, some of which we'll reuse from last time
    - Reading in a CSV file and returning the data (reuse Wk07)
    - Calculating the Euclidean distance between two points (reuse Wk07,
           with a modification)
    - get_distance_value, which takes a dictionary as a parameter and returns
        the value of the key 'distance' from that dictionary
    - Getting the k-nearest neighbor for a point from a list of points (reuse
           Wk07, with some modifications
           
Then, we'll read in a list of books and genre ratings, and use the k nearest
neighbor function to provide recommendations to the user based on their
preferences
"""

BOOKS_LIST = "books.csv"

import csv

## Q1: Reuse the read_csv_file function from last week. It should create an
## empty list, use the CSV library to parse the file, skip over the header line
## then append each line to the empty list.

def read_csv(filename):
    # name: read_csv_file
    # input: filename (string)
    # returns: list [header, items]
    #           header is a list containing the header from the CSV file
    #           items is a list of lists, containing the 
    
    lst = []
    with open(filename, "r") as infile: 
        csvfile = csv.reader(infile)
        next(csvfile) # skips over the header 
        infile.readline()
        for line in csvfile:
            lst.append(line)
            
    return lst 
    
    
## Q2: Reuse the Euclidean distance function from last week. Only change is
## to convert the points to floats here when calculating the squared distance
def euclidean_distance(point1, point2):
    # name: euclidean_distance
    # input: point1 (list), 
    #        point2 (list)
    #        lists can be of any length, but both must be the same length
    # returns: float
  
    distance = 0
    for i in range(len(point1)):
      distance += (((float(point1[i]))- float(point2[i])) ** 2)
    
    # after the euclidean finishes running and adding itself to 
    # distance, we find the sqrt
      
    return (distance ** 0.5)
  


## Q3: Create a new function, get_distance_value, that takes a dictionary as
## a parameter, than returns the value of the key 'distance' from it
## We'll need this for the sorted function later

def get_distance_value(d):
    # name: get_distance_value
    # input: d (dictionary)
    # returns: value of the 'distance' key from the dictionary
    return(d["distance"])
    
## Q4: Reuse the K nearest neighbors function from last week, but with a few
## changes.
## Remove the "ignore" parameter
## point_list is now a list of dictionaries, and each dictionary will have a
## "dimensions" key which accesses a list of all the dimensions for that point
## As before, we'll go through each point in the list and calculate the
## distance from the target_point, but we'll have to get "dimensions" key from
## each point to do this calculation
## Then, use the sorted() function on the distances list to create a new,
## sorted list, adding the "key" parameter and giving the it the name of our 
## get_distance_value function
## Because we're passing the function, don't include the () at the end of the name
## Then, return the first num_neighbors elements of the list

 

def get_k_nearest_neighbors(target, point_list, num_neighbors):
    # name: get_k_nearest_neighbors
    # input: target_point (list)
    #        point_list (list of dictionaries)
    #        num_neighbors (int)
    #        point_list is a list of dictionaries, with each dictionary
    #         having a list called "dimensions" which is the same length
    #         as target_point
    #
    #
    # Go through each point in the list, calculate the distance, and add the
    # distance as a new item in the point's dictionary, then add the points
    # to the empty list
    #
    # Sort the list of distances by using the .sorted() function, specifying
    # the key 
    #
    # Then, return the first num_neighbors elements of the sorted list
     
 
    # initialize list 
    point_distances = []
    for point in point_list:
        distance = euclidean_distance(target, point["dimensions"])
        point["distance"] = distance
        
        point_distances.append(point)
        
    sorted_list = sorted(point_distances, key = get_distance_value)
    
    return(sorted_list[:num_neighbors])


def main():
    ## Q5: Use the read_csv_file function to read in the book list file.
    ## Create an empty list for all the books, and then go through each item in
    ## list from the CSV file, creating a dictionary with the following keys:
    ## - id, the first item in each row
    ## - title, the second item 
    ## - authors, the third item
    ## - pub_year, the fourth item
    ## - avg_rating, the fifth item
    ## - dimensions, the remaining items in the row
    ## Then append that dictionary to the empty list
    
    csvfile = read_csv("books.csv")
    books = []
    
    for row in csvfile:
        
        dictionary_books = {}
        dictionary_books["id"] = row[0]
        dictionary_books["title"] = row[1]
        dictionary_books["authors"] = row[2]
        dictionary_books["pub_year"] = row[3]
        dictionary_books["avg_rating"] = row[4]
        dictionary_books["dimensions"] = row[5:]
    
        books.append(dictionary_books)

    
    ## Q6:  In the list below, replace the 0s with your own interest in each
    ## of the following book genres, represented as values from 0-100, with
    ## 0 representing no interest and 100 representing high interest
    ## Then, use the get_k_nearest_neighbors function with your preferences as
    ## the target point, and the cleaned list of books as the comparison points
    ## and find the 10 closest matches.
    ## Print out your recommendations in a neat fashion.

    my_preferences = [
            0, # adult
            0, # adult-fiction
            0, # adventure
            60, # biography
            0, # chick-lit
            0, # children
            0, # childrens
            15, # classics
            0, # comics
            0, # contemporary
            0, # crime
            20, # dystopian
            30, # fantasy
            100, # fiction
            0, # graphic-novels
            0, # historical
            100, # historical-fiction
            0, # history
            0, # horror
            0, # humor
            0, # magic
            0, # manga
            40, # memoir
            0, # mystery
            60, # non-fiction
            95, # novels
            0, # paranormal
            0, # paranormal-romance
            0, # philosophy
            90, # romance
            0, # sci-fi-fantasy
            0, # science
            0, # science-fiction
            0, # series
            0, # supernatural
            0, # teen
            70, # thriller
            0, # urban-fantasy
            0, # vampires
            0, # young-adult
            ]
    
    recs = get_k_nearest_neighbors(my_preferences, books, 10)
    
    print("Here are your 10 best recommendations:", recs)
    
    

main()