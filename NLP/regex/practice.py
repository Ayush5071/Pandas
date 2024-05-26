import re
regexp = re.compile(r"^ab[^\s]*cd$")

phrases = ["abcd","xxx","abxxxxxcd","ab cd"]
matches = []
for phrase in phrases :
    if re.match(regexp,phrase):
        matches.append(phrase)
print(matches)