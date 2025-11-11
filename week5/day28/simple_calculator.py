# Simple calculator program

while True:
    user_input = input("Enter calculation (e.g. 12 + 5) or 'exit':").strip()

    if user_input.lower() in ("exit", "quit"):
        break

    tokens = user_input.split()
    # print(f"DEBUG: tokens = {tokens}")

    try:
        if len(tokens) < 3:
            print("Enter values like: 12 + 5")
            continue

        num1 = tokens[0]
        operator = tokens[1]
        num2 = tokens[2]

        # print(f" the input values are {num1}, {operator}, {num2}")

        num1 = float(num1)
        num2 = float(num2)

        if operator not in ("+", "-", "*", "/"):
            print(f"Unsupported operator : {operator}")
            continue

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        else:
            if num2 == 0:
                print("Division by 0")
                continue
            else:
                result = num1 / num2
        
        print(f"Result of {user_input} = {result:.2f}")
    
    except ValueError as e:
        print(f"Invalid number {user_input}")

            


