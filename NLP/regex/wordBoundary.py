import re

# regexp = re.compile(r"story|book|read")
regexp = re.compile(r"\bread\b|\bhistory\b|\bbook\b") # using word boundary(\b)

phrases = ["i liked the history","the car treaded up the hill",'Tthis hat is nice']

matches = []
for phrase in phrases :
    if re.search(regexp,phrase):
        matches.append(phrase)

print(matches)
