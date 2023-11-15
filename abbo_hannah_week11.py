# -*- coding: utf-8 -*-
"""
DS2001 (S23-Matherly) Week 11

Rename this file as lastname_firstname_week11.py


@author: [YOUR NAME HERE]
"""



"""
This week, we'll be extending our text analysis to a document term matrix and
term frequencies, and using this to identify similar texts.
"""

GAME_DESCRIPTIONS = "games.csv"


import csv
import math

# Q1; Create corpus class
# It should have five methods (functions):
# - __init__, which creates the instance attributes for documents
#
class corpus:
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
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in punc:
            string = string.replace(char, '')
        return string

    
    def tokenize(self, string, sep = ' '):
        # name: tokenize
        # input: string to be tokenized (str)
        #        sep, optional separator parameter with default ' ' (str)
        # returns: token list, (list of str)
        return string.split(sep)

    def remove_stopwords(self, tokens, stopwords):
        # name: remove_stopwords
        # input: list of string tokens (list of str)
        # returns: list of string tokens with stopwords removed (list of str)
        out = []
        for token in tokens:
            if token not in stopwords:
                out.append(token)
        return out

    
    def add_document(self, document):
        # name: add_document
        # input: document (str)
        # returns: nothing
        # Cleans the document including putting it all in lower case, removing
        #  punctuation, tokenizing and removing stopwords, using the member
        #  functions of the class.
        #  Then, it should append the document to the document list that the
        #  init function creates
        doc = document.lower()
        doc = self.remove_punctuation(doc)
        doc = self.tokenize(doc)
        doc = self.remove_stopwords(doc, self.STOP_WORDS_LIST)
        self.documents.append(doc)

    
# Q2: Create vocabulary class
# It should have six methods (functions):
# - __init__, which creates the instance attributes for word_count, word2index and index2word
# - lookup_word, which takes a word and returns the index if it has been seen
# - lookup_index, which takes an index and return the matching word if it exists
# - parse_document, which takes a tokenized document and adds word to vocabulary
# - parse_corpus, which takes a corpus and parses its documents
# - most_common_words, which returns the 10 most common words in the vocabulary

class vocabulary:
   
    def __init__(self):
        # name: __init__
        # input: nothing
        # Creates object specific (using self.) dictionaries for word_count,
        #   word2index and index2word
        self.word_count = {}
        self.doc_frequencies = {}
        self.word2index = {}
        self.index2word = []
        self.vocabulary_length = 0

          
    def lookup_word(self, word):
        # name: lookup_word
        # input: word (str)
        # returns: index value corresponding to word (int), None if not found
        if word in self.index2word:
            return self.word2index[word]
        else:
            return None

        
    def lookup_index(self, index):
        # name: lookup_index
        # input: index (int)
        # returns: word corresponding to index value (str), None if not found
        if index <= len(self.index2word):
            return self.index2word[index]
        else:
            return None

    def parse_document(self, document):
        # name: parse_document
        # input: a tokenized document (list of str)
        # output: none
        # Parses a document that has been tokenized, going through the words
        #  and updating the word_count, word2index and index2word attributes
        for token in document:
            if token not in self.word2index:
                self.word2index[token] = len(self.index2word)                
                self.index2word.append(token)
                self.vocabulary_length += 1
                
            if token in self.word_count:
                self.word_count[token] += 1
            else:
                self.word_count[token] = 1
            

                
    def parse_corpus(self, corpus, verbose=False):
        # name: parse_corpus
        # input: A corpus object
        #        verbose, whether or not to output progress to screen (bool)
        # output: none
        # Uses the parse_document function to go through a corpus, which is
        #  a set of tokenized documents
        counter = 1
        for doc in corpus:
            self.parse_document(doc)
            if verbose:
                print("\r{}/{} processed.".format(counter, 
                                                  len(corpus)), end='')
            counter+=1
       
    def most_common_words(self, n = 10):
        # name: most_common_words
        # input: number of words to return (int)
        # output: return the n most common words in the corpus and the number 
        #  of times they occur (list of dicts)
        sorted_wordcounts = sorted(self.word_count.items(), 
                                   key=lambda x:x[1], reverse=True)
        return(sorted_wordcounts[:n])

    
