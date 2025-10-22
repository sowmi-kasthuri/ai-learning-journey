# implement a program that prompts the user for a str in English 
# and then outputs the “emojized” version of that str, 
# converting any codes (or aliases) therein to their corresponding emoji

# import package
import emoji

# def function to emojize input
def emojize_input(user_text):
    try:
        # Try emojizing the user input. language='alias' enables short names with _.
        return emoji.emojize(user_text,language="alias")
    except Exception as e:
        print("Failed to emojize input:", e)
        return user_text


# def main to gather input from user and print it
def main():
    while True:
        user_input = input("Enter the string for emoji (q to quit) : ")
        if user_input.lower() == 'q':
            print("Goodbye")
            break
        result = emojize_input(user_input)
        print("output: ", result)

# call main
if __name__ == "__main__":
    main()

