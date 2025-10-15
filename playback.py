# Implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods).
def replace_spaces_with_dots(user_input):
    return user_input.replace(" ", "......")

def main():
    user_input = input("Please enter some text: ")
    print('Your input is -->',user_input)
    modified_input = replace_spaces_with_dots(user_input)
    print('Modified input is -->',modified_input)

main()
