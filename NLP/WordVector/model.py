### INSIGHTS -> Word embeddings are dense vector representations of text that capture the semantic meaning of words and phrases.
### When you convert the sentence "i hate the story" to its vector representation using spaCy, it creates a numerical vector 
### that encapsulates the meaning of the sentence based on the training it received on a large corpus.
### Similar sentences or sentences with related meanings will have similar vector representations in this high-dimensional space.

import spacy
from sklearn import svm

# Load the spaCy model
nlp = spacy.load("en_core_web_md")

class Category:
    BOOKS = "BOOKS"
    CLOTHING = "CLOTHING"

# Training data
train_x = ["i love the book", "this is a great book", "the fit is great", "i love the shoes"]
train_y = [Category.BOOKS, Category.BOOKS, Category.CLOTHING, Category.CLOTHING]

# Convert training data to word vectors
train_x_word_vectors = [nlp(text).vector for text in train_x]

# Initialize and train the SVM classifier
clf_svm_wv = svm.SVC(kernel="linear")
clf_svm_wv.fit(train_x_word_vectors, train_y)

# Print the word embedding representation of the first training example
print("Word embedding for the first training example:")
print(train_x_word_vectors[0])

# Test data
test_x = ["i hate the story"]
test_x_word_vectors = [nlp(text).vector for text in test_x]

# Predict the category of the test data
predicted_category = clf_svm_wv.predict(test_x_word_vectors)

# Output the predictions
print("Predicted category for the test data:")
print(predicted_category)
