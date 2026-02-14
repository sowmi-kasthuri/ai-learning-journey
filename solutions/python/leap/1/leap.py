def leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Only run this part for interactive/demo, not during pytest
if __name__ == "__main__":
    try:
        year = int(input("Enter a year: ").strip())
        if leap_year(year):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    except ValueError:
        print("Invalid input. Please enter a valid year (integer).")
