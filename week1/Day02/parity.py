# Even / odd check with parity operator

def main ():
    num = int(input("Enter a number: "))
    if is_Even(num):
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

def is_Even (n):
    return n % 2 == 0  

main()
