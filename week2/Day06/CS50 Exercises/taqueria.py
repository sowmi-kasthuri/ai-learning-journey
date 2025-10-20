'''
One of the most popular places to eat in Harvard Square is Felipe’s Taqueria, 
which offers a menu of entrees, per the dict below, 
wherein the value of each key is a price in dollars:

{
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
Implement a program that enables a user to place an order, 
prompting them for items, one per line, until the user inputs control-d 
(which is a common way of ending one’s input to a program). 
After each inputted item, display the total cost of all items inputted thus far, 
prefixed with a dollar sign ($) and formatted to two decimal places. 
Treat the user’s input case insensitively. 
Ignore any input that isn’t an item. 
Assume that every item on the menu will be titlecased.
'''

# Define menu
def get_menu():
    return {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
# User enters menu items
def main():
    menu = get_menu()
    total = 0.00
    print("Welcome ! Please place your order by entering one item per line")
    print ("Press ctrl + Z when done")

# If the item is in the menu dictionary, display item price and total cost
    try:
        while True:
            item = input("Item: ").strip().title() # Convert input to Title case to check with dict
            if item in menu:
                price = menu[item]
                total += price
                print(f"Added {item} : ${price:.2f} to order. Order Total : ${total:.2f}")
            
            # Ignore the item if its not in the menu
            else:
                print(f"Item {item} not in menu.  Ignored")
# end the task with a control + Z
    except EOFError:
        pass
    
    print(f"Thank you for your order.  Your final total is ${total:.2f}")

main()

