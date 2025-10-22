'''
implement a program that:

Prompts the user for a level, 𝑛. 
If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and 𝑛, inclusive, using the random module.
Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
    If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
    If the guess is larger than that integer, the program should output Too large! and prompt the user again.
    If the guess is the same as that integer, the program should output Just right! and exit.
'''
# import necessary packages
import random

# define function to check positive integer
def get_positive_integer(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num <=0:
                raise ValueError("Number must be positive")
            return num
        except ValueError as e:
            print("Invalid input: {e}")

# define main
def main():
    try:
        level = get_positive_integer("Level: ")
        number = random.randint(1,level)

        while True:
            try:
                guess = get_positive_integer("Guess: ")
                if guess < number:
                    print("Too Small")
                elif guess > number:
                    print("Too Large")
                else:
                    print("Just Right")
                    break
            except Exception as e:
                print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error : {e}")


# call main
if __name__ == "__main__":
    main()