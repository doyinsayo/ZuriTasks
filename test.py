from collections import Counter

with open('test.txt', 'r') as f:
    counter = Counter()
    for line in f:
        counter.update(line.split())

print (counter)