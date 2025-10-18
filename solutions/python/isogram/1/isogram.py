def is_isogram(string):
    string = string.lower() # convert to lower case
    letters = [ch for ch in string if 'a' <= ch <= 'z'] 
    return len(set(letters)) == len(letters)

    
