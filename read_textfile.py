# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    f = open("./story.txt", "r")
    print(f.read())
    return "Hello World"


def count_words():
    #text = read_file_content("./story.txt")
    text = open('./story.txt', 'r').read().split
    # [assignment] Add your code here
    words = {}
    for w in text:
        if w not in words:
            words[w] = 1
        else:
            words[w] += 1

    return words        
    #return {"as": 10, "would": 20}
