#  Implement a program that prompts the user for an arithmetic expression 
# and then calculates and outputs the result as a floating-point value formatted to one decimal place. 
# Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:
# x is an integer
# y is +, -, *, or /
# z is an integer
# For instance, if the user inputs 1 + 1, your program should output 2.0. 
# Assume that, if y is /, then z will not be 0

def main():
    expression = input("Enter the arithmatic expression (x y z) : ").strip()

    try:
        # Split the input and assign the x and z values to an int variable
        x_str, op, z_str = expression.split(" ")
        x = int(x_str)
        z = int(z_str)

        match op:
            case "+":
                result = x + z
            case "-":
                result = x - z
            case "*":
                result = x * z
            case "/":
                result = x / z
            case _:
                result = None

        # print the result
        print(f"Result is {result:.1f}")
    
    except:
        print("Invalid input. Please enter as: x operator z (e.g. 1 + 2)")

main()
