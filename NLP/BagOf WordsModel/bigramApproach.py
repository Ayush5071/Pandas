# BIGRAM APPROACH TO CLASSIFY i.e. TAKE ONE WORD AT A TIME IN TEXT.......
# when we have 2 phrases like something is book or is not book ,than bigram aproach is super usefull
class Category:
    BOOKS = "BOOKS"
    CLOTHING = "CLOTHING"

from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm

train_x = ["i love the book","this is a great book","the fit is great","i love the shoes"]
train_y = [Category.BOOKS,Category.BOOKS,Category.CLOTHING,Category.CLOTHING]

vectorizer = CountVectorizer(binary=True,ngram_range=(1,2))
train_x_vectors = vectorizer.fit_transform(train_x)
print(vectorizer.get_feature_names_out())
print(train_x_vectors.toarray())

