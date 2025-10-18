def is_pangram(sentence):
    # Step 1: Make lowercase
    sentence = sentence.lower()
    # Step 2: Filter only 'a' to 'z'
    letters = set([ch for ch in sentence if 'a' <= ch <= 'z'])
    # Step 3: Check set size
    return len(letters) == 26
