# use match operator to find out the name belongs to which Harry Potter house
# use if-elif-else statements to find out the name belongs to which Harry Potter house

def main():
    name = input("Enter your name: ").strip().lower()

# using match-case statement (Python 3.10+)
    match name:
        case "harry" | "ron" | "hermione":
            print("Gryffindor")
        case "draco" | "pansy" | "crabbe" | "goyle":
            print("Slytherin")
        case "luna" | "cho" | "cedric":
            print("Ravenclaw")
        case "neville" | "seamus" | "dean":
            print("Hufflepuff")
        case _:
            print("Muggle")

main()


# using traditional if-elif-else statements
'''
    if name in ["harry", "ron", "hermione"]:
        print("Gryffindor")
    elif name in ["draco", "pansy", "crabbe", "goyle"]:
        print("Slytherin")
    elif name in ["luna", "cho", "cedric"]:
        print("Ravenclaw")
    elif name in ["neville", "seamus", "dean"]:
        print("Hufflepuff")
    else:
        print("Muggle")
'''