# nested loops

def main():
    print_square(3)

'''
def print_square(size):
    # for each row in the square
    for i in range(size):
        # for each brick in the row
        for j in range(size):
            # print brick
            print("#", end="")
        # next line    
        print()
'''

# above implementation but simpler
def print_square(size):
    # for each row in the square
    for i in range(size):
        print("#" * size)

main()
