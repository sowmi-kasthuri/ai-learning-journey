def square(number):
    """
    Returns the number of grains on the given square (1 to 64).
    Raises ValueError for invalid square numbers.
    """
    if not isinstance(number, int):
        raise ValueError("square must be an integer.")
    if not (1 <= number <= 64):
        raise ValueError("square must be between 1 and 64 inclusive.")
    return 2 ** (number - 1)

def total():
    """
    Returns the total number of grains on the chessboard.
    """
    return 2 ** 64 - 1

# Example usage (comment this out for submission on Exercism or when running pytest)
if __name__ == "__main__":
    try:
        n = int(input("Enter a square number (1-64): ").strip())
        print(f"Grains on square {n}: {square(n)}")
        print(f"Total grains on chessboard: {total()}")
    except ValueError as e:
        print("Error:", e)
