def is_armstrong_number(number):
    num = str(number)
    num_digits = len(num)
    total = 0
    for digit in num:
        total += int(digit) ** num_digits
    return total == number
