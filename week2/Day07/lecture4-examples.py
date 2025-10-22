# Python Libraries
'''
import random
coin = random.choice(["Head","Tail"])
print(coin)
'''

'''
from random import choice
coin = choice(["Head","Tail"])
print(coin)
'''

'''
import random
number = random.randint(1,100)
print(number)
'''

'''
import random
cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)
'''

'''
import statistics
print(statistics.mean([100,90]))
'''

'''
import sys
if len(sys.argv) < 2:
    print("too few arguments")
elif len(sys.argv) > 2:
    print("too many arguments")
else:
    print("Hello, my name is ", sys.argv[1])
'''

'''
import sys
if len(sys.argv) < 2:
    sys.exit("too few arguments")
elif len(sys.argv) > 2:
    sys.exit("too many arguments")
#Print name tags
print("Hello, my name is ", sys.argv[1])
'''

'''
import sys
if len(sys.argv) < 2:
    sys.exit("too few arguments")

#Print name tags
for arg in sys.argv:
    print("Hello, my name is ", arg)    # this will print the file name as well as the other input name tags.
'''

import sys
if len(sys.argv) < 2:
    sys.exit("too few arguments")

#Print name tags
for arg in sys.argv[1:]: # this will omit the file name as well as the other input name tags.
    print("Hello, my name is ", arg)    