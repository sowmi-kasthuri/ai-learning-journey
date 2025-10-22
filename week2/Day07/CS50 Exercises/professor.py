'''
Implement a program that:

Prompts the user for a level, 𝑛. If the user does not input 1, 2, or 3, 
    the program should prompt again.

Randomly generates ten (10) math problems formatted as X + Y = , 
    wherein each of X and Y is a non-negative integer with 𝑛 digits. 
    No need to support operations other than addition (+).

Note: The order in which you generate x and y matters. 
    Your program should generate random numbers in x, y pairs 
    to simulate generating one math question at a time (e.g., x0 with y0, x1 with y1, and so on).

Prompts the user to solve each of those problems. 
    If an answer is not correct (or not even a number), 
    the program should output EEE and prompt the user again, 
    allowing the user up to three tries in total for that problem. 
    If the user has still not answered correctly after three tries, 
    the program should output the correct answer.

The program should ultimately output the user’s score: 
    the number of correct answers out of 10.

Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) 
    the user for a level and returns 1, 2, or 3, and 
    generate_integer returns a single randomly generated non-negative integer with level digits 
    or raises a ValueError if level is not 1, 2, or 3:
'''

# import required functions
import random

# define the get level function
def get_level():
    while True:
        try:
            level = int(input("Level (1,2,3): "))
            if level in [1,2,3]:
                return level
        except ValueError:
            pass

# define the get integer function
def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    elif level == 3:
        return random.randint(100,999)
    else:
        raise ValueError("Invalid Level")


# define main
def main():

    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        tries = 0

    while tries < 3:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == x + y:
                score += 1
                break
            else:
                print("EEE")
                tries += 1
        except ValueError:
            print("EEE")
            tries += 1
        
        else:
            # 3 failed attempts
            print(f"{x} + {y} = {x + y}")
    print(f"Score = {score}")
            
# call main - main entry point
if __name__ == "__main__":
    main()