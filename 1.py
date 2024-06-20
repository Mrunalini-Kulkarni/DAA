# Python program to check if the input number is even or odd

def check_positive_negative_zero(digit):
    if digit > 0 :
        return 'positive'
    elif digit < 0:
        return 'negative'
    else:
        return 'zero'
    
def check_even_odd(digit):
    if digit % 2 ==0:
        return 'even'
    else:
        return 'odd'
    
digit = int(input("Enter a Number:"))
print(check_even_odd(digit))
print(check_positive_negative_zero(digit))