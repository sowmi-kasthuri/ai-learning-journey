# Implement a program that prompts the user to insert a coin, one at a time, 
# each time informing the user of the amount due. 
# Once the user has inputted at least 50 cents, 
# output how many cents in change the user is owed. 
# Assume that the user will only input integers, 
# and ignore any integer that isn’t an accepted denomination.

#define function to check coin inserted and accept valid coins
def accepted_coins(amount_due=50, accepted=[5,10,25]):

    # Initiate inserted coin variable
    total_inserted = 0

    # While loop to check the amount inserted
    while total_inserted < amount_due:
        try:
            coin = int(input(f"Amount Due : {amount_due - total_inserted} cents. Insert coin (5, 10, or 25): ").strip())
            
            # Check for coin denomination and accept only valid denominations
            if coin in accepted:
                total_inserted += coin
            else:
                print("Invalid coin. Only 5, 10, or 25 cents are accepted.")
        except ValueError:
            print("Invalid input. Please enter an integer value.")
    return(total_inserted)
        

# define function for main
def main():
    change = accepted_coins()
    print(f"Change Owed: {change} cents.")

# call main
main()