#Python program to find the sum of digits of an input number

def getSum(n): 
    
    sum = 0
    for digit in str(n):  
      sum += int(digit)       
    return sum
   
n = int(input("Enter the digits"))
print(getSum(n))