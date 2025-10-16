# assigning grade to student score

score = int(input("Enter your score: "))

'''
if score >= 90 and score <= 100:
    print("Your grade is A")
elif score >= 80 and score < 90:
    print("Your grade is B")   
elif score >= 70 and score < 80:
    print("Your grade is C")
elif score >= 60 and score < 70:
    print("Your grade is D")
elif score >= 0 and score < 60:
    print("Your grade is F")
'''

# order reversal
'''
if 90 <= score <= 100:
    print("Your grade is A")
elif 80 <= score < 90:
    print("Your grade is B")   
elif 70 <= score < 80:
    print("Your grade is C")
elif 60 <= score < 70:
    print("Your grade is D")
elif 0 <= score < 60:
    print("Your grade is F")
'''

# optimized version of above

if 90 <= score:
    print("Your grade is A")
elif 80 <= score:
    print("Your grade is B")   
elif 70 <= score:
    print("Your grade is C")
elif 60 <= score:
    print("Your grade is D")
elif 0 <= score:
    print("Your grade is F")