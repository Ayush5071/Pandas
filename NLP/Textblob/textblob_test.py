from textblob import TextBlob
phrase = "Simple is worst dirty than omplex"
tb_phrase = TextBlob(phrase)
print(tb_phrase)
print(tb_phrase.correct())
print(tb_phrase.sentiment)

