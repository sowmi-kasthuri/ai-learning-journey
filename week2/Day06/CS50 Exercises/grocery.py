'''
Suppose that you’re in the habit of making a list of items you need from the grocery store.
Implement a program that prompts the user for items, one per line, 
until the user inputs control-z (which is a common way of ending one’s input to a program). 
Then output the user’s grocery list in all uppercase, sorted alphabetically by item, 
prefixing each line with the number of times the user inputted that item. 
No need to pluralize the items. Treat the user’s input case-insensitively.
'''
# Initialize a dictionary
def main():
    grocery_count = {}
    print("Enter grocery items one line at a time.  Press Ctrl + Z once done")

# Get user input
    try:
        while True:
            item = input("Item: ").strip().lower()
            if item: # check for item availability in dict
                
                # if available increment the counter(Value)
                grocery_count[item] = grocery_count.get(item,0) + 1  # if not available add it to the dict
    except EOFError:
        pass 

# sort the items alphabetically and print the list of items with occurence count
    for item in sorted(grocery_count):
        print(f"{grocery_count[item]}  - {item.upper()}")
    


# call main
main()