# CMSC/LING 208 Lab 1
# Name: Nitisha Bhandari

from __future__ import division
import re
import random
import collections
import operator

mydata = open('CreepyRoommateCorpus.txt','r').read().split()
#mydata = open('trumpSpeechCorpus.txt','r').read().split()


# This function splits the data into bigrams, and unigrams and gets the 
# counts for each of the bigrams and unigrams 
def get_counts(data):
   
   # Replace unicode with the appropriate puntuations 
   data = replaceUnicode(data)

   #print(data)

   bigrams =  {} 

   for n, i in enumerate(mydata):
      if i == '.' or i == '?' or i == '!' or i == "?'" or i == ".'":
         mydata[n] = '#'

      elif i == ',' or i == '-' or i == ';' or i == '--' or i == ':' or i == "'" or i == ')' or i == '(' or i == '"':
         mydata[n] = ''

   filtered = [x for x in mydata if len(x.strip()) > 0]   #remove empty strings 

   tuples = zip(filtered, filtered[1:])   #make tuples of two consecutive words 

   #print(data)

   for t in tuples :
      if t in bigrams:
         bigrams[t] += 1    
      else:
         bigrams[t] = 1
  
   unigrams = {}

   for x in filtered : 
      if x in unigrams:
         unigrams[x] += 1
      else:
         unigrams[x] = 1
 
   #print(bigrams)
   return bigrams,unigrams


# Get the probability of each bigram 
# Make each bigram and its probability a dictionary and append them to a list 
def bigram_model(data):
   
   bigrams,unigrams = get_counts(data)
   model = {}
   
   #print(bigrams)
   for key in bigrams:
    model[key] = float ((bigrams[key]) / ((unigrams[key[0]])))

   #print(model)
   return model

# This function generates sentences using the bigram model. 
# It first gets the bigrams that start with '#' and adds them to a list, and picks 
# a random one. 
# It then matches the second word in the bigram with the first word in other bigrams, 
# adds them to a list and picks a random one. 
# Finally, it puts all the bigrams with the last word '#' in a list and picks a 
# random one to end the sentence. 
def generate_sentence(model):
   
  sentence = ''
  sen_initials = []  #list to store the bigrams that start with '#'

  for x in model:     #initial bigram
    if x[0] == '#':
      sen_initials.append(x)

  prev = random.choice(sen_initials)
  
  sentence += prev[1]   #append first word to sentence
  
  seq = []            # stores the words in sequence

  for i in range(0, 20):
    wordsList = []    # stores the bigrams that start with a particular word
    for w in model.keys():
      if prev[1] == '#':
        continue
      elif w[1] == '#':
        continue
      elif prev[1] == w[0]:
        wordsList.append(w)
        nextWord = getBestBigram(wordsList, model)
        #nextWord = random.choice(wordsList)
    prev = nextWord

    #print(seq)
    seq.append(nextWord[1])

  # Keep appending to the sentence
  for s in seq:
    sequence = " ".join(seq)   

  sentence += " "
  sentence += sequence
  
  #ending bigram
  sentence_ends = []

  for x in model:     
    if x[1] == '#':
      sentence_ends.append(x)

  last = random.choice(sentence_ends)

  sentence += " "
  sentence += last[0]     #append last bigram to the sentence

  return sentence


# This function takes in the current list of bigrams and the original bigram model, 
# then picks out the top "n" bigrams with the highest probabiities, makes a list of 
# these bigrams, and then randomly picks one from this list. 
# If the current list (wordsList) does not have "n" bigrams, it picks one randomly 
# from the list. 
# It returns the bigram to use for the next word
# n = 5 for Trump Speech Corpus, and n = 7 for Roommate Stories Corpus
def getBestBigram(wordsList, model):
  
  maxList = []
  valuesList = []
  bestBigram = ''
  topValues = []

  for x in wordsList:
    valuesList.append(model[x])

  sorted_v = valuesList.sort(reverse=True)
  #print(sorted_v)

  if len(wordsList) < 7:
    bestBigram = random.choice(wordsList)
    
  else:
    for x in range(0,7):
      topValues.append(valuesList[x])

    for y in topValues:
      maxList.append(model.keys()[model.values().index(y)])
      
    bestBigram = random.choice(maxList)

  #print(bestBigram)
  return bestBigram

# This function replaces the unicodes with the actual characters 
def replaceUnicode(data):
   for w in data:

      data = [w.replace('\xe2\x80\xa4', '.')]
      data = [w.replace('\xe2\x81\xbd', '(')]
      data = [w.replace('\xe2\x81\xbe', ')')]
      data = [w.replace('\xe2\x80\x99', '\'')]
      data = [w.replace('\xe2\x80\x93', '-')]
      data = [w.replace('\xe2\x80\x99', "'")]
      data = [w.replace('\xc3\xa9', 'e')]
      data = [w.replace('\xe2\x80\x90', '-')]
      data = [w.replace('\xe2\x80\x91', '-')]
      data = [w.replace('\xe2\x80\x92', '-')]
      data = [w.replace('\xe2\x80\x93', '-')]
      data = [w.replace('\xe2\x80\x94', '-')]
      data = [w.replace('\xe2\x80\x94', '-')]
      data = [w.replace('\xe2\x80\x98', "'")]
      data = [w.replace('\xe2\x80\x9b', "'")]
      data = [w.replace('\xe2\x80\x9c', '"')]
      data = [w.replace('\xe2\x80\x9d', '"')]
      data = [w.replace('\xe2\x80\x9e', '"')]
      data = [w.replace('\xe2\x80\x9f', '"')]
      data = [w.replace('\xe2\x80\xa6', '...')]
      data = [w.replace('\xe2\x80\xb2', "'")]
      data = [w.replace('\xe2\x80\xb3', "'")]
      data = [w.replace('\xe2\x80\xb4', "'")]
      data = [w.replace('\xe2\x80\xb5', "'")]
      data = [w.replace('\xe2\x80\xb6', "'")]
      data = [w.replace('\xe2\x80\xb7', "'")]
      data = [w.replace('\xe2\x81\xba', "+")]
      data = [w.replace('\xe2\x81\xbb', "-")]
      data = [w.replace('\xe2\x81\xbc', "=")]
      data = [w.replace('\xe2\x81\xbd', "(")]
      data = [w.replace('\xe2\x81\xbe', ")")]

   return data

def demo():
   mymodel = bigram_model(mydata)
   #grams = get_counts(mydata)
   #print('Probability of test sentence',get_sentence_probability(mymodel, sentence_to_test))
   print('Sample generated sentence',generate_sentence(mymodel))


if __name__ == "__main__":
   demo()