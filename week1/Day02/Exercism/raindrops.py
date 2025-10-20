'''

Convert a number into its corresponding raindrop sounds.
If a given number:
    is divisible by 3, add "Pling" to the result.
    is divisible by 5, add "Plang" to the result.
    is divisible by 7, add "Plong" to the result.
    is not divisible by 3, 5, or 7, the result should be the number as a string.

'''

def raindrops(number):
    # Error handling: input must be an integer
    if not isinstance(number, int):
        raise ValueError("Input must be an integer.")
    if number == 0:
        raise ValueError("Input must be a non-zero integer.")

    result = ""
    if number % 3 == 0:
        result += "Pling"
    if number % 5 == 0:
        result += "Plang"
    if number % 7 == 0:
        result += "Plong"
    if result == "":
        result = str(number)
    return result

# Example usage
try:
    num = int(input("Enter an integer: ").strip())
    print(raindrops(num))
except ValueError as e:
        print("Error:", e)
