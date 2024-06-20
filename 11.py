#Python program to find the greatest common divisor (GCD) of two input numbers

def hcf(a, b):
	if(b == 0):
		return a
	else:
		return hcf(b, a % b)

a = int(input())
b = int(input())

print("The gcd of numbers is : ", end="")
print(hcf(a, b))
