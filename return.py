def main():
    x = int(input("Enter an integer: "))
    print(f"{x} squared is", square(x))
    print ("Same info printed using regular format")
    print(x, "squared is", square(x))

def square(n):
    return n * n
    # return n ** 2
    # return pow(n, 2)
    

main()
