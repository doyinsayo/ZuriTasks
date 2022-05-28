# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
from collections import Counter

with open('test.txt', 'r') as f:
    counter = Counter()
    for line in f:
        counter.update(line.split())

print (counter)
