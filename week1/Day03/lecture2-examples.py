# https://cs50.harvard.edu/python/weeks/2/
# Loops

'''
# while loops to print meow 3 times
i = 3
while i !=0:
    print ("meow")  
    i = i - 1
'''

'''
# while loops to print meow 3 times with reverse counter
i = 1
while i <=3:
    print ("meow")  
    i += 1  # i = i + 1
'''
'''
# for loops
for i in [0,1,2]:
    print ("meow")
'''

'''
# for loops using range
for i in range(3):  # you can also define as for _ in range(3) if i is not used anywhere
    print ("meow")
'''

'''
# while with break and continue
while True:
    n = int(input("Enter a positive number "))
    if n < 0:
        continue
    else:
        break
'''

'''
# while with break and continue
while True:
    n = int(input("Enter a positive number "))
    if n > 0:
        break
for _ in range(n):
    print("meow")
'''

# The logic above using functions

def main():
    number = get_number()
    meow (number)

def get_number():
    while True:
        n = int(input("Enter a positive number "))
        if n > 0:
            return n 

def  meow(n):
    for _ in range(n):
        print("meow")

main()
