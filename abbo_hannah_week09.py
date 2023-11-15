# -*- coding: utf-8 -*-
"""
DS2001 (S23-Matherly) Week 9

sasRename this file as lastname_firstname_week09.py


@author: [Hannah Abbo]
"""



"""

"""

YELP_REVIEWS = "yelp_data.csv"

STOP_WORDS_LIST = ['which', 'because', 'didn', 'over', 'you', 'that', 
                   'mightnt', 'wasn', 'same', 'such', 'on', 'why', 'again', 
                   'aren', 'so', 'youve', 'youll', 'doing', 'do', 'these', 
                   'between', 'my', 'whom', 'below', 'did', 'our', 'should', 
                   'wont', 'hasn', 'here', 'll', 'don', 'couldn', 'can', 'has',
                   'to', 'your', 'in', 'its', 'nor', 'mightn', 'himself', 
                   'ourselves', 'didnt', 'and', 'of', 'couldnt', 'won', 'y', 
                   've', 'needn', 'than', 'them', 'before', 'wouldn', 'ma', 
                   'i', 'then', 'until', 'few', 'very', 'd', 'each', 'herself', 
                   'doesn', 'myself', 'any', 'down', 'arent', 'yourself', 'be',
                   'her', 'by', 'further', 'once', 'does', 'shouldve', 'had', 
                   'as', 'isn', 'havent', 'wouldnt', 'an', 'not', 'ain', 
                   'both', 'or', 'we', 't', 'above', 'me', 'were', 'other', 
                   'out', 'his', 'through', 'doesnt', 'from', 'haven', 
                   'having', 'under', 'thatll', 'been', 'this', 'themselves', 
                   'ours', 'was', 'the', 'where', 'youre', 'too', 'while', 
                   'hasnt', 'mustnt', 'up', 'into', 'mustn', 're', 'against', 
                   'some', 'its', 'werent', 'who', 'at', 'shes', 'being', 
                   'now', 'a', 'after', 'there', 'weren', 'him', 'only', 
                   'neednt', 'he', 'they', 'isnt', 'hadnt', 'dont', 'what', 
                   'no', 'will', 'is', 'but', 'shan', 'about', 'for', 'yours', 
                   'wasnt', 'their', 'shouldn', 'am', 'when', 'are', 'itself', 
                   'all', 'yourselves', 'hers', 'it', 'those', 'if', 'more', 
                   'o', 'shouldnt', 'just', 'shant', 'theirs', 'have', 'hadn', 
                   'with', 'how', 'own', 'she', 'm', 'off', 'youd', 'most', 
                   'during', 's', '']

import csv

## Created a new CSV reader - this one using the DictReader function from CSV
## This will read every line into a Dict, with keys corresponding to the header
def read_csv_file(filename):
    # name: read_csv_file
    # input: filename (str)
    # returns: contents of the file, (list of str)
    lst = []
    
    csvfile = csv.DictReader(open(filename))
    for line in csvfile:
        lst.append(line)
    return lst

## Q1: Write a function to convert a string to lower case
def to_lower_case(string):
    # name: to_lower_case
    # input: string to be converted to lower case (str)
    # returns: string all in lower case (str)
    return string.lower()
    
## Q2: Write a function to remove punctutation from a string
## The punc string contains all of the punctuation marks that need to removed
## The easiest way to do this is to use the str.replace() function, which takes
## two arguments - the string to be replaced and the string to replace it with
def remove_punctuation(string):
    # name: remove_punctuation
    # input: string to have punctuation removed
    # returns: string without punctuation (str)
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for p in punc:
        string = string.replace(punc, "")
    
    return string

## Q3: Write a function to tokenize a string
## It should take a string, split it using a separator, and then return
## a list of strings containing each of the tokens from the text
def tokenize(string, sep = ' '):
    # name: tokenize
    # input: string to be tokenized (str)
    #        sep, optional separator parameter with default ' ' (str)
    # returns: token list, (list of str)
    return string.split(sep)

## Q4: Write a function to stopwords from a list of string tokens
## It should take a list of strings that have been tokenized from a document,
## and a list of stop words. 
## It should return a list which has the stop words removed from it
def remove_stopwords(tokens, stopwords):
    # name: remove_stopwords
    # input: list of string tokens (list of str)
    # returns: list of string tokens with stopwords removed (list of str)
  lst = []
  for token in tokens:
      if token not in stopwords:
          lst.append(token)
  
  return lst

## Q5: Write a function to build a vocabulary from a given text corpus 
## The vocabulary will create two dictionaries and a list. They are:
## - word_count, which will have a word as a key and the word count as value
## - word2index, which will have a word as a key and the index number as value
## - index2word, a list of words where the list index corresponds to the index
## Word2index and index2word allow use to go back and forth between two
## ways of representing the data
## The function should take a corpus - a list of lists of strings
## It will return the two dictionarys and list
## It should go through the corpus list, with each item containing a document
## which has been cleaned and tokenized
## Then, go through each token in the text entry and...
## - See if it exists in the word2index dictionary. If it doesn't, then
##      add it to the dictionary with a value equal to the length of the 
##      index2word list. Then, append it to the index2word list
## - See if it exists in the word count dictionary. If it does, increase its 
##       counter. If it doesn't, add it and set it to one
## Have it return a dictionary with key-values for:
##  'word_count'
##  'word2index'
##  'index2word'
## correpsonding to these values
def build_vocabulary(corpus):
    # name: build_vocabuary
    # input: cleanaed tokenized text corpus, (list of lists of str)
    # returns: dictionary with three keys:
    #  'word_count' : a dictionary of the word counts for the corpus
    #  'word2index' : a dictionary of words to index
    #  'index2word' : a list of index to words
    word_count = {}
    # word as a key and the word count as value
    
    word2index = {}
    #word as a key and the index number as value
    
    index2word = []
    #list of words where the list index corresponds to the index
   
    
    for document in corpus:
        for token in document:
            if token in index2word:
                word_count[token] += 1
        
            else:
                word_count[token] = 1
                word2index[token] = len(index2word)
                index2word.append(token)
                
    return {'word_count': word_count, 'word2index': word2index, 'index2word': 
            index2word}


## Q6: Read in the Yelp reviews using the read_csv_file function
## Create an empty list for the cleaned text
## Then loop through the reviews, and for each review:
## - First, put the text of the review (the 'text' key in the dict) into a variable
## - Then, make it lower case and remove punctuation
## - Then, tokenize it, creating a new variable for the tokens list
## - Then, remove the stop words, using the STOP_WORD_LIST
## - Append it to the cleaned text list
##
## Then, create a vocabulary using the build_vocab function
## Sort the word counts list using the following code, replacing "my_vocabulary"
## with the name of the vocabulary you created
## sorted(my_vocabulary['word_count'].items(), key=lambda x:x[1], reverse=True)
## Print out the 100 most popular words in the reviews set

def main():
    
    csv = read_csv_file(YELP_REVIEWS)
    
    cleaned_text = []
    for line in csv:
        review = line['text']
        review = to_lower_case(review)
        review = remove_punctuation(review)
        token = tokenize(review, sep = ' ')
        remove_stopwords(token, STOP_WORDS_LIST)
        cleaned_text.append(token)
    
    vocabulary = build_vocabulary(cleaned_text)
    sorted(vocabulary['word_count'].items(), key = lambda x:x[1], reverse = 
           True)
    
    for key,values in vocabulary.items():
        print(key[:99])
    

    
        
    

main()