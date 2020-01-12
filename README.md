# Bigram Language Model 

*This is my final project for Speech Synthesis and Recognition class.* 

<br>
A bigram language model considers only the latest word to predict the next word. For example: if the sentence is "I love my ___",
then the sentence is split into bigrams like: [#, I], [I, love], [love, my], [my, #] where # indicates the beginning and end of the sentences. 
The model then looks into it's text corpus and calculates probabilities for all the bigrams where the first index is "my" and 
uses the word with the highest probability to predict what comes after my in the given sentence. The answer will vary depending on the corpus. 
It could be "dog", "life", "wife" anything, whichever appears the most in the given corpus. 

<br>

This model finds the bigrams with the top 5 or 7 probabilities and randomly picks one bigram from the lot and uses the second index
as the next predicted word. 

<br> 

This model is not accurate, as the accuracy of the generated sentences depends on many factors, one of which is 
how big or small the corpus is. 

## To Use: 

* Two corpora are uploaded in the file either download those, or use your own corpus and change the name of the file in the code. 
* Change the top-n probabilities if you wish to. 
