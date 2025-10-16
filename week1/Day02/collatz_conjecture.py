# Given a positive integer, return the number of steps it takes to reach 1 according to the rules of the Collatz Conjecture.

def steps(number):
    """
    Returns the number of steps required to reach 1 from number using the Collatz process.
    number must be a positive integer.
    """
    # check if the input number is an integer (isinstance) and is a positive number
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Input must be a positive integer.")
    
    # Initiate step counter
    steps_count = 0

    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
        steps_count += 1
    return steps_count

def main():
    print("Collatz Conjecture Interactive")
    while True:
        user_input = input("Enter a positive integer (or 'q' to quit): ").strip()
        if user_input.lower() == 'q':
            print("Goodbye!")
            break
        try:
            num = int(user_input)
            print(f"It takes {steps(num)} steps to reach 1.\n")
        except ValueError as e:
            print(f"Error: {e}\n")

if __name__ == "__main__":
    main()
