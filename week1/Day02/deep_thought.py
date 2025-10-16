# Implement a program that prompts the user for the answer to the Great Question of Life, 
# the Universe and Everything, outputting Yes if the user inputs 42 
# or (case-insensitively) forty-two or forty two. Otherwise output No.

def main():
    answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ")
    if answer == "42" or answer.lower() in ["forty-two", "forty two"]:
        print("Yes")
    else:
        print("No")

main()