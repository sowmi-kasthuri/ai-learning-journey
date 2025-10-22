'''
implement a program that prompts the user for names, one per line, 
until the user inputs control-d. Assume that the user will input at least one name. 
Then bid adieu to those names, separating two names with one and, 
three names with two commas and one and, and 
𝑛 names with 𝑛 −1 commas and one and, as in the below:

Adieu, adieu, to Liesl
Adieu, adieu, to Liesl and Friedrich
Adieu, adieu, to Liesl, Friedrich, and Louisa
Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl
'''
# function to format names
def format_names(names):
    if len(names) == 1: # check for one name
        return names[0]
    elif len(names) == 2: # check for 2 names
        return f"{names[0]} and {names[1]}"
    else: # check for multiple names
        return f"{', '.join(names[:-1])} and {names[-1]}"

# define main to gather input and print output
def main():
    print("Enter names one per line (press Ctrl+D or Ctrl+Z + Enter to finish):")
    names = []
    try:
        while True:
            name = input()  # get input
            if name.strip():
                names.append(name.strip())
    except EOFError:
        pass
    print(f"Adieu, adieu to {format_names(names)}")

# call main    
if __name__ == "__main__":
    main()

