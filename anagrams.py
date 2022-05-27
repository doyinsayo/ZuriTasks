# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word1, word2):
    # [assignment] Add your code here
    if len(word1) == len(word2):
        if sorted(word1) == sorted(word2):
            return True
        else:
            return False
    else:
        return False


word1 = str(input("enter word1:"))
word2 = str(input("enter word2:"))
print(find_anagram(word1, word2))
