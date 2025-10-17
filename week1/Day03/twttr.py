# Implement a program that prompts the user for a str of text and 
# then outputs that same text but with all vowels (A, E, I, O, and U) omitted, 
# whether inputted in uppercase or lowercase

# define function to remove vowels
def remove_vowels(text):
    # check for non alphabets
    if not isinstance(text, str):
        raise ValueError("Input must be a string.")
    # check for empty inputs
    if text.strip() == "":
        raise ValueError("Input cannot be empty.")
    #check for numeric inputs
    if any(ch.isdigit() for ch in text):
        raise ValueError("Input should not contain numbers.")
    vowels = "aeiouAEIOU"
    result = ""
    for ch in text:
        if ch not in vowels:
            result += ch
    return result    

# define main
def main():
    try:
        user_text = input("Enter any text: ").strip()
        no_vowels = remove_vowels(user_text)
        print("Text without vowels: ", no_vowels)
    except ValueError as e:
        print("Invalid input: ", e)

# call main
main()