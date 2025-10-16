def convert(number):
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

print(convert(28))   # "Plong"
print(convert(30))   # "PlingPlang"
print(convert(34))   # "34"
