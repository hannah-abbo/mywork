# -*- coding: utf-8 -*-
"""
DS2001 (S23-Matherly) Week 10

Rename this file as lastname_firstname_week10.py


@author: [YOUR NAME HERE]
"""



"""
This week, we'll be refactoring our code from last week into a more object
oriented form. You'll be creating two classes - corpus and vocabulary - which
will have the code we created last week modified slightly to be packaged in
this way.
"""

DELTA_REVIEWS = "delta.csv"


import csv

# Q1; Create corpus class
# It should have five methods (functions):
# - __init__, which creates the instance attributes for documents
#

class Corpus:
    # name: corpus
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
    
    def __init__(self, docs):
        # name: __init__
        # input: a list of text from documents (list of str)
        # Needs to create an instance attribute for documents, then use
        #  add_document to parse each one
        
        self.documents = []
        
        for doc in docs: 
            self.add_document(doc)
            
    
    def remove_punctuation(self, string):
        # name: remove_punctuation
        # input: string to have punctuation removed
        # returns: string without punctuation (str)
        self.string = string
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for p in punc:
            string = string.replace(punc, "")
        
        return string

    
    def tokenize(self, string, sep = ' '):
        # name: tokenize
        # input: string to be tokenized (str)
        #        sep, optional separator parameter with default ' ' (str)
        # returns: token list, (list of str)
        self.string = string
        return string.split(sep)

    def remove_stopwords(self, tokens, stopwords):
        # name: remove_stopwords
        # input: list of string tokens (list of str)
        # returns: list of string tokens with stopwords removed (list of str)
        lst = []
        self.tokens = tokens
        self.stopwords = stopwords 
        
        for token in tokens:
            if token not in stopwords:
              self.lst.append(token)
      
        return lst
  
    def to_lower_case(string):
        return string.lower()
    
    def add_document(self, document):
        # name: add_document
        # input: document (str)
        # returns: list of string tokens with stopwords removed (list of str)
        doc = remove_punctuation(document)
        doc = to_lower_case(doc)
        doc = tokenize(doc)
        doc = remove_stopwords(doc)

        self.documents.append(doc)
        
        
    
# Q2: Create vocabulary class
# It should have six methods (functions):
# - __init__, which creates the instance attributes for word_count, word2index and index2word
# - lookup_word, which takes a word and returns the index if it has been seen
# - lookup_index, which takes an index and return the matching word if it exists
# - parse_document, which takes a tokenized document and adds word to vocabulary
# - parse_corpus, which takes a corpus and parses its documents
# - most_common_words, which returns the 10 most common words in the vocabulary

class Vocabulary:
   
    def __init__(self, word_count, word2index, index2words):
        # name: __init__
        # input: nothing
        # Creates object specific (using self.) dictionaries for word_count,
        #   word2index and index2word
        self.word_count = {}
        self.word2index = {}
        self.index2word = []
        
    def lookup_word(self, word):
        # name: lookup_word
        # input: word (str)
        # returns: index value corresponding to word (int), None if not found
        if word in index2word:
            return index2word[word]
        else: 
            return None

        
    def lookup_index(self, index):
        # name: lookup_index
        # input: index (int)
        # returns: word corresponding to index value (str), None if not found
        if index <= len(index2list)
            return index2word[word]
        else: 
            return None

    def parse_document(self, document):
        # name: parse_document
        # input: a tokenized string (list of str)
        # output: none
        # - If preprocess is False, the document should be a list of tokens 
        #   (list of str)
        
                
    def parse_corpus(self, corpus, verbose=False):
        # name: parse_corpus
        # input: A corpus object
        #        verbose, whether or not to output progress to screen (bool)
        # output: none
        # 

       
    def most_common_words(self, n = 10):
        # name: most_common_words
        # input: number of words to return (int)
        # output: return the n most common words in the corpus and the number 
        #  of times they occur (list of dicts)


## Same read_csv_file we've used before
def read_csv_file(filename):
    # name: read_csv_file
    # input: filename (str)
    # returns: contents of the file, (list of str)
    lst = []
    
    csvfile = csv.DictReader(open(filename))
    for line in csvfile:
        lst.append(line)
    return lst


# Q3: Parse the Delta reviews
# - Read in the Delta reviews using the read_csv_file function
# - Create an empty list for the cleaned text, pull the text of the review out
#    from the list of reviews, and put it in the empty list
# - Create a new corpus object with the cleaned text
# - Create a new vocabulary object, then use the parse_corpus member function to
#    parse it
# - Print out the 20 most common words in the vocabulary
# - And print out how many words total are in the vocabulary



def main():
    mycorpus = corpus(docs)
    
    


main()