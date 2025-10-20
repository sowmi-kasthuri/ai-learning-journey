# CS50 Exercise
# implement a program that prompts the user for a fraction, formatted as X/Y, 
# wherein each of X and Y is a positive integer, and then outputs, 
# as a percentage rounded to the nearest integer, how much fuel is in the tank. 
# If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. 
# And if 99% or more remains, output F instead to indicate that the tank is essentially full.
# If, though, X or Y is not an integer, X is greater than Y, or Y is 0,
# instead prompt the user again. (It is not necessary for Y to be 4.) 
# Be sure to catch any exceptions like ValueError or ZeroDivisionError.

#Define main
def main():
    user_input = input("Enter the fraction in the format x/y (both integers): ")
    try:
        parts = user_input.strip().split("/")
        if len(parts) != 2:
            raise ValueError("Enter the fraction in the format x/y (both integers)")
        
        # convert both parts to integer
        x = int(parts[0])
        y = int(parts[1])

        # Check for zero division
        if y == 0:
            raise ZeroDivisionError ("Denominator cannot be zero")
        
        # Calculate %
        percentage = int((x / y) * 100)

        # check for E and F
        if percentage < 1:
            print("E")
        elif percentage > 99:
            print("F")
        else:
            print(f"Percentage - {percentage}%")
    except ValueError:
        print("Both X and Y must be integers in the format X/Y")
    except ZeroDivisionError:
        print("Error: Denominator cannot be zero")

main()