import nltk
from nltk import word_tokenize
#nltk.download()
dir(nltk)
inputTxt= "I am new to NLTK"
wordToken = word_tokenize(inputTxt)
print(inputTxt)
print(wordToken)