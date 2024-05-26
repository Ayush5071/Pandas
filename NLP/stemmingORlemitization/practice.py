# stemming or  lemitization
# words/word are taken in same in a dictionary..similar words are taken same 

import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

phrase = "reading the books"
words = word_tokenize(phrase)
stemmed_words = []
for word in words:
    stemmed_words.append(stemmer.stem(word))
print(" ".join(stemmed_words))

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
lemmatized_words = []

for word in words :
    lemmatized_words.append(lemmatizer.lemmatize(word,pos='v'))# telling the words are verb also

print(" ".join(lemmatized_words))

