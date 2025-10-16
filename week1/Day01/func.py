def main():
    name = input("Enter your name: ").title().strip() or "World"
    hello(name)

def hello(to="World"):
    print("Hello,",to)
    

main()