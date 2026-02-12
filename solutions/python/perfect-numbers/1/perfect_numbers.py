def classify(number):
    if number < 1:
        raise ValueError('Classification is only possible for positive integers.')
        
    divisors = [i for i in range(1,number) if number % i == 0]
    total = sum(divisors)
    if total == number:
        return "perfect"
    elif total > number:
        return "abundant"
    else:
        return "deficient"   