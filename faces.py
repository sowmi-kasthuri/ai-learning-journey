# Implement a function called convert that accepts a str as input and 
# returns that same input with any :) converted to 🙂 (otherwise known as a slightly smiling face) 
# and any :( converted to 🙁 (otherwise known as a slightly frowning face). 
# All other text should be returned unchanged.
def convert(user_input):
    return user_input.replace(":)", "🙂").replace(":(", "🙁")
    # return user_input.replace(":)", "🙂").replace(":(", "☹️"
    
def main():
    user_input = input("Please enter some text: ") or "No input provided"
    print(convert(user_input))

main()
