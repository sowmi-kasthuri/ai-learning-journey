# function to check if a sentence is a pangram ..i.e. contains all letters in an alphabet

def is_pangram(sentence):
    # Step 1: Make lowercase
    sentence = sentence.lower()
    # Step 2: Filter only 'a' to 'z'
    letters = set([ch for ch in sentence if 'a' <= ch <= 'z'])
    # Step 3: Check set size
    return len(letters) == 26


# same using a list

def is_pangram(sentence):
    sentence = sentence.lower()
    letters = []
    for ch in sentence:
        if 'a' <= ch <= 'z' and ch not in letters:
            letters.append(ch)
    return len(letters) == 26