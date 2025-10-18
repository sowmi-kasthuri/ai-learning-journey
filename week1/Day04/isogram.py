# Determine if a word or phrase is an isogram.
# An isogram (also known as a "non-pattern word") is a word or phrase without a repeating letter, 
# however spaces and hyphens are allowed to appear multiple times.

def is_isogram(string):
    string = string.lower() # convert to lower case
    letters = [ch for ch in string if 'a' <= ch <= 'z'] # create a list with all chars between a to z.  special chars ignored.
    return len(set(letters)) == len(letters) # set(letters) only takes the unique chars in the list letters
