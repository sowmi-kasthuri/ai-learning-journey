# Implement a program that prompts the user for a vanity plate and 
# then output Valid if meets all of the requirements or Invalid if it does not. 
# Assume that any letters in the user’s input will be uppercase. 
# Structure your program per the below, wherein is_valid returns True if s meets all requirements 
# and False if it does not. Assume that s will be a str. 
# You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).

# define function for valid length
def valid_length(s):
    return 2 <= len(s) <=6

# define function for valid start 
def valid_start(s):
    return len(s) >= 2 and s[0].isalpha() and s[1].isalpha()

# define function for valid characters
def valid_characters(s):
    return all(ch.isalnum() for ch in s)

# define function for valid numbers
def valid_numbers(s):
    number_started = False
    for ch in s:
        if ch.isdigit():
            if not number_started and ch == '0':
                return False
            number_started = True
        elif number_started:
            return False
    return True

# define function for vanity check
def is_valid(s):
    if not isinstance(s, str):
        raise ValueError("Input must be string")
    if not valid_length(s):
        raise ValueError("Plate must be 2 to 6 characters")
    if not valid_start(s):
        raise ValueError("Plate must start with atleast 2 letters")
    if not valid_characters(s):
        raise ValueError("Plate can only contain letters and numbers.")
    if not valid_numbers(s):
        raise ValueError("Numbers must not be in the middle, or start with zero.")
    return True

# define function for main
def main():
    try:
        plate = input("Enter vanity plate: ").strip().upper()
        if is_valid(plate):
            print("Valid")
    except ValueError as e:
        print("Invalid: ",e)
    except Exception as e:
        print("Exception: ",e)


# call main
main()