# Implement a program that prompts the user for the name of a variable in camel case and 
# outputs the corresponding name in snake case. 
# Assume that the user’s input will indeed be in camel case.
# no need to check for all lower cases


# define camel_to_snake conversion
def camel_to_snake(camel):
    if not isinstance(camel, str):
        raise ValueError("Input must be a string.")
    
    if camel.strip() == "":
        raise ValueError("Input cannot be empty.")
    
    if not any(ch.isalpha() for ch in camel):
        raise ValueError("Input must contain at least one letter.")

    snake = ""
    for c in camel:
        if c.isupper():
            snake += "_" + c.lower()
        else:
            snake += c
    return(snake)


# get user input
try:
    camel_case = input("Enter user name in camel case: ").strip()
    snake_case = camel_to_snake(camel_case)
    print("Snake case is : ", snake_case)
except ValueError as e:
    print("Error", e)
