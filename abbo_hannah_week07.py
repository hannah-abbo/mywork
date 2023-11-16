
"""
In this week's exercise, we're going to be trying to calculate 
k-nearest-neighbors from several data sets.

To do this, we'll need to write three functions:
    - Reading in a CSV file and returning the data
    - Calculating the Euclidean distance between two points
    - Getting the k-nearest neighbor for a point from a list of points
    
We'll use these functions to work on two different problems.

"""

# Download the two csv files and put their filenames here.
MBTA_LOCATIONS = "mbta_stations.csv"
MOVIES_LIST = "movies_list.csv"

import csv

    
## Q2: Write a function to calculate the Euclidean distance between two points
## These points can be of any number of dimensions, so we'll need to
## find the sum of the squared distances for each dimension, then get the
## square root of this number.
## To compute a number to a power, use the ** operator. E.g. 2**2 = 4
## Also, recall that the square root is equivalent to the .5 power
def euclidean_distance(point1, point2):
    # name: euclidean_distance
    # input: point1 (list), 
    #        point2 (list)
    #        lists can be of any length, but both must be the same length
    # returns: float
  
    distance = 0
    for i in range(len(point1)):
      distance += (point1[i]- point2[i]) ** 2
    
    # after the euclidean finishes running and adding itself to 
    # distance, we find the sqrt
      
    return (distance ** 0.5)

## Q3: Write a function to get the k-nearest neighbors to a point from a list
## of points. Use the euclidean_distance function to find the distance from the
## target to each point in the point_list.
## Then, sort this list based on the distance, and return a list of lists. 
## This list will have length num_neighbors, and each element will be a two
## element list, containing the point and the distance
def get_k_nearest_neighbors(target, point_list, ignore, num_neighbors):
    # name: get_k_nearest_neighbors
    # input: target (list)
    #        point_list (list of lists)
    #        ignore (int)
    #        num_neighbors (int)
    #        ignore is the number of elements in the list to ignore - use
    #           this to pass additional id information about the point that
    #           will be useful when trying to interpet the results
    #        points in point_list must be of same length as target list     
    #
    # Remember to "ignore" the first ignore elements in the list when 
    # calculating the Euclidean distance, and convert these values to floats
    # using a list comprehension
    #
    # Go through each point in the list, calculate the distance, and add that
    # distance to an empty list 
    # Sort the list of distances by using the .sort() function

     #
     # Then, you'll need to return a list of lists of length num_neighbors with
     # the points as the first element, and the distance as the second
     # One way to do this is to create another empty list, then go through each
     # distance in the distances list and find which point has the same distance
     # by recalculating the distance for that point. This is very slow but
     # simple.
     
 
    # initialize list 
    distances = []

    for point in point_list:
        print(point)
        print(target)
        distances.append(euclidean_distance(target, [float(el) for el in point[ignore:]]))
    
    distances.sort()
    distances_target = distances[:num_neighbors]
    
    output = []
    for distance in distances_target:
        for point in point_list: 
            if euclidean_distance(target, [float(el) for el in point[ignore:]]) == distance:
                output.append([point, distance])
                
    return(output)
                
def main():
    ## Q4: Use the read_csv_file function to read in the file mbta_locations.csv
    ## Remember to remove the header, the first element in the list returned
    ## by read_csv_file
    ## Then use the nearest neighbor function to find the 2 nearest MBTA
    ## locations for each of the following locations in the following list.
    
    ## The MBTA locations list of lists has station name and line in the first
    ## element, then the lat and long in the second and third elements.
    ## So, you'll want to set ignore to 1.
    
    mbta = []
    
    with open(MBTA_LOCATIONS, "r") as infile: 
        csvfile = csv.reader(infile)
        next(csvfile)
        
        for line in csvfile:
            mbta.append(line)
        
    locations = [[42.3385434,-71.0967954],
                 [42.3550897,-71.0679143],
                 [42.3466764,-71.0994065],
                 [42.3657944,-71.1192065]]
    
    ## Where are these places???
    
    two_nearest = get_k_nearest_neighbors(locations[0], mbta, 1, 2)
    print(two_nearest)

    ## Q5:  In the list below, replace the 0s with 1s for the movie genres you 
    ## like
    ## Use the read in the movie list file. Remember to remove the header!
    ## Then, get the 10 nearest neighbors to your preferences. Set the ignore
    ## value to 2 since the first two columns should be ignored in movies_list
    
    movies = []
    
    with open(MOVIES_LIST, "r") as infile:
        csvfile = csv.reader(infile)
        next(csvfile)
        
        for line in csvfile:
            movies.append(line)
    
    my_preferences = [
            1,#action
            1,#adventure
            0,#animation
            0,#biography
            1,#comedy
            0,#crime
            1,#documentary
            1,#drama
            1,#family
            1,#fantasy
            0,#film-noir
            0,#game-show
            0,#genre
            0,#history
            0,#horror
            1,#music
            0,#musical
            0,#mystery
            0,#news
            0,#reality-tv
            1,#romance
            0,#sci-fi
            0,#short
            0,#sport
            0,#talk-show
            1,#thriller
            0,#war
            0#western
            ]

    ten_nearest = get_k_nearest_neighbors(my_preferences, movies, 2, 10)
    print(ten_nearest)

    
main()
