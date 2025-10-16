# calculator.py
# A simple calculator that adds two numbers provided by the user.
x = int(input("What's the value of x? "))
y = int(input("What's the value of y? "))


z = int(x) + int(y)

print("The result of x + y is", z)
print("The result of x + y is", x + y)

# Addition in a single line along with input.  Dont do this...it makes you think too much.
print("The result of x + y is", int(input("What's the value of x? ")) + int(input("What's the value of y? ")))


# Float operations
print("Let's do it with floats now.")
x = float(input("What's the value of x? "))
y = float(input("What's the value of y? "))

print("The result of x + y is", float(x) + float(y))

# print with comma separators
print("The result of x + y is", f"{x + y:,}")
print("The result of x + y is", f"{x + y:,.2f}")  # 2 decimal places
