# Ask user for their name
name = input("What's your name? ")

# Greet the user
print("hello, " + name)
print("hello,",name)

# Use format strings in print function
print(f"hello, {name}")


# Remote whitespaces from the string
name = name.strip()
print(f"hello, {name}")


# Capitalize the user name
name = name.capitalize()
print(f"hello, {name}")


# Capitalize the first letter of each word in the user name
name = name.title()
print(f"hello, {name}")

# Combine multiple string methods
name = name.strip().title()
print(f"hello, {name}")

# Combine multiple string methods to variable input
name = input("What's your name? ").strip().title()
print(f"hello, {name}")

# Combine multiple string methods in a single print statement
print(f"hello, {input('What\'s your name? ').strip().title()}")

# Split the user name into first and last name
first, last = name.split(" ")
print(f"hello, {first}")



