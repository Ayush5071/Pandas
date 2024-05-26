from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

stop_words = stopwords.words('english') # all 179 stop words that are present in english 

# print(len(stop_words))

phrase = "Here is an example sentence demonstrating the removal of stop words"

words = word_tokenize(phrase)

stripped_phrase = []

for word in words :
    if word not in stop_words:
        stripped_phrase.append(word)
print(" ".join(stripped_phrase))
