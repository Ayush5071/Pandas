# UNIGRAM APPROACH TO CLASSIFY i.e. TAKE ONE WORD AT A TIME IN TEXT.......
class Category:
    BOOKS = "BOOKS"
    CLOTHING = "CLOTHING"

from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm

train_x = ["i love the book book book","this is a great book book","the fit is great","i love the shoes"]
train_y = [Category.BOOKS,Category.BOOKS,Category.CLOTHING,Category.CLOTHING]

vectorizer = CountVectorizer(binary=True)
train_x_vectors = vectorizer.fit_transform(train_x)

clf_svm = svm.SVC(kernel="linear")
clf_svm.fit(train_x_vectors,train_y)
print("***************** VECTORIZATION **************************")
print(vectorizer.get_feature_names_out())
print(train_x_vectors.toarray())
print("***************** CLASSIFICATION **************************")
test_x = vectorizer.fit_transform(["i like the clean book"])
print(test_x.get_feature_names_out())
print(test_x)
print(clf_svm.predict(test_x))
# HANDLING THE TIME WHEN THE WORD IN TEST TEXT ,NOT PRESENT IN TRAINING DATA 