# Q1: Create a document term matrix class
## Has two functions:
## __init__, which creates an instance of the class from a corpus
## tfrow2text, which takes a row from the term-frequency matrix and converts it
##  to a dictionary with the words and their frequencies
class document_term_matrix:
    
    def __init__(self, corpus):
        # name: __init__
        # input: corpus (corpus)
        # Initializes variables and creates the document-term matrix
        self.corpus = corpus
        self.vocabulary = vocabulary()
        self.vocabulary.parse_corpus(self.corpus.documents)
        
        ## First, need to create a variable to store the corpus in the DTM
        ## Then, reate a vocabulary object for the DTM, and use it to parse 
        ## the corpus
        
        
        ## Create two empty lists which will be used to create 2D lists for
        ## the document term matrix and term frequency matrix 
        self.dtm = []
        self.tfm = []
        
        ## Create a list of called doc_counts that will keep track of how many
        ## documents a word from the vocabulary appears in.
        ## It will have the same length as the vocabulary, and should be all 
        ## zeros to start with.
        ## A list of zeros can be created by multiplying a single element list
        ## [0] by the number of elements that are needed.
        ## E.g., a list of ten zeros can be created as [0] * 10
        
        self.doc_counts = [0] * self.vocabulary.vocabulary_length
            
        ## Last, create an empty list that will hold the length of each document
        self.doc_length = []

        ## Iterate over every document in the set of corpus.documents
        ## For each document:
        ## - Append the length of the document to doc_lengths
        ## - Create a list doc_indexes of all zeros that is vocabulary length
        ## - Create an empty list unique_words
        
        for document in self.corpus.documents:
            self.doc_lengths.append(len(document)) # how many tokens were in this odc
            doc_indexes = [0] * self.vocabulary.vocabulary_length 
            unique_words = []                  
        ## Then, loop over every word in the document and:
        ## - Increment the value of the index in doc_indexes 
        ## - See if the word is in the document's unique words list. If not, 
        ##   add it to the list.
            for word in document: 
                index = self.vocabulary.lookup_word(word)
                doc_indexes[index] += 1
                if word not in unique_words: 
                    unique_words.append(word)
                
            self.dtm.append(doc_indexes)
               
        ## After looping through all the words in the document, create the list
        ## dtf, which will hold the term frequencies for the document, by 
        ## dividing the number of times the word appeared in the document 
        ## (from the list dt) and dividing it by the number of words in the document
        ## Append the dt list to dtm, and the dtf list to tf 
        ## Last, go through all the words in unique_words, and increment the
        ## counters in doc_counts to keep track of how many times each word
        ## appeared in one of the documents
            td_row = [x / len(document) for x in doc_indexes]
            self.tdm.tfm.append(td_row)
            
            for word in unique_words:
                index = self.vocabulary.lookup_word(word)
                self.doc_counts[index] += 1
         
    def tfrow2text(self, tf_row):
        # name: dtmrow2text
        # input: dtm_row (list of numeric values))
        # returns: a dictionary of words present in the row and their values
        
        ## This will take a list from term frequency matrix, and return a 
        ## dictionary with the words that are present in the row and the 
        ## associated term frequency for that row 
        
        ## Create an empty dictionary, then use a for loop with a counter to
        ## go through every value in the dtm_row, and see if it is greater than
        ## zero. If so, then add a key for the matching word, and give it a
        ## value for the frequency, then return the dictionary

    


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

def cosine_similarity(row1, row2):
    # name: cosine_similarity
    # input: row1, row2 (list of numerics)
    # returns: cosine similarity of two vectors (float)
    sumxx = 0
    sumxy = 0
    sumyy = 0
    for i in range(len(row1)):
        sumxx += row1[i] * row1[i]
        sumyy += row2[i] * row2[i]
        sumxy += row1[i] * row2[i]
    return sumxy/pow(sumxx * sumyy, .5)

# Q2: Recommend some games
# - Read in the game descriptions using the read_csv_file function
# - Create an empty list for the summary text, pull the text of the sumamary out
#    from the list ['summary'], and put it in the empty list
# - Create a new corpus object using the list of game summaries
# - Create a new dtm object from the corpus
# - Pick a game you like and set it as the target game
# - Create an empty list of similarities, and then use a for i in range loop
#   to go through each of the games in the list, and create a dictionary
#   containing the name of the game (from the list of lines read in the from
#   games file, this will be in the 'title' column) and the cosine similarity
#   for that game, by passing the term frequency row from the dtm for the target
#   game and every other game to the cosine_similarity function
# - Then, use the sorted function below to sort the games, and neatly print out
#   the top ten most similar games 


def main():
    file = read_csv_file(GAME_DESCRIPTIONS)
    l = []
    for row in file:
        l.append(row["summary"])
        
    corp = corpus(l) # docs that we want to look at 
    dtm = document_term_matrix(corp) # create a dtm from those docs 
    

    # Here's indexes for a few popular games.
    # 686 Death Stranding
    # 687 Doom Eternal
    # 688 Final Fantasy XVI
    # 691 The Legend of Zelda: Breath of the Wild
    # 693 God of War
    # 698 Marvel's Spider-Man: Miles Morales
    # 700 Red Dead Redemption 2
    # 701 Cyberpunk 2077
    # 702 Metal Gear Rising: Revengeance
    # 714 Metroid Dread
    # 718 NieR: Automata
    # 723 Elden Ring
    
    # Pick one of these games, and then use that row's values as the target 
    # for your cosine similarity calculation

    target_game = 691
    
    sims = []
    for i in range(len(file)): 
        d = {"game" : file[i]["title"],
             "similarity" : cosine_similarity(dtm.tfm[target_game],
                                              dtm.tfm[i])}
        sims.append(d)
        
    sorted_games = sorted(sims, key=lambda d: d['similarity'], reverse=True)
    print(sorted_games[1:10])
           

        
    
    
    


main()