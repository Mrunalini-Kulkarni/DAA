#Python program to find the least common multiple (LCM) of two input numbers

def gcd(num1,num2): 
	if num1 == 0: 
		return num2 
	return gcd(num2 % num1, num1) 

def lcm(num1,num2): 
	return (num1 // gcd(num1,num2))* num2 
 
num1 = int(input())
num2 = int(input())
print('LCM of', num1, 'and', num2, 'is', lcm(num1, num2)) 

