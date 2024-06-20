#Python program to check if an input number is prime or not

from math import sqrt
n = int(input("Enter a Number:"))

flag = 0
if(n > 1):
    for i in range(2, int(sqrt(n)) + 1):
        if (n % i == 0):
            flag = 1
            break
    if (flag == 0):
        print("True")
    else:
        print("False")
else:
    print("False")
